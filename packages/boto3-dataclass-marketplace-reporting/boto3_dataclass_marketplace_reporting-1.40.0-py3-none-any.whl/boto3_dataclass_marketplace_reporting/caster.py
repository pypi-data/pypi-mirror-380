# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_marketplace_reporting import type_defs as bs_td


class MARKETPLACE_REPORTINGCaster:

    def get_buyer_dashboard(
        self,
        res: "bs_td.GetBuyerDashboardOutputTypeDef",
    ) -> "dc_td.GetBuyerDashboardOutput":
        return dc_td.GetBuyerDashboardOutput.make_one(res)


marketplace_reporting_caster = MARKETPLACE_REPORTINGCaster()
