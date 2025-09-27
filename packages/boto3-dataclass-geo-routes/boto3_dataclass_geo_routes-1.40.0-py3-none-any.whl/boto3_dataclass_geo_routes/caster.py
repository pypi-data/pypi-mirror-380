# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_geo_routes import type_defs as bs_td


class GEO_ROUTESCaster:

    def calculate_isolines(
        self,
        res: "bs_td.CalculateIsolinesResponseTypeDef",
    ) -> "dc_td.CalculateIsolinesResponse":
        return dc_td.CalculateIsolinesResponse.make_one(res)

    def calculate_route_matrix(
        self,
        res: "bs_td.CalculateRouteMatrixResponseTypeDef",
    ) -> "dc_td.CalculateRouteMatrixResponse":
        return dc_td.CalculateRouteMatrixResponse.make_one(res)

    def calculate_routes(
        self,
        res: "bs_td.CalculateRoutesResponseTypeDef",
    ) -> "dc_td.CalculateRoutesResponse":
        return dc_td.CalculateRoutesResponse.make_one(res)

    def optimize_waypoints(
        self,
        res: "bs_td.OptimizeWaypointsResponseTypeDef",
    ) -> "dc_td.OptimizeWaypointsResponse":
        return dc_td.OptimizeWaypointsResponse.make_one(res)

    def snap_to_roads(
        self,
        res: "bs_td.SnapToRoadsResponseTypeDef",
    ) -> "dc_td.SnapToRoadsResponse":
        return dc_td.SnapToRoadsResponse.make_one(res)


geo_routes_caster = GEO_ROUTESCaster()
