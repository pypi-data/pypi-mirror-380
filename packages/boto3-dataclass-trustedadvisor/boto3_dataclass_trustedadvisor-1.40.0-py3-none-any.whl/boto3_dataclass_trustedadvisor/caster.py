# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_trustedadvisor import type_defs as bs_td


class TRUSTEDADVISORCaster:

    def batch_update_recommendation_resource_exclusion(
        self,
        res: "bs_td.BatchUpdateRecommendationResourceExclusionResponseTypeDef",
    ) -> "dc_td.BatchUpdateRecommendationResourceExclusionResponse":
        return dc_td.BatchUpdateRecommendationResourceExclusionResponse.make_one(res)

    def get_organization_recommendation(
        self,
        res: "bs_td.GetOrganizationRecommendationResponseTypeDef",
    ) -> "dc_td.GetOrganizationRecommendationResponse":
        return dc_td.GetOrganizationRecommendationResponse.make_one(res)

    def get_recommendation(
        self,
        res: "bs_td.GetRecommendationResponseTypeDef",
    ) -> "dc_td.GetRecommendationResponse":
        return dc_td.GetRecommendationResponse.make_one(res)

    def list_checks(
        self,
        res: "bs_td.ListChecksResponseTypeDef",
    ) -> "dc_td.ListChecksResponse":
        return dc_td.ListChecksResponse.make_one(res)

    def list_organization_recommendation_accounts(
        self,
        res: "bs_td.ListOrganizationRecommendationAccountsResponseTypeDef",
    ) -> "dc_td.ListOrganizationRecommendationAccountsResponse":
        return dc_td.ListOrganizationRecommendationAccountsResponse.make_one(res)

    def list_organization_recommendation_resources(
        self,
        res: "bs_td.ListOrganizationRecommendationResourcesResponseTypeDef",
    ) -> "dc_td.ListOrganizationRecommendationResourcesResponse":
        return dc_td.ListOrganizationRecommendationResourcesResponse.make_one(res)

    def list_organization_recommendations(
        self,
        res: "bs_td.ListOrganizationRecommendationsResponseTypeDef",
    ) -> "dc_td.ListOrganizationRecommendationsResponse":
        return dc_td.ListOrganizationRecommendationsResponse.make_one(res)

    def list_recommendation_resources(
        self,
        res: "bs_td.ListRecommendationResourcesResponseTypeDef",
    ) -> "dc_td.ListRecommendationResourcesResponse":
        return dc_td.ListRecommendationResourcesResponse.make_one(res)

    def list_recommendations(
        self,
        res: "bs_td.ListRecommendationsResponseTypeDef",
    ) -> "dc_td.ListRecommendationsResponse":
        return dc_td.ListRecommendationsResponse.make_one(res)

    def update_organization_recommendation_lifecycle(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_recommendation_lifecycle(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


trustedadvisor_caster = TRUSTEDADVISORCaster()
