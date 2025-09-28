# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_location import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ApiKeyFilter:
    boto3_raw_data: "type_defs.ApiKeyFilterTypeDef" = dataclasses.field()

    KeyStatus = field("KeyStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiKeyFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiKeyFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiKeyRestrictionsOutput:
    boto3_raw_data: "type_defs.ApiKeyRestrictionsOutputTypeDef" = dataclasses.field()

    AllowActions = field("AllowActions")
    AllowResources = field("AllowResources")
    AllowReferers = field("AllowReferers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiKeyRestrictionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiKeyRestrictionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiKeyRestrictions:
    boto3_raw_data: "type_defs.ApiKeyRestrictionsTypeDef" = dataclasses.field()

    AllowActions = field("AllowActions")
    AllowResources = field("AllowResources")
    AllowReferers = field("AllowReferers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiKeyRestrictionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiKeyRestrictionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateTrackerConsumerRequest:
    boto3_raw_data: "type_defs.AssociateTrackerConsumerRequestTypeDef" = (
        dataclasses.field()
    )

    TrackerName = field("TrackerName")
    ConsumerArn = field("ConsumerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateTrackerConsumerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTrackerConsumerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchItemError:
    boto3_raw_data: "type_defs.BatchItemErrorTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchItemErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchItemErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDevicePositionHistoryRequest:
    boto3_raw_data: "type_defs.BatchDeleteDevicePositionHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    TrackerName = field("TrackerName")
    DeviceIds = field("DeviceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteDevicePositionHistoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDevicePositionHistoryRequestTypeDef"]
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
class BatchDeleteGeofenceRequest:
    boto3_raw_data: "type_defs.BatchDeleteGeofenceRequestTypeDef" = dataclasses.field()

    CollectionName = field("CollectionName")
    GeofenceIds = field("GeofenceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteGeofenceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteGeofenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDevicePositionRequest:
    boto3_raw_data: "type_defs.BatchGetDevicePositionRequestTypeDef" = (
        dataclasses.field()
    )

    TrackerName = field("TrackerName")
    DeviceIds = field("DeviceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetDevicePositionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDevicePositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutGeofenceSuccess:
    boto3_raw_data: "type_defs.BatchPutGeofenceSuccessTypeDef" = dataclasses.field()

    GeofenceId = field("GeofenceId")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutGeofenceSuccessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutGeofenceSuccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRouteCarModeOptions:
    boto3_raw_data: "type_defs.CalculateRouteCarModeOptionsTypeDef" = (
        dataclasses.field()
    )

    AvoidFerries = field("AvoidFerries")
    AvoidTolls = field("AvoidTolls")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateRouteCarModeOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRouteCarModeOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRouteMatrixSummary:
    boto3_raw_data: "type_defs.CalculateRouteMatrixSummaryTypeDef" = dataclasses.field()

    DataSource = field("DataSource")
    RouteCount = field("RouteCount")
    ErrorCount = field("ErrorCount")
    DistanceUnit = field("DistanceUnit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateRouteMatrixSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRouteMatrixSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRouteSummary:
    boto3_raw_data: "type_defs.CalculateRouteSummaryTypeDef" = dataclasses.field()

    RouteBBox = field("RouteBBox")
    DataSource = field("DataSource")
    Distance = field("Distance")
    DurationSeconds = field("DurationSeconds")
    DistanceUnit = field("DistanceUnit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateRouteSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRouteSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TruckDimensions:
    boto3_raw_data: "type_defs.TruckDimensionsTypeDef" = dataclasses.field()

    Length = field("Length")
    Height = field("Height")
    Width = field("Width")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TruckDimensionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TruckDimensionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TruckWeight:
    boto3_raw_data: "type_defs.TruckWeightTypeDef" = dataclasses.field()

    Total = field("Total")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TruckWeightTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TruckWeightTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CircleOutput:
    boto3_raw_data: "type_defs.CircleOutputTypeDef" = dataclasses.field()

    Center = field("Center")
    Radius = field("Radius")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CircleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CircleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Circle:
    boto3_raw_data: "type_defs.CircleTypeDef" = dataclasses.field()

    Center = field("Center")
    Radius = field("Radius")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CircleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CircleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGeofenceCollectionRequest:
    boto3_raw_data: "type_defs.CreateGeofenceCollectionRequestTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")
    PricingPlan = field("PricingPlan")
    PricingPlanDataSource = field("PricingPlanDataSource")
    Description = field("Description")
    Tags = field("Tags")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGeofenceCollectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGeofenceCollectionRequestTypeDef"]
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

    IntendedUse = field("IntendedUse")

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
class CreateRouteCalculatorRequest:
    boto3_raw_data: "type_defs.CreateRouteCalculatorRequestTypeDef" = (
        dataclasses.field()
    )

    CalculatorName = field("CalculatorName")
    DataSource = field("DataSource")
    PricingPlan = field("PricingPlan")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRouteCalculatorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteCalculatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrackerRequest:
    boto3_raw_data: "type_defs.CreateTrackerRequestTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")
    PricingPlan = field("PricingPlan")
    KmsKeyId = field("KmsKeyId")
    PricingPlanDataSource = field("PricingPlanDataSource")
    Description = field("Description")
    Tags = field("Tags")
    PositionFiltering = field("PositionFiltering")
    EventBridgeEnabled = field("EventBridgeEnabled")
    KmsKeyEnableGeospatialQueries = field("KmsKeyEnableGeospatialQueries")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrackerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrackerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGeofenceCollectionRequest:
    boto3_raw_data: "type_defs.DeleteGeofenceCollectionRequestTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteGeofenceCollectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGeofenceCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeyRequest:
    boto3_raw_data: "type_defs.DeleteKeyRequestTypeDef" = dataclasses.field()

    KeyName = field("KeyName")
    ForceDelete = field("ForceDelete")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteKeyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMapRequest:
    boto3_raw_data: "type_defs.DeleteMapRequestTypeDef" = dataclasses.field()

    MapName = field("MapName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteMapRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePlaceIndexRequest:
    boto3_raw_data: "type_defs.DeletePlaceIndexRequestTypeDef" = dataclasses.field()

    IndexName = field("IndexName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePlaceIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePlaceIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRouteCalculatorRequest:
    boto3_raw_data: "type_defs.DeleteRouteCalculatorRequestTypeDef" = (
        dataclasses.field()
    )

    CalculatorName = field("CalculatorName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRouteCalculatorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRouteCalculatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrackerRequest:
    boto3_raw_data: "type_defs.DeleteTrackerRequestTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTrackerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrackerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGeofenceCollectionRequest:
    boto3_raw_data: "type_defs.DescribeGeofenceCollectionRequestTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGeofenceCollectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGeofenceCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeyRequest:
    boto3_raw_data: "type_defs.DescribeKeyRequestTypeDef" = dataclasses.field()

    KeyName = field("KeyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMapRequest:
    boto3_raw_data: "type_defs.DescribeMapRequestTypeDef" = dataclasses.field()

    MapName = field("MapName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMapRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapConfigurationOutput:
    boto3_raw_data: "type_defs.MapConfigurationOutputTypeDef" = dataclasses.field()

    Style = field("Style")
    PoliticalView = field("PoliticalView")
    CustomLayers = field("CustomLayers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MapConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePlaceIndexRequest:
    boto3_raw_data: "type_defs.DescribePlaceIndexRequestTypeDef" = dataclasses.field()

    IndexName = field("IndexName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePlaceIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePlaceIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRouteCalculatorRequest:
    boto3_raw_data: "type_defs.DescribeRouteCalculatorRequestTypeDef" = (
        dataclasses.field()
    )

    CalculatorName = field("CalculatorName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRouteCalculatorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRouteCalculatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrackerRequest:
    boto3_raw_data: "type_defs.DescribeTrackerRequestTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTrackerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrackerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PositionalAccuracy:
    boto3_raw_data: "type_defs.PositionalAccuracyTypeDef" = dataclasses.field()

    Horizontal = field("Horizontal")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PositionalAccuracyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PositionalAccuracyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WiFiAccessPoint:
    boto3_raw_data: "type_defs.WiFiAccessPointTypeDef" = dataclasses.field()

    MacAddress = field("MacAddress")
    Rss = field("Rss")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WiFiAccessPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WiFiAccessPointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateTrackerConsumerRequest:
    boto3_raw_data: "type_defs.DisassociateTrackerConsumerRequestTypeDef" = (
        dataclasses.field()
    )

    TrackerName = field("TrackerName")
    ConsumerArn = field("ConsumerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateTrackerConsumerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateTrackerConsumerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForecastGeofenceEventsDeviceState:
    boto3_raw_data: "type_defs.ForecastGeofenceEventsDeviceStateTypeDef" = (
        dataclasses.field()
    )

    Position = field("Position")
    Speed = field("Speed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ForecastGeofenceEventsDeviceStateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForecastGeofenceEventsDeviceStateTypeDef"]
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
class ForecastedEvent:
    boto3_raw_data: "type_defs.ForecastedEventTypeDef" = dataclasses.field()

    EventId = field("EventId")
    GeofenceId = field("GeofenceId")
    IsDeviceInGeofence = field("IsDeviceInGeofence")
    NearestDistance = field("NearestDistance")
    EventType = field("EventType")
    ForecastedBreachTime = field("ForecastedBreachTime")
    GeofenceProperties = field("GeofenceProperties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ForecastedEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ForecastedEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDevicePositionRequest:
    boto3_raw_data: "type_defs.GetDevicePositionRequestTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")
    DeviceId = field("DeviceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDevicePositionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDevicePositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGeofenceRequest:
    boto3_raw_data: "type_defs.GetGeofenceRequestTypeDef" = dataclasses.field()

    CollectionName = field("CollectionName")
    GeofenceId = field("GeofenceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGeofenceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGeofenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMapGlyphsRequest:
    boto3_raw_data: "type_defs.GetMapGlyphsRequestTypeDef" = dataclasses.field()

    MapName = field("MapName")
    FontStack = field("FontStack")
    FontUnicodeRange = field("FontUnicodeRange")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMapGlyphsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMapGlyphsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMapSpritesRequest:
    boto3_raw_data: "type_defs.GetMapSpritesRequestTypeDef" = dataclasses.field()

    MapName = field("MapName")
    FileName = field("FileName")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMapSpritesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMapSpritesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMapStyleDescriptorRequest:
    boto3_raw_data: "type_defs.GetMapStyleDescriptorRequestTypeDef" = (
        dataclasses.field()
    )

    MapName = field("MapName")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMapStyleDescriptorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMapStyleDescriptorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMapTileRequest:
    boto3_raw_data: "type_defs.GetMapTileRequestTypeDef" = dataclasses.field()

    MapName = field("MapName")
    Z = field("Z")
    X = field("X")
    Y = field("Y")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMapTileRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMapTileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPlaceRequest:
    boto3_raw_data: "type_defs.GetPlaceRequestTypeDef" = dataclasses.field()

    IndexName = field("IndexName")
    PlaceId = field("PlaceId")
    Language = field("Language")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPlaceRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetPlaceRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LegGeometry:
    boto3_raw_data: "type_defs.LegGeometryTypeDef" = dataclasses.field()

    LineString = field("LineString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LegGeometryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LegGeometryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Step:
    boto3_raw_data: "type_defs.StepTypeDef" = dataclasses.field()

    StartPosition = field("StartPosition")
    EndPosition = field("EndPosition")
    Distance = field("Distance")
    DurationSeconds = field("DurationSeconds")
    GeometryOffset = field("GeometryOffset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrackingFilterGeometry:
    boto3_raw_data: "type_defs.TrackingFilterGeometryTypeDef" = dataclasses.field()

    Polygon = field("Polygon")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrackingFilterGeometryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrackingFilterGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeofenceCollectionsRequest:
    boto3_raw_data: "type_defs.ListGeofenceCollectionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGeofenceCollectionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeofenceCollectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeofenceCollectionsResponseEntry:
    boto3_raw_data: "type_defs.ListGeofenceCollectionsResponseEntryTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")
    Description = field("Description")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    PricingPlan = field("PricingPlan")
    PricingPlanDataSource = field("PricingPlanDataSource")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGeofenceCollectionsResponseEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeofenceCollectionsResponseEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeofencesRequest:
    boto3_raw_data: "type_defs.ListGeofencesRequestTypeDef" = dataclasses.field()

    CollectionName = field("CollectionName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGeofencesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeofencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMapsRequest:
    boto3_raw_data: "type_defs.ListMapsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMapsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListMapsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMapsResponseEntry:
    boto3_raw_data: "type_defs.ListMapsResponseEntryTypeDef" = dataclasses.field()

    MapName = field("MapName")
    Description = field("Description")
    DataSource = field("DataSource")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    PricingPlan = field("PricingPlan")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMapsResponseEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMapsResponseEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlaceIndexesRequest:
    boto3_raw_data: "type_defs.ListPlaceIndexesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPlaceIndexesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlaceIndexesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlaceIndexesResponseEntry:
    boto3_raw_data: "type_defs.ListPlaceIndexesResponseEntryTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")
    Description = field("Description")
    DataSource = field("DataSource")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    PricingPlan = field("PricingPlan")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPlaceIndexesResponseEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlaceIndexesResponseEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRouteCalculatorsRequest:
    boto3_raw_data: "type_defs.ListRouteCalculatorsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRouteCalculatorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRouteCalculatorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRouteCalculatorsResponseEntry:
    boto3_raw_data: "type_defs.ListRouteCalculatorsResponseEntryTypeDef" = (
        dataclasses.field()
    )

    CalculatorName = field("CalculatorName")
    Description = field("Description")
    DataSource = field("DataSource")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    PricingPlan = field("PricingPlan")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRouteCalculatorsResponseEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRouteCalculatorsResponseEntryTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class ListTrackerConsumersRequest:
    boto3_raw_data: "type_defs.ListTrackerConsumersRequestTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrackerConsumersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrackerConsumersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrackersRequest:
    boto3_raw_data: "type_defs.ListTrackersRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrackersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrackersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrackersResponseEntry:
    boto3_raw_data: "type_defs.ListTrackersResponseEntryTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")
    Description = field("Description")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    PricingPlan = field("PricingPlan")
    PricingPlanDataSource = field("PricingPlanDataSource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrackersResponseEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrackersResponseEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LteLocalId:
    boto3_raw_data: "type_defs.LteLocalIdTypeDef" = dataclasses.field()

    Earfcn = field("Earfcn")
    Pci = field("Pci")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LteLocalIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LteLocalIdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LteNetworkMeasurements:
    boto3_raw_data: "type_defs.LteNetworkMeasurementsTypeDef" = dataclasses.field()

    Earfcn = field("Earfcn")
    CellId = field("CellId")
    Pci = field("Pci")
    Rsrp = field("Rsrp")
    Rsrq = field("Rsrq")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LteNetworkMeasurementsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LteNetworkMeasurementsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapConfiguration:
    boto3_raw_data: "type_defs.MapConfigurationTypeDef" = dataclasses.field()

    Style = field("Style")
    PoliticalView = field("PoliticalView")
    CustomLayers = field("CustomLayers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MapConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapConfigurationUpdate:
    boto3_raw_data: "type_defs.MapConfigurationUpdateTypeDef" = dataclasses.field()

    PoliticalView = field("PoliticalView")
    CustomLayers = field("CustomLayers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MapConfigurationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlaceGeometry:
    boto3_raw_data: "type_defs.PlaceGeometryTypeDef" = dataclasses.field()

    Point = field("Point")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlaceGeometryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlaceGeometryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeZone:
    boto3_raw_data: "type_defs.TimeZoneTypeDef" = dataclasses.field()

    Name = field("Name")
    Offset = field("Offset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeZoneTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixEntryError:
    boto3_raw_data: "type_defs.RouteMatrixEntryErrorTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixEntryErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixEntryErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchForSuggestionsResult:
    boto3_raw_data: "type_defs.SearchForSuggestionsResultTypeDef" = dataclasses.field()

    Text = field("Text")
    PlaceId = field("PlaceId")
    Categories = field("Categories")
    SupplementalCategories = field("SupplementalCategories")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchForSuggestionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchForSuggestionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPlaceIndexForPositionRequest:
    boto3_raw_data: "type_defs.SearchPlaceIndexForPositionRequestTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")
    Position = field("Position")
    MaxResults = field("MaxResults")
    Language = field("Language")
    Key = field("Key")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchPlaceIndexForPositionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPlaceIndexForPositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPlaceIndexForPositionSummary:
    boto3_raw_data: "type_defs.SearchPlaceIndexForPositionSummaryTypeDef" = (
        dataclasses.field()
    )

    Position = field("Position")
    DataSource = field("DataSource")
    MaxResults = field("MaxResults")
    Language = field("Language")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchPlaceIndexForPositionSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPlaceIndexForPositionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPlaceIndexForSuggestionsRequest:
    boto3_raw_data: "type_defs.SearchPlaceIndexForSuggestionsRequestTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")
    Text = field("Text")
    BiasPosition = field("BiasPosition")
    FilterBBox = field("FilterBBox")
    FilterCountries = field("FilterCountries")
    MaxResults = field("MaxResults")
    Language = field("Language")
    FilterCategories = field("FilterCategories")
    Key = field("Key")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchPlaceIndexForSuggestionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPlaceIndexForSuggestionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPlaceIndexForSuggestionsSummary:
    boto3_raw_data: "type_defs.SearchPlaceIndexForSuggestionsSummaryTypeDef" = (
        dataclasses.field()
    )

    Text = field("Text")
    DataSource = field("DataSource")
    BiasPosition = field("BiasPosition")
    FilterBBox = field("FilterBBox")
    FilterCountries = field("FilterCountries")
    MaxResults = field("MaxResults")
    Language = field("Language")
    FilterCategories = field("FilterCategories")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchPlaceIndexForSuggestionsSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPlaceIndexForSuggestionsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPlaceIndexForTextRequest:
    boto3_raw_data: "type_defs.SearchPlaceIndexForTextRequestTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")
    Text = field("Text")
    BiasPosition = field("BiasPosition")
    FilterBBox = field("FilterBBox")
    FilterCountries = field("FilterCountries")
    MaxResults = field("MaxResults")
    Language = field("Language")
    FilterCategories = field("FilterCategories")
    Key = field("Key")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchPlaceIndexForTextRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPlaceIndexForTextRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPlaceIndexForTextSummary:
    boto3_raw_data: "type_defs.SearchPlaceIndexForTextSummaryTypeDef" = (
        dataclasses.field()
    )

    Text = field("Text")
    DataSource = field("DataSource")
    BiasPosition = field("BiasPosition")
    FilterBBox = field("FilterBBox")
    FilterCountries = field("FilterCountries")
    MaxResults = field("MaxResults")
    ResultBBox = field("ResultBBox")
    Language = field("Language")
    FilterCategories = field("FilterCategories")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchPlaceIndexForTextSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPlaceIndexForTextSummaryTypeDef"]
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

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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

    ResourceArn = field("ResourceArn")
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
class UpdateGeofenceCollectionRequest:
    boto3_raw_data: "type_defs.UpdateGeofenceCollectionRequestTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")
    PricingPlan = field("PricingPlan")
    PricingPlanDataSource = field("PricingPlanDataSource")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGeofenceCollectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGeofenceCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRouteCalculatorRequest:
    boto3_raw_data: "type_defs.UpdateRouteCalculatorRequestTypeDef" = (
        dataclasses.field()
    )

    CalculatorName = field("CalculatorName")
    PricingPlan = field("PricingPlan")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRouteCalculatorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteCalculatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrackerRequest:
    boto3_raw_data: "type_defs.UpdateTrackerRequestTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")
    PricingPlan = field("PricingPlan")
    PricingPlanDataSource = field("PricingPlanDataSource")
    Description = field("Description")
    PositionFiltering = field("PositionFiltering")
    EventBridgeEnabled = field("EventBridgeEnabled")
    KmsKeyEnableGeospatialQueries = field("KmsKeyEnableGeospatialQueries")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTrackerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrackerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysRequest:
    boto3_raw_data: "type_defs.ListKeysRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ApiKeyFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListKeysRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListKeysRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysResponseEntry:
    boto3_raw_data: "type_defs.ListKeysResponseEntryTypeDef" = dataclasses.field()

    KeyName = field("KeyName")
    ExpireTime = field("ExpireTime")

    @cached_property
    def Restrictions(self):  # pragma: no cover
        return ApiKeyRestrictionsOutput.make_one(self.boto3_raw_data["Restrictions"])

    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeysResponseEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeysResponseEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDevicePositionHistoryError:
    boto3_raw_data: "type_defs.BatchDeleteDevicePositionHistoryErrorTypeDef" = (
        dataclasses.field()
    )

    DeviceId = field("DeviceId")

    @cached_property
    def Error(self):  # pragma: no cover
        return BatchItemError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteDevicePositionHistoryErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDevicePositionHistoryErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteGeofenceError:
    boto3_raw_data: "type_defs.BatchDeleteGeofenceErrorTypeDef" = dataclasses.field()

    GeofenceId = field("GeofenceId")

    @cached_property
    def Error(self):  # pragma: no cover
        return BatchItemError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteGeofenceErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteGeofenceErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchEvaluateGeofencesError:
    boto3_raw_data: "type_defs.BatchEvaluateGeofencesErrorTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")
    SampleTime = field("SampleTime")

    @cached_property
    def Error(self):  # pragma: no cover
        return BatchItemError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchEvaluateGeofencesErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchEvaluateGeofencesErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDevicePositionError:
    boto3_raw_data: "type_defs.BatchGetDevicePositionErrorTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")

    @cached_property
    def Error(self):  # pragma: no cover
        return BatchItemError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetDevicePositionErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDevicePositionErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutGeofenceError:
    boto3_raw_data: "type_defs.BatchPutGeofenceErrorTypeDef" = dataclasses.field()

    GeofenceId = field("GeofenceId")

    @cached_property
    def Error(self):  # pragma: no cover
        return BatchItemError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutGeofenceErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutGeofenceErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateDevicePositionError:
    boto3_raw_data: "type_defs.BatchUpdateDevicePositionErrorTypeDef" = (
        dataclasses.field()
    )

    DeviceId = field("DeviceId")
    SampleTime = field("SampleTime")

    @cached_property
    def Error(self):  # pragma: no cover
        return BatchItemError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchUpdateDevicePositionErrorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateDevicePositionErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGeofenceCollectionResponse:
    boto3_raw_data: "type_defs.CreateGeofenceCollectionResponseTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")
    CollectionArn = field("CollectionArn")
    CreateTime = field("CreateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGeofenceCollectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGeofenceCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyResponse:
    boto3_raw_data: "type_defs.CreateKeyResponseTypeDef" = dataclasses.field()

    Key = field("Key")
    KeyArn = field("KeyArn")
    KeyName = field("KeyName")
    CreateTime = field("CreateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateKeyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMapResponse:
    boto3_raw_data: "type_defs.CreateMapResponseTypeDef" = dataclasses.field()

    MapName = field("MapName")
    MapArn = field("MapArn")
    CreateTime = field("CreateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateMapResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePlaceIndexResponse:
    boto3_raw_data: "type_defs.CreatePlaceIndexResponseTypeDef" = dataclasses.field()

    IndexName = field("IndexName")
    IndexArn = field("IndexArn")
    CreateTime = field("CreateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePlaceIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePlaceIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRouteCalculatorResponse:
    boto3_raw_data: "type_defs.CreateRouteCalculatorResponseTypeDef" = (
        dataclasses.field()
    )

    CalculatorName = field("CalculatorName")
    CalculatorArn = field("CalculatorArn")
    CreateTime = field("CreateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRouteCalculatorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteCalculatorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrackerResponse:
    boto3_raw_data: "type_defs.CreateTrackerResponseTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")
    TrackerArn = field("TrackerArn")
    CreateTime = field("CreateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrackerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrackerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGeofenceCollectionResponse:
    boto3_raw_data: "type_defs.DescribeGeofenceCollectionResponseTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")
    CollectionArn = field("CollectionArn")
    Description = field("Description")
    PricingPlan = field("PricingPlan")
    PricingPlanDataSource = field("PricingPlanDataSource")
    KmsKeyId = field("KmsKeyId")
    Tags = field("Tags")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    GeofenceCount = field("GeofenceCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGeofenceCollectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGeofenceCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeyResponse:
    boto3_raw_data: "type_defs.DescribeKeyResponseTypeDef" = dataclasses.field()

    Key = field("Key")
    KeyArn = field("KeyArn")
    KeyName = field("KeyName")

    @cached_property
    def Restrictions(self):  # pragma: no cover
        return ApiKeyRestrictionsOutput.make_one(self.boto3_raw_data["Restrictions"])

    CreateTime = field("CreateTime")
    ExpireTime = field("ExpireTime")
    UpdateTime = field("UpdateTime")
    Description = field("Description")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRouteCalculatorResponse:
    boto3_raw_data: "type_defs.DescribeRouteCalculatorResponseTypeDef" = (
        dataclasses.field()
    )

    CalculatorName = field("CalculatorName")
    CalculatorArn = field("CalculatorArn")
    PricingPlan = field("PricingPlan")
    Description = field("Description")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    DataSource = field("DataSource")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRouteCalculatorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRouteCalculatorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrackerResponse:
    boto3_raw_data: "type_defs.DescribeTrackerResponseTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")
    TrackerArn = field("TrackerArn")
    Description = field("Description")
    PricingPlan = field("PricingPlan")
    PricingPlanDataSource = field("PricingPlanDataSource")
    Tags = field("Tags")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    KmsKeyId = field("KmsKeyId")
    PositionFiltering = field("PositionFiltering")
    EventBridgeEnabled = field("EventBridgeEnabled")
    KmsKeyEnableGeospatialQueries = field("KmsKeyEnableGeospatialQueries")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTrackerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrackerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMapGlyphsResponse:
    boto3_raw_data: "type_defs.GetMapGlyphsResponseTypeDef" = dataclasses.field()

    Blob = field("Blob")
    ContentType = field("ContentType")
    CacheControl = field("CacheControl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMapGlyphsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMapGlyphsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMapSpritesResponse:
    boto3_raw_data: "type_defs.GetMapSpritesResponseTypeDef" = dataclasses.field()

    Blob = field("Blob")
    ContentType = field("ContentType")
    CacheControl = field("CacheControl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMapSpritesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMapSpritesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMapStyleDescriptorResponse:
    boto3_raw_data: "type_defs.GetMapStyleDescriptorResponseTypeDef" = (
        dataclasses.field()
    )

    Blob = field("Blob")
    ContentType = field("ContentType")
    CacheControl = field("CacheControl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMapStyleDescriptorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMapStyleDescriptorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMapTileResponse:
    boto3_raw_data: "type_defs.GetMapTileResponseTypeDef" = dataclasses.field()

    Blob = field("Blob")
    ContentType = field("ContentType")
    CacheControl = field("CacheControl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMapTileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMapTileResponseTypeDef"]
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

    Tags = field("Tags")

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
class ListTrackerConsumersResponse:
    boto3_raw_data: "type_defs.ListTrackerConsumersResponseTypeDef" = (
        dataclasses.field()
    )

    ConsumerArns = field("ConsumerArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrackerConsumersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrackerConsumersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutGeofenceResponse:
    boto3_raw_data: "type_defs.PutGeofenceResponseTypeDef" = dataclasses.field()

    GeofenceId = field("GeofenceId")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutGeofenceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutGeofenceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGeofenceCollectionResponse:
    boto3_raw_data: "type_defs.UpdateGeofenceCollectionResponseTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")
    CollectionArn = field("CollectionArn")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGeofenceCollectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGeofenceCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKeyResponse:
    boto3_raw_data: "type_defs.UpdateKeyResponseTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")
    KeyName = field("KeyName")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateKeyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMapResponse:
    boto3_raw_data: "type_defs.UpdateMapResponseTypeDef" = dataclasses.field()

    MapName = field("MapName")
    MapArn = field("MapArn")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateMapResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePlaceIndexResponse:
    boto3_raw_data: "type_defs.UpdatePlaceIndexResponseTypeDef" = dataclasses.field()

    IndexName = field("IndexName")
    IndexArn = field("IndexArn")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePlaceIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePlaceIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRouteCalculatorResponse:
    boto3_raw_data: "type_defs.UpdateRouteCalculatorResponseTypeDef" = (
        dataclasses.field()
    )

    CalculatorName = field("CalculatorName")
    CalculatorArn = field("CalculatorArn")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRouteCalculatorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteCalculatorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrackerResponse:
    boto3_raw_data: "type_defs.UpdateTrackerResponseTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")
    TrackerArn = field("TrackerArn")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTrackerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrackerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDevicePositionHistoryRequest:
    boto3_raw_data: "type_defs.GetDevicePositionHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    TrackerName = field("TrackerName")
    DeviceId = field("DeviceId")
    NextToken = field("NextToken")
    StartTimeInclusive = field("StartTimeInclusive")
    EndTimeExclusive = field("EndTimeExclusive")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDevicePositionHistoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDevicePositionHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRouteTruckModeOptions:
    boto3_raw_data: "type_defs.CalculateRouteTruckModeOptionsTypeDef" = (
        dataclasses.field()
    )

    AvoidFerries = field("AvoidFerries")
    AvoidTolls = field("AvoidTolls")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return TruckDimensions.make_one(self.boto3_raw_data["Dimensions"])

    @cached_property
    def Weight(self):  # pragma: no cover
        return TruckWeight.make_one(self.boto3_raw_data["Weight"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CalculateRouteTruckModeOptionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRouteTruckModeOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeofenceGeometryOutput:
    boto3_raw_data: "type_defs.GeofenceGeometryOutputTypeDef" = dataclasses.field()

    Polygon = field("Polygon")

    @cached_property
    def Circle(self):  # pragma: no cover
        return CircleOutput.make_one(self.boto3_raw_data["Circle"])

    Geobuf = field("Geobuf")
    MultiPolygon = field("MultiPolygon")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeofenceGeometryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeofenceGeometryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePlaceIndexRequest:
    boto3_raw_data: "type_defs.CreatePlaceIndexRequestTypeDef" = dataclasses.field()

    IndexName = field("IndexName")
    DataSource = field("DataSource")
    PricingPlan = field("PricingPlan")
    Description = field("Description")

    @cached_property
    def DataSourceConfiguration(self):  # pragma: no cover
        return DataSourceConfiguration.make_one(
            self.boto3_raw_data["DataSourceConfiguration"]
        )

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePlaceIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePlaceIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePlaceIndexResponse:
    boto3_raw_data: "type_defs.DescribePlaceIndexResponseTypeDef" = dataclasses.field()

    IndexName = field("IndexName")
    IndexArn = field("IndexArn")
    PricingPlan = field("PricingPlan")
    Description = field("Description")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    DataSource = field("DataSource")

    @cached_property
    def DataSourceConfiguration(self):  # pragma: no cover
        return DataSourceConfiguration.make_one(
            self.boto3_raw_data["DataSourceConfiguration"]
        )

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePlaceIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePlaceIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePlaceIndexRequest:
    boto3_raw_data: "type_defs.UpdatePlaceIndexRequestTypeDef" = dataclasses.field()

    IndexName = field("IndexName")
    PricingPlan = field("PricingPlan")
    Description = field("Description")

    @cached_property
    def DataSourceConfiguration(self):  # pragma: no cover
        return DataSourceConfiguration.make_one(
            self.boto3_raw_data["DataSourceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePlaceIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePlaceIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMapResponse:
    boto3_raw_data: "type_defs.DescribeMapResponseTypeDef" = dataclasses.field()

    MapName = field("MapName")
    MapArn = field("MapArn")
    PricingPlan = field("PricingPlan")
    DataSource = field("DataSource")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return MapConfigurationOutput.make_one(self.boto3_raw_data["Configuration"])

    Description = field("Description")
    Tags = field("Tags")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMapResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DevicePosition:
    boto3_raw_data: "type_defs.DevicePositionTypeDef" = dataclasses.field()

    SampleTime = field("SampleTime")
    ReceivedTime = field("ReceivedTime")
    Position = field("Position")
    DeviceId = field("DeviceId")

    @cached_property
    def Accuracy(self):  # pragma: no cover
        return PositionalAccuracy.make_one(self.boto3_raw_data["Accuracy"])

    PositionProperties = field("PositionProperties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DevicePositionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DevicePositionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DevicePositionUpdate:
    boto3_raw_data: "type_defs.DevicePositionUpdateTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")
    SampleTime = field("SampleTime")
    Position = field("Position")

    @cached_property
    def Accuracy(self):  # pragma: no cover
        return PositionalAccuracy.make_one(self.boto3_raw_data["Accuracy"])

    PositionProperties = field("PositionProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DevicePositionUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DevicePositionUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDevicePositionResponse:
    boto3_raw_data: "type_defs.GetDevicePositionResponseTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")
    SampleTime = field("SampleTime")
    ReceivedTime = field("ReceivedTime")
    Position = field("Position")

    @cached_property
    def Accuracy(self):  # pragma: no cover
        return PositionalAccuracy.make_one(self.boto3_raw_data["Accuracy"])

    PositionProperties = field("PositionProperties")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDevicePositionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDevicePositionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferredState:
    boto3_raw_data: "type_defs.InferredStateTypeDef" = dataclasses.field()

    ProxyDetected = field("ProxyDetected")
    Position = field("Position")

    @cached_property
    def Accuracy(self):  # pragma: no cover
        return PositionalAccuracy.make_one(self.boto3_raw_data["Accuracy"])

    DeviationDistance = field("DeviationDistance")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InferredStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InferredStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicePositionsResponseEntry:
    boto3_raw_data: "type_defs.ListDevicePositionsResponseEntryTypeDef" = (
        dataclasses.field()
    )

    DeviceId = field("DeviceId")
    SampleTime = field("SampleTime")
    Position = field("Position")

    @cached_property
    def Accuracy(self):  # pragma: no cover
        return PositionalAccuracy.make_one(self.boto3_raw_data["Accuracy"])

    PositionProperties = field("PositionProperties")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDevicePositionsResponseEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicePositionsResponseEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForecastGeofenceEventsRequest:
    boto3_raw_data: "type_defs.ForecastGeofenceEventsRequestTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")

    @cached_property
    def DeviceState(self):  # pragma: no cover
        return ForecastGeofenceEventsDeviceState.make_one(
            self.boto3_raw_data["DeviceState"]
        )

    TimeHorizonMinutes = field("TimeHorizonMinutes")
    DistanceUnit = field("DistanceUnit")
    SpeedUnit = field("SpeedUnit")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ForecastGeofenceEventsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForecastGeofenceEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForecastGeofenceEventsRequestPaginate:
    boto3_raw_data: "type_defs.ForecastGeofenceEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")

    @cached_property
    def DeviceState(self):  # pragma: no cover
        return ForecastGeofenceEventsDeviceState.make_one(
            self.boto3_raw_data["DeviceState"]
        )

    TimeHorizonMinutes = field("TimeHorizonMinutes")
    DistanceUnit = field("DistanceUnit")
    SpeedUnit = field("SpeedUnit")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ForecastGeofenceEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForecastGeofenceEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDevicePositionHistoryRequestPaginate:
    boto3_raw_data: "type_defs.GetDevicePositionHistoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TrackerName = field("TrackerName")
    DeviceId = field("DeviceId")
    StartTimeInclusive = field("StartTimeInclusive")
    EndTimeExclusive = field("EndTimeExclusive")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDevicePositionHistoryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDevicePositionHistoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeofenceCollectionsRequestPaginate:
    boto3_raw_data: "type_defs.ListGeofenceCollectionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGeofenceCollectionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeofenceCollectionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeofencesRequestPaginate:
    boto3_raw_data: "type_defs.ListGeofencesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGeofencesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeofencesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysRequestPaginate:
    boto3_raw_data: "type_defs.ListKeysRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def Filter(self):  # pragma: no cover
        return ApiKeyFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeysRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMapsRequestPaginate:
    boto3_raw_data: "type_defs.ListMapsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMapsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMapsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlaceIndexesRequestPaginate:
    boto3_raw_data: "type_defs.ListPlaceIndexesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPlaceIndexesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlaceIndexesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRouteCalculatorsRequestPaginate:
    boto3_raw_data: "type_defs.ListRouteCalculatorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRouteCalculatorsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRouteCalculatorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrackerConsumersRequestPaginate:
    boto3_raw_data: "type_defs.ListTrackerConsumersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TrackerName = field("TrackerName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrackerConsumersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrackerConsumersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrackersRequestPaginate:
    boto3_raw_data: "type_defs.ListTrackersRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrackersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrackersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForecastGeofenceEventsResponse:
    boto3_raw_data: "type_defs.ForecastGeofenceEventsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ForecastedEvents(self):  # pragma: no cover
        return ForecastedEvent.make_many(self.boto3_raw_data["ForecastedEvents"])

    DistanceUnit = field("DistanceUnit")
    SpeedUnit = field("SpeedUnit")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ForecastGeofenceEventsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForecastGeofenceEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Leg:
    boto3_raw_data: "type_defs.LegTypeDef" = dataclasses.field()

    StartPosition = field("StartPosition")
    EndPosition = field("EndPosition")
    Distance = field("Distance")
    DurationSeconds = field("DurationSeconds")

    @cached_property
    def Steps(self):  # pragma: no cover
        return Step.make_many(self.boto3_raw_data["Steps"])

    @cached_property
    def Geometry(self):  # pragma: no cover
        return LegGeometry.make_one(self.boto3_raw_data["Geometry"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LegTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LegTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicePositionsRequestPaginate:
    boto3_raw_data: "type_defs.ListDevicePositionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TrackerName = field("TrackerName")

    @cached_property
    def FilterGeometry(self):  # pragma: no cover
        return TrackingFilterGeometry.make_one(self.boto3_raw_data["FilterGeometry"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDevicePositionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicePositionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicePositionsRequest:
    boto3_raw_data: "type_defs.ListDevicePositionsRequestTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def FilterGeometry(self):  # pragma: no cover
        return TrackingFilterGeometry.make_one(self.boto3_raw_data["FilterGeometry"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDevicePositionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicePositionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeofenceCollectionsResponse:
    boto3_raw_data: "type_defs.ListGeofenceCollectionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Entries(self):  # pragma: no cover
        return ListGeofenceCollectionsResponseEntry.make_many(
            self.boto3_raw_data["Entries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGeofenceCollectionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeofenceCollectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMapsResponse:
    boto3_raw_data: "type_defs.ListMapsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entries(self):  # pragma: no cover
        return ListMapsResponseEntry.make_many(self.boto3_raw_data["Entries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMapsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMapsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlaceIndexesResponse:
    boto3_raw_data: "type_defs.ListPlaceIndexesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entries(self):  # pragma: no cover
        return ListPlaceIndexesResponseEntry.make_many(self.boto3_raw_data["Entries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPlaceIndexesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlaceIndexesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRouteCalculatorsResponse:
    boto3_raw_data: "type_defs.ListRouteCalculatorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Entries(self):  # pragma: no cover
        return ListRouteCalculatorsResponseEntry.make_many(
            self.boto3_raw_data["Entries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRouteCalculatorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRouteCalculatorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrackersResponse:
    boto3_raw_data: "type_defs.ListTrackersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entries(self):  # pragma: no cover
        return ListTrackersResponseEntry.make_many(self.boto3_raw_data["Entries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrackersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrackersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LteCellDetails:
    boto3_raw_data: "type_defs.LteCellDetailsTypeDef" = dataclasses.field()

    CellId = field("CellId")
    Mcc = field("Mcc")
    Mnc = field("Mnc")

    @cached_property
    def LocalId(self):  # pragma: no cover
        return LteLocalId.make_one(self.boto3_raw_data["LocalId"])

    @cached_property
    def NetworkMeasurements(self):  # pragma: no cover
        return LteNetworkMeasurements.make_many(
            self.boto3_raw_data["NetworkMeasurements"]
        )

    TimingAdvance = field("TimingAdvance")
    NrCapable = field("NrCapable")
    Rsrp = field("Rsrp")
    Rsrq = field("Rsrq")
    Tac = field("Tac")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LteCellDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LteCellDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMapRequest:
    boto3_raw_data: "type_defs.UpdateMapRequestTypeDef" = dataclasses.field()

    MapName = field("MapName")
    PricingPlan = field("PricingPlan")
    Description = field("Description")

    @cached_property
    def ConfigurationUpdate(self):  # pragma: no cover
        return MapConfigurationUpdate.make_one(
            self.boto3_raw_data["ConfigurationUpdate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateMapRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Place:
    boto3_raw_data: "type_defs.PlaceTypeDef" = dataclasses.field()

    @cached_property
    def Geometry(self):  # pragma: no cover
        return PlaceGeometry.make_one(self.boto3_raw_data["Geometry"])

    Label = field("Label")
    AddressNumber = field("AddressNumber")
    Street = field("Street")
    Neighborhood = field("Neighborhood")
    Municipality = field("Municipality")
    SubRegion = field("SubRegion")
    Region = field("Region")
    Country = field("Country")
    PostalCode = field("PostalCode")
    Interpolated = field("Interpolated")

    @cached_property
    def TimeZone(self):  # pragma: no cover
        return TimeZone.make_one(self.boto3_raw_data["TimeZone"])

    UnitType = field("UnitType")
    UnitNumber = field("UnitNumber")
    Categories = field("Categories")
    SupplementalCategories = field("SupplementalCategories")
    SubMunicipality = field("SubMunicipality")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlaceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixEntry:
    boto3_raw_data: "type_defs.RouteMatrixEntryTypeDef" = dataclasses.field()

    Distance = field("Distance")
    DurationSeconds = field("DurationSeconds")

    @cached_property
    def Error(self):  # pragma: no cover
        return RouteMatrixEntryError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPlaceIndexForSuggestionsResponse:
    boto3_raw_data: "type_defs.SearchPlaceIndexForSuggestionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summary(self):  # pragma: no cover
        return SearchPlaceIndexForSuggestionsSummary.make_one(
            self.boto3_raw_data["Summary"]
        )

    @cached_property
    def Results(self):  # pragma: no cover
        return SearchForSuggestionsResult.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchPlaceIndexForSuggestionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPlaceIndexForSuggestionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysResponse:
    boto3_raw_data: "type_defs.ListKeysResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entries(self):  # pragma: no cover
        return ListKeysResponseEntry.make_many(self.boto3_raw_data["Entries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListKeysResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyRequest:
    boto3_raw_data: "type_defs.CreateKeyRequestTypeDef" = dataclasses.field()

    KeyName = field("KeyName")
    Restrictions = field("Restrictions")
    Description = field("Description")
    ExpireTime = field("ExpireTime")
    NoExpiry = field("NoExpiry")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateKeyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKeyRequest:
    boto3_raw_data: "type_defs.UpdateKeyRequestTypeDef" = dataclasses.field()

    KeyName = field("KeyName")
    Description = field("Description")
    ExpireTime = field("ExpireTime")
    NoExpiry = field("NoExpiry")
    ForceUpdate = field("ForceUpdate")
    Restrictions = field("Restrictions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateKeyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDevicePositionHistoryResponse:
    boto3_raw_data: "type_defs.BatchDeleteDevicePositionHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchDeleteDevicePositionHistoryError.make_many(
            self.boto3_raw_data["Errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteDevicePositionHistoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDevicePositionHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteGeofenceResponse:
    boto3_raw_data: "type_defs.BatchDeleteGeofenceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchDeleteGeofenceError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteGeofenceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteGeofenceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchEvaluateGeofencesResponse:
    boto3_raw_data: "type_defs.BatchEvaluateGeofencesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchEvaluateGeofencesError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchEvaluateGeofencesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchEvaluateGeofencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutGeofenceResponse:
    boto3_raw_data: "type_defs.BatchPutGeofenceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Successes(self):  # pragma: no cover
        return BatchPutGeofenceSuccess.make_many(self.boto3_raw_data["Successes"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchPutGeofenceError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutGeofenceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutGeofenceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateDevicePositionResponse:
    boto3_raw_data: "type_defs.BatchUpdateDevicePositionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchUpdateDevicePositionError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateDevicePositionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateDevicePositionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRouteMatrixRequest:
    boto3_raw_data: "type_defs.CalculateRouteMatrixRequestTypeDef" = dataclasses.field()

    CalculatorName = field("CalculatorName")
    DeparturePositions = field("DeparturePositions")
    DestinationPositions = field("DestinationPositions")
    TravelMode = field("TravelMode")
    DepartureTime = field("DepartureTime")
    DepartNow = field("DepartNow")
    DistanceUnit = field("DistanceUnit")

    @cached_property
    def CarModeOptions(self):  # pragma: no cover
        return CalculateRouteCarModeOptions.make_one(
            self.boto3_raw_data["CarModeOptions"]
        )

    @cached_property
    def TruckModeOptions(self):  # pragma: no cover
        return CalculateRouteTruckModeOptions.make_one(
            self.boto3_raw_data["TruckModeOptions"]
        )

    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateRouteMatrixRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRouteMatrixRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRouteRequest:
    boto3_raw_data: "type_defs.CalculateRouteRequestTypeDef" = dataclasses.field()

    CalculatorName = field("CalculatorName")
    DeparturePosition = field("DeparturePosition")
    DestinationPosition = field("DestinationPosition")
    WaypointPositions = field("WaypointPositions")
    TravelMode = field("TravelMode")
    DepartureTime = field("DepartureTime")
    DepartNow = field("DepartNow")
    DistanceUnit = field("DistanceUnit")
    IncludeLegGeometry = field("IncludeLegGeometry")

    @cached_property
    def CarModeOptions(self):  # pragma: no cover
        return CalculateRouteCarModeOptions.make_one(
            self.boto3_raw_data["CarModeOptions"]
        )

    @cached_property
    def TruckModeOptions(self):  # pragma: no cover
        return CalculateRouteTruckModeOptions.make_one(
            self.boto3_raw_data["TruckModeOptions"]
        )

    ArrivalTime = field("ArrivalTime")
    OptimizeFor = field("OptimizeFor")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateRouteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRouteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGeofenceResponse:
    boto3_raw_data: "type_defs.GetGeofenceResponseTypeDef" = dataclasses.field()

    GeofenceId = field("GeofenceId")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return GeofenceGeometryOutput.make_one(self.boto3_raw_data["Geometry"])

    Status = field("Status")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    GeofenceProperties = field("GeofenceProperties")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGeofenceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGeofenceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeofenceResponseEntry:
    boto3_raw_data: "type_defs.ListGeofenceResponseEntryTypeDef" = dataclasses.field()

    GeofenceId = field("GeofenceId")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return GeofenceGeometryOutput.make_one(self.boto3_raw_data["Geometry"])

    Status = field("Status")
    CreateTime = field("CreateTime")
    UpdateTime = field("UpdateTime")
    GeofenceProperties = field("GeofenceProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGeofenceResponseEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeofenceResponseEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeofenceGeometry:
    boto3_raw_data: "type_defs.GeofenceGeometryTypeDef" = dataclasses.field()

    Polygon = field("Polygon")
    Circle = field("Circle")
    Geobuf = field("Geobuf")
    MultiPolygon = field("MultiPolygon")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeofenceGeometryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeofenceGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDevicePositionResponse:
    boto3_raw_data: "type_defs.BatchGetDevicePositionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchGetDevicePositionError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def DevicePositions(self):  # pragma: no cover
        return DevicePosition.make_many(self.boto3_raw_data["DevicePositions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetDevicePositionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDevicePositionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDevicePositionHistoryResponse:
    boto3_raw_data: "type_defs.GetDevicePositionHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DevicePositions(self):  # pragma: no cover
        return DevicePosition.make_many(self.boto3_raw_data["DevicePositions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDevicePositionHistoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDevicePositionHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchEvaluateGeofencesRequest:
    boto3_raw_data: "type_defs.BatchEvaluateGeofencesRequestTypeDef" = (
        dataclasses.field()
    )

    CollectionName = field("CollectionName")

    @cached_property
    def DevicePositionUpdates(self):  # pragma: no cover
        return DevicePositionUpdate.make_many(
            self.boto3_raw_data["DevicePositionUpdates"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchEvaluateGeofencesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchEvaluateGeofencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateDevicePositionRequest:
    boto3_raw_data: "type_defs.BatchUpdateDevicePositionRequestTypeDef" = (
        dataclasses.field()
    )

    TrackerName = field("TrackerName")

    @cached_property
    def Updates(self):  # pragma: no cover
        return DevicePositionUpdate.make_many(self.boto3_raw_data["Updates"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchUpdateDevicePositionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateDevicePositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyDevicePositionResponse:
    boto3_raw_data: "type_defs.VerifyDevicePositionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InferredState(self):  # pragma: no cover
        return InferredState.make_one(self.boto3_raw_data["InferredState"])

    DeviceId = field("DeviceId")
    SampleTime = field("SampleTime")
    ReceivedTime = field("ReceivedTime")
    DistanceUnit = field("DistanceUnit")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyDevicePositionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDevicePositionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicePositionsResponse:
    boto3_raw_data: "type_defs.ListDevicePositionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entries(self):  # pragma: no cover
        return ListDevicePositionsResponseEntry.make_many(
            self.boto3_raw_data["Entries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDevicePositionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicePositionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRouteResponse:
    boto3_raw_data: "type_defs.CalculateRouteResponseTypeDef" = dataclasses.field()

    @cached_property
    def Legs(self):  # pragma: no cover
        return Leg.make_many(self.boto3_raw_data["Legs"])

    @cached_property
    def Summary(self):  # pragma: no cover
        return CalculateRouteSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateRouteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRouteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CellSignals:
    boto3_raw_data: "type_defs.CellSignalsTypeDef" = dataclasses.field()

    @cached_property
    def LteCellDetails(self):  # pragma: no cover
        return LteCellDetails.make_many(self.boto3_raw_data["LteCellDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CellSignalsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CellSignalsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMapRequest:
    boto3_raw_data: "type_defs.CreateMapRequestTypeDef" = dataclasses.field()

    MapName = field("MapName")
    Configuration = field("Configuration")
    PricingPlan = field("PricingPlan")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateMapRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPlaceResponse:
    boto3_raw_data: "type_defs.GetPlaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return Place.make_one(self.boto3_raw_data["Place"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPlaceResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPlaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchForPositionResult:
    boto3_raw_data: "type_defs.SearchForPositionResultTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return Place.make_one(self.boto3_raw_data["Place"])

    Distance = field("Distance")
    PlaceId = field("PlaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchForPositionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchForPositionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchForTextResult:
    boto3_raw_data: "type_defs.SearchForTextResultTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return Place.make_one(self.boto3_raw_data["Place"])

    Distance = field("Distance")
    Relevance = field("Relevance")
    PlaceId = field("PlaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchForTextResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchForTextResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRouteMatrixResponse:
    boto3_raw_data: "type_defs.CalculateRouteMatrixResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RouteMatrix(self):  # pragma: no cover
        return RouteMatrixEntry.make_many(self.boto3_raw_data["RouteMatrix"])

    SnappedDeparturePositions = field("SnappedDeparturePositions")
    SnappedDestinationPositions = field("SnappedDestinationPositions")

    @cached_property
    def Summary(self):  # pragma: no cover
        return CalculateRouteMatrixSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateRouteMatrixResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRouteMatrixResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeofencesResponse:
    boto3_raw_data: "type_defs.ListGeofencesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entries(self):  # pragma: no cover
        return ListGeofenceResponseEntry.make_many(self.boto3_raw_data["Entries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGeofencesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeofencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceState:
    boto3_raw_data: "type_defs.DeviceStateTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")
    SampleTime = field("SampleTime")
    Position = field("Position")

    @cached_property
    def Accuracy(self):  # pragma: no cover
        return PositionalAccuracy.make_one(self.boto3_raw_data["Accuracy"])

    Ipv4Address = field("Ipv4Address")

    @cached_property
    def WiFiAccessPoints(self):  # pragma: no cover
        return WiFiAccessPoint.make_many(self.boto3_raw_data["WiFiAccessPoints"])

    @cached_property
    def CellSignals(self):  # pragma: no cover
        return CellSignals.make_one(self.boto3_raw_data["CellSignals"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPlaceIndexForPositionResponse:
    boto3_raw_data: "type_defs.SearchPlaceIndexForPositionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summary(self):  # pragma: no cover
        return SearchPlaceIndexForPositionSummary.make_one(
            self.boto3_raw_data["Summary"]
        )

    @cached_property
    def Results(self):  # pragma: no cover
        return SearchForPositionResult.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchPlaceIndexForPositionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPlaceIndexForPositionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPlaceIndexForTextResponse:
    boto3_raw_data: "type_defs.SearchPlaceIndexForTextResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summary(self):  # pragma: no cover
        return SearchPlaceIndexForTextSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def Results(self):  # pragma: no cover
        return SearchForTextResult.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchPlaceIndexForTextResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPlaceIndexForTextResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutGeofenceRequestEntry:
    boto3_raw_data: "type_defs.BatchPutGeofenceRequestEntryTypeDef" = (
        dataclasses.field()
    )

    GeofenceId = field("GeofenceId")
    Geometry = field("Geometry")
    GeofenceProperties = field("GeofenceProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutGeofenceRequestEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutGeofenceRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutGeofenceRequest:
    boto3_raw_data: "type_defs.PutGeofenceRequestTypeDef" = dataclasses.field()

    CollectionName = field("CollectionName")
    GeofenceId = field("GeofenceId")
    Geometry = field("Geometry")
    GeofenceProperties = field("GeofenceProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutGeofenceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutGeofenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyDevicePositionRequest:
    boto3_raw_data: "type_defs.VerifyDevicePositionRequestTypeDef" = dataclasses.field()

    TrackerName = field("TrackerName")

    @cached_property
    def DeviceState(self):  # pragma: no cover
        return DeviceState.make_one(self.boto3_raw_data["DeviceState"])

    DistanceUnit = field("DistanceUnit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyDevicePositionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDevicePositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutGeofenceRequest:
    boto3_raw_data: "type_defs.BatchPutGeofenceRequestTypeDef" = dataclasses.field()

    CollectionName = field("CollectionName")

    @cached_property
    def Entries(self):  # pragma: no cover
        return BatchPutGeofenceRequestEntry.make_many(self.boto3_raw_data["Entries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutGeofenceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutGeofenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
