# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_resourcegroupstaggingapi import type_defs as bs_td


class RESOURCEGROUPSTAGGINGAPICaster:

    def describe_report_creation(
        self,
        res: "bs_td.DescribeReportCreationOutputTypeDef",
    ) -> "dc_td.DescribeReportCreationOutput":
        return dc_td.DescribeReportCreationOutput.make_one(res)

    def get_compliance_summary(
        self,
        res: "bs_td.GetComplianceSummaryOutputTypeDef",
    ) -> "dc_td.GetComplianceSummaryOutput":
        return dc_td.GetComplianceSummaryOutput.make_one(res)

    def get_resources(
        self,
        res: "bs_td.GetResourcesOutputTypeDef",
    ) -> "dc_td.GetResourcesOutput":
        return dc_td.GetResourcesOutput.make_one(res)

    def get_tag_keys(
        self,
        res: "bs_td.GetTagKeysOutputTypeDef",
    ) -> "dc_td.GetTagKeysOutput":
        return dc_td.GetTagKeysOutput.make_one(res)

    def get_tag_values(
        self,
        res: "bs_td.GetTagValuesOutputTypeDef",
    ) -> "dc_td.GetTagValuesOutput":
        return dc_td.GetTagValuesOutput.make_one(res)

    def tag_resources(
        self,
        res: "bs_td.TagResourcesOutputTypeDef",
    ) -> "dc_td.TagResourcesOutput":
        return dc_td.TagResourcesOutput.make_one(res)

    def untag_resources(
        self,
        res: "bs_td.UntagResourcesOutputTypeDef",
    ) -> "dc_td.UntagResourcesOutput":
        return dc_td.UntagResourcesOutput.make_one(res)


resourcegroupstaggingapi_caster = RESOURCEGROUPSTAGGINGAPICaster()
