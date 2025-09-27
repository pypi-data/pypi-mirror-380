# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesis_video_archived_media import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Fragment:
    boto3_raw_data: "type_defs.FragmentTypeDef" = dataclasses.field()

    FragmentNumber = field("FragmentNumber")
    FragmentSizeInBytes = field("FragmentSizeInBytes")
    ProducerTimestamp = field("ProducerTimestamp")
    ServerTimestamp = field("ServerTimestamp")
    FragmentLengthInMilliseconds = field("FragmentLengthInMilliseconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FragmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FragmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Image:
    boto3_raw_data: "type_defs.ImageTypeDef" = dataclasses.field()

    TimeStamp = field("TimeStamp")
    Error = field("Error")
    ImageContent = field("ImageContent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaForFragmentListInput:
    boto3_raw_data: "type_defs.GetMediaForFragmentListInputTypeDef" = (
        dataclasses.field()
    )

    Fragments = field("Fragments")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMediaForFragmentListInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaForFragmentListInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClipTimestampRange:
    boto3_raw_data: "type_defs.ClipTimestampRangeTypeDef" = dataclasses.field()

    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClipTimestampRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClipTimestampRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DASHTimestampRange:
    boto3_raw_data: "type_defs.DASHTimestampRangeTypeDef" = dataclasses.field()

    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DASHTimestampRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DASHTimestampRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImagesInput:
    boto3_raw_data: "type_defs.GetImagesInputTypeDef" = dataclasses.field()

    ImageSelectorType = field("ImageSelectorType")
    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")
    Format = field("Format")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    SamplingInterval = field("SamplingInterval")
    FormatConfig = field("FormatConfig")
    WidthPixels = field("WidthPixels")
    HeightPixels = field("HeightPixels")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetImagesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetImagesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HLSTimestampRange:
    boto3_raw_data: "type_defs.HLSTimestampRangeTypeDef" = dataclasses.field()

    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HLSTimestampRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HLSTimestampRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestampRange:
    boto3_raw_data: "type_defs.TimestampRangeTypeDef" = dataclasses.field()

    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimestampRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimestampRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClipOutput:
    boto3_raw_data: "type_defs.GetClipOutputTypeDef" = dataclasses.field()

    ContentType = field("ContentType")
    Payload = field("Payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetClipOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetClipOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDASHStreamingSessionURLOutput:
    boto3_raw_data: "type_defs.GetDASHStreamingSessionURLOutputTypeDef" = (
        dataclasses.field()
    )

    DASHStreamingSessionURL = field("DASHStreamingSessionURL")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDASHStreamingSessionURLOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDASHStreamingSessionURLOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHLSStreamingSessionURLOutput:
    boto3_raw_data: "type_defs.GetHLSStreamingSessionURLOutputTypeDef" = (
        dataclasses.field()
    )

    HLSStreamingSessionURL = field("HLSStreamingSessionURL")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetHLSStreamingSessionURLOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHLSStreamingSessionURLOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaForFragmentListOutput:
    boto3_raw_data: "type_defs.GetMediaForFragmentListOutputTypeDef" = (
        dataclasses.field()
    )

    ContentType = field("ContentType")
    Payload = field("Payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMediaForFragmentListOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaForFragmentListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFragmentsOutput:
    boto3_raw_data: "type_defs.ListFragmentsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Fragments(self):  # pragma: no cover
        return Fragment.make_many(self.boto3_raw_data["Fragments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFragmentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFragmentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImagesInputPaginate:
    boto3_raw_data: "type_defs.GetImagesInputPaginateTypeDef" = dataclasses.field()

    ImageSelectorType = field("ImageSelectorType")
    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")
    Format = field("Format")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    SamplingInterval = field("SamplingInterval")
    FormatConfig = field("FormatConfig")
    WidthPixels = field("WidthPixels")
    HeightPixels = field("HeightPixels")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImagesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImagesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImagesOutput:
    boto3_raw_data: "type_defs.GetImagesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Images(self):  # pragma: no cover
        return Image.make_many(self.boto3_raw_data["Images"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetImagesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetImagesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClipFragmentSelector:
    boto3_raw_data: "type_defs.ClipFragmentSelectorTypeDef" = dataclasses.field()

    FragmentSelectorType = field("FragmentSelectorType")

    @cached_property
    def TimestampRange(self):  # pragma: no cover
        return ClipTimestampRange.make_one(self.boto3_raw_data["TimestampRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClipFragmentSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClipFragmentSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DASHFragmentSelector:
    boto3_raw_data: "type_defs.DASHFragmentSelectorTypeDef" = dataclasses.field()

    FragmentSelectorType = field("FragmentSelectorType")

    @cached_property
    def TimestampRange(self):  # pragma: no cover
        return DASHTimestampRange.make_one(self.boto3_raw_data["TimestampRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DASHFragmentSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DASHFragmentSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HLSFragmentSelector:
    boto3_raw_data: "type_defs.HLSFragmentSelectorTypeDef" = dataclasses.field()

    FragmentSelectorType = field("FragmentSelectorType")

    @cached_property
    def TimestampRange(self):  # pragma: no cover
        return HLSTimestampRange.make_one(self.boto3_raw_data["TimestampRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HLSFragmentSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HLSFragmentSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FragmentSelector:
    boto3_raw_data: "type_defs.FragmentSelectorTypeDef" = dataclasses.field()

    FragmentSelectorType = field("FragmentSelectorType")

    @cached_property
    def TimestampRange(self):  # pragma: no cover
        return TimestampRange.make_one(self.boto3_raw_data["TimestampRange"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FragmentSelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FragmentSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClipInput:
    boto3_raw_data: "type_defs.GetClipInputTypeDef" = dataclasses.field()

    @cached_property
    def ClipFragmentSelector(self):  # pragma: no cover
        return ClipFragmentSelector.make_one(
            self.boto3_raw_data["ClipFragmentSelector"]
        )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetClipInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetClipInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDASHStreamingSessionURLInput:
    boto3_raw_data: "type_defs.GetDASHStreamingSessionURLInputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    PlaybackMode = field("PlaybackMode")
    DisplayFragmentTimestamp = field("DisplayFragmentTimestamp")
    DisplayFragmentNumber = field("DisplayFragmentNumber")

    @cached_property
    def DASHFragmentSelector(self):  # pragma: no cover
        return DASHFragmentSelector.make_one(
            self.boto3_raw_data["DASHFragmentSelector"]
        )

    Expires = field("Expires")
    MaxManifestFragmentResults = field("MaxManifestFragmentResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDASHStreamingSessionURLInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDASHStreamingSessionURLInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHLSStreamingSessionURLInput:
    boto3_raw_data: "type_defs.GetHLSStreamingSessionURLInputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    PlaybackMode = field("PlaybackMode")

    @cached_property
    def HLSFragmentSelector(self):  # pragma: no cover
        return HLSFragmentSelector.make_one(self.boto3_raw_data["HLSFragmentSelector"])

    ContainerFormat = field("ContainerFormat")
    DiscontinuityMode = field("DiscontinuityMode")
    DisplayFragmentTimestamp = field("DisplayFragmentTimestamp")
    Expires = field("Expires")
    MaxMediaPlaylistFragmentResults = field("MaxMediaPlaylistFragmentResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetHLSStreamingSessionURLInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHLSStreamingSessionURLInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFragmentsInputPaginate:
    boto3_raw_data: "type_defs.ListFragmentsInputPaginateTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @cached_property
    def FragmentSelector(self):  # pragma: no cover
        return FragmentSelector.make_one(self.boto3_raw_data["FragmentSelector"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFragmentsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFragmentsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFragmentsInput:
    boto3_raw_data: "type_defs.ListFragmentsInputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def FragmentSelector(self):  # pragma: no cover
        return FragmentSelector.make_one(self.boto3_raw_data["FragmentSelector"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFragmentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFragmentsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
