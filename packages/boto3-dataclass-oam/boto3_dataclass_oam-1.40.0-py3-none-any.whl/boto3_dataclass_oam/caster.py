# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_oam import type_defs as bs_td


class OAMCaster:

    def create_link(
        self,
        res: "bs_td.CreateLinkOutputTypeDef",
    ) -> "dc_td.CreateLinkOutput":
        return dc_td.CreateLinkOutput.make_one(res)

    def create_sink(
        self,
        res: "bs_td.CreateSinkOutputTypeDef",
    ) -> "dc_td.CreateSinkOutput":
        return dc_td.CreateSinkOutput.make_one(res)

    def get_link(
        self,
        res: "bs_td.GetLinkOutputTypeDef",
    ) -> "dc_td.GetLinkOutput":
        return dc_td.GetLinkOutput.make_one(res)

    def get_sink(
        self,
        res: "bs_td.GetSinkOutputTypeDef",
    ) -> "dc_td.GetSinkOutput":
        return dc_td.GetSinkOutput.make_one(res)

    def get_sink_policy(
        self,
        res: "bs_td.GetSinkPolicyOutputTypeDef",
    ) -> "dc_td.GetSinkPolicyOutput":
        return dc_td.GetSinkPolicyOutput.make_one(res)

    def list_attached_links(
        self,
        res: "bs_td.ListAttachedLinksOutputTypeDef",
    ) -> "dc_td.ListAttachedLinksOutput":
        return dc_td.ListAttachedLinksOutput.make_one(res)

    def list_links(
        self,
        res: "bs_td.ListLinksOutputTypeDef",
    ) -> "dc_td.ListLinksOutput":
        return dc_td.ListLinksOutput.make_one(res)

    def list_sinks(
        self,
        res: "bs_td.ListSinksOutputTypeDef",
    ) -> "dc_td.ListSinksOutput":
        return dc_td.ListSinksOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def put_sink_policy(
        self,
        res: "bs_td.PutSinkPolicyOutputTypeDef",
    ) -> "dc_td.PutSinkPolicyOutput":
        return dc_td.PutSinkPolicyOutput.make_one(res)

    def update_link(
        self,
        res: "bs_td.UpdateLinkOutputTypeDef",
    ) -> "dc_td.UpdateLinkOutput":
        return dc_td.UpdateLinkOutput.make_one(res)


oam_caster = OAMCaster()
