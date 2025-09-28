# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_synthetics import type_defs as bs_td


class SYNTHETICSCaster:

    def create_canary(
        self,
        res: "bs_td.CreateCanaryResponseTypeDef",
    ) -> "dc_td.CreateCanaryResponse":
        return dc_td.CreateCanaryResponse.make_one(res)

    def create_group(
        self,
        res: "bs_td.CreateGroupResponseTypeDef",
    ) -> "dc_td.CreateGroupResponse":
        return dc_td.CreateGroupResponse.make_one(res)

    def describe_canaries(
        self,
        res: "bs_td.DescribeCanariesResponseTypeDef",
    ) -> "dc_td.DescribeCanariesResponse":
        return dc_td.DescribeCanariesResponse.make_one(res)

    def describe_canaries_last_run(
        self,
        res: "bs_td.DescribeCanariesLastRunResponseTypeDef",
    ) -> "dc_td.DescribeCanariesLastRunResponse":
        return dc_td.DescribeCanariesLastRunResponse.make_one(res)

    def describe_runtime_versions(
        self,
        res: "bs_td.DescribeRuntimeVersionsResponseTypeDef",
    ) -> "dc_td.DescribeRuntimeVersionsResponse":
        return dc_td.DescribeRuntimeVersionsResponse.make_one(res)

    def get_canary(
        self,
        res: "bs_td.GetCanaryResponseTypeDef",
    ) -> "dc_td.GetCanaryResponse":
        return dc_td.GetCanaryResponse.make_one(res)

    def get_canary_runs(
        self,
        res: "bs_td.GetCanaryRunsResponseTypeDef",
    ) -> "dc_td.GetCanaryRunsResponse":
        return dc_td.GetCanaryRunsResponse.make_one(res)

    def get_group(
        self,
        res: "bs_td.GetGroupResponseTypeDef",
    ) -> "dc_td.GetGroupResponse":
        return dc_td.GetGroupResponse.make_one(res)

    def list_associated_groups(
        self,
        res: "bs_td.ListAssociatedGroupsResponseTypeDef",
    ) -> "dc_td.ListAssociatedGroupsResponse":
        return dc_td.ListAssociatedGroupsResponse.make_one(res)

    def list_group_resources(
        self,
        res: "bs_td.ListGroupResourcesResponseTypeDef",
    ) -> "dc_td.ListGroupResourcesResponse":
        return dc_td.ListGroupResourcesResponse.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsResponseTypeDef",
    ) -> "dc_td.ListGroupsResponse":
        return dc_td.ListGroupsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_canary_dry_run(
        self,
        res: "bs_td.StartCanaryDryRunResponseTypeDef",
    ) -> "dc_td.StartCanaryDryRunResponse":
        return dc_td.StartCanaryDryRunResponse.make_one(res)


synthetics_caster = SYNTHETICSCaster()
