# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_medialive import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AacSettings:
    boto3_raw_data: "type_defs.AacSettingsTypeDef" = dataclasses.field()

    Bitrate = field("Bitrate")
    CodingMode = field("CodingMode")
    InputType = field("InputType")
    Profile = field("Profile")
    RateControlMode = field("RateControlMode")
    RawFormat = field("RawFormat")
    SampleRate = field("SampleRate")
    Spec = field("Spec")
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
    DrcProfile = field("DrcProfile")
    LfeFilter = field("LfeFilter")
    MetadataControl = field("MetadataControl")
    AttenuationControl = field("AttenuationControl")

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
class AcceptInputDeviceTransferRequest:
    boto3_raw_data: "type_defs.AcceptInputDeviceTransferRequestTypeDef" = (
        dataclasses.field()
    )

    InputDeviceId = field("InputDeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcceptInputDeviceTransferRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptInputDeviceTransferRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountConfiguration:
    boto3_raw_data: "type_defs.AccountConfigurationTypeDef" = dataclasses.field()

    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputLocationRef:
    boto3_raw_data: "type_defs.OutputLocationRefTypeDef" = dataclasses.field()

    DestinationRefId = field("DestinationRefId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputLocationRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputLocationRefTypeDef"]
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

    SourceAncillaryChannelNumber = field("SourceAncillaryChannelNumber")

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
class AnywhereSettings:
    boto3_raw_data: "type_defs.AnywhereSettingsTypeDef" = dataclasses.field()

    ChannelPlacementGroupId = field("ChannelPlacementGroupId")
    ClusterId = field("ClusterId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnywhereSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnywhereSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveS3Settings:
    boto3_raw_data: "type_defs.ArchiveS3SettingsTypeDef" = dataclasses.field()

    CannedAcl = field("CannedAcl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchiveS3SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveS3SettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputChannelLevel:
    boto3_raw_data: "type_defs.InputChannelLevelTypeDef" = dataclasses.field()

    Gain = field("Gain")
    InputChannel = field("InputChannel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputChannelLevelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputChannelLevelTypeDef"]
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
    CodingMode = field("CodingMode")
    Dialnorm = field("Dialnorm")
    DrcLine = field("DrcLine")
    DrcRf = field("DrcRf")
    HeightTrim = field("HeightTrim")
    SurroundTrim = field("SurroundTrim")

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
    DrcLine = field("DrcLine")
    DrcRf = field("DrcRf")
    LfeControl = field("LfeControl")
    LfeFilter = field("LfeFilter")
    LoRoCenterMixLevel = field("LoRoCenterMixLevel")
    LoRoSurroundMixLevel = field("LoRoSurroundMixLevel")
    LtRtCenterMixLevel = field("LtRtCenterMixLevel")
    LtRtSurroundMixLevel = field("LtRtSurroundMixLevel")
    MetadataControl = field("MetadataControl")
    PassthroughControl = field("PassthroughControl")
    PhaseControl = field("PhaseControl")
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
class Mp2Settings:
    boto3_raw_data: "type_defs.Mp2SettingsTypeDef" = dataclasses.field()

    Bitrate = field("Bitrate")
    CodingMode = field("CodingMode")
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
class WavSettings:
    boto3_raw_data: "type_defs.WavSettingsTypeDef" = dataclasses.field()

    BitDepth = field("BitDepth")
    CodingMode = field("CodingMode")
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
    TargetLkfs = field("TargetLkfs")

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
class AudioDolbyEDecode:
    boto3_raw_data: "type_defs.AudioDolbyEDecodeTypeDef" = dataclasses.field()

    ProgramSelection = field("ProgramSelection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioDolbyEDecodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioDolbyEDecodeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioHlsRenditionSelection:
    boto3_raw_data: "type_defs.AudioHlsRenditionSelectionTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioHlsRenditionSelectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioHlsRenditionSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioLanguageSelection:
    boto3_raw_data: "type_defs.AudioLanguageSelectionTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")
    LanguageSelectionPolicy = field("LanguageSelectionPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioLanguageSelectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioLanguageSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputLocation:
    boto3_raw_data: "type_defs.InputLocationTypeDef" = dataclasses.field()

    Uri = field("Uri")
    PasswordParam = field("PasswordParam")
    Username = field("Username")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioPidSelection:
    boto3_raw_data: "type_defs.AudioPidSelectionTypeDef" = dataclasses.field()

    Pid = field("Pid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioPidSelectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioPidSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioSilenceFailoverSettings:
    boto3_raw_data: "type_defs.AudioSilenceFailoverSettingsTypeDef" = (
        dataclasses.field()
    )

    AudioSelectorName = field("AudioSelectorName")
    AudioSilenceThresholdMsec = field("AudioSilenceThresholdMsec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioSilenceFailoverSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioSilenceFailoverSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioTrack:
    boto3_raw_data: "type_defs.AudioTrackTypeDef" = dataclasses.field()

    Track = field("Track")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioTrackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudioTrackTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Hdr10Settings:
    boto3_raw_data: "type_defs.Hdr10SettingsTypeDef" = dataclasses.field()

    MaxCll = field("MaxCll")
    MaxFall = field("MaxFall")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Hdr10SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Hdr10SettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimecodeBurninSettings:
    boto3_raw_data: "type_defs.TimecodeBurninSettingsTypeDef" = dataclasses.field()

    FontSize = field("FontSize")
    Position = field("Position")
    Prefix = field("Prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimecodeBurninSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimecodeBurninSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Esam:
    boto3_raw_data: "type_defs.EsamTypeDef" = dataclasses.field()

    AcquisitionPointId = field("AcquisitionPointId")
    PoisEndpoint = field("PoisEndpoint")
    AdAvailOffset = field("AdAvailOffset")
    PasswordParam = field("PasswordParam")
    Username = field("Username")
    ZoneIdentity = field("ZoneIdentity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EsamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EsamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35SpliceInsert:
    boto3_raw_data: "type_defs.Scte35SpliceInsertTypeDef" = dataclasses.field()

    AdAvailOffset = field("AdAvailOffset")
    NoRegionalBlackoutFlag = field("NoRegionalBlackoutFlag")
    WebDeliveryAllowedFlag = field("WebDeliveryAllowedFlag")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Scte35SpliceInsertTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35SpliceInsertTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35TimeSignalApos:
    boto3_raw_data: "type_defs.Scte35TimeSignalAposTypeDef" = dataclasses.field()

    AdAvailOffset = field("AdAvailOffset")
    NoRegionalBlackoutFlag = field("NoRegionalBlackoutFlag")
    WebDeliveryAllowedFlag = field("WebDeliveryAllowedFlag")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Scte35TimeSignalAposTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35TimeSignalAposTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BandwidthReductionFilterSettings:
    boto3_raw_data: "type_defs.BandwidthReductionFilterSettingsTypeDef" = (
        dataclasses.field()
    )

    PostFilterSharpening = field("PostFilterSharpening")
    Strength = field("Strength")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BandwidthReductionFilterSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BandwidthReductionFilterSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteRequest:
    boto3_raw_data: "type_defs.BatchDeleteRequestTypeDef" = dataclasses.field()

    ChannelIds = field("ChannelIds")
    InputIds = field("InputIds")
    InputSecurityGroupIds = field("InputSecurityGroupIds")
    MultiplexIds = field("MultiplexIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchFailedResultModel:
    boto3_raw_data: "type_defs.BatchFailedResultModelTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Code = field("Code")
    Id = field("Id")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchFailedResultModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchFailedResultModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSuccessfulResultModel:
    boto3_raw_data: "type_defs.BatchSuccessfulResultModelTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchSuccessfulResultModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchSuccessfulResultModelTypeDef"]
        ],
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
class BatchScheduleActionDeleteRequest:
    boto3_raw_data: "type_defs.BatchScheduleActionDeleteRequestTypeDef" = (
        dataclasses.field()
    )

    ActionNames = field("ActionNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchScheduleActionDeleteRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchScheduleActionDeleteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStartRequest:
    boto3_raw_data: "type_defs.BatchStartRequestTypeDef" = dataclasses.field()

    ChannelIds = field("ChannelIds")
    MultiplexIds = field("MultiplexIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchStartRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStartRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStopRequest:
    boto3_raw_data: "type_defs.BatchStopRequestTypeDef" = dataclasses.field()

    ChannelIds = field("ChannelIds")
    MultiplexIds = field("MultiplexIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchStopRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStopRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelInputDeviceTransferRequest:
    boto3_raw_data: "type_defs.CancelInputDeviceTransferRequestTypeDef" = (
        dataclasses.field()
    )

    InputDeviceId = field("InputDeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelInputDeviceTransferRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelInputDeviceTransferRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbuTtDDestinationSettings:
    boto3_raw_data: "type_defs.EbuTtDDestinationSettingsTypeDef" = dataclasses.field()

    CopyrightHolder = field("CopyrightHolder")
    FillLineGap = field("FillLineGap")
    FontFamily = field("FontFamily")
    StyleControl = field("StyleControl")
    DefaultFontSize = field("DefaultFontSize")
    DefaultLineHeight = field("DefaultLineHeight")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EbuTtDDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbuTtDDestinationSettingsTypeDef"]
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

    StyleControl = field("StyleControl")

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

    StyleControl = field("StyleControl")

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
class CaptionLanguageMapping:
    boto3_raw_data: "type_defs.CaptionLanguageMappingTypeDef" = dataclasses.field()

    CaptionChannel = field("CaptionChannel")
    LanguageCode = field("LanguageCode")
    LanguageDescription = field("LanguageDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptionLanguageMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionLanguageMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionRectangle:
    boto3_raw_data: "type_defs.CaptionRectangleTypeDef" = dataclasses.field()

    Height = field("Height")
    LeftOffset = field("LeftOffset")
    TopOffset = field("TopOffset")
    Width = field("Width")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaptionRectangleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionRectangleTypeDef"]
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

    OcrLanguage = field("OcrLanguage")
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
    Scte20Detection = field("Scte20Detection")
    Source608ChannelNumber = field("Source608ChannelNumber")
    Source608TrackNumber = field("Source608TrackNumber")

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
class Scte20SourceSettings:
    boto3_raw_data: "type_defs.Scte20SourceSettingsTypeDef" = dataclasses.field()

    Convert608To708 = field("Convert608To708")
    Source608ChannelNumber = field("Source608ChannelNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Scte20SourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte20SourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte27SourceSettings:
    boto3_raw_data: "type_defs.Scte27SourceSettingsTypeDef" = dataclasses.field()

    OcrLanguage = field("OcrLanguage")
    Pid = field("Pid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Scte27SourceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte27SourceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CdiInputSpecification:
    boto3_raw_data: "type_defs.CdiInputSpecificationTypeDef" = dataclasses.field()

    Resolution = field("Resolution")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CdiInputSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CdiInputSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelEgressEndpoint:
    boto3_raw_data: "type_defs.ChannelEgressEndpointTypeDef" = dataclasses.field()

    SourceIp = field("SourceIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelEgressEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelEgressEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelEngineVersionRequest:
    boto3_raw_data: "type_defs.ChannelEngineVersionRequestTypeDef" = dataclasses.field()

    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelEngineVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelEngineVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelEngineVersionResponse:
    boto3_raw_data: "type_defs.ChannelEngineVersionResponseTypeDef" = (
        dataclasses.field()
    )

    ExpirationDate = field("ExpirationDate")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelEngineVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelEngineVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnywhereSettings:
    boto3_raw_data: "type_defs.DescribeAnywhereSettingsTypeDef" = dataclasses.field()

    ChannelPlacementGroupId = field("ChannelPlacementGroupId")
    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAnywhereSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnywhereSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSpecification:
    boto3_raw_data: "type_defs.InputSpecificationTypeDef" = dataclasses.field()

    Codec = field("Codec")
    MaximumBitrate = field("MaximumBitrate")
    Resolution = field("Resolution")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceStatus:
    boto3_raw_data: "type_defs.MaintenanceStatusTypeDef" = dataclasses.field()

    MaintenanceDay = field("MaintenanceDay")
    MaintenanceDeadline = field("MaintenanceDeadline")
    MaintenanceScheduledDate = field("MaintenanceScheduledDate")
    MaintenanceStartTime = field("MaintenanceStartTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MaintenanceStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOutputSettingsDescription:
    boto3_raw_data: "type_defs.VpcOutputSettingsDescriptionTypeDef" = (
        dataclasses.field()
    )

    AvailabilityZones = field("AvailabilityZones")
    NetworkInterfaceIds = field("NetworkInterfaceIds")
    SecurityGroupIds = field("SecurityGroupIds")
    SubnetIds = field("SubnetIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcOutputSettingsDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcOutputSettingsDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClaimDeviceRequest:
    boto3_raw_data: "type_defs.ClaimDeviceRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClaimDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClaimDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchAlarmTemplateGroupSummary:
    boto3_raw_data: "type_defs.CloudWatchAlarmTemplateGroupSummaryTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Id = field("Id")
    Name = field("Name")
    TemplateCount = field("TemplateCount")
    Description = field("Description")
    ModifiedAt = field("ModifiedAt")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudWatchAlarmTemplateGroupSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchAlarmTemplateGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchAlarmTemplateSummary:
    boto3_raw_data: "type_defs.CloudWatchAlarmTemplateSummaryTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ComparisonOperator = field("ComparisonOperator")
    CreatedAt = field("CreatedAt")
    EvaluationPeriods = field("EvaluationPeriods")
    GroupId = field("GroupId")
    Id = field("Id")
    MetricName = field("MetricName")
    Name = field("Name")
    Period = field("Period")
    Statistic = field("Statistic")
    TargetResourceType = field("TargetResourceType")
    Threshold = field("Threshold")
    TreatMissingData = field("TreatMissingData")
    DatapointsToAlarm = field("DatapointsToAlarm")
    Description = field("Description")
    ModifiedAt = field("ModifiedAt")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchAlarmTemplateSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchAlarmTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterfaceMappingCreateRequest:
    boto3_raw_data: "type_defs.InterfaceMappingCreateRequestTypeDef" = (
        dataclasses.field()
    )

    LogicalInterfaceName = field("LogicalInterfaceName")
    NetworkId = field("NetworkId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InterfaceMappingCreateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterfaceMappingCreateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterfaceMapping:
    boto3_raw_data: "type_defs.InterfaceMappingTypeDef" = dataclasses.field()

    LogicalInterfaceName = field("LogicalInterfaceName")
    NetworkId = field("NetworkId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InterfaceMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterfaceMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterfaceMappingUpdateRequest:
    boto3_raw_data: "type_defs.InterfaceMappingUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    LogicalInterfaceName = field("LogicalInterfaceName")
    NetworkId = field("NetworkId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InterfaceMappingUpdateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterfaceMappingUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafIngestCaptionLanguageMapping:
    boto3_raw_data: "type_defs.CmafIngestCaptionLanguageMappingTypeDef" = (
        dataclasses.field()
    )

    CaptionChannel = field("CaptionChannel")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CmafIngestCaptionLanguageMappingTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafIngestCaptionLanguageMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafIngestOutputSettings:
    boto3_raw_data: "type_defs.CmafIngestOutputSettingsTypeDef" = dataclasses.field()

    NameModifier = field("NameModifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CmafIngestOutputSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafIngestOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColorCorrection:
    boto3_raw_data: "type_defs.ColorCorrectionTypeDef" = dataclasses.field()

    InputColorSpace = field("InputColorSpace")
    OutputColorSpace = field("OutputColorSpace")
    Uri = field("Uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColorCorrectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColorCorrectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelPlacementGroupRequest:
    boto3_raw_data: "type_defs.CreateChannelPlacementGroupRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")
    Name = field("Name")
    Nodes = field("Nodes")
    RequestId = field("RequestId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateChannelPlacementGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelPlacementGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceCreateSettings:
    boto3_raw_data: "type_defs.MaintenanceCreateSettingsTypeDef" = dataclasses.field()

    MaintenanceDay = field("MaintenanceDay")
    MaintenanceStartTime = field("MaintenanceStartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaintenanceCreateSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceCreateSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOutputSettings:
    boto3_raw_data: "type_defs.VpcOutputSettingsTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    PublicAddressAllocationIds = field("PublicAddressAllocationIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcOutputSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudWatchAlarmTemplateGroupRequest:
    boto3_raw_data: "type_defs.CreateCloudWatchAlarmTemplateGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")
    Tags = field("Tags")
    RequestId = field("RequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudWatchAlarmTemplateGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudWatchAlarmTemplateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudWatchAlarmTemplateRequest:
    boto3_raw_data: "type_defs.CreateCloudWatchAlarmTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    ComparisonOperator = field("ComparisonOperator")
    EvaluationPeriods = field("EvaluationPeriods")
    GroupIdentifier = field("GroupIdentifier")
    MetricName = field("MetricName")
    Name = field("Name")
    Period = field("Period")
    Statistic = field("Statistic")
    TargetResourceType = field("TargetResourceType")
    Threshold = field("Threshold")
    TreatMissingData = field("TreatMissingData")
    DatapointsToAlarm = field("DatapointsToAlarm")
    Description = field("Description")
    Tags = field("Tags")
    RequestId = field("RequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudWatchAlarmTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudWatchAlarmTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventBridgeRuleTemplateGroupRequest:
    boto3_raw_data: "type_defs.CreateEventBridgeRuleTemplateGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")
    Tags = field("Tags")
    RequestId = field("RequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEventBridgeRuleTemplateGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventBridgeRuleTemplateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBridgeRuleTemplateTarget:
    boto3_raw_data: "type_defs.EventBridgeRuleTemplateTargetTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EventBridgeRuleTemplateTargetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeRuleTemplateTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceSettings:
    boto3_raw_data: "type_defs.InputDeviceSettingsTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDeviceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSourceRequest:
    boto3_raw_data: "type_defs.InputSourceRequestTypeDef" = dataclasses.field()

    PasswordParam = field("PasswordParam")
    Url = field("Url")
    Username = field("Username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputVpcRequest:
    boto3_raw_data: "type_defs.InputVpcRequestTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputVpcRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputVpcRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaConnectFlowRequest:
    boto3_raw_data: "type_defs.MediaConnectFlowRequestTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaConnectFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaConnectFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputWhitelistRuleCidr:
    boto3_raw_data: "type_defs.InputWhitelistRuleCidrTypeDef" = dataclasses.field()

    Cidr = field("Cidr")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputWhitelistRuleCidrTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputWhitelistRuleCidrTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexSettings:
    boto3_raw_data: "type_defs.MultiplexSettingsTypeDef" = dataclasses.field()

    TransportStreamBitrate = field("TransportStreamBitrate")
    TransportStreamId = field("TransportStreamId")
    MaximumVideoBufferDelayMilliseconds = field("MaximumVideoBufferDelayMilliseconds")
    TransportStreamReservedBitrate = field("TransportStreamReservedBitrate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MultiplexSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpPoolCreateRequest:
    boto3_raw_data: "type_defs.IpPoolCreateRequestTypeDef" = dataclasses.field()

    Cidr = field("Cidr")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IpPoolCreateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IpPoolCreateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteCreateRequest:
    boto3_raw_data: "type_defs.RouteCreateRequestTypeDef" = dataclasses.field()

    Cidr = field("Cidr")
    Gateway = field("Gateway")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteCreateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteCreateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpPool:
    boto3_raw_data: "type_defs.IpPoolTypeDef" = dataclasses.field()

    Cidr = field("Cidr")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpPoolTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpPoolTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Route:
    boto3_raw_data: "type_defs.RouteTypeDef" = dataclasses.field()

    Cidr = field("Cidr")
    Gateway = field("Gateway")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeInterfaceMapping:
    boto3_raw_data: "type_defs.NodeInterfaceMappingTypeDef" = dataclasses.field()

    LogicalInterfaceName = field("LogicalInterfaceName")
    NetworkInterfaceMode = field("NetworkInterfaceMode")
    PhysicalInterfaceName = field("PhysicalInterfaceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeInterfaceMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeInterfaceMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeInterfaceMappingCreateRequest:
    boto3_raw_data: "type_defs.NodeInterfaceMappingCreateRequestTypeDef" = (
        dataclasses.field()
    )

    LogicalInterfaceName = field("LogicalInterfaceName")
    NetworkInterfaceMode = field("NetworkInterfaceMode")
    PhysicalInterfaceName = field("PhysicalInterfaceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NodeInterfaceMappingCreateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeInterfaceMappingCreateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SdiSourceMapping:
    boto3_raw_data: "type_defs.SdiSourceMappingTypeDef" = dataclasses.field()

    CardNumber = field("CardNumber")
    ChannelNumber = field("ChannelNumber")
    SdiSource = field("SdiSource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SdiSourceMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SdiSourceMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePartnerInputRequest:
    boto3_raw_data: "type_defs.CreatePartnerInputRequestTypeDef" = dataclasses.field()

    InputId = field("InputId")
    RequestId = field("RequestId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePartnerInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePartnerInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSdiSourceRequest:
    boto3_raw_data: "type_defs.CreateSdiSourceRequestTypeDef" = dataclasses.field()

    Mode = field("Mode")
    Name = field("Name")
    RequestId = field("RequestId")
    Tags = field("Tags")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSdiSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSdiSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SdiSource:
    boto3_raw_data: "type_defs.SdiSourceTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Inputs = field("Inputs")
    Mode = field("Mode")
    Name = field("Name")
    State = field("State")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SdiSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SdiSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSignalMapRequest:
    boto3_raw_data: "type_defs.CreateSignalMapRequestTypeDef" = dataclasses.field()

    DiscoveryEntryPointArn = field("DiscoveryEntryPointArn")
    Name = field("Name")
    CloudWatchAlarmTemplateGroupIdentifiers = field(
        "CloudWatchAlarmTemplateGroupIdentifiers"
    )
    Description = field("Description")
    EventBridgeRuleTemplateGroupIdentifiers = field(
        "EventBridgeRuleTemplateGroupIdentifiers"
    )
    Tags = field("Tags")
    RequestId = field("RequestId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSignalMapRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSignalMapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorDeployment:
    boto3_raw_data: "type_defs.MonitorDeploymentTypeDef" = dataclasses.field()

    Status = field("Status")
    DetailsUri = field("DetailsUri")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitorDeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitorDeploymentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessfulMonitorDeployment:
    boto3_raw_data: "type_defs.SuccessfulMonitorDeploymentTypeDef" = dataclasses.field()

    DetailsUri = field("DetailsUri")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuccessfulMonitorDeploymentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessfulMonitorDeploymentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTagsRequest:
    boto3_raw_data: "type_defs.CreateTagsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelPlacementGroupRequest:
    boto3_raw_data: "type_defs.DeleteChannelPlacementGroupRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelPlacementGroupId = field("ChannelPlacementGroupId")
    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteChannelPlacementGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelPlacementGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelRequest:
    boto3_raw_data: "type_defs.DeleteChannelRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCloudWatchAlarmTemplateGroupRequest:
    boto3_raw_data: "type_defs.DeleteCloudWatchAlarmTemplateGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCloudWatchAlarmTemplateGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCloudWatchAlarmTemplateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCloudWatchAlarmTemplateRequest:
    boto3_raw_data: "type_defs.DeleteCloudWatchAlarmTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCloudWatchAlarmTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCloudWatchAlarmTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterRequest:
    boto3_raw_data: "type_defs.DeleteClusterRequestTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventBridgeRuleTemplateGroupRequest:
    boto3_raw_data: "type_defs.DeleteEventBridgeRuleTemplateGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEventBridgeRuleTemplateGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventBridgeRuleTemplateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventBridgeRuleTemplateRequest:
    boto3_raw_data: "type_defs.DeleteEventBridgeRuleTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEventBridgeRuleTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventBridgeRuleTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInputRequest:
    boto3_raw_data: "type_defs.DeleteInputRequestTypeDef" = dataclasses.field()

    InputId = field("InputId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInputSecurityGroupRequest:
    boto3_raw_data: "type_defs.DeleteInputSecurityGroupRequestTypeDef" = (
        dataclasses.field()
    )

    InputSecurityGroupId = field("InputSecurityGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteInputSecurityGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInputSecurityGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMultiplexProgramRequest:
    boto3_raw_data: "type_defs.DeleteMultiplexProgramRequestTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")
    ProgramName = field("ProgramName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMultiplexProgramRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiplexProgramRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexProgramPacketIdentifiersMapOutput:
    boto3_raw_data: "type_defs.MultiplexProgramPacketIdentifiersMapOutputTypeDef" = (
        dataclasses.field()
    )

    AudioPids = field("AudioPids")
    DvbSubPids = field("DvbSubPids")
    DvbTeletextPid = field("DvbTeletextPid")
    EtvPlatformPid = field("EtvPlatformPid")
    EtvSignalPid = field("EtvSignalPid")
    KlvDataPids = field("KlvDataPids")
    PcrPid = field("PcrPid")
    PmtPid = field("PmtPid")
    PrivateMetadataPid = field("PrivateMetadataPid")
    Scte27Pids = field("Scte27Pids")
    Scte35Pid = field("Scte35Pid")
    TimedMetadataPid = field("TimedMetadataPid")
    VideoPid = field("VideoPid")
    AribCaptionsPid = field("AribCaptionsPid")
    DvbTeletextPids = field("DvbTeletextPids")
    EcmPid = field("EcmPid")
    Smpte2038Pid = field("Smpte2038Pid")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultiplexProgramPacketIdentifiersMapOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexProgramPacketIdentifiersMapOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexProgramPipelineDetail:
    boto3_raw_data: "type_defs.MultiplexProgramPipelineDetailTypeDef" = (
        dataclasses.field()
    )

    ActiveChannelPipeline = field("ActiveChannelPipeline")
    PipelineId = field("PipelineId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MultiplexProgramPipelineDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexProgramPipelineDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMultiplexRequest:
    boto3_raw_data: "type_defs.DeleteMultiplexRequestTypeDef" = dataclasses.field()

    MultiplexId = field("MultiplexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMultiplexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiplexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNetworkRequest:
    boto3_raw_data: "type_defs.DeleteNetworkRequestTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNodeRequest:
    boto3_raw_data: "type_defs.DeleteNodeRequestTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    NodeId = field("NodeId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteNodeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReservationRequest:
    boto3_raw_data: "type_defs.DeleteReservationRequestTypeDef" = dataclasses.field()

    ReservationId = field("ReservationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReservationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReservationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenewalSettings:
    boto3_raw_data: "type_defs.RenewalSettingsTypeDef" = dataclasses.field()

    AutomaticRenewal = field("AutomaticRenewal")
    RenewalCount = field("RenewalCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RenewalSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RenewalSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationResourceSpecification:
    boto3_raw_data: "type_defs.ReservationResourceSpecificationTypeDef" = (
        dataclasses.field()
    )

    ChannelClass = field("ChannelClass")
    Codec = field("Codec")
    MaximumBitrate = field("MaximumBitrate")
    MaximumFramerate = field("MaximumFramerate")
    Resolution = field("Resolution")
    ResourceType = field("ResourceType")
    SpecialFeature = field("SpecialFeature")
    VideoQuality = field("VideoQuality")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReservationResourceSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationResourceSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduleRequest:
    boto3_raw_data: "type_defs.DeleteScheduleRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSdiSourceRequest:
    boto3_raw_data: "type_defs.DeleteSdiSourceRequestTypeDef" = dataclasses.field()

    SdiSourceId = field("SdiSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSdiSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSdiSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSignalMapRequest:
    boto3_raw_data: "type_defs.DeleteSignalMapRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSignalMapRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSignalMapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagsRequest:
    boto3_raw_data: "type_defs.DeleteTagsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelPlacementGroupRequest:
    boto3_raw_data: "type_defs.DescribeChannelPlacementGroupRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelPlacementGroupId = field("ChannelPlacementGroupId")
    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelPlacementGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelPlacementGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelPlacementGroupSummary:
    boto3_raw_data: "type_defs.DescribeChannelPlacementGroupSummaryTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Channels = field("Channels")
    ClusterId = field("ClusterId")
    Id = field("Id")
    Name = field("Name")
    Nodes = field("Nodes")
    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelPlacementGroupSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelPlacementGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelRequest:
    boto3_raw_data: "type_defs.DescribeChannelRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterRequest:
    boto3_raw_data: "type_defs.DescribeClusterRequestTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputDeviceRequest:
    boto3_raw_data: "type_defs.DescribeInputDeviceRequestTypeDef" = dataclasses.field()

    InputDeviceId = field("InputDeviceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInputDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceHdSettings:
    boto3_raw_data: "type_defs.InputDeviceHdSettingsTypeDef" = dataclasses.field()

    ActiveInput = field("ActiveInput")
    ConfiguredInput = field("ConfiguredInput")
    DeviceState = field("DeviceState")
    Framerate = field("Framerate")
    Height = field("Height")
    MaxBitrate = field("MaxBitrate")
    ScanType = field("ScanType")
    Width = field("Width")
    LatencyMs = field("LatencyMs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDeviceHdSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceHdSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceNetworkSettings:
    boto3_raw_data: "type_defs.InputDeviceNetworkSettingsTypeDef" = dataclasses.field()

    DnsAddresses = field("DnsAddresses")
    Gateway = field("Gateway")
    IpAddress = field("IpAddress")
    IpScheme = field("IpScheme")
    SubnetMask = field("SubnetMask")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDeviceNetworkSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceNetworkSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputDeviceThumbnailRequest:
    boto3_raw_data: "type_defs.DescribeInputDeviceThumbnailRequestTypeDef" = (
        dataclasses.field()
    )

    InputDeviceId = field("InputDeviceId")
    Accept = field("Accept")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInputDeviceThumbnailRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputDeviceThumbnailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputRequest:
    boto3_raw_data: "type_defs.DescribeInputRequestTypeDef" = dataclasses.field()

    InputId = field("InputId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSource:
    boto3_raw_data: "type_defs.InputSourceTypeDef" = dataclasses.field()

    PasswordParam = field("PasswordParam")
    Url = field("Url")
    Username = field("Username")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaConnectFlow:
    boto3_raw_data: "type_defs.MediaConnectFlowTypeDef" = dataclasses.field()

    FlowArn = field("FlowArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaConnectFlowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaConnectFlowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputSecurityGroupRequest:
    boto3_raw_data: "type_defs.DescribeInputSecurityGroupRequestTypeDef" = (
        dataclasses.field()
    )

    InputSecurityGroupId = field("InputSecurityGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInputSecurityGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputSecurityGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputWhitelistRule:
    boto3_raw_data: "type_defs.InputWhitelistRuleTypeDef" = dataclasses.field()

    Cidr = field("Cidr")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputWhitelistRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputWhitelistRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiplexProgramRequest:
    boto3_raw_data: "type_defs.DescribeMultiplexProgramRequestTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")
    ProgramName = field("ProgramName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMultiplexProgramRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiplexProgramRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiplexRequest:
    boto3_raw_data: "type_defs.DescribeMultiplexRequestTypeDef" = dataclasses.field()

    MultiplexId = field("MultiplexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMultiplexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiplexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNetworkRequest:
    boto3_raw_data: "type_defs.DescribeNetworkRequestTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodeRequest:
    boto3_raw_data: "type_defs.DescribeNodeRequestTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    NodeId = field("NodeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNodeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOfferingRequest:
    boto3_raw_data: "type_defs.DescribeOfferingRequestTypeDef" = dataclasses.field()

    OfferingId = field("OfferingId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOfferingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOfferingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservationRequest:
    boto3_raw_data: "type_defs.DescribeReservationRequestTypeDef" = dataclasses.field()

    ReservationId = field("ReservationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReservationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservationRequestTypeDef"]
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
class DescribeScheduleRequest:
    boto3_raw_data: "type_defs.DescribeScheduleRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSdiSourceRequest:
    boto3_raw_data: "type_defs.DescribeSdiSourceRequestTypeDef" = dataclasses.field()

    SdiSourceId = field("SdiSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSdiSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSdiSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThumbnailsRequest:
    boto3_raw_data: "type_defs.DescribeThumbnailsRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")
    PipelineId = field("PipelineId")
    ThumbnailType = field("ThumbnailType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThumbnailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThumbnailsRequestTypeDef"]
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
    RepInterval = field("RepInterval")

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
    RepInterval = field("RepInterval")
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

    RepInterval = field("RepInterval")

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
class FeatureActivations:
    boto3_raw_data: "type_defs.FeatureActivationsTypeDef" = dataclasses.field()

    InputPrepareScheduleActions = field("InputPrepareScheduleActions")
    OutputStaticImageOverlayScheduleActions = field(
        "OutputStaticImageOverlayScheduleActions"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeatureActivationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeatureActivationsTypeDef"]
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

    DistributorId = field("DistributorId")
    NielsenPcmToId3Tagging = field("NielsenPcmToId3Tagging")

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
class ThumbnailConfiguration:
    boto3_raw_data: "type_defs.ThumbnailConfigurationTypeDef" = dataclasses.field()

    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThumbnailConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThumbnailConfigurationTypeDef"]
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

    Source = field("Source")
    SyncThreshold = field("SyncThreshold")

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
class EpochLockingSettings:
    boto3_raw_data: "type_defs.EpochLockingSettingsTypeDef" = dataclasses.field()

    CustomEpoch = field("CustomEpoch")
    JamSyncTime = field("JamSyncTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EpochLockingSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EpochLockingSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBridgeRuleTemplateGroupSummary:
    boto3_raw_data: "type_defs.EventBridgeRuleTemplateGroupSummaryTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Id = field("Id")
    Name = field("Name")
    TemplateCount = field("TemplateCount")
    Description = field("Description")
    ModifiedAt = field("ModifiedAt")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EventBridgeRuleTemplateGroupSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeRuleTemplateGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBridgeRuleTemplateSummary:
    boto3_raw_data: "type_defs.EventBridgeRuleTemplateSummaryTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    EventTargetCount = field("EventTargetCount")
    EventType = field("EventType")
    GroupId = field("GroupId")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    ModifiedAt = field("ModifiedAt")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EventBridgeRuleTemplateSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeRuleTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputLossFailoverSettings:
    boto3_raw_data: "type_defs.InputLossFailoverSettingsTypeDef" = dataclasses.field()

    InputLossThresholdMsec = field("InputLossThresholdMsec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputLossFailoverSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputLossFailoverSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoBlackFailoverSettings:
    boto3_raw_data: "type_defs.VideoBlackFailoverSettingsTypeDef" = dataclasses.field()

    BlackDetectThreshold = field("BlackDetectThreshold")
    VideoBlackThresholdMsec = field("VideoBlackThresholdMsec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoBlackFailoverSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoBlackFailoverSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FecOutputSettings:
    boto3_raw_data: "type_defs.FecOutputSettingsTypeDef" = dataclasses.field()

    ColumnDepth = field("ColumnDepth")
    IncludeFec = field("IncludeFec")
    RowLength = field("RowLength")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FecOutputSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FecOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FixedModeScheduleActionStartSettings:
    boto3_raw_data: "type_defs.FixedModeScheduleActionStartSettingsTypeDef" = (
        dataclasses.field()
    )

    Time = field("Time")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FixedModeScheduleActionStartSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FixedModeScheduleActionStartSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Fmp4HlsSettings:
    boto3_raw_data: "type_defs.Fmp4HlsSettingsTypeDef" = dataclasses.field()

    AudioRenditionSets = field("AudioRenditionSets")
    NielsenId3Behavior = field("NielsenId3Behavior")
    TimedMetadataBehavior = field("TimedMetadataBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Fmp4HlsSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Fmp4HlsSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FollowModeScheduleActionStartSettings:
    boto3_raw_data: "type_defs.FollowModeScheduleActionStartSettingsTypeDef" = (
        dataclasses.field()
    )

    FollowPoint = field("FollowPoint")
    ReferenceActionName = field("ReferenceActionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FollowModeScheduleActionStartSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FollowModeScheduleActionStartSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameCaptureS3Settings:
    boto3_raw_data: "type_defs.FrameCaptureS3SettingsTypeDef" = dataclasses.field()

    CannedAcl = field("CannedAcl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrameCaptureS3SettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameCaptureS3SettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameCaptureOutputSettings:
    boto3_raw_data: "type_defs.FrameCaptureOutputSettingsTypeDef" = dataclasses.field()

    NameModifier = field("NameModifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrameCaptureOutputSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameCaptureOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudWatchAlarmTemplateGroupRequest:
    boto3_raw_data: "type_defs.GetCloudWatchAlarmTemplateGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudWatchAlarmTemplateGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudWatchAlarmTemplateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudWatchAlarmTemplateRequest:
    boto3_raw_data: "type_defs.GetCloudWatchAlarmTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudWatchAlarmTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudWatchAlarmTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventBridgeRuleTemplateGroupRequest:
    boto3_raw_data: "type_defs.GetEventBridgeRuleTemplateGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEventBridgeRuleTemplateGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventBridgeRuleTemplateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventBridgeRuleTemplateRequest:
    boto3_raw_data: "type_defs.GetEventBridgeRuleTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEventBridgeRuleTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventBridgeRuleTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalMapRequest:
    boto3_raw_data: "type_defs.GetSignalMapRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSignalMapRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalMapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H264ColorSpaceSettingsOutput:
    boto3_raw_data: "type_defs.H264ColorSpaceSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    ColorSpacePassthroughSettings = field("ColorSpacePassthroughSettings")
    Rec601Settings = field("Rec601Settings")
    Rec709Settings = field("Rec709Settings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.H264ColorSpaceSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H264ColorSpaceSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H264ColorSpaceSettings:
    boto3_raw_data: "type_defs.H264ColorSpaceSettingsTypeDef" = dataclasses.field()

    ColorSpacePassthroughSettings = field("ColorSpacePassthroughSettings")
    Rec601Settings = field("Rec601Settings")
    Rec709Settings = field("Rec709Settings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.H264ColorSpaceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H264ColorSpaceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemporalFilterSettings:
    boto3_raw_data: "type_defs.TemporalFilterSettingsTypeDef" = dataclasses.field()

    PostFilterSharpening = field("PostFilterSharpening")
    Strength = field("Strength")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemporalFilterSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemporalFilterSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsAkamaiSettings:
    boto3_raw_data: "type_defs.HlsAkamaiSettingsTypeDef" = dataclasses.field()

    ConnectionRetryInterval = field("ConnectionRetryInterval")
    FilecacheDuration = field("FilecacheDuration")
    HttpTransferMode = field("HttpTransferMode")
    NumRetries = field("NumRetries")
    RestartDelay = field("RestartDelay")
    Salt = field("Salt")
    Token = field("Token")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsAkamaiSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsAkamaiSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsBasicPutSettings:
    boto3_raw_data: "type_defs.HlsBasicPutSettingsTypeDef" = dataclasses.field()

    ConnectionRetryInterval = field("ConnectionRetryInterval")
    FilecacheDuration = field("FilecacheDuration")
    NumRetries = field("NumRetries")
    RestartDelay = field("RestartDelay")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsBasicPutSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsBasicPutSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsMediaStoreSettings:
    boto3_raw_data: "type_defs.HlsMediaStoreSettingsTypeDef" = dataclasses.field()

    ConnectionRetryInterval = field("ConnectionRetryInterval")
    FilecacheDuration = field("FilecacheDuration")
    MediaStoreStorageClass = field("MediaStoreStorageClass")
    NumRetries = field("NumRetries")
    RestartDelay = field("RestartDelay")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsMediaStoreSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsMediaStoreSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsS3Settings:
    boto3_raw_data: "type_defs.HlsS3SettingsTypeDef" = dataclasses.field()

    CannedAcl = field("CannedAcl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsS3SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HlsS3SettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsWebdavSettings:
    boto3_raw_data: "type_defs.HlsWebdavSettingsTypeDef" = dataclasses.field()

    ConnectionRetryInterval = field("ConnectionRetryInterval")
    FilecacheDuration = field("FilecacheDuration")
    HttpTransferMode = field("HttpTransferMode")
    NumRetries = field("NumRetries")
    RestartDelay = field("RestartDelay")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsWebdavSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsWebdavSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsId3SegmentTaggingScheduleActionSettings:
    boto3_raw_data: "type_defs.HlsId3SegmentTaggingScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    Tag = field("Tag")
    Id3 = field("Id3")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HlsId3SegmentTaggingScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsId3SegmentTaggingScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsInputSettings:
    boto3_raw_data: "type_defs.HlsInputSettingsTypeDef" = dataclasses.field()

    Bandwidth = field("Bandwidth")
    BufferSegments = field("BufferSegments")
    Retries = field("Retries")
    RetryInterval = field("RetryInterval")
    Scte35Source = field("Scte35Source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsInputSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsInputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsTimedMetadataScheduleActionSettings:
    boto3_raw_data: "type_defs.HlsTimedMetadataScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    Id3 = field("Id3")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HlsTimedMetadataScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsTimedMetadataScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Id3SegmentTaggingScheduleActionSettings:
    boto3_raw_data: "type_defs.Id3SegmentTaggingScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    Id3 = field("Id3")
    Tag = field("Tag")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Id3SegmentTaggingScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Id3SegmentTaggingScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTimecode:
    boto3_raw_data: "type_defs.StartTimecodeTypeDef" = dataclasses.field()

    Timecode = field("Timecode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartTimecodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartTimecodeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopTimecode:
    boto3_raw_data: "type_defs.StopTimecodeTypeDef" = dataclasses.field()

    LastFrameClippingBehavior = field("LastFrameClippingBehavior")
    Timecode = field("Timecode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopTimecodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopTimecodeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputRequestDestinationRoute:
    boto3_raw_data: "type_defs.InputRequestDestinationRouteTypeDef" = (
        dataclasses.field()
    )

    Cidr = field("Cidr")
    Gateway = field("Gateway")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputRequestDestinationRouteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputRequestDestinationRouteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDestinationRoute:
    boto3_raw_data: "type_defs.InputDestinationRouteTypeDef" = dataclasses.field()

    Cidr = field("Cidr")
    Gateway = field("Gateway")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDestinationRouteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDestinationRouteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDestinationVpc:
    boto3_raw_data: "type_defs.InputDestinationVpcTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")
    NetworkInterfaceId = field("NetworkInterfaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDestinationVpcTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDestinationVpcTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceConfigurableAudioChannelPairConfig:
    boto3_raw_data: "type_defs.InputDeviceConfigurableAudioChannelPairConfigTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Profile = field("Profile")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputDeviceConfigurableAudioChannelPairConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceConfigurableAudioChannelPairConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceMediaConnectConfigurableSettings:
    boto3_raw_data: "type_defs.InputDeviceMediaConnectConfigurableSettingsTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")
    RoleArn = field("RoleArn")
    SecretArn = field("SecretArn")
    SourceName = field("SourceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputDeviceMediaConnectConfigurableSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceMediaConnectConfigurableSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceMediaConnectSettings:
    boto3_raw_data: "type_defs.InputDeviceMediaConnectSettingsTypeDef" = (
        dataclasses.field()
    )

    FlowArn = field("FlowArn")
    RoleArn = field("RoleArn")
    SecretArn = field("SecretArn")
    SourceName = field("SourceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InputDeviceMediaConnectSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceMediaConnectSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceRequest:
    boto3_raw_data: "type_defs.InputDeviceRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceUhdAudioChannelPairConfig:
    boto3_raw_data: "type_defs.InputDeviceUhdAudioChannelPairConfigTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Profile = field("Profile")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputDeviceUhdAudioChannelPairConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceUhdAudioChannelPairConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSdpLocation:
    boto3_raw_data: "type_defs.InputSdpLocationTypeDef" = dataclasses.field()

    MediaIndex = field("MediaIndex")
    SdpUrl = field("SdpUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputSdpLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSdpLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpPoolUpdateRequest:
    boto3_raw_data: "type_defs.IpPoolUpdateRequestTypeDef" = dataclasses.field()

    Cidr = field("Cidr")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IpPoolUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IpPoolUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelPlacementGroupsRequest:
    boto3_raw_data: "type_defs.ListChannelPlacementGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelPlacementGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelPlacementGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequest:
    boto3_raw_data: "type_defs.ListChannelsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudWatchAlarmTemplateGroupsRequest:
    boto3_raw_data: "type_defs.ListCloudWatchAlarmTemplateGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Scope = field("Scope")
    SignalMapIdentifier = field("SignalMapIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudWatchAlarmTemplateGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudWatchAlarmTemplateGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudWatchAlarmTemplatesRequest:
    boto3_raw_data: "type_defs.ListCloudWatchAlarmTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    GroupIdentifier = field("GroupIdentifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Scope = field("Scope")
    SignalMapIdentifier = field("SignalMapIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudWatchAlarmTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudWatchAlarmTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersRequest:
    boto3_raw_data: "type_defs.ListClustersRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventBridgeRuleTemplateGroupsRequest:
    boto3_raw_data: "type_defs.ListEventBridgeRuleTemplateGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SignalMapIdentifier = field("SignalMapIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEventBridgeRuleTemplateGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventBridgeRuleTemplateGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventBridgeRuleTemplatesRequest:
    boto3_raw_data: "type_defs.ListEventBridgeRuleTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    GroupIdentifier = field("GroupIdentifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SignalMapIdentifier = field("SignalMapIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEventBridgeRuleTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventBridgeRuleTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputDeviceTransfersRequest:
    boto3_raw_data: "type_defs.ListInputDeviceTransfersRequestTypeDef" = (
        dataclasses.field()
    )

    TransferType = field("TransferType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInputDeviceTransfersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputDeviceTransfersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferringInputDeviceSummary:
    boto3_raw_data: "type_defs.TransferringInputDeviceSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Message = field("Message")
    TargetCustomerId = field("TargetCustomerId")
    TransferType = field("TransferType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TransferringInputDeviceSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferringInputDeviceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputDevicesRequest:
    boto3_raw_data: "type_defs.ListInputDevicesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInputDevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputDevicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputSecurityGroupsRequest:
    boto3_raw_data: "type_defs.ListInputSecurityGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInputSecurityGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputSecurityGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputsRequest:
    boto3_raw_data: "type_defs.ListInputsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListInputsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiplexProgramsRequest:
    boto3_raw_data: "type_defs.ListMultiplexProgramsRequestTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMultiplexProgramsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiplexProgramsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexProgramSummary:
    boto3_raw_data: "type_defs.MultiplexProgramSummaryTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")
    ProgramName = field("ProgramName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiplexProgramSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexProgramSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiplexesRequest:
    boto3_raw_data: "type_defs.ListMultiplexesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMultiplexesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiplexesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNetworksRequest:
    boto3_raw_data: "type_defs.ListNetworksRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNetworksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNetworksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesRequest:
    boto3_raw_data: "type_defs.ListNodesRequestTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListNodesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOfferingsRequest:
    boto3_raw_data: "type_defs.ListOfferingsRequestTypeDef" = dataclasses.field()

    ChannelClass = field("ChannelClass")
    ChannelConfiguration = field("ChannelConfiguration")
    Codec = field("Codec")
    Duration = field("Duration")
    MaxResults = field("MaxResults")
    MaximumBitrate = field("MaximumBitrate")
    MaximumFramerate = field("MaximumFramerate")
    NextToken = field("NextToken")
    Resolution = field("Resolution")
    ResourceType = field("ResourceType")
    SpecialFeature = field("SpecialFeature")
    VideoQuality = field("VideoQuality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOfferingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOfferingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationsRequest:
    boto3_raw_data: "type_defs.ListReservationsRequestTypeDef" = dataclasses.field()

    ChannelClass = field("ChannelClass")
    Codec = field("Codec")
    MaxResults = field("MaxResults")
    MaximumBitrate = field("MaximumBitrate")
    MaximumFramerate = field("MaximumFramerate")
    NextToken = field("NextToken")
    Resolution = field("Resolution")
    ResourceType = field("ResourceType")
    SpecialFeature = field("SpecialFeature")
    VideoQuality = field("VideoQuality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReservationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSdiSourcesRequest:
    boto3_raw_data: "type_defs.ListSdiSourcesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSdiSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSdiSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SdiSourceSummary:
    boto3_raw_data: "type_defs.SdiSourceSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Inputs = field("Inputs")
    Mode = field("Mode")
    Name = field("Name")
    State = field("State")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SdiSourceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SdiSourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalMapsRequest:
    boto3_raw_data: "type_defs.ListSignalMapsRequestTypeDef" = dataclasses.field()

    CloudWatchAlarmTemplateGroupIdentifier = field(
        "CloudWatchAlarmTemplateGroupIdentifier"
    )
    EventBridgeRuleTemplateGroupIdentifier = field(
        "EventBridgeRuleTemplateGroupIdentifier"
    )
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSignalMapsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalMapsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalMapSummary:
    boto3_raw_data: "type_defs.SignalMapSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Id = field("Id")
    MonitorDeploymentStatus = field("MonitorDeploymentStatus")
    Name = field("Name")
    Status = field("Status")
    Description = field("Description")
    ModifiedAt = field("ModifiedAt")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignalMapSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalMapSummaryTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class M3u8Settings:
    boto3_raw_data: "type_defs.M3u8SettingsTypeDef" = dataclasses.field()

    AudioFramesPerPes = field("AudioFramesPerPes")
    AudioPids = field("AudioPids")
    EcmPid = field("EcmPid")
    NielsenId3Behavior = field("NielsenId3Behavior")
    PatInterval = field("PatInterval")
    PcrControl = field("PcrControl")
    PcrPeriod = field("PcrPeriod")
    PcrPid = field("PcrPid")
    PmtInterval = field("PmtInterval")
    PmtPid = field("PmtPid")
    ProgramNum = field("ProgramNum")
    Scte35Behavior = field("Scte35Behavior")
    Scte35Pid = field("Scte35Pid")
    TimedMetadataBehavior = field("TimedMetadataBehavior")
    TimedMetadataPid = field("TimedMetadataPid")
    TransportStreamId = field("TransportStreamId")
    VideoPid = field("VideoPid")
    KlvBehavior = field("KlvBehavior")
    KlvDataPids = field("KlvDataPids")

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
class MaintenanceUpdateSettings:
    boto3_raw_data: "type_defs.MaintenanceUpdateSettingsTypeDef" = dataclasses.field()

    MaintenanceDay = field("MaintenanceDay")
    MaintenanceScheduledDate = field("MaintenanceScheduledDate")
    MaintenanceStartTime = field("MaintenanceStartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaintenanceUpdateSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceUpdateSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPackageOutputDestinationSettings:
    boto3_raw_data: "type_defs.MediaPackageOutputDestinationSettingsTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")
    ChannelGroup = field("ChannelGroup")
    ChannelName = field("ChannelName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaPackageOutputDestinationSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaPackageOutputDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPackageV2DestinationSettings:
    boto3_raw_data: "type_defs.MediaPackageV2DestinationSettingsTypeDef" = (
        dataclasses.field()
    )

    AudioGroupId = field("AudioGroupId")
    AudioRenditionSets = field("AudioRenditionSets")
    HlsAutoSelect = field("HlsAutoSelect")
    HlsDefault = field("HlsDefault")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaPackageV2DestinationSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaPackageV2DestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaResourceNeighbor:
    boto3_raw_data: "type_defs.MediaResourceNeighborTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaResourceNeighborTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaResourceNeighborTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MotionGraphicsActivateScheduleActionSettings:
    boto3_raw_data: "type_defs.MotionGraphicsActivateScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    Duration = field("Duration")
    PasswordParam = field("PasswordParam")
    Url = field("Url")
    Username = field("Username")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MotionGraphicsActivateScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MotionGraphicsActivateScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MotionGraphicsSettingsOutput:
    boto3_raw_data: "type_defs.MotionGraphicsSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    HtmlMotionGraphicsSettings = field("HtmlMotionGraphicsSettings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MotionGraphicsSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MotionGraphicsSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MotionGraphicsSettings:
    boto3_raw_data: "type_defs.MotionGraphicsSettingsTypeDef" = dataclasses.field()

    HtmlMotionGraphicsSettings = field("HtmlMotionGraphicsSettings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MotionGraphicsSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MotionGraphicsSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MsSmoothOutputSettings:
    boto3_raw_data: "type_defs.MsSmoothOutputSettingsTypeDef" = dataclasses.field()

    H265PackagingType = field("H265PackagingType")
    NameModifier = field("NameModifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MsSmoothOutputSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MsSmoothOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastInputSettings:
    boto3_raw_data: "type_defs.MulticastInputSettingsTypeDef" = dataclasses.field()

    SourceIpAddress = field("SourceIpAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MulticastInputSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MulticastInputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastSourceCreateRequest:
    boto3_raw_data: "type_defs.MulticastSourceCreateRequestTypeDef" = (
        dataclasses.field()
    )

    Url = field("Url")
    SourceIp = field("SourceIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MulticastSourceCreateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MulticastSourceCreateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastSource:
    boto3_raw_data: "type_defs.MulticastSourceTypeDef" = dataclasses.field()

    Url = field("Url")
    SourceIp = field("SourceIp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MulticastSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MulticastSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastSourceUpdateRequest:
    boto3_raw_data: "type_defs.MulticastSourceUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    Url = field("Url")
    SourceIp = field("SourceIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MulticastSourceUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MulticastSourceUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexM2tsSettings:
    boto3_raw_data: "type_defs.MultiplexM2tsSettingsTypeDef" = dataclasses.field()

    AbsentInputAudioBehavior = field("AbsentInputAudioBehavior")
    Arib = field("Arib")
    AudioBufferModel = field("AudioBufferModel")
    AudioFramesPerPes = field("AudioFramesPerPes")
    AudioStreamType = field("AudioStreamType")
    CcDescriptor = field("CcDescriptor")
    Ebif = field("Ebif")
    EsRateInPes = field("EsRateInPes")
    Klv = field("Klv")
    NielsenId3Behavior = field("NielsenId3Behavior")
    PcrControl = field("PcrControl")
    PcrPeriod = field("PcrPeriod")
    Scte35Control = field("Scte35Control")
    Scte35PrerollPullupMilliseconds = field("Scte35PrerollPullupMilliseconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiplexM2tsSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexM2tsSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexMediaConnectOutputDestinationSettings:
    boto3_raw_data: (
        "type_defs.MultiplexMediaConnectOutputDestinationSettingsTypeDef"
    ) = dataclasses.field()

    EntitlementArn = field("EntitlementArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultiplexMediaConnectOutputDestinationSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.MultiplexMediaConnectOutputDestinationSettingsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexProgramChannelDestinationSettings:
    boto3_raw_data: "type_defs.MultiplexProgramChannelDestinationSettingsTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")
    ProgramName = field("ProgramName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultiplexProgramChannelDestinationSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexProgramChannelDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexProgramPacketIdentifiersMap:
    boto3_raw_data: "type_defs.MultiplexProgramPacketIdentifiersMapTypeDef" = (
        dataclasses.field()
    )

    AudioPids = field("AudioPids")
    DvbSubPids = field("DvbSubPids")
    DvbTeletextPid = field("DvbTeletextPid")
    EtvPlatformPid = field("EtvPlatformPid")
    EtvSignalPid = field("EtvSignalPid")
    KlvDataPids = field("KlvDataPids")
    PcrPid = field("PcrPid")
    PmtPid = field("PmtPid")
    PrivateMetadataPid = field("PrivateMetadataPid")
    Scte27Pids = field("Scte27Pids")
    Scte35Pid = field("Scte35Pid")
    TimedMetadataPid = field("TimedMetadataPid")
    VideoPid = field("VideoPid")
    AribCaptionsPid = field("AribCaptionsPid")
    DvbTeletextPids = field("DvbTeletextPids")
    EcmPid = field("EcmPid")
    Smpte2038Pid = field("Smpte2038Pid")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultiplexProgramPacketIdentifiersMapTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexProgramPacketIdentifiersMapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexProgramServiceDescriptor:
    boto3_raw_data: "type_defs.MultiplexProgramServiceDescriptorTypeDef" = (
        dataclasses.field()
    )

    ProviderName = field("ProviderName")
    ServiceName = field("ServiceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultiplexProgramServiceDescriptorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexProgramServiceDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexSettingsSummary:
    boto3_raw_data: "type_defs.MultiplexSettingsSummaryTypeDef" = dataclasses.field()

    TransportStreamBitrate = field("TransportStreamBitrate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiplexSettingsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexSettingsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexStatmuxVideoSettings:
    boto3_raw_data: "type_defs.MultiplexStatmuxVideoSettingsTypeDef" = (
        dataclasses.field()
    )

    MaximumBitrate = field("MaximumBitrate")
    MinimumBitrate = field("MinimumBitrate")
    Priority = field("Priority")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MultiplexStatmuxVideoSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexStatmuxVideoSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NielsenCBET:
    boto3_raw_data: "type_defs.NielsenCBETTypeDef" = dataclasses.field()

    CbetCheckDigitString = field("CbetCheckDigitString")
    CbetStepaside = field("CbetStepaside")
    Csid = field("Csid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NielsenCBETTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NielsenCBETTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NielsenNaesIiNw:
    boto3_raw_data: "type_defs.NielsenNaesIiNwTypeDef" = dataclasses.field()

    CheckDigitString = field("CheckDigitString")
    Sid = field("Sid")
    Timezone = field("Timezone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NielsenNaesIiNwTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NielsenNaesIiNwTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDestinationSettings:
    boto3_raw_data: "type_defs.OutputDestinationSettingsTypeDef" = dataclasses.field()

    PasswordParam = field("PasswordParam")
    StreamName = field("StreamName")
    Url = field("Url")
    Username = field("Username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtOutputDestinationSettings:
    boto3_raw_data: "type_defs.SrtOutputDestinationSettingsTypeDef" = (
        dataclasses.field()
    )

    EncryptionPassphraseSecretArn = field("EncryptionPassphraseSecretArn")
    StreamId = field("StreamId")
    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SrtOutputDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SrtOutputDestinationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RtmpGroupSettingsOutput:
    boto3_raw_data: "type_defs.RtmpGroupSettingsOutputTypeDef" = dataclasses.field()

    AdMarkers = field("AdMarkers")
    AuthenticationScheme = field("AuthenticationScheme")
    CacheFullBehavior = field("CacheFullBehavior")
    CacheLength = field("CacheLength")
    CaptionData = field("CaptionData")
    InputLossAction = field("InputLossAction")
    RestartDelay = field("RestartDelay")
    IncludeFillerNalUnits = field("IncludeFillerNalUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RtmpGroupSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RtmpGroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtGroupSettings:
    boto3_raw_data: "type_defs.SrtGroupSettingsTypeDef" = dataclasses.field()

    InputLossAction = field("InputLossAction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SrtGroupSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SrtGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UdpGroupSettings:
    boto3_raw_data: "type_defs.UdpGroupSettingsTypeDef" = dataclasses.field()

    InputLossAction = field("InputLossAction")
    TimedMetadataId3Frame = field("TimedMetadataId3Frame")
    TimedMetadataId3Period = field("TimedMetadataId3Period")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UdpGroupSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UdpGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RtmpGroupSettings:
    boto3_raw_data: "type_defs.RtmpGroupSettingsTypeDef" = dataclasses.field()

    AdMarkers = field("AdMarkers")
    AuthenticationScheme = field("AuthenticationScheme")
    CacheFullBehavior = field("CacheFullBehavior")
    CacheLength = field("CacheLength")
    CaptionData = field("CaptionData")
    InputLossAction = field("InputLossAction")
    RestartDelay = field("RestartDelay")
    IncludeFillerNalUnits = field("IncludeFillerNalUnits")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RtmpGroupSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RtmpGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelinePauseStateSettings:
    boto3_raw_data: "type_defs.PipelinePauseStateSettingsTypeDef" = dataclasses.field()

    PipelineId = field("PipelineId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelinePauseStateSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelinePauseStateSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootInputDeviceRequest:
    boto3_raw_data: "type_defs.RebootInputDeviceRequestTypeDef" = dataclasses.field()

    InputDeviceId = field("InputDeviceId")
    Force = field("Force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootInputDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootInputDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectInputDeviceTransferRequest:
    boto3_raw_data: "type_defs.RejectInputDeviceTransferRequestTypeDef" = (
        dataclasses.field()
    )

    InputDeviceId = field("InputDeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RejectInputDeviceTransferRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectInputDeviceTransferRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestartChannelPipelinesRequest:
    boto3_raw_data: "type_defs.RestartChannelPipelinesRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")
    PipelineIds = field("PipelineIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestartChannelPipelinesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestartChannelPipelinesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteUpdateRequest:
    boto3_raw_data: "type_defs.RouteUpdateRequestTypeDef" = dataclasses.field()

    Cidr = field("Cidr")
    Gateway = field("Gateway")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RouteUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35InputScheduleActionSettings:
    boto3_raw_data: "type_defs.Scte35InputScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    InputAttachmentNameReference = field("InputAttachmentNameReference")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Scte35InputScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35InputScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35ReturnToNetworkScheduleActionSettings:
    boto3_raw_data: "type_defs.Scte35ReturnToNetworkScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    SpliceEventId = field("SpliceEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Scte35ReturnToNetworkScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35ReturnToNetworkScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35SpliceInsertScheduleActionSettings:
    boto3_raw_data: "type_defs.Scte35SpliceInsertScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    SpliceEventId = field("SpliceEventId")
    Duration = field("Duration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Scte35SpliceInsertScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35SpliceInsertScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticImageDeactivateScheduleActionSettings:
    boto3_raw_data: "type_defs.StaticImageDeactivateScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    FadeOut = field("FadeOut")
    Layer = field("Layer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StaticImageDeactivateScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticImageDeactivateScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticImageOutputDeactivateScheduleActionSettingsOutput:
    boto3_raw_data: (
        "type_defs.StaticImageOutputDeactivateScheduleActionSettingsOutputTypeDef"
    ) = dataclasses.field()

    OutputNames = field("OutputNames")
    FadeOut = field("FadeOut")
    Layer = field("Layer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StaticImageOutputDeactivateScheduleActionSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StaticImageOutputDeactivateScheduleActionSettingsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimedMetadataScheduleActionSettings:
    boto3_raw_data: "type_defs.TimedMetadataScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    Id3 = field("Id3")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TimedMetadataScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimedMetadataScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35DeliveryRestrictions:
    boto3_raw_data: "type_defs.Scte35DeliveryRestrictionsTypeDef" = dataclasses.field()

    ArchiveAllowedFlag = field("ArchiveAllowedFlag")
    DeviceRestrictions = field("DeviceRestrictions")
    NoRegionalBlackoutFlag = field("NoRegionalBlackoutFlag")
    WebDeliveryAllowedFlag = field("WebDeliveryAllowedFlag")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Scte35DeliveryRestrictionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35DeliveryRestrictionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SdiSourceMappingUpdateRequest:
    boto3_raw_data: "type_defs.SdiSourceMappingUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    CardNumber = field("CardNumber")
    ChannelNumber = field("ChannelNumber")
    SdiSource = field("SdiSource")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SdiSourceMappingUpdateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SdiSourceMappingUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtCallerDecryptionRequest:
    boto3_raw_data: "type_defs.SrtCallerDecryptionRequestTypeDef" = dataclasses.field()

    Algorithm = field("Algorithm")
    PassphraseSecretArn = field("PassphraseSecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SrtCallerDecryptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SrtCallerDecryptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtCallerDecryption:
    boto3_raw_data: "type_defs.SrtCallerDecryptionTypeDef" = dataclasses.field()

    Algorithm = field("Algorithm")
    PassphraseSecretArn = field("PassphraseSecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SrtCallerDecryptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SrtCallerDecryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChannelRequest:
    boto3_raw_data: "type_defs.StartChannelRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDeleteMonitorDeploymentRequest:
    boto3_raw_data: "type_defs.StartDeleteMonitorDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDeleteMonitorDeploymentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeleteMonitorDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInputDeviceMaintenanceWindowRequest:
    boto3_raw_data: "type_defs.StartInputDeviceMaintenanceWindowRequestTypeDef" = (
        dataclasses.field()
    )

    InputDeviceId = field("InputDeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartInputDeviceMaintenanceWindowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInputDeviceMaintenanceWindowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInputDeviceRequest:
    boto3_raw_data: "type_defs.StartInputDeviceRequestTypeDef" = dataclasses.field()

    InputDeviceId = field("InputDeviceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInputDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInputDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMonitorDeploymentRequest:
    boto3_raw_data: "type_defs.StartMonitorDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMonitorDeploymentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMonitorDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMultiplexRequest:
    boto3_raw_data: "type_defs.StartMultiplexRequestTypeDef" = dataclasses.field()

    MultiplexId = field("MultiplexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMultiplexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMultiplexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartUpdateSignalMapRequest:
    boto3_raw_data: "type_defs.StartUpdateSignalMapRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    CloudWatchAlarmTemplateGroupIdentifiers = field(
        "CloudWatchAlarmTemplateGroupIdentifiers"
    )
    Description = field("Description")
    DiscoveryEntryPointArn = field("DiscoveryEntryPointArn")
    EventBridgeRuleTemplateGroupIdentifiers = field(
        "EventBridgeRuleTemplateGroupIdentifiers"
    )
    ForceRediscovery = field("ForceRediscovery")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartUpdateSignalMapRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartUpdateSignalMapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticImageOutputDeactivateScheduleActionSettings:
    boto3_raw_data: (
        "type_defs.StaticImageOutputDeactivateScheduleActionSettingsTypeDef"
    ) = dataclasses.field()

    OutputNames = field("OutputNames")
    FadeOut = field("FadeOut")
    Layer = field("Layer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StaticImageOutputDeactivateScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StaticImageOutputDeactivateScheduleActionSettingsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopChannelRequest:
    boto3_raw_data: "type_defs.StopChannelRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopInputDeviceRequest:
    boto3_raw_data: "type_defs.StopInputDeviceRequestTypeDef" = dataclasses.field()

    InputDeviceId = field("InputDeviceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopInputDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopInputDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopMultiplexRequest:
    boto3_raw_data: "type_defs.StopMultiplexRequestTypeDef" = dataclasses.field()

    MultiplexId = field("MultiplexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopMultiplexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopMultiplexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Thumbnail:
    boto3_raw_data: "type_defs.ThumbnailTypeDef" = dataclasses.field()

    Body = field("Body")
    ContentType = field("ContentType")
    ThumbnailType = field("ThumbnailType")
    TimeStamp = field("TimeStamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThumbnailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThumbnailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferInputDeviceRequest:
    boto3_raw_data: "type_defs.TransferInputDeviceRequestTypeDef" = dataclasses.field()

    InputDeviceId = field("InputDeviceId")
    TargetCustomerId = field("TargetCustomerId")
    TargetRegion = field("TargetRegion")
    TransferMessage = field("TransferMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransferInputDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferInputDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelPlacementGroupRequest:
    boto3_raw_data: "type_defs.UpdateChannelPlacementGroupRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelPlacementGroupId = field("ChannelPlacementGroupId")
    ClusterId = field("ClusterId")
    Name = field("Name")
    Nodes = field("Nodes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateChannelPlacementGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelPlacementGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCloudWatchAlarmTemplateGroupRequest:
    boto3_raw_data: "type_defs.UpdateCloudWatchAlarmTemplateGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCloudWatchAlarmTemplateGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCloudWatchAlarmTemplateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCloudWatchAlarmTemplateRequest:
    boto3_raw_data: "type_defs.UpdateCloudWatchAlarmTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    ComparisonOperator = field("ComparisonOperator")
    DatapointsToAlarm = field("DatapointsToAlarm")
    Description = field("Description")
    EvaluationPeriods = field("EvaluationPeriods")
    GroupIdentifier = field("GroupIdentifier")
    MetricName = field("MetricName")
    Name = field("Name")
    Period = field("Period")
    Statistic = field("Statistic")
    TargetResourceType = field("TargetResourceType")
    Threshold = field("Threshold")
    TreatMissingData = field("TreatMissingData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCloudWatchAlarmTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCloudWatchAlarmTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventBridgeRuleTemplateGroupRequest:
    boto3_raw_data: "type_defs.UpdateEventBridgeRuleTemplateGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEventBridgeRuleTemplateGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventBridgeRuleTemplateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNodeStateRequest:
    boto3_raw_data: "type_defs.UpdateNodeStateRequestTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    NodeId = field("NodeId")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNodeStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNodeStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSdiSourceRequest:
    boto3_raw_data: "type_defs.UpdateSdiSourceRequestTypeDef" = dataclasses.field()

    SdiSourceId = field("SdiSourceId")
    Mode = field("Mode")
    Name = field("Name")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSdiSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSdiSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoSelectorPid:
    boto3_raw_data: "type_defs.VideoSelectorPidTypeDef" = dataclasses.field()

    Pid = field("Pid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoSelectorPidTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoSelectorPidTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoSelectorProgramId:
    boto3_raw_data: "type_defs.VideoSelectorProgramIdTypeDef" = dataclasses.field()

    ProgramId = field("ProgramId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoSelectorProgramIdTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoSelectorProgramIdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateAccountConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountConfiguration(self):  # pragma: no cover
        return AccountConfiguration.make_one(
            self.boto3_raw_data["AccountConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccountConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalDestinations:
    boto3_raw_data: "type_defs.AdditionalDestinationsTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdditionalDestinationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalDestinationsTypeDef"]
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
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    AcquisitionPointId = field("AcquisitionPointId")
    AudioOnlyTimecodeControl = field("AudioOnlyTimecodeControl")
    CertificateMode = field("CertificateMode")
    ConnectionRetryInterval = field("ConnectionRetryInterval")
    EventId = field("EventId")
    EventIdMode = field("EventIdMode")
    EventStopBehavior = field("EventStopBehavior")
    FilecacheDuration = field("FilecacheDuration")
    FragmentLength = field("FragmentLength")
    InputLossAction = field("InputLossAction")
    NumRetries = field("NumRetries")
    RestartDelay = field("RestartDelay")
    SegmentationMode = field("SegmentationMode")
    SendDelayMs = field("SendDelayMs")
    SparseTrackType = field("SparseTrackType")
    StreamManifestBehavior = field("StreamManifestBehavior")
    TimestampOffset = field("TimestampOffset")
    TimestampOffsetMode = field("TimestampOffsetMode")

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
class RtmpOutputSettings:
    boto3_raw_data: "type_defs.RtmpOutputSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    CertificateMode = field("CertificateMode")
    ConnectionRetryInterval = field("ConnectionRetryInterval")
    NumRetries = field("NumRetries")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RtmpOutputSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RtmpOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveCdnSettings:
    boto3_raw_data: "type_defs.ArchiveCdnSettingsTypeDef" = dataclasses.field()

    @cached_property
    def ArchiveS3Settings(self):  # pragma: no cover
        return ArchiveS3Settings.make_one(self.boto3_raw_data["ArchiveS3Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveCdnSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveCdnSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioChannelMappingOutput:
    boto3_raw_data: "type_defs.AudioChannelMappingOutputTypeDef" = dataclasses.field()

    @cached_property
    def InputChannelLevels(self):  # pragma: no cover
        return InputChannelLevel.make_many(self.boto3_raw_data["InputChannelLevels"])

    OutputChannel = field("OutputChannel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioChannelMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioChannelMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioChannelMapping:
    boto3_raw_data: "type_defs.AudioChannelMappingTypeDef" = dataclasses.field()

    @cached_property
    def InputChannelLevels(self):  # pragma: no cover
        return InputChannelLevel.make_many(self.boto3_raw_data["InputChannelLevels"])

    OutputChannel = field("OutputChannel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioChannelMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioChannelMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioCodecSettingsOutput:
    boto3_raw_data: "type_defs.AudioCodecSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AacSettings(self):  # pragma: no cover
        return AacSettings.make_one(self.boto3_raw_data["AacSettings"])

    @cached_property
    def Ac3Settings(self):  # pragma: no cover
        return Ac3Settings.make_one(self.boto3_raw_data["Ac3Settings"])

    @cached_property
    def Eac3AtmosSettings(self):  # pragma: no cover
        return Eac3AtmosSettings.make_one(self.boto3_raw_data["Eac3AtmosSettings"])

    @cached_property
    def Eac3Settings(self):  # pragma: no cover
        return Eac3Settings.make_one(self.boto3_raw_data["Eac3Settings"])

    @cached_property
    def Mp2Settings(self):  # pragma: no cover
        return Mp2Settings.make_one(self.boto3_raw_data["Mp2Settings"])

    PassThroughSettings = field("PassThroughSettings")

    @cached_property
    def WavSettings(self):  # pragma: no cover
        return WavSettings.make_one(self.boto3_raw_data["WavSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioCodecSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioCodecSettingsOutputTypeDef"]
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
    def Eac3AtmosSettings(self):  # pragma: no cover
        return Eac3AtmosSettings.make_one(self.boto3_raw_data["Eac3AtmosSettings"])

    @cached_property
    def Eac3Settings(self):  # pragma: no cover
        return Eac3Settings.make_one(self.boto3_raw_data["Eac3Settings"])

    @cached_property
    def Mp2Settings(self):  # pragma: no cover
        return Mp2Settings.make_one(self.boto3_raw_data["Mp2Settings"])

    PassThroughSettings = field("PassThroughSettings")

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
class AudioOnlyHlsSettings:
    boto3_raw_data: "type_defs.AudioOnlyHlsSettingsTypeDef" = dataclasses.field()

    AudioGroupId = field("AudioGroupId")

    @cached_property
    def AudioOnlyImage(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["AudioOnlyImage"])

    AudioTrackType = field("AudioTrackType")
    SegmentType = field("SegmentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioOnlyHlsSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioOnlyHlsSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailBlanking:
    boto3_raw_data: "type_defs.AvailBlankingTypeDef" = dataclasses.field()

    @cached_property
    def AvailBlankingImage(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["AvailBlankingImage"])

    State = field("State")

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
class BlackoutSlate:
    boto3_raw_data: "type_defs.BlackoutSlateTypeDef" = dataclasses.field()

    @cached_property
    def BlackoutSlateImage(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["BlackoutSlateImage"])

    NetworkEndBlackout = field("NetworkEndBlackout")

    @cached_property
    def NetworkEndBlackoutImage(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["NetworkEndBlackoutImage"])

    NetworkId = field("NetworkId")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlackoutSlateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlackoutSlateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BurnInDestinationSettings:
    boto3_raw_data: "type_defs.BurnInDestinationSettingsTypeDef" = dataclasses.field()

    Alignment = field("Alignment")
    BackgroundColor = field("BackgroundColor")
    BackgroundOpacity = field("BackgroundOpacity")

    @cached_property
    def Font(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["Font"])

    FontColor = field("FontColor")
    FontOpacity = field("FontOpacity")
    FontResolution = field("FontResolution")
    FontSize = field("FontSize")
    OutlineColor = field("OutlineColor")
    OutlineSize = field("OutlineSize")
    ShadowColor = field("ShadowColor")
    ShadowOpacity = field("ShadowOpacity")
    ShadowXOffset = field("ShadowXOffset")
    ShadowYOffset = field("ShadowYOffset")
    TeletextGridControl = field("TeletextGridControl")
    XPosition = field("XPosition")
    YPosition = field("YPosition")
    SubtitleRows = field("SubtitleRows")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BurnInDestinationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BurnInDestinationSettingsTypeDef"]
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
    BackgroundColor = field("BackgroundColor")
    BackgroundOpacity = field("BackgroundOpacity")

    @cached_property
    def Font(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["Font"])

    FontColor = field("FontColor")
    FontOpacity = field("FontOpacity")
    FontResolution = field("FontResolution")
    FontSize = field("FontSize")
    OutlineColor = field("OutlineColor")
    OutlineSize = field("OutlineSize")
    ShadowColor = field("ShadowColor")
    ShadowOpacity = field("ShadowOpacity")
    ShadowXOffset = field("ShadowXOffset")
    ShadowYOffset = field("ShadowYOffset")
    TeletextGridControl = field("TeletextGridControl")
    XPosition = field("XPosition")
    YPosition = field("YPosition")
    SubtitleRows = field("SubtitleRows")

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
class InputLossBehavior:
    boto3_raw_data: "type_defs.InputLossBehaviorTypeDef" = dataclasses.field()

    BlackFrameMsec = field("BlackFrameMsec")
    InputLossImageColor = field("InputLossImageColor")

    @cached_property
    def InputLossImageSlate(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["InputLossImageSlate"])

    InputLossImageType = field("InputLossImageType")
    RepeatFrameMsec = field("RepeatFrameMsec")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputLossBehaviorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputLossBehaviorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticImageActivateScheduleActionSettings:
    boto3_raw_data: "type_defs.StaticImageActivateScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Image(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["Image"])

    Duration = field("Duration")
    FadeIn = field("FadeIn")
    FadeOut = field("FadeOut")
    Height = field("Height")
    ImageX = field("ImageX")
    ImageY = field("ImageY")
    Layer = field("Layer")
    Opacity = field("Opacity")
    Width = field("Width")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StaticImageActivateScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticImageActivateScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticImageOutputActivateScheduleActionSettingsOutput:
    boto3_raw_data: (
        "type_defs.StaticImageOutputActivateScheduleActionSettingsOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Image(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["Image"])

    OutputNames = field("OutputNames")
    Duration = field("Duration")
    FadeIn = field("FadeIn")
    FadeOut = field("FadeOut")
    Height = field("Height")
    ImageX = field("ImageX")
    ImageY = field("ImageY")
    Layer = field("Layer")
    Opacity = field("Opacity")
    Width = field("Width")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StaticImageOutputActivateScheduleActionSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StaticImageOutputActivateScheduleActionSettingsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticImageOutputActivateScheduleActionSettings:
    boto3_raw_data: (
        "type_defs.StaticImageOutputActivateScheduleActionSettingsTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Image(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["Image"])

    OutputNames = field("OutputNames")
    Duration = field("Duration")
    FadeIn = field("FadeIn")
    FadeOut = field("FadeOut")
    Height = field("Height")
    ImageX = field("ImageX")
    ImageY = field("ImageY")
    Layer = field("Layer")
    Opacity = field("Opacity")
    Width = field("Width")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StaticImageOutputActivateScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StaticImageOutputActivateScheduleActionSettingsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticKeySettings:
    boto3_raw_data: "type_defs.StaticKeySettingsTypeDef" = dataclasses.field()

    StaticKeyValue = field("StaticKeyValue")

    @cached_property
    def KeyProviderServer(self):  # pragma: no cover
        return InputLocation.make_one(self.boto3_raw_data["KeyProviderServer"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StaticKeySettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticKeySettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioTrackSelectionOutput:
    boto3_raw_data: "type_defs.AudioTrackSelectionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Tracks(self):  # pragma: no cover
        return AudioTrack.make_many(self.boto3_raw_data["Tracks"])

    @cached_property
    def DolbyEDecode(self):  # pragma: no cover
        return AudioDolbyEDecode.make_one(self.boto3_raw_data["DolbyEDecode"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioTrackSelectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioTrackSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioTrackSelection:
    boto3_raw_data: "type_defs.AudioTrackSelectionTypeDef" = dataclasses.field()

    @cached_property
    def Tracks(self):  # pragma: no cover
        return AudioTrack.make_many(self.boto3_raw_data["Tracks"])

    @cached_property
    def DolbyEDecode(self):  # pragma: no cover
        return AudioDolbyEDecode.make_one(self.boto3_raw_data["DolbyEDecode"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioTrackSelectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioTrackSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Av1ColorSpaceSettingsOutput:
    boto3_raw_data: "type_defs.Av1ColorSpaceSettingsOutputTypeDef" = dataclasses.field()

    ColorSpacePassthroughSettings = field("ColorSpacePassthroughSettings")

    @cached_property
    def Hdr10Settings(self):  # pragma: no cover
        return Hdr10Settings.make_one(self.boto3_raw_data["Hdr10Settings"])

    Rec601Settings = field("Rec601Settings")
    Rec709Settings = field("Rec709Settings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Av1ColorSpaceSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Av1ColorSpaceSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Av1ColorSpaceSettings:
    boto3_raw_data: "type_defs.Av1ColorSpaceSettingsTypeDef" = dataclasses.field()

    ColorSpacePassthroughSettings = field("ColorSpacePassthroughSettings")

    @cached_property
    def Hdr10Settings(self):  # pragma: no cover
        return Hdr10Settings.make_one(self.boto3_raw_data["Hdr10Settings"])

    Rec601Settings = field("Rec601Settings")
    Rec709Settings = field("Rec709Settings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Av1ColorSpaceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Av1ColorSpaceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H265ColorSpaceSettingsOutput:
    boto3_raw_data: "type_defs.H265ColorSpaceSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    ColorSpacePassthroughSettings = field("ColorSpacePassthroughSettings")
    DolbyVision81Settings = field("DolbyVision81Settings")

    @cached_property
    def Hdr10Settings(self):  # pragma: no cover
        return Hdr10Settings.make_one(self.boto3_raw_data["Hdr10Settings"])

    Rec601Settings = field("Rec601Settings")
    Rec709Settings = field("Rec709Settings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.H265ColorSpaceSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H265ColorSpaceSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H265ColorSpaceSettings:
    boto3_raw_data: "type_defs.H265ColorSpaceSettingsTypeDef" = dataclasses.field()

    ColorSpacePassthroughSettings = field("ColorSpacePassthroughSettings")
    DolbyVision81Settings = field("DolbyVision81Settings")

    @cached_property
    def Hdr10Settings(self):  # pragma: no cover
        return Hdr10Settings.make_one(self.boto3_raw_data["Hdr10Settings"])

    Rec601Settings = field("Rec601Settings")
    Rec709Settings = field("Rec709Settings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.H265ColorSpaceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H265ColorSpaceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoSelectorColorSpaceSettings:
    boto3_raw_data: "type_defs.VideoSelectorColorSpaceSettingsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Hdr10Settings(self):  # pragma: no cover
        return Hdr10Settings.make_one(self.boto3_raw_data["Hdr10Settings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VideoSelectorColorSpaceSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoSelectorColorSpaceSettingsTypeDef"]
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

    CaptureInterval = field("CaptureInterval")
    CaptureIntervalUnits = field("CaptureIntervalUnits")

    @cached_property
    def TimecodeBurninSettings(self):  # pragma: no cover
        return TimecodeBurninSettings.make_one(
            self.boto3_raw_data["TimecodeBurninSettings"]
        )

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
class AvailSettings:
    boto3_raw_data: "type_defs.AvailSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Esam(self):  # pragma: no cover
        return Esam.make_one(self.boto3_raw_data["Esam"])

    @cached_property
    def Scte35SpliceInsert(self):  # pragma: no cover
        return Scte35SpliceInsert.make_one(self.boto3_raw_data["Scte35SpliceInsert"])

    @cached_property
    def Scte35TimeSignalApos(self):  # pragma: no cover
        return Scte35TimeSignalApos.make_one(
            self.boto3_raw_data["Scte35TimeSignalApos"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvailSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AvailSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteResponse:
    boto3_raw_data: "type_defs.BatchDeleteResponseTypeDef" = dataclasses.field()

    @cached_property
    def Failed(self):  # pragma: no cover
        return BatchFailedResultModel.make_many(self.boto3_raw_data["Failed"])

    @cached_property
    def Successful(self):  # pragma: no cover
        return BatchSuccessfulResultModel.make_many(self.boto3_raw_data["Successful"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStartResponse:
    boto3_raw_data: "type_defs.BatchStartResponseTypeDef" = dataclasses.field()

    @cached_property
    def Failed(self):  # pragma: no cover
        return BatchFailedResultModel.make_many(self.boto3_raw_data["Failed"])

    @cached_property
    def Successful(self):  # pragma: no cover
        return BatchSuccessfulResultModel.make_many(self.boto3_raw_data["Successful"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchStartResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStartResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStopResponse:
    boto3_raw_data: "type_defs.BatchStopResponseTypeDef" = dataclasses.field()

    @cached_property
    def Failed(self):  # pragma: no cover
        return BatchFailedResultModel.make_many(self.boto3_raw_data["Failed"])

    @cached_property
    def Successful(self):  # pragma: no cover
        return BatchSuccessfulResultModel.make_many(self.boto3_raw_data["Successful"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchStopResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStopResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelPlacementGroupResponse:
    boto3_raw_data: "type_defs.CreateChannelPlacementGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Channels = field("Channels")
    ClusterId = field("ClusterId")
    Id = field("Id")
    Name = field("Name")
    Nodes = field("Nodes")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateChannelPlacementGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelPlacementGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudWatchAlarmTemplateGroupResponse:
    boto3_raw_data: "type_defs.CreateCloudWatchAlarmTemplateGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudWatchAlarmTemplateGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudWatchAlarmTemplateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudWatchAlarmTemplateResponse:
    boto3_raw_data: "type_defs.CreateCloudWatchAlarmTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ComparisonOperator = field("ComparisonOperator")
    CreatedAt = field("CreatedAt")
    DatapointsToAlarm = field("DatapointsToAlarm")
    Description = field("Description")
    EvaluationPeriods = field("EvaluationPeriods")
    GroupId = field("GroupId")
    Id = field("Id")
    MetricName = field("MetricName")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Period = field("Period")
    Statistic = field("Statistic")
    Tags = field("Tags")
    TargetResourceType = field("TargetResourceType")
    Threshold = field("Threshold")
    TreatMissingData = field("TreatMissingData")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudWatchAlarmTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudWatchAlarmTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventBridgeRuleTemplateGroupResponse:
    boto3_raw_data: "type_defs.CreateEventBridgeRuleTemplateGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEventBridgeRuleTemplateGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventBridgeRuleTemplateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodeRegistrationScriptResponse:
    boto3_raw_data: "type_defs.CreateNodeRegistrationScriptResponseTypeDef" = (
        dataclasses.field()
    )

    NodeRegistrationScript = field("NodeRegistrationScript")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateNodeRegistrationScriptResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNodeRegistrationScriptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelPlacementGroupResponse:
    boto3_raw_data: "type_defs.DeleteChannelPlacementGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Channels = field("Channels")
    ClusterId = field("ClusterId")
    Id = field("Id")
    Name = field("Name")
    Nodes = field("Nodes")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteChannelPlacementGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelPlacementGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeAccountConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountConfiguration(self):  # pragma: no cover
        return AccountConfiguration.make_one(
            self.boto3_raw_data["AccountConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelPlacementGroupResponse:
    boto3_raw_data: "type_defs.DescribeChannelPlacementGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Channels = field("Channels")
    ClusterId = field("ClusterId")
    Id = field("Id")
    Name = field("Name")
    Nodes = field("Nodes")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelPlacementGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelPlacementGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputDeviceThumbnailResponse:
    boto3_raw_data: "type_defs.DescribeInputDeviceThumbnailResponseTypeDef" = (
        dataclasses.field()
    )

    Body = field("Body")
    ContentType = field("ContentType")
    ContentLength = field("ContentLength")
    ETag = field("ETag")
    LastModified = field("LastModified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInputDeviceThumbnailResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputDeviceThumbnailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudWatchAlarmTemplateGroupResponse:
    boto3_raw_data: "type_defs.GetCloudWatchAlarmTemplateGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudWatchAlarmTemplateGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudWatchAlarmTemplateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudWatchAlarmTemplateResponse:
    boto3_raw_data: "type_defs.GetCloudWatchAlarmTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ComparisonOperator = field("ComparisonOperator")
    CreatedAt = field("CreatedAt")
    DatapointsToAlarm = field("DatapointsToAlarm")
    Description = field("Description")
    EvaluationPeriods = field("EvaluationPeriods")
    GroupId = field("GroupId")
    Id = field("Id")
    MetricName = field("MetricName")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Period = field("Period")
    Statistic = field("Statistic")
    Tags = field("Tags")
    TargetResourceType = field("TargetResourceType")
    Threshold = field("Threshold")
    TreatMissingData = field("TreatMissingData")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudWatchAlarmTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudWatchAlarmTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventBridgeRuleTemplateGroupResponse:
    boto3_raw_data: "type_defs.GetEventBridgeRuleTemplateGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEventBridgeRuleTemplateGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventBridgeRuleTemplateGroupResponseTypeDef"]
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

    Tags = field("Tags")

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
class UpdateAccountConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateAccountConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountConfiguration(self):  # pragma: no cover
        return AccountConfiguration.make_one(
            self.boto3_raw_data["AccountConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccountConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelPlacementGroupResponse:
    boto3_raw_data: "type_defs.UpdateChannelPlacementGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Channels = field("Channels")
    ClusterId = field("ClusterId")
    Id = field("Id")
    Name = field("Name")
    Nodes = field("Nodes")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateChannelPlacementGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelPlacementGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCloudWatchAlarmTemplateGroupResponse:
    boto3_raw_data: "type_defs.UpdateCloudWatchAlarmTemplateGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCloudWatchAlarmTemplateGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCloudWatchAlarmTemplateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCloudWatchAlarmTemplateResponse:
    boto3_raw_data: "type_defs.UpdateCloudWatchAlarmTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ComparisonOperator = field("ComparisonOperator")
    CreatedAt = field("CreatedAt")
    DatapointsToAlarm = field("DatapointsToAlarm")
    Description = field("Description")
    EvaluationPeriods = field("EvaluationPeriods")
    GroupId = field("GroupId")
    Id = field("Id")
    MetricName = field("MetricName")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Period = field("Period")
    Statistic = field("Statistic")
    Tags = field("Tags")
    TargetResourceType = field("TargetResourceType")
    Threshold = field("Threshold")
    TreatMissingData = field("TreatMissingData")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCloudWatchAlarmTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCloudWatchAlarmTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventBridgeRuleTemplateGroupResponse:
    boto3_raw_data: "type_defs.UpdateEventBridgeRuleTemplateGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEventBridgeRuleTemplateGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventBridgeRuleTemplateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPackageV2GroupSettingsOutput:
    boto3_raw_data: "type_defs.MediaPackageV2GroupSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CaptionLanguageMappings(self):  # pragma: no cover
        return CaptionLanguageMapping.make_many(
            self.boto3_raw_data["CaptionLanguageMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaPackageV2GroupSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaPackageV2GroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPackageV2GroupSettings:
    boto3_raw_data: "type_defs.MediaPackageV2GroupSettingsTypeDef" = dataclasses.field()

    @cached_property
    def CaptionLanguageMappings(self):  # pragma: no cover
        return CaptionLanguageMapping.make_many(
            self.boto3_raw_data["CaptionLanguageMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaPackageV2GroupSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaPackageV2GroupSettingsTypeDef"]
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

    @cached_property
    def OutputRectangle(self):  # pragma: no cover
        return CaptionRectangle.make_one(self.boto3_raw_data["OutputRectangle"])

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
class ListVersionsResponse:
    boto3_raw_data: "type_defs.ListVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Versions(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

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
class PipelineDetail:
    boto3_raw_data: "type_defs.PipelineDetailTypeDef" = dataclasses.field()

    ActiveInputAttachmentName = field("ActiveInputAttachmentName")
    ActiveInputSwitchActionName = field("ActiveInputSwitchActionName")
    ActiveMotionGraphicsActionName = field("ActiveMotionGraphicsActionName")
    ActiveMotionGraphicsUri = field("ActiveMotionGraphicsUri")
    PipelineId = field("PipelineId")

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudWatchAlarmTemplateGroupsResponse:
    boto3_raw_data: "type_defs.ListCloudWatchAlarmTemplateGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudWatchAlarmTemplateGroups(self):  # pragma: no cover
        return CloudWatchAlarmTemplateGroupSummary.make_many(
            self.boto3_raw_data["CloudWatchAlarmTemplateGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudWatchAlarmTemplateGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudWatchAlarmTemplateGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudWatchAlarmTemplatesResponse:
    boto3_raw_data: "type_defs.ListCloudWatchAlarmTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudWatchAlarmTemplates(self):  # pragma: no cover
        return CloudWatchAlarmTemplateSummary.make_many(
            self.boto3_raw_data["CloudWatchAlarmTemplates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudWatchAlarmTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudWatchAlarmTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterNetworkSettingsCreateRequest:
    boto3_raw_data: "type_defs.ClusterNetworkSettingsCreateRequestTypeDef" = (
        dataclasses.field()
    )

    DefaultRoute = field("DefaultRoute")

    @cached_property
    def InterfaceMappings(self):  # pragma: no cover
        return InterfaceMappingCreateRequest.make_many(
            self.boto3_raw_data["InterfaceMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ClusterNetworkSettingsCreateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterNetworkSettingsCreateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterNetworkSettings:
    boto3_raw_data: "type_defs.ClusterNetworkSettingsTypeDef" = dataclasses.field()

    DefaultRoute = field("DefaultRoute")

    @cached_property
    def InterfaceMappings(self):  # pragma: no cover
        return InterfaceMapping.make_many(self.boto3_raw_data["InterfaceMappings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterNetworkSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterNetworkSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterNetworkSettingsUpdateRequest:
    boto3_raw_data: "type_defs.ClusterNetworkSettingsUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    DefaultRoute = field("DefaultRoute")

    @cached_property
    def InterfaceMappings(self):  # pragma: no cover
        return InterfaceMappingUpdateRequest.make_many(
            self.boto3_raw_data["InterfaceMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ClusterNetworkSettingsUpdateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterNetworkSettingsUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColorCorrectionSettingsOutput:
    boto3_raw_data: "type_defs.ColorCorrectionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalColorCorrections(self):  # pragma: no cover
        return ColorCorrection.make_many(self.boto3_raw_data["GlobalColorCorrections"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ColorCorrectionSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColorCorrectionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColorCorrectionSettings:
    boto3_raw_data: "type_defs.ColorCorrectionSettingsTypeDef" = dataclasses.field()

    @cached_property
    def GlobalColorCorrections(self):  # pragma: no cover
        return ColorCorrection.make_many(self.boto3_raw_data["GlobalColorCorrections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ColorCorrectionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColorCorrectionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventBridgeRuleTemplateRequest:
    boto3_raw_data: "type_defs.CreateEventBridgeRuleTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    EventType = field("EventType")
    GroupIdentifier = field("GroupIdentifier")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def EventTargets(self):  # pragma: no cover
        return EventBridgeRuleTemplateTarget.make_many(
            self.boto3_raw_data["EventTargets"]
        )

    Tags = field("Tags")
    RequestId = field("RequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEventBridgeRuleTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventBridgeRuleTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventBridgeRuleTemplateResponse:
    boto3_raw_data: "type_defs.CreateEventBridgeRuleTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EventTargets(self):  # pragma: no cover
        return EventBridgeRuleTemplateTarget.make_many(
            self.boto3_raw_data["EventTargets"]
        )

    EventType = field("EventType")
    GroupId = field("GroupId")
    Id = field("Id")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEventBridgeRuleTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventBridgeRuleTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventBridgeRuleTemplateResponse:
    boto3_raw_data: "type_defs.GetEventBridgeRuleTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EventTargets(self):  # pragma: no cover
        return EventBridgeRuleTemplateTarget.make_many(
            self.boto3_raw_data["EventTargets"]
        )

    EventType = field("EventType")
    GroupId = field("GroupId")
    Id = field("Id")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEventBridgeRuleTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventBridgeRuleTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventBridgeRuleTemplateRequest:
    boto3_raw_data: "type_defs.UpdateEventBridgeRuleTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    Description = field("Description")

    @cached_property
    def EventTargets(self):  # pragma: no cover
        return EventBridgeRuleTemplateTarget.make_many(
            self.boto3_raw_data["EventTargets"]
        )

    EventType = field("EventType")
    GroupIdentifier = field("GroupIdentifier")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEventBridgeRuleTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventBridgeRuleTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventBridgeRuleTemplateResponse:
    boto3_raw_data: "type_defs.UpdateEventBridgeRuleTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EventTargets(self):  # pragma: no cover
        return EventBridgeRuleTemplateTarget.make_many(
            self.boto3_raw_data["EventTargets"]
        )

    EventType = field("EventType")
    GroupId = field("GroupId")
    Id = field("Id")
    ModifiedAt = field("ModifiedAt")
    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEventBridgeRuleTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventBridgeRuleTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInputSecurityGroupRequest:
    boto3_raw_data: "type_defs.CreateInputSecurityGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Tags = field("Tags")

    @cached_property
    def WhitelistRules(self):  # pragma: no cover
        return InputWhitelistRuleCidr.make_many(self.boto3_raw_data["WhitelistRules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateInputSecurityGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInputSecurityGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInputSecurityGroupRequest:
    boto3_raw_data: "type_defs.UpdateInputSecurityGroupRequestTypeDef" = (
        dataclasses.field()
    )

    InputSecurityGroupId = field("InputSecurityGroupId")
    Tags = field("Tags")

    @cached_property
    def WhitelistRules(self):  # pragma: no cover
        return InputWhitelistRuleCidr.make_many(self.boto3_raw_data["WhitelistRules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateInputSecurityGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInputSecurityGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultiplexRequest:
    boto3_raw_data: "type_defs.CreateMultiplexRequestTypeDef" = dataclasses.field()

    AvailabilityZones = field("AvailabilityZones")

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexSettings.make_one(self.boto3_raw_data["MultiplexSettings"])

    Name = field("Name")
    RequestId = field("RequestId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMultiplexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiplexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkRequest:
    boto3_raw_data: "type_defs.CreateNetworkRequestTypeDef" = dataclasses.field()

    @cached_property
    def IpPools(self):  # pragma: no cover
        return IpPoolCreateRequest.make_many(self.boto3_raw_data["IpPools"])

    Name = field("Name")
    RequestId = field("RequestId")

    @cached_property
    def Routes(self):  # pragma: no cover
        return RouteCreateRequest.make_many(self.boto3_raw_data["Routes"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkResponse:
    boto3_raw_data: "type_defs.CreateNetworkResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AssociatedClusterIds = field("AssociatedClusterIds")
    Id = field("Id")

    @cached_property
    def IpPools(self):  # pragma: no cover
        return IpPool.make_many(self.boto3_raw_data["IpPools"])

    Name = field("Name")

    @cached_property
    def Routes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["Routes"])

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNetworkResponse:
    boto3_raw_data: "type_defs.DeleteNetworkResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AssociatedClusterIds = field("AssociatedClusterIds")
    Id = field("Id")

    @cached_property
    def IpPools(self):  # pragma: no cover
        return IpPool.make_many(self.boto3_raw_data["IpPools"])

    Name = field("Name")

    @cached_property
    def Routes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["Routes"])

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNetworkResponse:
    boto3_raw_data: "type_defs.DescribeNetworkResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AssociatedClusterIds = field("AssociatedClusterIds")
    Id = field("Id")

    @cached_property
    def IpPools(self):  # pragma: no cover
        return IpPool.make_many(self.boto3_raw_data["IpPools"])

    Name = field("Name")

    @cached_property
    def Routes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["Routes"])

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNetworkSummary:
    boto3_raw_data: "type_defs.DescribeNetworkSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AssociatedClusterIds = field("AssociatedClusterIds")
    Id = field("Id")

    @cached_property
    def IpPools(self):  # pragma: no cover
        return IpPool.make_many(self.boto3_raw_data["IpPools"])

    Name = field("Name")

    @cached_property
    def Routes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["Routes"])

    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNetworkSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNetworkSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNetworkResponse:
    boto3_raw_data: "type_defs.UpdateNetworkResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AssociatedClusterIds = field("AssociatedClusterIds")
    Id = field("Id")

    @cached_property
    def IpPools(self):  # pragma: no cover
        return IpPool.make_many(self.boto3_raw_data["IpPools"])

    Name = field("Name")

    @cached_property
    def Routes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["Routes"])

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodeRegistrationScriptRequest:
    boto3_raw_data: "type_defs.CreateNodeRegistrationScriptRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")
    Id = field("Id")
    Name = field("Name")

    @cached_property
    def NodeInterfaceMappings(self):  # pragma: no cover
        return NodeInterfaceMapping.make_many(
            self.boto3_raw_data["NodeInterfaceMappings"]
        )

    RequestId = field("RequestId")
    Role = field("Role")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateNodeRegistrationScriptRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNodeRegistrationScriptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodeRequest:
    boto3_raw_data: "type_defs.CreateNodeRequestTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    Name = field("Name")

    @cached_property
    def NodeInterfaceMappings(self):  # pragma: no cover
        return NodeInterfaceMappingCreateRequest.make_many(
            self.boto3_raw_data["NodeInterfaceMappings"]
        )

    RequestId = field("RequestId")
    Role = field("Role")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateNodeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodeResponse:
    boto3_raw_data: "type_defs.CreateNodeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelPlacementGroups = field("ChannelPlacementGroups")
    ClusterId = field("ClusterId")
    ConnectionState = field("ConnectionState")
    Id = field("Id")
    InstanceArn = field("InstanceArn")
    Name = field("Name")

    @cached_property
    def NodeInterfaceMappings(self):  # pragma: no cover
        return NodeInterfaceMapping.make_many(
            self.boto3_raw_data["NodeInterfaceMappings"]
        )

    Role = field("Role")
    State = field("State")

    @cached_property
    def SdiSourceMappings(self):  # pragma: no cover
        return SdiSourceMapping.make_many(self.boto3_raw_data["SdiSourceMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNodeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNodeResponse:
    boto3_raw_data: "type_defs.DeleteNodeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelPlacementGroups = field("ChannelPlacementGroups")
    ClusterId = field("ClusterId")
    ConnectionState = field("ConnectionState")
    Id = field("Id")
    InstanceArn = field("InstanceArn")
    Name = field("Name")

    @cached_property
    def NodeInterfaceMappings(self):  # pragma: no cover
        return NodeInterfaceMapping.make_many(
            self.boto3_raw_data["NodeInterfaceMappings"]
        )

    Role = field("Role")
    State = field("State")

    @cached_property
    def SdiSourceMappings(self):  # pragma: no cover
        return SdiSourceMapping.make_many(self.boto3_raw_data["SdiSourceMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNodeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodeResponse:
    boto3_raw_data: "type_defs.DescribeNodeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelPlacementGroups = field("ChannelPlacementGroups")
    ClusterId = field("ClusterId")
    ConnectionState = field("ConnectionState")
    Id = field("Id")
    InstanceArn = field("InstanceArn")
    Name = field("Name")

    @cached_property
    def NodeInterfaceMappings(self):  # pragma: no cover
        return NodeInterfaceMapping.make_many(
            self.boto3_raw_data["NodeInterfaceMappings"]
        )

    Role = field("Role")
    State = field("State")

    @cached_property
    def SdiSourceMappings(self):  # pragma: no cover
        return SdiSourceMapping.make_many(self.boto3_raw_data["SdiSourceMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNodeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodeSummary:
    boto3_raw_data: "type_defs.DescribeNodeSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelPlacementGroups = field("ChannelPlacementGroups")
    ClusterId = field("ClusterId")
    ConnectionState = field("ConnectionState")
    Id = field("Id")
    InstanceArn = field("InstanceArn")
    ManagedInstanceId = field("ManagedInstanceId")
    Name = field("Name")

    @cached_property
    def NodeInterfaceMappings(self):  # pragma: no cover
        return NodeInterfaceMapping.make_many(
            self.boto3_raw_data["NodeInterfaceMappings"]
        )

    Role = field("Role")
    State = field("State")

    @cached_property
    def SdiSourceMappings(self):  # pragma: no cover
        return SdiSourceMapping.make_many(self.boto3_raw_data["SdiSourceMappings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNodeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNodeResponse:
    boto3_raw_data: "type_defs.UpdateNodeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelPlacementGroups = field("ChannelPlacementGroups")
    ClusterId = field("ClusterId")
    ConnectionState = field("ConnectionState")
    Id = field("Id")
    InstanceArn = field("InstanceArn")
    Name = field("Name")

    @cached_property
    def NodeInterfaceMappings(self):  # pragma: no cover
        return NodeInterfaceMapping.make_many(
            self.boto3_raw_data["NodeInterfaceMappings"]
        )

    Role = field("Role")
    State = field("State")

    @cached_property
    def SdiSourceMappings(self):  # pragma: no cover
        return SdiSourceMapping.make_many(self.boto3_raw_data["SdiSourceMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNodeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNodeStateResponse:
    boto3_raw_data: "type_defs.UpdateNodeStateResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelPlacementGroups = field("ChannelPlacementGroups")
    ClusterId = field("ClusterId")
    ConnectionState = field("ConnectionState")
    Id = field("Id")
    InstanceArn = field("InstanceArn")
    Name = field("Name")

    @cached_property
    def NodeInterfaceMappings(self):  # pragma: no cover
        return NodeInterfaceMapping.make_many(
            self.boto3_raw_data["NodeInterfaceMappings"]
        )

    Role = field("Role")
    State = field("State")

    @cached_property
    def SdiSourceMappings(self):  # pragma: no cover
        return SdiSourceMapping.make_many(self.boto3_raw_data["SdiSourceMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNodeStateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNodeStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSdiSourceResponse:
    boto3_raw_data: "type_defs.CreateSdiSourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def SdiSource(self):  # pragma: no cover
        return SdiSource.make_one(self.boto3_raw_data["SdiSource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSdiSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSdiSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSdiSourceResponse:
    boto3_raw_data: "type_defs.DeleteSdiSourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def SdiSource(self):  # pragma: no cover
        return SdiSource.make_one(self.boto3_raw_data["SdiSource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSdiSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSdiSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSdiSourceResponse:
    boto3_raw_data: "type_defs.DescribeSdiSourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def SdiSource(self):  # pragma: no cover
        return SdiSource.make_one(self.boto3_raw_data["SdiSource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSdiSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSdiSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSdiSourceResponse:
    boto3_raw_data: "type_defs.UpdateSdiSourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def SdiSource(self):  # pragma: no cover
        return SdiSource.make_one(self.boto3_raw_data["SdiSource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSdiSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSdiSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseOfferingRequest:
    boto3_raw_data: "type_defs.PurchaseOfferingRequestTypeDef" = dataclasses.field()

    Count = field("Count")
    OfferingId = field("OfferingId")
    Name = field("Name")

    @cached_property
    def RenewalSettings(self):  # pragma: no cover
        return RenewalSettings.make_one(self.boto3_raw_data["RenewalSettings"])

    RequestId = field("RequestId")
    Start = field("Start")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PurchaseOfferingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseOfferingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReservationRequest:
    boto3_raw_data: "type_defs.UpdateReservationRequestTypeDef" = dataclasses.field()

    ReservationId = field("ReservationId")
    Name = field("Name")

    @cached_property
    def RenewalSettings(self):  # pragma: no cover
        return RenewalSettings.make_one(self.boto3_raw_data["RenewalSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReservationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReservationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReservationResponse:
    boto3_raw_data: "type_defs.DeleteReservationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Count = field("Count")
    CurrencyCode = field("CurrencyCode")
    Duration = field("Duration")
    DurationUnits = field("DurationUnits")
    End = field("End")
    FixedPrice = field("FixedPrice")
    Name = field("Name")
    OfferingDescription = field("OfferingDescription")
    OfferingId = field("OfferingId")
    OfferingType = field("OfferingType")
    Region = field("Region")

    @cached_property
    def RenewalSettings(self):  # pragma: no cover
        return RenewalSettings.make_one(self.boto3_raw_data["RenewalSettings"])

    ReservationId = field("ReservationId")

    @cached_property
    def ResourceSpecification(self):  # pragma: no cover
        return ReservationResourceSpecification.make_one(
            self.boto3_raw_data["ResourceSpecification"]
        )

    Start = field("Start")
    State = field("State")
    Tags = field("Tags")
    UsagePrice = field("UsagePrice")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReservationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReservationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOfferingResponse:
    boto3_raw_data: "type_defs.DescribeOfferingResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CurrencyCode = field("CurrencyCode")
    Duration = field("Duration")
    DurationUnits = field("DurationUnits")
    FixedPrice = field("FixedPrice")
    OfferingDescription = field("OfferingDescription")
    OfferingId = field("OfferingId")
    OfferingType = field("OfferingType")
    Region = field("Region")

    @cached_property
    def ResourceSpecification(self):  # pragma: no cover
        return ReservationResourceSpecification.make_one(
            self.boto3_raw_data["ResourceSpecification"]
        )

    UsagePrice = field("UsagePrice")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOfferingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOfferingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservationResponse:
    boto3_raw_data: "type_defs.DescribeReservationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Count = field("Count")
    CurrencyCode = field("CurrencyCode")
    Duration = field("Duration")
    DurationUnits = field("DurationUnits")
    End = field("End")
    FixedPrice = field("FixedPrice")
    Name = field("Name")
    OfferingDescription = field("OfferingDescription")
    OfferingId = field("OfferingId")
    OfferingType = field("OfferingType")
    Region = field("Region")

    @cached_property
    def RenewalSettings(self):  # pragma: no cover
        return RenewalSettings.make_one(self.boto3_raw_data["RenewalSettings"])

    ReservationId = field("ReservationId")

    @cached_property
    def ResourceSpecification(self):  # pragma: no cover
        return ReservationResourceSpecification.make_one(
            self.boto3_raw_data["ResourceSpecification"]
        )

    Start = field("Start")
    State = field("State")
    Tags = field("Tags")
    UsagePrice = field("UsagePrice")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReservationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Offering:
    boto3_raw_data: "type_defs.OfferingTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CurrencyCode = field("CurrencyCode")
    Duration = field("Duration")
    DurationUnits = field("DurationUnits")
    FixedPrice = field("FixedPrice")
    OfferingDescription = field("OfferingDescription")
    OfferingId = field("OfferingId")
    OfferingType = field("OfferingType")
    Region = field("Region")

    @cached_property
    def ResourceSpecification(self):  # pragma: no cover
        return ReservationResourceSpecification.make_one(
            self.boto3_raw_data["ResourceSpecification"]
        )

    UsagePrice = field("UsagePrice")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OfferingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OfferingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Reservation:
    boto3_raw_data: "type_defs.ReservationTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Count = field("Count")
    CurrencyCode = field("CurrencyCode")
    Duration = field("Duration")
    DurationUnits = field("DurationUnits")
    End = field("End")
    FixedPrice = field("FixedPrice")
    Name = field("Name")
    OfferingDescription = field("OfferingDescription")
    OfferingId = field("OfferingId")
    OfferingType = field("OfferingType")
    Region = field("Region")

    @cached_property
    def RenewalSettings(self):  # pragma: no cover
        return RenewalSettings.make_one(self.boto3_raw_data["RenewalSettings"])

    ReservationId = field("ReservationId")

    @cached_property
    def ResourceSpecification(self):  # pragma: no cover
        return ReservationResourceSpecification.make_one(
            self.boto3_raw_data["ResourceSpecification"]
        )

    Start = field("Start")
    State = field("State")
    Tags = field("Tags")
    UsagePrice = field("UsagePrice")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReservationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReservationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelPlacementGroupRequestWaitExtraExtra:
    boto3_raw_data: (
        "type_defs.DescribeChannelPlacementGroupRequestWaitExtraExtraTypeDef"
    ) = dataclasses.field()

    ChannelPlacementGroupId = field("ChannelPlacementGroupId")
    ClusterId = field("ClusterId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelPlacementGroupRequestWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeChannelPlacementGroupRequestWaitExtraExtraTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelPlacementGroupRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeChannelPlacementGroupRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ChannelPlacementGroupId = field("ChannelPlacementGroupId")
    ClusterId = field("ClusterId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelPlacementGroupRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelPlacementGroupRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelPlacementGroupRequestWait:
    boto3_raw_data: "type_defs.DescribeChannelPlacementGroupRequestWaitTypeDef" = (
        dataclasses.field()
    )

    ChannelPlacementGroupId = field("ChannelPlacementGroupId")
    ClusterId = field("ClusterId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelPlacementGroupRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelPlacementGroupRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelRequestWaitExtraExtraExtra:
    boto3_raw_data: "type_defs.DescribeChannelRequestWaitExtraExtraExtraTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelRequestWaitExtraExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelRequestWaitExtraExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelRequestWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeChannelRequestWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelRequestWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelRequestWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeChannelRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeChannelRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelRequestWait:
    boto3_raw_data: "type_defs.DescribeChannelRequestWaitTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeClusterRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterRequestWait:
    boto3_raw_data: "type_defs.DescribeClusterRequestWaitTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputRequestWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeInputRequestWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    InputId = field("InputId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInputRequestWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputRequestWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeInputRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    InputId = field("InputId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInputRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputRequestWait:
    boto3_raw_data: "type_defs.DescribeInputRequestWaitTypeDef" = dataclasses.field()

    InputId = field("InputId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInputRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiplexRequestWaitExtraExtraExtra:
    boto3_raw_data: "type_defs.DescribeMultiplexRequestWaitExtraExtraExtraTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMultiplexRequestWaitExtraExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiplexRequestWaitExtraExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiplexRequestWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeMultiplexRequestWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMultiplexRequestWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiplexRequestWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiplexRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeMultiplexRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMultiplexRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiplexRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiplexRequestWait:
    boto3_raw_data: "type_defs.DescribeMultiplexRequestWaitTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMultiplexRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiplexRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodeRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeNodeRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")
    NodeId = field("NodeId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNodeRequestWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodeRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodeRequestWait:
    boto3_raw_data: "type_defs.DescribeNodeRequestWaitTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    NodeId = field("NodeId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNodeRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodeRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalMapRequestWaitExtraExtraExtra:
    boto3_raw_data: "type_defs.GetSignalMapRequestWaitExtraExtraExtraTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSignalMapRequestWaitExtraExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalMapRequestWaitExtraExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalMapRequestWaitExtraExtra:
    boto3_raw_data: "type_defs.GetSignalMapRequestWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSignalMapRequestWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalMapRequestWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalMapRequestWaitExtra:
    boto3_raw_data: "type_defs.GetSignalMapRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSignalMapRequestWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalMapRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalMapRequestWait:
    boto3_raw_data: "type_defs.GetSignalMapRequestWaitTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSignalMapRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalMapRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelPlacementGroupsResponse:
    boto3_raw_data: "type_defs.ListChannelPlacementGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChannelPlacementGroups(self):  # pragma: no cover
        return DescribeChannelPlacementGroupSummary.make_many(
            self.boto3_raw_data["ChannelPlacementGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelPlacementGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelPlacementGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputSecurityGroupResponse:
    boto3_raw_data: "type_defs.DescribeInputSecurityGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Id = field("Id")
    Inputs = field("Inputs")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def WhitelistRules(self):  # pragma: no cover
        return InputWhitelistRule.make_many(self.boto3_raw_data["WhitelistRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInputSecurityGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputSecurityGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSecurityGroup:
    boto3_raw_data: "type_defs.InputSecurityGroupTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Inputs = field("Inputs")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def WhitelistRules(self):  # pragma: no cover
        return InputWhitelistRule.make_many(self.boto3_raw_data["WhitelistRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputSecurityGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSecurityGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduleRequestPaginate:
    boto3_raw_data: "type_defs.DescribeScheduleRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScheduleRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduleRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelPlacementGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListChannelPlacementGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelPlacementGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelPlacementGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequestPaginate:
    boto3_raw_data: "type_defs.ListChannelsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudWatchAlarmTemplateGroupsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCloudWatchAlarmTemplateGroupsRequestPaginateTypeDef"
    ) = dataclasses.field()

    Scope = field("Scope")
    SignalMapIdentifier = field("SignalMapIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudWatchAlarmTemplateGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListCloudWatchAlarmTemplateGroupsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudWatchAlarmTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListCloudWatchAlarmTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GroupIdentifier = field("GroupIdentifier")
    Scope = field("Scope")
    SignalMapIdentifier = field("SignalMapIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudWatchAlarmTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudWatchAlarmTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersRequestPaginate:
    boto3_raw_data: "type_defs.ListClustersRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventBridgeRuleTemplateGroupsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListEventBridgeRuleTemplateGroupsRequestPaginateTypeDef"
    ) = dataclasses.field()

    SignalMapIdentifier = field("SignalMapIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEventBridgeRuleTemplateGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListEventBridgeRuleTemplateGroupsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventBridgeRuleTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListEventBridgeRuleTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GroupIdentifier = field("GroupIdentifier")
    SignalMapIdentifier = field("SignalMapIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEventBridgeRuleTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventBridgeRuleTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputDeviceTransfersRequestPaginate:
    boto3_raw_data: "type_defs.ListInputDeviceTransfersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TransferType = field("TransferType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInputDeviceTransfersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputDeviceTransfersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputDevicesRequestPaginate:
    boto3_raw_data: "type_defs.ListInputDevicesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInputDevicesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputDevicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputSecurityGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListInputSecurityGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInputSecurityGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputSecurityGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputsRequestPaginate:
    boto3_raw_data: "type_defs.ListInputsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInputsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiplexProgramsRequestPaginate:
    boto3_raw_data: "type_defs.ListMultiplexProgramsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMultiplexProgramsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiplexProgramsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiplexesRequestPaginate:
    boto3_raw_data: "type_defs.ListMultiplexesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMultiplexesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiplexesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNetworksRequestPaginate:
    boto3_raw_data: "type_defs.ListNetworksRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNetworksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNetworksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesRequestPaginate:
    boto3_raw_data: "type_defs.ListNodesRequestPaginateTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNodesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOfferingsRequestPaginate:
    boto3_raw_data: "type_defs.ListOfferingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ChannelClass = field("ChannelClass")
    ChannelConfiguration = field("ChannelConfiguration")
    Codec = field("Codec")
    Duration = field("Duration")
    MaximumBitrate = field("MaximumBitrate")
    MaximumFramerate = field("MaximumFramerate")
    Resolution = field("Resolution")
    ResourceType = field("ResourceType")
    SpecialFeature = field("SpecialFeature")
    VideoQuality = field("VideoQuality")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOfferingsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOfferingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationsRequestPaginate:
    boto3_raw_data: "type_defs.ListReservationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ChannelClass = field("ChannelClass")
    Codec = field("Codec")
    MaximumBitrate = field("MaximumBitrate")
    MaximumFramerate = field("MaximumFramerate")
    Resolution = field("Resolution")
    ResourceType = field("ResourceType")
    SpecialFeature = field("SpecialFeature")
    VideoQuality = field("VideoQuality")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReservationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSdiSourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListSdiSourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSdiSourcesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSdiSourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalMapsRequestPaginate:
    boto3_raw_data: "type_defs.ListSignalMapsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CloudWatchAlarmTemplateGroupIdentifier = field(
        "CloudWatchAlarmTemplateGroupIdentifier"
    )
    EventBridgeRuleTemplateGroupIdentifier = field(
        "EventBridgeRuleTemplateGroupIdentifier"
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSignalMapsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalMapsRequestPaginateTypeDef"]
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

    AbsentInputAudioBehavior = field("AbsentInputAudioBehavior")
    Arib = field("Arib")
    AribCaptionsPid = field("AribCaptionsPid")
    AribCaptionsPidControl = field("AribCaptionsPidControl")
    AudioBufferModel = field("AudioBufferModel")
    AudioFramesPerPes = field("AudioFramesPerPes")
    AudioPids = field("AudioPids")
    AudioStreamType = field("AudioStreamType")
    Bitrate = field("Bitrate")
    BufferModel = field("BufferModel")
    CcDescriptor = field("CcDescriptor")

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
    Ebif = field("Ebif")
    EbpAudioInterval = field("EbpAudioInterval")
    EbpLookaheadMs = field("EbpLookaheadMs")
    EbpPlacement = field("EbpPlacement")
    EcmPid = field("EcmPid")
    EsRateInPes = field("EsRateInPes")
    EtvPlatformPid = field("EtvPlatformPid")
    EtvSignalPid = field("EtvSignalPid")
    FragmentTime = field("FragmentTime")
    Klv = field("Klv")
    KlvDataPids = field("KlvDataPids")
    NielsenId3Behavior = field("NielsenId3Behavior")
    NullPacketBitrate = field("NullPacketBitrate")
    PatInterval = field("PatInterval")
    PcrControl = field("PcrControl")
    PcrPeriod = field("PcrPeriod")
    PcrPid = field("PcrPid")
    PmtInterval = field("PmtInterval")
    PmtPid = field("PmtPid")
    ProgramNum = field("ProgramNum")
    RateMode = field("RateMode")
    Scte27Pids = field("Scte27Pids")
    Scte35Control = field("Scte35Control")
    Scte35Pid = field("Scte35Pid")
    SegmentationMarkers = field("SegmentationMarkers")
    SegmentationStyle = field("SegmentationStyle")
    SegmentationTime = field("SegmentationTime")
    TimedMetadataBehavior = field("TimedMetadataBehavior")
    TimedMetadataPid = field("TimedMetadataPid")
    TransportStreamId = field("TransportStreamId")
    VideoPid = field("VideoPid")
    Scte35PrerollPullupMilliseconds = field("Scte35PrerollPullupMilliseconds")

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
class OutputLockingSettingsOutput:
    boto3_raw_data: "type_defs.OutputLockingSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def EpochLockingSettings(self):  # pragma: no cover
        return EpochLockingSettings.make_one(
            self.boto3_raw_data["EpochLockingSettings"]
        )

    PipelineLockingSettings = field("PipelineLockingSettings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputLockingSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputLockingSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputLockingSettings:
    boto3_raw_data: "type_defs.OutputLockingSettingsTypeDef" = dataclasses.field()

    @cached_property
    def EpochLockingSettings(self):  # pragma: no cover
        return EpochLockingSettings.make_one(
            self.boto3_raw_data["EpochLockingSettings"]
        )

    PipelineLockingSettings = field("PipelineLockingSettings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputLockingSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputLockingSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventBridgeRuleTemplateGroupsResponse:
    boto3_raw_data: "type_defs.ListEventBridgeRuleTemplateGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventBridgeRuleTemplateGroups(self):  # pragma: no cover
        return EventBridgeRuleTemplateGroupSummary.make_many(
            self.boto3_raw_data["EventBridgeRuleTemplateGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEventBridgeRuleTemplateGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventBridgeRuleTemplateGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventBridgeRuleTemplatesResponse:
    boto3_raw_data: "type_defs.ListEventBridgeRuleTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventBridgeRuleTemplates(self):  # pragma: no cover
        return EventBridgeRuleTemplateSummary.make_many(
            self.boto3_raw_data["EventBridgeRuleTemplates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEventBridgeRuleTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventBridgeRuleTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverConditionSettings:
    boto3_raw_data: "type_defs.FailoverConditionSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AudioSilenceSettings(self):  # pragma: no cover
        return AudioSilenceFailoverSettings.make_one(
            self.boto3_raw_data["AudioSilenceSettings"]
        )

    @cached_property
    def InputLossSettings(self):  # pragma: no cover
        return InputLossFailoverSettings.make_one(
            self.boto3_raw_data["InputLossSettings"]
        )

    @cached_property
    def VideoBlackSettings(self):  # pragma: no cover
        return VideoBlackFailoverSettings.make_one(
            self.boto3_raw_data["VideoBlackSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverConditionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverConditionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleActionStartSettingsOutput:
    boto3_raw_data: "type_defs.ScheduleActionStartSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FixedModeScheduleActionStartSettings(self):  # pragma: no cover
        return FixedModeScheduleActionStartSettings.make_one(
            self.boto3_raw_data["FixedModeScheduleActionStartSettings"]
        )

    @cached_property
    def FollowModeScheduleActionStartSettings(self):  # pragma: no cover
        return FollowModeScheduleActionStartSettings.make_one(
            self.boto3_raw_data["FollowModeScheduleActionStartSettings"]
        )

    ImmediateModeScheduleActionStartSettings = field(
        "ImmediateModeScheduleActionStartSettings"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScheduleActionStartSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleActionStartSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleActionStartSettings:
    boto3_raw_data: "type_defs.ScheduleActionStartSettingsTypeDef" = dataclasses.field()

    @cached_property
    def FixedModeScheduleActionStartSettings(self):  # pragma: no cover
        return FixedModeScheduleActionStartSettings.make_one(
            self.boto3_raw_data["FixedModeScheduleActionStartSettings"]
        )

    @cached_property
    def FollowModeScheduleActionStartSettings(self):  # pragma: no cover
        return FollowModeScheduleActionStartSettings.make_one(
            self.boto3_raw_data["FollowModeScheduleActionStartSettings"]
        )

    ImmediateModeScheduleActionStartSettings = field(
        "ImmediateModeScheduleActionStartSettings"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleActionStartSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleActionStartSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameCaptureCdnSettings:
    boto3_raw_data: "type_defs.FrameCaptureCdnSettingsTypeDef" = dataclasses.field()

    @cached_property
    def FrameCaptureS3Settings(self):  # pragma: no cover
        return FrameCaptureS3Settings.make_one(
            self.boto3_raw_data["FrameCaptureS3Settings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrameCaptureCdnSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameCaptureCdnSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H264FilterSettings:
    boto3_raw_data: "type_defs.H264FilterSettingsTypeDef" = dataclasses.field()

    @cached_property
    def TemporalFilterSettings(self):  # pragma: no cover
        return TemporalFilterSettings.make_one(
            self.boto3_raw_data["TemporalFilterSettings"]
        )

    @cached_property
    def BandwidthReductionFilterSettings(self):  # pragma: no cover
        return BandwidthReductionFilterSettings.make_one(
            self.boto3_raw_data["BandwidthReductionFilterSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.H264FilterSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H264FilterSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class H265FilterSettings:
    boto3_raw_data: "type_defs.H265FilterSettingsTypeDef" = dataclasses.field()

    @cached_property
    def TemporalFilterSettings(self):  # pragma: no cover
        return TemporalFilterSettings.make_one(
            self.boto3_raw_data["TemporalFilterSettings"]
        )

    @cached_property
    def BandwidthReductionFilterSettings(self):  # pragma: no cover
        return BandwidthReductionFilterSettings.make_one(
            self.boto3_raw_data["BandwidthReductionFilterSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.H265FilterSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.H265FilterSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mpeg2FilterSettings:
    boto3_raw_data: "type_defs.Mpeg2FilterSettingsTypeDef" = dataclasses.field()

    @cached_property
    def TemporalFilterSettings(self):  # pragma: no cover
        return TemporalFilterSettings.make_one(
            self.boto3_raw_data["TemporalFilterSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Mpeg2FilterSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Mpeg2FilterSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsCdnSettings:
    boto3_raw_data: "type_defs.HlsCdnSettingsTypeDef" = dataclasses.field()

    @cached_property
    def HlsAkamaiSettings(self):  # pragma: no cover
        return HlsAkamaiSettings.make_one(self.boto3_raw_data["HlsAkamaiSettings"])

    @cached_property
    def HlsBasicPutSettings(self):  # pragma: no cover
        return HlsBasicPutSettings.make_one(self.boto3_raw_data["HlsBasicPutSettings"])

    @cached_property
    def HlsMediaStoreSettings(self):  # pragma: no cover
        return HlsMediaStoreSettings.make_one(
            self.boto3_raw_data["HlsMediaStoreSettings"]
        )

    @cached_property
    def HlsS3Settings(self):  # pragma: no cover
        return HlsS3Settings.make_one(self.boto3_raw_data["HlsS3Settings"])

    @cached_property
    def HlsWebdavSettings(self):  # pragma: no cover
        return HlsWebdavSettings.make_one(self.boto3_raw_data["HlsWebdavSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsCdnSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HlsCdnSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputClippingSettings:
    boto3_raw_data: "type_defs.InputClippingSettingsTypeDef" = dataclasses.field()

    InputTimecodeSource = field("InputTimecodeSource")

    @cached_property
    def StartTimecode(self):  # pragma: no cover
        return StartTimecode.make_one(self.boto3_raw_data["StartTimecode"])

    @cached_property
    def StopTimecode(self):  # pragma: no cover
        return StopTimecode.make_one(self.boto3_raw_data["StopTimecode"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputClippingSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputClippingSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDestinationRequest:
    boto3_raw_data: "type_defs.InputDestinationRequestTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    Network = field("Network")

    @cached_property
    def NetworkRoutes(self):  # pragma: no cover
        return InputRequestDestinationRoute.make_many(
            self.boto3_raw_data["NetworkRoutes"]
        )

    StaticIpAddress = field("StaticIpAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDestination:
    boto3_raw_data: "type_defs.InputDestinationTypeDef" = dataclasses.field()

    Ip = field("Ip")
    Port = field("Port")
    Url = field("Url")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return InputDestinationVpc.make_one(self.boto3_raw_data["Vpc"])

    Network = field("Network")

    @cached_property
    def NetworkRoutes(self):  # pragma: no cover
        return InputDestinationRoute.make_many(self.boto3_raw_data["NetworkRoutes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceConfigurableSettings:
    boto3_raw_data: "type_defs.InputDeviceConfigurableSettingsTypeDef" = (
        dataclasses.field()
    )

    ConfiguredInput = field("ConfiguredInput")
    MaxBitrate = field("MaxBitrate")
    LatencyMs = field("LatencyMs")
    Codec = field("Codec")

    @cached_property
    def MediaconnectSettings(self):  # pragma: no cover
        return InputDeviceMediaConnectConfigurableSettings.make_one(
            self.boto3_raw_data["MediaconnectSettings"]
        )

    @cached_property
    def AudioChannelPairs(self):  # pragma: no cover
        return InputDeviceConfigurableAudioChannelPairConfig.make_many(
            self.boto3_raw_data["AudioChannelPairs"]
        )

    InputResolution = field("InputResolution")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InputDeviceConfigurableSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceConfigurableSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceUhdSettings:
    boto3_raw_data: "type_defs.InputDeviceUhdSettingsTypeDef" = dataclasses.field()

    ActiveInput = field("ActiveInput")
    ConfiguredInput = field("ConfiguredInput")
    DeviceState = field("DeviceState")
    Framerate = field("Framerate")
    Height = field("Height")
    MaxBitrate = field("MaxBitrate")
    ScanType = field("ScanType")
    Width = field("Width")
    LatencyMs = field("LatencyMs")
    Codec = field("Codec")

    @cached_property
    def MediaconnectSettings(self):  # pragma: no cover
        return InputDeviceMediaConnectSettings.make_one(
            self.boto3_raw_data["MediaconnectSettings"]
        )

    @cached_property
    def AudioChannelPairs(self):  # pragma: no cover
        return InputDeviceUhdAudioChannelPairConfig.make_many(
            self.boto3_raw_data["AudioChannelPairs"]
        )

    InputResolution = field("InputResolution")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDeviceUhdSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceUhdSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Smpte2110ReceiverGroupSdpSettingsOutput:
    boto3_raw_data: "type_defs.Smpte2110ReceiverGroupSdpSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AncillarySdps(self):  # pragma: no cover
        return InputSdpLocation.make_many(self.boto3_raw_data["AncillarySdps"])

    @cached_property
    def AudioSdps(self):  # pragma: no cover
        return InputSdpLocation.make_many(self.boto3_raw_data["AudioSdps"])

    @cached_property
    def VideoSdp(self):  # pragma: no cover
        return InputSdpLocation.make_one(self.boto3_raw_data["VideoSdp"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Smpte2110ReceiverGroupSdpSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Smpte2110ReceiverGroupSdpSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Smpte2110ReceiverGroupSdpSettings:
    boto3_raw_data: "type_defs.Smpte2110ReceiverGroupSdpSettingsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AncillarySdps(self):  # pragma: no cover
        return InputSdpLocation.make_many(self.boto3_raw_data["AncillarySdps"])

    @cached_property
    def AudioSdps(self):  # pragma: no cover
        return InputSdpLocation.make_many(self.boto3_raw_data["AudioSdps"])

    @cached_property
    def VideoSdp(self):  # pragma: no cover
        return InputSdpLocation.make_one(self.boto3_raw_data["VideoSdp"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Smpte2110ReceiverGroupSdpSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Smpte2110ReceiverGroupSdpSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputDeviceTransfersResponse:
    boto3_raw_data: "type_defs.ListInputDeviceTransfersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputDeviceTransfers(self):  # pragma: no cover
        return TransferringInputDeviceSummary.make_many(
            self.boto3_raw_data["InputDeviceTransfers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInputDeviceTransfersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputDeviceTransfersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiplexProgramsResponse:
    boto3_raw_data: "type_defs.ListMultiplexProgramsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MultiplexPrograms(self):  # pragma: no cover
        return MultiplexProgramSummary.make_many(
            self.boto3_raw_data["MultiplexPrograms"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMultiplexProgramsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiplexProgramsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSdiSourcesResponse:
    boto3_raw_data: "type_defs.ListSdiSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def SdiSources(self):  # pragma: no cover
        return SdiSourceSummary.make_many(self.boto3_raw_data["SdiSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSdiSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSdiSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalMapsResponse:
    boto3_raw_data: "type_defs.ListSignalMapsResponseTypeDef" = dataclasses.field()

    @cached_property
    def SignalMaps(self):  # pragma: no cover
        return SignalMapSummary.make_many(self.boto3_raw_data["SignalMaps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSignalMapsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalMapsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StandardHlsSettings:
    boto3_raw_data: "type_defs.StandardHlsSettingsTypeDef" = dataclasses.field()

    @cached_property
    def M3u8Settings(self):  # pragma: no cover
        return M3u8Settings.make_one(self.boto3_raw_data["M3u8Settings"])

    AudioRenditionSets = field("AudioRenditionSets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StandardHlsSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StandardHlsSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPackageOutputSettings:
    boto3_raw_data: "type_defs.MediaPackageOutputSettingsTypeDef" = dataclasses.field()

    @cached_property
    def MediaPackageV2DestinationSettings(self):  # pragma: no cover
        return MediaPackageV2DestinationSettings.make_one(
            self.boto3_raw_data["MediaPackageV2DestinationSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaPackageOutputSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaPackageOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaResource:
    boto3_raw_data: "type_defs.MediaResourceTypeDef" = dataclasses.field()

    @cached_property
    def Destinations(self):  # pragma: no cover
        return MediaResourceNeighbor.make_many(self.boto3_raw_data["Destinations"])

    Name = field("Name")

    @cached_property
    def Sources(self):  # pragma: no cover
        return MediaResourceNeighbor.make_many(self.boto3_raw_data["Sources"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MediaResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MotionGraphicsConfigurationOutput:
    boto3_raw_data: "type_defs.MotionGraphicsConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MotionGraphicsSettings(self):  # pragma: no cover
        return MotionGraphicsSettingsOutput.make_one(
            self.boto3_raw_data["MotionGraphicsSettings"]
        )

    MotionGraphicsInsertion = field("MotionGraphicsInsertion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MotionGraphicsConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MotionGraphicsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MotionGraphicsConfiguration:
    boto3_raw_data: "type_defs.MotionGraphicsConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def MotionGraphicsSettings(self):  # pragma: no cover
        return MotionGraphicsSettings.make_one(
            self.boto3_raw_data["MotionGraphicsSettings"]
        )

    MotionGraphicsInsertion = field("MotionGraphicsInsertion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MotionGraphicsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MotionGraphicsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInputSettings:
    boto3_raw_data: "type_defs.NetworkInputSettingsTypeDef" = dataclasses.field()

    @cached_property
    def HlsInputSettings(self):  # pragma: no cover
        return HlsInputSettings.make_one(self.boto3_raw_data["HlsInputSettings"])

    ServerValidation = field("ServerValidation")

    @cached_property
    def MulticastInputSettings(self):  # pragma: no cover
        return MulticastInputSettings.make_one(
            self.boto3_raw_data["MulticastInputSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkInputSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastSettingsCreateRequest:
    boto3_raw_data: "type_defs.MulticastSettingsCreateRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sources(self):  # pragma: no cover
        return MulticastSourceCreateRequest.make_many(self.boto3_raw_data["Sources"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MulticastSettingsCreateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MulticastSettingsCreateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastSettings:
    boto3_raw_data: "type_defs.MulticastSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Sources(self):  # pragma: no cover
        return MulticastSource.make_many(self.boto3_raw_data["Sources"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MulticastSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MulticastSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastSettingsUpdateRequest:
    boto3_raw_data: "type_defs.MulticastSettingsUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sources(self):  # pragma: no cover
        return MulticastSourceUpdateRequest.make_many(self.boto3_raw_data["Sources"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MulticastSettingsUpdateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MulticastSettingsUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexContainerSettings:
    boto3_raw_data: "type_defs.MultiplexContainerSettingsTypeDef" = dataclasses.field()

    @cached_property
    def MultiplexM2tsSettings(self):  # pragma: no cover
        return MultiplexM2tsSettings.make_one(
            self.boto3_raw_data["MultiplexM2tsSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiplexContainerSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexContainerSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexOutputDestination:
    boto3_raw_data: "type_defs.MultiplexOutputDestinationTypeDef" = dataclasses.field()

    @cached_property
    def MediaConnectSettings(self):  # pragma: no cover
        return MultiplexMediaConnectOutputDestinationSettings.make_one(
            self.boto3_raw_data["MediaConnectSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiplexOutputDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexOutputDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexSummary:
    boto3_raw_data: "type_defs.MultiplexSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AvailabilityZones = field("AvailabilityZones")
    Id = field("Id")

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexSettingsSummary.make_one(
            self.boto3_raw_data["MultiplexSettings"]
        )

    Name = field("Name")
    PipelinesRunningCount = field("PipelinesRunningCount")
    ProgramCount = field("ProgramCount")
    State = field("State")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MultiplexSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexVideoSettings:
    boto3_raw_data: "type_defs.MultiplexVideoSettingsTypeDef" = dataclasses.field()

    ConstantBitrate = field("ConstantBitrate")

    @cached_property
    def StatmuxSettings(self):  # pragma: no cover
        return MultiplexStatmuxVideoSettings.make_one(
            self.boto3_raw_data["StatmuxSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiplexVideoSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexVideoSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NielsenWatermarksSettings:
    boto3_raw_data: "type_defs.NielsenWatermarksSettingsTypeDef" = dataclasses.field()

    @cached_property
    def NielsenCbetSettings(self):  # pragma: no cover
        return NielsenCBET.make_one(self.boto3_raw_data["NielsenCbetSettings"])

    NielsenDistributionType = field("NielsenDistributionType")

    @cached_property
    def NielsenNaesIiNwSettings(self):  # pragma: no cover
        return NielsenNaesIiNw.make_one(self.boto3_raw_data["NielsenNaesIiNwSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NielsenWatermarksSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NielsenWatermarksSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDestinationOutput:
    boto3_raw_data: "type_defs.OutputDestinationOutputTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def MediaPackageSettings(self):  # pragma: no cover
        return MediaPackageOutputDestinationSettings.make_many(
            self.boto3_raw_data["MediaPackageSettings"]
        )

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexProgramChannelDestinationSettings.make_one(
            self.boto3_raw_data["MultiplexSettings"]
        )

    @cached_property
    def Settings(self):  # pragma: no cover
        return OutputDestinationSettings.make_many(self.boto3_raw_data["Settings"])

    @cached_property
    def SrtSettings(self):  # pragma: no cover
        return SrtOutputDestinationSettings.make_many(
            self.boto3_raw_data["SrtSettings"]
        )

    LogicalInterfaceNames = field("LogicalInterfaceNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputDestinationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputDestinationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDestination:
    boto3_raw_data: "type_defs.OutputDestinationTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def MediaPackageSettings(self):  # pragma: no cover
        return MediaPackageOutputDestinationSettings.make_many(
            self.boto3_raw_data["MediaPackageSettings"]
        )

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexProgramChannelDestinationSettings.make_one(
            self.boto3_raw_data["MultiplexSettings"]
        )

    @cached_property
    def Settings(self):  # pragma: no cover
        return OutputDestinationSettings.make_many(self.boto3_raw_data["Settings"])

    @cached_property
    def SrtSettings(self):  # pragma: no cover
        return SrtOutputDestinationSettings.make_many(
            self.boto3_raw_data["SrtSettings"]
        )

    LogicalInterfaceNames = field("LogicalInterfaceNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseStateScheduleActionSettingsOutput:
    boto3_raw_data: "type_defs.PauseStateScheduleActionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Pipelines(self):  # pragma: no cover
        return PipelinePauseStateSettings.make_many(self.boto3_raw_data["Pipelines"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PauseStateScheduleActionSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseStateScheduleActionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseStateScheduleActionSettings:
    boto3_raw_data: "type_defs.PauseStateScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Pipelines(self):  # pragma: no cover
        return PipelinePauseStateSettings.make_many(self.boto3_raw_data["Pipelines"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PauseStateScheduleActionSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseStateScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNetworkRequest:
    boto3_raw_data: "type_defs.UpdateNetworkRequestTypeDef" = dataclasses.field()

    NetworkId = field("NetworkId")

    @cached_property
    def IpPools(self):  # pragma: no cover
        return IpPoolUpdateRequest.make_many(self.boto3_raw_data["IpPools"])

    Name = field("Name")

    @cached_property
    def Routes(self):  # pragma: no cover
        return RouteUpdateRequest.make_many(self.boto3_raw_data["Routes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35SegmentationDescriptor:
    boto3_raw_data: "type_defs.Scte35SegmentationDescriptorTypeDef" = (
        dataclasses.field()
    )

    SegmentationCancelIndicator = field("SegmentationCancelIndicator")
    SegmentationEventId = field("SegmentationEventId")

    @cached_property
    def DeliveryRestrictions(self):  # pragma: no cover
        return Scte35DeliveryRestrictions.make_one(
            self.boto3_raw_data["DeliveryRestrictions"]
        )

    SegmentNum = field("SegmentNum")
    SegmentationDuration = field("SegmentationDuration")
    SegmentationTypeId = field("SegmentationTypeId")
    SegmentationUpid = field("SegmentationUpid")
    SegmentationUpidType = field("SegmentationUpidType")
    SegmentsExpected = field("SegmentsExpected")
    SubSegmentNum = field("SubSegmentNum")
    SubSegmentsExpected = field("SubSegmentsExpected")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Scte35SegmentationDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35SegmentationDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNodeRequest:
    boto3_raw_data: "type_defs.UpdateNodeRequestTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    NodeId = field("NodeId")
    Name = field("Name")
    Role = field("Role")

    @cached_property
    def SdiSourceMappings(self):  # pragma: no cover
        return SdiSourceMappingUpdateRequest.make_many(
            self.boto3_raw_data["SdiSourceMappings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateNodeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtCallerSourceRequest:
    boto3_raw_data: "type_defs.SrtCallerSourceRequestTypeDef" = dataclasses.field()

    @cached_property
    def Decryption(self):  # pragma: no cover
        return SrtCallerDecryptionRequest.make_one(self.boto3_raw_data["Decryption"])

    MinimumLatency = field("MinimumLatency")
    SrtListenerAddress = field("SrtListenerAddress")
    SrtListenerPort = field("SrtListenerPort")
    StreamId = field("StreamId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SrtCallerSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SrtCallerSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtCallerSource:
    boto3_raw_data: "type_defs.SrtCallerSourceTypeDef" = dataclasses.field()

    @cached_property
    def Decryption(self):  # pragma: no cover
        return SrtCallerDecryption.make_one(self.boto3_raw_data["Decryption"])

    MinimumLatency = field("MinimumLatency")
    SrtListenerAddress = field("SrtListenerAddress")
    SrtListenerPort = field("SrtListenerPort")
    StreamId = field("StreamId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SrtCallerSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SrtCallerSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThumbnailDetail:
    boto3_raw_data: "type_defs.ThumbnailDetailTypeDef" = dataclasses.field()

    PipelineId = field("PipelineId")

    @cached_property
    def Thumbnails(self):  # pragma: no cover
        return Thumbnail.make_many(self.boto3_raw_data["Thumbnails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThumbnailDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThumbnailDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoSelectorSettings:
    boto3_raw_data: "type_defs.VideoSelectorSettingsTypeDef" = dataclasses.field()

    @cached_property
    def VideoSelectorPid(self):  # pragma: no cover
        return VideoSelectorPid.make_one(self.boto3_raw_data["VideoSelectorPid"])

    @cached_property
    def VideoSelectorProgramId(self):  # pragma: no cover
        return VideoSelectorProgramId.make_one(
            self.boto3_raw_data["VideoSelectorProgramId"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoSelectorSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoSelectorSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafIngestGroupSettingsOutput:
    boto3_raw_data: "type_defs.CmafIngestGroupSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    NielsenId3Behavior = field("NielsenId3Behavior")
    Scte35Type = field("Scte35Type")
    SegmentLength = field("SegmentLength")
    SegmentLengthUnits = field("SegmentLengthUnits")
    SendDelayMs = field("SendDelayMs")
    KlvBehavior = field("KlvBehavior")
    KlvNameModifier = field("KlvNameModifier")
    NielsenId3NameModifier = field("NielsenId3NameModifier")
    Scte35NameModifier = field("Scte35NameModifier")
    Id3Behavior = field("Id3Behavior")
    Id3NameModifier = field("Id3NameModifier")

    @cached_property
    def CaptionLanguageMappings(self):  # pragma: no cover
        return CmafIngestCaptionLanguageMapping.make_many(
            self.boto3_raw_data["CaptionLanguageMappings"]
        )

    TimedMetadataId3Frame = field("TimedMetadataId3Frame")
    TimedMetadataId3Period = field("TimedMetadataId3Period")
    TimedMetadataPassthrough = field("TimedMetadataPassthrough")

    @cached_property
    def AdditionalDestinations(self):  # pragma: no cover
        return AdditionalDestinations.make_many(
            self.boto3_raw_data["AdditionalDestinations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CmafIngestGroupSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafIngestGroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafIngestGroupSettings:
    boto3_raw_data: "type_defs.CmafIngestGroupSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    NielsenId3Behavior = field("NielsenId3Behavior")
    Scte35Type = field("Scte35Type")
    SegmentLength = field("SegmentLength")
    SegmentLengthUnits = field("SegmentLengthUnits")
    SendDelayMs = field("SendDelayMs")
    KlvBehavior = field("KlvBehavior")
    KlvNameModifier = field("KlvNameModifier")
    NielsenId3NameModifier = field("NielsenId3NameModifier")
    Scte35NameModifier = field("Scte35NameModifier")
    Id3Behavior = field("Id3Behavior")
    Id3NameModifier = field("Id3NameModifier")

    @cached_property
    def CaptionLanguageMappings(self):  # pragma: no cover
        return CmafIngestCaptionLanguageMapping.make_many(
            self.boto3_raw_data["CaptionLanguageMappings"]
        )

    TimedMetadataId3Frame = field("TimedMetadataId3Frame")
    TimedMetadataId3Period = field("TimedMetadataId3Period")
    TimedMetadataPassthrough = field("TimedMetadataPassthrough")

    @cached_property
    def AdditionalDestinations(self):  # pragma: no cover
        return AdditionalDestinations.make_many(
            self.boto3_raw_data["AdditionalDestinations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CmafIngestGroupSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafIngestGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveGroupSettings:
    boto3_raw_data: "type_defs.ArchiveGroupSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def ArchiveCdnSettings(self):  # pragma: no cover
        return ArchiveCdnSettings.make_one(self.boto3_raw_data["ArchiveCdnSettings"])

    RolloverInterval = field("RolloverInterval")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveGroupSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveGroupSettingsTypeDef"]
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

    @cached_property
    def ChannelMappings(self):  # pragma: no cover
        return AudioChannelMappingOutput.make_many(
            self.boto3_raw_data["ChannelMappings"]
        )

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

    @cached_property
    def ChannelMappings(self):  # pragma: no cover
        return AudioChannelMapping.make_many(self.boto3_raw_data["ChannelMappings"])

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
class CaptionDestinationSettingsOutput:
    boto3_raw_data: "type_defs.CaptionDestinationSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    AribDestinationSettings = field("AribDestinationSettings")

    @cached_property
    def BurnInDestinationSettings(self):  # pragma: no cover
        return BurnInDestinationSettings.make_one(
            self.boto3_raw_data["BurnInDestinationSettings"]
        )

    @cached_property
    def DvbSubDestinationSettings(self):  # pragma: no cover
        return DvbSubDestinationSettings.make_one(
            self.boto3_raw_data["DvbSubDestinationSettings"]
        )

    @cached_property
    def EbuTtDDestinationSettings(self):  # pragma: no cover
        return EbuTtDDestinationSettings.make_one(
            self.boto3_raw_data["EbuTtDDestinationSettings"]
        )

    EmbeddedDestinationSettings = field("EmbeddedDestinationSettings")
    EmbeddedPlusScte20DestinationSettings = field(
        "EmbeddedPlusScte20DestinationSettings"
    )
    RtmpCaptionInfoDestinationSettings = field("RtmpCaptionInfoDestinationSettings")
    Scte20PlusEmbeddedDestinationSettings = field(
        "Scte20PlusEmbeddedDestinationSettings"
    )
    Scte27DestinationSettings = field("Scte27DestinationSettings")
    SmpteTtDestinationSettings = field("SmpteTtDestinationSettings")
    TeletextDestinationSettings = field("TeletextDestinationSettings")

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

    AribDestinationSettings = field("AribDestinationSettings")

    @cached_property
    def BurnInDestinationSettings(self):  # pragma: no cover
        return BurnInDestinationSettings.make_one(
            self.boto3_raw_data["BurnInDestinationSettings"]
        )

    @cached_property
    def DvbSubDestinationSettings(self):  # pragma: no cover
        return DvbSubDestinationSettings.make_one(
            self.boto3_raw_data["DvbSubDestinationSettings"]
        )

    @cached_property
    def EbuTtDDestinationSettings(self):  # pragma: no cover
        return EbuTtDDestinationSettings.make_one(
            self.boto3_raw_data["EbuTtDDestinationSettings"]
        )

    EmbeddedDestinationSettings = field("EmbeddedDestinationSettings")
    EmbeddedPlusScte20DestinationSettings = field(
        "EmbeddedPlusScte20DestinationSettings"
    )
    RtmpCaptionInfoDestinationSettings = field("RtmpCaptionInfoDestinationSettings")
    Scte20PlusEmbeddedDestinationSettings = field(
        "Scte20PlusEmbeddedDestinationSettings"
    )
    Scte27DestinationSettings = field("Scte27DestinationSettings")
    SmpteTtDestinationSettings = field("SmpteTtDestinationSettings")
    TeletextDestinationSettings = field("TeletextDestinationSettings")

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
class KeyProviderSettings:
    boto3_raw_data: "type_defs.KeyProviderSettingsTypeDef" = dataclasses.field()

    @cached_property
    def StaticKeySettings(self):  # pragma: no cover
        return StaticKeySettings.make_one(self.boto3_raw_data["StaticKeySettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyProviderSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioSelectorSettingsOutput:
    boto3_raw_data: "type_defs.AudioSelectorSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AudioHlsRenditionSelection(self):  # pragma: no cover
        return AudioHlsRenditionSelection.make_one(
            self.boto3_raw_data["AudioHlsRenditionSelection"]
        )

    @cached_property
    def AudioLanguageSelection(self):  # pragma: no cover
        return AudioLanguageSelection.make_one(
            self.boto3_raw_data["AudioLanguageSelection"]
        )

    @cached_property
    def AudioPidSelection(self):  # pragma: no cover
        return AudioPidSelection.make_one(self.boto3_raw_data["AudioPidSelection"])

    @cached_property
    def AudioTrackSelection(self):  # pragma: no cover
        return AudioTrackSelectionOutput.make_one(
            self.boto3_raw_data["AudioTrackSelection"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioSelectorSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioSelectorSettingsOutputTypeDef"]
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

    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    AfdSignaling = field("AfdSignaling")
    BufSize = field("BufSize")

    @cached_property
    def ColorSpaceSettings(self):  # pragma: no cover
        return Av1ColorSpaceSettingsOutput.make_one(
            self.boto3_raw_data["ColorSpaceSettings"]
        )

    FixedAfd = field("FixedAfd")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    Level = field("Level")
    LookAheadRateControl = field("LookAheadRateControl")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    QvbrQualityLevel = field("QvbrQualityLevel")
    SceneChangeDetect = field("SceneChangeDetect")

    @cached_property
    def TimecodeBurninSettings(self):  # pragma: no cover
        return TimecodeBurninSettings.make_one(
            self.boto3_raw_data["TimecodeBurninSettings"]
        )

    Bitrate = field("Bitrate")
    RateControlMode = field("RateControlMode")
    MinBitrate = field("MinBitrate")

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

    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    AfdSignaling = field("AfdSignaling")
    BufSize = field("BufSize")

    @cached_property
    def ColorSpaceSettings(self):  # pragma: no cover
        return Av1ColorSpaceSettings.make_one(self.boto3_raw_data["ColorSpaceSettings"])

    FixedAfd = field("FixedAfd")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    Level = field("Level")
    LookAheadRateControl = field("LookAheadRateControl")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    QvbrQualityLevel = field("QvbrQualityLevel")
    SceneChangeDetect = field("SceneChangeDetect")

    @cached_property
    def TimecodeBurninSettings(self):  # pragma: no cover
        return TimecodeBurninSettings.make_one(
            self.boto3_raw_data["TimecodeBurninSettings"]
        )

    Bitrate = field("Bitrate")
    RateControlMode = field("RateControlMode")
    MinBitrate = field("MinBitrate")

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
class AvailConfiguration:
    boto3_raw_data: "type_defs.AvailConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def AvailSettings(self):  # pragma: no cover
        return AvailSettings.make_one(self.boto3_raw_data["AvailSettings"])

    Scte35SegmentationScope = field("Scte35SegmentationScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPackageGroupSettingsOutput:
    boto3_raw_data: "type_defs.MediaPackageGroupSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def MediapackageV2GroupSettings(self):  # pragma: no cover
        return MediaPackageV2GroupSettingsOutput.make_one(
            self.boto3_raw_data["MediapackageV2GroupSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MediaPackageGroupSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaPackageGroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPackageGroupSettings:
    boto3_raw_data: "type_defs.MediaPackageGroupSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def MediapackageV2GroupSettings(self):  # pragma: no cover
        return MediaPackageV2GroupSettings.make_one(
            self.boto3_raw_data["MediapackageV2GroupSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaPackageGroupSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaPackageGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionSelectorSettingsOutput:
    boto3_raw_data: "type_defs.CaptionSelectorSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AncillarySourceSettings(self):  # pragma: no cover
        return AncillarySourceSettings.make_one(
            self.boto3_raw_data["AncillarySourceSettings"]
        )

    AribSourceSettings = field("AribSourceSettings")

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
    def Scte20SourceSettings(self):  # pragma: no cover
        return Scte20SourceSettings.make_one(
            self.boto3_raw_data["Scte20SourceSettings"]
        )

    @cached_property
    def Scte27SourceSettings(self):  # pragma: no cover
        return Scte27SourceSettings.make_one(
            self.boto3_raw_data["Scte27SourceSettings"]
        )

    @cached_property
    def TeletextSourceSettings(self):  # pragma: no cover
        return TeletextSourceSettings.make_one(
            self.boto3_raw_data["TeletextSourceSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CaptionSelectorSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionSelectorSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionSelectorSettings:
    boto3_raw_data: "type_defs.CaptionSelectorSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AncillarySourceSettings(self):  # pragma: no cover
        return AncillarySourceSettings.make_one(
            self.boto3_raw_data["AncillarySourceSettings"]
        )

    AribSourceSettings = field("AribSourceSettings")

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
    def Scte20SourceSettings(self):  # pragma: no cover
        return Scte20SourceSettings.make_one(
            self.boto3_raw_data["Scte20SourceSettings"]
        )

    @cached_property
    def Scte27SourceSettings(self):  # pragma: no cover
        return Scte27SourceSettings.make_one(
            self.boto3_raw_data["Scte27SourceSettings"]
        )

    @cached_property
    def TeletextSourceSettings(self):  # pragma: no cover
        return TeletextSourceSettings.make_one(
            self.boto3_raw_data["TeletextSourceSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptionSelectorSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionSelectorSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterRequest:
    boto3_raw_data: "type_defs.CreateClusterRequestTypeDef" = dataclasses.field()

    ClusterType = field("ClusterType")
    InstanceRoleArn = field("InstanceRoleArn")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return ClusterNetworkSettingsCreateRequest.make_one(
            self.boto3_raw_data["NetworkSettings"]
        )

    RequestId = field("RequestId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterResponse:
    boto3_raw_data: "type_defs.CreateClusterResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelIds = field("ChannelIds")
    ClusterType = field("ClusterType")
    Id = field("Id")
    InstanceRoleArn = field("InstanceRoleArn")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return ClusterNetworkSettings.make_one(self.boto3_raw_data["NetworkSettings"])

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterResponse:
    boto3_raw_data: "type_defs.DeleteClusterResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelIds = field("ChannelIds")
    ClusterType = field("ClusterType")
    Id = field("Id")
    InstanceRoleArn = field("InstanceRoleArn")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return ClusterNetworkSettings.make_one(self.boto3_raw_data["NetworkSettings"])

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterResponse:
    boto3_raw_data: "type_defs.DescribeClusterResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelIds = field("ChannelIds")
    ClusterType = field("ClusterType")
    Id = field("Id")
    InstanceRoleArn = field("InstanceRoleArn")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return ClusterNetworkSettings.make_one(self.boto3_raw_data["NetworkSettings"])

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterSummary:
    boto3_raw_data: "type_defs.DescribeClusterSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelIds = field("ChannelIds")
    ClusterType = field("ClusterType")
    Id = field("Id")
    InstanceRoleArn = field("InstanceRoleArn")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return ClusterNetworkSettings.make_one(self.boto3_raw_data["NetworkSettings"])

    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterResponse:
    boto3_raw_data: "type_defs.UpdateClusterResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelIds = field("ChannelIds")
    ClusterType = field("ClusterType")
    Id = field("Id")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return ClusterNetworkSettings.make_one(self.boto3_raw_data["NetworkSettings"])

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterRequest:
    boto3_raw_data: "type_defs.UpdateClusterRequestTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return ClusterNetworkSettingsUpdateRequest.make_one(
            self.boto3_raw_data["NetworkSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNetworksResponse:
    boto3_raw_data: "type_defs.ListNetworksResponseTypeDef" = dataclasses.field()

    @cached_property
    def Networks(self):  # pragma: no cover
        return DescribeNetworkSummary.make_many(self.boto3_raw_data["Networks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNetworksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNetworksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesResponse:
    boto3_raw_data: "type_defs.ListNodesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Nodes(self):  # pragma: no cover
        return DescribeNodeSummary.make_many(self.boto3_raw_data["Nodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListNodesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOfferingsResponse:
    boto3_raw_data: "type_defs.ListOfferingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Offerings(self):  # pragma: no cover
        return Offering.make_many(self.boto3_raw_data["Offerings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOfferingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOfferingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationsResponse:
    boto3_raw_data: "type_defs.ListReservationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Reservations(self):  # pragma: no cover
        return Reservation.make_many(self.boto3_raw_data["Reservations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReservationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseOfferingResponse:
    boto3_raw_data: "type_defs.PurchaseOfferingResponseTypeDef" = dataclasses.field()

    @cached_property
    def Reservation(self):  # pragma: no cover
        return Reservation.make_one(self.boto3_raw_data["Reservation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PurchaseOfferingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseOfferingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReservationResponse:
    boto3_raw_data: "type_defs.UpdateReservationResponseTypeDef" = dataclasses.field()

    @cached_property
    def Reservation(self):  # pragma: no cover
        return Reservation.make_one(self.boto3_raw_data["Reservation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReservationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReservationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInputSecurityGroupResponse:
    boto3_raw_data: "type_defs.CreateInputSecurityGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SecurityGroup(self):  # pragma: no cover
        return InputSecurityGroup.make_one(self.boto3_raw_data["SecurityGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateInputSecurityGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInputSecurityGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputSecurityGroupsResponse:
    boto3_raw_data: "type_defs.ListInputSecurityGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputSecurityGroups(self):  # pragma: no cover
        return InputSecurityGroup.make_many(self.boto3_raw_data["InputSecurityGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInputSecurityGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputSecurityGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInputSecurityGroupResponse:
    boto3_raw_data: "type_defs.UpdateInputSecurityGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SecurityGroup(self):  # pragma: no cover
        return InputSecurityGroup.make_one(self.boto3_raw_data["SecurityGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateInputSecurityGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInputSecurityGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveContainerSettingsOutput:
    boto3_raw_data: "type_defs.ArchiveContainerSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def M2tsSettings(self):  # pragma: no cover
        return M2tsSettings.make_one(self.boto3_raw_data["M2tsSettings"])

    RawSettings = field("RawSettings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ArchiveContainerSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveContainerSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveContainerSettings:
    boto3_raw_data: "type_defs.ArchiveContainerSettingsTypeDef" = dataclasses.field()

    @cached_property
    def M2tsSettings(self):  # pragma: no cover
        return M2tsSettings.make_one(self.boto3_raw_data["M2tsSettings"])

    RawSettings = field("RawSettings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveContainerSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveContainerSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UdpContainerSettings:
    boto3_raw_data: "type_defs.UdpContainerSettingsTypeDef" = dataclasses.field()

    @cached_property
    def M2tsSettings(self):  # pragma: no cover
        return M2tsSettings.make_one(self.boto3_raw_data["M2tsSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UdpContainerSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UdpContainerSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalConfigurationOutput:
    boto3_raw_data: "type_defs.GlobalConfigurationOutputTypeDef" = dataclasses.field()

    InitialAudioGain = field("InitialAudioGain")
    InputEndAction = field("InputEndAction")

    @cached_property
    def InputLossBehavior(self):  # pragma: no cover
        return InputLossBehavior.make_one(self.boto3_raw_data["InputLossBehavior"])

    OutputLockingMode = field("OutputLockingMode")
    OutputTimingSource = field("OutputTimingSource")
    SupportLowFramerateInputs = field("SupportLowFramerateInputs")

    @cached_property
    def OutputLockingSettings(self):  # pragma: no cover
        return OutputLockingSettingsOutput.make_one(
            self.boto3_raw_data["OutputLockingSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalConfiguration:
    boto3_raw_data: "type_defs.GlobalConfigurationTypeDef" = dataclasses.field()

    InitialAudioGain = field("InitialAudioGain")
    InputEndAction = field("InputEndAction")

    @cached_property
    def InputLossBehavior(self):  # pragma: no cover
        return InputLossBehavior.make_one(self.boto3_raw_data["InputLossBehavior"])

    OutputLockingMode = field("OutputLockingMode")
    OutputTimingSource = field("OutputTimingSource")
    SupportLowFramerateInputs = field("SupportLowFramerateInputs")

    @cached_property
    def OutputLockingSettings(self):  # pragma: no cover
        return OutputLockingSettings.make_one(
            self.boto3_raw_data["OutputLockingSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverCondition:
    boto3_raw_data: "type_defs.FailoverConditionTypeDef" = dataclasses.field()

    @cached_property
    def FailoverConditionSettings(self):  # pragma: no cover
        return FailoverConditionSettings.make_one(
            self.boto3_raw_data["FailoverConditionSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailoverConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameCaptureGroupSettings:
    boto3_raw_data: "type_defs.FrameCaptureGroupSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def FrameCaptureCdnSettings(self):  # pragma: no cover
        return FrameCaptureCdnSettings.make_one(
            self.boto3_raw_data["FrameCaptureCdnSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrameCaptureGroupSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameCaptureGroupSettingsTypeDef"]
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
    AfdSignaling = field("AfdSignaling")
    Bitrate = field("Bitrate")
    BufFillPct = field("BufFillPct")
    BufSize = field("BufSize")
    ColorMetadata = field("ColorMetadata")

    @cached_property
    def ColorSpaceSettings(self):  # pragma: no cover
        return H264ColorSpaceSettingsOutput.make_one(
            self.boto3_raw_data["ColorSpaceSettings"]
        )

    EntropyEncoding = field("EntropyEncoding")

    @cached_property
    def FilterSettings(self):  # pragma: no cover
        return H264FilterSettings.make_one(self.boto3_raw_data["FilterSettings"])

    FixedAfd = field("FixedAfd")
    FlickerAq = field("FlickerAq")
    ForceFieldPictures = field("ForceFieldPictures")
    FramerateControl = field("FramerateControl")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopBReference = field("GopBReference")
    GopClosedCadence = field("GopClosedCadence")
    GopNumBFrames = field("GopNumBFrames")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    Level = field("Level")
    LookAheadRateControl = field("LookAheadRateControl")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    NumRefFrames = field("NumRefFrames")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    Profile = field("Profile")
    QualityLevel = field("QualityLevel")
    QvbrQualityLevel = field("QvbrQualityLevel")
    RateControlMode = field("RateControlMode")
    ScanType = field("ScanType")
    SceneChangeDetect = field("SceneChangeDetect")
    Slices = field("Slices")
    Softness = field("Softness")
    SpatialAq = field("SpatialAq")
    SubgopLength = field("SubgopLength")
    Syntax = field("Syntax")
    TemporalAq = field("TemporalAq")
    TimecodeInsertion = field("TimecodeInsertion")

    @cached_property
    def TimecodeBurninSettings(self):  # pragma: no cover
        return TimecodeBurninSettings.make_one(
            self.boto3_raw_data["TimecodeBurninSettings"]
        )

    MinQp = field("MinQp")
    MinBitrate = field("MinBitrate")

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
    AfdSignaling = field("AfdSignaling")
    Bitrate = field("Bitrate")
    BufFillPct = field("BufFillPct")
    BufSize = field("BufSize")
    ColorMetadata = field("ColorMetadata")

    @cached_property
    def ColorSpaceSettings(self):  # pragma: no cover
        return H264ColorSpaceSettings.make_one(
            self.boto3_raw_data["ColorSpaceSettings"]
        )

    EntropyEncoding = field("EntropyEncoding")

    @cached_property
    def FilterSettings(self):  # pragma: no cover
        return H264FilterSettings.make_one(self.boto3_raw_data["FilterSettings"])

    FixedAfd = field("FixedAfd")
    FlickerAq = field("FlickerAq")
    ForceFieldPictures = field("ForceFieldPictures")
    FramerateControl = field("FramerateControl")
    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    GopBReference = field("GopBReference")
    GopClosedCadence = field("GopClosedCadence")
    GopNumBFrames = field("GopNumBFrames")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    Level = field("Level")
    LookAheadRateControl = field("LookAheadRateControl")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    NumRefFrames = field("NumRefFrames")
    ParControl = field("ParControl")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    Profile = field("Profile")
    QualityLevel = field("QualityLevel")
    QvbrQualityLevel = field("QvbrQualityLevel")
    RateControlMode = field("RateControlMode")
    ScanType = field("ScanType")
    SceneChangeDetect = field("SceneChangeDetect")
    Slices = field("Slices")
    Softness = field("Softness")
    SpatialAq = field("SpatialAq")
    SubgopLength = field("SubgopLength")
    Syntax = field("Syntax")
    TemporalAq = field("TemporalAq")
    TimecodeInsertion = field("TimecodeInsertion")

    @cached_property
    def TimecodeBurninSettings(self):  # pragma: no cover
        return TimecodeBurninSettings.make_one(
            self.boto3_raw_data["TimecodeBurninSettings"]
        )

    MinQp = field("MinQp")
    MinBitrate = field("MinBitrate")

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

    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    AdaptiveQuantization = field("AdaptiveQuantization")
    AfdSignaling = field("AfdSignaling")
    AlternativeTransferFunction = field("AlternativeTransferFunction")
    Bitrate = field("Bitrate")
    BufSize = field("BufSize")
    ColorMetadata = field("ColorMetadata")

    @cached_property
    def ColorSpaceSettings(self):  # pragma: no cover
        return H265ColorSpaceSettingsOutput.make_one(
            self.boto3_raw_data["ColorSpaceSettings"]
        )

    @cached_property
    def FilterSettings(self):  # pragma: no cover
        return H265FilterSettings.make_one(self.boto3_raw_data["FilterSettings"])

    FixedAfd = field("FixedAfd")
    FlickerAq = field("FlickerAq")
    GopClosedCadence = field("GopClosedCadence")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    Level = field("Level")
    LookAheadRateControl = field("LookAheadRateControl")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    Profile = field("Profile")
    QvbrQualityLevel = field("QvbrQualityLevel")
    RateControlMode = field("RateControlMode")
    ScanType = field("ScanType")
    SceneChangeDetect = field("SceneChangeDetect")
    Slices = field("Slices")
    Tier = field("Tier")
    TimecodeInsertion = field("TimecodeInsertion")

    @cached_property
    def TimecodeBurninSettings(self):  # pragma: no cover
        return TimecodeBurninSettings.make_one(
            self.boto3_raw_data["TimecodeBurninSettings"]
        )

    MvOverPictureBoundaries = field("MvOverPictureBoundaries")
    MvTemporalPredictor = field("MvTemporalPredictor")
    TileHeight = field("TileHeight")
    TilePadding = field("TilePadding")
    TileWidth = field("TileWidth")
    TreeblockSize = field("TreeblockSize")
    MinQp = field("MinQp")
    Deblocking = field("Deblocking")
    GopBReference = field("GopBReference")
    GopNumBFrames = field("GopNumBFrames")
    MinBitrate = field("MinBitrate")
    SubgopLength = field("SubgopLength")

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

    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    AdaptiveQuantization = field("AdaptiveQuantization")
    AfdSignaling = field("AfdSignaling")
    AlternativeTransferFunction = field("AlternativeTransferFunction")
    Bitrate = field("Bitrate")
    BufSize = field("BufSize")
    ColorMetadata = field("ColorMetadata")

    @cached_property
    def ColorSpaceSettings(self):  # pragma: no cover
        return H265ColorSpaceSettings.make_one(
            self.boto3_raw_data["ColorSpaceSettings"]
        )

    @cached_property
    def FilterSettings(self):  # pragma: no cover
        return H265FilterSettings.make_one(self.boto3_raw_data["FilterSettings"])

    FixedAfd = field("FixedAfd")
    FlickerAq = field("FlickerAq")
    GopClosedCadence = field("GopClosedCadence")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    Level = field("Level")
    LookAheadRateControl = field("LookAheadRateControl")
    MaxBitrate = field("MaxBitrate")
    MinIInterval = field("MinIInterval")
    ParDenominator = field("ParDenominator")
    ParNumerator = field("ParNumerator")
    Profile = field("Profile")
    QvbrQualityLevel = field("QvbrQualityLevel")
    RateControlMode = field("RateControlMode")
    ScanType = field("ScanType")
    SceneChangeDetect = field("SceneChangeDetect")
    Slices = field("Slices")
    Tier = field("Tier")
    TimecodeInsertion = field("TimecodeInsertion")

    @cached_property
    def TimecodeBurninSettings(self):  # pragma: no cover
        return TimecodeBurninSettings.make_one(
            self.boto3_raw_data["TimecodeBurninSettings"]
        )

    MvOverPictureBoundaries = field("MvOverPictureBoundaries")
    MvTemporalPredictor = field("MvTemporalPredictor")
    TileHeight = field("TileHeight")
    TilePadding = field("TilePadding")
    TileWidth = field("TileWidth")
    TreeblockSize = field("TreeblockSize")
    MinQp = field("MinQp")
    Deblocking = field("Deblocking")
    GopBReference = field("GopBReference")
    GopNumBFrames = field("GopNumBFrames")
    MinBitrate = field("MinBitrate")
    SubgopLength = field("SubgopLength")

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
class Mpeg2Settings:
    boto3_raw_data: "type_defs.Mpeg2SettingsTypeDef" = dataclasses.field()

    FramerateDenominator = field("FramerateDenominator")
    FramerateNumerator = field("FramerateNumerator")
    AdaptiveQuantization = field("AdaptiveQuantization")
    AfdSignaling = field("AfdSignaling")
    ColorMetadata = field("ColorMetadata")
    ColorSpace = field("ColorSpace")
    DisplayAspectRatio = field("DisplayAspectRatio")

    @cached_property
    def FilterSettings(self):  # pragma: no cover
        return Mpeg2FilterSettings.make_one(self.boto3_raw_data["FilterSettings"])

    FixedAfd = field("FixedAfd")
    GopClosedCadence = field("GopClosedCadence")
    GopNumBFrames = field("GopNumBFrames")
    GopSize = field("GopSize")
    GopSizeUnits = field("GopSizeUnits")
    ScanType = field("ScanType")
    SubgopLength = field("SubgopLength")
    TimecodeInsertion = field("TimecodeInsertion")

    @cached_property
    def TimecodeBurninSettings(self):  # pragma: no cover
        return TimecodeBurninSettings.make_one(
            self.boto3_raw_data["TimecodeBurninSettings"]
        )

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
class InputPrepareScheduleActionSettingsOutput:
    boto3_raw_data: "type_defs.InputPrepareScheduleActionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    InputAttachmentNameReference = field("InputAttachmentNameReference")

    @cached_property
    def InputClippingSettings(self):  # pragma: no cover
        return InputClippingSettings.make_one(
            self.boto3_raw_data["InputClippingSettings"]
        )

    UrlPath = field("UrlPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputPrepareScheduleActionSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputPrepareScheduleActionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputPrepareScheduleActionSettings:
    boto3_raw_data: "type_defs.InputPrepareScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    InputAttachmentNameReference = field("InputAttachmentNameReference")

    @cached_property
    def InputClippingSettings(self):  # pragma: no cover
        return InputClippingSettings.make_one(
            self.boto3_raw_data["InputClippingSettings"]
        )

    UrlPath = field("UrlPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputPrepareScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputPrepareScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSwitchScheduleActionSettingsOutput:
    boto3_raw_data: "type_defs.InputSwitchScheduleActionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    InputAttachmentNameReference = field("InputAttachmentNameReference")

    @cached_property
    def InputClippingSettings(self):  # pragma: no cover
        return InputClippingSettings.make_one(
            self.boto3_raw_data["InputClippingSettings"]
        )

    UrlPath = field("UrlPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputSwitchScheduleActionSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSwitchScheduleActionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSwitchScheduleActionSettings:
    boto3_raw_data: "type_defs.InputSwitchScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    InputAttachmentNameReference = field("InputAttachmentNameReference")

    @cached_property
    def InputClippingSettings(self):  # pragma: no cover
        return InputClippingSettings.make_one(
            self.boto3_raw_data["InputClippingSettings"]
        )

    UrlPath = field("UrlPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputSwitchScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSwitchScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInputDeviceRequest:
    boto3_raw_data: "type_defs.UpdateInputDeviceRequestTypeDef" = dataclasses.field()

    InputDeviceId = field("InputDeviceId")

    @cached_property
    def HdDeviceSettings(self):  # pragma: no cover
        return InputDeviceConfigurableSettings.make_one(
            self.boto3_raw_data["HdDeviceSettings"]
        )

    Name = field("Name")

    @cached_property
    def UhdDeviceSettings(self):  # pragma: no cover
        return InputDeviceConfigurableSettings.make_one(
            self.boto3_raw_data["UhdDeviceSettings"]
        )

    AvailabilityZone = field("AvailabilityZone")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInputDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInputDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInputDeviceResponse:
    boto3_raw_data: "type_defs.DescribeInputDeviceResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ConnectionState = field("ConnectionState")
    DeviceSettingsSyncState = field("DeviceSettingsSyncState")
    DeviceUpdateStatus = field("DeviceUpdateStatus")

    @cached_property
    def HdDeviceSettings(self):  # pragma: no cover
        return InputDeviceHdSettings.make_one(self.boto3_raw_data["HdDeviceSettings"])

    Id = field("Id")
    MacAddress = field("MacAddress")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return InputDeviceNetworkSettings.make_one(
            self.boto3_raw_data["NetworkSettings"]
        )

    SerialNumber = field("SerialNumber")
    Type = field("Type")

    @cached_property
    def UhdDeviceSettings(self):  # pragma: no cover
        return InputDeviceUhdSettings.make_one(self.boto3_raw_data["UhdDeviceSettings"])

    Tags = field("Tags")
    AvailabilityZone = field("AvailabilityZone")
    MedialiveInputArns = field("MedialiveInputArns")
    OutputType = field("OutputType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInputDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDeviceSummary:
    boto3_raw_data: "type_defs.InputDeviceSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ConnectionState = field("ConnectionState")
    DeviceSettingsSyncState = field("DeviceSettingsSyncState")
    DeviceUpdateStatus = field("DeviceUpdateStatus")

    @cached_property
    def HdDeviceSettings(self):  # pragma: no cover
        return InputDeviceHdSettings.make_one(self.boto3_raw_data["HdDeviceSettings"])

    Id = field("Id")
    MacAddress = field("MacAddress")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return InputDeviceNetworkSettings.make_one(
            self.boto3_raw_data["NetworkSettings"]
        )

    SerialNumber = field("SerialNumber")
    Type = field("Type")

    @cached_property
    def UhdDeviceSettings(self):  # pragma: no cover
        return InputDeviceUhdSettings.make_one(self.boto3_raw_data["UhdDeviceSettings"])

    Tags = field("Tags")
    AvailabilityZone = field("AvailabilityZone")
    MedialiveInputArns = field("MedialiveInputArns")
    OutputType = field("OutputType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDeviceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDeviceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInputDeviceResponse:
    boto3_raw_data: "type_defs.UpdateInputDeviceResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ConnectionState = field("ConnectionState")
    DeviceSettingsSyncState = field("DeviceSettingsSyncState")
    DeviceUpdateStatus = field("DeviceUpdateStatus")

    @cached_property
    def HdDeviceSettings(self):  # pragma: no cover
        return InputDeviceHdSettings.make_one(self.boto3_raw_data["HdDeviceSettings"])

    Id = field("Id")
    MacAddress = field("MacAddress")
    Name = field("Name")

    @cached_property
    def NetworkSettings(self):  # pragma: no cover
        return InputDeviceNetworkSettings.make_one(
            self.boto3_raw_data["NetworkSettings"]
        )

    SerialNumber = field("SerialNumber")
    Type = field("Type")

    @cached_property
    def UhdDeviceSettings(self):  # pragma: no cover
        return InputDeviceUhdSettings.make_one(self.boto3_raw_data["UhdDeviceSettings"])

    Tags = field("Tags")
    AvailabilityZone = field("AvailabilityZone")
    MedialiveInputArns = field("MedialiveInputArns")
    OutputType = field("OutputType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInputDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInputDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Smpte2110ReceiverGroupOutput:
    boto3_raw_data: "type_defs.Smpte2110ReceiverGroupOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SdpSettings(self):  # pragma: no cover
        return Smpte2110ReceiverGroupSdpSettingsOutput.make_one(
            self.boto3_raw_data["SdpSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Smpte2110ReceiverGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Smpte2110ReceiverGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Smpte2110ReceiverGroup:
    boto3_raw_data: "type_defs.Smpte2110ReceiverGroupTypeDef" = dataclasses.field()

    @cached_property
    def SdpSettings(self):  # pragma: no cover
        return Smpte2110ReceiverGroupSdpSettings.make_one(
            self.boto3_raw_data["SdpSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Smpte2110ReceiverGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Smpte2110ReceiverGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsSettingsOutput:
    boto3_raw_data: "type_defs.HlsSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AudioOnlyHlsSettings(self):  # pragma: no cover
        return AudioOnlyHlsSettings.make_one(
            self.boto3_raw_data["AudioOnlyHlsSettings"]
        )

    @cached_property
    def Fmp4HlsSettings(self):  # pragma: no cover
        return Fmp4HlsSettings.make_one(self.boto3_raw_data["Fmp4HlsSettings"])

    FrameCaptureHlsSettings = field("FrameCaptureHlsSettings")

    @cached_property
    def StandardHlsSettings(self):  # pragma: no cover
        return StandardHlsSettings.make_one(self.boto3_raw_data["StandardHlsSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsSettingsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsSettingsOutputTypeDef"]
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

    @cached_property
    def AudioOnlyHlsSettings(self):  # pragma: no cover
        return AudioOnlyHlsSettings.make_one(
            self.boto3_raw_data["AudioOnlyHlsSettings"]
        )

    @cached_property
    def Fmp4HlsSettings(self):  # pragma: no cover
        return Fmp4HlsSettings.make_one(self.boto3_raw_data["Fmp4HlsSettings"])

    FrameCaptureHlsSettings = field("FrameCaptureHlsSettings")

    @cached_property
    def StandardHlsSettings(self):  # pragma: no cover
        return StandardHlsSettings.make_one(self.boto3_raw_data["StandardHlsSettings"])

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
class CreateSignalMapResponse:
    boto3_raw_data: "type_defs.CreateSignalMapResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CloudWatchAlarmTemplateGroupIds = field("CloudWatchAlarmTemplateGroupIds")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    DiscoveryEntryPointArn = field("DiscoveryEntryPointArn")
    ErrorMessage = field("ErrorMessage")
    EventBridgeRuleTemplateGroupIds = field("EventBridgeRuleTemplateGroupIds")
    FailedMediaResourceMap = field("FailedMediaResourceMap")
    Id = field("Id")
    LastDiscoveredAt = field("LastDiscoveredAt")

    @cached_property
    def LastSuccessfulMonitorDeployment(self):  # pragma: no cover
        return SuccessfulMonitorDeployment.make_one(
            self.boto3_raw_data["LastSuccessfulMonitorDeployment"]
        )

    MediaResourceMap = field("MediaResourceMap")
    ModifiedAt = field("ModifiedAt")
    MonitorChangesPendingDeployment = field("MonitorChangesPendingDeployment")

    @cached_property
    def MonitorDeployment(self):  # pragma: no cover
        return MonitorDeployment.make_one(self.boto3_raw_data["MonitorDeployment"])

    Name = field("Name")
    Status = field("Status")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSignalMapResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSignalMapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalMapResponse:
    boto3_raw_data: "type_defs.GetSignalMapResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CloudWatchAlarmTemplateGroupIds = field("CloudWatchAlarmTemplateGroupIds")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    DiscoveryEntryPointArn = field("DiscoveryEntryPointArn")
    ErrorMessage = field("ErrorMessage")
    EventBridgeRuleTemplateGroupIds = field("EventBridgeRuleTemplateGroupIds")
    FailedMediaResourceMap = field("FailedMediaResourceMap")
    Id = field("Id")
    LastDiscoveredAt = field("LastDiscoveredAt")

    @cached_property
    def LastSuccessfulMonitorDeployment(self):  # pragma: no cover
        return SuccessfulMonitorDeployment.make_one(
            self.boto3_raw_data["LastSuccessfulMonitorDeployment"]
        )

    MediaResourceMap = field("MediaResourceMap")
    ModifiedAt = field("ModifiedAt")
    MonitorChangesPendingDeployment = field("MonitorChangesPendingDeployment")

    @cached_property
    def MonitorDeployment(self):  # pragma: no cover
        return MonitorDeployment.make_one(self.boto3_raw_data["MonitorDeployment"])

    Name = field("Name")
    Status = field("Status")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSignalMapResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalMapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDeleteMonitorDeploymentResponse:
    boto3_raw_data: "type_defs.StartDeleteMonitorDeploymentResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CloudWatchAlarmTemplateGroupIds = field("CloudWatchAlarmTemplateGroupIds")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    DiscoveryEntryPointArn = field("DiscoveryEntryPointArn")
    ErrorMessage = field("ErrorMessage")
    EventBridgeRuleTemplateGroupIds = field("EventBridgeRuleTemplateGroupIds")
    FailedMediaResourceMap = field("FailedMediaResourceMap")
    Id = field("Id")
    LastDiscoveredAt = field("LastDiscoveredAt")

    @cached_property
    def LastSuccessfulMonitorDeployment(self):  # pragma: no cover
        return SuccessfulMonitorDeployment.make_one(
            self.boto3_raw_data["LastSuccessfulMonitorDeployment"]
        )

    MediaResourceMap = field("MediaResourceMap")
    ModifiedAt = field("ModifiedAt")
    MonitorChangesPendingDeployment = field("MonitorChangesPendingDeployment")

    @cached_property
    def MonitorDeployment(self):  # pragma: no cover
        return MonitorDeployment.make_one(self.boto3_raw_data["MonitorDeployment"])

    Name = field("Name")
    Status = field("Status")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDeleteMonitorDeploymentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeleteMonitorDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMonitorDeploymentResponse:
    boto3_raw_data: "type_defs.StartMonitorDeploymentResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CloudWatchAlarmTemplateGroupIds = field("CloudWatchAlarmTemplateGroupIds")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    DiscoveryEntryPointArn = field("DiscoveryEntryPointArn")
    ErrorMessage = field("ErrorMessage")
    EventBridgeRuleTemplateGroupIds = field("EventBridgeRuleTemplateGroupIds")
    FailedMediaResourceMap = field("FailedMediaResourceMap")
    Id = field("Id")
    LastDiscoveredAt = field("LastDiscoveredAt")

    @cached_property
    def LastSuccessfulMonitorDeployment(self):  # pragma: no cover
        return SuccessfulMonitorDeployment.make_one(
            self.boto3_raw_data["LastSuccessfulMonitorDeployment"]
        )

    MediaResourceMap = field("MediaResourceMap")
    ModifiedAt = field("ModifiedAt")
    MonitorChangesPendingDeployment = field("MonitorChangesPendingDeployment")

    @cached_property
    def MonitorDeployment(self):  # pragma: no cover
        return MonitorDeployment.make_one(self.boto3_raw_data["MonitorDeployment"])

    Name = field("Name")
    Status = field("Status")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMonitorDeploymentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMonitorDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartUpdateSignalMapResponse:
    boto3_raw_data: "type_defs.StartUpdateSignalMapResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CloudWatchAlarmTemplateGroupIds = field("CloudWatchAlarmTemplateGroupIds")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    DiscoveryEntryPointArn = field("DiscoveryEntryPointArn")
    ErrorMessage = field("ErrorMessage")
    EventBridgeRuleTemplateGroupIds = field("EventBridgeRuleTemplateGroupIds")
    FailedMediaResourceMap = field("FailedMediaResourceMap")
    Id = field("Id")
    LastDiscoveredAt = field("LastDiscoveredAt")

    @cached_property
    def LastSuccessfulMonitorDeployment(self):  # pragma: no cover
        return SuccessfulMonitorDeployment.make_one(
            self.boto3_raw_data["LastSuccessfulMonitorDeployment"]
        )

    MediaResourceMap = field("MediaResourceMap")
    ModifiedAt = field("ModifiedAt")
    MonitorChangesPendingDeployment = field("MonitorChangesPendingDeployment")

    @cached_property
    def MonitorDeployment(self):  # pragma: no cover
        return MonitorDeployment.make_one(self.boto3_raw_data["MonitorDeployment"])

    Name = field("Name")
    Status = field("Status")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartUpdateSignalMapResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartUpdateSignalMapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexOutputSettings:
    boto3_raw_data: "type_defs.MultiplexOutputSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def ContainerSettings(self):  # pragma: no cover
        return MultiplexContainerSettings.make_one(
            self.boto3_raw_data["ContainerSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiplexOutputSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMultiplexResponse:
    boto3_raw_data: "type_defs.DeleteMultiplexResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AvailabilityZones = field("AvailabilityZones")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return MultiplexOutputDestination.make_many(self.boto3_raw_data["Destinations"])

    Id = field("Id")

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexSettings.make_one(self.boto3_raw_data["MultiplexSettings"])

    Name = field("Name")
    PipelinesRunningCount = field("PipelinesRunningCount")
    ProgramCount = field("ProgramCount")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMultiplexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiplexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiplexResponse:
    boto3_raw_data: "type_defs.DescribeMultiplexResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AvailabilityZones = field("AvailabilityZones")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return MultiplexOutputDestination.make_many(self.boto3_raw_data["Destinations"])

    Id = field("Id")

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexSettings.make_one(self.boto3_raw_data["MultiplexSettings"])

    Name = field("Name")
    PipelinesRunningCount = field("PipelinesRunningCount")
    ProgramCount = field("ProgramCount")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMultiplexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiplexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Multiplex:
    boto3_raw_data: "type_defs.MultiplexTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AvailabilityZones = field("AvailabilityZones")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return MultiplexOutputDestination.make_many(self.boto3_raw_data["Destinations"])

    Id = field("Id")

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexSettings.make_one(self.boto3_raw_data["MultiplexSettings"])

    Name = field("Name")
    PipelinesRunningCount = field("PipelinesRunningCount")
    ProgramCount = field("ProgramCount")
    State = field("State")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MultiplexTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MultiplexTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMultiplexResponse:
    boto3_raw_data: "type_defs.StartMultiplexResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AvailabilityZones = field("AvailabilityZones")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return MultiplexOutputDestination.make_many(self.boto3_raw_data["Destinations"])

    Id = field("Id")

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexSettings.make_one(self.boto3_raw_data["MultiplexSettings"])

    Name = field("Name")
    PipelinesRunningCount = field("PipelinesRunningCount")
    ProgramCount = field("ProgramCount")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMultiplexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMultiplexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopMultiplexResponse:
    boto3_raw_data: "type_defs.StopMultiplexResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AvailabilityZones = field("AvailabilityZones")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return MultiplexOutputDestination.make_many(self.boto3_raw_data["Destinations"])

    Id = field("Id")

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexSettings.make_one(self.boto3_raw_data["MultiplexSettings"])

    Name = field("Name")
    PipelinesRunningCount = field("PipelinesRunningCount")
    ProgramCount = field("ProgramCount")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopMultiplexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopMultiplexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMultiplexRequest:
    boto3_raw_data: "type_defs.UpdateMultiplexRequestTypeDef" = dataclasses.field()

    MultiplexId = field("MultiplexId")

    @cached_property
    def MultiplexSettings(self):  # pragma: no cover
        return MultiplexSettings.make_one(self.boto3_raw_data["MultiplexSettings"])

    Name = field("Name")
    PacketIdentifiersMapping = field("PacketIdentifiersMapping")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMultiplexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMultiplexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiplexesResponse:
    boto3_raw_data: "type_defs.ListMultiplexesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Multiplexes(self):  # pragma: no cover
        return MultiplexSummary.make_many(self.boto3_raw_data["Multiplexes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMultiplexesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiplexesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexProgramSettings:
    boto3_raw_data: "type_defs.MultiplexProgramSettingsTypeDef" = dataclasses.field()

    ProgramNumber = field("ProgramNumber")
    PreferredChannelPipeline = field("PreferredChannelPipeline")

    @cached_property
    def ServiceDescriptor(self):  # pragma: no cover
        return MultiplexProgramServiceDescriptor.make_one(
            self.boto3_raw_data["ServiceDescriptor"]
        )

    @cached_property
    def VideoSettings(self):  # pragma: no cover
        return MultiplexVideoSettings.make_one(self.boto3_raw_data["VideoSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiplexProgramSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexProgramSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioWatermarkSettings:
    boto3_raw_data: "type_defs.AudioWatermarkSettingsTypeDef" = dataclasses.field()

    @cached_property
    def NielsenWatermarksSettings(self):  # pragma: no cover
        return NielsenWatermarksSettings.make_one(
            self.boto3_raw_data["NielsenWatermarksSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioWatermarkSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioWatermarkSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35DescriptorSettings:
    boto3_raw_data: "type_defs.Scte35DescriptorSettingsTypeDef" = dataclasses.field()

    @cached_property
    def SegmentationDescriptorScte35DescriptorSettings(self):  # pragma: no cover
        return Scte35SegmentationDescriptor.make_one(
            self.boto3_raw_data["SegmentationDescriptorScte35DescriptorSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Scte35DescriptorSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35DescriptorSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtSettingsRequest:
    boto3_raw_data: "type_defs.SrtSettingsRequestTypeDef" = dataclasses.field()

    @cached_property
    def SrtCallerSources(self):  # pragma: no cover
        return SrtCallerSourceRequest.make_many(self.boto3_raw_data["SrtCallerSources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SrtSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SrtSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtSettings:
    boto3_raw_data: "type_defs.SrtSettingsTypeDef" = dataclasses.field()

    @cached_property
    def SrtCallerSources(self):  # pragma: no cover
        return SrtCallerSource.make_many(self.boto3_raw_data["SrtCallerSources"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SrtSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SrtSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThumbnailsResponse:
    boto3_raw_data: "type_defs.DescribeThumbnailsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ThumbnailDetails(self):  # pragma: no cover
        return ThumbnailDetail.make_many(self.boto3_raw_data["ThumbnailDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThumbnailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThumbnailsResponseTypeDef"]
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

    ColorSpace = field("ColorSpace")

    @cached_property
    def ColorSpaceSettings(self):  # pragma: no cover
        return VideoSelectorColorSpaceSettings.make_one(
            self.boto3_raw_data["ColorSpaceSettings"]
        )

    ColorSpaceUsage = field("ColorSpaceUsage")

    @cached_property
    def SelectorSettings(self):  # pragma: no cover
        return VideoSelectorSettings.make_one(self.boto3_raw_data["SelectorSettings"])

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
class CaptionDescriptionOutput:
    boto3_raw_data: "type_defs.CaptionDescriptionOutputTypeDef" = dataclasses.field()

    CaptionSelectorName = field("CaptionSelectorName")
    Name = field("Name")
    Accessibility = field("Accessibility")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return CaptionDestinationSettingsOutput.make_one(
            self.boto3_raw_data["DestinationSettings"]
        )

    LanguageCode = field("LanguageCode")
    LanguageDescription = field("LanguageDescription")
    CaptionDashRoles = field("CaptionDashRoles")
    DvbDashAccessibility = field("DvbDashAccessibility")

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
class CaptionDescription:
    boto3_raw_data: "type_defs.CaptionDescriptionTypeDef" = dataclasses.field()

    CaptionSelectorName = field("CaptionSelectorName")
    Name = field("Name")
    Accessibility = field("Accessibility")

    @cached_property
    def DestinationSettings(self):  # pragma: no cover
        return CaptionDestinationSettings.make_one(
            self.boto3_raw_data["DestinationSettings"]
        )

    LanguageCode = field("LanguageCode")
    LanguageDescription = field("LanguageDescription")
    CaptionDashRoles = field("CaptionDashRoles")
    DvbDashAccessibility = field("DvbDashAccessibility")

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
class HlsGroupSettingsOutput:
    boto3_raw_data: "type_defs.HlsGroupSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    AdMarkers = field("AdMarkers")
    BaseUrlContent = field("BaseUrlContent")
    BaseUrlContent1 = field("BaseUrlContent1")
    BaseUrlManifest = field("BaseUrlManifest")
    BaseUrlManifest1 = field("BaseUrlManifest1")

    @cached_property
    def CaptionLanguageMappings(self):  # pragma: no cover
        return CaptionLanguageMapping.make_many(
            self.boto3_raw_data["CaptionLanguageMappings"]
        )

    CaptionLanguageSetting = field("CaptionLanguageSetting")
    ClientCache = field("ClientCache")
    CodecSpecification = field("CodecSpecification")
    ConstantIv = field("ConstantIv")
    DirectoryStructure = field("DirectoryStructure")
    DiscontinuityTags = field("DiscontinuityTags")
    EncryptionType = field("EncryptionType")

    @cached_property
    def HlsCdnSettings(self):  # pragma: no cover
        return HlsCdnSettings.make_one(self.boto3_raw_data["HlsCdnSettings"])

    HlsId3SegmentTagging = field("HlsId3SegmentTagging")
    IFrameOnlyPlaylists = field("IFrameOnlyPlaylists")
    IncompleteSegmentBehavior = field("IncompleteSegmentBehavior")
    IndexNSegments = field("IndexNSegments")
    InputLossAction = field("InputLossAction")
    IvInManifest = field("IvInManifest")
    IvSource = field("IvSource")
    KeepSegments = field("KeepSegments")
    KeyFormat = field("KeyFormat")
    KeyFormatVersions = field("KeyFormatVersions")

    @cached_property
    def KeyProviderSettings(self):  # pragma: no cover
        return KeyProviderSettings.make_one(self.boto3_raw_data["KeyProviderSettings"])

    ManifestCompression = field("ManifestCompression")
    ManifestDurationFormat = field("ManifestDurationFormat")
    MinSegmentLength = field("MinSegmentLength")
    Mode = field("Mode")
    OutputSelection = field("OutputSelection")
    ProgramDateTime = field("ProgramDateTime")
    ProgramDateTimeClock = field("ProgramDateTimeClock")
    ProgramDateTimePeriod = field("ProgramDateTimePeriod")
    RedundantManifest = field("RedundantManifest")
    SegmentLength = field("SegmentLength")
    SegmentationMode = field("SegmentationMode")
    SegmentsPerSubdirectory = field("SegmentsPerSubdirectory")
    StreamInfResolution = field("StreamInfResolution")
    TimedMetadataId3Frame = field("TimedMetadataId3Frame")
    TimedMetadataId3Period = field("TimedMetadataId3Period")
    TimestampDeltaMilliseconds = field("TimestampDeltaMilliseconds")
    TsFileMode = field("TsFileMode")

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

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    AdMarkers = field("AdMarkers")
    BaseUrlContent = field("BaseUrlContent")
    BaseUrlContent1 = field("BaseUrlContent1")
    BaseUrlManifest = field("BaseUrlManifest")
    BaseUrlManifest1 = field("BaseUrlManifest1")

    @cached_property
    def CaptionLanguageMappings(self):  # pragma: no cover
        return CaptionLanguageMapping.make_many(
            self.boto3_raw_data["CaptionLanguageMappings"]
        )

    CaptionLanguageSetting = field("CaptionLanguageSetting")
    ClientCache = field("ClientCache")
    CodecSpecification = field("CodecSpecification")
    ConstantIv = field("ConstantIv")
    DirectoryStructure = field("DirectoryStructure")
    DiscontinuityTags = field("DiscontinuityTags")
    EncryptionType = field("EncryptionType")

    @cached_property
    def HlsCdnSettings(self):  # pragma: no cover
        return HlsCdnSettings.make_one(self.boto3_raw_data["HlsCdnSettings"])

    HlsId3SegmentTagging = field("HlsId3SegmentTagging")
    IFrameOnlyPlaylists = field("IFrameOnlyPlaylists")
    IncompleteSegmentBehavior = field("IncompleteSegmentBehavior")
    IndexNSegments = field("IndexNSegments")
    InputLossAction = field("InputLossAction")
    IvInManifest = field("IvInManifest")
    IvSource = field("IvSource")
    KeepSegments = field("KeepSegments")
    KeyFormat = field("KeyFormat")
    KeyFormatVersions = field("KeyFormatVersions")

    @cached_property
    def KeyProviderSettings(self):  # pragma: no cover
        return KeyProviderSettings.make_one(self.boto3_raw_data["KeyProviderSettings"])

    ManifestCompression = field("ManifestCompression")
    ManifestDurationFormat = field("ManifestDurationFormat")
    MinSegmentLength = field("MinSegmentLength")
    Mode = field("Mode")
    OutputSelection = field("OutputSelection")
    ProgramDateTime = field("ProgramDateTime")
    ProgramDateTimeClock = field("ProgramDateTimeClock")
    ProgramDateTimePeriod = field("ProgramDateTimePeriod")
    RedundantManifest = field("RedundantManifest")
    SegmentLength = field("SegmentLength")
    SegmentationMode = field("SegmentationMode")
    SegmentsPerSubdirectory = field("SegmentsPerSubdirectory")
    StreamInfResolution = field("StreamInfResolution")
    TimedMetadataId3Frame = field("TimedMetadataId3Frame")
    TimedMetadataId3Period = field("TimedMetadataId3Period")
    TimestampDeltaMilliseconds = field("TimestampDeltaMilliseconds")
    TsFileMode = field("TsFileMode")

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
class AudioSelectorOutput:
    boto3_raw_data: "type_defs.AudioSelectorOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def SelectorSettings(self):  # pragma: no cover
        return AudioSelectorSettingsOutput.make_one(
            self.boto3_raw_data["SelectorSettings"]
        )

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
class AudioSelectorSettings:
    boto3_raw_data: "type_defs.AudioSelectorSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AudioHlsRenditionSelection(self):  # pragma: no cover
        return AudioHlsRenditionSelection.make_one(
            self.boto3_raw_data["AudioHlsRenditionSelection"]
        )

    @cached_property
    def AudioLanguageSelection(self):  # pragma: no cover
        return AudioLanguageSelection.make_one(
            self.boto3_raw_data["AudioLanguageSelection"]
        )

    @cached_property
    def AudioPidSelection(self):  # pragma: no cover
        return AudioPidSelection.make_one(self.boto3_raw_data["AudioPidSelection"])

    AudioTrackSelection = field("AudioTrackSelection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioSelectorSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioSelectorSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionSelectorOutput:
    boto3_raw_data: "type_defs.CaptionSelectorOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    LanguageCode = field("LanguageCode")

    @cached_property
    def SelectorSettings(self):  # pragma: no cover
        return CaptionSelectorSettingsOutput.make_one(
            self.boto3_raw_data["SelectorSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptionSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptionSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersResponse:
    boto3_raw_data: "type_defs.ListClustersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Clusters(self):  # pragma: no cover
        return DescribeClusterSummary.make_many(self.boto3_raw_data["Clusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveOutputSettingsOutput:
    boto3_raw_data: "type_defs.ArchiveOutputSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ContainerSettings(self):  # pragma: no cover
        return ArchiveContainerSettingsOutput.make_one(
            self.boto3_raw_data["ContainerSettings"]
        )

    Extension = field("Extension")
    NameModifier = field("NameModifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveOutputSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveOutputSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveOutputSettings:
    boto3_raw_data: "type_defs.ArchiveOutputSettingsTypeDef" = dataclasses.field()

    @cached_property
    def ContainerSettings(self):  # pragma: no cover
        return ArchiveContainerSettings.make_one(
            self.boto3_raw_data["ContainerSettings"]
        )

    Extension = field("Extension")
    NameModifier = field("NameModifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveOutputSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SrtOutputSettings:
    boto3_raw_data: "type_defs.SrtOutputSettingsTypeDef" = dataclasses.field()

    @cached_property
    def ContainerSettings(self):  # pragma: no cover
        return UdpContainerSettings.make_one(self.boto3_raw_data["ContainerSettings"])

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    BufferMsec = field("BufferMsec")
    EncryptionType = field("EncryptionType")
    Latency = field("Latency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SrtOutputSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SrtOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UdpOutputSettings:
    boto3_raw_data: "type_defs.UdpOutputSettingsTypeDef" = dataclasses.field()

    @cached_property
    def ContainerSettings(self):  # pragma: no cover
        return UdpContainerSettings.make_one(self.boto3_raw_data["ContainerSettings"])

    @cached_property
    def Destination(self):  # pragma: no cover
        return OutputLocationRef.make_one(self.boto3_raw_data["Destination"])

    BufferMsec = field("BufferMsec")

    @cached_property
    def FecOutputSettings(self):  # pragma: no cover
        return FecOutputSettings.make_one(self.boto3_raw_data["FecOutputSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UdpOutputSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UdpOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomaticInputFailoverSettingsOutput:
    boto3_raw_data: "type_defs.AutomaticInputFailoverSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    SecondaryInputId = field("SecondaryInputId")
    ErrorClearTimeMsec = field("ErrorClearTimeMsec")

    @cached_property
    def FailoverConditions(self):  # pragma: no cover
        return FailoverCondition.make_many(self.boto3_raw_data["FailoverConditions"])

    InputPreference = field("InputPreference")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomaticInputFailoverSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomaticInputFailoverSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomaticInputFailoverSettings:
    boto3_raw_data: "type_defs.AutomaticInputFailoverSettingsTypeDef" = (
        dataclasses.field()
    )

    SecondaryInputId = field("SecondaryInputId")
    ErrorClearTimeMsec = field("ErrorClearTimeMsec")

    @cached_property
    def FailoverConditions(self):  # pragma: no cover
        return FailoverCondition.make_many(self.boto3_raw_data["FailoverConditions"])

    InputPreference = field("InputPreference")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomaticInputFailoverSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomaticInputFailoverSettingsTypeDef"]
        ],
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
    def FrameCaptureSettings(self):  # pragma: no cover
        return FrameCaptureSettings.make_one(
            self.boto3_raw_data["FrameCaptureSettings"]
        )

    @cached_property
    def H264Settings(self):  # pragma: no cover
        return H264SettingsOutput.make_one(self.boto3_raw_data["H264Settings"])

    @cached_property
    def H265Settings(self):  # pragma: no cover
        return H265SettingsOutput.make_one(self.boto3_raw_data["H265Settings"])

    @cached_property
    def Mpeg2Settings(self):  # pragma: no cover
        return Mpeg2Settings.make_one(self.boto3_raw_data["Mpeg2Settings"])

    @cached_property
    def Av1Settings(self):  # pragma: no cover
        return Av1SettingsOutput.make_one(self.boto3_raw_data["Av1Settings"])

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
    def FrameCaptureSettings(self):  # pragma: no cover
        return FrameCaptureSettings.make_one(
            self.boto3_raw_data["FrameCaptureSettings"]
        )

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
    def Av1Settings(self):  # pragma: no cover
        return Av1Settings.make_one(self.boto3_raw_data["Av1Settings"])

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
class ListInputDevicesResponse:
    boto3_raw_data: "type_defs.ListInputDevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def InputDevices(self):  # pragma: no cover
        return InputDeviceSummary.make_many(self.boto3_raw_data["InputDevices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInputDevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputDevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Smpte2110ReceiverGroupSettingsOutput:
    boto3_raw_data: "type_defs.Smpte2110ReceiverGroupSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Smpte2110ReceiverGroups(self):  # pragma: no cover
        return Smpte2110ReceiverGroupOutput.make_many(
            self.boto3_raw_data["Smpte2110ReceiverGroups"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Smpte2110ReceiverGroupSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Smpte2110ReceiverGroupSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Smpte2110ReceiverGroupSettings:
    boto3_raw_data: "type_defs.Smpte2110ReceiverGroupSettingsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Smpte2110ReceiverGroups(self):  # pragma: no cover
        return Smpte2110ReceiverGroup.make_many(
            self.boto3_raw_data["Smpte2110ReceiverGroups"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.Smpte2110ReceiverGroupSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Smpte2110ReceiverGroupSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsOutputSettingsOutput:
    boto3_raw_data: "type_defs.HlsOutputSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def HlsSettings(self):  # pragma: no cover
        return HlsSettingsOutput.make_one(self.boto3_raw_data["HlsSettings"])

    H265PackagingType = field("H265PackagingType")
    NameModifier = field("NameModifier")
    SegmentModifier = field("SegmentModifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsOutputSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsOutputSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsOutputSettings:
    boto3_raw_data: "type_defs.HlsOutputSettingsTypeDef" = dataclasses.field()

    @cached_property
    def HlsSettings(self):  # pragma: no cover
        return HlsSettings.make_one(self.boto3_raw_data["HlsSettings"])

    H265PackagingType = field("H265PackagingType")
    NameModifier = field("NameModifier")
    SegmentModifier = field("SegmentModifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsOutputSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsOutputSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultiplexResponse:
    boto3_raw_data: "type_defs.CreateMultiplexResponseTypeDef" = dataclasses.field()

    @cached_property
    def Multiplex(self):  # pragma: no cover
        return Multiplex.make_one(self.boto3_raw_data["Multiplex"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMultiplexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiplexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMultiplexResponse:
    boto3_raw_data: "type_defs.UpdateMultiplexResponseTypeDef" = dataclasses.field()

    @cached_property
    def Multiplex(self):  # pragma: no cover
        return Multiplex.make_one(self.boto3_raw_data["Multiplex"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMultiplexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMultiplexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultiplexProgramRequest:
    boto3_raw_data: "type_defs.CreateMultiplexProgramRequestTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")

    @cached_property
    def MultiplexProgramSettings(self):  # pragma: no cover
        return MultiplexProgramSettings.make_one(
            self.boto3_raw_data["MultiplexProgramSettings"]
        )

    ProgramName = field("ProgramName")
    RequestId = field("RequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMultiplexProgramRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiplexProgramRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMultiplexProgramResponse:
    boto3_raw_data: "type_defs.DeleteMultiplexProgramResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")

    @cached_property
    def MultiplexProgramSettings(self):  # pragma: no cover
        return MultiplexProgramSettings.make_one(
            self.boto3_raw_data["MultiplexProgramSettings"]
        )

    @cached_property
    def PacketIdentifiersMap(self):  # pragma: no cover
        return MultiplexProgramPacketIdentifiersMapOutput.make_one(
            self.boto3_raw_data["PacketIdentifiersMap"]
        )

    @cached_property
    def PipelineDetails(self):  # pragma: no cover
        return MultiplexProgramPipelineDetail.make_many(
            self.boto3_raw_data["PipelineDetails"]
        )

    ProgramName = field("ProgramName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMultiplexProgramResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiplexProgramResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiplexProgramResponse:
    boto3_raw_data: "type_defs.DescribeMultiplexProgramResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")

    @cached_property
    def MultiplexProgramSettings(self):  # pragma: no cover
        return MultiplexProgramSettings.make_one(
            self.boto3_raw_data["MultiplexProgramSettings"]
        )

    @cached_property
    def PacketIdentifiersMap(self):  # pragma: no cover
        return MultiplexProgramPacketIdentifiersMapOutput.make_one(
            self.boto3_raw_data["PacketIdentifiersMap"]
        )

    @cached_property
    def PipelineDetails(self):  # pragma: no cover
        return MultiplexProgramPipelineDetail.make_many(
            self.boto3_raw_data["PipelineDetails"]
        )

    ProgramName = field("ProgramName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMultiplexProgramResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiplexProgramResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiplexProgram:
    boto3_raw_data: "type_defs.MultiplexProgramTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")

    @cached_property
    def MultiplexProgramSettings(self):  # pragma: no cover
        return MultiplexProgramSettings.make_one(
            self.boto3_raw_data["MultiplexProgramSettings"]
        )

    @cached_property
    def PacketIdentifiersMap(self):  # pragma: no cover
        return MultiplexProgramPacketIdentifiersMapOutput.make_one(
            self.boto3_raw_data["PacketIdentifiersMap"]
        )

    @cached_property
    def PipelineDetails(self):  # pragma: no cover
        return MultiplexProgramPipelineDetail.make_many(
            self.boto3_raw_data["PipelineDetails"]
        )

    ProgramName = field("ProgramName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MultiplexProgramTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiplexProgramTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMultiplexProgramRequest:
    boto3_raw_data: "type_defs.UpdateMultiplexProgramRequestTypeDef" = (
        dataclasses.field()
    )

    MultiplexId = field("MultiplexId")
    ProgramName = field("ProgramName")

    @cached_property
    def MultiplexProgramSettings(self):  # pragma: no cover
        return MultiplexProgramSettings.make_one(
            self.boto3_raw_data["MultiplexProgramSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMultiplexProgramRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMultiplexProgramRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioDescriptionOutput:
    boto3_raw_data: "type_defs.AudioDescriptionOutputTypeDef" = dataclasses.field()

    AudioSelectorName = field("AudioSelectorName")
    Name = field("Name")

    @cached_property
    def AudioNormalizationSettings(self):  # pragma: no cover
        return AudioNormalizationSettings.make_one(
            self.boto3_raw_data["AudioNormalizationSettings"]
        )

    AudioType = field("AudioType")
    AudioTypeControl = field("AudioTypeControl")

    @cached_property
    def AudioWatermarkingSettings(self):  # pragma: no cover
        return AudioWatermarkSettings.make_one(
            self.boto3_raw_data["AudioWatermarkingSettings"]
        )

    @cached_property
    def CodecSettings(self):  # pragma: no cover
        return AudioCodecSettingsOutput.make_one(self.boto3_raw_data["CodecSettings"])

    LanguageCode = field("LanguageCode")
    LanguageCodeControl = field("LanguageCodeControl")

    @cached_property
    def RemixSettings(self):  # pragma: no cover
        return RemixSettingsOutput.make_one(self.boto3_raw_data["RemixSettings"])

    StreamName = field("StreamName")
    AudioDashRoles = field("AudioDashRoles")
    DvbDashAccessibility = field("DvbDashAccessibility")

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
class AudioDescription:
    boto3_raw_data: "type_defs.AudioDescriptionTypeDef" = dataclasses.field()

    AudioSelectorName = field("AudioSelectorName")
    Name = field("Name")

    @cached_property
    def AudioNormalizationSettings(self):  # pragma: no cover
        return AudioNormalizationSettings.make_one(
            self.boto3_raw_data["AudioNormalizationSettings"]
        )

    AudioType = field("AudioType")
    AudioTypeControl = field("AudioTypeControl")

    @cached_property
    def AudioWatermarkingSettings(self):  # pragma: no cover
        return AudioWatermarkSettings.make_one(
            self.boto3_raw_data["AudioWatermarkingSettings"]
        )

    @cached_property
    def CodecSettings(self):  # pragma: no cover
        return AudioCodecSettings.make_one(self.boto3_raw_data["CodecSettings"])

    LanguageCode = field("LanguageCode")
    LanguageCodeControl = field("LanguageCodeControl")

    @cached_property
    def RemixSettings(self):  # pragma: no cover
        return RemixSettings.make_one(self.boto3_raw_data["RemixSettings"])

    StreamName = field("StreamName")
    AudioDashRoles = field("AudioDashRoles")
    DvbDashAccessibility = field("DvbDashAccessibility")

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
class UpdateChannelClassRequest:
    boto3_raw_data: "type_defs.UpdateChannelClassRequestTypeDef" = dataclasses.field()

    ChannelClass = field("ChannelClass")
    ChannelId = field("ChannelId")
    Destinations = field("Destinations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelClassRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelClassRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35Descriptor:
    boto3_raw_data: "type_defs.Scte35DescriptorTypeDef" = dataclasses.field()

    @cached_property
    def Scte35DescriptorSettings(self):  # pragma: no cover
        return Scte35DescriptorSettings.make_one(
            self.boto3_raw_data["Scte35DescriptorSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Scte35DescriptorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35DescriptorTypeDef"]
        ],
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
    def ArchiveGroupSettings(self):  # pragma: no cover
        return ArchiveGroupSettings.make_one(
            self.boto3_raw_data["ArchiveGroupSettings"]
        )

    @cached_property
    def FrameCaptureGroupSettings(self):  # pragma: no cover
        return FrameCaptureGroupSettings.make_one(
            self.boto3_raw_data["FrameCaptureGroupSettings"]
        )

    @cached_property
    def HlsGroupSettings(self):  # pragma: no cover
        return HlsGroupSettingsOutput.make_one(self.boto3_raw_data["HlsGroupSettings"])

    @cached_property
    def MediaPackageGroupSettings(self):  # pragma: no cover
        return MediaPackageGroupSettingsOutput.make_one(
            self.boto3_raw_data["MediaPackageGroupSettings"]
        )

    @cached_property
    def MsSmoothGroupSettings(self):  # pragma: no cover
        return MsSmoothGroupSettings.make_one(
            self.boto3_raw_data["MsSmoothGroupSettings"]
        )

    MultiplexGroupSettings = field("MultiplexGroupSettings")

    @cached_property
    def RtmpGroupSettings(self):  # pragma: no cover
        return RtmpGroupSettingsOutput.make_one(
            self.boto3_raw_data["RtmpGroupSettings"]
        )

    @cached_property
    def UdpGroupSettings(self):  # pragma: no cover
        return UdpGroupSettings.make_one(self.boto3_raw_data["UdpGroupSettings"])

    @cached_property
    def CmafIngestGroupSettings(self):  # pragma: no cover
        return CmafIngestGroupSettingsOutput.make_one(
            self.boto3_raw_data["CmafIngestGroupSettings"]
        )

    @cached_property
    def SrtGroupSettings(self):  # pragma: no cover
        return SrtGroupSettings.make_one(self.boto3_raw_data["SrtGroupSettings"])

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
    def ArchiveGroupSettings(self):  # pragma: no cover
        return ArchiveGroupSettings.make_one(
            self.boto3_raw_data["ArchiveGroupSettings"]
        )

    @cached_property
    def FrameCaptureGroupSettings(self):  # pragma: no cover
        return FrameCaptureGroupSettings.make_one(
            self.boto3_raw_data["FrameCaptureGroupSettings"]
        )

    @cached_property
    def HlsGroupSettings(self):  # pragma: no cover
        return HlsGroupSettings.make_one(self.boto3_raw_data["HlsGroupSettings"])

    @cached_property
    def MediaPackageGroupSettings(self):  # pragma: no cover
        return MediaPackageGroupSettings.make_one(
            self.boto3_raw_data["MediaPackageGroupSettings"]
        )

    @cached_property
    def MsSmoothGroupSettings(self):  # pragma: no cover
        return MsSmoothGroupSettings.make_one(
            self.boto3_raw_data["MsSmoothGroupSettings"]
        )

    MultiplexGroupSettings = field("MultiplexGroupSettings")

    @cached_property
    def RtmpGroupSettings(self):  # pragma: no cover
        return RtmpGroupSettings.make_one(self.boto3_raw_data["RtmpGroupSettings"])

    @cached_property
    def UdpGroupSettings(self):  # pragma: no cover
        return UdpGroupSettings.make_one(self.boto3_raw_data["UdpGroupSettings"])

    @cached_property
    def CmafIngestGroupSettings(self):  # pragma: no cover
        return CmafIngestGroupSettings.make_one(
            self.boto3_raw_data["CmafIngestGroupSettings"]
        )

    @cached_property
    def SrtGroupSettings(self):  # pragma: no cover
        return SrtGroupSettings.make_one(self.boto3_raw_data["SrtGroupSettings"])

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
class InputSettingsOutput:
    boto3_raw_data: "type_defs.InputSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AudioSelectors(self):  # pragma: no cover
        return AudioSelectorOutput.make_many(self.boto3_raw_data["AudioSelectors"])

    @cached_property
    def CaptionSelectors(self):  # pragma: no cover
        return CaptionSelectorOutput.make_many(self.boto3_raw_data["CaptionSelectors"])

    DeblockFilter = field("DeblockFilter")
    DenoiseFilter = field("DenoiseFilter")
    FilterStrength = field("FilterStrength")
    InputFilter = field("InputFilter")

    @cached_property
    def NetworkInputSettings(self):  # pragma: no cover
        return NetworkInputSettings.make_one(
            self.boto3_raw_data["NetworkInputSettings"]
        )

    Scte35Pid = field("Scte35Pid")
    Smpte2038DataPreference = field("Smpte2038DataPreference")
    SourceEndBehavior = field("SourceEndBehavior")

    @cached_property
    def VideoSelector(self):  # pragma: no cover
        return VideoSelector.make_one(self.boto3_raw_data["VideoSelector"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSettingsOutputTypeDef"]
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

    Name = field("Name")
    LanguageCode = field("LanguageCode")
    SelectorSettings = field("SelectorSettings")

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
class VideoDescriptionOutput:
    boto3_raw_data: "type_defs.VideoDescriptionOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def CodecSettings(self):  # pragma: no cover
        return VideoCodecSettingsOutput.make_one(self.boto3_raw_data["CodecSettings"])

    Height = field("Height")
    RespondToAfd = field("RespondToAfd")
    ScalingBehavior = field("ScalingBehavior")
    Sharpness = field("Sharpness")
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

    Name = field("Name")

    @cached_property
    def CodecSettings(self):  # pragma: no cover
        return VideoCodecSettings.make_one(self.boto3_raw_data["CodecSettings"])

    Height = field("Height")
    RespondToAfd = field("RespondToAfd")
    ScalingBehavior = field("ScalingBehavior")
    Sharpness = field("Sharpness")
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
class DescribeInputResponse:
    boto3_raw_data: "type_defs.DescribeInputResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AttachedChannels = field("AttachedChannels")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return InputDestination.make_many(self.boto3_raw_data["Destinations"])

    Id = field("Id")
    InputClass = field("InputClass")

    @cached_property
    def InputDevices(self):  # pragma: no cover
        return InputDeviceSettings.make_many(self.boto3_raw_data["InputDevices"])

    InputPartnerIds = field("InputPartnerIds")
    InputSourceType = field("InputSourceType")

    @cached_property
    def MediaConnectFlows(self):  # pragma: no cover
        return MediaConnectFlow.make_many(self.boto3_raw_data["MediaConnectFlows"])

    Name = field("Name")
    RoleArn = field("RoleArn")
    SecurityGroups = field("SecurityGroups")

    @cached_property
    def Sources(self):  # pragma: no cover
        return InputSource.make_many(self.boto3_raw_data["Sources"])

    State = field("State")
    Tags = field("Tags")
    Type = field("Type")

    @cached_property
    def SrtSettings(self):  # pragma: no cover
        return SrtSettings.make_one(self.boto3_raw_data["SrtSettings"])

    InputNetworkLocation = field("InputNetworkLocation")

    @cached_property
    def MulticastSettings(self):  # pragma: no cover
        return MulticastSettings.make_one(self.boto3_raw_data["MulticastSettings"])

    @cached_property
    def Smpte2110ReceiverGroupSettings(self):  # pragma: no cover
        return Smpte2110ReceiverGroupSettingsOutput.make_one(
            self.boto3_raw_data["Smpte2110ReceiverGroupSettings"]
        )

    SdiSources = field("SdiSources")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Input:
    boto3_raw_data: "type_defs.InputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AttachedChannels = field("AttachedChannels")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return InputDestination.make_many(self.boto3_raw_data["Destinations"])

    Id = field("Id")
    InputClass = field("InputClass")

    @cached_property
    def InputDevices(self):  # pragma: no cover
        return InputDeviceSettings.make_many(self.boto3_raw_data["InputDevices"])

    InputPartnerIds = field("InputPartnerIds")
    InputSourceType = field("InputSourceType")

    @cached_property
    def MediaConnectFlows(self):  # pragma: no cover
        return MediaConnectFlow.make_many(self.boto3_raw_data["MediaConnectFlows"])

    Name = field("Name")
    RoleArn = field("RoleArn")
    SecurityGroups = field("SecurityGroups")

    @cached_property
    def Sources(self):  # pragma: no cover
        return InputSource.make_many(self.boto3_raw_data["Sources"])

    State = field("State")
    Tags = field("Tags")
    Type = field("Type")

    @cached_property
    def SrtSettings(self):  # pragma: no cover
        return SrtSettings.make_one(self.boto3_raw_data["SrtSettings"])

    InputNetworkLocation = field("InputNetworkLocation")

    @cached_property
    def MulticastSettings(self):  # pragma: no cover
        return MulticastSettings.make_one(self.boto3_raw_data["MulticastSettings"])

    @cached_property
    def Smpte2110ReceiverGroupSettings(self):  # pragma: no cover
        return Smpte2110ReceiverGroupSettingsOutput.make_one(
            self.boto3_raw_data["Smpte2110ReceiverGroupSettings"]
        )

    SdiSources = field("SdiSources")

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
class OutputSettingsOutput:
    boto3_raw_data: "type_defs.OutputSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ArchiveOutputSettings(self):  # pragma: no cover
        return ArchiveOutputSettingsOutput.make_one(
            self.boto3_raw_data["ArchiveOutputSettings"]
        )

    @cached_property
    def FrameCaptureOutputSettings(self):  # pragma: no cover
        return FrameCaptureOutputSettings.make_one(
            self.boto3_raw_data["FrameCaptureOutputSettings"]
        )

    @cached_property
    def HlsOutputSettings(self):  # pragma: no cover
        return HlsOutputSettingsOutput.make_one(
            self.boto3_raw_data["HlsOutputSettings"]
        )

    @cached_property
    def MediaPackageOutputSettings(self):  # pragma: no cover
        return MediaPackageOutputSettings.make_one(
            self.boto3_raw_data["MediaPackageOutputSettings"]
        )

    @cached_property
    def MsSmoothOutputSettings(self):  # pragma: no cover
        return MsSmoothOutputSettings.make_one(
            self.boto3_raw_data["MsSmoothOutputSettings"]
        )

    @cached_property
    def MultiplexOutputSettings(self):  # pragma: no cover
        return MultiplexOutputSettings.make_one(
            self.boto3_raw_data["MultiplexOutputSettings"]
        )

    @cached_property
    def RtmpOutputSettings(self):  # pragma: no cover
        return RtmpOutputSettings.make_one(self.boto3_raw_data["RtmpOutputSettings"])

    @cached_property
    def UdpOutputSettings(self):  # pragma: no cover
        return UdpOutputSettings.make_one(self.boto3_raw_data["UdpOutputSettings"])

    @cached_property
    def CmafIngestOutputSettings(self):  # pragma: no cover
        return CmafIngestOutputSettings.make_one(
            self.boto3_raw_data["CmafIngestOutputSettings"]
        )

    @cached_property
    def SrtOutputSettings(self):  # pragma: no cover
        return SrtOutputSettings.make_one(self.boto3_raw_data["SrtOutputSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputSettingsOutputTypeDef"]
        ],
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
    def ArchiveOutputSettings(self):  # pragma: no cover
        return ArchiveOutputSettings.make_one(
            self.boto3_raw_data["ArchiveOutputSettings"]
        )

    @cached_property
    def FrameCaptureOutputSettings(self):  # pragma: no cover
        return FrameCaptureOutputSettings.make_one(
            self.boto3_raw_data["FrameCaptureOutputSettings"]
        )

    @cached_property
    def HlsOutputSettings(self):  # pragma: no cover
        return HlsOutputSettings.make_one(self.boto3_raw_data["HlsOutputSettings"])

    @cached_property
    def MediaPackageOutputSettings(self):  # pragma: no cover
        return MediaPackageOutputSettings.make_one(
            self.boto3_raw_data["MediaPackageOutputSettings"]
        )

    @cached_property
    def MsSmoothOutputSettings(self):  # pragma: no cover
        return MsSmoothOutputSettings.make_one(
            self.boto3_raw_data["MsSmoothOutputSettings"]
        )

    @cached_property
    def MultiplexOutputSettings(self):  # pragma: no cover
        return MultiplexOutputSettings.make_one(
            self.boto3_raw_data["MultiplexOutputSettings"]
        )

    @cached_property
    def RtmpOutputSettings(self):  # pragma: no cover
        return RtmpOutputSettings.make_one(self.boto3_raw_data["RtmpOutputSettings"])

    @cached_property
    def UdpOutputSettings(self):  # pragma: no cover
        return UdpOutputSettings.make_one(self.boto3_raw_data["UdpOutputSettings"])

    @cached_property
    def CmafIngestOutputSettings(self):  # pragma: no cover
        return CmafIngestOutputSettings.make_one(
            self.boto3_raw_data["CmafIngestOutputSettings"]
        )

    @cached_property
    def SrtOutputSettings(self):  # pragma: no cover
        return SrtOutputSettings.make_one(self.boto3_raw_data["SrtOutputSettings"])

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
class CreateMultiplexProgramResponse:
    boto3_raw_data: "type_defs.CreateMultiplexProgramResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MultiplexProgram(self):  # pragma: no cover
        return MultiplexProgram.make_one(self.boto3_raw_data["MultiplexProgram"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMultiplexProgramResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiplexProgramResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMultiplexProgramResponse:
    boto3_raw_data: "type_defs.UpdateMultiplexProgramResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MultiplexProgram(self):  # pragma: no cover
        return MultiplexProgram.make_one(self.boto3_raw_data["MultiplexProgram"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMultiplexProgramResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMultiplexProgramResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35TimeSignalScheduleActionSettingsOutput:
    boto3_raw_data: "type_defs.Scte35TimeSignalScheduleActionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Scte35Descriptors(self):  # pragma: no cover
        return Scte35Descriptor.make_many(self.boto3_raw_data["Scte35Descriptors"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Scte35TimeSignalScheduleActionSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35TimeSignalScheduleActionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scte35TimeSignalScheduleActionSettings:
    boto3_raw_data: "type_defs.Scte35TimeSignalScheduleActionSettingsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Scte35Descriptors(self):  # pragma: no cover
        return Scte35Descriptor.make_many(self.boto3_raw_data["Scte35Descriptors"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Scte35TimeSignalScheduleActionSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Scte35TimeSignalScheduleActionSettingsTypeDef"]
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

    Name = field("Name")
    SelectorSettings = field("SelectorSettings")

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
class InputAttachmentOutput:
    boto3_raw_data: "type_defs.InputAttachmentOutputTypeDef" = dataclasses.field()

    @cached_property
    def AutomaticInputFailoverSettings(self):  # pragma: no cover
        return AutomaticInputFailoverSettingsOutput.make_one(
            self.boto3_raw_data["AutomaticInputFailoverSettings"]
        )

    InputAttachmentName = field("InputAttachmentName")
    InputId = field("InputId")

    @cached_property
    def InputSettings(self):  # pragma: no cover
        return InputSettingsOutput.make_one(self.boto3_raw_data["InputSettings"])

    LogicalInterfaceNames = field("LogicalInterfaceNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputAttachmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputAttachmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInputResponse:
    boto3_raw_data: "type_defs.CreateInputResponseTypeDef" = dataclasses.field()

    @cached_property
    def Input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePartnerInputResponse:
    boto3_raw_data: "type_defs.CreatePartnerInputResponseTypeDef" = dataclasses.field()

    @cached_property
    def Input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePartnerInputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePartnerInputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInputsResponse:
    boto3_raw_data: "type_defs.ListInputsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Inputs(self):  # pragma: no cover
        return Input.make_many(self.boto3_raw_data["Inputs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInputsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInputsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInputResponse:
    boto3_raw_data: "type_defs.UpdateInputResponseTypeDef" = dataclasses.field()

    @cached_property
    def Input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInputRequest:
    boto3_raw_data: "type_defs.CreateInputRequestTypeDef" = dataclasses.field()

    @cached_property
    def Destinations(self):  # pragma: no cover
        return InputDestinationRequest.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def InputDevices(self):  # pragma: no cover
        return InputDeviceSettings.make_many(self.boto3_raw_data["InputDevices"])

    InputSecurityGroups = field("InputSecurityGroups")

    @cached_property
    def MediaConnectFlows(self):  # pragma: no cover
        return MediaConnectFlowRequest.make_many(
            self.boto3_raw_data["MediaConnectFlows"]
        )

    Name = field("Name")
    RequestId = field("RequestId")
    RoleArn = field("RoleArn")

    @cached_property
    def Sources(self):  # pragma: no cover
        return InputSourceRequest.make_many(self.boto3_raw_data["Sources"])

    Tags = field("Tags")
    Type = field("Type")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return InputVpcRequest.make_one(self.boto3_raw_data["Vpc"])

    @cached_property
    def SrtSettings(self):  # pragma: no cover
        return SrtSettingsRequest.make_one(self.boto3_raw_data["SrtSettings"])

    InputNetworkLocation = field("InputNetworkLocation")

    @cached_property
    def MulticastSettings(self):  # pragma: no cover
        return MulticastSettingsCreateRequest.make_one(
            self.boto3_raw_data["MulticastSettings"]
        )

    Smpte2110ReceiverGroupSettings = field("Smpte2110ReceiverGroupSettings")
    SdiSources = field("SdiSources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInputRequest:
    boto3_raw_data: "type_defs.UpdateInputRequestTypeDef" = dataclasses.field()

    InputId = field("InputId")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return InputDestinationRequest.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def InputDevices(self):  # pragma: no cover
        return InputDeviceRequest.make_many(self.boto3_raw_data["InputDevices"])

    InputSecurityGroups = field("InputSecurityGroups")

    @cached_property
    def MediaConnectFlows(self):  # pragma: no cover
        return MediaConnectFlowRequest.make_many(
            self.boto3_raw_data["MediaConnectFlows"]
        )

    Name = field("Name")
    RoleArn = field("RoleArn")

    @cached_property
    def Sources(self):  # pragma: no cover
        return InputSourceRequest.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def SrtSettings(self):  # pragma: no cover
        return SrtSettingsRequest.make_one(self.boto3_raw_data["SrtSettings"])

    @cached_property
    def MulticastSettings(self):  # pragma: no cover
        return MulticastSettingsUpdateRequest.make_one(
            self.boto3_raw_data["MulticastSettings"]
        )

    Smpte2110ReceiverGroupSettings = field("Smpte2110ReceiverGroupSettings")
    SdiSources = field("SdiSources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInputRequestTypeDef"]
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
    def OutputSettings(self):  # pragma: no cover
        return OutputSettingsOutput.make_one(self.boto3_raw_data["OutputSettings"])

    AudioDescriptionNames = field("AudioDescriptionNames")
    CaptionDescriptionNames = field("CaptionDescriptionNames")
    OutputName = field("OutputName")
    VideoDescriptionName = field("VideoDescriptionName")

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
class Output:
    boto3_raw_data: "type_defs.OutputTypeDef" = dataclasses.field()

    @cached_property
    def OutputSettings(self):  # pragma: no cover
        return OutputSettings.make_one(self.boto3_raw_data["OutputSettings"])

    AudioDescriptionNames = field("AudioDescriptionNames")
    CaptionDescriptionNames = field("CaptionDescriptionNames")
    OutputName = field("OutputName")
    VideoDescriptionName = field("VideoDescriptionName")

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
class ScheduleActionSettingsOutput:
    boto3_raw_data: "type_defs.ScheduleActionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HlsId3SegmentTaggingSettings(self):  # pragma: no cover
        return HlsId3SegmentTaggingScheduleActionSettings.make_one(
            self.boto3_raw_data["HlsId3SegmentTaggingSettings"]
        )

    @cached_property
    def HlsTimedMetadataSettings(self):  # pragma: no cover
        return HlsTimedMetadataScheduleActionSettings.make_one(
            self.boto3_raw_data["HlsTimedMetadataSettings"]
        )

    @cached_property
    def InputPrepareSettings(self):  # pragma: no cover
        return InputPrepareScheduleActionSettingsOutput.make_one(
            self.boto3_raw_data["InputPrepareSettings"]
        )

    @cached_property
    def InputSwitchSettings(self):  # pragma: no cover
        return InputSwitchScheduleActionSettingsOutput.make_one(
            self.boto3_raw_data["InputSwitchSettings"]
        )

    @cached_property
    def MotionGraphicsImageActivateSettings(self):  # pragma: no cover
        return MotionGraphicsActivateScheduleActionSettings.make_one(
            self.boto3_raw_data["MotionGraphicsImageActivateSettings"]
        )

    MotionGraphicsImageDeactivateSettings = field(
        "MotionGraphicsImageDeactivateSettings"
    )

    @cached_property
    def PauseStateSettings(self):  # pragma: no cover
        return PauseStateScheduleActionSettingsOutput.make_one(
            self.boto3_raw_data["PauseStateSettings"]
        )

    @cached_property
    def Scte35InputSettings(self):  # pragma: no cover
        return Scte35InputScheduleActionSettings.make_one(
            self.boto3_raw_data["Scte35InputSettings"]
        )

    @cached_property
    def Scte35ReturnToNetworkSettings(self):  # pragma: no cover
        return Scte35ReturnToNetworkScheduleActionSettings.make_one(
            self.boto3_raw_data["Scte35ReturnToNetworkSettings"]
        )

    @cached_property
    def Scte35SpliceInsertSettings(self):  # pragma: no cover
        return Scte35SpliceInsertScheduleActionSettings.make_one(
            self.boto3_raw_data["Scte35SpliceInsertSettings"]
        )

    @cached_property
    def Scte35TimeSignalSettings(self):  # pragma: no cover
        return Scte35TimeSignalScheduleActionSettingsOutput.make_one(
            self.boto3_raw_data["Scte35TimeSignalSettings"]
        )

    @cached_property
    def StaticImageActivateSettings(self):  # pragma: no cover
        return StaticImageActivateScheduleActionSettings.make_one(
            self.boto3_raw_data["StaticImageActivateSettings"]
        )

    @cached_property
    def StaticImageDeactivateSettings(self):  # pragma: no cover
        return StaticImageDeactivateScheduleActionSettings.make_one(
            self.boto3_raw_data["StaticImageDeactivateSettings"]
        )

    @cached_property
    def StaticImageOutputActivateSettings(self):  # pragma: no cover
        return StaticImageOutputActivateScheduleActionSettingsOutput.make_one(
            self.boto3_raw_data["StaticImageOutputActivateSettings"]
        )

    @cached_property
    def StaticImageOutputDeactivateSettings(self):  # pragma: no cover
        return StaticImageOutputDeactivateScheduleActionSettingsOutput.make_one(
            self.boto3_raw_data["StaticImageOutputDeactivateSettings"]
        )

    @cached_property
    def Id3SegmentTaggingSettings(self):  # pragma: no cover
        return Id3SegmentTaggingScheduleActionSettings.make_one(
            self.boto3_raw_data["Id3SegmentTaggingSettings"]
        )

    @cached_property
    def TimedMetadataSettings(self):  # pragma: no cover
        return TimedMetadataScheduleActionSettings.make_one(
            self.boto3_raw_data["TimedMetadataSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleActionSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleActionSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelSummary:
    boto3_raw_data: "type_defs.ChannelSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def CdiInputSpecification(self):  # pragma: no cover
        return CdiInputSpecification.make_one(
            self.boto3_raw_data["CdiInputSpecification"]
        )

    ChannelClass = field("ChannelClass")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return OutputDestinationOutput.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def EgressEndpoints(self):  # pragma: no cover
        return ChannelEgressEndpoint.make_many(self.boto3_raw_data["EgressEndpoints"])

    Id = field("Id")

    @cached_property
    def InputAttachments(self):  # pragma: no cover
        return InputAttachmentOutput.make_many(self.boto3_raw_data["InputAttachments"])

    @cached_property
    def InputSpecification(self):  # pragma: no cover
        return InputSpecification.make_one(self.boto3_raw_data["InputSpecification"])

    LogLevel = field("LogLevel")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return MaintenanceStatus.make_one(self.boto3_raw_data["Maintenance"])

    Name = field("Name")
    PipelinesRunningCount = field("PipelinesRunningCount")
    RoleArn = field("RoleArn")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return VpcOutputSettingsDescription.make_one(self.boto3_raw_data["Vpc"])

    @cached_property
    def AnywhereSettings(self):  # pragma: no cover
        return DescribeAnywhereSettings.make_one(
            self.boto3_raw_data["AnywhereSettings"]
        )

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    @cached_property
    def UsedChannelEngineVersions(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_many(
            self.boto3_raw_data["UsedChannelEngineVersions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelSummaryTypeDef"]],
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
    def OutputGroupSettings(self):  # pragma: no cover
        return OutputGroupSettingsOutput.make_one(
            self.boto3_raw_data["OutputGroupSettings"]
        )

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Extra.make_many(self.boto3_raw_data["Outputs"])

    Name = field("Name")

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
class OutputGroup:
    boto3_raw_data: "type_defs.OutputGroupTypeDef" = dataclasses.field()

    @cached_property
    def OutputGroupSettings(self):  # pragma: no cover
        return OutputGroupSettings.make_one(self.boto3_raw_data["OutputGroupSettings"])

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["Outputs"])

    Name = field("Name")

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
class ScheduleActionOutput:
    boto3_raw_data: "type_defs.ScheduleActionOutputTypeDef" = dataclasses.field()

    ActionName = field("ActionName")

    @cached_property
    def ScheduleActionSettings(self):  # pragma: no cover
        return ScheduleActionSettingsOutput.make_one(
            self.boto3_raw_data["ScheduleActionSettings"]
        )

    @cached_property
    def ScheduleActionStartSettings(self):  # pragma: no cover
        return ScheduleActionStartSettingsOutput.make_one(
            self.boto3_raw_data["ScheduleActionStartSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleActionSettings:
    boto3_raw_data: "type_defs.ScheduleActionSettingsTypeDef" = dataclasses.field()

    @cached_property
    def HlsId3SegmentTaggingSettings(self):  # pragma: no cover
        return HlsId3SegmentTaggingScheduleActionSettings.make_one(
            self.boto3_raw_data["HlsId3SegmentTaggingSettings"]
        )

    @cached_property
    def HlsTimedMetadataSettings(self):  # pragma: no cover
        return HlsTimedMetadataScheduleActionSettings.make_one(
            self.boto3_raw_data["HlsTimedMetadataSettings"]
        )

    InputPrepareSettings = field("InputPrepareSettings")
    InputSwitchSettings = field("InputSwitchSettings")

    @cached_property
    def MotionGraphicsImageActivateSettings(self):  # pragma: no cover
        return MotionGraphicsActivateScheduleActionSettings.make_one(
            self.boto3_raw_data["MotionGraphicsImageActivateSettings"]
        )

    MotionGraphicsImageDeactivateSettings = field(
        "MotionGraphicsImageDeactivateSettings"
    )
    PauseStateSettings = field("PauseStateSettings")

    @cached_property
    def Scte35InputSettings(self):  # pragma: no cover
        return Scte35InputScheduleActionSettings.make_one(
            self.boto3_raw_data["Scte35InputSettings"]
        )

    @cached_property
    def Scte35ReturnToNetworkSettings(self):  # pragma: no cover
        return Scte35ReturnToNetworkScheduleActionSettings.make_one(
            self.boto3_raw_data["Scte35ReturnToNetworkSettings"]
        )

    @cached_property
    def Scte35SpliceInsertSettings(self):  # pragma: no cover
        return Scte35SpliceInsertScheduleActionSettings.make_one(
            self.boto3_raw_data["Scte35SpliceInsertSettings"]
        )

    Scte35TimeSignalSettings = field("Scte35TimeSignalSettings")

    @cached_property
    def StaticImageActivateSettings(self):  # pragma: no cover
        return StaticImageActivateScheduleActionSettings.make_one(
            self.boto3_raw_data["StaticImageActivateSettings"]
        )

    @cached_property
    def StaticImageDeactivateSettings(self):  # pragma: no cover
        return StaticImageDeactivateScheduleActionSettings.make_one(
            self.boto3_raw_data["StaticImageDeactivateSettings"]
        )

    StaticImageOutputActivateSettings = field("StaticImageOutputActivateSettings")
    StaticImageOutputDeactivateSettings = field("StaticImageOutputDeactivateSettings")

    @cached_property
    def Id3SegmentTaggingSettings(self):  # pragma: no cover
        return Id3SegmentTaggingScheduleActionSettings.make_one(
            self.boto3_raw_data["Id3SegmentTaggingSettings"]
        )

    @cached_property
    def TimedMetadataSettings(self):  # pragma: no cover
        return TimedMetadataScheduleActionSettings.make_one(
            self.boto3_raw_data["TimedMetadataSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleActionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleActionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSettings:
    boto3_raw_data: "type_defs.InputSettingsTypeDef" = dataclasses.field()

    AudioSelectors = field("AudioSelectors")
    CaptionSelectors = field("CaptionSelectors")
    DeblockFilter = field("DeblockFilter")
    DenoiseFilter = field("DenoiseFilter")
    FilterStrength = field("FilterStrength")
    InputFilter = field("InputFilter")

    @cached_property
    def NetworkInputSettings(self):  # pragma: no cover
        return NetworkInputSettings.make_one(
            self.boto3_raw_data["NetworkInputSettings"]
        )

    Scte35Pid = field("Scte35Pid")
    Smpte2038DataPreference = field("Smpte2038DataPreference")
    SourceEndBehavior = field("SourceEndBehavior")

    @cached_property
    def VideoSelector(self):  # pragma: no cover
        return VideoSelector.make_one(self.boto3_raw_data["VideoSelector"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsResponse:
    boto3_raw_data: "type_defs.ListChannelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Channels(self):  # pragma: no cover
        return ChannelSummary.make_many(self.boto3_raw_data["Channels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncoderSettingsOutput:
    boto3_raw_data: "type_defs.EncoderSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AudioDescriptions(self):  # pragma: no cover
        return AudioDescriptionOutput.make_many(
            self.boto3_raw_data["AudioDescriptions"]
        )

    @cached_property
    def OutputGroups(self):  # pragma: no cover
        return OutputGroupOutput.make_many(self.boto3_raw_data["OutputGroups"])

    @cached_property
    def TimecodeConfig(self):  # pragma: no cover
        return TimecodeConfig.make_one(self.boto3_raw_data["TimecodeConfig"])

    @cached_property
    def VideoDescriptions(self):  # pragma: no cover
        return VideoDescriptionOutput.make_many(
            self.boto3_raw_data["VideoDescriptions"]
        )

    @cached_property
    def AvailBlanking(self):  # pragma: no cover
        return AvailBlanking.make_one(self.boto3_raw_data["AvailBlanking"])

    @cached_property
    def AvailConfiguration(self):  # pragma: no cover
        return AvailConfiguration.make_one(self.boto3_raw_data["AvailConfiguration"])

    @cached_property
    def BlackoutSlate(self):  # pragma: no cover
        return BlackoutSlate.make_one(self.boto3_raw_data["BlackoutSlate"])

    @cached_property
    def CaptionDescriptions(self):  # pragma: no cover
        return CaptionDescriptionOutput.make_many(
            self.boto3_raw_data["CaptionDescriptions"]
        )

    @cached_property
    def FeatureActivations(self):  # pragma: no cover
        return FeatureActivations.make_one(self.boto3_raw_data["FeatureActivations"])

    @cached_property
    def GlobalConfiguration(self):  # pragma: no cover
        return GlobalConfigurationOutput.make_one(
            self.boto3_raw_data["GlobalConfiguration"]
        )

    @cached_property
    def MotionGraphicsConfiguration(self):  # pragma: no cover
        return MotionGraphicsConfigurationOutput.make_one(
            self.boto3_raw_data["MotionGraphicsConfiguration"]
        )

    @cached_property
    def NielsenConfiguration(self):  # pragma: no cover
        return NielsenConfiguration.make_one(
            self.boto3_raw_data["NielsenConfiguration"]
        )

    @cached_property
    def ThumbnailConfiguration(self):  # pragma: no cover
        return ThumbnailConfiguration.make_one(
            self.boto3_raw_data["ThumbnailConfiguration"]
        )

    @cached_property
    def ColorCorrectionSettings(self):  # pragma: no cover
        return ColorCorrectionSettingsOutput.make_one(
            self.boto3_raw_data["ColorCorrectionSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncoderSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncoderSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncoderSettings:
    boto3_raw_data: "type_defs.EncoderSettingsTypeDef" = dataclasses.field()

    @cached_property
    def AudioDescriptions(self):  # pragma: no cover
        return AudioDescription.make_many(self.boto3_raw_data["AudioDescriptions"])

    @cached_property
    def OutputGroups(self):  # pragma: no cover
        return OutputGroup.make_many(self.boto3_raw_data["OutputGroups"])

    @cached_property
    def TimecodeConfig(self):  # pragma: no cover
        return TimecodeConfig.make_one(self.boto3_raw_data["TimecodeConfig"])

    @cached_property
    def VideoDescriptions(self):  # pragma: no cover
        return VideoDescription.make_many(self.boto3_raw_data["VideoDescriptions"])

    @cached_property
    def AvailBlanking(self):  # pragma: no cover
        return AvailBlanking.make_one(self.boto3_raw_data["AvailBlanking"])

    @cached_property
    def AvailConfiguration(self):  # pragma: no cover
        return AvailConfiguration.make_one(self.boto3_raw_data["AvailConfiguration"])

    @cached_property
    def BlackoutSlate(self):  # pragma: no cover
        return BlackoutSlate.make_one(self.boto3_raw_data["BlackoutSlate"])

    @cached_property
    def CaptionDescriptions(self):  # pragma: no cover
        return CaptionDescription.make_many(self.boto3_raw_data["CaptionDescriptions"])

    @cached_property
    def FeatureActivations(self):  # pragma: no cover
        return FeatureActivations.make_one(self.boto3_raw_data["FeatureActivations"])

    @cached_property
    def GlobalConfiguration(self):  # pragma: no cover
        return GlobalConfiguration.make_one(self.boto3_raw_data["GlobalConfiguration"])

    @cached_property
    def MotionGraphicsConfiguration(self):  # pragma: no cover
        return MotionGraphicsConfiguration.make_one(
            self.boto3_raw_data["MotionGraphicsConfiguration"]
        )

    @cached_property
    def NielsenConfiguration(self):  # pragma: no cover
        return NielsenConfiguration.make_one(
            self.boto3_raw_data["NielsenConfiguration"]
        )

    @cached_property
    def ThumbnailConfiguration(self):  # pragma: no cover
        return ThumbnailConfiguration.make_one(
            self.boto3_raw_data["ThumbnailConfiguration"]
        )

    @cached_property
    def ColorCorrectionSettings(self):  # pragma: no cover
        return ColorCorrectionSettings.make_one(
            self.boto3_raw_data["ColorCorrectionSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncoderSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncoderSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchScheduleActionCreateResult:
    boto3_raw_data: "type_defs.BatchScheduleActionCreateResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScheduleActions(self):  # pragma: no cover
        return ScheduleActionOutput.make_many(self.boto3_raw_data["ScheduleActions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchScheduleActionCreateResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchScheduleActionCreateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchScheduleActionDeleteResult:
    boto3_raw_data: "type_defs.BatchScheduleActionDeleteResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScheduleActions(self):  # pragma: no cover
        return ScheduleActionOutput.make_many(self.boto3_raw_data["ScheduleActions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchScheduleActionDeleteResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchScheduleActionDeleteResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduleResponse:
    boto3_raw_data: "type_defs.DescribeScheduleResponseTypeDef" = dataclasses.field()

    @cached_property
    def ScheduleActions(self):  # pragma: no cover
        return ScheduleActionOutput.make_many(self.boto3_raw_data["ScheduleActions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Channel:
    boto3_raw_data: "type_defs.ChannelTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def CdiInputSpecification(self):  # pragma: no cover
        return CdiInputSpecification.make_one(
            self.boto3_raw_data["CdiInputSpecification"]
        )

    ChannelClass = field("ChannelClass")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return OutputDestinationOutput.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def EgressEndpoints(self):  # pragma: no cover
        return ChannelEgressEndpoint.make_many(self.boto3_raw_data["EgressEndpoints"])

    @cached_property
    def EncoderSettings(self):  # pragma: no cover
        return EncoderSettingsOutput.make_one(self.boto3_raw_data["EncoderSettings"])

    Id = field("Id")

    @cached_property
    def InputAttachments(self):  # pragma: no cover
        return InputAttachmentOutput.make_many(self.boto3_raw_data["InputAttachments"])

    @cached_property
    def InputSpecification(self):  # pragma: no cover
        return InputSpecification.make_one(self.boto3_raw_data["InputSpecification"])

    LogLevel = field("LogLevel")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return MaintenanceStatus.make_one(self.boto3_raw_data["Maintenance"])

    Name = field("Name")

    @cached_property
    def PipelineDetails(self):  # pragma: no cover
        return PipelineDetail.make_many(self.boto3_raw_data["PipelineDetails"])

    PipelinesRunningCount = field("PipelinesRunningCount")
    RoleArn = field("RoleArn")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return VpcOutputSettingsDescription.make_one(self.boto3_raw_data["Vpc"])

    @cached_property
    def AnywhereSettings(self):  # pragma: no cover
        return DescribeAnywhereSettings.make_one(
            self.boto3_raw_data["AnywhereSettings"]
        )

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelResponse:
    boto3_raw_data: "type_defs.DeleteChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def CdiInputSpecification(self):  # pragma: no cover
        return CdiInputSpecification.make_one(
            self.boto3_raw_data["CdiInputSpecification"]
        )

    ChannelClass = field("ChannelClass")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return OutputDestinationOutput.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def EgressEndpoints(self):  # pragma: no cover
        return ChannelEgressEndpoint.make_many(self.boto3_raw_data["EgressEndpoints"])

    @cached_property
    def EncoderSettings(self):  # pragma: no cover
        return EncoderSettingsOutput.make_one(self.boto3_raw_data["EncoderSettings"])

    Id = field("Id")

    @cached_property
    def InputAttachments(self):  # pragma: no cover
        return InputAttachmentOutput.make_many(self.boto3_raw_data["InputAttachments"])

    @cached_property
    def InputSpecification(self):  # pragma: no cover
        return InputSpecification.make_one(self.boto3_raw_data["InputSpecification"])

    LogLevel = field("LogLevel")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return MaintenanceStatus.make_one(self.boto3_raw_data["Maintenance"])

    Name = field("Name")

    @cached_property
    def PipelineDetails(self):  # pragma: no cover
        return PipelineDetail.make_many(self.boto3_raw_data["PipelineDetails"])

    PipelinesRunningCount = field("PipelinesRunningCount")
    RoleArn = field("RoleArn")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return VpcOutputSettingsDescription.make_one(self.boto3_raw_data["Vpc"])

    @cached_property
    def AnywhereSettings(self):  # pragma: no cover
        return DescribeAnywhereSettings.make_one(
            self.boto3_raw_data["AnywhereSettings"]
        )

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelResponse:
    boto3_raw_data: "type_defs.DescribeChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def CdiInputSpecification(self):  # pragma: no cover
        return CdiInputSpecification.make_one(
            self.boto3_raw_data["CdiInputSpecification"]
        )

    ChannelClass = field("ChannelClass")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return OutputDestinationOutput.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def EgressEndpoints(self):  # pragma: no cover
        return ChannelEgressEndpoint.make_many(self.boto3_raw_data["EgressEndpoints"])

    @cached_property
    def EncoderSettings(self):  # pragma: no cover
        return EncoderSettingsOutput.make_one(self.boto3_raw_data["EncoderSettings"])

    Id = field("Id")

    @cached_property
    def InputAttachments(self):  # pragma: no cover
        return InputAttachmentOutput.make_many(self.boto3_raw_data["InputAttachments"])

    @cached_property
    def InputSpecification(self):  # pragma: no cover
        return InputSpecification.make_one(self.boto3_raw_data["InputSpecification"])

    LogLevel = field("LogLevel")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return MaintenanceStatus.make_one(self.boto3_raw_data["Maintenance"])

    Name = field("Name")

    @cached_property
    def PipelineDetails(self):  # pragma: no cover
        return PipelineDetail.make_many(self.boto3_raw_data["PipelineDetails"])

    PipelinesRunningCount = field("PipelinesRunningCount")
    RoleArn = field("RoleArn")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return VpcOutputSettingsDescription.make_one(self.boto3_raw_data["Vpc"])

    @cached_property
    def AnywhereSettings(self):  # pragma: no cover
        return DescribeAnywhereSettings.make_one(
            self.boto3_raw_data["AnywhereSettings"]
        )

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestartChannelPipelinesResponse:
    boto3_raw_data: "type_defs.RestartChannelPipelinesResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def CdiInputSpecification(self):  # pragma: no cover
        return CdiInputSpecification.make_one(
            self.boto3_raw_data["CdiInputSpecification"]
        )

    ChannelClass = field("ChannelClass")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return OutputDestinationOutput.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def EgressEndpoints(self):  # pragma: no cover
        return ChannelEgressEndpoint.make_many(self.boto3_raw_data["EgressEndpoints"])

    @cached_property
    def EncoderSettings(self):  # pragma: no cover
        return EncoderSettingsOutput.make_one(self.boto3_raw_data["EncoderSettings"])

    Id = field("Id")

    @cached_property
    def InputAttachments(self):  # pragma: no cover
        return InputAttachmentOutput.make_many(self.boto3_raw_data["InputAttachments"])

    @cached_property
    def InputSpecification(self):  # pragma: no cover
        return InputSpecification.make_one(self.boto3_raw_data["InputSpecification"])

    LogLevel = field("LogLevel")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return MaintenanceStatus.make_one(self.boto3_raw_data["Maintenance"])

    MaintenanceStatus = field("MaintenanceStatus")
    Name = field("Name")

    @cached_property
    def PipelineDetails(self):  # pragma: no cover
        return PipelineDetail.make_many(self.boto3_raw_data["PipelineDetails"])

    PipelinesRunningCount = field("PipelinesRunningCount")
    RoleArn = field("RoleArn")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return VpcOutputSettingsDescription.make_one(self.boto3_raw_data["Vpc"])

    @cached_property
    def AnywhereSettings(self):  # pragma: no cover
        return DescribeAnywhereSettings.make_one(
            self.boto3_raw_data["AnywhereSettings"]
        )

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestartChannelPipelinesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestartChannelPipelinesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChannelResponse:
    boto3_raw_data: "type_defs.StartChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def CdiInputSpecification(self):  # pragma: no cover
        return CdiInputSpecification.make_one(
            self.boto3_raw_data["CdiInputSpecification"]
        )

    ChannelClass = field("ChannelClass")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return OutputDestinationOutput.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def EgressEndpoints(self):  # pragma: no cover
        return ChannelEgressEndpoint.make_many(self.boto3_raw_data["EgressEndpoints"])

    @cached_property
    def EncoderSettings(self):  # pragma: no cover
        return EncoderSettingsOutput.make_one(self.boto3_raw_data["EncoderSettings"])

    Id = field("Id")

    @cached_property
    def InputAttachments(self):  # pragma: no cover
        return InputAttachmentOutput.make_many(self.boto3_raw_data["InputAttachments"])

    @cached_property
    def InputSpecification(self):  # pragma: no cover
        return InputSpecification.make_one(self.boto3_raw_data["InputSpecification"])

    LogLevel = field("LogLevel")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return MaintenanceStatus.make_one(self.boto3_raw_data["Maintenance"])

    Name = field("Name")

    @cached_property
    def PipelineDetails(self):  # pragma: no cover
        return PipelineDetail.make_many(self.boto3_raw_data["PipelineDetails"])

    PipelinesRunningCount = field("PipelinesRunningCount")
    RoleArn = field("RoleArn")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return VpcOutputSettingsDescription.make_one(self.boto3_raw_data["Vpc"])

    @cached_property
    def AnywhereSettings(self):  # pragma: no cover
        return DescribeAnywhereSettings.make_one(
            self.boto3_raw_data["AnywhereSettings"]
        )

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopChannelResponse:
    boto3_raw_data: "type_defs.StopChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def CdiInputSpecification(self):  # pragma: no cover
        return CdiInputSpecification.make_one(
            self.boto3_raw_data["CdiInputSpecification"]
        )

    ChannelClass = field("ChannelClass")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return OutputDestinationOutput.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def EgressEndpoints(self):  # pragma: no cover
        return ChannelEgressEndpoint.make_many(self.boto3_raw_data["EgressEndpoints"])

    @cached_property
    def EncoderSettings(self):  # pragma: no cover
        return EncoderSettingsOutput.make_one(self.boto3_raw_data["EncoderSettings"])

    Id = field("Id")

    @cached_property
    def InputAttachments(self):  # pragma: no cover
        return InputAttachmentOutput.make_many(self.boto3_raw_data["InputAttachments"])

    @cached_property
    def InputSpecification(self):  # pragma: no cover
        return InputSpecification.make_one(self.boto3_raw_data["InputSpecification"])

    LogLevel = field("LogLevel")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return MaintenanceStatus.make_one(self.boto3_raw_data["Maintenance"])

    Name = field("Name")

    @cached_property
    def PipelineDetails(self):  # pragma: no cover
        return PipelineDetail.make_many(self.boto3_raw_data["PipelineDetails"])

    PipelinesRunningCount = field("PipelinesRunningCount")
    RoleArn = field("RoleArn")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return VpcOutputSettingsDescription.make_one(self.boto3_raw_data["Vpc"])

    @cached_property
    def AnywhereSettings(self):  # pragma: no cover
        return DescribeAnywhereSettings.make_one(
            self.boto3_raw_data["AnywhereSettings"]
        )

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionResponse.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateScheduleResponse:
    boto3_raw_data: "type_defs.BatchUpdateScheduleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Creates(self):  # pragma: no cover
        return BatchScheduleActionCreateResult.make_one(self.boto3_raw_data["Creates"])

    @cached_property
    def Deletes(self):  # pragma: no cover
        return BatchScheduleActionDeleteResult.make_one(self.boto3_raw_data["Deletes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleAction:
    boto3_raw_data: "type_defs.ScheduleActionTypeDef" = dataclasses.field()

    ActionName = field("ActionName")
    ScheduleActionSettings = field("ScheduleActionSettings")
    ScheduleActionStartSettings = field("ScheduleActionStartSettings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputAttachment:
    boto3_raw_data: "type_defs.InputAttachmentTypeDef" = dataclasses.field()

    AutomaticInputFailoverSettings = field("AutomaticInputFailoverSettings")
    InputAttachmentName = field("InputAttachmentName")
    InputId = field("InputId")
    InputSettings = field("InputSettings")
    LogicalInterfaceNames = field("LogicalInterfaceNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputAttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputAttachmentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelResponse:
    boto3_raw_data: "type_defs.CreateChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def Channel(self):  # pragma: no cover
        return Channel.make_one(self.boto3_raw_data["Channel"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelClassResponse:
    boto3_raw_data: "type_defs.UpdateChannelClassResponseTypeDef" = dataclasses.field()

    @cached_property
    def Channel(self):  # pragma: no cover
        return Channel.make_one(self.boto3_raw_data["Channel"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelClassResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelClassResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelResponse:
    boto3_raw_data: "type_defs.UpdateChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def Channel(self):  # pragma: no cover
        return Channel.make_one(self.boto3_raw_data["Channel"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchScheduleActionCreateRequest:
    boto3_raw_data: "type_defs.BatchScheduleActionCreateRequestTypeDef" = (
        dataclasses.field()
    )

    ScheduleActions = field("ScheduleActions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchScheduleActionCreateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchScheduleActionCreateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelRequest:
    boto3_raw_data: "type_defs.CreateChannelRequestTypeDef" = dataclasses.field()

    @cached_property
    def CdiInputSpecification(self):  # pragma: no cover
        return CdiInputSpecification.make_one(
            self.boto3_raw_data["CdiInputSpecification"]
        )

    ChannelClass = field("ChannelClass")
    Destinations = field("Destinations")
    EncoderSettings = field("EncoderSettings")
    InputAttachments = field("InputAttachments")

    @cached_property
    def InputSpecification(self):  # pragma: no cover
        return InputSpecification.make_one(self.boto3_raw_data["InputSpecification"])

    LogLevel = field("LogLevel")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return MaintenanceCreateSettings.make_one(self.boto3_raw_data["Maintenance"])

    Name = field("Name")
    RequestId = field("RequestId")
    Reserved = field("Reserved")
    RoleArn = field("RoleArn")
    Tags = field("Tags")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return VpcOutputSettings.make_one(self.boto3_raw_data["Vpc"])

    @cached_property
    def AnywhereSettings(self):  # pragma: no cover
        return AnywhereSettings.make_one(self.boto3_raw_data["AnywhereSettings"])

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionRequest.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelRequest:
    boto3_raw_data: "type_defs.UpdateChannelRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")

    @cached_property
    def CdiInputSpecification(self):  # pragma: no cover
        return CdiInputSpecification.make_one(
            self.boto3_raw_data["CdiInputSpecification"]
        )

    Destinations = field("Destinations")
    EncoderSettings = field("EncoderSettings")
    InputAttachments = field("InputAttachments")

    @cached_property
    def InputSpecification(self):  # pragma: no cover
        return InputSpecification.make_one(self.boto3_raw_data["InputSpecification"])

    LogLevel = field("LogLevel")

    @cached_property
    def Maintenance(self):  # pragma: no cover
        return MaintenanceUpdateSettings.make_one(self.boto3_raw_data["Maintenance"])

    Name = field("Name")
    RoleArn = field("RoleArn")

    @cached_property
    def ChannelEngineVersion(self):  # pragma: no cover
        return ChannelEngineVersionRequest.make_one(
            self.boto3_raw_data["ChannelEngineVersion"]
        )

    DryRun = field("DryRun")

    @cached_property
    def AnywhereSettings(self):  # pragma: no cover
        return AnywhereSettings.make_one(self.boto3_raw_data["AnywhereSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateScheduleRequest:
    boto3_raw_data: "type_defs.BatchUpdateScheduleRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")

    @cached_property
    def Creates(self):  # pragma: no cover
        return BatchScheduleActionCreateRequest.make_one(self.boto3_raw_data["Creates"])

    @cached_property
    def Deletes(self):  # pragma: no cover
        return BatchScheduleActionDeleteRequest.make_one(self.boto3_raw_data["Deletes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
