# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workmailmessageflow import type_defs as bs_td


class WORKMAILMESSAGEFLOWCaster:

    def get_raw_message_content(
        self,
        res: "bs_td.GetRawMessageContentResponseTypeDef",
    ) -> "dc_td.GetRawMessageContentResponse":
        return dc_td.GetRawMessageContentResponse.make_one(res)


workmailmessageflow_caster = WORKMAILMESSAGEFLOWCaster()
