# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesis_video_signaling import type_defs as bs_td


class KINESIS_VIDEO_SIGNALINGCaster:

    def get_ice_server_config(
        self,
        res: "bs_td.GetIceServerConfigResponseTypeDef",
    ) -> "dc_td.GetIceServerConfigResponse":
        return dc_td.GetIceServerConfigResponse.make_one(res)

    def send_alexa_offer_to_master(
        self,
        res: "bs_td.SendAlexaOfferToMasterResponseTypeDef",
    ) -> "dc_td.SendAlexaOfferToMasterResponse":
        return dc_td.SendAlexaOfferToMasterResponse.make_one(res)


kinesis_video_signaling_caster = KINESIS_VIDEO_SIGNALINGCaster()
