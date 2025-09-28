# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediaconvert import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AacSettings:
    boto3_raw_data: "type_defs.AacSettingsTypeDef" = dataclasses.field()

    AudioDescriptionBroadcasterMix = field("AudioDescriptionBroadcasterMix")
    Bitrate = field("Bitrate")
    CodecProfile = field("CodecProfile")
    CodingMode = field("CodingMode")
    LoudnessMeasurementMode = field("LoudnessMeasurementMode")
    RapInterval = field("RapInterval")
    RateControlMode = field("RateControlMode")
    RawFormat = field("RawFormat")
    SampleRate = field("SampleRate")
    Specification = field("Specification")
    TargetLoudnessRange = field("TargetLoudnessRange")
    VbrQuality = field("VbrQuality")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AacSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AacSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ac3Settings:
    boto3_raw_data: "type_defs.Ac3SettingsTypeDef" = dataclasses.field()

    Bitrate = field("Bitrate")
    BitstreamMode = field("BitstreamMode")
    CodingMode = field("CodingMode")
    Dialnorm = field("Dialnorm")
    DynamicRangeCompressionLine = field("DynamicRangeCompressionLine")
    DynamicRangeCompressionProfile = field("DynamicRangeCompressionProfile")
    DynamicRangeCompressionRf = field("DynamicRangeCompressionRf")
    LfeFilter = field("LfeFilter")
    MetadataControl = field("MetadataControl")
    SampleRate = field("SampleRate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ac3SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Ac3SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccelerationSettings:
    boto3_raw_data: "type_defs.AccelerationSettingsTypeDef" = dataclasses.field()

    Mode = field("Mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccelerationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccelerationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedInputFilterSettings:
    boto3_raw_data: "type_defs.AdvancedInputFilterSettingsTypeDef" = dataclasses.field()

    AddTexture = field("AddTexture")
    Sharpening = field("Sharpening")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedInputFilterSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedInputFilterSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AiffSettings:
    boto3_raw_data: "type_defs.AiffSettingsTypeDef" = dataclasses.field()

    BitDepth = field("BitDepth")
    Channels = field("Channels")
    SampleRate = field("SampleRate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AiffSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AiffSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowedRenditionSize:
    boto3_raw_data: "type_defs.AllowedRenditionSizeTypeDef" = dataclasses.field()

    Height = field("Height")
    Required = field("Required")
    Width = field("Width")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AllowedRenditionSizeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowedRenditionSizeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AncillarySourceSettings:
    boto3_raw_data: "type_defs.AncillarySourceSettingsTypeDef" = dataclasses.field()

    Convert608To708 = field("Convert608To708")
    SourceAncillaryChannelNumber = field("SourceAncillaryChannelNumber")
    TerminateCaptions = field("TerminateCaptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AncillarySourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AncillarySourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateCertificateRequest:
    boto3_raw_data: "type_defs.AssociateCertificateRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioChannelTaggingSettingsOutput:
    boto3_raw_data: "type_defs.AudioChannelTaggingSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    ChannelTag = field("ChannelTag")
    ChannelTags = field("ChannelTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AudioChannelTaggingSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioChannelTaggingSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioChannelTaggingSettings:
    boto3_raw_data: "type_defs.AudioChannelTaggingSettingsTypeDef" = dataclasses.field()

    ChannelTag = field("ChannelTag")
    ChannelTags = field("ChannelTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioChannelTaggingSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioChannelTaggingSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Eac3AtmosSettings:
    boto3_raw_data: "type_defs.Eac3AtmosSettingsTypeDef" = dataclasses.field()

    Bitrate = field("Bitrate")
    BitstreamMode = field("BitstreamMode")
    CodingMode = field("CodingMode")
    DialogueIntelligence = field("DialogueIntelligence")
    DownmixControl = field("DownmixControl")
    DynamicRangeCompressionLine = field("DynamicRangeCompressionLine")
    DynamicRangeCompressionRf = field("DynamicRangeCompressionRf")
    DynamicRangeControl = field("DynamicRangeControl")
    LoRoCenterMixLevel = field("LoRoCenterMixLevel")
    LoRoSurroundMixLevel = field("LoRoSurroundMixLevel")
    LtRtCenterMixLevel = field("LtRtCenterMixLevel")
    LtRtSurroundMixLevel = field("LtRtSurroundMixLevel")
    MeteringMode = field("MeteringMode")
    SampleRate = field("SampleRate")
    SpeechThreshold = field("SpeechThreshold")
    StereoDownmix = field("StereoDownmix")
    SurroundExMode = field("SurroundExMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Eac3AtmosSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Eac3AtmosSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Eac3Settings:
    boto3_raw_data: "type_defs.Eac3SettingsTypeDef" = dataclasses.field()

    AttenuationControl = field("AttenuationControl")
    Bitrate = field("Bitrate")
    BitstreamMode = field("BitstreamMode")
    CodingMode = field("CodingMode")
    DcFilter = field("DcFilter")
    Dialnorm = field("Dialnorm")
    DynamicRangeCompressionLine = field("DynamicRangeCompressionLine")
    DynamicRangeCompressionRf = field("DynamicRangeCompressionRf")
    LfeControl = field("LfeControl")
    LfeFilter = field("LfeFilter")
    LoRoCenterMixLevel = field("LoRoCenterMixLevel")
    LoRoSurroundMixLevel = field("LoRoSurroundMixLevel")
    LtRtCenterMixLevel = field("LtRtCenterMixLevel")
    LtRtSurroundMixLevel = field("LtRtSurroundMixLevel")
    MetadataControl = field("MetadataControl")
    PassthroughControl = field("PassthroughControl")
    PhaseControl = field("PhaseControl")
    SampleRate = field("SampleRate")
    StereoDownmix = field("StereoDownmix")
    SurroundExMode = field("SurroundExMode")
    SurroundMode = field("SurroundMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Eac3SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Eac3SettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlacSettings:
    boto3_raw_data: "type_defs.FlacSettingsTypeDef" = dataclasses.field()

    BitDepth = field("BitDepth")
    Channels = field("Channels")
    SampleRate = field("SampleRate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlacSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlacSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mp2Settings:
    boto3_raw_data: "type_defs.Mp2SettingsTypeDef" = dataclasses.field()

    AudioDescriptionMix = field("AudioDescriptionMix")
    Bitrate = field("Bitrate")
    Channels = field("Channels")
    SampleRate = field("SampleRate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Mp2SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Mp2SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mp3Settings:
    boto3_raw_data: "type_defs.Mp3SettingsTypeDef" = dataclasses.field()

    Bitrate = field("Bitrate")
    Channels = field("Channels")
    RateControlMode = field("RateControlMode")
    SampleRate = field("SampleRate")
    VbrQuality = field("VbrQuality")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Mp3SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Mp3SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpusSettings:
    boto3_raw_data: "type_defs.OpusSettingsTypeDef" = dataclasses.field()

    Bitrate = field("Bitrate")
    Channels = field("Channels")
    SampleRate = field("SampleRate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpusSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpusSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VorbisSettings:
    boto3_raw_data: "type_defs.VorbisSettingsTypeDef" = dataclasses.field()

    Channels = field("Channels")
    SampleRate = field("SampleRate")
    VbrQuality = field("VbrQuality")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VorbisSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VorbisSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WavSettings:
    boto3_raw_data: "type_defs.WavSettingsTypeDef" = dataclasses.field()

    BitDepth = field("BitDepth")
    Channels = field("Channels")
    Format = field("Format")
    SampleRate = field("SampleRate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WavSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WavSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioNormalizationSettings:
    boto3_raw_data: "type_defs.AudioNormalizationSettingsTypeDef" = dataclasses.field()

    Algorithm = field("Algorithm")
    AlgorithmControl = field("AlgorithmControl")
    CorrectionGateLevel = field("CorrectionGateLevel")
    LoudnessLogging = field("LoudnessLogging")
    PeakCalculation = field("PeakCalculation")
    TargetLkfs = field("TargetLkfs")
    TruePeakLimiterThreshold = field("TruePeakLimiterThreshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioNormalizationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioNormalizationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameRate:
    boto3_raw_data: "type_defs.FrameRateTypeDef" = dataclasses.field()

    Denominator = field("Denominator")
    Numerator = field("Numerator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrameRateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FrameRateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioSelectorGroupOutput:
    boto3_raw_data: "type_defs.AudioSelectorGroupOutputTypeDef" = dataclasses.field()

    AudioSelectorNames = field("AudioSelectorNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioSelectorGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioSelectorGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioSelectorGroup:
    boto3_raw_data: "type_defs.AudioSelectorGroupTypeDef" = dataclasses.field()

    AudioSelectorNames = field("AudioSelectorNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioSelectorGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioSelectorGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsRenditionGroupSettings:
    boto3_raw_data: "type_defs.HlsRenditionGroupSettingsTypeDef" = dataclasses.field()

    RenditionGroupId = field("RenditionGroupId")
    RenditionLanguageCode = field("RenditionLanguageCode")
    RenditionName = field("RenditionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsRenditionGroupSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsRenditionGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForceIncludeRenditionSize:
    boto3_raw_data: "type_defs.ForceIncludeRenditionSizeTypeDef" = dataclasses.field()

    Height = field("Height")
    Width = field("Width")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForceIncludeRenditionSizeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForceIncludeRenditionSizeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MinBottomRenditionSize:
    boto3_raw_data: "type_defs.MinBottomRenditionSizeTypeDef" = dataclasses.field()

    Height = field("Height")
    Width = field("Width")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MinBottomRenditionSizeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MinBottomRenditionSizeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MinTopRenditionSize:
    boto3_raw_data: "type_defs.MinTopRenditionSizeTypeDef" = dataclasses.field()

    Height = field("Height")
    Width = field("Width")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MinTopRenditionSizeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MinTopRenditionSizeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Av1QvbrSettings:
    boto3_raw_data: "type_defs.Av1QvbrSettingsTypeDef" = dataclasses.field()

    QvbrQualityLevel = field("QvbrQualityLevel")
    QvbrQualityLevelFineTune = field("QvbrQualityLevelFineTune")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Av1QvbrSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Av1QvbrSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailBlanking:
    boto3_raw_data: "type_defs.AvailBlankingTypeDef" = dataclasses.field()

    AvailBlankingImage = field("AvailBlankingImage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvailBlankingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AvailBlankingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvcIntraUhdSettings:
    boto3_raw_data: "type_defs.AvcIntraUhdSettingsTypeDef" = dataclasses.field()

    QualityTuningLevel = field("QualityTuningLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvcIntraUhdSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvcIntraUhdSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BandwidthReductionFilter:
    boto3_raw_data: "type_defs.BandwidthReductionFilterTypeDef" = dataclasses.field()

    Sharpening = field("Sharpening")
    Strength = field("Strength")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BandwidthReductionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BandwidthReductionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BurninDestinationSettings:
    boto3_raw_data: "type_defs.BurninDestinationSettingsTypeDef" = dataclasses.field()

    Alignment = field("Alignment")
    ApplyFontColor = field("ApplyFontColor")
    BackgroundColor = field("BackgroundColor")
    BackgroundOpacity = field("BackgroundOpacity")
    FallbackFont = field("FallbackFont")
    FontColor = field("FontColor")
    FontFileBold = field("FontFileBold")
    FontFileBoldItalic = field("FontFileBoldItalic")
    FontFileItalic = field("FontFileItalic")
    FontFileRegular = field("FontFileRegular")
    FontOpacity = field("FontOpacity")
    FontResolution = field("FontResolution")
    FontScript = field("FontScript")
    FontSize = field("FontSize")
    HexFontColor = field("HexFontColor")
    OutlineColor = field("OutlineColor")
    OutlineSize = field("OutlineSize")
    RemoveRubyReserveAttributes = field("RemoveRubyReserveAttributes")
    ShadowColor = field("ShadowColor")
    ShadowOpacity = field("ShadowOpacity")
    ShadowXOffset = field("ShadowXOffset")
    ShadowYOffset = field("ShadowYOffset")
    StylePassthrough = field("StylePassthrough")
    TeletextSpacing = field("TeletextSpacing")
    XPosition = field("XPosition")
    YPosition = field("YPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BurninDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BurninDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobRequest:
    boto3_raw_data: "type_defs.CancelJobRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DvbSubDestinationSettings:
    boto3_raw_data: "type_defs.DvbSubDestinationSettingsTypeDef" = dataclasses.field()

    Alignment = field("Alignment")
    ApplyFontColor = field("ApplyFontColor")
    BackgroundColor = field("BackgroundColor")
    BackgroundOpacity = field("BackgroundOpacity")
    DdsHandling = field("DdsHandling")
    DdsXCoordinate = field("DdsXCoordinate")
    DdsYCoordinate = field("DdsYCoordinate")
    FallbackFont = field("FallbackFont")
    FontColor = field("FontColor")
    FontFileBold = field("FontFileBold")
    FontFileBoldItalic = field("FontFileBoldItalic")
    FontFileItalic = field("FontFileItalic")
    FontFileRegular = field("FontFileRegular")
    FontOpacity = field("FontOpacity")
    FontResolution = field("FontResolution")
    FontScript = field("FontScript")
    FontSize = field("FontSize")
    Height = field("Height")
    HexFontColor = field("HexFontColor")
    OutlineColor = field("OutlineColor")
    OutlineSize = field("OutlineSize")
    ShadowColor = field("ShadowColor")
    ShadowOpacity = field("ShadowOpacity")
    ShadowXOffset = field("ShadowXOffset")
    ShadowYOffset = field("ShadowYOffset")
    StylePassthrough = field("StylePassthrough")
    SubtitlingType = field("SubtitlingType")
    TeletextSpacing = field("TeletextSpacing")
    Width = field("Width")
    XPosition = field("XPosition")
    YPosition = field("YPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DvbSubDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DvbSubDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmbeddedDestinationSettings:
    boto3_raw_data: "type_defs.EmbeddedDestinationSettingsTypeDef" = dataclasses.field()

    Destination608ChannelNumber = field("Destination608ChannelNumber")
    Destination708ServiceNumber = field("Destination708ServiceNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmbeddedDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmbeddedDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImscDestinationSettings:
    boto3_raw_data: "type_defs.ImscDestinationSettingsTypeDef" = dataclasses.field()

    Accessibility = field("Accessibility")
    StylePassthrough = field("StylePassthrough")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImscDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImscDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SccDestinationSettings:
    boto3_raw_data: "type_defs.SccDestinationSettingsTypeDef" = dataclasses.field()

    Framerate = field("Framerate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SccDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SccDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtDestinationSettings:
    boto3_raw_data: "type_defs.SrtDestinationSettingsTypeDef" = dataclasses.field()

    StylePassthrough = field("StylePassthrough")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SrtDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SrtDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TeletextDestinationSettingsOutput:
    boto3_raw_data: "type_defs.TeletextDestinationSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    PageNumber = field("PageNumber")
    PageTypes = field("PageTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TeletextDestinationSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TeletextDestinationSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TtmlDestinationSettings:
    boto3_raw_data: "type_defs.TtmlDestinationSettingsTypeDef" = dataclasses.field()

    StylePassthrough = field("StylePassthrough")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TtmlDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TtmlDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebvttDestinationSettings:
    boto3_raw_data: "type_defs.WebvttDestinationSettingsTypeDef" = dataclasses.field()

    Accessibility = field("Accessibility")
    StylePassthrough = field("StylePassthrough")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebvttDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebvttDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TeletextDestinationSettings:
    boto3_raw_data: "type_defs.TeletextDestinationSettingsTypeDef" = dataclasses.field()

    PageNumber = field("PageNumber")
    PageTypes = field("PageTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TeletextDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TeletextDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionSourceFramerate:
    boto3_raw_data: "type_defs.CaptionSourceFramerateTypeDef" = dataclasses.field()

    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptionSourceFramerateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionSourceFramerateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DvbSubSourceSettings:
    boto3_raw_data: "type_defs.DvbSubSourceSettingsTypeDef" = dataclasses.field()

    Pid = field("Pid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DvbSubSourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DvbSubSourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmbeddedSourceSettings:
    boto3_raw_data: "type_defs.EmbeddedSourceSettingsTypeDef" = dataclasses.field()

    Convert608To708 = field("Convert608To708")
    Source608ChannelNumber = field("Source608ChannelNumber")
    Source608TrackNumber = field("Source608TrackNumber")
    TerminateCaptions = field("TerminateCaptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmbeddedSourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmbeddedSourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TeletextSourceSettings:
    boto3_raw_data: "type_defs.TeletextSourceSettingsTypeDef" = dataclasses.field()

    PageNumber = field("PageNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TeletextSourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TeletextSourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrackSourceSettings:
    boto3_raw_data: "type_defs.TrackSourceSettingsTypeDef" = dataclasses.field()

    TrackNumber = field("TrackNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrackSourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrackSourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebvttHlsSourceSettings:
    boto3_raw_data: "type_defs.WebvttHlsSourceSettingsTypeDef" = dataclasses.field()

    RenditionGroupId = field("RenditionGroupId")
    RenditionLanguageCode = field("RenditionLanguageCode")
    RenditionName = field("RenditionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebvttHlsSourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebvttHlsSourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputChannelMappingOutput:
    boto3_raw_data: "type_defs.OutputChannelMappingOutputTypeDef" = dataclasses.field()

    InputChannels = field("InputChannels")
    InputChannelsFineTune = field("InputChannelsFineTune")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputChannelMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputChannelMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputChannelMapping:
    boto3_raw_data: "type_defs.OutputChannelMappingTypeDef" = dataclasses.field()

    InputChannels = field("InputChannels")
    InputChannelsFineTune = field("InputChannelsFineTune")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputChannelMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputChannelMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClipLimits:
    boto3_raw_data: "type_defs.ClipLimitsTypeDef" = dataclasses.field()

    MaximumRGBTolerance = field("MaximumRGBTolerance")
    MaximumYUV = field("MaximumYUV")
    MinimumRGBTolerance = field("MinimumRGBTolerance")
    MinimumYUV = field("MinimumYUV")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClipLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClipLimitsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafAdditionalManifestOutput:
    boto3_raw_data: "type_defs.CmafAdditionalManifestOutputTypeDef" = (
        dataclasses.field()
    )

    ManifestNameModifier = field("ManifestNameModifier")
    SelectedOutputs = field("SelectedOutputs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CmafAdditionalManifestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafAdditionalManifestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafAdditionalManifest:
    boto3_raw_data: "type_defs.CmafAdditionalManifestTypeDef" = dataclasses.field()

    ManifestNameModifier = field("ManifestNameModifier")
    SelectedOutputs = field("SelectedOutputs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CmafAdditionalManifestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafAdditionalManifestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticKeyProvider:
    boto3_raw_data: "type_defs.StaticKeyProviderTypeDef" = dataclasses.field()

    KeyFormat = field("KeyFormat")
    KeyFormatVersions = field("KeyFormatVersions")
    StaticKeyValue = field("StaticKeyValue")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StaticKeyProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticKeyProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafImageBasedTrickPlaySettings:
    boto3_raw_data: "type_defs.CmafImageBasedTrickPlaySettingsTypeDef" = (
        dataclasses.field()
    )

    IntervalCadence = field("IntervalCadence")
    ThumbnailHeight = field("ThumbnailHeight")
    ThumbnailInterval = field("ThumbnailInterval")
    ThumbnailWidth = field("ThumbnailWidth")
    TileHeight = field("TileHeight")
    TileWidth = field("TileWidth")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CmafImageBasedTrickPlaySettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafImageBasedTrickPlaySettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmfcSettings:
    boto3_raw_data: "type_defs.CmfcSettingsTypeDef" = dataclasses.field()

    AudioDuration = field("AudioDuration")
    AudioGroupId = field("AudioGroupId")
    AudioRenditionSets = field("AudioRenditionSets")
    AudioTrackType = field("AudioTrackType")
    DescriptiveVideoServiceFlag = field("DescriptiveVideoServiceFlag")
    IFrameOnlyManifest = field("IFrameOnlyManifest")
    KlvMetadata = field("KlvMetadata")
    ManifestMetadataSignaling = field("ManifestMetadataSignaling")
    Scte35Esam = field("Scte35Esam")
    Scte35Source = field("Scte35Source")
    TimedMetadata = field("TimedMetadata")
    TimedMetadataBoxVersion = field("TimedMetadataBoxVersion")
    TimedMetadataSchemeIdUri = field("TimedMetadataSchemeIdUri")
    TimedMetadataValue = field("TimedMetadataValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CmfcSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CmfcSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColorConversion3DLUTSetting:
    boto3_raw_data: "type_defs.ColorConversion3DLUTSettingTypeDef" = dataclasses.field()

    FileInput = field("FileInput")
    InputColorSpace = field("InputColorSpace")
    InputMasteringLuminance = field("InputMasteringLuminance")
    OutputColorSpace = field("OutputColorSpace")
    OutputMasteringLuminance = field("OutputMasteringLuminance")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ColorConversion3DLUTSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColorConversion3DLUTSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Hdr10Metadata:
    boto3_raw_data: "type_defs.Hdr10MetadataTypeDef" = dataclasses.field()

    BluePrimaryX = field("BluePrimaryX")
    BluePrimaryY = field("BluePrimaryY")
    GreenPrimaryX = field("GreenPrimaryX")
    GreenPrimaryY = field("GreenPrimaryY")
    MaxContentLightLevel = field("MaxContentLightLevel")
    MaxFrameAverageLightLevel = field("MaxFrameAverageLightLevel")
    MaxLuminance = field("MaxLuminance")
    MinLuminance = field("MinLuminance")
    RedPrimaryX = field("RedPrimaryX")
    RedPrimaryY = field("RedPrimaryY")
    WhitePointX = field("WhitePointX")
    WhitePointY = field("WhitePointY")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Hdr10MetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Hdr10MetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class F4vSettings:
    boto3_raw_data: "type_defs.F4vSettingsTypeDef" = dataclasses.field()

    MoovPlacement = field("MoovPlacement")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.F4vSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.F4vSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M3u8SettingsOutput:
    boto3_raw_data: "type_defs.M3u8SettingsOutputTypeDef" = dataclasses.field()

    AudioDuration = field("AudioDuration")
    AudioFramesPerPes = field("AudioFramesPerPes")
    AudioPids = field("AudioPids")
    AudioPtsOffsetDelta = field("AudioPtsOffsetDelta")
    DataPTSControl = field("DataPTSControl")
    MaxPcrInterval = field("MaxPcrInterval")
    NielsenId3 = field("NielsenId3")
    PatInterval = field("PatInterval")
    PcrControl = field("PcrControl")
    PcrPid = field("PcrPid")
    PmtInterval = field("PmtInterval")
    PmtPid = field("PmtPid")
    PrivateMetadataPid = field("PrivateMetadataPid")
    ProgramNumber = field("ProgramNumber")
    PtsOffset = field("PtsOffset")
    PtsOffsetMode = field("PtsOffsetMode")
    Scte35Pid = field("Scte35Pid")
    Scte35Source = field("Scte35Source")
    TimedMetadata = field("TimedMetadata")
    TimedMetadataPid = field("TimedMetadataPid")
    TransportStreamId = field("TransportStreamId")
    VideoPid = field("VideoPid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.M3u8SettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M3u8SettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MovSettings:
    boto3_raw_data: "type_defs.MovSettingsTypeDef" = dataclasses.field()

    ClapAtom = field("ClapAtom")
    CslgAtom = field("CslgAtom")
    Mpeg2FourCCControl = field("Mpeg2FourCCControl")
    PaddingControl = field("PaddingControl")
    Reference = field("Reference")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MovSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MovSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mp4Settings:
    boto3_raw_data: "type_defs.Mp4SettingsTypeDef" = dataclasses.field()

    AudioDuration = field("AudioDuration")
    C2paManifest = field("C2paManifest")
    CertificateSecret = field("CertificateSecret")
    CslgAtom = field("CslgAtom")
    CttsVersion = field("CttsVersion")
    FreeSpaceBox = field("FreeSpaceBox")
    MoovPlacement = field("MoovPlacement")
    Mp4MajorBrand = field("Mp4MajorBrand")
    SigningKmsKey = field("SigningKmsKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Mp4SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Mp4SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MpdSettings:
    boto3_raw_data: "type_defs.MpdSettingsTypeDef" = dataclasses.field()

    AccessibilityCaptionHints = field("AccessibilityCaptionHints")
    AudioDuration = field("AudioDuration")
    CaptionContainerType = field("CaptionContainerType")
    KlvMetadata = field("KlvMetadata")
    ManifestMetadataSignaling = field("ManifestMetadataSignaling")
    Scte35Esam = field("Scte35Esam")
    Scte35Source = field("Scte35Source")
    TimedMetadata = field("TimedMetadata")
    TimedMetadataBoxVersion = field("TimedMetadataBoxVersion")
    TimedMetadataSchemeIdUri = field("TimedMetadataSchemeIdUri")
    TimedMetadataValue = field("TimedMetadataValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MpdSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MpdSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M3u8Settings:
    boto3_raw_data: "type_defs.M3u8SettingsTypeDef" = dataclasses.field()

    AudioDuration = field("AudioDuration")
    AudioFramesPerPes = field("AudioFramesPerPes")
    AudioPids = field("AudioPids")
    AudioPtsOffsetDelta = field("AudioPtsOffsetDelta")
    DataPTSControl = field("DataPTSControl")
    MaxPcrInterval = field("MaxPcrInterval")
    NielsenId3 = field("NielsenId3")
    PatInterval = field("PatInterval")
    PcrControl = field("PcrControl")
    PcrPid = field("PcrPid")
    PmtInterval = field("PmtInterval")
    PmtPid = field("PmtPid")
    PrivateMetadataPid = field("PrivateMetadataPid")
    ProgramNumber = field("ProgramNumber")
    PtsOffset = field("PtsOffset")
    PtsOffsetMode = field("PtsOffsetMode")
    Scte35Pid = field("Scte35Pid")
    Scte35Source = field("Scte35Source")
    TimedMetadata = field("TimedMetadata")
    TimedMetadataPid = field("TimedMetadataPid")
    TransportStreamId = field("TransportStreamId")
    VideoPid = field("VideoPid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.M3u8SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.M3u8SettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HopDestination:
    boto3_raw_data: "type_defs.HopDestinationTypeDef" = dataclasses.field()

    Priority = field("Priority")
    Queue = field("Queue")
    WaitMinutes = field("WaitMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HopDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HopDestinationTypeDef"]],
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
class ReservationPlanSettings:
    boto3_raw_data: "type_defs.ReservationPlanSettingsTypeDef" = dataclasses.field()

    Commitment = field("Commitment")
    RenewalType = field("RenewalType")
    ReservedSlots = field("ReservedSlots")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservationPlanSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationPlanSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceShareRequest:
    boto3_raw_data: "type_defs.CreateResourceShareRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    SupportCaseId = field("SupportCaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourceShareRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceShareRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashAdditionalManifestOutput:
    boto3_raw_data: "type_defs.DashAdditionalManifestOutputTypeDef" = (
        dataclasses.field()
    )

    ManifestNameModifier = field("ManifestNameModifier")
    SelectedOutputs = field("SelectedOutputs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashAdditionalManifestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashAdditionalManifestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashAdditionalManifest:
    boto3_raw_data: "type_defs.DashAdditionalManifestTypeDef" = dataclasses.field()

    ManifestNameModifier = field("ManifestNameModifier")
    SelectedOutputs = field("SelectedOutputs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashAdditionalManifestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashAdditionalManifestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashIsoImageBasedTrickPlaySettings:
    boto3_raw_data: "type_defs.DashIsoImageBasedTrickPlaySettingsTypeDef" = (
        dataclasses.field()
    )

    IntervalCadence = field("IntervalCadence")
    ThumbnailHeight = field("ThumbnailHeight")
    ThumbnailInterval = field("ThumbnailInterval")
    ThumbnailWidth = field("ThumbnailWidth")
    TileHeight = field("TileHeight")
    TileWidth = field("TileWidth")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DashIsoImageBasedTrickPlaySettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashIsoImageBasedTrickPlaySettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProperties:
    boto3_raw_data: "type_defs.DataPropertiesTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataPropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Deinterlacer:
    boto3_raw_data: "type_defs.DeinterlacerTypeDef" = dataclasses.field()

    Algorithm = field("Algorithm")
    Control = field("Control")
    Mode = field("Mode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeinterlacerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeinterlacerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobTemplateRequest:
    boto3_raw_data: "type_defs.DeleteJobTemplateRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePresetRequest:
    boto3_raw_data: "type_defs.DeletePresetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePresetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePresetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueueRequest:
    boto3_raw_data: "type_defs.DeleteQueueRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueueRequestTypeDef"]
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
class DescribeEndpointsRequest:
    boto3_raw_data: "type_defs.DescribeEndpointsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    Mode = field("Mode")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Endpoint:
    boto3_raw_data: "type_defs.EndpointTypeDef" = dataclasses.field()

    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateCertificateRequest:
    boto3_raw_data: "type_defs.DisassociateCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DolbyVisionLevel6Metadata:
    boto3_raw_data: "type_defs.DolbyVisionLevel6MetadataTypeDef" = dataclasses.field()

    MaxCll = field("MaxCll")
    MaxFall = field("MaxFall")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DolbyVisionLevel6MetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DolbyVisionLevel6MetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DvbNitSettings:
    boto3_raw_data: "type_defs.DvbNitSettingsTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")
    NetworkName = field("NetworkName")
    NitInterval = field("NitInterval")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DvbNitSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DvbNitSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DvbSdtSettings:
    boto3_raw_data: "type_defs.DvbSdtSettingsTypeDef" = dataclasses.field()

    OutputSdt = field("OutputSdt")
    SdtInterval = field("SdtInterval")
    ServiceName = field("ServiceName")
    ServiceProviderName = field("ServiceProviderName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DvbSdtSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DvbSdtSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DvbTdtSettings:
    boto3_raw_data: "type_defs.DvbTdtSettingsTypeDef" = dataclasses.field()

    TdtInterval = field("TdtInterval")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DvbTdtSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DvbTdtSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamicAudioSelector:
    boto3_raw_data: "type_defs.DynamicAudioSelectorTypeDef" = dataclasses.field()

    AudioDurationCorrection = field("AudioDurationCorrection")
    ExternalAudioFileInput = field("ExternalAudioFileInput")
    LanguageCode = field("LanguageCode")
    Offset = field("Offset")
    SelectorType = field("SelectorType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DynamicAudioSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamicAudioSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionContractConfiguration:
    boto3_raw_data: "type_defs.EncryptionContractConfigurationTypeDef" = (
        dataclasses.field()
    )

    SpekeAudioPreset = field("SpekeAudioPreset")
    SpekeVideoPreset = field("SpekeVideoPreset")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EncryptionContractConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionContractConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EsamManifestConfirmConditionNotification:
    boto3_raw_data: "type_defs.EsamManifestConfirmConditionNotificationTypeDef" = (
        dataclasses.field()
    )

    MccXml = field("MccXml")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EsamManifestConfirmConditionNotificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EsamManifestConfirmConditionNotificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EsamSignalProcessingNotification:
    boto3_raw_data: "type_defs.EsamSignalProcessingNotificationTypeDef" = (
        dataclasses.field()
    )

    SccXml = field("SccXml")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EsamSignalProcessingNotificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EsamSignalProcessingNotificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendedDataServices:
    boto3_raw_data: "type_defs.ExtendedDataServicesTypeDef" = dataclasses.field()

    CopyProtectionAction = field("CopyProtectionAction")
    VchipAction = field("VchipAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtendedDataServicesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtendedDataServicesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameCaptureSettings:
    boto3_raw_data: "type_defs.FrameCaptureSettingsTypeDef" = dataclasses.field()

    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    MaxCaptures = field("MaxCaptures")
    Quality = field("Quality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrameCaptureSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameCaptureSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobRequest:
    boto3_raw_data: "type_defs.GetJobRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobTemplateRequest:
    boto3_raw_data: "type_defs.GetJobTemplateRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Policy:
    boto3_raw_data: "type_defs.PolicyTypeDef" = dataclasses.field()

    HttpInputs = field("HttpInputs")
    HttpsInputs = field("HttpsInputs")
    S3Inputs = field("S3Inputs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPresetRequest:
    boto3_raw_data: "type_defs.GetPresetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPresetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPresetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueRequest:
    boto3_raw_data: "type_defs.GetQueueRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQueueRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetQueueRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GifSettings:
    boto3_raw_data: "type_defs.GifSettingsTypeDef" = dataclasses.field()

    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GifSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GifSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H264QvbrSettings:
    boto3_raw_data: "type_defs.H264QvbrSettingsTypeDef" = dataclasses.field()

    MaxAverageBitrate = field("MaxAverageBitrate")
    QvbrQualityLevel = field("QvbrQualityLevel")
    QvbrQualityLevelFineTune = field("QvbrQualityLevelFineTune")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.H264QvbrSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H264QvbrSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H265QvbrSettings:
    boto3_raw_data: "type_defs.H265QvbrSettingsTypeDef" = dataclasses.field()

    MaxAverageBitrate = field("MaxAverageBitrate")
    QvbrQualityLevel = field("QvbrQualityLevel")
    QvbrQualityLevelFineTune = field("QvbrQualityLevelFineTune")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.H265QvbrSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H265QvbrSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Hdr10Plus:
    boto3_raw_data: "type_defs.Hdr10PlusTypeDef" = dataclasses.field()

    MasteringMonitorNits = field("MasteringMonitorNits")
    TargetMonitorNits = field("TargetMonitorNits")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Hdr10PlusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Hdr10PlusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsAdditionalManifestOutput:
    boto3_raw_data: "type_defs.HlsAdditionalManifestOutputTypeDef" = dataclasses.field()

    ManifestNameModifier = field("ManifestNameModifier")
    SelectedOutputs = field("SelectedOutputs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsAdditionalManifestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsAdditionalManifestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsAdditionalManifest:
    boto3_raw_data: "type_defs.HlsAdditionalManifestTypeDef" = dataclasses.field()

    ManifestNameModifier = field("ManifestNameModifier")
    SelectedOutputs = field("SelectedOutputs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsAdditionalManifestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsAdditionalManifestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsCaptionLanguageMapping:
    boto3_raw_data: "type_defs.HlsCaptionLanguageMappingTypeDef" = dataclasses.field()

    CaptionChannel = field("CaptionChannel")
    CustomLanguageCode = field("CustomLanguageCode")
    LanguageCode = field("LanguageCode")
    LanguageDescription = field("LanguageDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsCaptionLanguageMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsCaptionLanguageMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsImageBasedTrickPlaySettings:
    boto3_raw_data: "type_defs.HlsImageBasedTrickPlaySettingsTypeDef" = (
        dataclasses.field()
    )

    IntervalCadence = field("IntervalCadence")
    ThumbnailHeight = field("ThumbnailHeight")
    ThumbnailInterval = field("ThumbnailInterval")
    ThumbnailWidth = field("ThumbnailWidth")
    TileHeight = field("TileHeight")
    TileWidth = field("TileWidth")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HlsImageBasedTrickPlaySettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsImageBasedTrickPlaySettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsSettings:
    boto3_raw_data: "type_defs.HlsSettingsTypeDef" = dataclasses.field()

    AudioGroupId = field("AudioGroupId")
    AudioOnlyContainer = field("AudioOnlyContainer")
    AudioRenditionSets = field("AudioRenditionSets")
    AudioTrackType = field("AudioTrackType")
    DescriptiveVideoServiceFlag = field("DescriptiveVideoServiceFlag")
    IFrameOnlyManifest = field("IFrameOnlyManifest")
    SegmentModifier = field("SegmentModifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HlsSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Id3Insertion:
    boto3_raw_data: "type_defs.Id3InsertionTypeDef" = dataclasses.field()

    Id3 = field("Id3")
    Timecode = field("Timecode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Id3InsertionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Id3InsertionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsertableImage:
    boto3_raw_data: "type_defs.InsertableImageTypeDef" = dataclasses.field()

    Duration = field("Duration")
    FadeIn = field("FadeIn")
    FadeOut = field("FadeOut")
    Height = field("Height")
    ImageInserterInput = field("ImageInserterInput")
    ImageX = field("ImageX")
    ImageY = field("ImageY")
    Layer = field("Layer")
    Opacity = field("Opacity")
    StartTime = field("StartTime")
    Width = field("Width")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsertableImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsertableImageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputClipping:
    boto3_raw_data: "type_defs.InputClippingTypeDef" = dataclasses.field()

    EndTimecode = field("EndTimecode")
    StartTimecode = field("StartTimecode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputClippingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputClippingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDecryptionSettings:
    boto3_raw_data: "type_defs.InputDecryptionSettingsTypeDef" = dataclasses.field()

    DecryptionMode = field("DecryptionMode")
    EncryptedDecryptionKey = field("EncryptedDecryptionKey")
    InitializationVector = field("InitializationVector")
    KmsKeyRegion = field("KmsKeyRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDecryptionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDecryptionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputTamsSettings:
    boto3_raw_data: "type_defs.InputTamsSettingsTypeDef" = dataclasses.field()

    AuthConnectionArn = field("AuthConnectionArn")
    GapHandling = field("GapHandling")
    SourceId = field("SourceId")
    Timerange = field("Timerange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputTamsSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputTamsSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputVideoGenerator:
    boto3_raw_data: "type_defs.InputVideoGeneratorTypeDef" = dataclasses.field()

    Channels = field("Channels")
    Duration = field("Duration")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    SampleRate = field("SampleRate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputVideoGeneratorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputVideoGeneratorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rectangle:
    boto3_raw_data: "type_defs.RectangleTypeDef" = dataclasses.field()

    Height = field("Height")
    Width = field("Width")
    X = field("X")
    Y = field("Y")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RectangleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RectangleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobEngineVersion:
    boto3_raw_data: "type_defs.JobEngineVersionTypeDef" = dataclasses.field()

    ExpirationDate = field("ExpirationDate")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobEngineVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobEngineVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobMessages:
    boto3_raw_data: "type_defs.JobMessagesTypeDef" = dataclasses.field()

    Info = field("Info")
    Warning = field("Warning")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobMessagesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobMessagesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KantarWatermarkSettings:
    boto3_raw_data: "type_defs.KantarWatermarkSettingsTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")
    ContentReference = field("ContentReference")
    CredentialsSecretName = field("CredentialsSecretName")
    FileOffset = field("FileOffset")
    KantarLicenseId = field("KantarLicenseId")
    KantarServerUrl = field("KantarServerUrl")
    LogDestination = field("LogDestination")
    Metadata3 = field("Metadata3")
    Metadata4 = field("Metadata4")
    Metadata5 = field("Metadata5")
    Metadata6 = field("Metadata6")
    Metadata7 = field("Metadata7")
    Metadata8 = field("Metadata8")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KantarWatermarkSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KantarWatermarkSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NielsenConfiguration:
    boto3_raw_data: "type_defs.NielsenConfigurationTypeDef" = dataclasses.field()

    BreakoutCode = field("BreakoutCode")
    DistributorId = field("DistributorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NielsenConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NielsenConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NielsenNonLinearWatermarkSettings:
    boto3_raw_data: "type_defs.NielsenNonLinearWatermarkSettingsTypeDef" = (
        dataclasses.field()
    )

    ActiveWatermarkProcess = field("ActiveWatermarkProcess")
    AdiFilename = field("AdiFilename")
    AssetId = field("AssetId")
    AssetName = field("AssetName")
    CbetSourceId = field("CbetSourceId")
    EpisodeId = field("EpisodeId")
    MetadataDestination = field("MetadataDestination")
    SourceId = field("SourceId")
    SourceWatermarkStatus = field("SourceWatermarkStatus")
    TicServerUrl = field("TicServerUrl")
    UniqueTicPerAudioTrack = field("UniqueTicPerAudioTrack")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NielsenNonLinearWatermarkSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NielsenNonLinearWatermarkSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimecodeConfig:
    boto3_raw_data: "type_defs.TimecodeConfigTypeDef" = dataclasses.field()

    Anchor = field("Anchor")
    Source = field("Source")
    Start = field("Start")
    TimestampOffset = field("TimestampOffset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimecodeConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimecodeConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueTransition:
    boto3_raw_data: "type_defs.QueueTransitionTypeDef" = dataclasses.field()

    DestinationQueue = field("DestinationQueue")
    SourceQueue = field("SourceQueue")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueTransitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueTransitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Timing:
    boto3_raw_data: "type_defs.TimingTypeDef" = dataclasses.field()

    FinishTime = field("FinishTime")
    StartTime = field("StartTime")
    SubmitTime = field("SubmitTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WarningGroup:
    boto3_raw_data: "type_defs.WarningGroupTypeDef" = dataclasses.field()

    Code = field("Code")
    Count = field("Count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WarningGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WarningGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesRequest:
    boto3_raw_data: "type_defs.ListJobTemplatesRequestTypeDef" = dataclasses.field()

    Category = field("Category")
    ListBy = field("ListBy")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Order = field("Order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequest:
    boto3_raw_data: "type_defs.ListJobsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Order = field("Order")
    Queue = field("Queue")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPresetsRequest:
    boto3_raw_data: "type_defs.ListPresetsRequestTypeDef" = dataclasses.field()

    Category = field("Category")
    ListBy = field("ListBy")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Order = field("Order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPresetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPresetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesRequest:
    boto3_raw_data: "type_defs.ListQueuesRequestTypeDef" = dataclasses.field()

    ListBy = field("ListBy")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Order = field("Order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListQueuesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTags:
    boto3_raw_data: "type_defs.ResourceTagsTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVersionsRequest:
    boto3_raw_data: "type_defs.ListVersionsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2tsScte35Esam:
    boto3_raw_data: "type_defs.M2tsScte35EsamTypeDef" = dataclasses.field()

    Scte35EsamPid = field("Scte35EsamPid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.M2tsScte35EsamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.M2tsScte35EsamTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metadata:
    boto3_raw_data: "type_defs.MetadataTypeDef" = dataclasses.field()

    ETag = field("ETag")
    FileSize = field("FileSize")
    LastModified = field("LastModified")
    MimeType = field("MimeType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MotionImageInsertionFramerate:
    boto3_raw_data: "type_defs.MotionImageInsertionFramerateTypeDef" = (
        dataclasses.field()
    )

    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MotionImageInsertionFramerateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MotionImageInsertionFramerateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MotionImageInsertionOffset:
    boto3_raw_data: "type_defs.MotionImageInsertionOffsetTypeDef" = dataclasses.field()

    ImageX = field("ImageX")
    ImageY = field("ImageY")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MotionImageInsertionOffsetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MotionImageInsertionOffsetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mpeg2SettingsOutput:
    boto3_raw_data: "type_defs.Mpeg2SettingsOutputTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")
    Bitrate = field("Bitrate")
    CodecLevel = field("CodecLevel")
    CodecProfile = field("CodecProfile")
    DynamicSubGop = field("DynamicSubGop")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopClosedCadence = field("GopClosedCadence")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    HrdBufferFinalFillPercentage = field("HrdBufferFinalFillPercentage")
    HrdBufferInitialFillPercentage = field("HrdBufferInitialFillPercentage")
    HrdBufferSize = field("HrdBufferSize")
    InterlaceMode = field("InterlaceMode")
    IntraDcPrecision = field("IntraDcPrecision")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    NumberBFramesBetweenReferenceFrames = field("NumberBFramesBetweenReferenceFrames")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    QualityTuningLevel = field("QualityTuningLevel")
    RateControlMode = field("RateControlMode")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SceneChangeDetect = field("SceneChangeDetect")
    SlowPal = field("SlowPal")
    Softness = field("Softness")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")
    Syntax = field("Syntax")
    Telecine = field("Telecine")
    TemporalAdaptiveQuantization = field("TemporalAdaptiveQuantization")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Mpeg2SettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Mpeg2SettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mpeg2Settings:
    boto3_raw_data: "type_defs.Mpeg2SettingsTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")
    Bitrate = field("Bitrate")
    CodecLevel = field("CodecLevel")
    CodecProfile = field("CodecProfile")
    DynamicSubGop = field("DynamicSubGop")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopClosedCadence = field("GopClosedCadence")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    HrdBufferFinalFillPercentage = field("HrdBufferFinalFillPercentage")
    HrdBufferInitialFillPercentage = field("HrdBufferInitialFillPercentage")
    HrdBufferSize = field("HrdBufferSize")
    InterlaceMode = field("InterlaceMode")
    IntraDcPrecision = field("IntraDcPrecision")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    NumberBFramesBetweenReferenceFrames = field("NumberBFramesBetweenReferenceFrames")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    QualityTuningLevel = field("QualityTuningLevel")
    RateControlMode = field("RateControlMode")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SceneChangeDetect = field("SceneChangeDetect")
    SlowPal = field("SlowPal")
    Softness = field("Softness")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")
    Syntax = field("Syntax")
    Telecine = field("Telecine")
    TemporalAdaptiveQuantization = field("TemporalAdaptiveQuantization")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Mpeg2SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Mpeg2SettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MsSmoothAdditionalManifestOutput:
    boto3_raw_data: "type_defs.MsSmoothAdditionalManifestOutputTypeDef" = (
        dataclasses.field()
    )

    ManifestNameModifier = field("ManifestNameModifier")
    SelectedOutputs = field("SelectedOutputs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MsSmoothAdditionalManifestOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MsSmoothAdditionalManifestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MsSmoothAdditionalManifest:
    boto3_raw_data: "type_defs.MsSmoothAdditionalManifestTypeDef" = dataclasses.field()

    ManifestNameModifier = field("ManifestNameModifier")
    SelectedOutputs = field("SelectedOutputs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MsSmoothAdditionalManifestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MsSmoothAdditionalManifestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MxfXavcProfileSettings:
    boto3_raw_data: "type_defs.MxfXavcProfileSettingsTypeDef" = dataclasses.field()

    DurationMode = field("DurationMode")
    MaxAncDataSize = field("MaxAncDataSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MxfXavcProfileSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MxfXavcProfileSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NexGuardFileMarkerSettings:
    boto3_raw_data: "type_defs.NexGuardFileMarkerSettingsTypeDef" = dataclasses.field()

    License = field("License")
    Payload = field("Payload")
    Preset = field("Preset")
    Strength = field("Strength")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NexGuardFileMarkerSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NexGuardFileMarkerSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoiseReducerFilterSettings:
    boto3_raw_data: "type_defs.NoiseReducerFilterSettingsTypeDef" = dataclasses.field()

    Strength = field("Strength")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NoiseReducerFilterSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoiseReducerFilterSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoiseReducerSpatialFilterSettings:
    boto3_raw_data: "type_defs.NoiseReducerSpatialFilterSettingsTypeDef" = (
        dataclasses.field()
    )

    PostFilterSharpenStrength = field("PostFilterSharpenStrength")
    Speed = field("Speed")
    Strength = field("Strength")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NoiseReducerSpatialFilterSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoiseReducerSpatialFilterSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoiseReducerTemporalFilterSettings:
    boto3_raw_data: "type_defs.NoiseReducerTemporalFilterSettingsTypeDef" = (
        dataclasses.field()
    )

    AggressiveMode = field("AggressiveMode")
    PostTemporalSharpening = field("PostTemporalSharpening")
    PostTemporalSharpeningStrength = field("PostTemporalSharpeningStrength")
    Speed = field("Speed")
    Strength = field("Strength")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NoiseReducerTemporalFilterSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoiseReducerTemporalFilterSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoDetail:
    boto3_raw_data: "type_defs.VideoDetailTypeDef" = dataclasses.field()

    HeightInPx = field("HeightInPx")
    WidthInPx = field("WidthInPx")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProbeInputFile:
    boto3_raw_data: "type_defs.ProbeInputFileTypeDef" = dataclasses.field()

    FileUrl = field("FileUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProbeInputFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProbeInputFileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrackMapping:
    boto3_raw_data: "type_defs.TrackMappingTypeDef" = dataclasses.field()

    AudioTrackIndexes = field("AudioTrackIndexes")
    DataTrackIndexes = field("DataTrackIndexes")
    VideoTrackIndexes = field("VideoTrackIndexes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrackMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrackMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProresSettingsOutput:
    boto3_raw_data: "type_defs.ProresSettingsOutputTypeDef" = dataclasses.field()

    ChromaSampling = field("ChromaSampling")
    CodecProfile = field("CodecProfile")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    InterlaceMode = field("InterlaceMode")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SlowPal = field("SlowPal")
    Telecine = field("Telecine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProresSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProresSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProresSettings:
    boto3_raw_data: "type_defs.ProresSettingsTypeDef" = dataclasses.field()

    ChromaSampling = field("ChromaSampling")
    CodecProfile = field("CodecProfile")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    InterlaceMode = field("InterlaceMode")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SlowPal = field("SlowPal")
    Telecine = field("Telecine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProresSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProresSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationPlan:
    boto3_raw_data: "type_defs.ReservationPlanTypeDef" = dataclasses.field()

    Commitment = field("Commitment")
    ExpiresAt = field("ExpiresAt")
    PurchasedAt = field("PurchasedAt")
    RenewalType = field("RenewalType")
    ReservedSlots = field("ReservedSlots")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReservationPlanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReservationPlanTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceOverride:
    boto3_raw_data: "type_defs.ServiceOverrideTypeDef" = dataclasses.field()

    Message = field("Message")
    Name = field("Name")
    OverrideValue = field("OverrideValue")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationAccessControl:
    boto3_raw_data: "type_defs.S3DestinationAccessControlTypeDef" = dataclasses.field()

    CannedAcl = field("CannedAcl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationAccessControlTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationAccessControlTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3EncryptionSettings:
    boto3_raw_data: "type_defs.S3EncryptionSettingsTypeDef" = dataclasses.field()

    EncryptionType = field("EncryptionType")
    KmsEncryptionContext = field("KmsEncryptionContext")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3EncryptionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3EncryptionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchJobsRequest:
    boto3_raw_data: "type_defs.SearchJobsRequestTypeDef" = dataclasses.field()

    InputFile = field("InputFile")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Order = field("Order")
    Queue = field("Queue")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimecodeBurnin:
    boto3_raw_data: "type_defs.TimecodeBurninTypeDef" = dataclasses.field()

    FontSize = field("FontSize")
    Position = field("Position")
    Prefix = field("Prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimecodeBurninTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimecodeBurninTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UncompressedSettings:
    boto3_raw_data: "type_defs.UncompressedSettingsTypeDef" = dataclasses.field()

    Fourcc = field("Fourcc")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    InterlaceMode = field("InterlaceMode")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SlowPal = field("SlowPal")
    Telecine = field("Telecine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UncompressedSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UncompressedSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Vc3Settings:
    boto3_raw_data: "type_defs.Vc3SettingsTypeDef" = dataclasses.field()

    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    InterlaceMode = field("InterlaceMode")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SlowPal = field("SlowPal")
    Telecine = field("Telecine")
    Vc3Class = field("Vc3Class")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Vc3SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Vc3SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Vp8Settings:
    boto3_raw_data: "type_defs.Vp8SettingsTypeDef" = dataclasses.field()

    Bitrate = field("Bitrate")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopSize = field("GopSize")
    HrdBufferSize = field("HrdBufferSize")
    MaxBitrate = field("MaxBitrate")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    QualityTuningLevel = field("QualityTuningLevel")
    RateControlMode = field("RateControlMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Vp8SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Vp8SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Vp9Settings:
    boto3_raw_data: "type_defs.Vp9SettingsTypeDef" = dataclasses.field()

    Bitrate = field("Bitrate")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopSize = field("GopSize")
    HrdBufferSize = field("HrdBufferSize")
    MaxBitrate = field("MaxBitrate")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    QualityTuningLevel = field("QualityTuningLevel")
    RateControlMode = field("RateControlMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Vp9SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Vp9SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoOverlayCrop:
    boto3_raw_data: "type_defs.VideoOverlayCropTypeDef" = dataclasses.field()

    Height = field("Height")
    Unit = field("Unit")
    Width = field("Width")
    X = field("X")
    Y = field("Y")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoOverlayCropTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoOverlayCropTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoOverlayInputClipping:
    boto3_raw_data: "type_defs.VideoOverlayInputClippingTypeDef" = dataclasses.field()

    EndTimecode = field("EndTimecode")
    StartTimecode = field("StartTimecode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoOverlayInputClippingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoOverlayInputClippingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoOverlayPosition:
    boto3_raw_data: "type_defs.VideoOverlayPositionTypeDef" = dataclasses.field()

    Height = field("Height")
    Unit = field("Unit")
    Width = field("Width")
    XPosition = field("XPosition")
    YPosition = field("YPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoOverlayPositionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoOverlayPositionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Xavc4kIntraCbgProfileSettings:
    boto3_raw_data: "type_defs.Xavc4kIntraCbgProfileSettingsTypeDef" = (
        dataclasses.field()
    )

    XavcClass = field("XavcClass")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.Xavc4kIntraCbgProfileSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Xavc4kIntraCbgProfileSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Xavc4kIntraVbrProfileSettings:
    boto3_raw_data: "type_defs.Xavc4kIntraVbrProfileSettingsTypeDef" = (
        dataclasses.field()
    )

    XavcClass = field("XavcClass")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.Xavc4kIntraVbrProfileSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Xavc4kIntraVbrProfileSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Xavc4kProfileSettings:
    boto3_raw_data: "type_defs.Xavc4kProfileSettingsTypeDef" = dataclasses.field()

    BitrateClass = field("BitrateClass")
    CodecProfile = field("CodecProfile")
    FlickerAdaptiveQuantization = field("FlickerAdaptiveQuantization")
    GopBReference = field("GopBReference")
    GopClosedCadence = field("GopClosedCadence")
    HrdBufferSize = field("HrdBufferSize")
    QualityTuningLevel = field("QualityTuningLevel")
    Slices = field("Slices")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Xavc4kProfileSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Xavc4kProfileSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class XavcHdIntraCbgProfileSettings:
    boto3_raw_data: "type_defs.XavcHdIntraCbgProfileSettingsTypeDef" = (
        dataclasses.field()
    )

    XavcClass = field("XavcClass")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.XavcHdIntraCbgProfileSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.XavcHdIntraCbgProfileSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class XavcHdProfileSettings:
    boto3_raw_data: "type_defs.XavcHdProfileSettingsTypeDef" = dataclasses.field()

    BitrateClass = field("BitrateClass")
    FlickerAdaptiveQuantization = field("FlickerAdaptiveQuantization")
    GopBReference = field("GopBReference")
    GopClosedCadence = field("GopClosedCadence")
    HrdBufferSize = field("HrdBufferSize")
    InterlaceMode = field("InterlaceMode")
    QualityTuningLevel = field("QualityTuningLevel")
    Slices = field("Slices")
    Telecine = field("Telecine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.XavcHdProfileSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.XavcHdProfileSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioCodecSettings:
    boto3_raw_data: "type_defs.AudioCodecSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AacSettings(self):  # pragma: no cover
        return AacSettings.make_one(self.boto3_raw_data["AacSettings"])

    @cached_property
    def Ac3Settings(self):  # pragma: no cover
        return Ac3Settings.make_one(self.boto3_raw_data["Ac3Settings"])

    @cached_property
    def AiffSettings(self):  # pragma: no cover
        return AiffSettings.make_one(self.boto3_raw_data["AiffSettings"])

    Codec = field("Codec")

    @cached_property
    def Eac3AtmosSettings(self):  # pragma: no cover
        return Eac3AtmosSettings.make_one(self.boto3_raw_data["Eac3AtmosSettings"])

    @cached_property
    def Eac3Settings(self):  # pragma: no cover
        return Eac3Settings.make_one(self.boto3_raw_data["Eac3Settings"])

    @cached_property
    def FlacSettings(self):  # pragma: no cover
        return FlacSettings.make_one(self.boto3_raw_data["FlacSettings"])

    @cached_property
    def Mp2Settings(self):  # pragma: no cover
        return Mp2Settings.make_one(self.boto3_raw_data["Mp2Settings"])

    @cached_property
    def Mp3Settings(self):  # pragma: no cover
        return Mp3Settings.make_one(self.boto3_raw_data["Mp3Settings"])

    @cached_property
    def OpusSettings(self):  # pragma: no cover
        return OpusSettings.make_one(self.boto3_raw_data["OpusSettings"])

    @cached_property
    def VorbisSettings(self):  # pragma: no cover
        return VorbisSettings.make_one(self.boto3_raw_data["VorbisSettings"])

    @cached_property
    def WavSettings(self):  # pragma: no cover
        return WavSettings.make_one(self.boto3_raw_data["WavSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioCodecSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioCodecSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioProperties:
    boto3_raw_data: "type_defs.AudioPropertiesTypeDef" = dataclasses.field()

    BitDepth = field("BitDepth")
    BitRate = field("BitRate")
    Channels = field("Channels")

    @cached_property
    def FrameRate(self):  # pragma: no cover
        return FrameRate.make_one(self.boto3_raw_data["FrameRate"])

    LanguageCode = field("LanguageCode")
    SampleRate = field("SampleRate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudioPropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoProperties:
    boto3_raw_data: "type_defs.VideoPropertiesTypeDef" = dataclasses.field()

    BitDepth = field("BitDepth")
    BitRate = field("BitRate")
    ColorPrimaries = field("ColorPrimaries")

    @cached_property
    def FrameRate(self):  # pragma: no cover
        return FrameRate.make_one(self.boto3_raw_data["FrameRate"])

    Height = field("Height")
    MatrixCoefficients = field("MatrixCoefficients")
    TransferCharacteristics = field("TransferCharacteristics")
    Width = field("Width")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoPropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedAbrRuleOutput:
    boto3_raw_data: "type_defs.AutomatedAbrRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def AllowedRenditions(self):  # pragma: no cover
        return AllowedRenditionSize.make_many(self.boto3_raw_data["AllowedRenditions"])

    @cached_property
    def ForceIncludeRenditions(self):  # pragma: no cover
        return ForceIncludeRenditionSize.make_many(
            self.boto3_raw_data["ForceIncludeRenditions"]
        )

    @cached_property
    def MinBottomRenditionSize(self):  # pragma: no cover
        return MinBottomRenditionSize.make_one(
            self.boto3_raw_data["MinBottomRenditionSize"]
        )

    @cached_property
    def MinTopRenditionSize(self):  # pragma: no cover
        return MinTopRenditionSize.make_one(self.boto3_raw_data["MinTopRenditionSize"])

    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomatedAbrRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedAbrRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedAbrRule:
    boto3_raw_data: "type_defs.AutomatedAbrRuleTypeDef" = dataclasses.field()

    @cached_property
    def AllowedRenditions(self):  # pragma: no cover
        return AllowedRenditionSize.make_many(self.boto3_raw_data["AllowedRenditions"])

    @cached_property
    def ForceIncludeRenditions(self):  # pragma: no cover
        return ForceIncludeRenditionSize.make_many(
            self.boto3_raw_data["ForceIncludeRenditions"]
        )

    @cached_property
    def MinBottomRenditionSize(self):  # pragma: no cover
        return MinBottomRenditionSize.make_one(
            self.boto3_raw_data["MinBottomRenditionSize"]
        )

    @cached_property
    def MinTopRenditionSize(self):  # pragma: no cover
        return MinTopRenditionSize.make_one(self.boto3_raw_data["MinTopRenditionSize"])

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutomatedAbrRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedAbrRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Av1SettingsOutput:
    boto3_raw_data: "type_defs.Av1SettingsOutputTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")
    BitDepth = field("BitDepth")
    FilmGrainSynthesis = field("FilmGrainSynthesis")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopSize = field("GopSize")
    MaxBitrate = field("MaxBitrate")
    NumberBFramesBetweenReferenceFrames = field("NumberBFramesBetweenReferenceFrames")
    PerFrameMetrics = field("PerFrameMetrics")

    @cached_property
    def QvbrSettings(self):  # pragma: no cover
        return Av1QvbrSettings.make_one(self.boto3_raw_data["QvbrSettings"])

    RateControlMode = field("RateControlMode")
    Slices = field("Slices")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Av1SettingsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Av1SettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Av1Settings:
    boto3_raw_data: "type_defs.Av1SettingsTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")
    BitDepth = field("BitDepth")
    FilmGrainSynthesis = field("FilmGrainSynthesis")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopSize = field("GopSize")
    MaxBitrate = field("MaxBitrate")
    NumberBFramesBetweenReferenceFrames = field("NumberBFramesBetweenReferenceFrames")
    PerFrameMetrics = field("PerFrameMetrics")

    @cached_property
    def QvbrSettings(self):  # pragma: no cover
        return Av1QvbrSettings.make_one(self.boto3_raw_data["QvbrSettings"])

    RateControlMode = field("RateControlMode")
    Slices = field("Slices")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Av1SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Av1SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvcIntraSettingsOutput:
    boto3_raw_data: "type_defs.AvcIntraSettingsOutputTypeDef" = dataclasses.field()

    AvcIntraClass = field("AvcIntraClass")

    @cached_property
    def AvcIntraUhdSettings(self):  # pragma: no cover
        return AvcIntraUhdSettings.make_one(self.boto3_raw_data["AvcIntraUhdSettings"])

    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    InterlaceMode = field("InterlaceMode")
    PerFrameMetrics = field("PerFrameMetrics")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SlowPal = field("SlowPal")
    Telecine = field("Telecine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvcIntraSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvcIntraSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvcIntraSettings:
    boto3_raw_data: "type_defs.AvcIntraSettingsTypeDef" = dataclasses.field()

    AvcIntraClass = field("AvcIntraClass")

    @cached_property
    def AvcIntraUhdSettings(self):  # pragma: no cover
        return AvcIntraUhdSettings.make_one(self.boto3_raw_data["AvcIntraUhdSettings"])

    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    InterlaceMode = field("InterlaceMode")
    PerFrameMetrics = field("PerFrameMetrics")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SlowPal = field("SlowPal")
    Telecine = field("Telecine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvcIntraSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvcIntraSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionDestinationSettingsOutput:
    boto3_raw_data: "type_defs.CaptionDestinationSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BurninDestinationSettings(self):  # pragma: no cover
        return BurninDestinationSettings.make_one(
            self.boto3_raw_data["BurninDestinationSettings"]
        )

    DestinationType = field("DestinationType")

    @cached_property
    def DvbSubDestinationSettings(self):  # pragma: no cover
        return DvbSubDestinationSettings.make_one(
            self.boto3_raw_data["DvbSubDestinationSettings"]
        )

    @cached_property
    def EmbeddedDestinationSettings(self):  # pragma: no cover
        return EmbeddedDestinationSettings.make_one(
            self.boto3_raw_data["EmbeddedDestinationSettings"]
        )

    @cached_property
    def ImscDestinationSettings(self):  # pragma: no cover
        return ImscDestinationSettings.make_one(
            self.boto3_raw_data["ImscDestinationSettings"]
        )

    @cached_property
    def SccDestinationSettings(self):  # pragma: no cover
        return SccDestinationSettings.make_one(
            self.boto3_raw_data["SccDestinationSettings"]
        )

    @cached_property
    def SrtDestinationSettings(self):  # pragma: no cover
        return SrtDestinationSettings.make_one(
            self.boto3_raw_data["SrtDestinationSettings"]
        )

    @cached_property
    def TeletextDestinationSettings(self):  # pragma: no cover
        return TeletextDestinationSettingsOutput.make_one(
            self.boto3_raw_data["TeletextDestinationSettings"]
        )

    @cached_property
    def TtmlDestinationSettings(self):  # pragma: no cover
        return TtmlDestinationSettings.make_one(
            self.boto3_raw_data["TtmlDestinationSettings"]
        )

    @cached_property
    def WebvttDestinationSettings(self):  # pragma: no cover
        return WebvttDestinationSettings.make_one(
            self.boto3_raw_data["WebvttDestinationSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CaptionDestinationSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionDestinationSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionDestinationSettings:
    boto3_raw_data: "type_defs.CaptionDestinationSettingsTypeDef" = dataclasses.field()

    @cached_property
    def BurninDestinationSettings(self):  # pragma: no cover
        return BurninDestinationSettings.make_one(
            self.boto3_raw_data["BurninDestinationSettings"]
        )

    DestinationType = field("DestinationType")

    @cached_property
    def DvbSubDestinationSettings(self):  # pragma: no cover
        return DvbSubDestinationSettings.make_one(
            self.boto3_raw_data["DvbSubDestinationSettings"]
        )

    @cached_property
    def EmbeddedDestinationSettings(self):  # pragma: no cover
        return EmbeddedDestinationSettings.make_one(
            self.boto3_raw_data["EmbeddedDestinationSettings"]
        )

    @cached_property
    def ImscDestinationSettings(self):  # pragma: no cover
        return ImscDestinationSettings.make_one(
            self.boto3_raw_data["ImscDestinationSettings"]
        )

    @cached_property
    def SccDestinationSettings(self):  # pragma: no cover
        return SccDestinationSettings.make_one(
            self.boto3_raw_data["SccDestinationSettings"]
        )

    @cached_property
    def SrtDestinationSettings(self):  # pragma: no cover
        return SrtDestinationSettings.make_one(
            self.boto3_raw_data["SrtDestinationSettings"]
        )

    @cached_property
    def TeletextDestinationSettings(self):  # pragma: no cover
        return TeletextDestinationSettings.make_one(
            self.boto3_raw_data["TeletextDestinationSettings"]
        )

    @cached_property
    def TtmlDestinationSettings(self):  # pragma: no cover
        return TtmlDestinationSettings.make_one(
            self.boto3_raw_data["TtmlDestinationSettings"]
        )

    @cached_property
    def WebvttDestinationSettings(self):  # pragma: no cover
        return WebvttDestinationSettings.make_one(
            self.boto3_raw_data["WebvttDestinationSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptionDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSourceSettings:
    boto3_raw_data: "type_defs.FileSourceSettingsTypeDef" = dataclasses.field()

    ByteRateLimit = field("ByteRateLimit")
    Convert608To708 = field("Convert608To708")
    ConvertPaintToPop = field("ConvertPaintToPop")

    @cached_property
    def Framerate(self):  # pragma: no cover
        return CaptionSourceFramerate.make_one(self.boto3_raw_data["Framerate"])

    SourceFile = field("SourceFile")
    TimeDelta = field("TimeDelta")
    TimeDeltaUnits = field("TimeDeltaUnits")
    UpconvertSTLToTeletext = field("UpconvertSTLToTeletext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMappingOutput:
    boto3_raw_data: "type_defs.ChannelMappingOutputTypeDef" = dataclasses.field()

    @cached_property
    def OutputChannels(self):  # pragma: no cover
        return OutputChannelMappingOutput.make_many(
            self.boto3_raw_data["OutputChannels"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMapping:
    boto3_raw_data: "type_defs.ChannelMappingTypeDef" = dataclasses.field()

    @cached_property
    def OutputChannels(self):  # pragma: no cover
        return OutputChannelMapping.make_many(self.boto3_raw_data["OutputChannels"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColorCorrector:
    boto3_raw_data: "type_defs.ColorCorrectorTypeDef" = dataclasses.field()

    Brightness = field("Brightness")

    @cached_property
    def ClipLimits(self):  # pragma: no cover
        return ClipLimits.make_one(self.boto3_raw_data["ClipLimits"])

    ColorSpaceConversion = field("ColorSpaceConversion")
    Contrast = field("Contrast")

    @cached_property
    def Hdr10Metadata(self):  # pragma: no cover
        return Hdr10Metadata.make_one(self.boto3_raw_data["Hdr10Metadata"])

    HdrToSdrToneMapper = field("HdrToSdrToneMapper")
    Hue = field("Hue")
    MaxLuminance = field("MaxLuminance")
    SampleRangeConversion = field("SampleRangeConversion")
    Saturation = field("Saturation")
    SdrReferenceWhiteLevel = field("SdrReferenceWhiteLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColorCorrectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColorCorrectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoSelectorOutput:
    boto3_raw_data: "type_defs.VideoSelectorOutputTypeDef" = dataclasses.field()

    AlphaBehavior = field("AlphaBehavior")
    ColorSpace = field("ColorSpace")
    ColorSpaceUsage = field("ColorSpaceUsage")
    EmbeddedTimecodeOverride = field("EmbeddedTimecodeOverride")

    @cached_property
    def Hdr10Metadata(self):  # pragma: no cover
        return Hdr10Metadata.make_one(self.boto3_raw_data["Hdr10Metadata"])

    MaxLuminance = field("MaxLuminance")
    PadVideo = field("PadVideo")
    Pid = field("Pid")
    ProgramNumber = field("ProgramNumber")
    Rotate = field("Rotate")
    SampleRange = field("SampleRange")
    SelectorType = field("SelectorType")
    Streams = field("Streams")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoSelector:
    boto3_raw_data: "type_defs.VideoSelectorTypeDef" = dataclasses.field()

    AlphaBehavior = field("AlphaBehavior")
    ColorSpace = field("ColorSpace")
    ColorSpaceUsage = field("ColorSpaceUsage")
    EmbeddedTimecodeOverride = field("EmbeddedTimecodeOverride")

    @cached_property
    def Hdr10Metadata(self):  # pragma: no cover
        return Hdr10Metadata.make_one(self.boto3_raw_data["Hdr10Metadata"])

    MaxLuminance = field("MaxLuminance")
    PadVideo = field("PadVideo")
    Pid = field("Pid")
    ProgramNumber = field("ProgramNumber")
    Rotate = field("Rotate")
    SampleRange = field("SampleRange")
    SelectorType = field("SelectorType")
    Streams = field("Streams")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoSelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoSelectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueRequest:
    boto3_raw_data: "type_defs.CreateQueueRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ConcurrentJobs = field("ConcurrentJobs")
    Description = field("Description")
    PricingPlan = field("PricingPlan")

    @cached_property
    def ReservationPlanSettings(self):  # pragma: no cover
        return ReservationPlanSettings.make_one(
            self.boto3_raw_data["ReservationPlanSettings"]
        )

    Status = field("Status")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueRequest:
    boto3_raw_data: "type_defs.UpdateQueueRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ConcurrentJobs = field("ConcurrentJobs")
    Description = field("Description")

    @cached_property
    def ReservationPlanSettings(self):  # pragma: no cover
        return ReservationPlanSettings.make_one(
            self.boto3_raw_data["ReservationPlanSettings"]
        )

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEndpointsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListJobTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Category = field("Category")
    ListBy = field("ListBy")
    Order = field("Order")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListJobTemplatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsRequestPaginateTypeDef" = dataclasses.field()

    Order = field("Order")
    Queue = field("Queue")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPresetsRequestPaginate:
    boto3_raw_data: "type_defs.ListPresetsRequestPaginateTypeDef" = dataclasses.field()

    Category = field("Category")
    ListBy = field("ListBy")
    Order = field("Order")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPresetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPresetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesRequestPaginate:
    boto3_raw_data: "type_defs.ListQueuesRequestPaginateTypeDef" = dataclasses.field()

    ListBy = field("ListBy")
    Order = field("Order")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueuesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListVersionsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVersionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchJobsRequestPaginate:
    boto3_raw_data: "type_defs.SearchJobsRequestPaginateTypeDef" = dataclasses.field()

    InputFile = field("InputFile")
    Order = field("Order")
    Queue = field("Queue")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointsResponse:
    boto3_raw_data: "type_defs.DescribeEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return Endpoint.make_many(self.boto3_raw_data["Endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DolbyVision:
    boto3_raw_data: "type_defs.DolbyVisionTypeDef" = dataclasses.field()

    @cached_property
    def L6Metadata(self):  # pragma: no cover
        return DolbyVisionLevel6Metadata.make_one(self.boto3_raw_data["L6Metadata"])

    L6Mode = field("L6Mode")
    Mapping = field("Mapping")
    Profile = field("Profile")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DolbyVisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DolbyVisionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpekeKeyProviderCmafOutput:
    boto3_raw_data: "type_defs.SpekeKeyProviderCmafOutputTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")
    DashSignaledSystemIds = field("DashSignaledSystemIds")

    @cached_property
    def EncryptionContractConfiguration(self):  # pragma: no cover
        return EncryptionContractConfiguration.make_one(
            self.boto3_raw_data["EncryptionContractConfiguration"]
        )

    HlsSignaledSystemIds = field("HlsSignaledSystemIds")
    ResourceId = field("ResourceId")
    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpekeKeyProviderCmafOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpekeKeyProviderCmafOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpekeKeyProviderCmaf:
    boto3_raw_data: "type_defs.SpekeKeyProviderCmafTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")
    DashSignaledSystemIds = field("DashSignaledSystemIds")

    @cached_property
    def EncryptionContractConfiguration(self):  # pragma: no cover
        return EncryptionContractConfiguration.make_one(
            self.boto3_raw_data["EncryptionContractConfiguration"]
        )

    HlsSignaledSystemIds = field("HlsSignaledSystemIds")
    ResourceId = field("ResourceId")
    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpekeKeyProviderCmafTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpekeKeyProviderCmafTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpekeKeyProviderOutput:
    boto3_raw_data: "type_defs.SpekeKeyProviderOutputTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @cached_property
    def EncryptionContractConfiguration(self):  # pragma: no cover
        return EncryptionContractConfiguration.make_one(
            self.boto3_raw_data["EncryptionContractConfiguration"]
        )

    ResourceId = field("ResourceId")
    SystemIds = field("SystemIds")
    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpekeKeyProviderOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpekeKeyProviderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpekeKeyProvider:
    boto3_raw_data: "type_defs.SpekeKeyProviderTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @cached_property
    def EncryptionContractConfiguration(self):  # pragma: no cover
        return EncryptionContractConfiguration.make_one(
            self.boto3_raw_data["EncryptionContractConfiguration"]
        )

    ResourceId = field("ResourceId")
    SystemIds = field("SystemIds")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpekeKeyProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpekeKeyProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EsamSettings:
    boto3_raw_data: "type_defs.EsamSettingsTypeDef" = dataclasses.field()

    @cached_property
    def ManifestConfirmConditionNotification(self):  # pragma: no cover
        return EsamManifestConfirmConditionNotification.make_one(
            self.boto3_raw_data["ManifestConfirmConditionNotification"]
        )

    ResponseSignalPreroll = field("ResponseSignalPreroll")

    @cached_property
    def SignalProcessingNotification(self):  # pragma: no cover
        return EsamSignalProcessingNotification.make_one(
            self.boto3_raw_data["SignalProcessingNotification"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EsamSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EsamSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyResponse:
    boto3_raw_data: "type_defs.GetPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def Policy(self):  # pragma: no cover
        return Policy.make_one(self.boto3_raw_data["Policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPolicyRequest:
    boto3_raw_data: "type_defs.PutPolicyRequestTypeDef" = dataclasses.field()

    @cached_property
    def Policy(self):  # pragma: no cover
        return Policy.make_one(self.boto3_raw_data["Policy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutPolicyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPolicyResponse:
    boto3_raw_data: "type_defs.PutPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def Policy(self):  # pragma: no cover
        return Policy.make_one(self.boto3_raw_data["Policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutPolicyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H264SettingsOutput:
    boto3_raw_data: "type_defs.H264SettingsOutputTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")

    @cached_property
    def BandwidthReductionFilter(self):  # pragma: no cover
        return BandwidthReductionFilter.make_one(
            self.boto3_raw_data["BandwidthReductionFilter"]
        )

    Bitrate = field("Bitrate")
    CodecLevel = field("CodecLevel")
    CodecProfile = field("CodecProfile")
    DynamicSubGop = field("DynamicSubGop")
    EndOfStreamMarkers = field("EndOfStreamMarkers")
    EntropyEncoding = field("EntropyEncoding")
    FieldEncoding = field("FieldEncoding")
    FlickerAdaptiveQuantization = field("FlickerAdaptiveQuantization")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopBReference = field("GopBReference")
    GopClosedCadence = field("GopClosedCadence")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    HrdBufferFinalFillPercentage = field("HrdBufferFinalFillPercentage")
    HrdBufferInitialFillPercentage = field("HrdBufferInitialFillPercentage")
    HrdBufferSize = field("HrdBufferSize")
    InterlaceMode = field("InterlaceMode")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    NumberBFramesBetweenReferenceFrames = field("NumberBFramesBetweenReferenceFrames")
    NumberReferenceFrames = field("NumberReferenceFrames")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    QualityTuningLevel = field("QualityTuningLevel")

    @cached_property
    def QvbrSettings(self):  # pragma: no cover
        return H264QvbrSettings.make_one(self.boto3_raw_data["QvbrSettings"])

    RateControlMode = field("RateControlMode")
    RepeatPps = field("RepeatPps")
    SaliencyAwareEncoding = field("SaliencyAwareEncoding")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SceneChangeDetect = field("SceneChangeDetect")
    Slices = field("Slices")
    SlowPal = field("SlowPal")
    Softness = field("Softness")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")
    Syntax = field("Syntax")
    Telecine = field("Telecine")
    TemporalAdaptiveQuantization = field("TemporalAdaptiveQuantization")
    UnregisteredSeiTimecode = field("UnregisteredSeiTimecode")
    WriteMp4PackagingType = field("WriteMp4PackagingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.H264SettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H264SettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H264Settings:
    boto3_raw_data: "type_defs.H264SettingsTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")

    @cached_property
    def BandwidthReductionFilter(self):  # pragma: no cover
        return BandwidthReductionFilter.make_one(
            self.boto3_raw_data["BandwidthReductionFilter"]
        )

    Bitrate = field("Bitrate")
    CodecLevel = field("CodecLevel")
    CodecProfile = field("CodecProfile")
    DynamicSubGop = field("DynamicSubGop")
    EndOfStreamMarkers = field("EndOfStreamMarkers")
    EntropyEncoding = field("EntropyEncoding")
    FieldEncoding = field("FieldEncoding")
    FlickerAdaptiveQuantization = field("FlickerAdaptiveQuantization")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopBReference = field("GopBReference")
    GopClosedCadence = field("GopClosedCadence")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    HrdBufferFinalFillPercentage = field("HrdBufferFinalFillPercentage")
    HrdBufferInitialFillPercentage = field("HrdBufferInitialFillPercentage")
    HrdBufferSize = field("HrdBufferSize")
    InterlaceMode = field("InterlaceMode")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    NumberBFramesBetweenReferenceFrames = field("NumberBFramesBetweenReferenceFrames")
    NumberReferenceFrames = field("NumberReferenceFrames")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    QualityTuningLevel = field("QualityTuningLevel")

    @cached_property
    def QvbrSettings(self):  # pragma: no cover
        return H264QvbrSettings.make_one(self.boto3_raw_data["QvbrSettings"])

    RateControlMode = field("RateControlMode")
    RepeatPps = field("RepeatPps")
    SaliencyAwareEncoding = field("SaliencyAwareEncoding")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SceneChangeDetect = field("SceneChangeDetect")
    Slices = field("Slices")
    SlowPal = field("SlowPal")
    Softness = field("Softness")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")
    Syntax = field("Syntax")
    Telecine = field("Telecine")
    TemporalAdaptiveQuantization = field("TemporalAdaptiveQuantization")
    UnregisteredSeiTimecode = field("UnregisteredSeiTimecode")
    WriteMp4PackagingType = field("WriteMp4PackagingType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.H264SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.H264SettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H265SettingsOutput:
    boto3_raw_data: "type_defs.H265SettingsOutputTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")
    AlternateTransferFunctionSei = field("AlternateTransferFunctionSei")

    @cached_property
    def BandwidthReductionFilter(self):  # pragma: no cover
        return BandwidthReductionFilter.make_one(
            self.boto3_raw_data["BandwidthReductionFilter"]
        )

    Bitrate = field("Bitrate")
    CodecLevel = field("CodecLevel")
    CodecProfile = field("CodecProfile")
    Deblocking = field("Deblocking")
    DynamicSubGop = field("DynamicSubGop")
    EndOfStreamMarkers = field("EndOfStreamMarkers")
    FlickerAdaptiveQuantization = field("FlickerAdaptiveQuantization")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopBReference = field("GopBReference")
    GopClosedCadence = field("GopClosedCadence")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    HrdBufferFinalFillPercentage = field("HrdBufferFinalFillPercentage")
    HrdBufferInitialFillPercentage = field("HrdBufferInitialFillPercentage")
    HrdBufferSize = field("HrdBufferSize")
    InterlaceMode = field("InterlaceMode")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    NumberBFramesBetweenReferenceFrames = field("NumberBFramesBetweenReferenceFrames")
    NumberReferenceFrames = field("NumberReferenceFrames")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    QualityTuningLevel = field("QualityTuningLevel")

    @cached_property
    def QvbrSettings(self):  # pragma: no cover
        return H265QvbrSettings.make_one(self.boto3_raw_data["QvbrSettings"])

    RateControlMode = field("RateControlMode")
    SampleAdaptiveOffsetFilterMode = field("SampleAdaptiveOffsetFilterMode")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SceneChangeDetect = field("SceneChangeDetect")
    Slices = field("Slices")
    SlowPal = field("SlowPal")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")
    Telecine = field("Telecine")
    TemporalAdaptiveQuantization = field("TemporalAdaptiveQuantization")
    TemporalIds = field("TemporalIds")
    Tiles = field("Tiles")
    UnregisteredSeiTimecode = field("UnregisteredSeiTimecode")
    WriteMp4PackagingType = field("WriteMp4PackagingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.H265SettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H265SettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H265Settings:
    boto3_raw_data: "type_defs.H265SettingsTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")
    AlternateTransferFunctionSei = field("AlternateTransferFunctionSei")

    @cached_property
    def BandwidthReductionFilter(self):  # pragma: no cover
        return BandwidthReductionFilter.make_one(
            self.boto3_raw_data["BandwidthReductionFilter"]
        )

    Bitrate = field("Bitrate")
    CodecLevel = field("CodecLevel")
    CodecProfile = field("CodecProfile")
    Deblocking = field("Deblocking")
    DynamicSubGop = field("DynamicSubGop")
    EndOfStreamMarkers = field("EndOfStreamMarkers")
    FlickerAdaptiveQuantization = field("FlickerAdaptiveQuantization")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopBReference = field("GopBReference")
    GopClosedCadence = field("GopClosedCadence")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    HrdBufferFinalFillPercentage = field("HrdBufferFinalFillPercentage")
    HrdBufferInitialFillPercentage = field("HrdBufferInitialFillPercentage")
    HrdBufferSize = field("HrdBufferSize")
    InterlaceMode = field("InterlaceMode")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    NumberBFramesBetweenReferenceFrames = field("NumberBFramesBetweenReferenceFrames")
    NumberReferenceFrames = field("NumberReferenceFrames")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    QualityTuningLevel = field("QualityTuningLevel")

    @cached_property
    def QvbrSettings(self):  # pragma: no cover
        return H265QvbrSettings.make_one(self.boto3_raw_data["QvbrSettings"])

    RateControlMode = field("RateControlMode")
    SampleAdaptiveOffsetFilterMode = field("SampleAdaptiveOffsetFilterMode")
    ScanTypeConversionMode = field("ScanTypeConversionMode")
    SceneChangeDetect = field("SceneChangeDetect")
    Slices = field("Slices")
    SlowPal = field("SlowPal")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")
    Telecine = field("Telecine")
    TemporalAdaptiveQuantization = field("TemporalAdaptiveQuantization")
    TemporalIds = field("TemporalIds")
    Tiles = field("Tiles")
    UnregisteredSeiTimecode = field("UnregisteredSeiTimecode")
    WriteMp4PackagingType = field("WriteMp4PackagingType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.H265SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.H265SettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputSettings:
    boto3_raw_data: "type_defs.OutputSettingsTypeDef" = dataclasses.field()

    @cached_property
    def HlsSettings(self):  # pragma: no cover
        return HlsSettings.make_one(self.boto3_raw_data["HlsSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimedMetadataInsertionOutput:
    boto3_raw_data: "type_defs.TimedMetadataInsertionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Id3Insertions(self):  # pragma: no cover
        return Id3Insertion.make_many(self.boto3_raw_data["Id3Insertions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimedMetadataInsertionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimedMetadataInsertionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimedMetadataInsertion:
    boto3_raw_data: "type_defs.TimedMetadataInsertionTypeDef" = dataclasses.field()

    @cached_property
    def Id3Insertions(self):  # pragma: no cover
        return Id3Insertion.make_many(self.boto3_raw_data["Id3Insertions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimedMetadataInsertionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimedMetadataInsertionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageInserterOutput:
    boto3_raw_data: "type_defs.ImageInserterOutputTypeDef" = dataclasses.field()

    @cached_property
    def InsertableImages(self):  # pragma: no cover
        return InsertableImage.make_many(self.boto3_raw_data["InsertableImages"])

    SdrReferenceWhiteLevel = field("SdrReferenceWhiteLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageInserterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageInserterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageInserter:
    boto3_raw_data: "type_defs.ImageInserterTypeDef" = dataclasses.field()

    @cached_property
    def InsertableImages(self):  # pragma: no cover
        return InsertableImage.make_many(self.boto3_raw_data["InsertableImages"])

    SdrReferenceWhiteLevel = field("SdrReferenceWhiteLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageInserterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageInserterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVersionsResponse:
    boto3_raw_data: "type_defs.ListVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Versions(self):  # pragma: no cover
        return JobEngineVersion.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTags.make_one(self.boto3_raw_data["ResourceTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2tsSettingsOutput:
    boto3_raw_data: "type_defs.M2tsSettingsOutputTypeDef" = dataclasses.field()

    AudioBufferModel = field("AudioBufferModel")
    AudioDuration = field("AudioDuration")
    AudioFramesPerPes = field("AudioFramesPerPes")
    AudioPids = field("AudioPids")
    AudioPtsOffsetDelta = field("AudioPtsOffsetDelta")
    Bitrate = field("Bitrate")
    BufferModel = field("BufferModel")
    DataPTSControl = field("DataPTSControl")

    @cached_property
    def DvbNitSettings(self):  # pragma: no cover
        return DvbNitSettings.make_one(self.boto3_raw_data["DvbNitSettings"])

    @cached_property
    def DvbSdtSettings(self):  # pragma: no cover
        return DvbSdtSettings.make_one(self.boto3_raw_data["DvbSdtSettings"])

    DvbSubPids = field("DvbSubPids")

    @cached_property
    def DvbTdtSettings(self):  # pragma: no cover
        return DvbTdtSettings.make_one(self.boto3_raw_data["DvbTdtSettings"])

    DvbTeletextPid = field("DvbTeletextPid")
    EbpAudioInterval = field("EbpAudioInterval")
    EbpPlacement = field("EbpPlacement")
    EsRateInPes = field("EsRateInPes")
    ForceTsVideoEbpOrder = field("ForceTsVideoEbpOrder")
    FragmentTime = field("FragmentTime")
    KlvMetadata = field("KlvMetadata")
    MaxPcrInterval = field("MaxPcrInterval")
    MinEbpInterval = field("MinEbpInterval")
    NielsenId3 = field("NielsenId3")
    NullPacketBitrate = field("NullPacketBitrate")
    PatInterval = field("PatInterval")
    PcrControl = field("PcrControl")
    PcrPid = field("PcrPid")
    PmtInterval = field("PmtInterval")
    PmtPid = field("PmtPid")
    PreventBufferUnderflow = field("PreventBufferUnderflow")
    PrivateMetadataPid = field("PrivateMetadataPid")
    ProgramNumber = field("ProgramNumber")
    PtsOffset = field("PtsOffset")
    PtsOffsetMode = field("PtsOffsetMode")
    RateMode = field("RateMode")

    @cached_property
    def Scte35Esam(self):  # pragma: no cover
        return M2tsScte35Esam.make_one(self.boto3_raw_data["Scte35Esam"])

    Scte35Pid = field("Scte35Pid")
    Scte35Source = field("Scte35Source")
    SegmentationMarkers = field("SegmentationMarkers")
    SegmentationStyle = field("SegmentationStyle")
    SegmentationTime = field("SegmentationTime")
    TimedMetadataPid = field("TimedMetadataPid")
    TransportStreamId = field("TransportStreamId")
    VideoPid = field("VideoPid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.M2tsSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2tsSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2tsSettings:
    boto3_raw_data: "type_defs.M2tsSettingsTypeDef" = dataclasses.field()

    AudioBufferModel = field("AudioBufferModel")
    AudioDuration = field("AudioDuration")
    AudioFramesPerPes = field("AudioFramesPerPes")
    AudioPids = field("AudioPids")
    AudioPtsOffsetDelta = field("AudioPtsOffsetDelta")
    Bitrate = field("Bitrate")
    BufferModel = field("BufferModel")
    DataPTSControl = field("DataPTSControl")

    @cached_property
    def DvbNitSettings(self):  # pragma: no cover
        return DvbNitSettings.make_one(self.boto3_raw_data["DvbNitSettings"])

    @cached_property
    def DvbSdtSettings(self):  # pragma: no cover
        return DvbSdtSettings.make_one(self.boto3_raw_data["DvbSdtSettings"])

    DvbSubPids = field("DvbSubPids")

    @cached_property
    def DvbTdtSettings(self):  # pragma: no cover
        return DvbTdtSettings.make_one(self.boto3_raw_data["DvbTdtSettings"])

    DvbTeletextPid = field("DvbTeletextPid")
    EbpAudioInterval = field("EbpAudioInterval")
    EbpPlacement = field("EbpPlacement")
    EsRateInPes = field("EsRateInPes")
    ForceTsVideoEbpOrder = field("ForceTsVideoEbpOrder")
    FragmentTime = field("FragmentTime")
    KlvMetadata = field("KlvMetadata")
    MaxPcrInterval = field("MaxPcrInterval")
    MinEbpInterval = field("MinEbpInterval")
    NielsenId3 = field("NielsenId3")
    NullPacketBitrate = field("NullPacketBitrate")
    PatInterval = field("PatInterval")
    PcrControl = field("PcrControl")
    PcrPid = field("PcrPid")
    PmtInterval = field("PmtInterval")
    PmtPid = field("PmtPid")
    PreventBufferUnderflow = field("PreventBufferUnderflow")
    PrivateMetadataPid = field("PrivateMetadataPid")
    ProgramNumber = field("ProgramNumber")
    PtsOffset = field("PtsOffset")
    PtsOffsetMode = field("PtsOffsetMode")
    RateMode = field("RateMode")

    @cached_property
    def Scte35Esam(self):  # pragma: no cover
        return M2tsScte35Esam.make_one(self.boto3_raw_data["Scte35Esam"])

    Scte35Pid = field("Scte35Pid")
    Scte35Source = field("Scte35Source")
    SegmentationMarkers = field("SegmentationMarkers")
    SegmentationStyle = field("SegmentationStyle")
    SegmentationTime = field("SegmentationTime")
    TimedMetadataPid = field("TimedMetadataPid")
    TransportStreamId = field("TransportStreamId")
    VideoPid = field("VideoPid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.M2tsSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.M2tsSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MotionImageInserter:
    boto3_raw_data: "type_defs.MotionImageInserterTypeDef" = dataclasses.field()

    @cached_property
    def Framerate(self):  # pragma: no cover
        return MotionImageInsertionFramerate.make_one(self.boto3_raw_data["Framerate"])

    Input = field("Input")
    InsertionMode = field("InsertionMode")

    @cached_property
    def Offset(self):  # pragma: no cover
        return MotionImageInsertionOffset.make_one(self.boto3_raw_data["Offset"])

    Playback = field("Playback")
    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MotionImageInserterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MotionImageInserterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MxfSettings:
    boto3_raw_data: "type_defs.MxfSettingsTypeDef" = dataclasses.field()

    AfdSignaling = field("AfdSignaling")
    Profile = field("Profile")

    @cached_property
    def XavcProfileSettings(self):  # pragma: no cover
        return MxfXavcProfileSettings.make_one(
            self.boto3_raw_data["XavcProfileSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MxfSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MxfSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartnerWatermarking:
    boto3_raw_data: "type_defs.PartnerWatermarkingTypeDef" = dataclasses.field()

    @cached_property
    def NexguardFileMarkerSettings(self):  # pragma: no cover
        return NexGuardFileMarkerSettings.make_one(
            self.boto3_raw_data["NexguardFileMarkerSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PartnerWatermarkingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartnerWatermarkingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoiseReducer:
    boto3_raw_data: "type_defs.NoiseReducerTypeDef" = dataclasses.field()

    Filter = field("Filter")

    @cached_property
    def FilterSettings(self):  # pragma: no cover
        return NoiseReducerFilterSettings.make_one(
            self.boto3_raw_data["FilterSettings"]
        )

    @cached_property
    def SpatialFilterSettings(self):  # pragma: no cover
        return NoiseReducerSpatialFilterSettings.make_one(
            self.boto3_raw_data["SpatialFilterSettings"]
        )

    @cached_property
    def TemporalFilterSettings(self):  # pragma: no cover
        return NoiseReducerTemporalFilterSettings.make_one(
            self.boto3_raw_data["TemporalFilterSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NoiseReducerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NoiseReducerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDetail:
    boto3_raw_data: "type_defs.OutputDetailTypeDef" = dataclasses.field()

    DurationInMs = field("DurationInMs")

    @cached_property
    def VideoDetails(self):  # pragma: no cover
        return VideoDetail.make_one(self.boto3_raw_data["VideoDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProbeRequest:
    boto3_raw_data: "type_defs.ProbeRequestTypeDef" = dataclasses.field()

    @cached_property
    def InputFiles(self):  # pragma: no cover
        return ProbeInputFile.make_many(self.boto3_raw_data["InputFiles"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProbeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProbeRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Queue:
    boto3_raw_data: "type_defs.QueueTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    ConcurrentJobs = field("ConcurrentJobs")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    LastUpdated = field("LastUpdated")
    PricingPlan = field("PricingPlan")
    ProgressingJobsCount = field("ProgressingJobsCount")

    @cached_property
    def ReservationPlan(self):  # pragma: no cover
        return ReservationPlan.make_one(self.boto3_raw_data["ReservationPlan"])

    @cached_property
    def ServiceOverrides(self):  # pragma: no cover
        return ServiceOverride.make_many(self.boto3_raw_data["ServiceOverrides"])

    Status = field("Status")
    SubmittedJobsCount = field("SubmittedJobsCount")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationSettings:
    boto3_raw_data: "type_defs.S3DestinationSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AccessControl(self):  # pragma: no cover
        return S3DestinationAccessControl.make_one(self.boto3_raw_data["AccessControl"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return S3EncryptionSettings.make_one(self.boto3_raw_data["Encryption"])

    StorageClass = field("StorageClass")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoOverlayInputOutput:
    boto3_raw_data: "type_defs.VideoOverlayInputOutputTypeDef" = dataclasses.field()

    FileInput = field("FileInput")

    @cached_property
    def InputClippings(self):  # pragma: no cover
        return VideoOverlayInputClipping.make_many(
            self.boto3_raw_data["InputClippings"]
        )

    TimecodeSource = field("TimecodeSource")
    TimecodeStart = field("TimecodeStart")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoOverlayInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoOverlayInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoOverlayInput:
    boto3_raw_data: "type_defs.VideoOverlayInputTypeDef" = dataclasses.field()

    FileInput = field("FileInput")

    @cached_property
    def InputClippings(self):  # pragma: no cover
        return VideoOverlayInputClipping.make_many(
            self.boto3_raw_data["InputClippings"]
        )

    TimecodeSource = field("TimecodeSource")
    TimecodeStart = field("TimecodeStart")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoOverlayInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoOverlayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoOverlayTransition:
    boto3_raw_data: "type_defs.VideoOverlayTransitionTypeDef" = dataclasses.field()

    @cached_property
    def EndPosition(self):  # pragma: no cover
        return VideoOverlayPosition.make_one(self.boto3_raw_data["EndPosition"])

    EndTimecode = field("EndTimecode")
    StartTimecode = field("StartTimecode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoOverlayTransitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoOverlayTransitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class XavcSettingsOutput:
    boto3_raw_data: "type_defs.XavcSettingsOutputTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")
    EntropyEncoding = field("EntropyEncoding")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    Profile = field("Profile")
    SlowPal = field("SlowPal")
    Softness = field("Softness")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")
    TemporalAdaptiveQuantization = field("TemporalAdaptiveQuantization")

    @cached_property
    def Xavc4kIntraCbgProfileSettings(self):  # pragma: no cover
        return Xavc4kIntraCbgProfileSettings.make_one(
            self.boto3_raw_data["Xavc4kIntraCbgProfileSettings"]
        )

    @cached_property
    def Xavc4kIntraVbrProfileSettings(self):  # pragma: no cover
        return Xavc4kIntraVbrProfileSettings.make_one(
            self.boto3_raw_data["Xavc4kIntraVbrProfileSettings"]
        )

    @cached_property
    def Xavc4kProfileSettings(self):  # pragma: no cover
        return Xavc4kProfileSettings.make_one(
            self.boto3_raw_data["Xavc4kProfileSettings"]
        )

    @cached_property
    def XavcHdIntraCbgProfileSettings(self):  # pragma: no cover
        return XavcHdIntraCbgProfileSettings.make_one(
            self.boto3_raw_data["XavcHdIntraCbgProfileSettings"]
        )

    @cached_property
    def XavcHdProfileSettings(self):  # pragma: no cover
        return XavcHdProfileSettings.make_one(
            self.boto3_raw_data["XavcHdProfileSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.XavcSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.XavcSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class XavcSettings:
    boto3_raw_data: "type_defs.XavcSettingsTypeDef" = dataclasses.field()

    AdaptiveQuantization = field("AdaptiveQuantization")
    EntropyEncoding = field("EntropyEncoding")
    FramerateControl = field("FramerateControl")
    FramerateConversionAlgorithm = field("FramerateConversionAlgorithm")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    PerFrameMetrics = field("PerFrameMetrics")
    Profile = field("Profile")
    SlowPal = field("SlowPal")
    Softness = field("Softness")
    SpatialAdaptiveQuantization = field("SpatialAdaptiveQuantization")
    TemporalAdaptiveQuantization = field("TemporalAdaptiveQuantization")

    @cached_property
    def Xavc4kIntraCbgProfileSettings(self):  # pragma: no cover
        return Xavc4kIntraCbgProfileSettings.make_one(
            self.boto3_raw_data["Xavc4kIntraCbgProfileSettings"]
        )

    @cached_property
    def Xavc4kIntraVbrProfileSettings(self):  # pragma: no cover
        return Xavc4kIntraVbrProfileSettings.make_one(
            self.boto3_raw_data["Xavc4kIntraVbrProfileSettings"]
        )

    @cached_property
    def Xavc4kProfileSettings(self):  # pragma: no cover
        return Xavc4kProfileSettings.make_one(
            self.boto3_raw_data["Xavc4kProfileSettings"]
        )

    @cached_property
    def XavcHdIntraCbgProfileSettings(self):  # pragma: no cover
        return XavcHdIntraCbgProfileSettings.make_one(
            self.boto3_raw_data["XavcHdIntraCbgProfileSettings"]
        )

    @cached_property
    def XavcHdProfileSettings(self):  # pragma: no cover
        return XavcHdProfileSettings.make_one(
            self.boto3_raw_data["XavcHdProfileSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.XavcSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.XavcSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Track:
    boto3_raw_data: "type_defs.TrackTypeDef" = dataclasses.field()

    @cached_property
    def AudioProperties(self):  # pragma: no cover
        return AudioProperties.make_one(self.boto3_raw_data["AudioProperties"])

    Codec = field("Codec")

    @cached_property
    def DataProperties(self):  # pragma: no cover
        return DataProperties.make_one(self.boto3_raw_data["DataProperties"])

    Duration = field("Duration")
    Index = field("Index")
    TrackType = field("TrackType")

    @cached_property
    def VideoProperties(self):  # pragma: no cover
        return VideoProperties.make_one(self.boto3_raw_data["VideoProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrackTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedAbrSettingsOutput:
    boto3_raw_data: "type_defs.AutomatedAbrSettingsOutputTypeDef" = dataclasses.field()

    MaxAbrBitrate = field("MaxAbrBitrate")
    MaxQualityLevel = field("MaxQualityLevel")
    MaxRenditions = field("MaxRenditions")
    MinAbrBitrate = field("MinAbrBitrate")

    @cached_property
    def Rules(self):  # pragma: no cover
        return AutomatedAbrRuleOutput.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomatedAbrSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedAbrSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedAbrSettings:
    boto3_raw_data: "type_defs.AutomatedAbrSettingsTypeDef" = dataclasses.field()

    MaxAbrBitrate = field("MaxAbrBitrate")
    MaxQualityLevel = field("MaxQualityLevel")
    MaxRenditions = field("MaxRenditions")
    MinAbrBitrate = field("MinAbrBitrate")

    @cached_property
    def Rules(self):  # pragma: no cover
        return AutomatedAbrRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomatedAbrSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedAbrSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionDescriptionOutput:
    boto3_raw_data: "type_defs.CaptionDescriptionOutputTypeDef" = dataclasses.field()

    CaptionSelectorName = field("CaptionSelectorName")
    CustomLanguageCode = field("CustomLanguageCode")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return CaptionDestinationSettingsOutput.make_one(
            self.boto3_raw_data["DestinationSettings"]
        )

    LanguageCode = field("LanguageCode")
    LanguageDescription = field("LanguageDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptionDescriptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionDescriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionDescriptionPresetOutput:
    boto3_raw_data: "type_defs.CaptionDescriptionPresetOutputTypeDef" = (
        dataclasses.field()
    )

    CustomLanguageCode = field("CustomLanguageCode")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return CaptionDestinationSettingsOutput.make_one(
            self.boto3_raw_data["DestinationSettings"]
        )

    LanguageCode = field("LanguageCode")
    LanguageDescription = field("LanguageDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CaptionDescriptionPresetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionDescriptionPresetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionDescriptionPreset:
    boto3_raw_data: "type_defs.CaptionDescriptionPresetTypeDef" = dataclasses.field()

    CustomLanguageCode = field("CustomLanguageCode")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return CaptionDestinationSettings.make_one(
            self.boto3_raw_data["DestinationSettings"]
        )

    LanguageCode = field("LanguageCode")
    LanguageDescription = field("LanguageDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptionDescriptionPresetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionDescriptionPresetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionDescription:
    boto3_raw_data: "type_defs.CaptionDescriptionTypeDef" = dataclasses.field()

    CaptionSelectorName = field("CaptionSelectorName")
    CustomLanguageCode = field("CustomLanguageCode")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return CaptionDestinationSettings.make_one(
            self.boto3_raw_data["DestinationSettings"]
        )

    LanguageCode = field("LanguageCode")
    LanguageDescription = field("LanguageDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptionDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionSourceSettings:
    boto3_raw_data: "type_defs.CaptionSourceSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AncillarySourceSettings(self):  # pragma: no cover
        return AncillarySourceSettings.make_one(
            self.boto3_raw_data["AncillarySourceSettings"]
        )

    @cached_property
    def DvbSubSourceSettings(self):  # pragma: no cover
        return DvbSubSourceSettings.make_one(
            self.boto3_raw_data["DvbSubSourceSettings"]
        )

    @cached_property
    def EmbeddedSourceSettings(self):  # pragma: no cover
        return EmbeddedSourceSettings.make_one(
            self.boto3_raw_data["EmbeddedSourceSettings"]
        )

    @cached_property
    def FileSourceSettings(self):  # pragma: no cover
        return FileSourceSettings.make_one(self.boto3_raw_data["FileSourceSettings"])

    SourceType = field("SourceType")

    @cached_property
    def TeletextSourceSettings(self):  # pragma: no cover
        return TeletextSourceSettings.make_one(
            self.boto3_raw_data["TeletextSourceSettings"]
        )

    @cached_property
    def TrackSourceSettings(self):  # pragma: no cover
        return TrackSourceSettings.make_one(self.boto3_raw_data["TrackSourceSettings"])

    @cached_property
    def WebvttHlsSourceSettings(self):  # pragma: no cover
        return WebvttHlsSourceSettings.make_one(
            self.boto3_raw_data["WebvttHlsSourceSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptionSourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionSourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemixSettingsOutput:
    boto3_raw_data: "type_defs.RemixSettingsOutputTypeDef" = dataclasses.field()

    AudioDescriptionAudioChannel = field("AudioDescriptionAudioChannel")
    AudioDescriptionDataChannel = field("AudioDescriptionDataChannel")

    @cached_property
    def ChannelMapping(self):  # pragma: no cover
        return ChannelMappingOutput.make_one(self.boto3_raw_data["ChannelMapping"])

    ChannelsIn = field("ChannelsIn")
    ChannelsOut = field("ChannelsOut")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemixSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemixSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemixSettings:
    boto3_raw_data: "type_defs.RemixSettingsTypeDef" = dataclasses.field()

    AudioDescriptionAudioChannel = field("AudioDescriptionAudioChannel")
    AudioDescriptionDataChannel = field("AudioDescriptionDataChannel")

    @cached_property
    def ChannelMapping(self):  # pragma: no cover
        return ChannelMapping.make_one(self.boto3_raw_data["ChannelMapping"])

    ChannelsIn = field("ChannelsIn")
    ChannelsOut = field("ChannelsOut")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemixSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemixSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafEncryptionSettingsOutput:
    boto3_raw_data: "type_defs.CmafEncryptionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    ConstantInitializationVector = field("ConstantInitializationVector")
    EncryptionMethod = field("EncryptionMethod")
    InitializationVectorInManifest = field("InitializationVectorInManifest")

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderCmafOutput.make_one(
            self.boto3_raw_data["SpekeKeyProvider"]
        )

    @cached_property
    def StaticKeyProvider(self):  # pragma: no cover
        return StaticKeyProvider.make_one(self.boto3_raw_data["StaticKeyProvider"])

    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CmafEncryptionSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafEncryptionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafEncryptionSettings:
    boto3_raw_data: "type_defs.CmafEncryptionSettingsTypeDef" = dataclasses.field()

    ConstantInitializationVector = field("ConstantInitializationVector")
    EncryptionMethod = field("EncryptionMethod")
    InitializationVectorInManifest = field("InitializationVectorInManifest")

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderCmaf.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    @cached_property
    def StaticKeyProvider(self):  # pragma: no cover
        return StaticKeyProvider.make_one(self.boto3_raw_data["StaticKeyProvider"])

    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CmafEncryptionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafEncryptionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashIsoEncryptionSettingsOutput:
    boto3_raw_data: "type_defs.DashIsoEncryptionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    PlaybackDeviceCompatibility = field("PlaybackDeviceCompatibility")

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderOutput.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DashIsoEncryptionSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashIsoEncryptionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsEncryptionSettingsOutput:
    boto3_raw_data: "type_defs.HlsEncryptionSettingsOutputTypeDef" = dataclasses.field()

    ConstantInitializationVector = field("ConstantInitializationVector")
    EncryptionMethod = field("EncryptionMethod")
    InitializationVectorInManifest = field("InitializationVectorInManifest")
    OfflineEncrypted = field("OfflineEncrypted")

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderOutput.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    @cached_property
    def StaticKeyProvider(self):  # pragma: no cover
        return StaticKeyProvider.make_one(self.boto3_raw_data["StaticKeyProvider"])

    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsEncryptionSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsEncryptionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MsSmoothEncryptionSettingsOutput:
    boto3_raw_data: "type_defs.MsSmoothEncryptionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderOutput.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MsSmoothEncryptionSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MsSmoothEncryptionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashIsoEncryptionSettings:
    boto3_raw_data: "type_defs.DashIsoEncryptionSettingsTypeDef" = dataclasses.field()

    PlaybackDeviceCompatibility = field("PlaybackDeviceCompatibility")

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProvider.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashIsoEncryptionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashIsoEncryptionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsEncryptionSettings:
    boto3_raw_data: "type_defs.HlsEncryptionSettingsTypeDef" = dataclasses.field()

    ConstantInitializationVector = field("ConstantInitializationVector")
    EncryptionMethod = field("EncryptionMethod")
    InitializationVectorInManifest = field("InitializationVectorInManifest")
    OfflineEncrypted = field("OfflineEncrypted")

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProvider.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    @cached_property
    def StaticKeyProvider(self):  # pragma: no cover
        return StaticKeyProvider.make_one(self.boto3_raw_data["StaticKeyProvider"])

    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsEncryptionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsEncryptionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MsSmoothEncryptionSettings:
    boto3_raw_data: "type_defs.MsSmoothEncryptionSettingsTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProvider.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MsSmoothEncryptionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MsSmoothEncryptionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerSettingsOutput:
    boto3_raw_data: "type_defs.ContainerSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CmfcSettings(self):  # pragma: no cover
        return CmfcSettings.make_one(self.boto3_raw_data["CmfcSettings"])

    Container = field("Container")

    @cached_property
    def F4vSettings(self):  # pragma: no cover
        return F4vSettings.make_one(self.boto3_raw_data["F4vSettings"])

    @cached_property
    def M2tsSettings(self):  # pragma: no cover
        return M2tsSettingsOutput.make_one(self.boto3_raw_data["M2tsSettings"])

    @cached_property
    def M3u8Settings(self):  # pragma: no cover
        return M3u8SettingsOutput.make_one(self.boto3_raw_data["M3u8Settings"])

    @cached_property
    def MovSettings(self):  # pragma: no cover
        return MovSettings.make_one(self.boto3_raw_data["MovSettings"])

    @cached_property
    def Mp4Settings(self):  # pragma: no cover
        return Mp4Settings.make_one(self.boto3_raw_data["Mp4Settings"])

    @cached_property
    def MpdSettings(self):  # pragma: no cover
        return MpdSettings.make_one(self.boto3_raw_data["MpdSettings"])

    @cached_property
    def MxfSettings(self):  # pragma: no cover
        return MxfSettings.make_one(self.boto3_raw_data["MxfSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerSettings:
    boto3_raw_data: "type_defs.ContainerSettingsTypeDef" = dataclasses.field()

    @cached_property
    def CmfcSettings(self):  # pragma: no cover
        return CmfcSettings.make_one(self.boto3_raw_data["CmfcSettings"])

    Container = field("Container")

    @cached_property
    def F4vSettings(self):  # pragma: no cover
        return F4vSettings.make_one(self.boto3_raw_data["F4vSettings"])

    @cached_property
    def M2tsSettings(self):  # pragma: no cover
        return M2tsSettings.make_one(self.boto3_raw_data["M2tsSettings"])

    @cached_property
    def M3u8Settings(self):  # pragma: no cover
        return M3u8Settings.make_one(self.boto3_raw_data["M3u8Settings"])

    @cached_property
    def MovSettings(self):  # pragma: no cover
        return MovSettings.make_one(self.boto3_raw_data["MovSettings"])

    @cached_property
    def Mp4Settings(self):  # pragma: no cover
        return Mp4Settings.make_one(self.boto3_raw_data["Mp4Settings"])

    @cached_property
    def MpdSettings(self):  # pragma: no cover
        return MpdSettings.make_one(self.boto3_raw_data["MpdSettings"])

    @cached_property
    def MxfSettings(self):  # pragma: no cover
        return MxfSettings.make_one(self.boto3_raw_data["MxfSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoPreprocessorOutput:
    boto3_raw_data: "type_defs.VideoPreprocessorOutputTypeDef" = dataclasses.field()

    @cached_property
    def ColorCorrector(self):  # pragma: no cover
        return ColorCorrector.make_one(self.boto3_raw_data["ColorCorrector"])

    @cached_property
    def Deinterlacer(self):  # pragma: no cover
        return Deinterlacer.make_one(self.boto3_raw_data["Deinterlacer"])

    @cached_property
    def DolbyVision(self):  # pragma: no cover
        return DolbyVision.make_one(self.boto3_raw_data["DolbyVision"])

    @cached_property
    def Hdr10Plus(self):  # pragma: no cover
        return Hdr10Plus.make_one(self.boto3_raw_data["Hdr10Plus"])

    @cached_property
    def ImageInserter(self):  # pragma: no cover
        return ImageInserterOutput.make_one(self.boto3_raw_data["ImageInserter"])

    @cached_property
    def NoiseReducer(self):  # pragma: no cover
        return NoiseReducer.make_one(self.boto3_raw_data["NoiseReducer"])

    @cached_property
    def PartnerWatermarking(self):  # pragma: no cover
        return PartnerWatermarking.make_one(self.boto3_raw_data["PartnerWatermarking"])

    @cached_property
    def TimecodeBurnin(self):  # pragma: no cover
        return TimecodeBurnin.make_one(self.boto3_raw_data["TimecodeBurnin"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoPreprocessorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoPreprocessorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoPreprocessor:
    boto3_raw_data: "type_defs.VideoPreprocessorTypeDef" = dataclasses.field()

    @cached_property
    def ColorCorrector(self):  # pragma: no cover
        return ColorCorrector.make_one(self.boto3_raw_data["ColorCorrector"])

    @cached_property
    def Deinterlacer(self):  # pragma: no cover
        return Deinterlacer.make_one(self.boto3_raw_data["Deinterlacer"])

    @cached_property
    def DolbyVision(self):  # pragma: no cover
        return DolbyVision.make_one(self.boto3_raw_data["DolbyVision"])

    @cached_property
    def Hdr10Plus(self):  # pragma: no cover
        return Hdr10Plus.make_one(self.boto3_raw_data["Hdr10Plus"])

    @cached_property
    def ImageInserter(self):  # pragma: no cover
        return ImageInserter.make_one(self.boto3_raw_data["ImageInserter"])

    @cached_property
    def NoiseReducer(self):  # pragma: no cover
        return NoiseReducer.make_one(self.boto3_raw_data["NoiseReducer"])

    @cached_property
    def PartnerWatermarking(self):  # pragma: no cover
        return PartnerWatermarking.make_one(self.boto3_raw_data["PartnerWatermarking"])

    @cached_property
    def TimecodeBurnin(self):  # pragma: no cover
        return TimecodeBurnin.make_one(self.boto3_raw_data["TimecodeBurnin"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoPreprocessorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoPreprocessorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputGroupDetail:
    boto3_raw_data: "type_defs.OutputGroupDetailTypeDef" = dataclasses.field()

    @cached_property
    def OutputDetails(self):  # pragma: no cover
        return OutputDetail.make_many(self.boto3_raw_data["OutputDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputGroupDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputGroupDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueResponse:
    boto3_raw_data: "type_defs.CreateQueueResponseTypeDef" = dataclasses.field()

    @cached_property
    def Queue(self):  # pragma: no cover
        return Queue.make_one(self.boto3_raw_data["Queue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQueueResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueResponse:
    boto3_raw_data: "type_defs.GetQueueResponseTypeDef" = dataclasses.field()

    @cached_property
    def Queue(self):  # pragma: no cover
        return Queue.make_one(self.boto3_raw_data["Queue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQueueResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesResponse:
    boto3_raw_data: "type_defs.ListQueuesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Queues(self):  # pragma: no cover
        return Queue.make_many(self.boto3_raw_data["Queues"])

    TotalConcurrentJobs = field("TotalConcurrentJobs")
    UnallocatedConcurrentJobs = field("UnallocatedConcurrentJobs")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueuesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueResponse:
    boto3_raw_data: "type_defs.UpdateQueueResponseTypeDef" = dataclasses.field()

    @cached_property
    def Queue(self):  # pragma: no cover
        return Queue.make_one(self.boto3_raw_data["Queue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQueueResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationSettings:
    boto3_raw_data: "type_defs.DestinationSettingsTypeDef" = dataclasses.field()

    @cached_property
    def S3Settings(self):  # pragma: no cover
        return S3DestinationSettings.make_one(self.boto3_raw_data["S3Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoOverlayOutput:
    boto3_raw_data: "type_defs.VideoOverlayOutputTypeDef" = dataclasses.field()

    @cached_property
    def Crop(self):  # pragma: no cover
        return VideoOverlayCrop.make_one(self.boto3_raw_data["Crop"])

    EndTimecode = field("EndTimecode")

    @cached_property
    def InitialPosition(self):  # pragma: no cover
        return VideoOverlayPosition.make_one(self.boto3_raw_data["InitialPosition"])

    @cached_property
    def Input(self):  # pragma: no cover
        return VideoOverlayInputOutput.make_one(self.boto3_raw_data["Input"])

    Playback = field("Playback")
    StartTimecode = field("StartTimecode")

    @cached_property
    def Transitions(self):  # pragma: no cover
        return VideoOverlayTransition.make_many(self.boto3_raw_data["Transitions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoOverlayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoOverlayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoOverlay:
    boto3_raw_data: "type_defs.VideoOverlayTypeDef" = dataclasses.field()

    @cached_property
    def Crop(self):  # pragma: no cover
        return VideoOverlayCrop.make_one(self.boto3_raw_data["Crop"])

    EndTimecode = field("EndTimecode")

    @cached_property
    def InitialPosition(self):  # pragma: no cover
        return VideoOverlayPosition.make_one(self.boto3_raw_data["InitialPosition"])

    @cached_property
    def Input(self):  # pragma: no cover
        return VideoOverlayInput.make_one(self.boto3_raw_data["Input"])

    Playback = field("Playback")
    StartTimecode = field("StartTimecode")

    @cached_property
    def Transitions(self):  # pragma: no cover
        return VideoOverlayTransition.make_many(self.boto3_raw_data["Transitions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoOverlayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoOverlayTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoCodecSettingsOutput:
    boto3_raw_data: "type_defs.VideoCodecSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Av1Settings(self):  # pragma: no cover
        return Av1SettingsOutput.make_one(self.boto3_raw_data["Av1Settings"])

    @cached_property
    def AvcIntraSettings(self):  # pragma: no cover
        return AvcIntraSettingsOutput.make_one(self.boto3_raw_data["AvcIntraSettings"])

    Codec = field("Codec")

    @cached_property
    def FrameCaptureSettings(self):  # pragma: no cover
        return FrameCaptureSettings.make_one(
            self.boto3_raw_data["FrameCaptureSettings"]
        )

    @cached_property
    def GifSettings(self):  # pragma: no cover
        return GifSettings.make_one(self.boto3_raw_data["GifSettings"])

    @cached_property
    def H264Settings(self):  # pragma: no cover
        return H264SettingsOutput.make_one(self.boto3_raw_data["H264Settings"])

    @cached_property
    def H265Settings(self):  # pragma: no cover
        return H265SettingsOutput.make_one(self.boto3_raw_data["H265Settings"])

    @cached_property
    def Mpeg2Settings(self):  # pragma: no cover
        return Mpeg2SettingsOutput.make_one(self.boto3_raw_data["Mpeg2Settings"])

    @cached_property
    def ProresSettings(self):  # pragma: no cover
        return ProresSettingsOutput.make_one(self.boto3_raw_data["ProresSettings"])

    @cached_property
    def UncompressedSettings(self):  # pragma: no cover
        return UncompressedSettings.make_one(
            self.boto3_raw_data["UncompressedSettings"]
        )

    @cached_property
    def Vc3Settings(self):  # pragma: no cover
        return Vc3Settings.make_one(self.boto3_raw_data["Vc3Settings"])

    @cached_property
    def Vp8Settings(self):  # pragma: no cover
        return Vp8Settings.make_one(self.boto3_raw_data["Vp8Settings"])

    @cached_property
    def Vp9Settings(self):  # pragma: no cover
        return Vp9Settings.make_one(self.boto3_raw_data["Vp9Settings"])

    @cached_property
    def XavcSettings(self):  # pragma: no cover
        return XavcSettingsOutput.make_one(self.boto3_raw_data["XavcSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoCodecSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoCodecSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoCodecSettings:
    boto3_raw_data: "type_defs.VideoCodecSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Av1Settings(self):  # pragma: no cover
        return Av1Settings.make_one(self.boto3_raw_data["Av1Settings"])

    @cached_property
    def AvcIntraSettings(self):  # pragma: no cover
        return AvcIntraSettings.make_one(self.boto3_raw_data["AvcIntraSettings"])

    Codec = field("Codec")

    @cached_property
    def FrameCaptureSettings(self):  # pragma: no cover
        return FrameCaptureSettings.make_one(
            self.boto3_raw_data["FrameCaptureSettings"]
        )

    @cached_property
    def GifSettings(self):  # pragma: no cover
        return GifSettings.make_one(self.boto3_raw_data["GifSettings"])

    @cached_property
    def H264Settings(self):  # pragma: no cover
        return H264Settings.make_one(self.boto3_raw_data["H264Settings"])

    @cached_property
    def H265Settings(self):  # pragma: no cover
        return H265Settings.make_one(self.boto3_raw_data["H265Settings"])

    @cached_property
    def Mpeg2Settings(self):  # pragma: no cover
        return Mpeg2Settings.make_one(self.boto3_raw_data["Mpeg2Settings"])

    @cached_property
    def ProresSettings(self):  # pragma: no cover
        return ProresSettings.make_one(self.boto3_raw_data["ProresSettings"])

    @cached_property
    def UncompressedSettings(self):  # pragma: no cover
        return UncompressedSettings.make_one(
            self.boto3_raw_data["UncompressedSettings"]
        )

    @cached_property
    def Vc3Settings(self):  # pragma: no cover
        return Vc3Settings.make_one(self.boto3_raw_data["Vc3Settings"])

    @cached_property
    def Vp8Settings(self):  # pragma: no cover
        return Vp8Settings.make_one(self.boto3_raw_data["Vp8Settings"])

    @cached_property
    def Vp9Settings(self):  # pragma: no cover
        return Vp9Settings.make_one(self.boto3_raw_data["Vp9Settings"])

    @cached_property
    def XavcSettings(self):  # pragma: no cover
        return XavcSettings.make_one(self.boto3_raw_data["XavcSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoCodecSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoCodecSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Container:
    boto3_raw_data: "type_defs.ContainerTypeDef" = dataclasses.field()

    Duration = field("Duration")
    Format = field("Format")

    @cached_property
    def Tracks(self):  # pragma: no cover
        return Track.make_many(self.boto3_raw_data["Tracks"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedEncodingSettingsOutput:
    boto3_raw_data: "type_defs.AutomatedEncodingSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AbrSettings(self):  # pragma: no cover
        return AutomatedAbrSettingsOutput.make_one(self.boto3_raw_data["AbrSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedEncodingSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedEncodingSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedEncodingSettings:
    boto3_raw_data: "type_defs.AutomatedEncodingSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AbrSettings(self):  # pragma: no cover
        return AutomatedAbrSettings.make_one(self.boto3_raw_data["AbrSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomatedEncodingSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedEncodingSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionSelector:
    boto3_raw_data: "type_defs.CaptionSelectorTypeDef" = dataclasses.field()

    CustomLanguageCode = field("CustomLanguageCode")
    LanguageCode = field("LanguageCode")

    @cached_property
    def SourceSettings(self):  # pragma: no cover
        return CaptionSourceSettings.make_one(self.boto3_raw_data["SourceSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaptionSelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaptionSelectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioDescriptionOutput:
    boto3_raw_data: "type_defs.AudioDescriptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def AudioChannelTaggingSettings(self):  # pragma: no cover
        return AudioChannelTaggingSettingsOutput.make_one(
            self.boto3_raw_data["AudioChannelTaggingSettings"]
        )

    @cached_property
    def AudioNormalizationSettings(self):  # pragma: no cover
        return AudioNormalizationSettings.make_one(
            self.boto3_raw_data["AudioNormalizationSettings"]
        )

    AudioSourceName = field("AudioSourceName")
    AudioType = field("AudioType")
    AudioTypeControl = field("AudioTypeControl")

    @cached_property
    def CodecSettings(self):  # pragma: no cover
        return AudioCodecSettings.make_one(self.boto3_raw_data["CodecSettings"])

    CustomLanguageCode = field("CustomLanguageCode")
    LanguageCode = field("LanguageCode")
    LanguageCodeControl = field("LanguageCodeControl")

    @cached_property
    def RemixSettings(self):  # pragma: no cover
        return RemixSettingsOutput.make_one(self.boto3_raw_data["RemixSettings"])

    StreamName = field("StreamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioDescriptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioDescriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioSelectorOutput:
    boto3_raw_data: "type_defs.AudioSelectorOutputTypeDef" = dataclasses.field()

    AudioDurationCorrection = field("AudioDurationCorrection")
    CustomLanguageCode = field("CustomLanguageCode")
    DefaultSelection = field("DefaultSelection")
    ExternalAudioFileInput = field("ExternalAudioFileInput")

    @cached_property
    def HlsRenditionGroupSettings(self):  # pragma: no cover
        return HlsRenditionGroupSettings.make_one(
            self.boto3_raw_data["HlsRenditionGroupSettings"]
        )

    LanguageCode = field("LanguageCode")
    Offset = field("Offset")
    Pids = field("Pids")
    ProgramSelection = field("ProgramSelection")

    @cached_property
    def RemixSettings(self):  # pragma: no cover
        return RemixSettingsOutput.make_one(self.boto3_raw_data["RemixSettings"])

    SelectorType = field("SelectorType")
    Tracks = field("Tracks")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioDescription:
    boto3_raw_data: "type_defs.AudioDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def AudioChannelTaggingSettings(self):  # pragma: no cover
        return AudioChannelTaggingSettings.make_one(
            self.boto3_raw_data["AudioChannelTaggingSettings"]
        )

    @cached_property
    def AudioNormalizationSettings(self):  # pragma: no cover
        return AudioNormalizationSettings.make_one(
            self.boto3_raw_data["AudioNormalizationSettings"]
        )

    AudioSourceName = field("AudioSourceName")
    AudioType = field("AudioType")
    AudioTypeControl = field("AudioTypeControl")

    @cached_property
    def CodecSettings(self):  # pragma: no cover
        return AudioCodecSettings.make_one(self.boto3_raw_data["CodecSettings"])

    CustomLanguageCode = field("CustomLanguageCode")
    LanguageCode = field("LanguageCode")
    LanguageCodeControl = field("LanguageCodeControl")

    @cached_property
    def RemixSettings(self):  # pragma: no cover
        return RemixSettings.make_one(self.boto3_raw_data["RemixSettings"])

    StreamName = field("StreamName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioSelector:
    boto3_raw_data: "type_defs.AudioSelectorTypeDef" = dataclasses.field()

    AudioDurationCorrection = field("AudioDurationCorrection")
    CustomLanguageCode = field("CustomLanguageCode")
    DefaultSelection = field("DefaultSelection")
    ExternalAudioFileInput = field("ExternalAudioFileInput")

    @cached_property
    def HlsRenditionGroupSettings(self):  # pragma: no cover
        return HlsRenditionGroupSettings.make_one(
            self.boto3_raw_data["HlsRenditionGroupSettings"]
        )

    LanguageCode = field("LanguageCode")
    Offset = field("Offset")
    Pids = field("Pids")
    ProgramSelection = field("ProgramSelection")

    @cached_property
    def RemixSettings(self):  # pragma: no cover
        return RemixSettings.make_one(self.boto3_raw_data["RemixSettings"])

    SelectorType = field("SelectorType")
    Tracks = field("Tracks")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioSelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudioSelectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafGroupSettingsOutput:
    boto3_raw_data: "type_defs.CmafGroupSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AdditionalManifests(self):  # pragma: no cover
        return CmafAdditionalManifestOutput.make_many(
            self.boto3_raw_data["AdditionalManifests"]
        )

    BaseUrl = field("BaseUrl")
    ClientCache = field("ClientCache")
    CodecSpecification = field("CodecSpecification")
    DashIFrameTrickPlayNameModifier = field("DashIFrameTrickPlayNameModifier")
    DashManifestStyle = field("DashManifestStyle")
    Destination = field("Destination")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return DestinationSettings.make_one(self.boto3_raw_data["DestinationSettings"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return CmafEncryptionSettingsOutput.make_one(self.boto3_raw_data["Encryption"])

    FragmentLength = field("FragmentLength")
    ImageBasedTrickPlay = field("ImageBasedTrickPlay")

    @cached_property
    def ImageBasedTrickPlaySettings(self):  # pragma: no cover
        return CmafImageBasedTrickPlaySettings.make_one(
            self.boto3_raw_data["ImageBasedTrickPlaySettings"]
        )

    ManifestCompression = field("ManifestCompression")
    ManifestDurationFormat = field("ManifestDurationFormat")
    MinBufferTime = field("MinBufferTime")
    MinFinalSegmentLength = field("MinFinalSegmentLength")
    MpdManifestBandwidthType = field("MpdManifestBandwidthType")
    MpdProfile = field("MpdProfile")
    PtsOffsetHandlingForBFrames = field("PtsOffsetHandlingForBFrames")
    SegmentControl = field("SegmentControl")
    SegmentLength = field("SegmentLength")
    SegmentLengthControl = field("SegmentLengthControl")
    StreamInfResolution = field("StreamInfResolution")
    TargetDurationCompatibilityMode = field("TargetDurationCompatibilityMode")
    VideoCompositionOffsets = field("VideoCompositionOffsets")
    WriteDashManifest = field("WriteDashManifest")
    WriteHlsManifest = field("WriteHlsManifest")
    WriteSegmentTimelineInRepresentation = field("WriteSegmentTimelineInRepresentation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CmafGroupSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafGroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafGroupSettings:
    boto3_raw_data: "type_defs.CmafGroupSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AdditionalManifests(self):  # pragma: no cover
        return CmafAdditionalManifest.make_many(
            self.boto3_raw_data["AdditionalManifests"]
        )

    BaseUrl = field("BaseUrl")
    ClientCache = field("ClientCache")
    CodecSpecification = field("CodecSpecification")
    DashIFrameTrickPlayNameModifier = field("DashIFrameTrickPlayNameModifier")
    DashManifestStyle = field("DashManifestStyle")
    Destination = field("Destination")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return DestinationSettings.make_one(self.boto3_raw_data["DestinationSettings"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return CmafEncryptionSettings.make_one(self.boto3_raw_data["Encryption"])

    FragmentLength = field("FragmentLength")
    ImageBasedTrickPlay = field("ImageBasedTrickPlay")

    @cached_property
    def ImageBasedTrickPlaySettings(self):  # pragma: no cover
        return CmafImageBasedTrickPlaySettings.make_one(
            self.boto3_raw_data["ImageBasedTrickPlaySettings"]
        )

    ManifestCompression = field("ManifestCompression")
    ManifestDurationFormat = field("ManifestDurationFormat")
    MinBufferTime = field("MinBufferTime")
    MinFinalSegmentLength = field("MinFinalSegmentLength")
    MpdManifestBandwidthType = field("MpdManifestBandwidthType")
    MpdProfile = field("MpdProfile")
    PtsOffsetHandlingForBFrames = field("PtsOffsetHandlingForBFrames")
    SegmentControl = field("SegmentControl")
    SegmentLength = field("SegmentLength")
    SegmentLengthControl = field("SegmentLengthControl")
    StreamInfResolution = field("StreamInfResolution")
    TargetDurationCompatibilityMode = field("TargetDurationCompatibilityMode")
    VideoCompositionOffsets = field("VideoCompositionOffsets")
    WriteDashManifest = field("WriteDashManifest")
    WriteHlsManifest = field("WriteHlsManifest")
    WriteSegmentTimelineInRepresentation = field("WriteSegmentTimelineInRepresentation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CmafGroupSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashIsoGroupSettingsOutput:
    boto3_raw_data: "type_defs.DashIsoGroupSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AdditionalManifests(self):  # pragma: no cover
        return DashAdditionalManifestOutput.make_many(
            self.boto3_raw_data["AdditionalManifests"]
        )

    AudioChannelConfigSchemeIdUri = field("AudioChannelConfigSchemeIdUri")
    BaseUrl = field("BaseUrl")
    DashIFrameTrickPlayNameModifier = field("DashIFrameTrickPlayNameModifier")
    DashManifestStyle = field("DashManifestStyle")
    Destination = field("Destination")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return DestinationSettings.make_one(self.boto3_raw_data["DestinationSettings"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return DashIsoEncryptionSettingsOutput.make_one(
            self.boto3_raw_data["Encryption"]
        )

    FragmentLength = field("FragmentLength")
    HbbtvCompliance = field("HbbtvCompliance")
    ImageBasedTrickPlay = field("ImageBasedTrickPlay")

    @cached_property
    def ImageBasedTrickPlaySettings(self):  # pragma: no cover
        return DashIsoImageBasedTrickPlaySettings.make_one(
            self.boto3_raw_data["ImageBasedTrickPlaySettings"]
        )

    MinBufferTime = field("MinBufferTime")
    MinFinalSegmentLength = field("MinFinalSegmentLength")
    MpdManifestBandwidthType = field("MpdManifestBandwidthType")
    MpdProfile = field("MpdProfile")
    PtsOffsetHandlingForBFrames = field("PtsOffsetHandlingForBFrames")
    SegmentControl = field("SegmentControl")
    SegmentLength = field("SegmentLength")
    SegmentLengthControl = field("SegmentLengthControl")
    VideoCompositionOffsets = field("VideoCompositionOffsets")
    WriteSegmentTimelineInRepresentation = field("WriteSegmentTimelineInRepresentation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashIsoGroupSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashIsoGroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashIsoGroupSettings:
    boto3_raw_data: "type_defs.DashIsoGroupSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AdditionalManifests(self):  # pragma: no cover
        return DashAdditionalManifest.make_many(
            self.boto3_raw_data["AdditionalManifests"]
        )

    AudioChannelConfigSchemeIdUri = field("AudioChannelConfigSchemeIdUri")
    BaseUrl = field("BaseUrl")
    DashIFrameTrickPlayNameModifier = field("DashIFrameTrickPlayNameModifier")
    DashManifestStyle = field("DashManifestStyle")
    Destination = field("Destination")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return DestinationSettings.make_one(self.boto3_raw_data["DestinationSettings"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return DashIsoEncryptionSettings.make_one(self.boto3_raw_data["Encryption"])

    FragmentLength = field("FragmentLength")
    HbbtvCompliance = field("HbbtvCompliance")
    ImageBasedTrickPlay = field("ImageBasedTrickPlay")

    @cached_property
    def ImageBasedTrickPlaySettings(self):  # pragma: no cover
        return DashIsoImageBasedTrickPlaySettings.make_one(
            self.boto3_raw_data["ImageBasedTrickPlaySettings"]
        )

    MinBufferTime = field("MinBufferTime")
    MinFinalSegmentLength = field("MinFinalSegmentLength")
    MpdManifestBandwidthType = field("MpdManifestBandwidthType")
    MpdProfile = field("MpdProfile")
    PtsOffsetHandlingForBFrames = field("PtsOffsetHandlingForBFrames")
    SegmentControl = field("SegmentControl")
    SegmentLength = field("SegmentLength")
    SegmentLengthControl = field("SegmentLengthControl")
    VideoCompositionOffsets = field("VideoCompositionOffsets")
    WriteSegmentTimelineInRepresentation = field("WriteSegmentTimelineInRepresentation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashIsoGroupSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashIsoGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileGroupSettings:
    boto3_raw_data: "type_defs.FileGroupSettingsTypeDef" = dataclasses.field()

    Destination = field("Destination")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return DestinationSettings.make_one(self.boto3_raw_data["DestinationSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileGroupSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsGroupSettingsOutput:
    boto3_raw_data: "type_defs.HlsGroupSettingsOutputTypeDef" = dataclasses.field()

    AdMarkers = field("AdMarkers")

    @cached_property
    def AdditionalManifests(self):  # pragma: no cover
        return HlsAdditionalManifestOutput.make_many(
            self.boto3_raw_data["AdditionalManifests"]
        )

    AudioOnlyHeader = field("AudioOnlyHeader")
    BaseUrl = field("BaseUrl")

    @cached_property
    def CaptionLanguageMappings(self):  # pragma: no cover
        return HlsCaptionLanguageMapping.make_many(
            self.boto3_raw_data["CaptionLanguageMappings"]
        )

    CaptionLanguageSetting = field("CaptionLanguageSetting")
    CaptionSegmentLengthControl = field("CaptionSegmentLengthControl")
    ClientCache = field("ClientCache")
    CodecSpecification = field("CodecSpecification")
    Destination = field("Destination")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return DestinationSettings.make_one(self.boto3_raw_data["DestinationSettings"])

    DirectoryStructure = field("DirectoryStructure")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return HlsEncryptionSettingsOutput.make_one(self.boto3_raw_data["Encryption"])

    ImageBasedTrickPlay = field("ImageBasedTrickPlay")

    @cached_property
    def ImageBasedTrickPlaySettings(self):  # pragma: no cover
        return HlsImageBasedTrickPlaySettings.make_one(
            self.boto3_raw_data["ImageBasedTrickPlaySettings"]
        )

    ManifestCompression = field("ManifestCompression")
    ManifestDurationFormat = field("ManifestDurationFormat")
    MinFinalSegmentLength = field("MinFinalSegmentLength")
    MinSegmentLength = field("MinSegmentLength")
    OutputSelection = field("OutputSelection")
    ProgramDateTime = field("ProgramDateTime")
    ProgramDateTimePeriod = field("ProgramDateTimePeriod")
    ProgressiveWriteHlsManifest = field("ProgressiveWriteHlsManifest")
    SegmentControl = field("SegmentControl")
    SegmentLength = field("SegmentLength")
    SegmentLengthControl = field("SegmentLengthControl")
    SegmentsPerSubdirectory = field("SegmentsPerSubdirectory")
    StreamInfResolution = field("StreamInfResolution")
    TargetDurationCompatibilityMode = field("TargetDurationCompatibilityMode")
    TimedMetadataId3Frame = field("TimedMetadataId3Frame")
    TimedMetadataId3Period = field("TimedMetadataId3Period")
    TimestampDeltaMilliseconds = field("TimestampDeltaMilliseconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsGroupSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsGroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsGroupSettings:
    boto3_raw_data: "type_defs.HlsGroupSettingsTypeDef" = dataclasses.field()

    AdMarkers = field("AdMarkers")

    @cached_property
    def AdditionalManifests(self):  # pragma: no cover
        return HlsAdditionalManifest.make_many(
            self.boto3_raw_data["AdditionalManifests"]
        )

    AudioOnlyHeader = field("AudioOnlyHeader")
    BaseUrl = field("BaseUrl")

    @cached_property
    def CaptionLanguageMappings(self):  # pragma: no cover
        return HlsCaptionLanguageMapping.make_many(
            self.boto3_raw_data["CaptionLanguageMappings"]
        )

    CaptionLanguageSetting = field("CaptionLanguageSetting")
    CaptionSegmentLengthControl = field("CaptionSegmentLengthControl")
    ClientCache = field("ClientCache")
    CodecSpecification = field("CodecSpecification")
    Destination = field("Destination")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return DestinationSettings.make_one(self.boto3_raw_data["DestinationSettings"])

    DirectoryStructure = field("DirectoryStructure")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return HlsEncryptionSettings.make_one(self.boto3_raw_data["Encryption"])

    ImageBasedTrickPlay = field("ImageBasedTrickPlay")

    @cached_property
    def ImageBasedTrickPlaySettings(self):  # pragma: no cover
        return HlsImageBasedTrickPlaySettings.make_one(
            self.boto3_raw_data["ImageBasedTrickPlaySettings"]
        )

    ManifestCompression = field("ManifestCompression")
    ManifestDurationFormat = field("ManifestDurationFormat")
    MinFinalSegmentLength = field("MinFinalSegmentLength")
    MinSegmentLength = field("MinSegmentLength")
    OutputSelection = field("OutputSelection")
    ProgramDateTime = field("ProgramDateTime")
    ProgramDateTimePeriod = field("ProgramDateTimePeriod")
    ProgressiveWriteHlsManifest = field("ProgressiveWriteHlsManifest")
    SegmentControl = field("SegmentControl")
    SegmentLength = field("SegmentLength")
    SegmentLengthControl = field("SegmentLengthControl")
    SegmentsPerSubdirectory = field("SegmentsPerSubdirectory")
    StreamInfResolution = field("StreamInfResolution")
    TargetDurationCompatibilityMode = field("TargetDurationCompatibilityMode")
    TimedMetadataId3Frame = field("TimedMetadataId3Frame")
    TimedMetadataId3Period = field("TimedMetadataId3Period")
    TimestampDeltaMilliseconds = field("TimestampDeltaMilliseconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsGroupSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MsSmoothGroupSettingsOutput:
    boto3_raw_data: "type_defs.MsSmoothGroupSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AdditionalManifests(self):  # pragma: no cover
        return MsSmoothAdditionalManifestOutput.make_many(
            self.boto3_raw_data["AdditionalManifests"]
        )

    AudioDeduplication = field("AudioDeduplication")
    Destination = field("Destination")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return DestinationSettings.make_one(self.boto3_raw_data["DestinationSettings"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return MsSmoothEncryptionSettingsOutput.make_one(
            self.boto3_raw_data["Encryption"]
        )

    FragmentLength = field("FragmentLength")
    FragmentLengthControl = field("FragmentLengthControl")
    ManifestEncoding = field("ManifestEncoding")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MsSmoothGroupSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MsSmoothGroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MsSmoothGroupSettings:
    boto3_raw_data: "type_defs.MsSmoothGroupSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AdditionalManifests(self):  # pragma: no cover
        return MsSmoothAdditionalManifest.make_many(
            self.boto3_raw_data["AdditionalManifests"]
        )

    AudioDeduplication = field("AudioDeduplication")
    Destination = field("Destination")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return DestinationSettings.make_one(self.boto3_raw_data["DestinationSettings"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return MsSmoothEncryptionSettings.make_one(self.boto3_raw_data["Encryption"])

    FragmentLength = field("FragmentLength")
    FragmentLengthControl = field("FragmentLengthControl")
    ManifestEncoding = field("ManifestEncoding")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MsSmoothGroupSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MsSmoothGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoDescriptionOutput:
    boto3_raw_data: "type_defs.VideoDescriptionOutputTypeDef" = dataclasses.field()

    AfdSignaling = field("AfdSignaling")
    AntiAlias = field("AntiAlias")
    ChromaPositionMode = field("ChromaPositionMode")

    @cached_property
    def CodecSettings(self):  # pragma: no cover
        return VideoCodecSettingsOutput.make_one(self.boto3_raw_data["CodecSettings"])

    ColorMetadata = field("ColorMetadata")

    @cached_property
    def Crop(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Crop"])

    DropFrameTimecode = field("DropFrameTimecode")
    FixedAfd = field("FixedAfd")
    Height = field("Height")

    @cached_property
    def Position(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Position"])

    RespondToAfd = field("RespondToAfd")
    ScalingBehavior = field("ScalingBehavior")
    Sharpness = field("Sharpness")
    TimecodeInsertion = field("TimecodeInsertion")
    TimecodeTrack = field("TimecodeTrack")

    @cached_property
    def VideoPreprocessors(self):  # pragma: no cover
        return VideoPreprocessorOutput.make_one(
            self.boto3_raw_data["VideoPreprocessors"]
        )

    Width = field("Width")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoDescriptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoDescriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoDescription:
    boto3_raw_data: "type_defs.VideoDescriptionTypeDef" = dataclasses.field()

    AfdSignaling = field("AfdSignaling")
    AntiAlias = field("AntiAlias")
    ChromaPositionMode = field("ChromaPositionMode")

    @cached_property
    def CodecSettings(self):  # pragma: no cover
        return VideoCodecSettings.make_one(self.boto3_raw_data["CodecSettings"])

    ColorMetadata = field("ColorMetadata")

    @cached_property
    def Crop(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Crop"])

    DropFrameTimecode = field("DropFrameTimecode")
    FixedAfd = field("FixedAfd")
    Height = field("Height")

    @cached_property
    def Position(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Position"])

    RespondToAfd = field("RespondToAfd")
    ScalingBehavior = field("ScalingBehavior")
    Sharpness = field("Sharpness")
    TimecodeInsertion = field("TimecodeInsertion")
    TimecodeTrack = field("TimecodeTrack")

    @cached_property
    def VideoPreprocessors(self):  # pragma: no cover
        return VideoPreprocessor.make_one(self.boto3_raw_data["VideoPreprocessors"])

    Width = field("Width")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProbeResult:
    boto3_raw_data: "type_defs.ProbeResultTypeDef" = dataclasses.field()

    @cached_property
    def Container(self):  # pragma: no cover
        return Container.make_one(self.boto3_raw_data["Container"])

    @cached_property
    def Metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["Metadata"])

    @cached_property
    def TrackMappings(self):  # pragma: no cover
        return TrackMapping.make_many(self.boto3_raw_data["TrackMappings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProbeResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProbeResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputOutput:
    boto3_raw_data: "type_defs.InputOutputTypeDef" = dataclasses.field()

    AdvancedInputFilter = field("AdvancedInputFilter")

    @cached_property
    def AdvancedInputFilterSettings(self):  # pragma: no cover
        return AdvancedInputFilterSettings.make_one(
            self.boto3_raw_data["AdvancedInputFilterSettings"]
        )

    AudioSelectorGroups = field("AudioSelectorGroups")
    AudioSelectors = field("AudioSelectors")
    CaptionSelectors = field("CaptionSelectors")

    @cached_property
    def Crop(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Crop"])

    DeblockFilter = field("DeblockFilter")

    @cached_property
    def DecryptionSettings(self):  # pragma: no cover
        return InputDecryptionSettings.make_one(
            self.boto3_raw_data["DecryptionSettings"]
        )

    DenoiseFilter = field("DenoiseFilter")
    DolbyVisionMetadataXml = field("DolbyVisionMetadataXml")
    DynamicAudioSelectors = field("DynamicAudioSelectors")
    FileInput = field("FileInput")
    FilterEnable = field("FilterEnable")
    FilterStrength = field("FilterStrength")

    @cached_property
    def ImageInserter(self):  # pragma: no cover
        return ImageInserterOutput.make_one(self.boto3_raw_data["ImageInserter"])

    @cached_property
    def InputClippings(self):  # pragma: no cover
        return InputClipping.make_many(self.boto3_raw_data["InputClippings"])

    InputScanType = field("InputScanType")

    @cached_property
    def Position(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Position"])

    ProgramNumber = field("ProgramNumber")
    PsiControl = field("PsiControl")
    SupplementalImps = field("SupplementalImps")

    @cached_property
    def TamsSettings(self):  # pragma: no cover
        return InputTamsSettings.make_one(self.boto3_raw_data["TamsSettings"])

    TimecodeSource = field("TimecodeSource")
    TimecodeStart = field("TimecodeStart")

    @cached_property
    def VideoGenerator(self):  # pragma: no cover
        return InputVideoGenerator.make_one(self.boto3_raw_data["VideoGenerator"])

    @cached_property
    def VideoOverlays(self):  # pragma: no cover
        return VideoOverlayOutput.make_many(self.boto3_raw_data["VideoOverlays"])

    @cached_property
    def VideoSelector(self):  # pragma: no cover
        return VideoSelectorOutput.make_one(self.boto3_raw_data["VideoSelector"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputTemplateOutput:
    boto3_raw_data: "type_defs.InputTemplateOutputTypeDef" = dataclasses.field()

    AdvancedInputFilter = field("AdvancedInputFilter")

    @cached_property
    def AdvancedInputFilterSettings(self):  # pragma: no cover
        return AdvancedInputFilterSettings.make_one(
            self.boto3_raw_data["AdvancedInputFilterSettings"]
        )

    AudioSelectorGroups = field("AudioSelectorGroups")
    AudioSelectors = field("AudioSelectors")
    CaptionSelectors = field("CaptionSelectors")

    @cached_property
    def Crop(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Crop"])

    DeblockFilter = field("DeblockFilter")
    DenoiseFilter = field("DenoiseFilter")
    DolbyVisionMetadataXml = field("DolbyVisionMetadataXml")
    DynamicAudioSelectors = field("DynamicAudioSelectors")
    FilterEnable = field("FilterEnable")
    FilterStrength = field("FilterStrength")

    @cached_property
    def ImageInserter(self):  # pragma: no cover
        return ImageInserterOutput.make_one(self.boto3_raw_data["ImageInserter"])

    @cached_property
    def InputClippings(self):  # pragma: no cover
        return InputClipping.make_many(self.boto3_raw_data["InputClippings"])

    InputScanType = field("InputScanType")

    @cached_property
    def Position(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Position"])

    ProgramNumber = field("ProgramNumber")
    PsiControl = field("PsiControl")
    TimecodeSource = field("TimecodeSource")
    TimecodeStart = field("TimecodeStart")

    @cached_property
    def VideoOverlays(self):  # pragma: no cover
        return VideoOverlayOutput.make_many(self.boto3_raw_data["VideoOverlays"])

    @cached_property
    def VideoSelector(self):  # pragma: no cover
        return VideoSelectorOutput.make_one(self.boto3_raw_data["VideoSelector"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputTemplate:
    boto3_raw_data: "type_defs.InputTemplateTypeDef" = dataclasses.field()

    AdvancedInputFilter = field("AdvancedInputFilter")

    @cached_property
    def AdvancedInputFilterSettings(self):  # pragma: no cover
        return AdvancedInputFilterSettings.make_one(
            self.boto3_raw_data["AdvancedInputFilterSettings"]
        )

    AudioSelectorGroups = field("AudioSelectorGroups")
    AudioSelectors = field("AudioSelectors")
    CaptionSelectors = field("CaptionSelectors")

    @cached_property
    def Crop(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Crop"])

    DeblockFilter = field("DeblockFilter")
    DenoiseFilter = field("DenoiseFilter")
    DolbyVisionMetadataXml = field("DolbyVisionMetadataXml")
    DynamicAudioSelectors = field("DynamicAudioSelectors")
    FilterEnable = field("FilterEnable")
    FilterStrength = field("FilterStrength")

    @cached_property
    def ImageInserter(self):  # pragma: no cover
        return ImageInserter.make_one(self.boto3_raw_data["ImageInserter"])

    @cached_property
    def InputClippings(self):  # pragma: no cover
        return InputClipping.make_many(self.boto3_raw_data["InputClippings"])

    InputScanType = field("InputScanType")

    @cached_property
    def Position(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Position"])

    ProgramNumber = field("ProgramNumber")
    PsiControl = field("PsiControl")
    TimecodeSource = field("TimecodeSource")
    TimecodeStart = field("TimecodeStart")

    @cached_property
    def VideoOverlays(self):  # pragma: no cover
        return VideoOverlay.make_many(self.boto3_raw_data["VideoOverlays"])

    @cached_property
    def VideoSelector(self):  # pragma: no cover
        return VideoSelector.make_one(self.boto3_raw_data["VideoSelector"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputTemplateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Input:
    boto3_raw_data: "type_defs.InputTypeDef" = dataclasses.field()

    AdvancedInputFilter = field("AdvancedInputFilter")

    @cached_property
    def AdvancedInputFilterSettings(self):  # pragma: no cover
        return AdvancedInputFilterSettings.make_one(
            self.boto3_raw_data["AdvancedInputFilterSettings"]
        )

    AudioSelectorGroups = field("AudioSelectorGroups")
    AudioSelectors = field("AudioSelectors")
    CaptionSelectors = field("CaptionSelectors")

    @cached_property
    def Crop(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Crop"])

    DeblockFilter = field("DeblockFilter")

    @cached_property
    def DecryptionSettings(self):  # pragma: no cover
        return InputDecryptionSettings.make_one(
            self.boto3_raw_data["DecryptionSettings"]
        )

    DenoiseFilter = field("DenoiseFilter")
    DolbyVisionMetadataXml = field("DolbyVisionMetadataXml")
    DynamicAudioSelectors = field("DynamicAudioSelectors")
    FileInput = field("FileInput")
    FilterEnable = field("FilterEnable")
    FilterStrength = field("FilterStrength")

    @cached_property
    def ImageInserter(self):  # pragma: no cover
        return ImageInserter.make_one(self.boto3_raw_data["ImageInserter"])

    @cached_property
    def InputClippings(self):  # pragma: no cover
        return InputClipping.make_many(self.boto3_raw_data["InputClippings"])

    InputScanType = field("InputScanType")

    @cached_property
    def Position(self):  # pragma: no cover
        return Rectangle.make_one(self.boto3_raw_data["Position"])

    ProgramNumber = field("ProgramNumber")
    PsiControl = field("PsiControl")
    SupplementalImps = field("SupplementalImps")

    @cached_property
    def TamsSettings(self):  # pragma: no cover
        return InputTamsSettings.make_one(self.boto3_raw_data["TamsSettings"])

    TimecodeSource = field("TimecodeSource")
    TimecodeStart = field("TimecodeStart")

    @cached_property
    def VideoGenerator(self):  # pragma: no cover
        return InputVideoGenerator.make_one(self.boto3_raw_data["VideoGenerator"])

    @cached_property
    def VideoOverlays(self):  # pragma: no cover
        return VideoOverlay.make_many(self.boto3_raw_data["VideoOverlays"])

    @cached_property
    def VideoSelector(self):  # pragma: no cover
        return VideoSelector.make_one(self.boto3_raw_data["VideoSelector"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputGroupSettingsOutput:
    boto3_raw_data: "type_defs.OutputGroupSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CmafGroupSettings(self):  # pragma: no cover
        return CmafGroupSettingsOutput.make_one(
            self.boto3_raw_data["CmafGroupSettings"]
        )

    @cached_property
    def DashIsoGroupSettings(self):  # pragma: no cover
        return DashIsoGroupSettingsOutput.make_one(
            self.boto3_raw_data["DashIsoGroupSettings"]
        )

    @cached_property
    def FileGroupSettings(self):  # pragma: no cover
        return FileGroupSettings.make_one(self.boto3_raw_data["FileGroupSettings"])

    @cached_property
    def HlsGroupSettings(self):  # pragma: no cover
        return HlsGroupSettingsOutput.make_one(self.boto3_raw_data["HlsGroupSettings"])

    @cached_property
    def MsSmoothGroupSettings(self):  # pragma: no cover
        return MsSmoothGroupSettingsOutput.make_one(
            self.boto3_raw_data["MsSmoothGroupSettings"]
        )

    PerFrameMetrics = field("PerFrameMetrics")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputGroupSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputGroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputGroupSettings:
    boto3_raw_data: "type_defs.OutputGroupSettingsTypeDef" = dataclasses.field()

    @cached_property
    def CmafGroupSettings(self):  # pragma: no cover
        return CmafGroupSettings.make_one(self.boto3_raw_data["CmafGroupSettings"])

    @cached_property
    def DashIsoGroupSettings(self):  # pragma: no cover
        return DashIsoGroupSettings.make_one(
            self.boto3_raw_data["DashIsoGroupSettings"]
        )

    @cached_property
    def FileGroupSettings(self):  # pragma: no cover
        return FileGroupSettings.make_one(self.boto3_raw_data["FileGroupSettings"])

    @cached_property
    def HlsGroupSettings(self):  # pragma: no cover
        return HlsGroupSettings.make_one(self.boto3_raw_data["HlsGroupSettings"])

    @cached_property
    def MsSmoothGroupSettings(self):  # pragma: no cover
        return MsSmoothGroupSettings.make_one(
            self.boto3_raw_data["MsSmoothGroupSettings"]
        )

    PerFrameMetrics = field("PerFrameMetrics")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputGroupSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Extra:
    boto3_raw_data: "type_defs.ExtraTypeDef" = dataclasses.field()

    @cached_property
    def AudioDescriptions(self):  # pragma: no cover
        return AudioDescriptionOutput.make_many(
            self.boto3_raw_data["AudioDescriptions"]
        )

    @cached_property
    def CaptionDescriptions(self):  # pragma: no cover
        return CaptionDescriptionOutput.make_many(
            self.boto3_raw_data["CaptionDescriptions"]
        )

    @cached_property
    def ContainerSettings(self):  # pragma: no cover
        return ContainerSettingsOutput.make_one(
            self.boto3_raw_data["ContainerSettings"]
        )

    Extension = field("Extension")
    NameModifier = field("NameModifier")

    @cached_property
    def OutputSettings(self):  # pragma: no cover
        return OutputSettings.make_one(self.boto3_raw_data["OutputSettings"])

    Preset = field("Preset")

    @cached_property
    def VideoDescription(self):  # pragma: no cover
        return VideoDescriptionOutput.make_one(self.boto3_raw_data["VideoDescription"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtraTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtraTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PresetSettingsOutput:
    boto3_raw_data: "type_defs.PresetSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AudioDescriptions(self):  # pragma: no cover
        return AudioDescriptionOutput.make_many(
            self.boto3_raw_data["AudioDescriptions"]
        )

    @cached_property
    def CaptionDescriptions(self):  # pragma: no cover
        return CaptionDescriptionPresetOutput.make_many(
            self.boto3_raw_data["CaptionDescriptions"]
        )

    @cached_property
    def ContainerSettings(self):  # pragma: no cover
        return ContainerSettingsOutput.make_one(
            self.boto3_raw_data["ContainerSettings"]
        )

    @cached_property
    def VideoDescription(self):  # pragma: no cover
        return VideoDescriptionOutput.make_one(self.boto3_raw_data["VideoDescription"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PresetSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PresetSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Output:
    boto3_raw_data: "type_defs.OutputTypeDef" = dataclasses.field()

    @cached_property
    def AudioDescriptions(self):  # pragma: no cover
        return AudioDescription.make_many(self.boto3_raw_data["AudioDescriptions"])

    @cached_property
    def CaptionDescriptions(self):  # pragma: no cover
        return CaptionDescription.make_many(self.boto3_raw_data["CaptionDescriptions"])

    @cached_property
    def ContainerSettings(self):  # pragma: no cover
        return ContainerSettings.make_one(self.boto3_raw_data["ContainerSettings"])

    Extension = field("Extension")
    NameModifier = field("NameModifier")

    @cached_property
    def OutputSettings(self):  # pragma: no cover
        return OutputSettings.make_one(self.boto3_raw_data["OutputSettings"])

    Preset = field("Preset")

    @cached_property
    def VideoDescription(self):  # pragma: no cover
        return VideoDescription.make_one(self.boto3_raw_data["VideoDescription"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PresetSettings:
    boto3_raw_data: "type_defs.PresetSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AudioDescriptions(self):  # pragma: no cover
        return AudioDescription.make_many(self.boto3_raw_data["AudioDescriptions"])

    @cached_property
    def CaptionDescriptions(self):  # pragma: no cover
        return CaptionDescriptionPreset.make_many(
            self.boto3_raw_data["CaptionDescriptions"]
        )

    @cached_property
    def ContainerSettings(self):  # pragma: no cover
        return ContainerSettings.make_one(self.boto3_raw_data["ContainerSettings"])

    @cached_property
    def VideoDescription(self):  # pragma: no cover
        return VideoDescription.make_one(self.boto3_raw_data["VideoDescription"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PresetSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PresetSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProbeResponse:
    boto3_raw_data: "type_defs.ProbeResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProbeResults(self):  # pragma: no cover
        return ProbeResult.make_many(self.boto3_raw_data["ProbeResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProbeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProbeResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputGroupOutput:
    boto3_raw_data: "type_defs.OutputGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def AutomatedEncodingSettings(self):  # pragma: no cover
        return AutomatedEncodingSettingsOutput.make_one(
            self.boto3_raw_data["AutomatedEncodingSettings"]
        )

    CustomName = field("CustomName")
    Name = field("Name")

    @cached_property
    def OutputGroupSettings(self):  # pragma: no cover
        return OutputGroupSettingsOutput.make_one(
            self.boto3_raw_data["OutputGroupSettings"]
        )

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Extra.make_many(self.boto3_raw_data["Outputs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputGroupOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Preset:
    boto3_raw_data: "type_defs.PresetTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Settings(self):  # pragma: no cover
        return PresetSettingsOutput.make_one(self.boto3_raw_data["Settings"])

    Arn = field("Arn")
    Category = field("Category")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    LastUpdated = field("LastUpdated")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PresetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PresetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputGroup:
    boto3_raw_data: "type_defs.OutputGroupTypeDef" = dataclasses.field()

    @cached_property
    def AutomatedEncodingSettings(self):  # pragma: no cover
        return AutomatedEncodingSettings.make_one(
            self.boto3_raw_data["AutomatedEncodingSettings"]
        )

    CustomName = field("CustomName")
    Name = field("Name")

    @cached_property
    def OutputGroupSettings(self):  # pragma: no cover
        return OutputGroupSettings.make_one(self.boto3_raw_data["OutputGroupSettings"])

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["Outputs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSettingsOutput:
    boto3_raw_data: "type_defs.JobSettingsOutputTypeDef" = dataclasses.field()

    AdAvailOffset = field("AdAvailOffset")

    @cached_property
    def AvailBlanking(self):  # pragma: no cover
        return AvailBlanking.make_one(self.boto3_raw_data["AvailBlanking"])

    @cached_property
    def ColorConversion3DLUTSettings(self):  # pragma: no cover
        return ColorConversion3DLUTSetting.make_many(
            self.boto3_raw_data["ColorConversion3DLUTSettings"]
        )

    @cached_property
    def Esam(self):  # pragma: no cover
        return EsamSettings.make_one(self.boto3_raw_data["Esam"])

    @cached_property
    def ExtendedDataServices(self):  # pragma: no cover
        return ExtendedDataServices.make_one(
            self.boto3_raw_data["ExtendedDataServices"]
        )

    FollowSource = field("FollowSource")

    @cached_property
    def Inputs(self):  # pragma: no cover
        return InputOutput.make_many(self.boto3_raw_data["Inputs"])

    @cached_property
    def KantarWatermark(self):  # pragma: no cover
        return KantarWatermarkSettings.make_one(self.boto3_raw_data["KantarWatermark"])

    @cached_property
    def MotionImageInserter(self):  # pragma: no cover
        return MotionImageInserter.make_one(self.boto3_raw_data["MotionImageInserter"])

    @cached_property
    def NielsenConfiguration(self):  # pragma: no cover
        return NielsenConfiguration.make_one(
            self.boto3_raw_data["NielsenConfiguration"]
        )

    @cached_property
    def NielsenNonLinearWatermark(self):  # pragma: no cover
        return NielsenNonLinearWatermarkSettings.make_one(
            self.boto3_raw_data["NielsenNonLinearWatermark"]
        )

    @cached_property
    def OutputGroups(self):  # pragma: no cover
        return OutputGroupOutput.make_many(self.boto3_raw_data["OutputGroups"])

    @cached_property
    def TimecodeConfig(self):  # pragma: no cover
        return TimecodeConfig.make_one(self.boto3_raw_data["TimecodeConfig"])

    @cached_property
    def TimedMetadataInsertion(self):  # pragma: no cover
        return TimedMetadataInsertionOutput.make_one(
            self.boto3_raw_data["TimedMetadataInsertion"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSettingsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTemplateSettingsOutput:
    boto3_raw_data: "type_defs.JobTemplateSettingsOutputTypeDef" = dataclasses.field()

    AdAvailOffset = field("AdAvailOffset")

    @cached_property
    def AvailBlanking(self):  # pragma: no cover
        return AvailBlanking.make_one(self.boto3_raw_data["AvailBlanking"])

    @cached_property
    def ColorConversion3DLUTSettings(self):  # pragma: no cover
        return ColorConversion3DLUTSetting.make_many(
            self.boto3_raw_data["ColorConversion3DLUTSettings"]
        )

    @cached_property
    def Esam(self):  # pragma: no cover
        return EsamSettings.make_one(self.boto3_raw_data["Esam"])

    @cached_property
    def ExtendedDataServices(self):  # pragma: no cover
        return ExtendedDataServices.make_one(
            self.boto3_raw_data["ExtendedDataServices"]
        )

    FollowSource = field("FollowSource")

    @cached_property
    def Inputs(self):  # pragma: no cover
        return InputTemplateOutput.make_many(self.boto3_raw_data["Inputs"])

    @cached_property
    def KantarWatermark(self):  # pragma: no cover
        return KantarWatermarkSettings.make_one(self.boto3_raw_data["KantarWatermark"])

    @cached_property
    def MotionImageInserter(self):  # pragma: no cover
        return MotionImageInserter.make_one(self.boto3_raw_data["MotionImageInserter"])

    @cached_property
    def NielsenConfiguration(self):  # pragma: no cover
        return NielsenConfiguration.make_one(
            self.boto3_raw_data["NielsenConfiguration"]
        )

    @cached_property
    def NielsenNonLinearWatermark(self):  # pragma: no cover
        return NielsenNonLinearWatermarkSettings.make_one(
            self.boto3_raw_data["NielsenNonLinearWatermark"]
        )

    @cached_property
    def OutputGroups(self):  # pragma: no cover
        return OutputGroupOutput.make_many(self.boto3_raw_data["OutputGroups"])

    @cached_property
    def TimecodeConfig(self):  # pragma: no cover
        return TimecodeConfig.make_one(self.boto3_raw_data["TimecodeConfig"])

    @cached_property
    def TimedMetadataInsertion(self):  # pragma: no cover
        return TimedMetadataInsertionOutput.make_one(
            self.boto3_raw_data["TimedMetadataInsertion"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobTemplateSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobTemplateSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePresetResponse:
    boto3_raw_data: "type_defs.CreatePresetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Preset(self):  # pragma: no cover
        return Preset.make_one(self.boto3_raw_data["Preset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePresetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePresetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPresetResponse:
    boto3_raw_data: "type_defs.GetPresetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Preset(self):  # pragma: no cover
        return Preset.make_one(self.boto3_raw_data["Preset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPresetResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPresetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPresetsResponse:
    boto3_raw_data: "type_defs.ListPresetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Presets(self):  # pragma: no cover
        return Preset.make_many(self.boto3_raw_data["Presets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPresetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPresetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePresetResponse:
    boto3_raw_data: "type_defs.UpdatePresetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Preset(self):  # pragma: no cover
        return Preset.make_one(self.boto3_raw_data["Preset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePresetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePresetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSettings:
    boto3_raw_data: "type_defs.JobSettingsTypeDef" = dataclasses.field()

    AdAvailOffset = field("AdAvailOffset")

    @cached_property
    def AvailBlanking(self):  # pragma: no cover
        return AvailBlanking.make_one(self.boto3_raw_data["AvailBlanking"])

    @cached_property
    def ColorConversion3DLUTSettings(self):  # pragma: no cover
        return ColorConversion3DLUTSetting.make_many(
            self.boto3_raw_data["ColorConversion3DLUTSettings"]
        )

    @cached_property
    def Esam(self):  # pragma: no cover
        return EsamSettings.make_one(self.boto3_raw_data["Esam"])

    @cached_property
    def ExtendedDataServices(self):  # pragma: no cover
        return ExtendedDataServices.make_one(
            self.boto3_raw_data["ExtendedDataServices"]
        )

    FollowSource = field("FollowSource")

    @cached_property
    def Inputs(self):  # pragma: no cover
        return Input.make_many(self.boto3_raw_data["Inputs"])

    @cached_property
    def KantarWatermark(self):  # pragma: no cover
        return KantarWatermarkSettings.make_one(self.boto3_raw_data["KantarWatermark"])

    @cached_property
    def MotionImageInserter(self):  # pragma: no cover
        return MotionImageInserter.make_one(self.boto3_raw_data["MotionImageInserter"])

    @cached_property
    def NielsenConfiguration(self):  # pragma: no cover
        return NielsenConfiguration.make_one(
            self.boto3_raw_data["NielsenConfiguration"]
        )

    @cached_property
    def NielsenNonLinearWatermark(self):  # pragma: no cover
        return NielsenNonLinearWatermarkSettings.make_one(
            self.boto3_raw_data["NielsenNonLinearWatermark"]
        )

    @cached_property
    def OutputGroups(self):  # pragma: no cover
        return OutputGroup.make_many(self.boto3_raw_data["OutputGroups"])

    @cached_property
    def TimecodeConfig(self):  # pragma: no cover
        return TimecodeConfig.make_one(self.boto3_raw_data["TimecodeConfig"])

    @cached_property
    def TimedMetadataInsertion(self):  # pragma: no cover
        return TimedMetadataInsertion.make_one(
            self.boto3_raw_data["TimedMetadataInsertion"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTemplateSettings:
    boto3_raw_data: "type_defs.JobTemplateSettingsTypeDef" = dataclasses.field()

    AdAvailOffset = field("AdAvailOffset")

    @cached_property
    def AvailBlanking(self):  # pragma: no cover
        return AvailBlanking.make_one(self.boto3_raw_data["AvailBlanking"])

    @cached_property
    def ColorConversion3DLUTSettings(self):  # pragma: no cover
        return ColorConversion3DLUTSetting.make_many(
            self.boto3_raw_data["ColorConversion3DLUTSettings"]
        )

    @cached_property
    def Esam(self):  # pragma: no cover
        return EsamSettings.make_one(self.boto3_raw_data["Esam"])

    @cached_property
    def ExtendedDataServices(self):  # pragma: no cover
        return ExtendedDataServices.make_one(
            self.boto3_raw_data["ExtendedDataServices"]
        )

    FollowSource = field("FollowSource")

    @cached_property
    def Inputs(self):  # pragma: no cover
        return InputTemplate.make_many(self.boto3_raw_data["Inputs"])

    @cached_property
    def KantarWatermark(self):  # pragma: no cover
        return KantarWatermarkSettings.make_one(self.boto3_raw_data["KantarWatermark"])

    @cached_property
    def MotionImageInserter(self):  # pragma: no cover
        return MotionImageInserter.make_one(self.boto3_raw_data["MotionImageInserter"])

    @cached_property
    def NielsenConfiguration(self):  # pragma: no cover
        return NielsenConfiguration.make_one(
            self.boto3_raw_data["NielsenConfiguration"]
        )

    @cached_property
    def NielsenNonLinearWatermark(self):  # pragma: no cover
        return NielsenNonLinearWatermarkSettings.make_one(
            self.boto3_raw_data["NielsenNonLinearWatermark"]
        )

    @cached_property
    def OutputGroups(self):  # pragma: no cover
        return OutputGroup.make_many(self.boto3_raw_data["OutputGroups"])

    @cached_property
    def TimecodeConfig(self):  # pragma: no cover
        return TimecodeConfig.make_one(self.boto3_raw_data["TimecodeConfig"])

    @cached_property
    def TimedMetadataInsertion(self):  # pragma: no cover
        return TimedMetadataInsertion.make_one(
            self.boto3_raw_data["TimedMetadataInsertion"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobTemplateSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobTemplateSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePresetRequest:
    boto3_raw_data: "type_defs.CreatePresetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Settings = field("Settings")
    Category = field("Category")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePresetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePresetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePresetRequest:
    boto3_raw_data: "type_defs.UpdatePresetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Category = field("Category")
    Description = field("Description")
    Settings = field("Settings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePresetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePresetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Job:
    boto3_raw_data: "type_defs.JobTypeDef" = dataclasses.field()

    Role = field("Role")

    @cached_property
    def Settings(self):  # pragma: no cover
        return JobSettingsOutput.make_one(self.boto3_raw_data["Settings"])

    @cached_property
    def AccelerationSettings(self):  # pragma: no cover
        return AccelerationSettings.make_one(
            self.boto3_raw_data["AccelerationSettings"]
        )

    AccelerationStatus = field("AccelerationStatus")
    Arn = field("Arn")
    BillingTagsSource = field("BillingTagsSource")
    ClientRequestToken = field("ClientRequestToken")
    CreatedAt = field("CreatedAt")
    CurrentPhase = field("CurrentPhase")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @cached_property
    def HopDestinations(self):  # pragma: no cover
        return HopDestination.make_many(self.boto3_raw_data["HopDestinations"])

    Id = field("Id")
    JobEngineVersionRequested = field("JobEngineVersionRequested")
    JobEngineVersionUsed = field("JobEngineVersionUsed")
    JobPercentComplete = field("JobPercentComplete")
    JobTemplate = field("JobTemplate")
    LastShareDetails = field("LastShareDetails")

    @cached_property
    def Messages(self):  # pragma: no cover
        return JobMessages.make_one(self.boto3_raw_data["Messages"])

    @cached_property
    def OutputGroupDetails(self):  # pragma: no cover
        return OutputGroupDetail.make_many(self.boto3_raw_data["OutputGroupDetails"])

    Priority = field("Priority")
    Queue = field("Queue")

    @cached_property
    def QueueTransitions(self):  # pragma: no cover
        return QueueTransition.make_many(self.boto3_raw_data["QueueTransitions"])

    RetryCount = field("RetryCount")
    ShareStatus = field("ShareStatus")
    SimulateReservedQueue = field("SimulateReservedQueue")
    Status = field("Status")
    StatusUpdateInterval = field("StatusUpdateInterval")

    @cached_property
    def Timing(self):  # pragma: no cover
        return Timing.make_one(self.boto3_raw_data["Timing"])

    UserMetadata = field("UserMetadata")

    @cached_property
    def Warnings(self):  # pragma: no cover
        return WarningGroup.make_many(self.boto3_raw_data["Warnings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTemplate:
    boto3_raw_data: "type_defs.JobTemplateTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Settings(self):  # pragma: no cover
        return JobTemplateSettingsOutput.make_one(self.boto3_raw_data["Settings"])

    @cached_property
    def AccelerationSettings(self):  # pragma: no cover
        return AccelerationSettings.make_one(
            self.boto3_raw_data["AccelerationSettings"]
        )

    Arn = field("Arn")
    Category = field("Category")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def HopDestinations(self):  # pragma: no cover
        return HopDestination.make_many(self.boto3_raw_data["HopDestinations"])

    LastUpdated = field("LastUpdated")
    Priority = field("Priority")
    Queue = field("Queue")
    StatusUpdateInterval = field("StatusUpdateInterval")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTemplateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobResponse:
    boto3_raw_data: "type_defs.CreateJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def Job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["Job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobResponse:
    boto3_raw_data: "type_defs.GetJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def Job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["Job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsResponse:
    boto3_raw_data: "type_defs.ListJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["Jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchJobsResponse:
    boto3_raw_data: "type_defs.SearchJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["Jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobTemplateResponse:
    boto3_raw_data: "type_defs.CreateJobTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def JobTemplate(self):  # pragma: no cover
        return JobTemplate.make_one(self.boto3_raw_data["JobTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobTemplateResponse:
    boto3_raw_data: "type_defs.GetJobTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def JobTemplate(self):  # pragma: no cover
        return JobTemplate.make_one(self.boto3_raw_data["JobTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesResponse:
    boto3_raw_data: "type_defs.ListJobTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def JobTemplates(self):  # pragma: no cover
        return JobTemplate.make_many(self.boto3_raw_data["JobTemplates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobTemplateResponse:
    boto3_raw_data: "type_defs.UpdateJobTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def JobTemplate(self):  # pragma: no cover
        return JobTemplate.make_one(self.boto3_raw_data["JobTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobRequest:
    boto3_raw_data: "type_defs.CreateJobRequestTypeDef" = dataclasses.field()

    Role = field("Role")
    Settings = field("Settings")

    @cached_property
    def AccelerationSettings(self):  # pragma: no cover
        return AccelerationSettings.make_one(
            self.boto3_raw_data["AccelerationSettings"]
        )

    BillingTagsSource = field("BillingTagsSource")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def HopDestinations(self):  # pragma: no cover
        return HopDestination.make_many(self.boto3_raw_data["HopDestinations"])

    JobEngineVersion = field("JobEngineVersion")
    JobTemplate = field("JobTemplate")
    Priority = field("Priority")
    Queue = field("Queue")
    SimulateReservedQueue = field("SimulateReservedQueue")
    StatusUpdateInterval = field("StatusUpdateInterval")
    Tags = field("Tags")
    UserMetadata = field("UserMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobTemplateRequest:
    boto3_raw_data: "type_defs.CreateJobTemplateRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Settings = field("Settings")

    @cached_property
    def AccelerationSettings(self):  # pragma: no cover
        return AccelerationSettings.make_one(
            self.boto3_raw_data["AccelerationSettings"]
        )

    Category = field("Category")
    Description = field("Description")

    @cached_property
    def HopDestinations(self):  # pragma: no cover
        return HopDestination.make_many(self.boto3_raw_data["HopDestinations"])

    Priority = field("Priority")
    Queue = field("Queue")
    StatusUpdateInterval = field("StatusUpdateInterval")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobTemplateRequest:
    boto3_raw_data: "type_defs.UpdateJobTemplateRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def AccelerationSettings(self):  # pragma: no cover
        return AccelerationSettings.make_one(
            self.boto3_raw_data["AccelerationSettings"]
        )

    Category = field("Category")
    Description = field("Description")

    @cached_property
    def HopDestinations(self):  # pragma: no cover
        return HopDestination.make_many(self.boto3_raw_data["HopDestinations"])

    Priority = field("Priority")
    Queue = field("Queue")
    Settings = field("Settings")
    StatusUpdateInterval = field("StatusUpdateInterval")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
