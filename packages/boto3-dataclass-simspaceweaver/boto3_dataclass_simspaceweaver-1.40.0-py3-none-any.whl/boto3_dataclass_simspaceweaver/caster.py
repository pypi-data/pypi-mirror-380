# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_simspaceweaver import type_defs as bs_td


class SIMSPACEWEAVERCaster:

    def describe_app(
        self,
        res: "bs_td.DescribeAppOutputTypeDef",
    ) -> "dc_td.DescribeAppOutput":
        return dc_td.DescribeAppOutput.make_one(res)

    def describe_simulation(
        self,
        res: "bs_td.DescribeSimulationOutputTypeDef",
    ) -> "dc_td.DescribeSimulationOutput":
        return dc_td.DescribeSimulationOutput.make_one(res)

    def list_apps(
        self,
        res: "bs_td.ListAppsOutputTypeDef",
    ) -> "dc_td.ListAppsOutput":
        return dc_td.ListAppsOutput.make_one(res)

    def list_simulations(
        self,
        res: "bs_td.ListSimulationsOutputTypeDef",
    ) -> "dc_td.ListSimulationsOutput":
        return dc_td.ListSimulationsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def start_app(
        self,
        res: "bs_td.StartAppOutputTypeDef",
    ) -> "dc_td.StartAppOutput":
        return dc_td.StartAppOutput.make_one(res)

    def start_simulation(
        self,
        res: "bs_td.StartSimulationOutputTypeDef",
    ) -> "dc_td.StartSimulationOutput":
        return dc_td.StartSimulationOutput.make_one(res)


simspaceweaver_caster = SIMSPACEWEAVERCaster()
