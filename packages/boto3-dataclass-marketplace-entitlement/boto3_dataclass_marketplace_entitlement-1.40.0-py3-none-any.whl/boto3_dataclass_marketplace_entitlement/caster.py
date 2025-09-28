# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_marketplace_entitlement import type_defs as bs_td


class MARKETPLACE_ENTITLEMENTCaster:

    def get_entitlements(
        self,
        res: "bs_td.GetEntitlementsResultTypeDef",
    ) -> "dc_td.GetEntitlementsResult":
        return dc_td.GetEntitlementsResult.make_one(res)


marketplace_entitlement_caster = MARKETPLACE_ENTITLEMENTCaster()
