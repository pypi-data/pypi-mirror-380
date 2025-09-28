# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediastore import type_defs as bs_td


class MEDIASTORECaster:

    def create_container(
        self,
        res: "bs_td.CreateContainerOutputTypeDef",
    ) -> "dc_td.CreateContainerOutput":
        return dc_td.CreateContainerOutput.make_one(res)

    def describe_container(
        self,
        res: "bs_td.DescribeContainerOutputTypeDef",
    ) -> "dc_td.DescribeContainerOutput":
        return dc_td.DescribeContainerOutput.make_one(res)

    def get_container_policy(
        self,
        res: "bs_td.GetContainerPolicyOutputTypeDef",
    ) -> "dc_td.GetContainerPolicyOutput":
        return dc_td.GetContainerPolicyOutput.make_one(res)

    def get_cors_policy(
        self,
        res: "bs_td.GetCorsPolicyOutputTypeDef",
    ) -> "dc_td.GetCorsPolicyOutput":
        return dc_td.GetCorsPolicyOutput.make_one(res)

    def get_lifecycle_policy(
        self,
        res: "bs_td.GetLifecyclePolicyOutputTypeDef",
    ) -> "dc_td.GetLifecyclePolicyOutput":
        return dc_td.GetLifecyclePolicyOutput.make_one(res)

    def get_metric_policy(
        self,
        res: "bs_td.GetMetricPolicyOutputTypeDef",
    ) -> "dc_td.GetMetricPolicyOutput":
        return dc_td.GetMetricPolicyOutput.make_one(res)

    def list_containers(
        self,
        res: "bs_td.ListContainersOutputTypeDef",
    ) -> "dc_td.ListContainersOutput":
        return dc_td.ListContainersOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)


mediastore_caster = MEDIASTORECaster()
