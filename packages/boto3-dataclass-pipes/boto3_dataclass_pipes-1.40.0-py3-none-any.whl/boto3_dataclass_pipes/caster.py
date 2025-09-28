# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pipes import type_defs as bs_td


class PIPESCaster:

    def create_pipe(
        self,
        res: "bs_td.CreatePipeResponseTypeDef",
    ) -> "dc_td.CreatePipeResponse":
        return dc_td.CreatePipeResponse.make_one(res)

    def delete_pipe(
        self,
        res: "bs_td.DeletePipeResponseTypeDef",
    ) -> "dc_td.DeletePipeResponse":
        return dc_td.DeletePipeResponse.make_one(res)

    def describe_pipe(
        self,
        res: "bs_td.DescribePipeResponseTypeDef",
    ) -> "dc_td.DescribePipeResponse":
        return dc_td.DescribePipeResponse.make_one(res)

    def list_pipes(
        self,
        res: "bs_td.ListPipesResponseTypeDef",
    ) -> "dc_td.ListPipesResponse":
        return dc_td.ListPipesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_pipe(
        self,
        res: "bs_td.StartPipeResponseTypeDef",
    ) -> "dc_td.StartPipeResponse":
        return dc_td.StartPipeResponse.make_one(res)

    def stop_pipe(
        self,
        res: "bs_td.StopPipeResponseTypeDef",
    ) -> "dc_td.StopPipeResponse":
        return dc_td.StopPipeResponse.make_one(res)

    def update_pipe(
        self,
        res: "bs_td.UpdatePipeResponseTypeDef",
    ) -> "dc_td.UpdatePipeResponse":
        return dc_td.UpdatePipeResponse.make_one(res)


pipes_caster = PIPESCaster()
