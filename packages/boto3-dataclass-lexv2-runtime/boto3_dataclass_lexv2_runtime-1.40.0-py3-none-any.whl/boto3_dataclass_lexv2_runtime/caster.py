# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lexv2_runtime import type_defs as bs_td


class LEXV2_RUNTIMECaster:

    def delete_session(
        self,
        res: "bs_td.DeleteSessionResponseTypeDef",
    ) -> "dc_td.DeleteSessionResponse":
        return dc_td.DeleteSessionResponse.make_one(res)

    def get_session(
        self,
        res: "bs_td.GetSessionResponseTypeDef",
    ) -> "dc_td.GetSessionResponse":
        return dc_td.GetSessionResponse.make_one(res)

    def put_session(
        self,
        res: "bs_td.PutSessionResponseTypeDef",
    ) -> "dc_td.PutSessionResponse":
        return dc_td.PutSessionResponse.make_one(res)

    def recognize_text(
        self,
        res: "bs_td.RecognizeTextResponseTypeDef",
    ) -> "dc_td.RecognizeTextResponse":
        return dc_td.RecognizeTextResponse.make_one(res)

    def recognize_utterance(
        self,
        res: "bs_td.RecognizeUtteranceResponseTypeDef",
    ) -> "dc_td.RecognizeUtteranceResponse":
        return dc_td.RecognizeUtteranceResponse.make_one(res)

    def start_conversation(
        self,
        res: "bs_td.StartConversationResponseTypeDef",
    ) -> "dc_td.StartConversationResponse":
        return dc_td.StartConversationResponse.make_one(res)


lexv2_runtime_caster = LEXV2_RUNTIMECaster()
