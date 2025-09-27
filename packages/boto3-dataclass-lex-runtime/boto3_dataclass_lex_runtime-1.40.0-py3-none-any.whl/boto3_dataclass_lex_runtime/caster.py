# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lex_runtime import type_defs as bs_td


class LEX_RUNTIMECaster:

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

    def post_content(
        self,
        res: "bs_td.PostContentResponseTypeDef",
    ) -> "dc_td.PostContentResponse":
        return dc_td.PostContentResponse.make_one(res)

    def post_text(
        self,
        res: "bs_td.PostTextResponseTypeDef",
    ) -> "dc_td.PostTextResponse":
        return dc_td.PostTextResponse.make_one(res)

    def put_session(
        self,
        res: "bs_td.PutSessionResponseTypeDef",
    ) -> "dc_td.PutSessionResponse":
        return dc_td.PutSessionResponse.make_one(res)


lex_runtime_caster = LEX_RUNTIMECaster()
