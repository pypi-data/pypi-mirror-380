# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesis_video_archived_media import type_defs as bs_td


class KINESIS_VIDEO_ARCHIVED_MEDIACaster:

    def get_clip(
        self,
        res: "bs_td.GetClipOutputTypeDef",
    ) -> "dc_td.GetClipOutput":
        return dc_td.GetClipOutput.make_one(res)

    def get_dash_streaming_session_url(
        self,
        res: "bs_td.GetDASHStreamingSessionURLOutputTypeDef",
    ) -> "dc_td.GetDASHStreamingSessionURLOutput":
        return dc_td.GetDASHStreamingSessionURLOutput.make_one(res)

    def get_hls_streaming_session_url(
        self,
        res: "bs_td.GetHLSStreamingSessionURLOutputTypeDef",
    ) -> "dc_td.GetHLSStreamingSessionURLOutput":
        return dc_td.GetHLSStreamingSessionURLOutput.make_one(res)

    def get_images(
        self,
        res: "bs_td.GetImagesOutputTypeDef",
    ) -> "dc_td.GetImagesOutput":
        return dc_td.GetImagesOutput.make_one(res)

    def get_media_for_fragment_list(
        self,
        res: "bs_td.GetMediaForFragmentListOutputTypeDef",
    ) -> "dc_td.GetMediaForFragmentListOutput":
        return dc_td.GetMediaForFragmentListOutput.make_one(res)

    def list_fragments(
        self,
        res: "bs_td.ListFragmentsOutputTypeDef",
    ) -> "dc_td.ListFragmentsOutput":
        return dc_td.ListFragmentsOutput.make_one(res)


kinesis_video_archived_media_caster = KINESIS_VIDEO_ARCHIVED_MEDIACaster()
