# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_meteringmarketplace import type_defs as bs_td


class METERINGMARKETPLACECaster:

    def batch_meter_usage(
        self,
        res: "bs_td.BatchMeterUsageResultTypeDef",
    ) -> "dc_td.BatchMeterUsageResult":
        return dc_td.BatchMeterUsageResult.make_one(res)

    def meter_usage(
        self,
        res: "bs_td.MeterUsageResultTypeDef",
    ) -> "dc_td.MeterUsageResult":
        return dc_td.MeterUsageResult.make_one(res)

    def register_usage(
        self,
        res: "bs_td.RegisterUsageResultTypeDef",
    ) -> "dc_td.RegisterUsageResult":
        return dc_td.RegisterUsageResult.make_one(res)

    def resolve_customer(
        self,
        res: "bs_td.ResolveCustomerResultTypeDef",
    ) -> "dc_td.ResolveCustomerResult":
        return dc_td.ResolveCustomerResult.make_one(res)


meteringmarketplace_caster = METERINGMARKETPLACECaster()
