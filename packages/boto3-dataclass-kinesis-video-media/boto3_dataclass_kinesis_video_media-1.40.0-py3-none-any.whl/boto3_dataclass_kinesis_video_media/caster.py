# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesis_video_media import type_defs as bs_td


class KINESIS_VIDEO_MEDIACaster:

    def get_media(
        self,
        res: "bs_td.GetMediaOutputTypeDef",
    ) -> "dc_td.GetMediaOutput":
        return dc_td.GetMediaOutput.make_one(res)


kinesis_video_media_caster = KINESIS_VIDEO_MEDIACaster()
