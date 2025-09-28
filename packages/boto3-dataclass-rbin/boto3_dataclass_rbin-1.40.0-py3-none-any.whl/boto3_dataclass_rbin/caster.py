# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rbin import type_defs as bs_td


class RBINCaster:

    def create_rule(
        self,
        res: "bs_td.CreateRuleResponseTypeDef",
    ) -> "dc_td.CreateRuleResponse":
        return dc_td.CreateRuleResponse.make_one(res)

    def get_rule(
        self,
        res: "bs_td.GetRuleResponseTypeDef",
    ) -> "dc_td.GetRuleResponse":
        return dc_td.GetRuleResponse.make_one(res)

    def list_rules(
        self,
        res: "bs_td.ListRulesResponseTypeDef",
    ) -> "dc_td.ListRulesResponse":
        return dc_td.ListRulesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def lock_rule(
        self,
        res: "bs_td.LockRuleResponseTypeDef",
    ) -> "dc_td.LockRuleResponse":
        return dc_td.LockRuleResponse.make_one(res)

    def unlock_rule(
        self,
        res: "bs_td.UnlockRuleResponseTypeDef",
    ) -> "dc_td.UnlockRuleResponse":
        return dc_td.UnlockRuleResponse.make_one(res)

    def update_rule(
        self,
        res: "bs_td.UpdateRuleResponseTypeDef",
    ) -> "dc_td.UpdateRuleResponse":
        return dc_td.UpdateRuleResponse.make_one(res)


rbin_caster = RBINCaster()
