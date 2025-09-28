# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53_recovery_cluster import type_defs as bs_td


class ROUTE53_RECOVERY_CLUSTERCaster:

    def get_routing_control_state(
        self,
        res: "bs_td.GetRoutingControlStateResponseTypeDef",
    ) -> "dc_td.GetRoutingControlStateResponse":
        return dc_td.GetRoutingControlStateResponse.make_one(res)

    def list_routing_controls(
        self,
        res: "bs_td.ListRoutingControlsResponseTypeDef",
    ) -> "dc_td.ListRoutingControlsResponse":
        return dc_td.ListRoutingControlsResponse.make_one(res)


route53_recovery_cluster_caster = ROUTE53_RECOVERY_CLUSTERCaster()
