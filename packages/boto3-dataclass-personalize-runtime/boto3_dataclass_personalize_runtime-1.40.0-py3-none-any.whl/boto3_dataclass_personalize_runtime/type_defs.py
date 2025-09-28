# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_personalize_runtime import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class GetActionRecommendationsRequest:
    boto3_raw_data: "type_defs.GetActionRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    campaignArn = field("campaignArn")
    userId = field("userId")
    numResults = field("numResults")
    filterArn = field("filterArn")
    filterValues = field("filterValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetActionRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActionRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictedAction:
    boto3_raw_data: "type_defs.PredictedActionTypeDef" = dataclasses.field()

    actionId = field("actionId")
    score = field("score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictedActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredictedActionTypeDef"]],
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
class GetPersonalizedRankingRequest:
    boto3_raw_data: "type_defs.GetPersonalizedRankingRequestTypeDef" = (
        dataclasses.field()
    )

    campaignArn = field("campaignArn")
    inputList = field("inputList")
    userId = field("userId")
    context = field("context")
    filterArn = field("filterArn")
    filterValues = field("filterValues")
    metadataColumns = field("metadataColumns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPersonalizedRankingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPersonalizedRankingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictedItem:
    boto3_raw_data: "type_defs.PredictedItemTypeDef" = dataclasses.field()

    itemId = field("itemId")
    score = field("score")
    promotionName = field("promotionName")
    metadata = field("metadata")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictedItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredictedItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Promotion:
    boto3_raw_data: "type_defs.PromotionTypeDef" = dataclasses.field()

    name = field("name")
    percentPromotedItems = field("percentPromotedItems")
    filterArn = field("filterArn")
    filterValues = field("filterValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromotionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromotionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetActionRecommendationsResponse:
    boto3_raw_data: "type_defs.GetActionRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def actionList(self):  # pragma: no cover
        return PredictedAction.make_many(self.boto3_raw_data["actionList"])

    recommendationId = field("recommendationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetActionRecommendationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActionRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPersonalizedRankingResponse:
    boto3_raw_data: "type_defs.GetPersonalizedRankingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def personalizedRanking(self):  # pragma: no cover
        return PredictedItem.make_many(self.boto3_raw_data["personalizedRanking"])

    recommendationId = field("recommendationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPersonalizedRankingResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPersonalizedRankingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationsResponse:
    boto3_raw_data: "type_defs.GetRecommendationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def itemList(self):  # pragma: no cover
        return PredictedItem.make_many(self.boto3_raw_data["itemList"])

    recommendationId = field("recommendationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationsRequest:
    boto3_raw_data: "type_defs.GetRecommendationsRequestTypeDef" = dataclasses.field()

    campaignArn = field("campaignArn")
    itemId = field("itemId")
    userId = field("userId")
    numResults = field("numResults")
    context = field("context")
    filterArn = field("filterArn")
    filterValues = field("filterValues")
    recommenderArn = field("recommenderArn")

    @cached_property
    def promotions(self):  # pragma: no cover
        return Promotion.make_many(self.boto3_raw_data["promotions"])

    metadataColumns = field("metadataColumns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
