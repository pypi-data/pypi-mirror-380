# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesis_video_webrtc_storage import type_defs as bs_td


class KINESIS_VIDEO_WEBRTC_STORAGECaster:

    def join_storage_session(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def join_storage_session_as_viewer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


kinesis_video_webrtc_storage_caster = KINESIS_VIDEO_WEBRTC_STORAGECaster()
