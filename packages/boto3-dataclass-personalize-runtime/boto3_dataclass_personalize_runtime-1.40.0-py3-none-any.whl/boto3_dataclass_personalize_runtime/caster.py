# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_personalize_runtime import type_defs as bs_td


class PERSONALIZE_RUNTIMECaster:

    def get_action_recommendations(
        self,
        res: "bs_td.GetActionRecommendationsResponseTypeDef",
    ) -> "dc_td.GetActionRecommendationsResponse":
        return dc_td.GetActionRecommendationsResponse.make_one(res)

    def get_personalized_ranking(
        self,
        res: "bs_td.GetPersonalizedRankingResponseTypeDef",
    ) -> "dc_td.GetPersonalizedRankingResponse":
        return dc_td.GetPersonalizedRankingResponse.make_one(res)

    def get_recommendations(
        self,
        res: "bs_td.GetRecommendationsResponseTypeDef",
    ) -> "dc_td.GetRecommendationsResponse":
        return dc_td.GetRecommendationsResponse.make_one(res)


personalize_runtime_caster = PERSONALIZE_RUNTIMECaster()
