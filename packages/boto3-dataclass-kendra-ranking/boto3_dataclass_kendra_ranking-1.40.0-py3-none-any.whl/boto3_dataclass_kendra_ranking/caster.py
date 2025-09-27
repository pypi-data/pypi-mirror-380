# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kendra_ranking import type_defs as bs_td


class KENDRA_RANKINGCaster:

    def create_rescore_execution_plan(
        self,
        res: "bs_td.CreateRescoreExecutionPlanResponseTypeDef",
    ) -> "dc_td.CreateRescoreExecutionPlanResponse":
        return dc_td.CreateRescoreExecutionPlanResponse.make_one(res)

    def delete_rescore_execution_plan(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_rescore_execution_plan(
        self,
        res: "bs_td.DescribeRescoreExecutionPlanResponseTypeDef",
    ) -> "dc_td.DescribeRescoreExecutionPlanResponse":
        return dc_td.DescribeRescoreExecutionPlanResponse.make_one(res)

    def list_rescore_execution_plans(
        self,
        res: "bs_td.ListRescoreExecutionPlansResponseTypeDef",
    ) -> "dc_td.ListRescoreExecutionPlansResponse":
        return dc_td.ListRescoreExecutionPlansResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def rescore(
        self,
        res: "bs_td.RescoreResultTypeDef",
    ) -> "dc_td.RescoreResult":
        return dc_td.RescoreResult.make_one(res)

    def update_rescore_execution_plan(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


kendra_ranking_caster = KENDRA_RANKINGCaster()
