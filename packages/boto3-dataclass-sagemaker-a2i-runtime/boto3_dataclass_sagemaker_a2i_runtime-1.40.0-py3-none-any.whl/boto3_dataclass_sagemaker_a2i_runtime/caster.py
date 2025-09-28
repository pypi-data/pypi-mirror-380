# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_a2i_runtime import type_defs as bs_td


class SAGEMAKER_A2I_RUNTIMECaster:

    def describe_human_loop(
        self,
        res: "bs_td.DescribeHumanLoopResponseTypeDef",
    ) -> "dc_td.DescribeHumanLoopResponse":
        return dc_td.DescribeHumanLoopResponse.make_one(res)

    def list_human_loops(
        self,
        res: "bs_td.ListHumanLoopsResponseTypeDef",
    ) -> "dc_td.ListHumanLoopsResponse":
        return dc_td.ListHumanLoopsResponse.make_one(res)

    def start_human_loop(
        self,
        res: "bs_td.StartHumanLoopResponseTypeDef",
    ) -> "dc_td.StartHumanLoopResponse":
        return dc_td.StartHumanLoopResponse.make_one(res)


sagemaker_a2i_runtime_caster = SAGEMAKER_A2I_RUNTIMECaster()
