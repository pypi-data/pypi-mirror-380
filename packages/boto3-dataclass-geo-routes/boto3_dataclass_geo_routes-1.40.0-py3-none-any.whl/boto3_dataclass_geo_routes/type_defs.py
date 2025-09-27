# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_geo_routes import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class IsolineAllowOptions:
    boto3_raw_data: "type_defs.IsolineAllowOptionsTypeDef" = dataclasses.field()

    Hot = field("Hot")
    Hov = field("Hov")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineAllowOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineAllowOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineGranularityOptions:
    boto3_raw_data: "type_defs.IsolineGranularityOptionsTypeDef" = dataclasses.field()

    MaxPoints = field("MaxPoints")
    MaxResolution = field("MaxResolution")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineGranularityOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineGranularityOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineThresholds:
    boto3_raw_data: "type_defs.IsolineThresholdsTypeDef" = dataclasses.field()

    Distance = field("Distance")
    Time = field("Time")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IsolineThresholdsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineThresholdsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineTrafficOptions:
    boto3_raw_data: "type_defs.IsolineTrafficOptionsTypeDef" = dataclasses.field()

    FlowEventThresholdOverride = field("FlowEventThresholdOverride")
    Usage = field("Usage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineTrafficOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineTrafficOptionsTypeDef"]
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
class RouteMatrixAllowOptions:
    boto3_raw_data: "type_defs.RouteMatrixAllowOptionsTypeDef" = dataclasses.field()

    Hot = field("Hot")
    Hov = field("Hov")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixAllowOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixAllowOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixExclusionOptions:
    boto3_raw_data: "type_defs.RouteMatrixExclusionOptionsTypeDef" = dataclasses.field()

    Countries = field("Countries")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixExclusionOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixExclusionOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixTrafficOptions:
    boto3_raw_data: "type_defs.RouteMatrixTrafficOptionsTypeDef" = dataclasses.field()

    FlowEventThresholdOverride = field("FlowEventThresholdOverride")
    Usage = field("Usage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixTrafficOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixTrafficOptionsTypeDef"]
        ],
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
    Duration = field("Duration")
    Error = field("Error")

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
class RouteAllowOptions:
    boto3_raw_data: "type_defs.RouteAllowOptionsTypeDef" = dataclasses.field()

    Hot = field("Hot")
    Hov = field("Hov")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteAllowOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteAllowOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteExclusionOptions:
    boto3_raw_data: "type_defs.RouteExclusionOptionsTypeDef" = dataclasses.field()

    Countries = field("Countries")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteExclusionOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteExclusionOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTrafficOptions:
    boto3_raw_data: "type_defs.RouteTrafficOptionsTypeDef" = dataclasses.field()

    FlowEventThresholdOverride = field("FlowEventThresholdOverride")
    Usage = field("Usage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteTrafficOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTrafficOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteResponseNotice:
    boto3_raw_data: "type_defs.RouteResponseNoticeTypeDef" = dataclasses.field()

    Code = field("Code")
    Impact = field("Impact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteResponseNoticeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteResponseNoticeTypeDef"]
        ],
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
class Corridor:
    boto3_raw_data: "type_defs.CorridorTypeDef" = dataclasses.field()

    LineString = field("LineString")
    Radius = field("Radius")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CorridorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CorridorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolylineCorridor:
    boto3_raw_data: "type_defs.PolylineCorridorTypeDef" = dataclasses.field()

    Polyline = field("Polyline")
    Radius = field("Radius")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolylineCorridorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolylineCorridorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineAvoidanceZoneCategory:
    boto3_raw_data: "type_defs.IsolineAvoidanceZoneCategoryTypeDef" = (
        dataclasses.field()
    )

    Category = field("Category")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineAvoidanceZoneCategoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineAvoidanceZoneCategoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineVehicleLicensePlate:
    boto3_raw_data: "type_defs.IsolineVehicleLicensePlateTypeDef" = dataclasses.field()

    LastCharacter = field("LastCharacter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineVehicleLicensePlateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineVehicleLicensePlateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineConnectionGeometry:
    boto3_raw_data: "type_defs.IsolineConnectionGeometryTypeDef" = dataclasses.field()

    LineString = field("LineString")
    Polyline = field("Polyline")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineConnectionGeometryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineConnectionGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineMatchingOptions:
    boto3_raw_data: "type_defs.IsolineMatchingOptionsTypeDef" = dataclasses.field()

    NameHint = field("NameHint")
    OnRoadThreshold = field("OnRoadThreshold")
    Radius = field("Radius")
    Strategy = field("Strategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineMatchingOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineMatchingOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineSideOfStreetOptions:
    boto3_raw_data: "type_defs.IsolineSideOfStreetOptionsTypeDef" = dataclasses.field()

    Position = field("Position")
    UseWith = field("UseWith")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineSideOfStreetOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineSideOfStreetOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineShapeGeometry:
    boto3_raw_data: "type_defs.IsolineShapeGeometryTypeDef" = dataclasses.field()

    Polygon = field("Polygon")
    PolylinePolygon = field("PolylinePolygon")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineShapeGeometryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineShapeGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineTrailerOptions:
    boto3_raw_data: "type_defs.IsolineTrailerOptionsTypeDef" = dataclasses.field()

    AxleCount = field("AxleCount")
    TrailerCount = field("TrailerCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineTrailerOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineTrailerOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WeightPerAxleGroup:
    boto3_raw_data: "type_defs.WeightPerAxleGroupTypeDef" = dataclasses.field()

    Single = field("Single")
    Tandem = field("Tandem")
    Triple = field("Triple")
    Quad = field("Quad")
    Quint = field("Quint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WeightPerAxleGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WeightPerAxleGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalizedString:
    boto3_raw_data: "type_defs.LocalizedStringTypeDef" = dataclasses.field()

    Value = field("Value")
    Language = field("Language")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocalizedStringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocalizedStringTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationExclusionOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationExclusionOptionsTypeDef" = (
        dataclasses.field()
    )

    Countries = field("Countries")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationExclusionOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationExclusionOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationOriginOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationOriginOptionsTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationOriginOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationOriginOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationTrafficOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationTrafficOptionsTypeDef" = (
        dataclasses.field()
    )

    Usage = field("Usage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationTrafficOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationTrafficOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationConnection:
    boto3_raw_data: "type_defs.WaypointOptimizationConnectionTypeDef" = (
        dataclasses.field()
    )

    Distance = field("Distance")
    From = field("From")
    RestDuration = field("RestDuration")
    To = field("To")
    TravelDuration = field("TravelDuration")
    WaitDuration = field("WaitDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WaypointOptimizationConnectionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationOptimizedWaypoint:
    boto3_raw_data: "type_defs.WaypointOptimizationOptimizedWaypointTypeDef" = (
        dataclasses.field()
    )

    DepartureTime = field("DepartureTime")
    Id = field("Id")
    Position = field("Position")
    ArrivalTime = field("ArrivalTime")
    ClusterIndex = field("ClusterIndex")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationOptimizedWaypointTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationOptimizedWaypointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationTimeBreakdown:
    boto3_raw_data: "type_defs.WaypointOptimizationTimeBreakdownTypeDef" = (
        dataclasses.field()
    )

    RestDuration = field("RestDuration")
    ServiceDuration = field("ServiceDuration")
    TravelDuration = field("TravelDuration")
    WaitDuration = field("WaitDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationTimeBreakdownTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationTimeBreakdownTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoadSnapNotice:
    boto3_raw_data: "type_defs.RoadSnapNoticeTypeDef" = dataclasses.field()

    Code = field("Code")
    Title = field("Title")
    TracePointIndexes = field("TracePointIndexes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoadSnapNoticeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoadSnapNoticeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoadSnapSnappedGeometry:
    boto3_raw_data: "type_defs.RoadSnapSnappedGeometryTypeDef" = dataclasses.field()

    LineString = field("LineString")
    Polyline = field("Polyline")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoadSnapSnappedGeometryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoadSnapSnappedGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoadSnapSnappedTracePoint:
    boto3_raw_data: "type_defs.RoadSnapSnappedTracePointTypeDef" = dataclasses.field()

    Confidence = field("Confidence")
    OriginalPosition = field("OriginalPosition")
    SnappedPosition = field("SnappedPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoadSnapSnappedTracePointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoadSnapSnappedTracePointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoadSnapTracePoint:
    boto3_raw_data: "type_defs.RoadSnapTracePointTypeDef" = dataclasses.field()

    Position = field("Position")
    Heading = field("Heading")
    Speed = field("Speed")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoadSnapTracePointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoadSnapTracePointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoadSnapTrailerOptions:
    boto3_raw_data: "type_defs.RoadSnapTrailerOptionsTypeDef" = dataclasses.field()

    TrailerCount = field("TrailerCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoadSnapTrailerOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoadSnapTrailerOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteAvoidanceZoneCategory:
    boto3_raw_data: "type_defs.RouteAvoidanceZoneCategoryTypeDef" = dataclasses.field()

    Category = field("Category")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteAvoidanceZoneCategoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteAvoidanceZoneCategoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleLicensePlate:
    boto3_raw_data: "type_defs.RouteVehicleLicensePlateTypeDef" = dataclasses.field()

    LastCharacter = field("LastCharacter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleLicensePlateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleLicensePlateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatchingOptions:
    boto3_raw_data: "type_defs.RouteMatchingOptionsTypeDef" = dataclasses.field()

    NameHint = field("NameHint")
    OnRoadThreshold = field("OnRoadThreshold")
    Radius = field("Radius")
    Strategy = field("Strategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatchingOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatchingOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteSideOfStreetOptions:
    boto3_raw_data: "type_defs.RouteSideOfStreetOptionsTypeDef" = dataclasses.field()

    Position = field("Position")
    UseWith = field("UseWith")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteSideOfStreetOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteSideOfStreetOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteDriverScheduleInterval:
    boto3_raw_data: "type_defs.RouteDriverScheduleIntervalTypeDef" = dataclasses.field()

    DriveDuration = field("DriveDuration")
    RestDuration = field("RestDuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteDriverScheduleIntervalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteDriverScheduleIntervalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteEmissionType:
    boto3_raw_data: "type_defs.RouteEmissionTypeTypeDef" = dataclasses.field()

    Type = field("Type")
    Co2EmissionClass = field("Co2EmissionClass")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteEmissionTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteEmissionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryAfterTravelStep:
    boto3_raw_data: "type_defs.RouteFerryAfterTravelStepTypeDef" = dataclasses.field()

    Duration = field("Duration")
    Type = field("Type")
    Instruction = field("Instruction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteFerryAfterTravelStepTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerryAfterTravelStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryPlace:
    boto3_raw_data: "type_defs.RouteFerryPlaceTypeDef" = dataclasses.field()

    Position = field("Position")
    Name = field("Name")
    OriginalPosition = field("OriginalPosition")
    WaypointIndex = field("WaypointIndex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteFerryPlaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteFerryPlaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryBeforeTravelStep:
    boto3_raw_data: "type_defs.RouteFerryBeforeTravelStepTypeDef" = dataclasses.field()

    Duration = field("Duration")
    Type = field("Type")
    Instruction = field("Instruction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteFerryBeforeTravelStepTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerryBeforeTravelStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryNotice:
    boto3_raw_data: "type_defs.RouteFerryNoticeTypeDef" = dataclasses.field()

    Code = field("Code")
    Impact = field("Impact")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteFerryNoticeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerryNoticeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryTravelStep:
    boto3_raw_data: "type_defs.RouteFerryTravelStepTypeDef" = dataclasses.field()

    Duration = field("Duration")
    Type = field("Type")
    Distance = field("Distance")
    GeometryOffset = field("GeometryOffset")
    Instruction = field("Instruction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteFerryTravelStepTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerryTravelStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryOverviewSummary:
    boto3_raw_data: "type_defs.RouteFerryOverviewSummaryTypeDef" = dataclasses.field()

    Distance = field("Distance")
    Duration = field("Duration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteFerryOverviewSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerryOverviewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryTravelOnlySummary:
    boto3_raw_data: "type_defs.RouteFerryTravelOnlySummaryTypeDef" = dataclasses.field()

    Duration = field("Duration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteFerryTravelOnlySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerryTravelOnlySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteLegGeometry:
    boto3_raw_data: "type_defs.RouteLegGeometryTypeDef" = dataclasses.field()

    LineString = field("LineString")
    Polyline = field("Polyline")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteLegGeometryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteLegGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteNumber:
    boto3_raw_data: "type_defs.RouteNumberTypeDef" = dataclasses.field()

    Value = field("Value")
    Direction = field("Direction")
    Language = field("Language")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteNumberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteNumberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixAutoCircle:
    boto3_raw_data: "type_defs.RouteMatrixAutoCircleTypeDef" = dataclasses.field()

    Margin = field("Margin")
    MaxRadius = field("MaxRadius")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixAutoCircleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixAutoCircleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixAvoidanceAreaGeometry:
    boto3_raw_data: "type_defs.RouteMatrixAvoidanceAreaGeometryTypeDef" = (
        dataclasses.field()
    )

    BoundingBox = field("BoundingBox")
    Polygon = field("Polygon")
    PolylinePolygon = field("PolylinePolygon")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteMatrixAvoidanceAreaGeometryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixAvoidanceAreaGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixAvoidanceZoneCategory:
    boto3_raw_data: "type_defs.RouteMatrixAvoidanceZoneCategoryTypeDef" = (
        dataclasses.field()
    )

    Category = field("Category")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteMatrixAvoidanceZoneCategoryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixAvoidanceZoneCategoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixVehicleLicensePlate:
    boto3_raw_data: "type_defs.RouteMatrixVehicleLicensePlateTypeDef" = (
        dataclasses.field()
    )

    LastCharacter = field("LastCharacter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteMatrixVehicleLicensePlateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixVehicleLicensePlateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixMatchingOptions:
    boto3_raw_data: "type_defs.RouteMatrixMatchingOptionsTypeDef" = dataclasses.field()

    NameHint = field("NameHint")
    OnRoadThreshold = field("OnRoadThreshold")
    Radius = field("Radius")
    Strategy = field("Strategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixMatchingOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixMatchingOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixSideOfStreetOptions:
    boto3_raw_data: "type_defs.RouteMatrixSideOfStreetOptionsTypeDef" = (
        dataclasses.field()
    )

    Position = field("Position")
    UseWith = field("UseWith")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteMatrixSideOfStreetOptionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixSideOfStreetOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixTrailerOptions:
    boto3_raw_data: "type_defs.RouteMatrixTrailerOptionsTypeDef" = dataclasses.field()

    TrailerCount = field("TrailerCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixTrailerOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixTrailerOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteNoticeDetailRange:
    boto3_raw_data: "type_defs.RouteNoticeDetailRangeTypeDef" = dataclasses.field()

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteNoticeDetailRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteNoticeDetailRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePassThroughPlace:
    boto3_raw_data: "type_defs.RoutePassThroughPlaceTypeDef" = dataclasses.field()

    Position = field("Position")
    OriginalPosition = field("OriginalPosition")
    WaypointIndex = field("WaypointIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePassThroughPlaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePassThroughPlaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianPlace:
    boto3_raw_data: "type_defs.RoutePedestrianPlaceTypeDef" = dataclasses.field()

    Position = field("Position")
    Name = field("Name")
    OriginalPosition = field("OriginalPosition")
    SideOfStreet = field("SideOfStreet")
    WaypointIndex = field("WaypointIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePedestrianPlaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianPlaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianNotice:
    boto3_raw_data: "type_defs.RoutePedestrianNoticeTypeDef" = dataclasses.field()

    Code = field("Code")
    Impact = field("Impact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePedestrianNoticeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianNoticeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianOptions:
    boto3_raw_data: "type_defs.RoutePedestrianOptionsTypeDef" = dataclasses.field()

    Speed = field("Speed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePedestrianOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianOverviewSummary:
    boto3_raw_data: "type_defs.RoutePedestrianOverviewSummaryTypeDef" = (
        dataclasses.field()
    )

    Distance = field("Distance")
    Duration = field("Duration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RoutePedestrianOverviewSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianOverviewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteSpanDynamicSpeedDetails:
    boto3_raw_data: "type_defs.RouteSpanDynamicSpeedDetailsTypeDef" = (
        dataclasses.field()
    )

    BestCaseSpeed = field("BestCaseSpeed")
    TurnDuration = field("TurnDuration")
    TypicalSpeed = field("TypicalSpeed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteSpanDynamicSpeedDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteSpanDynamicSpeedDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteSpanSpeedLimitDetails:
    boto3_raw_data: "type_defs.RouteSpanSpeedLimitDetailsTypeDef" = dataclasses.field()

    MaxSpeed = field("MaxSpeed")
    Unlimited = field("Unlimited")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteSpanSpeedLimitDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteSpanSpeedLimitDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianTravelOnlySummary:
    boto3_raw_data: "type_defs.RoutePedestrianTravelOnlySummaryTypeDef" = (
        dataclasses.field()
    )

    Duration = field("Duration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RoutePedestrianTravelOnlySummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianTravelOnlySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollPassValidityPeriod:
    boto3_raw_data: "type_defs.RouteTollPassValidityPeriodTypeDef" = dataclasses.field()

    Period = field("Period")
    PeriodCount = field("PeriodCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteTollPassValidityPeriodTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTollPassValidityPeriodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollPaymentSite:
    boto3_raw_data: "type_defs.RouteTollPaymentSiteTypeDef" = dataclasses.field()

    Position = field("Position")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteTollPaymentSiteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTollPaymentSiteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollPriceValueRange:
    boto3_raw_data: "type_defs.RouteTollPriceValueRangeTypeDef" = dataclasses.field()

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteTollPriceValueRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTollPriceValueRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTransponder:
    boto3_raw_data: "type_defs.RouteTransponderTypeDef" = dataclasses.field()

    SystemName = field("SystemName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTransponderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTransponderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollSystem:
    boto3_raw_data: "type_defs.RouteTollSystemTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTollSystemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTollSystemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTrailerOptions:
    boto3_raw_data: "type_defs.RouteTrailerOptionsTypeDef" = dataclasses.field()

    AxleCount = field("AxleCount")
    TrailerCount = field("TrailerCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteTrailerOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTrailerOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehiclePlace:
    boto3_raw_data: "type_defs.RouteVehiclePlaceTypeDef" = dataclasses.field()

    Position = field("Position")
    Name = field("Name")
    OriginalPosition = field("OriginalPosition")
    SideOfStreet = field("SideOfStreet")
    WaypointIndex = field("WaypointIndex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteVehiclePlaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehiclePlaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleIncident:
    boto3_raw_data: "type_defs.RouteVehicleIncidentTypeDef" = dataclasses.field()

    Description = field("Description")
    EndTime = field("EndTime")
    Severity = field("Severity")
    StartTime = field("StartTime")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleIncidentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleIncidentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteZone:
    boto3_raw_data: "type_defs.RouteZoneTypeDef" = dataclasses.field()

    Category = field("Category")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteZoneTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleOverviewSummary:
    boto3_raw_data: "type_defs.RouteVehicleOverviewSummaryTypeDef" = dataclasses.field()

    Distance = field("Distance")
    Duration = field("Duration")
    BestCaseDuration = field("BestCaseDuration")
    TypicalDuration = field("TypicalDuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleOverviewSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleOverviewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleTravelOnlySummary:
    boto3_raw_data: "type_defs.RouteVehicleTravelOnlySummaryTypeDef" = (
        dataclasses.field()
    )

    Duration = field("Duration")
    BestCaseDuration = field("BestCaseDuration")
    TypicalDuration = field("TypicalDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteVehicleTravelOnlySummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleTravelOnlySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteWeightConstraint:
    boto3_raw_data: "type_defs.RouteWeightConstraintTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteWeightConstraintTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteWeightConstraintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationAccessHoursEntry:
    boto3_raw_data: "type_defs.WaypointOptimizationAccessHoursEntryTypeDef" = (
        dataclasses.field()
    )

    DayOfWeek = field("DayOfWeek")
    TimeOfDay = field("TimeOfDay")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationAccessHoursEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationAccessHoursEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationAvoidanceAreaGeometry:
    boto3_raw_data: "type_defs.WaypointOptimizationAvoidanceAreaGeometryTypeDef" = (
        dataclasses.field()
    )

    BoundingBox = field("BoundingBox")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationAvoidanceAreaGeometryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationAvoidanceAreaGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationDrivingDistanceOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationDrivingDistanceOptionsTypeDef" = (
        dataclasses.field()
    )

    DrivingDistance = field("DrivingDistance")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationDrivingDistanceOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationDrivingDistanceOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationSideOfStreetOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationSideOfStreetOptionsTypeDef" = (
        dataclasses.field()
    )

    Position = field("Position")
    UseWith = field("UseWith")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationSideOfStreetOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationSideOfStreetOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationRestProfile:
    boto3_raw_data: "type_defs.WaypointOptimizationRestProfileTypeDef" = (
        dataclasses.field()
    )

    Profile = field("Profile")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WaypointOptimizationRestProfileTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationRestProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationFailedConstraint:
    boto3_raw_data: "type_defs.WaypointOptimizationFailedConstraintTypeDef" = (
        dataclasses.field()
    )

    Constraint = field("Constraint")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationFailedConstraintTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationFailedConstraintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationPedestrianOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationPedestrianOptionsTypeDef" = (
        dataclasses.field()
    )

    Speed = field("Speed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationPedestrianOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationPedestrianOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationRestCycleDurations:
    boto3_raw_data: "type_defs.WaypointOptimizationRestCycleDurationsTypeDef" = (
        dataclasses.field()
    )

    RestDuration = field("RestDuration")
    WorkDuration = field("WorkDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationRestCycleDurationsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationRestCycleDurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationTrailerOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationTrailerOptionsTypeDef" = (
        dataclasses.field()
    )

    TrailerCount = field("TrailerCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationTrailerOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationTrailerOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineAvoidanceAreaGeometry:
    boto3_raw_data: "type_defs.IsolineAvoidanceAreaGeometryTypeDef" = (
        dataclasses.field()
    )

    BoundingBox = field("BoundingBox")

    @cached_property
    def Corridor(self):  # pragma: no cover
        return Corridor.make_one(self.boto3_raw_data["Corridor"])

    Polygon = field("Polygon")

    @cached_property
    def PolylineCorridor(self):  # pragma: no cover
        return PolylineCorridor.make_one(self.boto3_raw_data["PolylineCorridor"])

    PolylinePolygon = field("PolylinePolygon")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineAvoidanceAreaGeometryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineAvoidanceAreaGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteAvoidanceAreaGeometry:
    boto3_raw_data: "type_defs.RouteAvoidanceAreaGeometryTypeDef" = dataclasses.field()

    @cached_property
    def Corridor(self):  # pragma: no cover
        return Corridor.make_one(self.boto3_raw_data["Corridor"])

    BoundingBox = field("BoundingBox")
    Polygon = field("Polygon")

    @cached_property
    def PolylineCorridor(self):  # pragma: no cover
        return PolylineCorridor.make_one(self.boto3_raw_data["PolylineCorridor"])

    PolylinePolygon = field("PolylinePolygon")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteAvoidanceAreaGeometryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteAvoidanceAreaGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineCarOptions:
    boto3_raw_data: "type_defs.IsolineCarOptionsTypeDef" = dataclasses.field()

    EngineType = field("EngineType")

    @cached_property
    def LicensePlate(self):  # pragma: no cover
        return IsolineVehicleLicensePlate.make_one(self.boto3_raw_data["LicensePlate"])

    MaxSpeed = field("MaxSpeed")
    Occupancy = field("Occupancy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IsolineCarOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineCarOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineScooterOptions:
    boto3_raw_data: "type_defs.IsolineScooterOptionsTypeDef" = dataclasses.field()

    EngineType = field("EngineType")

    @cached_property
    def LicensePlate(self):  # pragma: no cover
        return IsolineVehicleLicensePlate.make_one(self.boto3_raw_data["LicensePlate"])

    MaxSpeed = field("MaxSpeed")
    Occupancy = field("Occupancy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineScooterOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineScooterOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineConnection:
    boto3_raw_data: "type_defs.IsolineConnectionTypeDef" = dataclasses.field()

    FromPolygonIndex = field("FromPolygonIndex")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return IsolineConnectionGeometry.make_one(self.boto3_raw_data["Geometry"])

    ToPolygonIndex = field("ToPolygonIndex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IsolineConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineDestinationOptions:
    boto3_raw_data: "type_defs.IsolineDestinationOptionsTypeDef" = dataclasses.field()

    AvoidActionsForDistance = field("AvoidActionsForDistance")
    Heading = field("Heading")

    @cached_property
    def Matching(self):  # pragma: no cover
        return IsolineMatchingOptions.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def SideOfStreet(self):  # pragma: no cover
        return IsolineSideOfStreetOptions.make_one(self.boto3_raw_data["SideOfStreet"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineDestinationOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineDestinationOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineOriginOptions:
    boto3_raw_data: "type_defs.IsolineOriginOptionsTypeDef" = dataclasses.field()

    AvoidActionsForDistance = field("AvoidActionsForDistance")
    Heading = field("Heading")

    @cached_property
    def Matching(self):  # pragma: no cover
        return IsolineMatchingOptions.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def SideOfStreet(self):  # pragma: no cover
        return IsolineSideOfStreetOptions.make_one(self.boto3_raw_data["SideOfStreet"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineOriginOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineOriginOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineTruckOptions:
    boto3_raw_data: "type_defs.IsolineTruckOptionsTypeDef" = dataclasses.field()

    AxleCount = field("AxleCount")
    EngineType = field("EngineType")
    GrossWeight = field("GrossWeight")
    HazardousCargos = field("HazardousCargos")
    Height = field("Height")
    HeightAboveFirstAxle = field("HeightAboveFirstAxle")
    KpraLength = field("KpraLength")
    Length = field("Length")

    @cached_property
    def LicensePlate(self):  # pragma: no cover
        return IsolineVehicleLicensePlate.make_one(self.boto3_raw_data["LicensePlate"])

    MaxSpeed = field("MaxSpeed")
    Occupancy = field("Occupancy")
    PayloadCapacity = field("PayloadCapacity")
    TireCount = field("TireCount")

    @cached_property
    def Trailer(self):  # pragma: no cover
        return IsolineTrailerOptions.make_one(self.boto3_raw_data["Trailer"])

    TruckType = field("TruckType")
    TunnelRestrictionCode = field("TunnelRestrictionCode")
    WeightPerAxle = field("WeightPerAxle")

    @cached_property
    def WeightPerAxleGroup(self):  # pragma: no cover
        return WeightPerAxleGroup.make_one(self.boto3_raw_data["WeightPerAxleGroup"])

    Width = field("Width")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineTruckOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineTruckOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteContinueHighwayStepDetails:
    boto3_raw_data: "type_defs.RouteContinueHighwayStepDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    SteeringDirection = field("SteeringDirection")
    TurnAngle = field("TurnAngle")
    TurnIntensity = field("TurnIntensity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteContinueHighwayStepDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteContinueHighwayStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteContinueStepDetails:
    boto3_raw_data: "type_defs.RouteContinueStepDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteContinueStepDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteContinueStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteEnterHighwayStepDetails:
    boto3_raw_data: "type_defs.RouteEnterHighwayStepDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    SteeringDirection = field("SteeringDirection")
    TurnAngle = field("TurnAngle")
    TurnIntensity = field("TurnIntensity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteEnterHighwayStepDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteEnterHighwayStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteExitStepDetails:
    boto3_raw_data: "type_defs.RouteExitStepDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    RelativeExit = field("RelativeExit")
    SteeringDirection = field("SteeringDirection")
    TurnAngle = field("TurnAngle")
    TurnIntensity = field("TurnIntensity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteExitStepDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteExitStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerrySpan:
    boto3_raw_data: "type_defs.RouteFerrySpanTypeDef" = dataclasses.field()

    Country = field("Country")
    Distance = field("Distance")
    Duration = field("Duration")
    GeometryOffset = field("GeometryOffset")

    @cached_property
    def Names(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Names"])

    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteFerrySpanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteFerrySpanTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteKeepStepDetails:
    boto3_raw_data: "type_defs.RouteKeepStepDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    SteeringDirection = field("SteeringDirection")
    TurnAngle = field("TurnAngle")
    TurnIntensity = field("TurnIntensity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteKeepStepDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteKeepStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteRampStepDetails:
    boto3_raw_data: "type_defs.RouteRampStepDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    SteeringDirection = field("SteeringDirection")
    TurnAngle = field("TurnAngle")
    TurnIntensity = field("TurnIntensity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteRampStepDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteRampStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteRoundaboutEnterStepDetails:
    boto3_raw_data: "type_defs.RouteRoundaboutEnterStepDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    SteeringDirection = field("SteeringDirection")
    TurnAngle = field("TurnAngle")
    TurnIntensity = field("TurnIntensity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteRoundaboutEnterStepDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteRoundaboutEnterStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteRoundaboutExitStepDetails:
    boto3_raw_data: "type_defs.RouteRoundaboutExitStepDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    RelativeExit = field("RelativeExit")
    RoundaboutAngle = field("RoundaboutAngle")
    SteeringDirection = field("SteeringDirection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteRoundaboutExitStepDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteRoundaboutExitStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteRoundaboutPassStepDetails:
    boto3_raw_data: "type_defs.RouteRoundaboutPassStepDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    SteeringDirection = field("SteeringDirection")
    TurnAngle = field("TurnAngle")
    TurnIntensity = field("TurnIntensity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteRoundaboutPassStepDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteRoundaboutPassStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTurnStepDetails:
    boto3_raw_data: "type_defs.RouteTurnStepDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    SteeringDirection = field("SteeringDirection")
    TurnAngle = field("TurnAngle")
    TurnIntensity = field("TurnIntensity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteTurnStepDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTurnStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteUTurnStepDetails:
    boto3_raw_data: "type_defs.RouteUTurnStepDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Intersection(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Intersection"])

    SteeringDirection = field("SteeringDirection")
    TurnAngle = field("TurnAngle")
    TurnIntensity = field("TurnIntensity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteUTurnStepDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteUTurnStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapToRoadsResponse:
    boto3_raw_data: "type_defs.SnapToRoadsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Notices(self):  # pragma: no cover
        return RoadSnapNotice.make_many(self.boto3_raw_data["Notices"])

    PricingBucket = field("PricingBucket")

    @cached_property
    def SnappedGeometry(self):  # pragma: no cover
        return RoadSnapSnappedGeometry.make_one(self.boto3_raw_data["SnappedGeometry"])

    SnappedGeometryFormat = field("SnappedGeometryFormat")

    @cached_property
    def SnappedTracePoints(self):  # pragma: no cover
        return RoadSnapSnappedTracePoint.make_many(
            self.boto3_raw_data["SnappedTracePoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnapToRoadsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapToRoadsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoadSnapTruckOptions:
    boto3_raw_data: "type_defs.RoadSnapTruckOptionsTypeDef" = dataclasses.field()

    GrossWeight = field("GrossWeight")
    HazardousCargos = field("HazardousCargos")
    Height = field("Height")
    Length = field("Length")

    @cached_property
    def Trailer(self):  # pragma: no cover
        return RoadSnapTrailerOptions.make_one(self.boto3_raw_data["Trailer"])

    TunnelRestrictionCode = field("TunnelRestrictionCode")
    Width = field("Width")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoadSnapTruckOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoadSnapTruckOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteCarOptions:
    boto3_raw_data: "type_defs.RouteCarOptionsTypeDef" = dataclasses.field()

    EngineType = field("EngineType")

    @cached_property
    def LicensePlate(self):  # pragma: no cover
        return RouteVehicleLicensePlate.make_one(self.boto3_raw_data["LicensePlate"])

    MaxSpeed = field("MaxSpeed")
    Occupancy = field("Occupancy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteCarOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteCarOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteScooterOptions:
    boto3_raw_data: "type_defs.RouteScooterOptionsTypeDef" = dataclasses.field()

    EngineType = field("EngineType")

    @cached_property
    def LicensePlate(self):  # pragma: no cover
        return RouteVehicleLicensePlate.make_one(self.boto3_raw_data["LicensePlate"])

    MaxSpeed = field("MaxSpeed")
    Occupancy = field("Occupancy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteScooterOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteScooterOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteDestinationOptions:
    boto3_raw_data: "type_defs.RouteDestinationOptionsTypeDef" = dataclasses.field()

    AvoidActionsForDistance = field("AvoidActionsForDistance")
    AvoidUTurns = field("AvoidUTurns")
    Heading = field("Heading")

    @cached_property
    def Matching(self):  # pragma: no cover
        return RouteMatchingOptions.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def SideOfStreet(self):  # pragma: no cover
        return RouteSideOfStreetOptions.make_one(self.boto3_raw_data["SideOfStreet"])

    StopDuration = field("StopDuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteDestinationOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteDestinationOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteOriginOptions:
    boto3_raw_data: "type_defs.RouteOriginOptionsTypeDef" = dataclasses.field()

    AvoidActionsForDistance = field("AvoidActionsForDistance")
    AvoidUTurns = field("AvoidUTurns")
    Heading = field("Heading")

    @cached_property
    def Matching(self):  # pragma: no cover
        return RouteMatchingOptions.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def SideOfStreet(self):  # pragma: no cover
        return RouteSideOfStreetOptions.make_one(self.boto3_raw_data["SideOfStreet"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteOriginOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteOriginOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteWaypoint:
    boto3_raw_data: "type_defs.RouteWaypointTypeDef" = dataclasses.field()

    Position = field("Position")
    AvoidActionsForDistance = field("AvoidActionsForDistance")
    AvoidUTurns = field("AvoidUTurns")
    Heading = field("Heading")

    @cached_property
    def Matching(self):  # pragma: no cover
        return RouteMatchingOptions.make_one(self.boto3_raw_data["Matching"])

    PassThrough = field("PassThrough")

    @cached_property
    def SideOfStreet(self):  # pragma: no cover
        return RouteSideOfStreetOptions.make_one(self.boto3_raw_data["SideOfStreet"])

    StopDuration = field("StopDuration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteWaypointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteWaypointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteDriverOptions:
    boto3_raw_data: "type_defs.RouteDriverOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Schedule(self):  # pragma: no cover
        return RouteDriverScheduleInterval.make_many(self.boto3_raw_data["Schedule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteDriverOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteDriverOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollOptions:
    boto3_raw_data: "type_defs.RouteTollOptionsTypeDef" = dataclasses.field()

    AllTransponders = field("AllTransponders")
    AllVignettes = field("AllVignettes")
    Currency = field("Currency")

    @cached_property
    def EmissionType(self):  # pragma: no cover
        return RouteEmissionType.make_one(self.boto3_raw_data["EmissionType"])

    VehicleCategory = field("VehicleCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTollOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTollOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryArrival:
    boto3_raw_data: "type_defs.RouteFerryArrivalTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return RouteFerryPlace.make_one(self.boto3_raw_data["Place"])

    Time = field("Time")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteFerryArrivalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerryArrivalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryDeparture:
    boto3_raw_data: "type_defs.RouteFerryDepartureTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return RouteFerryPlace.make_one(self.boto3_raw_data["Place"])

    Time = field("Time")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteFerryDepartureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerryDepartureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerrySummary:
    boto3_raw_data: "type_defs.RouteFerrySummaryTypeDef" = dataclasses.field()

    @cached_property
    def Overview(self):  # pragma: no cover
        return RouteFerryOverviewSummary.make_one(self.boto3_raw_data["Overview"])

    @cached_property
    def TravelOnly(self):  # pragma: no cover
        return RouteFerryTravelOnlySummary.make_one(self.boto3_raw_data["TravelOnly"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteFerrySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerrySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMajorRoadLabel:
    boto3_raw_data: "type_defs.RouteMajorRoadLabelTypeDef" = dataclasses.field()

    @cached_property
    def RoadName(self):  # pragma: no cover
        return LocalizedString.make_one(self.boto3_raw_data["RoadName"])

    @cached_property
    def RouteNumber(self):  # pragma: no cover
        return RouteNumber.make_one(self.boto3_raw_data["RouteNumber"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMajorRoadLabelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMajorRoadLabelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteRoad:
    boto3_raw_data: "type_defs.RouteRoadTypeDef" = dataclasses.field()

    @cached_property
    def RoadName(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["RoadName"])

    @cached_property
    def RouteNumber(self):  # pragma: no cover
        return RouteNumber.make_many(self.boto3_raw_data["RouteNumber"])

    @cached_property
    def Towards(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Towards"])

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteRoadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteRoadTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteSignpostLabel:
    boto3_raw_data: "type_defs.RouteSignpostLabelTypeDef" = dataclasses.field()

    @cached_property
    def RouteNumber(self):  # pragma: no cover
        return RouteNumber.make_one(self.boto3_raw_data["RouteNumber"])

    @cached_property
    def Text(self):  # pragma: no cover
        return LocalizedString.make_one(self.boto3_raw_data["Text"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteSignpostLabelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteSignpostLabelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixBoundaryGeometryOutput:
    boto3_raw_data: "type_defs.RouteMatrixBoundaryGeometryOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoCircle(self):  # pragma: no cover
        return RouteMatrixAutoCircle.make_one(self.boto3_raw_data["AutoCircle"])

    @cached_property
    def Circle(self):  # pragma: no cover
        return CircleOutput.make_one(self.boto3_raw_data["Circle"])

    BoundingBox = field("BoundingBox")
    Polygon = field("Polygon")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RouteMatrixBoundaryGeometryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixBoundaryGeometryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixBoundaryGeometry:
    boto3_raw_data: "type_defs.RouteMatrixBoundaryGeometryTypeDef" = dataclasses.field()

    @cached_property
    def AutoCircle(self):  # pragma: no cover
        return RouteMatrixAutoCircle.make_one(self.boto3_raw_data["AutoCircle"])

    @cached_property
    def Circle(self):  # pragma: no cover
        return Circle.make_one(self.boto3_raw_data["Circle"])

    BoundingBox = field("BoundingBox")
    Polygon = field("Polygon")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixBoundaryGeometryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixBoundaryGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixAvoidanceArea:
    boto3_raw_data: "type_defs.RouteMatrixAvoidanceAreaTypeDef" = dataclasses.field()

    @cached_property
    def Geometry(self):  # pragma: no cover
        return RouteMatrixAvoidanceAreaGeometry.make_one(
            self.boto3_raw_data["Geometry"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixAvoidanceAreaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixAvoidanceAreaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixCarOptions:
    boto3_raw_data: "type_defs.RouteMatrixCarOptionsTypeDef" = dataclasses.field()

    @cached_property
    def LicensePlate(self):  # pragma: no cover
        return RouteMatrixVehicleLicensePlate.make_one(
            self.boto3_raw_data["LicensePlate"]
        )

    MaxSpeed = field("MaxSpeed")
    Occupancy = field("Occupancy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixCarOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixCarOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixScooterOptions:
    boto3_raw_data: "type_defs.RouteMatrixScooterOptionsTypeDef" = dataclasses.field()

    @cached_property
    def LicensePlate(self):  # pragma: no cover
        return RouteMatrixVehicleLicensePlate.make_one(
            self.boto3_raw_data["LicensePlate"]
        )

    MaxSpeed = field("MaxSpeed")
    Occupancy = field("Occupancy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixScooterOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixScooterOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixDestinationOptions:
    boto3_raw_data: "type_defs.RouteMatrixDestinationOptionsTypeDef" = (
        dataclasses.field()
    )

    AvoidActionsForDistance = field("AvoidActionsForDistance")
    Heading = field("Heading")

    @cached_property
    def Matching(self):  # pragma: no cover
        return RouteMatrixMatchingOptions.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def SideOfStreet(self):  # pragma: no cover
        return RouteMatrixSideOfStreetOptions.make_one(
            self.boto3_raw_data["SideOfStreet"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RouteMatrixDestinationOptionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixDestinationOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixOriginOptions:
    boto3_raw_data: "type_defs.RouteMatrixOriginOptionsTypeDef" = dataclasses.field()

    AvoidActionsForDistance = field("AvoidActionsForDistance")
    Heading = field("Heading")

    @cached_property
    def Matching(self):  # pragma: no cover
        return RouteMatrixMatchingOptions.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def SideOfStreet(self):  # pragma: no cover
        return RouteMatrixSideOfStreetOptions.make_one(
            self.boto3_raw_data["SideOfStreet"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixOriginOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixOriginOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixTruckOptions:
    boto3_raw_data: "type_defs.RouteMatrixTruckOptionsTypeDef" = dataclasses.field()

    AxleCount = field("AxleCount")
    GrossWeight = field("GrossWeight")
    HazardousCargos = field("HazardousCargos")
    Height = field("Height")
    KpraLength = field("KpraLength")
    Length = field("Length")

    @cached_property
    def LicensePlate(self):  # pragma: no cover
        return RouteMatrixVehicleLicensePlate.make_one(
            self.boto3_raw_data["LicensePlate"]
        )

    MaxSpeed = field("MaxSpeed")
    Occupancy = field("Occupancy")
    PayloadCapacity = field("PayloadCapacity")

    @cached_property
    def Trailer(self):  # pragma: no cover
        return RouteMatrixTrailerOptions.make_one(self.boto3_raw_data["Trailer"])

    TruckType = field("TruckType")
    TunnelRestrictionCode = field("TunnelRestrictionCode")
    WeightPerAxle = field("WeightPerAxle")

    @cached_property
    def WeightPerAxleGroup(self):  # pragma: no cover
        return WeightPerAxleGroup.make_one(self.boto3_raw_data["WeightPerAxleGroup"])

    Width = field("Width")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixTruckOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixTruckOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePassThroughWaypoint:
    boto3_raw_data: "type_defs.RoutePassThroughWaypointTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return RoutePassThroughPlace.make_one(self.boto3_raw_data["Place"])

    GeometryOffset = field("GeometryOffset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePassThroughWaypointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePassThroughWaypointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianArrival:
    boto3_raw_data: "type_defs.RoutePedestrianArrivalTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return RoutePedestrianPlace.make_one(self.boto3_raw_data["Place"])

    Time = field("Time")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePedestrianArrivalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianArrivalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianDeparture:
    boto3_raw_data: "type_defs.RoutePedestrianDepartureTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return RoutePedestrianPlace.make_one(self.boto3_raw_data["Place"])

    Time = field("Time")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePedestrianDepartureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianDepartureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianSpan:
    boto3_raw_data: "type_defs.RoutePedestrianSpanTypeDef" = dataclasses.field()

    BestCaseDuration = field("BestCaseDuration")
    Country = field("Country")
    Distance = field("Distance")
    Duration = field("Duration")

    @cached_property
    def DynamicSpeed(self):  # pragma: no cover
        return RouteSpanDynamicSpeedDetails.make_one(
            self.boto3_raw_data["DynamicSpeed"]
        )

    FunctionalClassification = field("FunctionalClassification")
    GeometryOffset = field("GeometryOffset")
    Incidents = field("Incidents")

    @cached_property
    def Names(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Names"])

    PedestrianAccess = field("PedestrianAccess")
    Region = field("Region")
    RoadAttributes = field("RoadAttributes")

    @cached_property
    def RouteNumbers(self):  # pragma: no cover
        return RouteNumber.make_many(self.boto3_raw_data["RouteNumbers"])

    @cached_property
    def SpeedLimit(self):  # pragma: no cover
        return RouteSpanSpeedLimitDetails.make_one(self.boto3_raw_data["SpeedLimit"])

    TypicalDuration = field("TypicalDuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePedestrianSpanTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianSpanTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleSpan:
    boto3_raw_data: "type_defs.RouteVehicleSpanTypeDef" = dataclasses.field()

    BestCaseDuration = field("BestCaseDuration")
    CarAccess = field("CarAccess")
    Country = field("Country")
    Distance = field("Distance")
    Duration = field("Duration")

    @cached_property
    def DynamicSpeed(self):  # pragma: no cover
        return RouteSpanDynamicSpeedDetails.make_one(
            self.boto3_raw_data["DynamicSpeed"]
        )

    FunctionalClassification = field("FunctionalClassification")
    Gate = field("Gate")
    GeometryOffset = field("GeometryOffset")
    Incidents = field("Incidents")

    @cached_property
    def Names(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["Names"])

    Notices = field("Notices")
    RailwayCrossing = field("RailwayCrossing")
    Region = field("Region")
    RoadAttributes = field("RoadAttributes")

    @cached_property
    def RouteNumbers(self):  # pragma: no cover
        return RouteNumber.make_many(self.boto3_raw_data["RouteNumbers"])

    ScooterAccess = field("ScooterAccess")

    @cached_property
    def SpeedLimit(self):  # pragma: no cover
        return RouteSpanSpeedLimitDetails.make_one(self.boto3_raw_data["SpeedLimit"])

    TollSystems = field("TollSystems")
    TruckAccess = field("TruckAccess")
    TruckRoadTypes = field("TruckRoadTypes")
    TypicalDuration = field("TypicalDuration")
    Zones = field("Zones")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleSpanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleSpanTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianSummary:
    boto3_raw_data: "type_defs.RoutePedestrianSummaryTypeDef" = dataclasses.field()

    @cached_property
    def Overview(self):  # pragma: no cover
        return RoutePedestrianOverviewSummary.make_one(self.boto3_raw_data["Overview"])

    @cached_property
    def TravelOnly(self):  # pragma: no cover
        return RoutePedestrianTravelOnlySummary.make_one(
            self.boto3_raw_data["TravelOnly"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePedestrianSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollPass:
    boto3_raw_data: "type_defs.RouteTollPassTypeDef" = dataclasses.field()

    IncludesReturnTrip = field("IncludesReturnTrip")
    SeniorPass = field("SeniorPass")
    TransferCount = field("TransferCount")
    TripCount = field("TripCount")

    @cached_property
    def ValidityPeriod(self):  # pragma: no cover
        return RouteTollPassValidityPeriod.make_one(
            self.boto3_raw_data["ValidityPeriod"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTollPassTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTollPassTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollPriceSummary:
    boto3_raw_data: "type_defs.RouteTollPriceSummaryTypeDef" = dataclasses.field()

    Currency = field("Currency")
    Estimate = field("Estimate")
    Range = field("Range")
    Value = field("Value")

    @cached_property
    def RangeValue(self):  # pragma: no cover
        return RouteTollPriceValueRange.make_one(self.boto3_raw_data["RangeValue"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteTollPriceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTollPriceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollPrice:
    boto3_raw_data: "type_defs.RouteTollPriceTypeDef" = dataclasses.field()

    Currency = field("Currency")
    Estimate = field("Estimate")
    Range = field("Range")
    Value = field("Value")
    PerDuration = field("PerDuration")

    @cached_property
    def RangeValue(self):  # pragma: no cover
        return RouteTollPriceValueRange.make_one(self.boto3_raw_data["RangeValue"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTollPriceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTollPriceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTruckOptions:
    boto3_raw_data: "type_defs.RouteTruckOptionsTypeDef" = dataclasses.field()

    AxleCount = field("AxleCount")
    EngineType = field("EngineType")
    GrossWeight = field("GrossWeight")
    HazardousCargos = field("HazardousCargos")
    Height = field("Height")
    HeightAboveFirstAxle = field("HeightAboveFirstAxle")
    KpraLength = field("KpraLength")
    Length = field("Length")

    @cached_property
    def LicensePlate(self):  # pragma: no cover
        return RouteVehicleLicensePlate.make_one(self.boto3_raw_data["LicensePlate"])

    MaxSpeed = field("MaxSpeed")
    Occupancy = field("Occupancy")
    PayloadCapacity = field("PayloadCapacity")
    TireCount = field("TireCount")

    @cached_property
    def Trailer(self):  # pragma: no cover
        return RouteTrailerOptions.make_one(self.boto3_raw_data["Trailer"])

    TruckType = field("TruckType")
    TunnelRestrictionCode = field("TunnelRestrictionCode")
    WeightPerAxle = field("WeightPerAxle")

    @cached_property
    def WeightPerAxleGroup(self):  # pragma: no cover
        return WeightPerAxleGroup.make_one(self.boto3_raw_data["WeightPerAxleGroup"])

    Width = field("Width")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTruckOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTruckOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleArrival:
    boto3_raw_data: "type_defs.RouteVehicleArrivalTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return RouteVehiclePlace.make_one(self.boto3_raw_data["Place"])

    Time = field("Time")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleArrivalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleArrivalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleDeparture:
    boto3_raw_data: "type_defs.RouteVehicleDepartureTypeDef" = dataclasses.field()

    @cached_property
    def Place(self):  # pragma: no cover
        return RouteVehiclePlace.make_one(self.boto3_raw_data["Place"])

    Time = field("Time")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleDepartureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleDepartureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleSummary:
    boto3_raw_data: "type_defs.RouteVehicleSummaryTypeDef" = dataclasses.field()

    @cached_property
    def Overview(self):  # pragma: no cover
        return RouteVehicleOverviewSummary.make_one(self.boto3_raw_data["Overview"])

    @cached_property
    def TravelOnly(self):  # pragma: no cover
        return RouteVehicleTravelOnlySummary.make_one(self.boto3_raw_data["TravelOnly"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteViolatedConstraints:
    boto3_raw_data: "type_defs.RouteViolatedConstraintsTypeDef" = dataclasses.field()

    HazardousCargos = field("HazardousCargos")
    AllHazardsRestricted = field("AllHazardsRestricted")

    @cached_property
    def AxleCount(self):  # pragma: no cover
        return RouteNoticeDetailRange.make_one(self.boto3_raw_data["AxleCount"])

    MaxHeight = field("MaxHeight")
    MaxKpraLength = field("MaxKpraLength")
    MaxLength = field("MaxLength")
    MaxPayloadCapacity = field("MaxPayloadCapacity")

    @cached_property
    def MaxWeight(self):  # pragma: no cover
        return RouteWeightConstraint.make_one(self.boto3_raw_data["MaxWeight"])

    MaxWeightPerAxle = field("MaxWeightPerAxle")

    @cached_property
    def MaxWeightPerAxleGroup(self):  # pragma: no cover
        return WeightPerAxleGroup.make_one(self.boto3_raw_data["MaxWeightPerAxleGroup"])

    MaxWidth = field("MaxWidth")

    @cached_property
    def Occupancy(self):  # pragma: no cover
        return RouteNoticeDetailRange.make_one(self.boto3_raw_data["Occupancy"])

    RestrictedTimes = field("RestrictedTimes")
    TimeDependent = field("TimeDependent")

    @cached_property
    def TrailerCount(self):  # pragma: no cover
        return RouteNoticeDetailRange.make_one(self.boto3_raw_data["TrailerCount"])

    TravelMode = field("TravelMode")
    TruckRoadType = field("TruckRoadType")
    TruckType = field("TruckType")
    TunnelRestrictionCode = field("TunnelRestrictionCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteViolatedConstraintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteViolatedConstraintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationAccessHours:
    boto3_raw_data: "type_defs.WaypointOptimizationAccessHoursTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def From(self):  # pragma: no cover
        return WaypointOptimizationAccessHoursEntry.make_one(
            self.boto3_raw_data["From"]
        )

    @cached_property
    def To(self):  # pragma: no cover
        return WaypointOptimizationAccessHoursEntry.make_one(self.boto3_raw_data["To"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WaypointOptimizationAccessHoursTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationAccessHoursTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationAvoidanceArea:
    boto3_raw_data: "type_defs.WaypointOptimizationAvoidanceAreaTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Geometry(self):  # pragma: no cover
        return WaypointOptimizationAvoidanceAreaGeometry.make_one(
            self.boto3_raw_data["Geometry"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationAvoidanceAreaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationAvoidanceAreaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationClusteringOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationClusteringOptionsTypeDef" = (
        dataclasses.field()
    )

    Algorithm = field("Algorithm")

    @cached_property
    def DrivingDistanceOptions(self):  # pragma: no cover
        return WaypointOptimizationDrivingDistanceOptions.make_one(
            self.boto3_raw_data["DrivingDistanceOptions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationClusteringOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationClusteringOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationImpedingWaypoint:
    boto3_raw_data: "type_defs.WaypointOptimizationImpedingWaypointTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedConstraints(self):  # pragma: no cover
        return WaypointOptimizationFailedConstraint.make_many(
            self.boto3_raw_data["FailedConstraints"]
        )

    Id = field("Id")
    Position = field("Position")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationImpedingWaypointTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationImpedingWaypointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationRestCycles:
    boto3_raw_data: "type_defs.WaypointOptimizationRestCyclesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LongCycle(self):  # pragma: no cover
        return WaypointOptimizationRestCycleDurations.make_one(
            self.boto3_raw_data["LongCycle"]
        )

    @cached_property
    def ShortCycle(self):  # pragma: no cover
        return WaypointOptimizationRestCycleDurations.make_one(
            self.boto3_raw_data["ShortCycle"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WaypointOptimizationRestCyclesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationRestCyclesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationTruckOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationTruckOptionsTypeDef" = (
        dataclasses.field()
    )

    GrossWeight = field("GrossWeight")
    HazardousCargos = field("HazardousCargos")
    Height = field("Height")
    Length = field("Length")

    @cached_property
    def Trailer(self):  # pragma: no cover
        return WaypointOptimizationTrailerOptions.make_one(
            self.boto3_raw_data["Trailer"]
        )

    TruckType = field("TruckType")
    TunnelRestrictionCode = field("TunnelRestrictionCode")
    WeightPerAxle = field("WeightPerAxle")
    Width = field("Width")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WaypointOptimizationTruckOptionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationTruckOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineAvoidanceArea:
    boto3_raw_data: "type_defs.IsolineAvoidanceAreaTypeDef" = dataclasses.field()

    @cached_property
    def Geometry(self):  # pragma: no cover
        return IsolineAvoidanceAreaGeometry.make_one(self.boto3_raw_data["Geometry"])

    @cached_property
    def Except(self):  # pragma: no cover
        return IsolineAvoidanceAreaGeometry.make_many(self.boto3_raw_data["Except"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineAvoidanceAreaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineAvoidanceAreaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteAvoidanceArea:
    boto3_raw_data: "type_defs.RouteAvoidanceAreaTypeDef" = dataclasses.field()

    @cached_property
    def Geometry(self):  # pragma: no cover
        return RouteAvoidanceAreaGeometry.make_one(self.boto3_raw_data["Geometry"])

    @cached_property
    def Except(self):  # pragma: no cover
        return RouteAvoidanceAreaGeometry.make_many(self.boto3_raw_data["Except"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteAvoidanceAreaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteAvoidanceAreaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Isoline:
    boto3_raw_data: "type_defs.IsolineTypeDef" = dataclasses.field()

    @cached_property
    def Connections(self):  # pragma: no cover
        return IsolineConnection.make_many(self.boto3_raw_data["Connections"])

    @cached_property
    def Geometries(self):  # pragma: no cover
        return IsolineShapeGeometry.make_many(self.boto3_raw_data["Geometries"])

    DistanceThreshold = field("DistanceThreshold")
    TimeThreshold = field("TimeThreshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IsolineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IsolineTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineTravelModeOptions:
    boto3_raw_data: "type_defs.IsolineTravelModeOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Car(self):  # pragma: no cover
        return IsolineCarOptions.make_one(self.boto3_raw_data["Car"])

    @cached_property
    def Scooter(self):  # pragma: no cover
        return IsolineScooterOptions.make_one(self.boto3_raw_data["Scooter"])

    @cached_property
    def Truck(self):  # pragma: no cover
        return IsolineTruckOptions.make_one(self.boto3_raw_data["Truck"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineTravelModeOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineTravelModeOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoadSnapTravelModeOptions:
    boto3_raw_data: "type_defs.RoadSnapTravelModeOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Truck(self):  # pragma: no cover
        return RoadSnapTruckOptions.make_one(self.boto3_raw_data["Truck"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoadSnapTravelModeOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoadSnapTravelModeOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteSignpost:
    boto3_raw_data: "type_defs.RouteSignpostTypeDef" = dataclasses.field()

    @cached_property
    def Labels(self):  # pragma: no cover
        return RouteSignpostLabel.make_many(self.boto3_raw_data["Labels"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteSignpostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteSignpostTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixBoundaryOutput:
    boto3_raw_data: "type_defs.RouteMatrixBoundaryOutputTypeDef" = dataclasses.field()

    @cached_property
    def Geometry(self):  # pragma: no cover
        return RouteMatrixBoundaryGeometryOutput.make_one(
            self.boto3_raw_data["Geometry"]
        )

    Unbounded = field("Unbounded")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixBoundaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixBoundaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixBoundary:
    boto3_raw_data: "type_defs.RouteMatrixBoundaryTypeDef" = dataclasses.field()

    @cached_property
    def Geometry(self):  # pragma: no cover
        return RouteMatrixBoundaryGeometry.make_one(self.boto3_raw_data["Geometry"])

    Unbounded = field("Unbounded")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixBoundaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixBoundaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixAvoidanceOptions:
    boto3_raw_data: "type_defs.RouteMatrixAvoidanceOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Areas(self):  # pragma: no cover
        return RouteMatrixAvoidanceArea.make_many(self.boto3_raw_data["Areas"])

    CarShuttleTrains = field("CarShuttleTrains")
    ControlledAccessHighways = field("ControlledAccessHighways")
    DirtRoads = field("DirtRoads")
    Ferries = field("Ferries")
    TollRoads = field("TollRoads")
    TollTransponders = field("TollTransponders")
    TruckRoadTypes = field("TruckRoadTypes")
    Tunnels = field("Tunnels")
    UTurns = field("UTurns")

    @cached_property
    def ZoneCategories(self):  # pragma: no cover
        return RouteMatrixAvoidanceZoneCategory.make_many(
            self.boto3_raw_data["ZoneCategories"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixAvoidanceOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixAvoidanceOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixDestination:
    boto3_raw_data: "type_defs.RouteMatrixDestinationTypeDef" = dataclasses.field()

    Position = field("Position")

    @cached_property
    def Options(self):  # pragma: no cover
        return RouteMatrixDestinationOptions.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixOrigin:
    boto3_raw_data: "type_defs.RouteMatrixOriginTypeDef" = dataclasses.field()

    Position = field("Position")

    @cached_property
    def Options(self):  # pragma: no cover
        return RouteMatrixOriginOptions.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixOriginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixOriginTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteMatrixTravelModeOptions:
    boto3_raw_data: "type_defs.RouteMatrixTravelModeOptionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Car(self):  # pragma: no cover
        return RouteMatrixCarOptions.make_one(self.boto3_raw_data["Car"])

    @cached_property
    def Scooter(self):  # pragma: no cover
        return RouteMatrixScooterOptions.make_one(self.boto3_raw_data["Scooter"])

    @cached_property
    def Truck(self):  # pragma: no cover
        return RouteMatrixTruckOptions.make_one(self.boto3_raw_data["Truck"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteMatrixTravelModeOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteMatrixTravelModeOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteFerryLegDetails:
    boto3_raw_data: "type_defs.RouteFerryLegDetailsTypeDef" = dataclasses.field()

    @cached_property
    def AfterTravelSteps(self):  # pragma: no cover
        return RouteFerryAfterTravelStep.make_many(
            self.boto3_raw_data["AfterTravelSteps"]
        )

    @cached_property
    def Arrival(self):  # pragma: no cover
        return RouteFerryArrival.make_one(self.boto3_raw_data["Arrival"])

    @cached_property
    def BeforeTravelSteps(self):  # pragma: no cover
        return RouteFerryBeforeTravelStep.make_many(
            self.boto3_raw_data["BeforeTravelSteps"]
        )

    @cached_property
    def Departure(self):  # pragma: no cover
        return RouteFerryDeparture.make_one(self.boto3_raw_data["Departure"])

    @cached_property
    def Notices(self):  # pragma: no cover
        return RouteFerryNotice.make_many(self.boto3_raw_data["Notices"])

    @cached_property
    def PassThroughWaypoints(self):  # pragma: no cover
        return RoutePassThroughWaypoint.make_many(
            self.boto3_raw_data["PassThroughWaypoints"]
        )

    @cached_property
    def Spans(self):  # pragma: no cover
        return RouteFerrySpan.make_many(self.boto3_raw_data["Spans"])

    @cached_property
    def TravelSteps(self):  # pragma: no cover
        return RouteFerryTravelStep.make_many(self.boto3_raw_data["TravelSteps"])

    RouteName = field("RouteName")

    @cached_property
    def Summary(self):  # pragma: no cover
        return RouteFerrySummary.make_one(self.boto3_raw_data["Summary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteFerryLegDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFerryLegDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollSummary:
    boto3_raw_data: "type_defs.RouteTollSummaryTypeDef" = dataclasses.field()

    @cached_property
    def Total(self):  # pragma: no cover
        return RouteTollPriceSummary.make_one(self.boto3_raw_data["Total"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTollSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTollSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTollRate:
    boto3_raw_data: "type_defs.RouteTollRateTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def LocalPrice(self):  # pragma: no cover
        return RouteTollPrice.make_one(self.boto3_raw_data["LocalPrice"])

    Name = field("Name")
    PaymentMethods = field("PaymentMethods")

    @cached_property
    def Transponders(self):  # pragma: no cover
        return RouteTransponder.make_many(self.boto3_raw_data["Transponders"])

    ApplicableTimes = field("ApplicableTimes")

    @cached_property
    def ConvertedPrice(self):  # pragma: no cover
        return RouteTollPrice.make_one(self.boto3_raw_data["ConvertedPrice"])

    @cached_property
    def Pass(self):  # pragma: no cover
        return RouteTollPass.make_one(self.boto3_raw_data["Pass"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTollRateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTollRateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteTravelModeOptions:
    boto3_raw_data: "type_defs.RouteTravelModeOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Car(self):  # pragma: no cover
        return RouteCarOptions.make_one(self.boto3_raw_data["Car"])

    @cached_property
    def Pedestrian(self):  # pragma: no cover
        return RoutePedestrianOptions.make_one(self.boto3_raw_data["Pedestrian"])

    @cached_property
    def Scooter(self):  # pragma: no cover
        return RouteScooterOptions.make_one(self.boto3_raw_data["Scooter"])

    @cached_property
    def Truck(self):  # pragma: no cover
        return RouteTruckOptions.make_one(self.boto3_raw_data["Truck"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteTravelModeOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteTravelModeOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleNoticeDetail:
    boto3_raw_data: "type_defs.RouteVehicleNoticeDetailTypeDef" = dataclasses.field()

    Title = field("Title")

    @cached_property
    def ViolatedConstraints(self):  # pragma: no cover
        return RouteViolatedConstraints.make_one(
            self.boto3_raw_data["ViolatedConstraints"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleNoticeDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleNoticeDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationDestinationOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationDestinationOptionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessHours(self):  # pragma: no cover
        return WaypointOptimizationAccessHours.make_one(
            self.boto3_raw_data["AccessHours"]
        )

    AppointmentTime = field("AppointmentTime")
    Heading = field("Heading")
    Id = field("Id")
    ServiceDuration = field("ServiceDuration")

    @cached_property
    def SideOfStreet(self):  # pragma: no cover
        return WaypointOptimizationSideOfStreetOptions.make_one(
            self.boto3_raw_data["SideOfStreet"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationDestinationOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationDestinationOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationWaypoint:
    boto3_raw_data: "type_defs.WaypointOptimizationWaypointTypeDef" = (
        dataclasses.field()
    )

    Position = field("Position")

    @cached_property
    def AccessHours(self):  # pragma: no cover
        return WaypointOptimizationAccessHours.make_one(
            self.boto3_raw_data["AccessHours"]
        )

    AppointmentTime = field("AppointmentTime")
    Before = field("Before")
    Heading = field("Heading")
    Id = field("Id")
    ServiceDuration = field("ServiceDuration")

    @cached_property
    def SideOfStreet(self):  # pragma: no cover
        return WaypointOptimizationSideOfStreetOptions.make_one(
            self.boto3_raw_data["SideOfStreet"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WaypointOptimizationWaypointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationWaypointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationAvoidanceOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationAvoidanceOptionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Areas(self):  # pragma: no cover
        return WaypointOptimizationAvoidanceArea.make_many(self.boto3_raw_data["Areas"])

    CarShuttleTrains = field("CarShuttleTrains")
    ControlledAccessHighways = field("ControlledAccessHighways")
    DirtRoads = field("DirtRoads")
    Ferries = field("Ferries")
    TollRoads = field("TollRoads")
    Tunnels = field("Tunnels")
    UTurns = field("UTurns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationAvoidanceOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationAvoidanceOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptimizeWaypointsResponse:
    boto3_raw_data: "type_defs.OptimizeWaypointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connections(self):  # pragma: no cover
        return WaypointOptimizationConnection.make_many(
            self.boto3_raw_data["Connections"]
        )

    Distance = field("Distance")
    Duration = field("Duration")

    @cached_property
    def ImpedingWaypoints(self):  # pragma: no cover
        return WaypointOptimizationImpedingWaypoint.make_many(
            self.boto3_raw_data["ImpedingWaypoints"]
        )

    @cached_property
    def OptimizedWaypoints(self):  # pragma: no cover
        return WaypointOptimizationOptimizedWaypoint.make_many(
            self.boto3_raw_data["OptimizedWaypoints"]
        )

    PricingBucket = field("PricingBucket")

    @cached_property
    def TimeBreakdown(self):  # pragma: no cover
        return WaypointOptimizationTimeBreakdown.make_one(
            self.boto3_raw_data["TimeBreakdown"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptimizeWaypointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptimizeWaypointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationDriverOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationDriverOptionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RestCycles(self):  # pragma: no cover
        return WaypointOptimizationRestCycles.make_one(
            self.boto3_raw_data["RestCycles"]
        )

    @cached_property
    def RestProfile(self):  # pragma: no cover
        return WaypointOptimizationRestProfile.make_one(
            self.boto3_raw_data["RestProfile"]
        )

    TreatServiceTimeAs = field("TreatServiceTimeAs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationDriverOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationDriverOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaypointOptimizationTravelModeOptions:
    boto3_raw_data: "type_defs.WaypointOptimizationTravelModeOptionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Pedestrian(self):  # pragma: no cover
        return WaypointOptimizationPedestrianOptions.make_one(
            self.boto3_raw_data["Pedestrian"]
        )

    @cached_property
    def Truck(self):  # pragma: no cover
        return WaypointOptimizationTruckOptions.make_one(self.boto3_raw_data["Truck"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaypointOptimizationTravelModeOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaypointOptimizationTravelModeOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsolineAvoidanceOptions:
    boto3_raw_data: "type_defs.IsolineAvoidanceOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Areas(self):  # pragma: no cover
        return IsolineAvoidanceArea.make_many(self.boto3_raw_data["Areas"])

    CarShuttleTrains = field("CarShuttleTrains")
    ControlledAccessHighways = field("ControlledAccessHighways")
    DirtRoads = field("DirtRoads")
    Ferries = field("Ferries")
    SeasonalClosure = field("SeasonalClosure")
    TollRoads = field("TollRoads")
    TollTransponders = field("TollTransponders")
    TruckRoadTypes = field("TruckRoadTypes")
    Tunnels = field("Tunnels")
    UTurns = field("UTurns")

    @cached_property
    def ZoneCategories(self):  # pragma: no cover
        return IsolineAvoidanceZoneCategory.make_many(
            self.boto3_raw_data["ZoneCategories"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsolineAvoidanceOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsolineAvoidanceOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteAvoidanceOptions:
    boto3_raw_data: "type_defs.RouteAvoidanceOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Areas(self):  # pragma: no cover
        return RouteAvoidanceArea.make_many(self.boto3_raw_data["Areas"])

    CarShuttleTrains = field("CarShuttleTrains")
    ControlledAccessHighways = field("ControlledAccessHighways")
    DirtRoads = field("DirtRoads")
    Ferries = field("Ferries")
    SeasonalClosure = field("SeasonalClosure")
    TollRoads = field("TollRoads")
    TollTransponders = field("TollTransponders")
    TruckRoadTypes = field("TruckRoadTypes")
    Tunnels = field("Tunnels")
    UTurns = field("UTurns")

    @cached_property
    def ZoneCategories(self):  # pragma: no cover
        return RouteAvoidanceZoneCategory.make_many(
            self.boto3_raw_data["ZoneCategories"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteAvoidanceOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteAvoidanceOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateIsolinesResponse:
    boto3_raw_data: "type_defs.CalculateIsolinesResponseTypeDef" = dataclasses.field()

    ArrivalTime = field("ArrivalTime")
    DepartureTime = field("DepartureTime")
    IsolineGeometryFormat = field("IsolineGeometryFormat")

    @cached_property
    def Isolines(self):  # pragma: no cover
        return Isoline.make_many(self.boto3_raw_data["Isolines"])

    PricingBucket = field("PricingBucket")
    SnappedDestination = field("SnappedDestination")
    SnappedOrigin = field("SnappedOrigin")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateIsolinesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateIsolinesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapToRoadsRequest:
    boto3_raw_data: "type_defs.SnapToRoadsRequestTypeDef" = dataclasses.field()

    @cached_property
    def TracePoints(self):  # pragma: no cover
        return RoadSnapTracePoint.make_many(self.boto3_raw_data["TracePoints"])

    Key = field("Key")
    SnappedGeometryFormat = field("SnappedGeometryFormat")
    SnapRadius = field("SnapRadius")
    TravelMode = field("TravelMode")

    @cached_property
    def TravelModeOptions(self):  # pragma: no cover
        return RoadSnapTravelModeOptions.make_one(
            self.boto3_raw_data["TravelModeOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnapToRoadsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapToRoadsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianTravelStep:
    boto3_raw_data: "type_defs.RoutePedestrianTravelStepTypeDef" = dataclasses.field()

    Duration = field("Duration")
    Type = field("Type")

    @cached_property
    def ContinueStepDetails(self):  # pragma: no cover
        return RouteContinueStepDetails.make_one(
            self.boto3_raw_data["ContinueStepDetails"]
        )

    @cached_property
    def CurrentRoad(self):  # pragma: no cover
        return RouteRoad.make_one(self.boto3_raw_data["CurrentRoad"])

    Distance = field("Distance")

    @cached_property
    def ExitNumber(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["ExitNumber"])

    GeometryOffset = field("GeometryOffset")
    Instruction = field("Instruction")

    @cached_property
    def KeepStepDetails(self):  # pragma: no cover
        return RouteKeepStepDetails.make_one(self.boto3_raw_data["KeepStepDetails"])

    @cached_property
    def NextRoad(self):  # pragma: no cover
        return RouteRoad.make_one(self.boto3_raw_data["NextRoad"])

    @cached_property
    def RoundaboutEnterStepDetails(self):  # pragma: no cover
        return RouteRoundaboutEnterStepDetails.make_one(
            self.boto3_raw_data["RoundaboutEnterStepDetails"]
        )

    @cached_property
    def RoundaboutExitStepDetails(self):  # pragma: no cover
        return RouteRoundaboutExitStepDetails.make_one(
            self.boto3_raw_data["RoundaboutExitStepDetails"]
        )

    @cached_property
    def RoundaboutPassStepDetails(self):  # pragma: no cover
        return RouteRoundaboutPassStepDetails.make_one(
            self.boto3_raw_data["RoundaboutPassStepDetails"]
        )

    @cached_property
    def Signpost(self):  # pragma: no cover
        return RouteSignpost.make_one(self.boto3_raw_data["Signpost"])

    @cached_property
    def TurnStepDetails(self):  # pragma: no cover
        return RouteTurnStepDetails.make_one(self.boto3_raw_data["TurnStepDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePedestrianTravelStepTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianTravelStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleTravelStep:
    boto3_raw_data: "type_defs.RouteVehicleTravelStepTypeDef" = dataclasses.field()

    Duration = field("Duration")
    Type = field("Type")

    @cached_property
    def ContinueHighwayStepDetails(self):  # pragma: no cover
        return RouteContinueHighwayStepDetails.make_one(
            self.boto3_raw_data["ContinueHighwayStepDetails"]
        )

    @cached_property
    def ContinueStepDetails(self):  # pragma: no cover
        return RouteContinueStepDetails.make_one(
            self.boto3_raw_data["ContinueStepDetails"]
        )

    @cached_property
    def CurrentRoad(self):  # pragma: no cover
        return RouteRoad.make_one(self.boto3_raw_data["CurrentRoad"])

    Distance = field("Distance")

    @cached_property
    def EnterHighwayStepDetails(self):  # pragma: no cover
        return RouteEnterHighwayStepDetails.make_one(
            self.boto3_raw_data["EnterHighwayStepDetails"]
        )

    @cached_property
    def ExitNumber(self):  # pragma: no cover
        return LocalizedString.make_many(self.boto3_raw_data["ExitNumber"])

    @cached_property
    def ExitStepDetails(self):  # pragma: no cover
        return RouteExitStepDetails.make_one(self.boto3_raw_data["ExitStepDetails"])

    GeometryOffset = field("GeometryOffset")
    Instruction = field("Instruction")

    @cached_property
    def KeepStepDetails(self):  # pragma: no cover
        return RouteKeepStepDetails.make_one(self.boto3_raw_data["KeepStepDetails"])

    @cached_property
    def NextRoad(self):  # pragma: no cover
        return RouteRoad.make_one(self.boto3_raw_data["NextRoad"])

    @cached_property
    def RampStepDetails(self):  # pragma: no cover
        return RouteRampStepDetails.make_one(self.boto3_raw_data["RampStepDetails"])

    @cached_property
    def RoundaboutEnterStepDetails(self):  # pragma: no cover
        return RouteRoundaboutEnterStepDetails.make_one(
            self.boto3_raw_data["RoundaboutEnterStepDetails"]
        )

    @cached_property
    def RoundaboutExitStepDetails(self):  # pragma: no cover
        return RouteRoundaboutExitStepDetails.make_one(
            self.boto3_raw_data["RoundaboutExitStepDetails"]
        )

    @cached_property
    def RoundaboutPassStepDetails(self):  # pragma: no cover
        return RouteRoundaboutPassStepDetails.make_one(
            self.boto3_raw_data["RoundaboutPassStepDetails"]
        )

    @cached_property
    def Signpost(self):  # pragma: no cover
        return RouteSignpost.make_one(self.boto3_raw_data["Signpost"])

    @cached_property
    def TurnStepDetails(self):  # pragma: no cover
        return RouteTurnStepDetails.make_one(self.boto3_raw_data["TurnStepDetails"])

    @cached_property
    def UTurnStepDetails(self):  # pragma: no cover
        return RouteUTurnStepDetails.make_one(self.boto3_raw_data["UTurnStepDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleTravelStepTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleTravelStepTypeDef"]
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

    ErrorCount = field("ErrorCount")
    PricingBucket = field("PricingBucket")

    @cached_property
    def RouteMatrix(self):  # pragma: no cover
        return RouteMatrixEntry.make_many(self.boto3_raw_data["RouteMatrix"])

    @cached_property
    def RoutingBoundary(self):  # pragma: no cover
        return RouteMatrixBoundaryOutput.make_one(
            self.boto3_raw_data["RoutingBoundary"]
        )

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
class RouteSummary:
    boto3_raw_data: "type_defs.RouteSummaryTypeDef" = dataclasses.field()

    Distance = field("Distance")
    Duration = field("Duration")

    @cached_property
    def Tolls(self):  # pragma: no cover
        return RouteTollSummary.make_one(self.boto3_raw_data["Tolls"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteToll:
    boto3_raw_data: "type_defs.RouteTollTypeDef" = dataclasses.field()

    @cached_property
    def PaymentSites(self):  # pragma: no cover
        return RouteTollPaymentSite.make_many(self.boto3_raw_data["PaymentSites"])

    @cached_property
    def Rates(self):  # pragma: no cover
        return RouteTollRate.make_many(self.boto3_raw_data["Rates"])

    Systems = field("Systems")
    Country = field("Country")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTollTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTollTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteVehicleNotice:
    boto3_raw_data: "type_defs.RouteVehicleNoticeTypeDef" = dataclasses.field()

    Code = field("Code")

    @cached_property
    def Details(self):  # pragma: no cover
        return RouteVehicleNoticeDetail.make_many(self.boto3_raw_data["Details"])

    Impact = field("Impact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleNoticeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleNoticeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptimizeWaypointsRequest:
    boto3_raw_data: "type_defs.OptimizeWaypointsRequestTypeDef" = dataclasses.field()

    Origin = field("Origin")

    @cached_property
    def Avoid(self):  # pragma: no cover
        return WaypointOptimizationAvoidanceOptions.make_one(
            self.boto3_raw_data["Avoid"]
        )

    @cached_property
    def Clustering(self):  # pragma: no cover
        return WaypointOptimizationClusteringOptions.make_one(
            self.boto3_raw_data["Clustering"]
        )

    DepartureTime = field("DepartureTime")
    Destination = field("Destination")

    @cached_property
    def DestinationOptions(self):  # pragma: no cover
        return WaypointOptimizationDestinationOptions.make_one(
            self.boto3_raw_data["DestinationOptions"]
        )

    @cached_property
    def Driver(self):  # pragma: no cover
        return WaypointOptimizationDriverOptions.make_one(self.boto3_raw_data["Driver"])

    @cached_property
    def Exclude(self):  # pragma: no cover
        return WaypointOptimizationExclusionOptions.make_one(
            self.boto3_raw_data["Exclude"]
        )

    Key = field("Key")
    OptimizeSequencingFor = field("OptimizeSequencingFor")

    @cached_property
    def OriginOptions(self):  # pragma: no cover
        return WaypointOptimizationOriginOptions.make_one(
            self.boto3_raw_data["OriginOptions"]
        )

    @cached_property
    def Traffic(self):  # pragma: no cover
        return WaypointOptimizationTrafficOptions.make_one(
            self.boto3_raw_data["Traffic"]
        )

    TravelMode = field("TravelMode")

    @cached_property
    def TravelModeOptions(self):  # pragma: no cover
        return WaypointOptimizationTravelModeOptions.make_one(
            self.boto3_raw_data["TravelModeOptions"]
        )

    @cached_property
    def Waypoints(self):  # pragma: no cover
        return WaypointOptimizationWaypoint.make_many(self.boto3_raw_data["Waypoints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptimizeWaypointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptimizeWaypointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateIsolinesRequest:
    boto3_raw_data: "type_defs.CalculateIsolinesRequestTypeDef" = dataclasses.field()

    @cached_property
    def Thresholds(self):  # pragma: no cover
        return IsolineThresholds.make_one(self.boto3_raw_data["Thresholds"])

    @cached_property
    def Allow(self):  # pragma: no cover
        return IsolineAllowOptions.make_one(self.boto3_raw_data["Allow"])

    ArrivalTime = field("ArrivalTime")

    @cached_property
    def Avoid(self):  # pragma: no cover
        return IsolineAvoidanceOptions.make_one(self.boto3_raw_data["Avoid"])

    DepartNow = field("DepartNow")
    DepartureTime = field("DepartureTime")
    Destination = field("Destination")

    @cached_property
    def DestinationOptions(self):  # pragma: no cover
        return IsolineDestinationOptions.make_one(
            self.boto3_raw_data["DestinationOptions"]
        )

    IsolineGeometryFormat = field("IsolineGeometryFormat")

    @cached_property
    def IsolineGranularity(self):  # pragma: no cover
        return IsolineGranularityOptions.make_one(
            self.boto3_raw_data["IsolineGranularity"]
        )

    Key = field("Key")
    OptimizeIsolineFor = field("OptimizeIsolineFor")
    OptimizeRoutingFor = field("OptimizeRoutingFor")
    Origin = field("Origin")

    @cached_property
    def OriginOptions(self):  # pragma: no cover
        return IsolineOriginOptions.make_one(self.boto3_raw_data["OriginOptions"])

    @cached_property
    def Traffic(self):  # pragma: no cover
        return IsolineTrafficOptions.make_one(self.boto3_raw_data["Traffic"])

    TravelMode = field("TravelMode")

    @cached_property
    def TravelModeOptions(self):  # pragma: no cover
        return IsolineTravelModeOptions.make_one(
            self.boto3_raw_data["TravelModeOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateIsolinesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateIsolinesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRoutesRequest:
    boto3_raw_data: "type_defs.CalculateRoutesRequestTypeDef" = dataclasses.field()

    Destination = field("Destination")
    Origin = field("Origin")

    @cached_property
    def Allow(self):  # pragma: no cover
        return RouteAllowOptions.make_one(self.boto3_raw_data["Allow"])

    ArrivalTime = field("ArrivalTime")

    @cached_property
    def Avoid(self):  # pragma: no cover
        return RouteAvoidanceOptions.make_one(self.boto3_raw_data["Avoid"])

    DepartNow = field("DepartNow")
    DepartureTime = field("DepartureTime")

    @cached_property
    def DestinationOptions(self):  # pragma: no cover
        return RouteDestinationOptions.make_one(
            self.boto3_raw_data["DestinationOptions"]
        )

    @cached_property
    def Driver(self):  # pragma: no cover
        return RouteDriverOptions.make_one(self.boto3_raw_data["Driver"])

    @cached_property
    def Exclude(self):  # pragma: no cover
        return RouteExclusionOptions.make_one(self.boto3_raw_data["Exclude"])

    InstructionsMeasurementSystem = field("InstructionsMeasurementSystem")
    Key = field("Key")
    Languages = field("Languages")
    LegAdditionalFeatures = field("LegAdditionalFeatures")
    LegGeometryFormat = field("LegGeometryFormat")
    MaxAlternatives = field("MaxAlternatives")
    OptimizeRoutingFor = field("OptimizeRoutingFor")

    @cached_property
    def OriginOptions(self):  # pragma: no cover
        return RouteOriginOptions.make_one(self.boto3_raw_data["OriginOptions"])

    SpanAdditionalFeatures = field("SpanAdditionalFeatures")

    @cached_property
    def Tolls(self):  # pragma: no cover
        return RouteTollOptions.make_one(self.boto3_raw_data["Tolls"])

    @cached_property
    def Traffic(self):  # pragma: no cover
        return RouteTrafficOptions.make_one(self.boto3_raw_data["Traffic"])

    TravelMode = field("TravelMode")

    @cached_property
    def TravelModeOptions(self):  # pragma: no cover
        return RouteTravelModeOptions.make_one(self.boto3_raw_data["TravelModeOptions"])

    TravelStepType = field("TravelStepType")

    @cached_property
    def Waypoints(self):  # pragma: no cover
        return RouteWaypoint.make_many(self.boto3_raw_data["Waypoints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateRoutesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRoutesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutePedestrianLegDetails:
    boto3_raw_data: "type_defs.RoutePedestrianLegDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Arrival(self):  # pragma: no cover
        return RoutePedestrianArrival.make_one(self.boto3_raw_data["Arrival"])

    @cached_property
    def Departure(self):  # pragma: no cover
        return RoutePedestrianDeparture.make_one(self.boto3_raw_data["Departure"])

    @cached_property
    def Notices(self):  # pragma: no cover
        return RoutePedestrianNotice.make_many(self.boto3_raw_data["Notices"])

    @cached_property
    def PassThroughWaypoints(self):  # pragma: no cover
        return RoutePassThroughWaypoint.make_many(
            self.boto3_raw_data["PassThroughWaypoints"]
        )

    @cached_property
    def Spans(self):  # pragma: no cover
        return RoutePedestrianSpan.make_many(self.boto3_raw_data["Spans"])

    @cached_property
    def TravelSteps(self):  # pragma: no cover
        return RoutePedestrianTravelStep.make_many(self.boto3_raw_data["TravelSteps"])

    @cached_property
    def Summary(self):  # pragma: no cover
        return RoutePedestrianSummary.make_one(self.boto3_raw_data["Summary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutePedestrianLegDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutePedestrianLegDetailsTypeDef"]
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

    @cached_property
    def Destinations(self):  # pragma: no cover
        return RouteMatrixDestination.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def Origins(self):  # pragma: no cover
        return RouteMatrixOrigin.make_many(self.boto3_raw_data["Origins"])

    RoutingBoundary = field("RoutingBoundary")

    @cached_property
    def Allow(self):  # pragma: no cover
        return RouteMatrixAllowOptions.make_one(self.boto3_raw_data["Allow"])

    @cached_property
    def Avoid(self):  # pragma: no cover
        return RouteMatrixAvoidanceOptions.make_one(self.boto3_raw_data["Avoid"])

    DepartNow = field("DepartNow")
    DepartureTime = field("DepartureTime")

    @cached_property
    def Exclude(self):  # pragma: no cover
        return RouteMatrixExclusionOptions.make_one(self.boto3_raw_data["Exclude"])

    Key = field("Key")
    OptimizeRoutingFor = field("OptimizeRoutingFor")

    @cached_property
    def Traffic(self):  # pragma: no cover
        return RouteMatrixTrafficOptions.make_one(self.boto3_raw_data["Traffic"])

    TravelMode = field("TravelMode")

    @cached_property
    def TravelModeOptions(self):  # pragma: no cover
        return RouteMatrixTravelModeOptions.make_one(
            self.boto3_raw_data["TravelModeOptions"]
        )

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
class RouteVehicleLegDetails:
    boto3_raw_data: "type_defs.RouteVehicleLegDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Arrival(self):  # pragma: no cover
        return RouteVehicleArrival.make_one(self.boto3_raw_data["Arrival"])

    @cached_property
    def Departure(self):  # pragma: no cover
        return RouteVehicleDeparture.make_one(self.boto3_raw_data["Departure"])

    @cached_property
    def Incidents(self):  # pragma: no cover
        return RouteVehicleIncident.make_many(self.boto3_raw_data["Incidents"])

    @cached_property
    def Notices(self):  # pragma: no cover
        return RouteVehicleNotice.make_many(self.boto3_raw_data["Notices"])

    @cached_property
    def PassThroughWaypoints(self):  # pragma: no cover
        return RoutePassThroughWaypoint.make_many(
            self.boto3_raw_data["PassThroughWaypoints"]
        )

    @cached_property
    def Spans(self):  # pragma: no cover
        return RouteVehicleSpan.make_many(self.boto3_raw_data["Spans"])

    @cached_property
    def Tolls(self):  # pragma: no cover
        return RouteToll.make_many(self.boto3_raw_data["Tolls"])

    @cached_property
    def TollSystems(self):  # pragma: no cover
        return RouteTollSystem.make_many(self.boto3_raw_data["TollSystems"])

    @cached_property
    def TravelSteps(self):  # pragma: no cover
        return RouteVehicleTravelStep.make_many(self.boto3_raw_data["TravelSteps"])

    TruckRoadTypes = field("TruckRoadTypes")

    @cached_property
    def Zones(self):  # pragma: no cover
        return RouteZone.make_many(self.boto3_raw_data["Zones"])

    @cached_property
    def Summary(self):  # pragma: no cover
        return RouteVehicleSummary.make_one(self.boto3_raw_data["Summary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteVehicleLegDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteVehicleLegDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteLeg:
    boto3_raw_data: "type_defs.RouteLegTypeDef" = dataclasses.field()

    @cached_property
    def Geometry(self):  # pragma: no cover
        return RouteLegGeometry.make_one(self.boto3_raw_data["Geometry"])

    TravelMode = field("TravelMode")
    Type = field("Type")

    @cached_property
    def FerryLegDetails(self):  # pragma: no cover
        return RouteFerryLegDetails.make_one(self.boto3_raw_data["FerryLegDetails"])

    Language = field("Language")

    @cached_property
    def PedestrianLegDetails(self):  # pragma: no cover
        return RoutePedestrianLegDetails.make_one(
            self.boto3_raw_data["PedestrianLegDetails"]
        )

    @cached_property
    def VehicleLegDetails(self):  # pragma: no cover
        return RouteVehicleLegDetails.make_one(self.boto3_raw_data["VehicleLegDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteLegTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteLegTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Route:
    boto3_raw_data: "type_defs.RouteTypeDef" = dataclasses.field()

    @cached_property
    def Legs(self):  # pragma: no cover
        return RouteLeg.make_many(self.boto3_raw_data["Legs"])

    @cached_property
    def MajorRoadLabels(self):  # pragma: no cover
        return RouteMajorRoadLabel.make_many(self.boto3_raw_data["MajorRoadLabels"])

    @cached_property
    def Summary(self):  # pragma: no cover
        return RouteSummary.make_one(self.boto3_raw_data["Summary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculateRoutesResponse:
    boto3_raw_data: "type_defs.CalculateRoutesResponseTypeDef" = dataclasses.field()

    LegGeometryFormat = field("LegGeometryFormat")

    @cached_property
    def Notices(self):  # pragma: no cover
        return RouteResponseNotice.make_many(self.boto3_raw_data["Notices"])

    PricingBucket = field("PricingBucket")

    @cached_property
    def Routes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["Routes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculateRoutesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculateRoutesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
