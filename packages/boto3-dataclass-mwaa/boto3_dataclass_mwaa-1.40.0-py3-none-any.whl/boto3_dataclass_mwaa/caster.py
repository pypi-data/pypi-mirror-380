# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mwaa import type_defs as bs_td


class MWAACaster:

    def create_cli_token(
        self,
        res: "bs_td.CreateCliTokenResponseTypeDef",
    ) -> "dc_td.CreateCliTokenResponse":
        return dc_td.CreateCliTokenResponse.make_one(res)

    def create_environment(
        self,
        res: "bs_td.CreateEnvironmentOutputTypeDef",
    ) -> "dc_td.CreateEnvironmentOutput":
        return dc_td.CreateEnvironmentOutput.make_one(res)

    def create_web_login_token(
        self,
        res: "bs_td.CreateWebLoginTokenResponseTypeDef",
    ) -> "dc_td.CreateWebLoginTokenResponse":
        return dc_td.CreateWebLoginTokenResponse.make_one(res)

    def get_environment(
        self,
        res: "bs_td.GetEnvironmentOutputTypeDef",
    ) -> "dc_td.GetEnvironmentOutput":
        return dc_td.GetEnvironmentOutput.make_one(res)

    def invoke_rest_api(
        self,
        res: "bs_td.InvokeRestApiResponseTypeDef",
    ) -> "dc_td.InvokeRestApiResponse":
        return dc_td.InvokeRestApiResponse.make_one(res)

    def list_environments(
        self,
        res: "bs_td.ListEnvironmentsOutputTypeDef",
    ) -> "dc_td.ListEnvironmentsOutput":
        return dc_td.ListEnvironmentsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def update_environment(
        self,
        res: "bs_td.UpdateEnvironmentOutputTypeDef",
    ) -> "dc_td.UpdateEnvironmentOutput":
        return dc_td.UpdateEnvironmentOutput.make_one(res)


mwaa_caster = MWAACaster()
