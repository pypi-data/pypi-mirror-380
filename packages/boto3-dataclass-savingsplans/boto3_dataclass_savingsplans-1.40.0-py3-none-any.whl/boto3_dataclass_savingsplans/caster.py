# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_savingsplans import type_defs as bs_td


class SAVINGSPLANSCaster:

    def create_savings_plan(
        self,
        res: "bs_td.CreateSavingsPlanResponseTypeDef",
    ) -> "dc_td.CreateSavingsPlanResponse":
        return dc_td.CreateSavingsPlanResponse.make_one(res)

    def describe_savings_plan_rates(
        self,
        res: "bs_td.DescribeSavingsPlanRatesResponseTypeDef",
    ) -> "dc_td.DescribeSavingsPlanRatesResponse":
        return dc_td.DescribeSavingsPlanRatesResponse.make_one(res)

    def describe_savings_plans(
        self,
        res: "bs_td.DescribeSavingsPlansResponseTypeDef",
    ) -> "dc_td.DescribeSavingsPlansResponse":
        return dc_td.DescribeSavingsPlansResponse.make_one(res)

    def describe_savings_plans_offering_rates(
        self,
        res: "bs_td.DescribeSavingsPlansOfferingRatesResponseTypeDef",
    ) -> "dc_td.DescribeSavingsPlansOfferingRatesResponse":
        return dc_td.DescribeSavingsPlansOfferingRatesResponse.make_one(res)

    def describe_savings_plans_offerings(
        self,
        res: "bs_td.DescribeSavingsPlansOfferingsResponseTypeDef",
    ) -> "dc_td.DescribeSavingsPlansOfferingsResponse":
        return dc_td.DescribeSavingsPlansOfferingsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def return_savings_plan(
        self,
        res: "bs_td.ReturnSavingsPlanResponseTypeDef",
    ) -> "dc_td.ReturnSavingsPlanResponse":
        return dc_td.ReturnSavingsPlanResponse.make_one(res)


savingsplans_caster = SAVINGSPLANSCaster()
