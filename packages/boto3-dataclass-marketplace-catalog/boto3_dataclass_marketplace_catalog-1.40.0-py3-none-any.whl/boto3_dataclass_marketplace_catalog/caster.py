# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_marketplace_catalog import type_defs as bs_td


class MARKETPLACE_CATALOGCaster:

    def batch_describe_entities(
        self,
        res: "bs_td.BatchDescribeEntitiesResponseTypeDef",
    ) -> "dc_td.BatchDescribeEntitiesResponse":
        return dc_td.BatchDescribeEntitiesResponse.make_one(res)

    def cancel_change_set(
        self,
        res: "bs_td.CancelChangeSetResponseTypeDef",
    ) -> "dc_td.CancelChangeSetResponse":
        return dc_td.CancelChangeSetResponse.make_one(res)

    def describe_change_set(
        self,
        res: "bs_td.DescribeChangeSetResponseTypeDef",
    ) -> "dc_td.DescribeChangeSetResponse":
        return dc_td.DescribeChangeSetResponse.make_one(res)

    def describe_entity(
        self,
        res: "bs_td.DescribeEntityResponseTypeDef",
    ) -> "dc_td.DescribeEntityResponse":
        return dc_td.DescribeEntityResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def list_change_sets(
        self,
        res: "bs_td.ListChangeSetsResponseTypeDef",
    ) -> "dc_td.ListChangeSetsResponse":
        return dc_td.ListChangeSetsResponse.make_one(res)

    def list_entities(
        self,
        res: "bs_td.ListEntitiesResponseTypeDef",
    ) -> "dc_td.ListEntitiesResponse":
        return dc_td.ListEntitiesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_change_set(
        self,
        res: "bs_td.StartChangeSetResponseTypeDef",
    ) -> "dc_td.StartChangeSetResponse":
        return dc_td.StartChangeSetResponse.make_one(res)


marketplace_catalog_caster = MARKETPLACE_CATALOGCaster()
