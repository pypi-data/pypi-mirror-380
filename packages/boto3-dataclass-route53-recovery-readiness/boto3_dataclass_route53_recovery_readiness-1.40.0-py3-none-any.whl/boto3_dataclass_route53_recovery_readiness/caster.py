# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53_recovery_readiness import type_defs as bs_td


class ROUTE53_RECOVERY_READINESSCaster:

    def create_cell(
        self,
        res: "bs_td.CreateCellResponseTypeDef",
    ) -> "dc_td.CreateCellResponse":
        return dc_td.CreateCellResponse.make_one(res)

    def create_cross_account_authorization(
        self,
        res: "bs_td.CreateCrossAccountAuthorizationResponseTypeDef",
    ) -> "dc_td.CreateCrossAccountAuthorizationResponse":
        return dc_td.CreateCrossAccountAuthorizationResponse.make_one(res)

    def create_readiness_check(
        self,
        res: "bs_td.CreateReadinessCheckResponseTypeDef",
    ) -> "dc_td.CreateReadinessCheckResponse":
        return dc_td.CreateReadinessCheckResponse.make_one(res)

    def create_recovery_group(
        self,
        res: "bs_td.CreateRecoveryGroupResponseTypeDef",
    ) -> "dc_td.CreateRecoveryGroupResponse":
        return dc_td.CreateRecoveryGroupResponse.make_one(res)

    def create_resource_set(
        self,
        res: "bs_td.CreateResourceSetResponseTypeDef",
    ) -> "dc_td.CreateResourceSetResponse":
        return dc_td.CreateResourceSetResponse.make_one(res)

    def delete_cell(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_readiness_check(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_recovery_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_set(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_architecture_recommendations(
        self,
        res: "bs_td.GetArchitectureRecommendationsResponseTypeDef",
    ) -> "dc_td.GetArchitectureRecommendationsResponse":
        return dc_td.GetArchitectureRecommendationsResponse.make_one(res)

    def get_cell(
        self,
        res: "bs_td.GetCellResponseTypeDef",
    ) -> "dc_td.GetCellResponse":
        return dc_td.GetCellResponse.make_one(res)

    def get_cell_readiness_summary(
        self,
        res: "bs_td.GetCellReadinessSummaryResponseTypeDef",
    ) -> "dc_td.GetCellReadinessSummaryResponse":
        return dc_td.GetCellReadinessSummaryResponse.make_one(res)

    def get_readiness_check(
        self,
        res: "bs_td.GetReadinessCheckResponseTypeDef",
    ) -> "dc_td.GetReadinessCheckResponse":
        return dc_td.GetReadinessCheckResponse.make_one(res)

    def get_readiness_check_resource_status(
        self,
        res: "bs_td.GetReadinessCheckResourceStatusResponseTypeDef",
    ) -> "dc_td.GetReadinessCheckResourceStatusResponse":
        return dc_td.GetReadinessCheckResourceStatusResponse.make_one(res)

    def get_readiness_check_status(
        self,
        res: "bs_td.GetReadinessCheckStatusResponseTypeDef",
    ) -> "dc_td.GetReadinessCheckStatusResponse":
        return dc_td.GetReadinessCheckStatusResponse.make_one(res)

    def get_recovery_group(
        self,
        res: "bs_td.GetRecoveryGroupResponseTypeDef",
    ) -> "dc_td.GetRecoveryGroupResponse":
        return dc_td.GetRecoveryGroupResponse.make_one(res)

    def get_recovery_group_readiness_summary(
        self,
        res: "bs_td.GetRecoveryGroupReadinessSummaryResponseTypeDef",
    ) -> "dc_td.GetRecoveryGroupReadinessSummaryResponse":
        return dc_td.GetRecoveryGroupReadinessSummaryResponse.make_one(res)

    def get_resource_set(
        self,
        res: "bs_td.GetResourceSetResponseTypeDef",
    ) -> "dc_td.GetResourceSetResponse":
        return dc_td.GetResourceSetResponse.make_one(res)

    def list_cells(
        self,
        res: "bs_td.ListCellsResponseTypeDef",
    ) -> "dc_td.ListCellsResponse":
        return dc_td.ListCellsResponse.make_one(res)

    def list_cross_account_authorizations(
        self,
        res: "bs_td.ListCrossAccountAuthorizationsResponseTypeDef",
    ) -> "dc_td.ListCrossAccountAuthorizationsResponse":
        return dc_td.ListCrossAccountAuthorizationsResponse.make_one(res)

    def list_readiness_checks(
        self,
        res: "bs_td.ListReadinessChecksResponseTypeDef",
    ) -> "dc_td.ListReadinessChecksResponse":
        return dc_td.ListReadinessChecksResponse.make_one(res)

    def list_recovery_groups(
        self,
        res: "bs_td.ListRecoveryGroupsResponseTypeDef",
    ) -> "dc_td.ListRecoveryGroupsResponse":
        return dc_td.ListRecoveryGroupsResponse.make_one(res)

    def list_resource_sets(
        self,
        res: "bs_td.ListResourceSetsResponseTypeDef",
    ) -> "dc_td.ListResourceSetsResponse":
        return dc_td.ListResourceSetsResponse.make_one(res)

    def list_rules(
        self,
        res: "bs_td.ListRulesResponseTypeDef",
    ) -> "dc_td.ListRulesResponse":
        return dc_td.ListRulesResponse.make_one(res)

    def list_tags_for_resources(
        self,
        res: "bs_td.ListTagsForResourcesResponseTypeDef",
    ) -> "dc_td.ListTagsForResourcesResponse":
        return dc_td.ListTagsForResourcesResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_cell(
        self,
        res: "bs_td.UpdateCellResponseTypeDef",
    ) -> "dc_td.UpdateCellResponse":
        return dc_td.UpdateCellResponse.make_one(res)

    def update_readiness_check(
        self,
        res: "bs_td.UpdateReadinessCheckResponseTypeDef",
    ) -> "dc_td.UpdateReadinessCheckResponse":
        return dc_td.UpdateReadinessCheckResponse.make_one(res)

    def update_recovery_group(
        self,
        res: "bs_td.UpdateRecoveryGroupResponseTypeDef",
    ) -> "dc_td.UpdateRecoveryGroupResponse":
        return dc_td.UpdateRecoveryGroupResponse.make_one(res)

    def update_resource_set(
        self,
        res: "bs_td.UpdateResourceSetResponseTypeDef",
    ) -> "dc_td.UpdateResourceSetResponse":
        return dc_td.UpdateResourceSetResponse.make_one(res)


route53_recovery_readiness_caster = ROUTE53_RECOVERY_READINESSCaster()
