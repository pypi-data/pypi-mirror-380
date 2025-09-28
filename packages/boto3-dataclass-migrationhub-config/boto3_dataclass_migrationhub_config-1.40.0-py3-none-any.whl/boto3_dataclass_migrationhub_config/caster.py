# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_migrationhub_config import type_defs as bs_td


class MIGRATIONHUB_CONFIGCaster:

    def create_home_region_control(
        self,
        res: "bs_td.CreateHomeRegionControlResultTypeDef",
    ) -> "dc_td.CreateHomeRegionControlResult":
        return dc_td.CreateHomeRegionControlResult.make_one(res)

    def describe_home_region_controls(
        self,
        res: "bs_td.DescribeHomeRegionControlsResultTypeDef",
    ) -> "dc_td.DescribeHomeRegionControlsResult":
        return dc_td.DescribeHomeRegionControlsResult.make_one(res)

    def get_home_region(
        self,
        res: "bs_td.GetHomeRegionResultTypeDef",
    ) -> "dc_td.GetHomeRegionResult":
        return dc_td.GetHomeRegionResult.make_one(res)


migrationhub_config_caster = MIGRATIONHUB_CONFIGCaster()
