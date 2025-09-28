# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_storagegateway import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
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
class AddCacheInput:
    boto3_raw_data: "type_defs.AddCacheInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    DiskIds = field("DiskIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddCacheInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddCacheInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddUploadBufferInput:
    boto3_raw_data: "type_defs.AddUploadBufferInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    DiskIds = field("DiskIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddUploadBufferInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddUploadBufferInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddWorkingStorageInput:
    boto3_raw_data: "type_defs.AddWorkingStorageInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    DiskIds = field("DiskIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddWorkingStorageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddWorkingStorageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignTapePoolInput:
    boto3_raw_data: "type_defs.AssignTapePoolInputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")
    PoolId = field("PoolId")
    BypassGovernanceRetention = field("BypassGovernanceRetention")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssignTapePoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignTapePoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheAttributes:
    boto3_raw_data: "type_defs.CacheAttributesTypeDef" = dataclasses.field()

    CacheStaleTimeoutInSeconds = field("CacheStaleTimeoutInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CacheAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachVolumeInput:
    boto3_raw_data: "type_defs.AttachVolumeInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    VolumeARN = field("VolumeARN")
    NetworkInterfaceId = field("NetworkInterfaceId")
    TargetName = field("TargetName")
    DiskId = field("DiskId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachVolumeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachVolumeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomaticTapeCreationRule:
    boto3_raw_data: "type_defs.AutomaticTapeCreationRuleTypeDef" = dataclasses.field()

    TapeBarcodePrefix = field("TapeBarcodePrefix")
    PoolId = field("PoolId")
    TapeSizeInBytes = field("TapeSizeInBytes")
    MinimumNumTapes = field("MinimumNumTapes")
    Worm = field("Worm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomaticTapeCreationRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomaticTapeCreationRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BandwidthRateLimitIntervalOutput:
    boto3_raw_data: "type_defs.BandwidthRateLimitIntervalOutputTypeDef" = (
        dataclasses.field()
    )

    StartHourOfDay = field("StartHourOfDay")
    StartMinuteOfHour = field("StartMinuteOfHour")
    EndHourOfDay = field("EndHourOfDay")
    EndMinuteOfHour = field("EndMinuteOfHour")
    DaysOfWeek = field("DaysOfWeek")
    AverageUploadRateLimitInBitsPerSec = field("AverageUploadRateLimitInBitsPerSec")
    AverageDownloadRateLimitInBitsPerSec = field("AverageDownloadRateLimitInBitsPerSec")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BandwidthRateLimitIntervalOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BandwidthRateLimitIntervalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BandwidthRateLimitInterval:
    boto3_raw_data: "type_defs.BandwidthRateLimitIntervalTypeDef" = dataclasses.field()

    StartHourOfDay = field("StartHourOfDay")
    StartMinuteOfHour = field("StartMinuteOfHour")
    EndHourOfDay = field("EndHourOfDay")
    EndMinuteOfHour = field("EndMinuteOfHour")
    DaysOfWeek = field("DaysOfWeek")
    AverageUploadRateLimitInBitsPerSec = field("AverageUploadRateLimitInBitsPerSec")
    AverageDownloadRateLimitInBitsPerSec = field("AverageDownloadRateLimitInBitsPerSec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BandwidthRateLimitIntervalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BandwidthRateLimitIntervalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheReportFilterOutput:
    boto3_raw_data: "type_defs.CacheReportFilterOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheReportFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheReportFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheReportFilter:
    boto3_raw_data: "type_defs.CacheReportFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheReportFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheReportFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeiSCSIAttributes:
    boto3_raw_data: "type_defs.VolumeiSCSIAttributesTypeDef" = dataclasses.field()

    TargetARN = field("TargetARN")
    NetworkInterfaceId = field("NetworkInterfaceId")
    NetworkInterfacePort = field("NetworkInterfacePort")
    LunNumber = field("LunNumber")
    ChapEnabled = field("ChapEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VolumeiSCSIAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VolumeiSCSIAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelArchivalInput:
    boto3_raw_data: "type_defs.CancelArchivalInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    TapeARN = field("TapeARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelArchivalInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelArchivalInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelCacheReportInput:
    boto3_raw_data: "type_defs.CancelCacheReportInputTypeDef" = dataclasses.field()

    CacheReportARN = field("CacheReportARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelCacheReportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelCacheReportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelRetrievalInput:
    boto3_raw_data: "type_defs.CancelRetrievalInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    TapeARN = field("TapeARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelRetrievalInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelRetrievalInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChapInfo:
    boto3_raw_data: "type_defs.ChapInfoTypeDef" = dataclasses.field()

    TargetARN = field("TargetARN")
    SecretToAuthenticateInitiator = field("SecretToAuthenticateInitiator")
    InitiatorName = field("InitiatorName")
    SecretToAuthenticateTarget = field("SecretToAuthenticateTarget")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChapInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChapInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NFSFileShareDefaults:
    boto3_raw_data: "type_defs.NFSFileShareDefaultsTypeDef" = dataclasses.field()

    FileMode = field("FileMode")
    DirectoryMode = field("DirectoryMode")
    GroupId = field("GroupId")
    OwnerId = field("OwnerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NFSFileShareDefaultsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NFSFileShareDefaultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutomaticTapeCreationPolicyInput:
    boto3_raw_data: "type_defs.DeleteAutomaticTapeCreationPolicyInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAutomaticTapeCreationPolicyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAutomaticTapeCreationPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBandwidthRateLimitInput:
    boto3_raw_data: "type_defs.DeleteBandwidthRateLimitInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    BandwidthType = field("BandwidthType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBandwidthRateLimitInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBandwidthRateLimitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCacheReportInput:
    boto3_raw_data: "type_defs.DeleteCacheReportInputTypeDef" = dataclasses.field()

    CacheReportARN = field("CacheReportARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCacheReportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCacheReportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChapCredentialsInput:
    boto3_raw_data: "type_defs.DeleteChapCredentialsInputTypeDef" = dataclasses.field()

    TargetARN = field("TargetARN")
    InitiatorName = field("InitiatorName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChapCredentialsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChapCredentialsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileShareInput:
    boto3_raw_data: "type_defs.DeleteFileShareInputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")
    ForceDelete = field("ForceDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFileShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayInput:
    boto3_raw_data: "type_defs.DeleteGatewayInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotScheduleInput:
    boto3_raw_data: "type_defs.DeleteSnapshotScheduleInputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotScheduleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotScheduleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTapeArchiveInput:
    boto3_raw_data: "type_defs.DeleteTapeArchiveInputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")
    BypassGovernanceRetention = field("BypassGovernanceRetention")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTapeArchiveInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTapeArchiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTapeInput:
    boto3_raw_data: "type_defs.DeleteTapeInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    TapeARN = field("TapeARN")
    BypassGovernanceRetention = field("BypassGovernanceRetention")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTapeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteTapeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTapePoolInput:
    boto3_raw_data: "type_defs.DeleteTapePoolInputTypeDef" = dataclasses.field()

    PoolARN = field("PoolARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTapePoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTapePoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVolumeInput:
    boto3_raw_data: "type_defs.DeleteVolumeInputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteVolumeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVolumeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAvailabilityMonitorTestInput:
    boto3_raw_data: "type_defs.DescribeAvailabilityMonitorTestInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAvailabilityMonitorTestInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAvailabilityMonitorTestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBandwidthRateLimitInput:
    boto3_raw_data: "type_defs.DescribeBandwidthRateLimitInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBandwidthRateLimitInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBandwidthRateLimitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBandwidthRateLimitScheduleInput:
    boto3_raw_data: "type_defs.DescribeBandwidthRateLimitScheduleInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBandwidthRateLimitScheduleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBandwidthRateLimitScheduleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheInput:
    boto3_raw_data: "type_defs.DescribeCacheInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCacheInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheReportInput:
    boto3_raw_data: "type_defs.DescribeCacheReportInputTypeDef" = dataclasses.field()

    CacheReportARN = field("CacheReportARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCacheReportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheReportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCachediSCSIVolumesInput:
    boto3_raw_data: "type_defs.DescribeCachediSCSIVolumesInputTypeDef" = (
        dataclasses.field()
    )

    VolumeARNs = field("VolumeARNs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCachediSCSIVolumesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCachediSCSIVolumesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChapCredentialsInput:
    boto3_raw_data: "type_defs.DescribeChapCredentialsInputTypeDef" = (
        dataclasses.field()
    )

    TargetARN = field("TargetARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChapCredentialsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChapCredentialsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemAssociationsInput:
    boto3_raw_data: "type_defs.DescribeFileSystemAssociationsInputTypeDef" = (
        dataclasses.field()
    )

    FileSystemAssociationARNList = field("FileSystemAssociationARNList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFileSystemAssociationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemAssociationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayInformationInput:
    boto3_raw_data: "type_defs.DescribeGatewayInformationInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGatewayInformationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayInformationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInterface:
    boto3_raw_data: "type_defs.NetworkInterfaceTypeDef" = dataclasses.field()

    Ipv4Address = field("Ipv4Address")
    MacAddress = field("MacAddress")
    Ipv6Address = field("Ipv6Address")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceStartTimeInput:
    boto3_raw_data: "type_defs.DescribeMaintenanceStartTimeInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceStartTimeInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceStartTimeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SoftwareUpdatePreferences:
    boto3_raw_data: "type_defs.SoftwareUpdatePreferencesTypeDef" = dataclasses.field()

    AutomaticUpdatePolicy = field("AutomaticUpdatePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SoftwareUpdatePreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SoftwareUpdatePreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNFSFileSharesInput:
    boto3_raw_data: "type_defs.DescribeNFSFileSharesInputTypeDef" = dataclasses.field()

    FileShareARNList = field("FileShareARNList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNFSFileSharesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNFSFileSharesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSMBFileSharesInput:
    boto3_raw_data: "type_defs.DescribeSMBFileSharesInputTypeDef" = dataclasses.field()

    FileShareARNList = field("FileShareARNList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSMBFileSharesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSMBFileSharesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSMBSettingsInput:
    boto3_raw_data: "type_defs.DescribeSMBSettingsInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSMBSettingsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSMBSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMBLocalGroupsOutput:
    boto3_raw_data: "type_defs.SMBLocalGroupsOutputTypeDef" = dataclasses.field()

    GatewayAdmins = field("GatewayAdmins")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SMBLocalGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMBLocalGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotScheduleInput:
    boto3_raw_data: "type_defs.DescribeSnapshotScheduleInputTypeDef" = (
        dataclasses.field()
    )

    VolumeARN = field("VolumeARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSnapshotScheduleInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotScheduleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStorediSCSIVolumesInput:
    boto3_raw_data: "type_defs.DescribeStorediSCSIVolumesInputTypeDef" = (
        dataclasses.field()
    )

    VolumeARNs = field("VolumeARNs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStorediSCSIVolumesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStorediSCSIVolumesInputTypeDef"]
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
class DescribeTapeArchivesInput:
    boto3_raw_data: "type_defs.DescribeTapeArchivesInputTypeDef" = dataclasses.field()

    TapeARNs = field("TapeARNs")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTapeArchivesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTapeArchivesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TapeArchive:
    boto3_raw_data: "type_defs.TapeArchiveTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")
    TapeBarcode = field("TapeBarcode")
    TapeCreatedDate = field("TapeCreatedDate")
    TapeSizeInBytes = field("TapeSizeInBytes")
    CompletionTime = field("CompletionTime")
    RetrievedTo = field("RetrievedTo")
    TapeStatus = field("TapeStatus")
    TapeUsedInBytes = field("TapeUsedInBytes")
    KMSKey = field("KMSKey")
    PoolId = field("PoolId")
    Worm = field("Worm")
    RetentionStartDate = field("RetentionStartDate")
    PoolEntryDate = field("PoolEntryDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TapeArchiveTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TapeArchiveTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTapeRecoveryPointsInput:
    boto3_raw_data: "type_defs.DescribeTapeRecoveryPointsInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTapeRecoveryPointsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTapeRecoveryPointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TapeRecoveryPointInfo:
    boto3_raw_data: "type_defs.TapeRecoveryPointInfoTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")
    TapeRecoveryPointTime = field("TapeRecoveryPointTime")
    TapeSizeInBytes = field("TapeSizeInBytes")
    TapeStatus = field("TapeStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TapeRecoveryPointInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TapeRecoveryPointInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTapesInput:
    boto3_raw_data: "type_defs.DescribeTapesInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    TapeARNs = field("TapeARNs")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTapesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTapesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tape:
    boto3_raw_data: "type_defs.TapeTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")
    TapeBarcode = field("TapeBarcode")
    TapeCreatedDate = field("TapeCreatedDate")
    TapeSizeInBytes = field("TapeSizeInBytes")
    TapeStatus = field("TapeStatus")
    VTLDevice = field("VTLDevice")
    Progress = field("Progress")
    TapeUsedInBytes = field("TapeUsedInBytes")
    KMSKey = field("KMSKey")
    PoolId = field("PoolId")
    Worm = field("Worm")
    RetentionStartDate = field("RetentionStartDate")
    PoolEntryDate = field("PoolEntryDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TapeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TapeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUploadBufferInput:
    boto3_raw_data: "type_defs.DescribeUploadBufferInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUploadBufferInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUploadBufferInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVTLDevicesInput:
    boto3_raw_data: "type_defs.DescribeVTLDevicesInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    VTLDeviceARNs = field("VTLDeviceARNs")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVTLDevicesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVTLDevicesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkingStorageInput:
    boto3_raw_data: "type_defs.DescribeWorkingStorageInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkingStorageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkingStorageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachVolumeInput:
    boto3_raw_data: "type_defs.DetachVolumeInputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")
    ForceDetach = field("ForceDetach")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetachVolumeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachVolumeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceiSCSIAttributes:
    boto3_raw_data: "type_defs.DeviceiSCSIAttributesTypeDef" = dataclasses.field()

    TargetARN = field("TargetARN")
    NetworkInterfaceId = field("NetworkInterfaceId")
    NetworkInterfacePort = field("NetworkInterfacePort")
    ChapEnabled = field("ChapEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeviceiSCSIAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeviceiSCSIAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableGatewayInput:
    boto3_raw_data: "type_defs.DisableGatewayInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableGatewayInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableGatewayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFileSystemInput:
    boto3_raw_data: "type_defs.DisassociateFileSystemInputTypeDef" = dataclasses.field()

    FileSystemAssociationARN = field("FileSystemAssociationARN")
    ForceDelete = field("ForceDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateFileSystemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFileSystemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Disk:
    boto3_raw_data: "type_defs.DiskTypeDef" = dataclasses.field()

    DiskId = field("DiskId")
    DiskPath = field("DiskPath")
    DiskNode = field("DiskNode")
    DiskStatus = field("DiskStatus")
    DiskSizeInBytes = field("DiskSizeInBytes")
    DiskAllocationType = field("DiskAllocationType")
    DiskAllocationResource = field("DiskAllocationResource")
    DiskAttributeList = field("DiskAttributeList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DiskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DiskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointNetworkConfigurationOutput:
    boto3_raw_data: "type_defs.EndpointNetworkConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    IpAddresses = field("IpAddresses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EndpointNetworkConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointNetworkConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointNetworkConfiguration:
    boto3_raw_data: "type_defs.EndpointNetworkConfigurationTypeDef" = (
        dataclasses.field()
    )

    IpAddresses = field("IpAddresses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointNetworkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointNetworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvictFilesFailingUploadInput:
    boto3_raw_data: "type_defs.EvictFilesFailingUploadInputTypeDef" = (
        dataclasses.field()
    )

    FileShareARN = field("FileShareARN")
    ForceRemove = field("ForceRemove")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvictFilesFailingUploadInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvictFilesFailingUploadInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileShareInfo:
    boto3_raw_data: "type_defs.FileShareInfoTypeDef" = dataclasses.field()

    FileShareType = field("FileShareType")
    FileShareARN = field("FileShareARN")
    FileShareId = field("FileShareId")
    FileShareStatus = field("FileShareStatus")
    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileShareInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileShareInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemAssociationStatusDetail:
    boto3_raw_data: "type_defs.FileSystemAssociationStatusDetailTypeDef" = (
        dataclasses.field()
    )

    ErrorCode = field("ErrorCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FileSystemAssociationStatusDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemAssociationStatusDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemAssociationSummary:
    boto3_raw_data: "type_defs.FileSystemAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    FileSystemAssociationId = field("FileSystemAssociationId")
    FileSystemAssociationARN = field("FileSystemAssociationARN")
    FileSystemAssociationStatus = field("FileSystemAssociationStatus")
    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSystemAssociationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayInfo:
    boto3_raw_data: "type_defs.GatewayInfoTypeDef" = dataclasses.field()

    GatewayId = field("GatewayId")
    GatewayARN = field("GatewayARN")
    GatewayType = field("GatewayType")
    GatewayOperationalState = field("GatewayOperationalState")
    GatewayName = field("GatewayName")
    Ec2InstanceId = field("Ec2InstanceId")
    Ec2InstanceRegion = field("Ec2InstanceRegion")
    HostEnvironment = field("HostEnvironment")
    HostEnvironmentId = field("HostEnvironmentId")
    DeprecationDate = field("DeprecationDate")
    SoftwareVersion = field("SoftwareVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewayInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JoinDomainInput:
    boto3_raw_data: "type_defs.JoinDomainInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    DomainName = field("DomainName")
    UserName = field("UserName")
    Password = field("Password")
    OrganizationalUnit = field("OrganizationalUnit")
    DomainControllers = field("DomainControllers")
    TimeoutInSeconds = field("TimeoutInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JoinDomainInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JoinDomainInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomaticTapeCreationPoliciesInput:
    boto3_raw_data: "type_defs.ListAutomaticTapeCreationPoliciesInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomaticTapeCreationPoliciesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomaticTapeCreationPoliciesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCacheReportsInput:
    boto3_raw_data: "type_defs.ListCacheReportsInputTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCacheReportsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCacheReportsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileSharesInput:
    boto3_raw_data: "type_defs.ListFileSharesInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFileSharesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileSharesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileSystemAssociationsInput:
    boto3_raw_data: "type_defs.ListFileSystemAssociationsInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFileSystemAssociationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileSystemAssociationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysInput:
    boto3_raw_data: "type_defs.ListGatewaysInputTypeDef" = dataclasses.field()

    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLocalDisksInput:
    boto3_raw_data: "type_defs.ListLocalDisksInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLocalDisksInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLocalDisksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTapePoolsInput:
    boto3_raw_data: "type_defs.ListTapePoolsInputTypeDef" = dataclasses.field()

    PoolARNs = field("PoolARNs")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTapePoolsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTapePoolsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PoolInfo:
    boto3_raw_data: "type_defs.PoolInfoTypeDef" = dataclasses.field()

    PoolARN = field("PoolARN")
    PoolName = field("PoolName")
    StorageClass = field("StorageClass")
    RetentionLockType = field("RetentionLockType")
    RetentionLockTimeInDays = field("RetentionLockTimeInDays")
    PoolStatus = field("PoolStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PoolInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PoolInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTapesInput:
    boto3_raw_data: "type_defs.ListTapesInputTypeDef" = dataclasses.field()

    TapeARNs = field("TapeARNs")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTapesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTapesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TapeInfo:
    boto3_raw_data: "type_defs.TapeInfoTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")
    TapeBarcode = field("TapeBarcode")
    TapeSizeInBytes = field("TapeSizeInBytes")
    TapeStatus = field("TapeStatus")
    GatewayARN = field("GatewayARN")
    PoolId = field("PoolId")
    RetentionStartDate = field("RetentionStartDate")
    PoolEntryDate = field("PoolEntryDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TapeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TapeInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVolumeInitiatorsInput:
    boto3_raw_data: "type_defs.ListVolumeInitiatorsInputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVolumeInitiatorsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVolumeInitiatorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVolumeRecoveryPointsInput:
    boto3_raw_data: "type_defs.ListVolumeRecoveryPointsInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVolumeRecoveryPointsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVolumeRecoveryPointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeRecoveryPointInfo:
    boto3_raw_data: "type_defs.VolumeRecoveryPointInfoTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")
    VolumeSizeInBytes = field("VolumeSizeInBytes")
    VolumeUsageInBytes = field("VolumeUsageInBytes")
    VolumeRecoveryPointTime = field("VolumeRecoveryPointTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VolumeRecoveryPointInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VolumeRecoveryPointInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVolumesInput:
    boto3_raw_data: "type_defs.ListVolumesInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    Marker = field("Marker")
    Limit = field("Limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListVolumesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVolumesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeInfo:
    boto3_raw_data: "type_defs.VolumeInfoTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")
    VolumeId = field("VolumeId")
    GatewayARN = field("GatewayARN")
    GatewayId = field("GatewayId")
    VolumeType = field("VolumeType")
    VolumeSizeInBytes = field("VolumeSizeInBytes")
    VolumeAttachmentStatus = field("VolumeAttachmentStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyWhenUploadedInput:
    boto3_raw_data: "type_defs.NotifyWhenUploadedInputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotifyWhenUploadedInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyWhenUploadedInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshCacheInput:
    boto3_raw_data: "type_defs.RefreshCacheInputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")
    FolderList = field("FolderList")
    Recursive = field("Recursive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RefreshCacheInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshCacheInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromResourceInput:
    boto3_raw_data: "type_defs.RemoveTagsFromResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsFromResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetCacheInput:
    boto3_raw_data: "type_defs.ResetCacheInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResetCacheInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResetCacheInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveTapeArchiveInput:
    boto3_raw_data: "type_defs.RetrieveTapeArchiveInputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")
    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveTapeArchiveInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveTapeArchiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveTapeRecoveryPointInput:
    boto3_raw_data: "type_defs.RetrieveTapeRecoveryPointInputTypeDef" = (
        dataclasses.field()
    )

    TapeARN = field("TapeARN")
    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrieveTapeRecoveryPointInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveTapeRecoveryPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMBLocalGroups:
    boto3_raw_data: "type_defs.SMBLocalGroupsTypeDef" = dataclasses.field()

    GatewayAdmins = field("GatewayAdmins")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SMBLocalGroupsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SMBLocalGroupsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetLocalConsolePasswordInput:
    boto3_raw_data: "type_defs.SetLocalConsolePasswordInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    LocalConsolePassword = field("LocalConsolePassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetLocalConsolePasswordInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetLocalConsolePasswordInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetSMBGuestPasswordInput:
    boto3_raw_data: "type_defs.SetSMBGuestPasswordInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    Password = field("Password")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetSMBGuestPasswordInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetSMBGuestPasswordInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShutdownGatewayInput:
    boto3_raw_data: "type_defs.ShutdownGatewayInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShutdownGatewayInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShutdownGatewayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAvailabilityMonitorTestInput:
    boto3_raw_data: "type_defs.StartAvailabilityMonitorTestInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAvailabilityMonitorTestInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAvailabilityMonitorTestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartGatewayInput:
    boto3_raw_data: "type_defs.StartGatewayInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartGatewayInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartGatewayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBandwidthRateLimitInput:
    boto3_raw_data: "type_defs.UpdateBandwidthRateLimitInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    AverageUploadRateLimitInBitsPerSec = field("AverageUploadRateLimitInBitsPerSec")
    AverageDownloadRateLimitInBitsPerSec = field("AverageDownloadRateLimitInBitsPerSec")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBandwidthRateLimitInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBandwidthRateLimitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChapCredentialsInput:
    boto3_raw_data: "type_defs.UpdateChapCredentialsInputTypeDef" = dataclasses.field()

    TargetARN = field("TargetARN")
    SecretToAuthenticateInitiator = field("SecretToAuthenticateInitiator")
    InitiatorName = field("InitiatorName")
    SecretToAuthenticateTarget = field("SecretToAuthenticateTarget")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChapCredentialsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChapCredentialsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayInformationInput:
    boto3_raw_data: "type_defs.UpdateGatewayInformationInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    GatewayName = field("GatewayName")
    GatewayTimezone = field("GatewayTimezone")
    CloudWatchLogGroupARN = field("CloudWatchLogGroupARN")
    GatewayCapacity = field("GatewayCapacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGatewayInformationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayInformationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewaySoftwareNowInput:
    boto3_raw_data: "type_defs.UpdateGatewaySoftwareNowInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGatewaySoftwareNowInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewaySoftwareNowInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSMBFileShareVisibilityInput:
    boto3_raw_data: "type_defs.UpdateSMBFileShareVisibilityInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    FileSharesVisible = field("FileSharesVisible")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSMBFileShareVisibilityInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSMBFileShareVisibilityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSMBSecurityStrategyInput:
    boto3_raw_data: "type_defs.UpdateSMBSecurityStrategyInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    SMBSecurityStrategy = field("SMBSecurityStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSMBSecurityStrategyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSMBSecurityStrategyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVTLDeviceTypeInput:
    boto3_raw_data: "type_defs.UpdateVTLDeviceTypeInputTypeDef" = dataclasses.field()

    VTLDeviceARN = field("VTLDeviceARN")
    DeviceType = field("DeviceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVTLDeviceTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVTLDeviceTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateGatewayInput:
    boto3_raw_data: "type_defs.ActivateGatewayInputTypeDef" = dataclasses.field()

    ActivationKey = field("ActivationKey")
    GatewayName = field("GatewayName")
    GatewayTimezone = field("GatewayTimezone")
    GatewayRegion = field("GatewayRegion")
    GatewayType = field("GatewayType")
    TapeDriveType = field("TapeDriveType")
    MediumChangerType = field("MediumChangerType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateGatewayInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateGatewayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsToResourceInput:
    boto3_raw_data: "type_defs.AddTagsToResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddTagsToResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCachediSCSIVolumeInput:
    boto3_raw_data: "type_defs.CreateCachediSCSIVolumeInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    VolumeSizeInBytes = field("VolumeSizeInBytes")
    TargetName = field("TargetName")
    NetworkInterfaceId = field("NetworkInterfaceId")
    ClientToken = field("ClientToken")
    SnapshotId = field("SnapshotId")
    SourceVolumeARN = field("SourceVolumeARN")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCachediSCSIVolumeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCachediSCSIVolumeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotFromVolumeRecoveryPointInput:
    boto3_raw_data: "type_defs.CreateSnapshotFromVolumeRecoveryPointInputTypeDef" = (
        dataclasses.field()
    )

    VolumeARN = field("VolumeARN")
    SnapshotDescription = field("SnapshotDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSnapshotFromVolumeRecoveryPointInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotFromVolumeRecoveryPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotInput:
    boto3_raw_data: "type_defs.CreateSnapshotInputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")
    SnapshotDescription = field("SnapshotDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorediSCSIVolumeInput:
    boto3_raw_data: "type_defs.CreateStorediSCSIVolumeInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    DiskId = field("DiskId")
    PreserveExistingData = field("PreserveExistingData")
    TargetName = field("TargetName")
    NetworkInterfaceId = field("NetworkInterfaceId")
    SnapshotId = field("SnapshotId")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStorediSCSIVolumeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorediSCSIVolumeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTapePoolInput:
    boto3_raw_data: "type_defs.CreateTapePoolInputTypeDef" = dataclasses.field()

    PoolName = field("PoolName")
    StorageClass = field("StorageClass")
    RetentionLockType = field("RetentionLockType")
    RetentionLockTimeInDays = field("RetentionLockTimeInDays")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTapePoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTapePoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTapeWithBarcodeInput:
    boto3_raw_data: "type_defs.CreateTapeWithBarcodeInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    TapeSizeInBytes = field("TapeSizeInBytes")
    TapeBarcode = field("TapeBarcode")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")
    PoolId = field("PoolId")
    Worm = field("Worm")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTapeWithBarcodeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTapeWithBarcodeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTapesInput:
    boto3_raw_data: "type_defs.CreateTapesInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    TapeSizeInBytes = field("TapeSizeInBytes")
    ClientToken = field("ClientToken")
    NumTapesToCreate = field("NumTapesToCreate")
    TapeBarcodePrefix = field("TapeBarcodePrefix")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")
    PoolId = field("PoolId")
    Worm = field("Worm")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTapesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTapesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSnapshotScheduleInput:
    boto3_raw_data: "type_defs.UpdateSnapshotScheduleInputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")
    StartAt = field("StartAt")
    RecurrenceInHours = field("RecurrenceInHours")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSnapshotScheduleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSnapshotScheduleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateGatewayOutput:
    boto3_raw_data: "type_defs.ActivateGatewayOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddCacheOutput:
    boto3_raw_data: "type_defs.AddCacheOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddCacheOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddCacheOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsToResourceOutput:
    boto3_raw_data: "type_defs.AddTagsToResourceOutputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddTagsToResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddUploadBufferOutput:
    boto3_raw_data: "type_defs.AddUploadBufferOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddUploadBufferOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddUploadBufferOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddWorkingStorageOutput:
    boto3_raw_data: "type_defs.AddWorkingStorageOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddWorkingStorageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddWorkingStorageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignTapePoolOutput:
    boto3_raw_data: "type_defs.AssignTapePoolOutputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssignTapePoolOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignTapePoolOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFileSystemOutput:
    boto3_raw_data: "type_defs.AssociateFileSystemOutputTypeDef" = dataclasses.field()

    FileSystemAssociationARN = field("FileSystemAssociationARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateFileSystemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFileSystemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachVolumeOutput:
    boto3_raw_data: "type_defs.AttachVolumeOutputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")
    TargetARN = field("TargetARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachVolumeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachVolumeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelArchivalOutput:
    boto3_raw_data: "type_defs.CancelArchivalOutputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelArchivalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelArchivalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelCacheReportOutput:
    boto3_raw_data: "type_defs.CancelCacheReportOutputTypeDef" = dataclasses.field()

    CacheReportARN = field("CacheReportARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelCacheReportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelCacheReportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelRetrievalOutput:
    boto3_raw_data: "type_defs.CancelRetrievalOutputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelRetrievalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelRetrievalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCachediSCSIVolumeOutput:
    boto3_raw_data: "type_defs.CreateCachediSCSIVolumeOutputTypeDef" = (
        dataclasses.field()
    )

    VolumeARN = field("VolumeARN")
    TargetARN = field("TargetARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCachediSCSIVolumeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCachediSCSIVolumeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNFSFileShareOutput:
    boto3_raw_data: "type_defs.CreateNFSFileShareOutputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNFSFileShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNFSFileShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSMBFileShareOutput:
    boto3_raw_data: "type_defs.CreateSMBFileShareOutputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSMBFileShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSMBFileShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotFromVolumeRecoveryPointOutput:
    boto3_raw_data: "type_defs.CreateSnapshotFromVolumeRecoveryPointOutputTypeDef" = (
        dataclasses.field()
    )

    SnapshotId = field("SnapshotId")
    VolumeARN = field("VolumeARN")
    VolumeRecoveryPointTime = field("VolumeRecoveryPointTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSnapshotFromVolumeRecoveryPointOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotFromVolumeRecoveryPointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotOutput:
    boto3_raw_data: "type_defs.CreateSnapshotOutputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")
    SnapshotId = field("SnapshotId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorediSCSIVolumeOutput:
    boto3_raw_data: "type_defs.CreateStorediSCSIVolumeOutputTypeDef" = (
        dataclasses.field()
    )

    VolumeARN = field("VolumeARN")
    VolumeSizeInBytes = field("VolumeSizeInBytes")
    TargetARN = field("TargetARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateStorediSCSIVolumeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorediSCSIVolumeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTapePoolOutput:
    boto3_raw_data: "type_defs.CreateTapePoolOutputTypeDef" = dataclasses.field()

    PoolARN = field("PoolARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTapePoolOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTapePoolOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTapeWithBarcodeOutput:
    boto3_raw_data: "type_defs.CreateTapeWithBarcodeOutputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTapeWithBarcodeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTapeWithBarcodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTapesOutput:
    boto3_raw_data: "type_defs.CreateTapesOutputTypeDef" = dataclasses.field()

    TapeARNs = field("TapeARNs")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTapesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTapesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutomaticTapeCreationPolicyOutput:
    boto3_raw_data: "type_defs.DeleteAutomaticTapeCreationPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAutomaticTapeCreationPolicyOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAutomaticTapeCreationPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBandwidthRateLimitOutput:
    boto3_raw_data: "type_defs.DeleteBandwidthRateLimitOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBandwidthRateLimitOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBandwidthRateLimitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCacheReportOutput:
    boto3_raw_data: "type_defs.DeleteCacheReportOutputTypeDef" = dataclasses.field()

    CacheReportARN = field("CacheReportARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCacheReportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCacheReportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChapCredentialsOutput:
    boto3_raw_data: "type_defs.DeleteChapCredentialsOutputTypeDef" = dataclasses.field()

    TargetARN = field("TargetARN")
    InitiatorName = field("InitiatorName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChapCredentialsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChapCredentialsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileShareOutput:
    boto3_raw_data: "type_defs.DeleteFileShareOutputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFileShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayOutput:
    boto3_raw_data: "type_defs.DeleteGatewayOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotScheduleOutput:
    boto3_raw_data: "type_defs.DeleteSnapshotScheduleOutputTypeDef" = (
        dataclasses.field()
    )

    VolumeARN = field("VolumeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotScheduleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTapeArchiveOutput:
    boto3_raw_data: "type_defs.DeleteTapeArchiveOutputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTapeArchiveOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTapeArchiveOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTapeOutput:
    boto3_raw_data: "type_defs.DeleteTapeOutputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTapeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTapeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTapePoolOutput:
    boto3_raw_data: "type_defs.DeleteTapePoolOutputTypeDef" = dataclasses.field()

    PoolARN = field("PoolARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTapePoolOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTapePoolOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVolumeOutput:
    boto3_raw_data: "type_defs.DeleteVolumeOutputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVolumeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVolumeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAvailabilityMonitorTestOutput:
    boto3_raw_data: "type_defs.DescribeAvailabilityMonitorTestOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    Status = field("Status")
    StartTime = field("StartTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAvailabilityMonitorTestOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAvailabilityMonitorTestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBandwidthRateLimitOutput:
    boto3_raw_data: "type_defs.DescribeBandwidthRateLimitOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    AverageUploadRateLimitInBitsPerSec = field("AverageUploadRateLimitInBitsPerSec")
    AverageDownloadRateLimitInBitsPerSec = field("AverageDownloadRateLimitInBitsPerSec")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBandwidthRateLimitOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBandwidthRateLimitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheOutput:
    boto3_raw_data: "type_defs.DescribeCacheOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    DiskIds = field("DiskIds")
    CacheAllocatedInBytes = field("CacheAllocatedInBytes")
    CacheUsedPercentage = field("CacheUsedPercentage")
    CacheDirtyPercentage = field("CacheDirtyPercentage")
    CacheHitPercentage = field("CacheHitPercentage")
    CacheMissPercentage = field("CacheMissPercentage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCacheOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotScheduleOutput:
    boto3_raw_data: "type_defs.DescribeSnapshotScheduleOutputTypeDef" = (
        dataclasses.field()
    )

    VolumeARN = field("VolumeARN")
    StartAt = field("StartAt")
    RecurrenceInHours = field("RecurrenceInHours")
    Description = field("Description")
    Timezone = field("Timezone")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSnapshotScheduleOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUploadBufferOutput:
    boto3_raw_data: "type_defs.DescribeUploadBufferOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    DiskIds = field("DiskIds")
    UploadBufferUsedInBytes = field("UploadBufferUsedInBytes")
    UploadBufferAllocatedInBytes = field("UploadBufferAllocatedInBytes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUploadBufferOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUploadBufferOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkingStorageOutput:
    boto3_raw_data: "type_defs.DescribeWorkingStorageOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    DiskIds = field("DiskIds")
    WorkingStorageUsedInBytes = field("WorkingStorageUsedInBytes")
    WorkingStorageAllocatedInBytes = field("WorkingStorageAllocatedInBytes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkingStorageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkingStorageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachVolumeOutput:
    boto3_raw_data: "type_defs.DetachVolumeOutputTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachVolumeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachVolumeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableGatewayOutput:
    boto3_raw_data: "type_defs.DisableGatewayOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFileSystemOutput:
    boto3_raw_data: "type_defs.DisassociateFileSystemOutputTypeDef" = (
        dataclasses.field()
    )

    FileSystemAssociationARN = field("FileSystemAssociationARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateFileSystemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFileSystemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvictFilesFailingUploadOutput:
    boto3_raw_data: "type_defs.EvictFilesFailingUploadOutputTypeDef" = (
        dataclasses.field()
    )

    NotificationId = field("NotificationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EvictFilesFailingUploadOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvictFilesFailingUploadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JoinDomainOutput:
    boto3_raw_data: "type_defs.JoinDomainOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    ActiveDirectoryStatus = field("ActiveDirectoryStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JoinDomainOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JoinDomainOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    Marker = field("Marker")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVolumeInitiatorsOutput:
    boto3_raw_data: "type_defs.ListVolumeInitiatorsOutputTypeDef" = dataclasses.field()

    Initiators = field("Initiators")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVolumeInitiatorsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVolumeInitiatorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyWhenUploadedOutput:
    boto3_raw_data: "type_defs.NotifyWhenUploadedOutputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")
    NotificationId = field("NotificationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotifyWhenUploadedOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyWhenUploadedOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshCacheOutput:
    boto3_raw_data: "type_defs.RefreshCacheOutputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")
    NotificationId = field("NotificationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshCacheOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshCacheOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromResourceOutput:
    boto3_raw_data: "type_defs.RemoveTagsFromResourceOutputTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsFromResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetCacheOutput:
    boto3_raw_data: "type_defs.ResetCacheOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResetCacheOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetCacheOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveTapeArchiveOutput:
    boto3_raw_data: "type_defs.RetrieveTapeArchiveOutputTypeDef" = dataclasses.field()

    TapeARN = field("TapeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveTapeArchiveOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveTapeArchiveOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveTapeRecoveryPointOutput:
    boto3_raw_data: "type_defs.RetrieveTapeRecoveryPointOutputTypeDef" = (
        dataclasses.field()
    )

    TapeARN = field("TapeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrieveTapeRecoveryPointOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveTapeRecoveryPointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetLocalConsolePasswordOutput:
    boto3_raw_data: "type_defs.SetLocalConsolePasswordOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetLocalConsolePasswordOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetLocalConsolePasswordOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetSMBGuestPasswordOutput:
    boto3_raw_data: "type_defs.SetSMBGuestPasswordOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetSMBGuestPasswordOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetSMBGuestPasswordOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShutdownGatewayOutput:
    boto3_raw_data: "type_defs.ShutdownGatewayOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShutdownGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShutdownGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAvailabilityMonitorTestOutput:
    boto3_raw_data: "type_defs.StartAvailabilityMonitorTestOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAvailabilityMonitorTestOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAvailabilityMonitorTestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCacheReportOutput:
    boto3_raw_data: "type_defs.StartCacheReportOutputTypeDef" = dataclasses.field()

    CacheReportARN = field("CacheReportARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCacheReportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCacheReportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartGatewayOutput:
    boto3_raw_data: "type_defs.StartGatewayOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutomaticTapeCreationPolicyOutput:
    boto3_raw_data: "type_defs.UpdateAutomaticTapeCreationPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutomaticTapeCreationPolicyOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAutomaticTapeCreationPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBandwidthRateLimitOutput:
    boto3_raw_data: "type_defs.UpdateBandwidthRateLimitOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBandwidthRateLimitOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBandwidthRateLimitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBandwidthRateLimitScheduleOutput:
    boto3_raw_data: "type_defs.UpdateBandwidthRateLimitScheduleOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBandwidthRateLimitScheduleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBandwidthRateLimitScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChapCredentialsOutput:
    boto3_raw_data: "type_defs.UpdateChapCredentialsOutputTypeDef" = dataclasses.field()

    TargetARN = field("TargetARN")
    InitiatorName = field("InitiatorName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChapCredentialsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChapCredentialsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemAssociationOutput:
    boto3_raw_data: "type_defs.UpdateFileSystemAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    FileSystemAssociationARN = field("FileSystemAssociationARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFileSystemAssociationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayInformationOutput:
    boto3_raw_data: "type_defs.UpdateGatewayInformationOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    GatewayName = field("GatewayName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGatewayInformationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayInformationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewaySoftwareNowOutput:
    boto3_raw_data: "type_defs.UpdateGatewaySoftwareNowOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGatewaySoftwareNowOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewaySoftwareNowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMaintenanceStartTimeOutput:
    boto3_raw_data: "type_defs.UpdateMaintenanceStartTimeOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMaintenanceStartTimeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMaintenanceStartTimeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNFSFileShareOutput:
    boto3_raw_data: "type_defs.UpdateNFSFileShareOutputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNFSFileShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNFSFileShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSMBFileShareOutput:
    boto3_raw_data: "type_defs.UpdateSMBFileShareOutputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSMBFileShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSMBFileShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSMBFileShareVisibilityOutput:
    boto3_raw_data: "type_defs.UpdateSMBFileShareVisibilityOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSMBFileShareVisibilityOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSMBFileShareVisibilityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSMBLocalGroupsOutput:
    boto3_raw_data: "type_defs.UpdateSMBLocalGroupsOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSMBLocalGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSMBLocalGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSMBSecurityStrategyOutput:
    boto3_raw_data: "type_defs.UpdateSMBSecurityStrategyOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSMBSecurityStrategyOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSMBSecurityStrategyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSnapshotScheduleOutput:
    boto3_raw_data: "type_defs.UpdateSnapshotScheduleOutputTypeDef" = (
        dataclasses.field()
    )

    VolumeARN = field("VolumeARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSnapshotScheduleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSnapshotScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVTLDeviceTypeOutput:
    boto3_raw_data: "type_defs.UpdateVTLDeviceTypeOutputTypeDef" = dataclasses.field()

    VTLDeviceARN = field("VTLDeviceARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVTLDeviceTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVTLDeviceTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSMBFileShareInput:
    boto3_raw_data: "type_defs.CreateSMBFileShareInputTypeDef" = dataclasses.field()

    ClientToken = field("ClientToken")
    GatewayARN = field("GatewayARN")
    Role = field("Role")
    LocationARN = field("LocationARN")
    EncryptionType = field("EncryptionType")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")
    DefaultStorageClass = field("DefaultStorageClass")
    ObjectACL = field("ObjectACL")
    ReadOnly = field("ReadOnly")
    GuessMIMETypeEnabled = field("GuessMIMETypeEnabled")
    RequesterPays = field("RequesterPays")
    SMBACLEnabled = field("SMBACLEnabled")
    AccessBasedEnumeration = field("AccessBasedEnumeration")
    AdminUserList = field("AdminUserList")
    ValidUserList = field("ValidUserList")
    InvalidUserList = field("InvalidUserList")
    AuditDestinationARN = field("AuditDestinationARN")
    Authentication = field("Authentication")
    CaseSensitivity = field("CaseSensitivity")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    FileShareName = field("FileShareName")

    @cached_property
    def CacheAttributes(self):  # pragma: no cover
        return CacheAttributes.make_one(self.boto3_raw_data["CacheAttributes"])

    NotificationPolicy = field("NotificationPolicy")
    VPCEndpointDNSName = field("VPCEndpointDNSName")
    BucketRegion = field("BucketRegion")
    OplocksEnabled = field("OplocksEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSMBFileShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSMBFileShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMBFileShareInfo:
    boto3_raw_data: "type_defs.SMBFileShareInfoTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")
    FileShareId = field("FileShareId")
    FileShareStatus = field("FileShareStatus")
    GatewayARN = field("GatewayARN")
    EncryptionType = field("EncryptionType")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")
    Path = field("Path")
    Role = field("Role")
    LocationARN = field("LocationARN")
    DefaultStorageClass = field("DefaultStorageClass")
    ObjectACL = field("ObjectACL")
    ReadOnly = field("ReadOnly")
    GuessMIMETypeEnabled = field("GuessMIMETypeEnabled")
    RequesterPays = field("RequesterPays")
    SMBACLEnabled = field("SMBACLEnabled")
    AccessBasedEnumeration = field("AccessBasedEnumeration")
    AdminUserList = field("AdminUserList")
    ValidUserList = field("ValidUserList")
    InvalidUserList = field("InvalidUserList")
    AuditDestinationARN = field("AuditDestinationARN")
    Authentication = field("Authentication")
    CaseSensitivity = field("CaseSensitivity")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    FileShareName = field("FileShareName")

    @cached_property
    def CacheAttributes(self):  # pragma: no cover
        return CacheAttributes.make_one(self.boto3_raw_data["CacheAttributes"])

    NotificationPolicy = field("NotificationPolicy")
    VPCEndpointDNSName = field("VPCEndpointDNSName")
    BucketRegion = field("BucketRegion")
    OplocksEnabled = field("OplocksEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SMBFileShareInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMBFileShareInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemAssociationInput:
    boto3_raw_data: "type_defs.UpdateFileSystemAssociationInputTypeDef" = (
        dataclasses.field()
    )

    FileSystemAssociationARN = field("FileSystemAssociationARN")
    UserName = field("UserName")
    Password = field("Password")
    AuditDestinationARN = field("AuditDestinationARN")

    @cached_property
    def CacheAttributes(self):  # pragma: no cover
        return CacheAttributes.make_one(self.boto3_raw_data["CacheAttributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFileSystemAssociationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSMBFileShareInput:
    boto3_raw_data: "type_defs.UpdateSMBFileShareInputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")
    EncryptionType = field("EncryptionType")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")
    DefaultStorageClass = field("DefaultStorageClass")
    ObjectACL = field("ObjectACL")
    ReadOnly = field("ReadOnly")
    GuessMIMETypeEnabled = field("GuessMIMETypeEnabled")
    RequesterPays = field("RequesterPays")
    SMBACLEnabled = field("SMBACLEnabled")
    AccessBasedEnumeration = field("AccessBasedEnumeration")
    AdminUserList = field("AdminUserList")
    ValidUserList = field("ValidUserList")
    InvalidUserList = field("InvalidUserList")
    AuditDestinationARN = field("AuditDestinationARN")
    CaseSensitivity = field("CaseSensitivity")
    FileShareName = field("FileShareName")

    @cached_property
    def CacheAttributes(self):  # pragma: no cover
        return CacheAttributes.make_one(self.boto3_raw_data["CacheAttributes"])

    NotificationPolicy = field("NotificationPolicy")
    OplocksEnabled = field("OplocksEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSMBFileShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSMBFileShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomaticTapeCreationPolicyInfo:
    boto3_raw_data: "type_defs.AutomaticTapeCreationPolicyInfoTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutomaticTapeCreationRules(self):  # pragma: no cover
        return AutomaticTapeCreationRule.make_many(
            self.boto3_raw_data["AutomaticTapeCreationRules"]
        )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomaticTapeCreationPolicyInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomaticTapeCreationPolicyInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutomaticTapeCreationPolicyInput:
    boto3_raw_data: "type_defs.UpdateAutomaticTapeCreationPolicyInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutomaticTapeCreationRules(self):  # pragma: no cover
        return AutomaticTapeCreationRule.make_many(
            self.boto3_raw_data["AutomaticTapeCreationRules"]
        )

    GatewayARN = field("GatewayARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutomaticTapeCreationPolicyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAutomaticTapeCreationPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBandwidthRateLimitScheduleOutput:
    boto3_raw_data: "type_defs.DescribeBandwidthRateLimitScheduleOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def BandwidthRateLimitIntervals(self):  # pragma: no cover
        return BandwidthRateLimitIntervalOutput.make_many(
            self.boto3_raw_data["BandwidthRateLimitIntervals"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBandwidthRateLimitScheduleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBandwidthRateLimitScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheReportInfo:
    boto3_raw_data: "type_defs.CacheReportInfoTypeDef" = dataclasses.field()

    CacheReportARN = field("CacheReportARN")
    CacheReportStatus = field("CacheReportStatus")
    ReportCompletionPercent = field("ReportCompletionPercent")
    EndTime = field("EndTime")
    Role = field("Role")
    FileShareARN = field("FileShareARN")
    LocationARN = field("LocationARN")
    StartTime = field("StartTime")

    @cached_property
    def InclusionFilters(self):  # pragma: no cover
        return CacheReportFilterOutput.make_many(
            self.boto3_raw_data["InclusionFilters"]
        )

    @cached_property
    def ExclusionFilters(self):  # pragma: no cover
        return CacheReportFilterOutput.make_many(
            self.boto3_raw_data["ExclusionFilters"]
        )

    ReportName = field("ReportName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheReportInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CacheReportInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachediSCSIVolume:
    boto3_raw_data: "type_defs.CachediSCSIVolumeTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")
    VolumeId = field("VolumeId")
    VolumeType = field("VolumeType")
    VolumeStatus = field("VolumeStatus")
    VolumeAttachmentStatus = field("VolumeAttachmentStatus")
    VolumeSizeInBytes = field("VolumeSizeInBytes")
    VolumeProgress = field("VolumeProgress")
    SourceSnapshotId = field("SourceSnapshotId")

    @cached_property
    def VolumeiSCSIAttributes(self):  # pragma: no cover
        return VolumeiSCSIAttributes.make_one(
            self.boto3_raw_data["VolumeiSCSIAttributes"]
        )

    CreatedDate = field("CreatedDate")
    VolumeUsedInBytes = field("VolumeUsedInBytes")
    KMSKey = field("KMSKey")
    TargetName = field("TargetName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CachediSCSIVolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachediSCSIVolumeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorediSCSIVolume:
    boto3_raw_data: "type_defs.StorediSCSIVolumeTypeDef" = dataclasses.field()

    VolumeARN = field("VolumeARN")
    VolumeId = field("VolumeId")
    VolumeType = field("VolumeType")
    VolumeStatus = field("VolumeStatus")
    VolumeAttachmentStatus = field("VolumeAttachmentStatus")
    VolumeSizeInBytes = field("VolumeSizeInBytes")
    VolumeProgress = field("VolumeProgress")
    VolumeDiskId = field("VolumeDiskId")
    SourceSnapshotId = field("SourceSnapshotId")
    PreservedExistingData = field("PreservedExistingData")

    @cached_property
    def VolumeiSCSIAttributes(self):  # pragma: no cover
        return VolumeiSCSIAttributes.make_one(
            self.boto3_raw_data["VolumeiSCSIAttributes"]
        )

    CreatedDate = field("CreatedDate")
    VolumeUsedInBytes = field("VolumeUsedInBytes")
    KMSKey = field("KMSKey")
    TargetName = field("TargetName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorediSCSIVolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorediSCSIVolumeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChapCredentialsOutput:
    boto3_raw_data: "type_defs.DescribeChapCredentialsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChapCredentials(self):  # pragma: no cover
        return ChapInfo.make_many(self.boto3_raw_data["ChapCredentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeChapCredentialsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChapCredentialsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNFSFileShareInput:
    boto3_raw_data: "type_defs.CreateNFSFileShareInputTypeDef" = dataclasses.field()

    ClientToken = field("ClientToken")
    GatewayARN = field("GatewayARN")
    Role = field("Role")
    LocationARN = field("LocationARN")

    @cached_property
    def NFSFileShareDefaults(self):  # pragma: no cover
        return NFSFileShareDefaults.make_one(
            self.boto3_raw_data["NFSFileShareDefaults"]
        )

    EncryptionType = field("EncryptionType")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")
    DefaultStorageClass = field("DefaultStorageClass")
    ObjectACL = field("ObjectACL")
    ClientList = field("ClientList")
    Squash = field("Squash")
    ReadOnly = field("ReadOnly")
    GuessMIMETypeEnabled = field("GuessMIMETypeEnabled")
    RequesterPays = field("RequesterPays")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    FileShareName = field("FileShareName")

    @cached_property
    def CacheAttributes(self):  # pragma: no cover
        return CacheAttributes.make_one(self.boto3_raw_data["CacheAttributes"])

    NotificationPolicy = field("NotificationPolicy")
    VPCEndpointDNSName = field("VPCEndpointDNSName")
    BucketRegion = field("BucketRegion")
    AuditDestinationARN = field("AuditDestinationARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNFSFileShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNFSFileShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NFSFileShareInfo:
    boto3_raw_data: "type_defs.NFSFileShareInfoTypeDef" = dataclasses.field()

    @cached_property
    def NFSFileShareDefaults(self):  # pragma: no cover
        return NFSFileShareDefaults.make_one(
            self.boto3_raw_data["NFSFileShareDefaults"]
        )

    FileShareARN = field("FileShareARN")
    FileShareId = field("FileShareId")
    FileShareStatus = field("FileShareStatus")
    GatewayARN = field("GatewayARN")
    EncryptionType = field("EncryptionType")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")
    Path = field("Path")
    Role = field("Role")
    LocationARN = field("LocationARN")
    DefaultStorageClass = field("DefaultStorageClass")
    ObjectACL = field("ObjectACL")
    ClientList = field("ClientList")
    Squash = field("Squash")
    ReadOnly = field("ReadOnly")
    GuessMIMETypeEnabled = field("GuessMIMETypeEnabled")
    RequesterPays = field("RequesterPays")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    FileShareName = field("FileShareName")

    @cached_property
    def CacheAttributes(self):  # pragma: no cover
        return CacheAttributes.make_one(self.boto3_raw_data["CacheAttributes"])

    NotificationPolicy = field("NotificationPolicy")
    VPCEndpointDNSName = field("VPCEndpointDNSName")
    BucketRegion = field("BucketRegion")
    AuditDestinationARN = field("AuditDestinationARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NFSFileShareInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NFSFileShareInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNFSFileShareInput:
    boto3_raw_data: "type_defs.UpdateNFSFileShareInputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")
    EncryptionType = field("EncryptionType")
    KMSEncrypted = field("KMSEncrypted")
    KMSKey = field("KMSKey")

    @cached_property
    def NFSFileShareDefaults(self):  # pragma: no cover
        return NFSFileShareDefaults.make_one(
            self.boto3_raw_data["NFSFileShareDefaults"]
        )

    DefaultStorageClass = field("DefaultStorageClass")
    ObjectACL = field("ObjectACL")
    ClientList = field("ClientList")
    Squash = field("Squash")
    ReadOnly = field("ReadOnly")
    GuessMIMETypeEnabled = field("GuessMIMETypeEnabled")
    RequesterPays = field("RequesterPays")
    FileShareName = field("FileShareName")

    @cached_property
    def CacheAttributes(self):  # pragma: no cover
        return CacheAttributes.make_one(self.boto3_raw_data["CacheAttributes"])

    NotificationPolicy = field("NotificationPolicy")
    AuditDestinationARN = field("AuditDestinationARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNFSFileShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNFSFileShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayInformationOutput:
    boto3_raw_data: "type_defs.DescribeGatewayInformationOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    GatewayId = field("GatewayId")
    GatewayName = field("GatewayName")
    GatewayTimezone = field("GatewayTimezone")
    GatewayState = field("GatewayState")

    @cached_property
    def GatewayNetworkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(
            self.boto3_raw_data["GatewayNetworkInterfaces"]
        )

    GatewayType = field("GatewayType")
    NextUpdateAvailabilityDate = field("NextUpdateAvailabilityDate")
    LastSoftwareUpdate = field("LastSoftwareUpdate")
    Ec2InstanceId = field("Ec2InstanceId")
    Ec2InstanceRegion = field("Ec2InstanceRegion")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    VPCEndpoint = field("VPCEndpoint")
    CloudWatchLogGroupARN = field("CloudWatchLogGroupARN")
    HostEnvironment = field("HostEnvironment")
    EndpointType = field("EndpointType")
    SoftwareUpdatesEndDate = field("SoftwareUpdatesEndDate")
    DeprecationDate = field("DeprecationDate")
    GatewayCapacity = field("GatewayCapacity")
    SupportedGatewayCapacities = field("SupportedGatewayCapacities")
    HostEnvironmentId = field("HostEnvironmentId")
    SoftwareVersion = field("SoftwareVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGatewayInformationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayInformationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceStartTimeOutput:
    boto3_raw_data: "type_defs.DescribeMaintenanceStartTimeOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    HourOfDay = field("HourOfDay")
    MinuteOfHour = field("MinuteOfHour")
    DayOfWeek = field("DayOfWeek")
    DayOfMonth = field("DayOfMonth")
    Timezone = field("Timezone")

    @cached_property
    def SoftwareUpdatePreferences(self):  # pragma: no cover
        return SoftwareUpdatePreferences.make_one(
            self.boto3_raw_data["SoftwareUpdatePreferences"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceStartTimeOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceStartTimeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMaintenanceStartTimeInput:
    boto3_raw_data: "type_defs.UpdateMaintenanceStartTimeInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    HourOfDay = field("HourOfDay")
    MinuteOfHour = field("MinuteOfHour")
    DayOfWeek = field("DayOfWeek")
    DayOfMonth = field("DayOfMonth")

    @cached_property
    def SoftwareUpdatePreferences(self):  # pragma: no cover
        return SoftwareUpdatePreferences.make_one(
            self.boto3_raw_data["SoftwareUpdatePreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMaintenanceStartTimeInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMaintenanceStartTimeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSMBSettingsOutput:
    boto3_raw_data: "type_defs.DescribeSMBSettingsOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    DomainName = field("DomainName")
    ActiveDirectoryStatus = field("ActiveDirectoryStatus")
    SMBGuestPasswordSet = field("SMBGuestPasswordSet")
    SMBSecurityStrategy = field("SMBSecurityStrategy")
    FileSharesVisible = field("FileSharesVisible")

    @cached_property
    def SMBLocalGroups(self):  # pragma: no cover
        return SMBLocalGroupsOutput.make_one(self.boto3_raw_data["SMBLocalGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSMBSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSMBSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTapeArchivesInputPaginate:
    boto3_raw_data: "type_defs.DescribeTapeArchivesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    TapeARNs = field("TapeARNs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTapeArchivesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTapeArchivesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTapeRecoveryPointsInputPaginate:
    boto3_raw_data: "type_defs.DescribeTapeRecoveryPointsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTapeRecoveryPointsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTapeRecoveryPointsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTapesInputPaginate:
    boto3_raw_data: "type_defs.DescribeTapesInputPaginateTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    TapeARNs = field("TapeARNs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTapesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTapesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVTLDevicesInputPaginate:
    boto3_raw_data: "type_defs.DescribeVTLDevicesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    VTLDeviceARNs = field("VTLDeviceARNs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeVTLDevicesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVTLDevicesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCacheReportsInputPaginate:
    boto3_raw_data: "type_defs.ListCacheReportsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCacheReportsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCacheReportsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileSharesInputPaginate:
    boto3_raw_data: "type_defs.ListFileSharesInputPaginateTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFileSharesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileSharesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileSystemAssociationsInputPaginate:
    boto3_raw_data: "type_defs.ListFileSystemAssociationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFileSystemAssociationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileSystemAssociationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysInputPaginate:
    boto3_raw_data: "type_defs.ListGatewaysInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInputPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTapePoolsInputPaginate:
    boto3_raw_data: "type_defs.ListTapePoolsInputPaginateTypeDef" = dataclasses.field()

    PoolARNs = field("PoolARNs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTapePoolsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTapePoolsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTapesInputPaginate:
    boto3_raw_data: "type_defs.ListTapesInputPaginateTypeDef" = dataclasses.field()

    TapeARNs = field("TapeARNs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTapesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTapesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVolumesInputPaginate:
    boto3_raw_data: "type_defs.ListVolumesInputPaginateTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVolumesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVolumesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTapeArchivesOutput:
    boto3_raw_data: "type_defs.DescribeTapeArchivesOutputTypeDef" = dataclasses.field()

    @cached_property
    def TapeArchives(self):  # pragma: no cover
        return TapeArchive.make_many(self.boto3_raw_data["TapeArchives"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTapeArchivesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTapeArchivesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTapeRecoveryPointsOutput:
    boto3_raw_data: "type_defs.DescribeTapeRecoveryPointsOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def TapeRecoveryPointInfos(self):  # pragma: no cover
        return TapeRecoveryPointInfo.make_many(
            self.boto3_raw_data["TapeRecoveryPointInfos"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTapeRecoveryPointsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTapeRecoveryPointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTapesOutput:
    boto3_raw_data: "type_defs.DescribeTapesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Tapes(self):  # pragma: no cover
        return Tape.make_many(self.boto3_raw_data["Tapes"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTapesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTapesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VTLDevice:
    boto3_raw_data: "type_defs.VTLDeviceTypeDef" = dataclasses.field()

    VTLDeviceARN = field("VTLDeviceARN")
    VTLDeviceType = field("VTLDeviceType")
    VTLDeviceVendor = field("VTLDeviceVendor")
    VTLDeviceProductIdentifier = field("VTLDeviceProductIdentifier")

    @cached_property
    def DeviceiSCSIAttributes(self):  # pragma: no cover
        return DeviceiSCSIAttributes.make_one(
            self.boto3_raw_data["DeviceiSCSIAttributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VTLDeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VTLDeviceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLocalDisksOutput:
    boto3_raw_data: "type_defs.ListLocalDisksOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def Disks(self):  # pragma: no cover
        return Disk.make_many(self.boto3_raw_data["Disks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLocalDisksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLocalDisksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileSharesOutput:
    boto3_raw_data: "type_defs.ListFileSharesOutputTypeDef" = dataclasses.field()

    Marker = field("Marker")
    NextMarker = field("NextMarker")

    @cached_property
    def FileShareInfoList(self):  # pragma: no cover
        return FileShareInfo.make_many(self.boto3_raw_data["FileShareInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFileSharesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileSharesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemAssociationInfo:
    boto3_raw_data: "type_defs.FileSystemAssociationInfoTypeDef" = dataclasses.field()

    FileSystemAssociationARN = field("FileSystemAssociationARN")
    LocationARN = field("LocationARN")
    FileSystemAssociationStatus = field("FileSystemAssociationStatus")
    AuditDestinationARN = field("AuditDestinationARN")
    GatewayARN = field("GatewayARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def CacheAttributes(self):  # pragma: no cover
        return CacheAttributes.make_one(self.boto3_raw_data["CacheAttributes"])

    @cached_property
    def EndpointNetworkConfiguration(self):  # pragma: no cover
        return EndpointNetworkConfigurationOutput.make_one(
            self.boto3_raw_data["EndpointNetworkConfiguration"]
        )

    @cached_property
    def FileSystemAssociationStatusDetails(self):  # pragma: no cover
        return FileSystemAssociationStatusDetail.make_many(
            self.boto3_raw_data["FileSystemAssociationStatusDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSystemAssociationInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemAssociationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileSystemAssociationsOutput:
    boto3_raw_data: "type_defs.ListFileSystemAssociationsOutputTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    NextMarker = field("NextMarker")

    @cached_property
    def FileSystemAssociationSummaryList(self):  # pragma: no cover
        return FileSystemAssociationSummary.make_many(
            self.boto3_raw_data["FileSystemAssociationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFileSystemAssociationsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileSystemAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysOutput:
    boto3_raw_data: "type_defs.ListGatewaysOutputTypeDef" = dataclasses.field()

    @cached_property
    def Gateways(self):  # pragma: no cover
        return GatewayInfo.make_many(self.boto3_raw_data["Gateways"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTapePoolsOutput:
    boto3_raw_data: "type_defs.ListTapePoolsOutputTypeDef" = dataclasses.field()

    @cached_property
    def PoolInfos(self):  # pragma: no cover
        return PoolInfo.make_many(self.boto3_raw_data["PoolInfos"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTapePoolsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTapePoolsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTapesOutput:
    boto3_raw_data: "type_defs.ListTapesOutputTypeDef" = dataclasses.field()

    @cached_property
    def TapeInfos(self):  # pragma: no cover
        return TapeInfo.make_many(self.boto3_raw_data["TapeInfos"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTapesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTapesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVolumeRecoveryPointsOutput:
    boto3_raw_data: "type_defs.ListVolumeRecoveryPointsOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")

    @cached_property
    def VolumeRecoveryPointInfos(self):  # pragma: no cover
        return VolumeRecoveryPointInfo.make_many(
            self.boto3_raw_data["VolumeRecoveryPointInfos"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVolumeRecoveryPointsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVolumeRecoveryPointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVolumesOutput:
    boto3_raw_data: "type_defs.ListVolumesOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    Marker = field("Marker")

    @cached_property
    def VolumeInfos(self):  # pragma: no cover
        return VolumeInfo.make_many(self.boto3_raw_data["VolumeInfos"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListVolumesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVolumesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSMBFileSharesOutput:
    boto3_raw_data: "type_defs.DescribeSMBFileSharesOutputTypeDef" = dataclasses.field()

    @cached_property
    def SMBFileShareInfoList(self):  # pragma: no cover
        return SMBFileShareInfo.make_many(self.boto3_raw_data["SMBFileShareInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSMBFileSharesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSMBFileSharesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomaticTapeCreationPoliciesOutput:
    boto3_raw_data: "type_defs.ListAutomaticTapeCreationPoliciesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutomaticTapeCreationPolicyInfos(self):  # pragma: no cover
        return AutomaticTapeCreationPolicyInfo.make_many(
            self.boto3_raw_data["AutomaticTapeCreationPolicyInfos"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomaticTapeCreationPoliciesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomaticTapeCreationPoliciesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBandwidthRateLimitScheduleInput:
    boto3_raw_data: "type_defs.UpdateBandwidthRateLimitScheduleInputTypeDef" = (
        dataclasses.field()
    )

    GatewayARN = field("GatewayARN")
    BandwidthRateLimitIntervals = field("BandwidthRateLimitIntervals")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBandwidthRateLimitScheduleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBandwidthRateLimitScheduleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheReportOutput:
    boto3_raw_data: "type_defs.DescribeCacheReportOutputTypeDef" = dataclasses.field()

    @cached_property
    def CacheReportInfo(self):  # pragma: no cover
        return CacheReportInfo.make_one(self.boto3_raw_data["CacheReportInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCacheReportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheReportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCacheReportsOutput:
    boto3_raw_data: "type_defs.ListCacheReportsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CacheReportList(self):  # pragma: no cover
        return CacheReportInfo.make_many(self.boto3_raw_data["CacheReportList"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCacheReportsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCacheReportsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCacheReportInput:
    boto3_raw_data: "type_defs.StartCacheReportInputTypeDef" = dataclasses.field()

    FileShareARN = field("FileShareARN")
    Role = field("Role")
    LocationARN = field("LocationARN")
    BucketRegion = field("BucketRegion")
    ClientToken = field("ClientToken")
    VPCEndpointDNSName = field("VPCEndpointDNSName")
    InclusionFilters = field("InclusionFilters")
    ExclusionFilters = field("ExclusionFilters")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCacheReportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCacheReportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCachediSCSIVolumesOutput:
    boto3_raw_data: "type_defs.DescribeCachediSCSIVolumesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CachediSCSIVolumes(self):  # pragma: no cover
        return CachediSCSIVolume.make_many(self.boto3_raw_data["CachediSCSIVolumes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCachediSCSIVolumesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCachediSCSIVolumesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStorediSCSIVolumesOutput:
    boto3_raw_data: "type_defs.DescribeStorediSCSIVolumesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StorediSCSIVolumes(self):  # pragma: no cover
        return StorediSCSIVolume.make_many(self.boto3_raw_data["StorediSCSIVolumes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStorediSCSIVolumesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStorediSCSIVolumesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNFSFileSharesOutput:
    boto3_raw_data: "type_defs.DescribeNFSFileSharesOutputTypeDef" = dataclasses.field()

    @cached_property
    def NFSFileShareInfoList(self):  # pragma: no cover
        return NFSFileShareInfo.make_many(self.boto3_raw_data["NFSFileShareInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNFSFileSharesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNFSFileSharesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVTLDevicesOutput:
    boto3_raw_data: "type_defs.DescribeVTLDevicesOutputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")

    @cached_property
    def VTLDevices(self):  # pragma: no cover
        return VTLDevice.make_many(self.boto3_raw_data["VTLDevices"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVTLDevicesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVTLDevicesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFileSystemInput:
    boto3_raw_data: "type_defs.AssociateFileSystemInputTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Password = field("Password")
    ClientToken = field("ClientToken")
    GatewayARN = field("GatewayARN")
    LocationARN = field("LocationARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AuditDestinationARN = field("AuditDestinationARN")

    @cached_property
    def CacheAttributes(self):  # pragma: no cover
        return CacheAttributes.make_one(self.boto3_raw_data["CacheAttributes"])

    EndpointNetworkConfiguration = field("EndpointNetworkConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateFileSystemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFileSystemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemAssociationsOutput:
    boto3_raw_data: "type_defs.DescribeFileSystemAssociationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FileSystemAssociationInfoList(self):  # pragma: no cover
        return FileSystemAssociationInfo.make_many(
            self.boto3_raw_data["FileSystemAssociationInfoList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFileSystemAssociationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSMBLocalGroupsInput:
    boto3_raw_data: "type_defs.UpdateSMBLocalGroupsInputTypeDef" = dataclasses.field()

    GatewayARN = field("GatewayARN")
    SMBLocalGroups = field("SMBLocalGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSMBLocalGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSMBLocalGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
