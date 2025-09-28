# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_marketplace_deployment import type_defs as bs_td


class MARKETPLACE_DEPLOYMENTCaster:

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_deployment_parameter(
        self,
        res: "bs_td.PutDeploymentParameterResponseTypeDef",
    ) -> "dc_td.PutDeploymentParameterResponse":
        return dc_td.PutDeploymentParameterResponse.make_one(res)


marketplace_deployment_caster = MARKETPLACE_DEPLOYMENTCaster()
