# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesisanalyticsv2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CloudWatchLoggingOption:
    boto3_raw_data: "type_defs.CloudWatchLoggingOptionTypeDef" = dataclasses.field()

    LogStreamARN = field("LogStreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLoggingOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLoggingOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLoggingOptionDescription:
    boto3_raw_data: "type_defs.CloudWatchLoggingOptionDescriptionTypeDef" = (
        dataclasses.field()
    )

    LogStreamARN = field("LogStreamARN")
    CloudWatchLoggingOptionId = field("CloudWatchLoggingOptionId")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudWatchLoggingOptionDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLoggingOptionDescriptionTypeDef"]
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
class VpcConfiguration:
    boto3_raw_data: "type_defs.VpcConfigurationTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigurationDescription:
    boto3_raw_data: "type_defs.VpcConfigurationDescriptionTypeDef" = dataclasses.field()

    VpcConfigurationId = field("VpcConfigurationId")
    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationEncryptionConfigurationDescription:
    boto3_raw_data: "type_defs.ApplicationEncryptionConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    KeyType = field("KeyType")
    KeyId = field("KeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationEncryptionConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationEncryptionConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSnapshotConfigurationDescription:
    boto3_raw_data: "type_defs.ApplicationSnapshotConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    SnapshotsEnabled = field("SnapshotsEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationSnapshotConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSnapshotConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSystemRollbackConfigurationDescription:
    boto3_raw_data: (
        "type_defs.ApplicationSystemRollbackConfigurationDescriptionTypeDef"
    ) = dataclasses.field()

    RollbackEnabled = field("RollbackEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationSystemRollbackConfigurationDescriptionTypeDef"
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
                "type_defs.ApplicationSystemRollbackConfigurationDescriptionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationEncryptionConfiguration:
    boto3_raw_data: "type_defs.ApplicationEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    KeyType = field("KeyType")
    KeyId = field("KeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSnapshotConfiguration:
    boto3_raw_data: "type_defs.ApplicationSnapshotConfigurationTypeDef" = (
        dataclasses.field()
    )

    SnapshotsEnabled = field("SnapshotsEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationSnapshotConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSnapshotConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSystemRollbackConfiguration:
    boto3_raw_data: "type_defs.ApplicationSystemRollbackConfigurationTypeDef" = (
        dataclasses.field()
    )

    RollbackEnabled = field("RollbackEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationSystemRollbackConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSystemRollbackConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationEncryptionConfigurationUpdate:
    boto3_raw_data: "type_defs.ApplicationEncryptionConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    KeyTypeUpdate = field("KeyTypeUpdate")
    KeyIdUpdate = field("KeyIdUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationEncryptionConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationEncryptionConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSnapshotConfigurationUpdate:
    boto3_raw_data: "type_defs.ApplicationSnapshotConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    SnapshotsEnabledUpdate = field("SnapshotsEnabledUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationSnapshotConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSnapshotConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSystemRollbackConfigurationUpdate:
    boto3_raw_data: "type_defs.ApplicationSystemRollbackConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    RollbackEnabledUpdate = field("RollbackEnabledUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationSystemRollbackConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSystemRollbackConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigurationUpdate:
    boto3_raw_data: "type_defs.VpcConfigurationUpdateTypeDef" = dataclasses.field()

    VpcConfigurationId = field("VpcConfigurationId")
    SubnetIdUpdates = field("SubnetIdUpdates")
    SecurityGroupIdUpdates = field("SecurityGroupIdUpdates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationMaintenanceConfigurationDescription:
    boto3_raw_data: (
        "type_defs.ApplicationMaintenanceConfigurationDescriptionTypeDef"
    ) = dataclasses.field()

    ApplicationMaintenanceWindowStartTime = field(
        "ApplicationMaintenanceWindowStartTime"
    )
    ApplicationMaintenanceWindowEndTime = field("ApplicationMaintenanceWindowEndTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationMaintenanceConfigurationDescriptionTypeDef"
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
                "type_defs.ApplicationMaintenanceConfigurationDescriptionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationMaintenanceConfigurationUpdate:
    boto3_raw_data: "type_defs.ApplicationMaintenanceConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    ApplicationMaintenanceWindowStartTimeUpdate = field(
        "ApplicationMaintenanceWindowStartTimeUpdate"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationMaintenanceConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationMaintenanceConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationVersionChangeDetails:
    boto3_raw_data: "type_defs.ApplicationVersionChangeDetailsTypeDef" = (
        dataclasses.field()
    )

    ApplicationVersionUpdatedFrom = field("ApplicationVersionUpdatedFrom")
    ApplicationVersionUpdatedTo = field("ApplicationVersionUpdatedTo")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationVersionChangeDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationVersionChangeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationOperationInfo:
    boto3_raw_data: "type_defs.ApplicationOperationInfoTypeDef" = dataclasses.field()

    Operation = field("Operation")
    OperationId = field("OperationId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    OperationStatus = field("OperationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationOperationInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationOperationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationRestoreConfiguration:
    boto3_raw_data: "type_defs.ApplicationRestoreConfigurationTypeDef" = (
        dataclasses.field()
    )

    ApplicationRestoreType = field("ApplicationRestoreType")
    SnapshotName = field("SnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationRestoreConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationRestoreConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSummary:
    boto3_raw_data: "type_defs.ApplicationSummaryTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    ApplicationARN = field("ApplicationARN")
    ApplicationStatus = field("ApplicationStatus")
    ApplicationVersionId = field("ApplicationVersionId")
    RuntimeEnvironment = field("RuntimeEnvironment")
    ApplicationMode = field("ApplicationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationVersionSummary:
    boto3_raw_data: "type_defs.ApplicationVersionSummaryTypeDef" = dataclasses.field()

    ApplicationVersionId = field("ApplicationVersionId")
    ApplicationStatus = field("ApplicationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CSVMappingParameters:
    boto3_raw_data: "type_defs.CSVMappingParametersTypeDef" = dataclasses.field()

    RecordRowDelimiter = field("RecordRowDelimiter")
    RecordColumnDelimiter = field("RecordColumnDelimiter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CSVMappingParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CSVMappingParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueDataCatalogConfigurationDescription:
    boto3_raw_data: "type_defs.GlueDataCatalogConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    DatabaseARN = field("DatabaseARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GlueDataCatalogConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueDataCatalogConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueDataCatalogConfiguration:
    boto3_raw_data: "type_defs.GlueDataCatalogConfigurationTypeDef" = (
        dataclasses.field()
    )

    DatabaseARN = field("DatabaseARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlueDataCatalogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueDataCatalogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueDataCatalogConfigurationUpdate:
    boto3_raw_data: "type_defs.GlueDataCatalogConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    DatabaseARNUpdate = field("DatabaseARNUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GlueDataCatalogConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueDataCatalogConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckpointConfigurationDescription:
    boto3_raw_data: "type_defs.CheckpointConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    ConfigurationType = field("ConfigurationType")
    CheckpointingEnabled = field("CheckpointingEnabled")
    CheckpointInterval = field("CheckpointInterval")
    MinPauseBetweenCheckpoints = field("MinPauseBetweenCheckpoints")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CheckpointConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckpointConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckpointConfiguration:
    boto3_raw_data: "type_defs.CheckpointConfigurationTypeDef" = dataclasses.field()

    ConfigurationType = field("ConfigurationType")
    CheckpointingEnabled = field("CheckpointingEnabled")
    CheckpointInterval = field("CheckpointInterval")
    MinPauseBetweenCheckpoints = field("MinPauseBetweenCheckpoints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckpointConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckpointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckpointConfigurationUpdate:
    boto3_raw_data: "type_defs.CheckpointConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    ConfigurationTypeUpdate = field("ConfigurationTypeUpdate")
    CheckpointingEnabledUpdate = field("CheckpointingEnabledUpdate")
    CheckpointIntervalUpdate = field("CheckpointIntervalUpdate")
    MinPauseBetweenCheckpointsUpdate = field("MinPauseBetweenCheckpointsUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CheckpointConfigurationUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckpointConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLoggingOptionUpdate:
    boto3_raw_data: "type_defs.CloudWatchLoggingOptionUpdateTypeDef" = (
        dataclasses.field()
    )

    CloudWatchLoggingOptionId = field("CloudWatchLoggingOptionId")
    LogStreamARNUpdate = field("LogStreamARNUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchLoggingOptionUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLoggingOptionUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ApplicationCodeLocationDescription:
    boto3_raw_data: "type_defs.S3ApplicationCodeLocationDescriptionTypeDef" = (
        dataclasses.field()
    )

    BucketARN = field("BucketARN")
    FileKey = field("FileKey")
    ObjectVersion = field("ObjectVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3ApplicationCodeLocationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ApplicationCodeLocationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ContentLocation:
    boto3_raw_data: "type_defs.S3ContentLocationTypeDef" = dataclasses.field()

    BucketARN = field("BucketARN")
    FileKey = field("FileKey")
    ObjectVersion = field("ObjectVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ContentLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ContentLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ContentLocationUpdate:
    boto3_raw_data: "type_defs.S3ContentLocationUpdateTypeDef" = dataclasses.field()

    BucketARNUpdate = field("BucketARNUpdate")
    FileKeyUpdate = field("FileKeyUpdate")
    ObjectVersionUpdate = field("ObjectVersionUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ContentLocationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ContentLocationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationPresignedUrlRequest:
    boto3_raw_data: "type_defs.CreateApplicationPresignedUrlRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    UrlType = field("UrlType")
    SessionExpirationDurationInSeconds = field("SessionExpirationDurationInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateApplicationPresignedUrlRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationPresignedUrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


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
class CreateApplicationSnapshotRequest:
    boto3_raw_data: "type_defs.CreateApplicationSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    SnapshotName = field("SnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateApplicationSnapshotRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MavenReference:
    boto3_raw_data: "type_defs.MavenReferenceTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    ArtifactId = field("ArtifactId")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MavenReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MavenReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationCloudWatchLoggingOptionRequest:
    boto3_raw_data: (
        "type_defs.DeleteApplicationCloudWatchLoggingOptionRequestTypeDef"
    ) = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CloudWatchLoggingOptionId = field("CloudWatchLoggingOptionId")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    ConditionalToken = field("ConditionalToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationCloudWatchLoggingOptionRequestTypeDef"
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
                "type_defs.DeleteApplicationCloudWatchLoggingOptionRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationInputProcessingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteApplicationInputProcessingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    InputId = field("InputId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationInputProcessingConfigurationRequestTypeDef"
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
                "type_defs.DeleteApplicationInputProcessingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationOutputRequest:
    boto3_raw_data: "type_defs.DeleteApplicationOutputRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    OutputId = field("OutputId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApplicationOutputRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationReferenceDataSourceRequest:
    boto3_raw_data: "type_defs.DeleteApplicationReferenceDataSourceRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    ReferenceId = field("ReferenceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationReferenceDataSourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationReferenceDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationVpcConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteApplicationVpcConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VpcConfigurationId = field("VpcConfigurationId")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    ConditionalToken = field("ConditionalToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationVpcConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationVpcConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ContentBaseLocationDescription:
    boto3_raw_data: "type_defs.S3ContentBaseLocationDescriptionTypeDef" = (
        dataclasses.field()
    )

    BucketARN = field("BucketARN")
    BasePath = field("BasePath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3ContentBaseLocationDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ContentBaseLocationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ContentBaseLocation:
    boto3_raw_data: "type_defs.S3ContentBaseLocationTypeDef" = dataclasses.field()

    BucketARN = field("BucketARN")
    BasePath = field("BasePath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ContentBaseLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ContentBaseLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ContentBaseLocationUpdate:
    boto3_raw_data: "type_defs.S3ContentBaseLocationUpdateTypeDef" = dataclasses.field()

    BucketARNUpdate = field("BucketARNUpdate")
    BasePathUpdate = field("BasePathUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ContentBaseLocationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ContentBaseLocationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationOperationRequest:
    boto3_raw_data: "type_defs.DescribeApplicationOperationRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    OperationId = field("OperationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationOperationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationRequest:
    boto3_raw_data: "type_defs.DescribeApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    IncludeAdditionalDetails = field("IncludeAdditionalDetails")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationSnapshotRequest:
    boto3_raw_data: "type_defs.DescribeApplicationSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    SnapshotName = field("SnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationVersionRequest:
    boto3_raw_data: "type_defs.DescribeApplicationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    ApplicationVersionId = field("ApplicationVersionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationSchema:
    boto3_raw_data: "type_defs.DestinationSchemaTypeDef" = dataclasses.field()

    RecordFormatType = field("RecordFormatType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputStartingPositionConfiguration:
    boto3_raw_data: "type_defs.InputStartingPositionConfigurationTypeDef" = (
        dataclasses.field()
    )

    InputStartingPosition = field("InputStartingPosition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputStartingPositionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputStartingPositionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Configuration:
    boto3_raw_data: "type_defs.S3ConfigurationTypeDef" = dataclasses.field()

    BucketARN = field("BucketARN")
    FileKey = field("FileKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyGroupOutput:
    boto3_raw_data: "type_defs.PropertyGroupOutputTypeDef" = dataclasses.field()

    PropertyGroupId = field("PropertyGroupId")
    PropertyMap = field("PropertyMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorInfo:
    boto3_raw_data: "type_defs.ErrorInfoTypeDef" = dataclasses.field()

    ErrorString = field("ErrorString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoringConfigurationDescription:
    boto3_raw_data: "type_defs.MonitoringConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    ConfigurationType = field("ConfigurationType")
    MetricsLevel = field("MetricsLevel")
    LogLevel = field("LogLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MonitoringConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoringConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParallelismConfigurationDescription:
    boto3_raw_data: "type_defs.ParallelismConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    ConfigurationType = field("ConfigurationType")
    Parallelism = field("Parallelism")
    ParallelismPerKPU = field("ParallelismPerKPU")
    CurrentParallelism = field("CurrentParallelism")
    AutoScalingEnabled = field("AutoScalingEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParallelismConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParallelismConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoringConfiguration:
    boto3_raw_data: "type_defs.MonitoringConfigurationTypeDef" = dataclasses.field()

    ConfigurationType = field("ConfigurationType")
    MetricsLevel = field("MetricsLevel")
    LogLevel = field("LogLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitoringConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParallelismConfiguration:
    boto3_raw_data: "type_defs.ParallelismConfigurationTypeDef" = dataclasses.field()

    ConfigurationType = field("ConfigurationType")
    Parallelism = field("Parallelism")
    ParallelismPerKPU = field("ParallelismPerKPU")
    AutoScalingEnabled = field("AutoScalingEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParallelismConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParallelismConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoringConfigurationUpdate:
    boto3_raw_data: "type_defs.MonitoringConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    ConfigurationTypeUpdate = field("ConfigurationTypeUpdate")
    MetricsLevelUpdate = field("MetricsLevelUpdate")
    LogLevelUpdate = field("LogLevelUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MonitoringConfigurationUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoringConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParallelismConfigurationUpdate:
    boto3_raw_data: "type_defs.ParallelismConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    ConfigurationTypeUpdate = field("ConfigurationTypeUpdate")
    ParallelismUpdate = field("ParallelismUpdate")
    ParallelismPerKPUUpdate = field("ParallelismPerKPUUpdate")
    AutoScalingEnabledUpdate = field("AutoScalingEnabledUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ParallelismConfigurationUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParallelismConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlinkRunConfiguration:
    boto3_raw_data: "type_defs.FlinkRunConfigurationTypeDef" = dataclasses.field()

    AllowNonRestoredState = field("AllowNonRestoredState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlinkRunConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlinkRunConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputParallelism:
    boto3_raw_data: "type_defs.InputParallelismTypeDef" = dataclasses.field()

    Count = field("Count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputParallelismTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputParallelismTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseInputDescription:
    boto3_raw_data: "type_defs.KinesisFirehoseInputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisFirehoseInputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseInputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsInputDescription:
    boto3_raw_data: "type_defs.KinesisStreamsInputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisStreamsInputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsInputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputLambdaProcessorDescription:
    boto3_raw_data: "type_defs.InputLambdaProcessorDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InputLambdaProcessorDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputLambdaProcessorDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputLambdaProcessor:
    boto3_raw_data: "type_defs.InputLambdaProcessorTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputLambdaProcessorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputLambdaProcessorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputLambdaProcessorUpdate:
    boto3_raw_data: "type_defs.InputLambdaProcessorUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputLambdaProcessorUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputLambdaProcessorUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputParallelismUpdate:
    boto3_raw_data: "type_defs.InputParallelismUpdateTypeDef" = dataclasses.field()

    CountUpdate = field("CountUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputParallelismUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputParallelismUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordColumn:
    boto3_raw_data: "type_defs.RecordColumnTypeDef" = dataclasses.field()

    Name = field("Name")
    SqlType = field("SqlType")
    Mapping = field("Mapping")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordColumnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordColumnTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseInput:
    boto3_raw_data: "type_defs.KinesisFirehoseInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsInput:
    boto3_raw_data: "type_defs.KinesisStreamsInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseInputUpdate:
    boto3_raw_data: "type_defs.KinesisFirehoseInputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseInputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseInputUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsInputUpdate:
    boto3_raw_data: "type_defs.KinesisStreamsInputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamsInputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsInputUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JSONMappingParameters:
    boto3_raw_data: "type_defs.JSONMappingParametersTypeDef" = dataclasses.field()

    RecordRowPath = field("RecordRowPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JSONMappingParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JSONMappingParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseOutputDescription:
    boto3_raw_data: "type_defs.KinesisFirehoseOutputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisFirehoseOutputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseOutputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseOutput:
    boto3_raw_data: "type_defs.KinesisFirehoseOutputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseOutputUpdate:
    boto3_raw_data: "type_defs.KinesisFirehoseOutputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseOutputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseOutputUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsOutputDescription:
    boto3_raw_data: "type_defs.KinesisStreamsOutputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisStreamsOutputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsOutputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsOutput:
    boto3_raw_data: "type_defs.KinesisStreamsOutputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamsOutputUpdate:
    boto3_raw_data: "type_defs.KinesisStreamsOutputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamsOutputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamsOutputUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaOutputDescription:
    boto3_raw_data: "type_defs.LambdaOutputDescriptionTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaOutputDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaOutputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaOutput:
    boto3_raw_data: "type_defs.LambdaOutputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaOutputUpdate:
    boto3_raw_data: "type_defs.LambdaOutputUpdateTypeDef" = dataclasses.field()

    ResourceARNUpdate = field("ResourceARNUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaOutputUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaOutputUpdateTypeDef"]
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
class ListApplicationOperationsRequest:
    boto3_raw_data: "type_defs.ListApplicationOperationsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    Limit = field("Limit")
    NextToken = field("NextToken")
    Operation = field("Operation")
    OperationStatus = field("OperationStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationOperationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationSnapshotsRequest:
    boto3_raw_data: "type_defs.ListApplicationSnapshotsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationSnapshotsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationVersionsRequest:
    boto3_raw_data: "type_defs.ListApplicationVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class PropertyGroup:
    boto3_raw_data: "type_defs.PropertyGroupTypeDef" = dataclasses.field()

    PropertyGroupId = field("PropertyGroupId")
    PropertyMap = field("PropertyMap")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ReferenceDataSourceDescription:
    boto3_raw_data: "type_defs.S3ReferenceDataSourceDescriptionTypeDef" = (
        dataclasses.field()
    )

    BucketARN = field("BucketARN")
    FileKey = field("FileKey")
    ReferenceRoleARN = field("ReferenceRoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3ReferenceDataSourceDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ReferenceDataSourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ReferenceDataSource:
    boto3_raw_data: "type_defs.S3ReferenceDataSourceTypeDef" = dataclasses.field()

    BucketARN = field("BucketARN")
    FileKey = field("FileKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ReferenceDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ReferenceDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ReferenceDataSourceUpdate:
    boto3_raw_data: "type_defs.S3ReferenceDataSourceUpdateTypeDef" = dataclasses.field()

    BucketARNUpdate = field("BucketARNUpdate")
    FileKeyUpdate = field("FileKeyUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ReferenceDataSourceUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ReferenceDataSourceUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackApplicationRequest:
    boto3_raw_data: "type_defs.RollbackApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopApplicationRequest:
    boto3_raw_data: "type_defs.StopApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    Force = field("Force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopApplicationRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")
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
class ZeppelinMonitoringConfigurationDescription:
    boto3_raw_data: "type_defs.ZeppelinMonitoringConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    LogLevel = field("LogLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ZeppelinMonitoringConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZeppelinMonitoringConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZeppelinMonitoringConfiguration:
    boto3_raw_data: "type_defs.ZeppelinMonitoringConfigurationTypeDef" = (
        dataclasses.field()
    )

    LogLevel = field("LogLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ZeppelinMonitoringConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZeppelinMonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZeppelinMonitoringConfigurationUpdate:
    boto3_raw_data: "type_defs.ZeppelinMonitoringConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    LogLevelUpdate = field("LogLevelUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ZeppelinMonitoringConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZeppelinMonitoringConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationCloudWatchLoggingOptionRequest:
    boto3_raw_data: "type_defs.AddApplicationCloudWatchLoggingOptionRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")

    @cached_property
    def CloudWatchLoggingOption(self):  # pragma: no cover
        return CloudWatchLoggingOption.make_one(
            self.boto3_raw_data["CloudWatchLoggingOption"]
        )

    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    ConditionalToken = field("ConditionalToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationCloudWatchLoggingOptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationCloudWatchLoggingOptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationCloudWatchLoggingOptionResponse:
    boto3_raw_data: "type_defs.AddApplicationCloudWatchLoggingOptionResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")

    @cached_property
    def CloudWatchLoggingOptionDescriptions(self):  # pragma: no cover
        return CloudWatchLoggingOptionDescription.make_many(
            self.boto3_raw_data["CloudWatchLoggingOptionDescriptions"]
        )

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationCloudWatchLoggingOptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationCloudWatchLoggingOptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationPresignedUrlResponse:
    boto3_raw_data: "type_defs.CreateApplicationPresignedUrlResponseTypeDef" = (
        dataclasses.field()
    )

    AuthorizedUrl = field("AuthorizedUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateApplicationPresignedUrlResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationPresignedUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationCloudWatchLoggingOptionResponse:
    boto3_raw_data: (
        "type_defs.DeleteApplicationCloudWatchLoggingOptionResponseTypeDef"
    ) = dataclasses.field()

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")

    @cached_property
    def CloudWatchLoggingOptionDescriptions(self):  # pragma: no cover
        return CloudWatchLoggingOptionDescription.make_many(
            self.boto3_raw_data["CloudWatchLoggingOptionDescriptions"]
        )

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationCloudWatchLoggingOptionResponseTypeDef"
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
                "type_defs.DeleteApplicationCloudWatchLoggingOptionResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationInputProcessingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.DeleteApplicationInputProcessingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationInputProcessingConfigurationResponseTypeDef"
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
                "type_defs.DeleteApplicationInputProcessingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationOutputResponse:
    boto3_raw_data: "type_defs.DeleteApplicationOutputResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApplicationOutputResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationOutputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationReferenceDataSourceResponse:
    boto3_raw_data: "type_defs.DeleteApplicationReferenceDataSourceResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationReferenceDataSourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationReferenceDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationVpcConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteApplicationVpcConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")
    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationVpcConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationVpcConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartApplicationResponse:
    boto3_raw_data: "type_defs.StartApplicationResponseTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopApplicationResponse:
    boto3_raw_data: "type_defs.StopApplicationResponseTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationVpcConfigurationRequest:
    boto3_raw_data: "type_defs.AddApplicationVpcConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["VpcConfiguration"])

    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    ConditionalToken = field("ConditionalToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationVpcConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationVpcConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationVpcConfigurationResponse:
    boto3_raw_data: "type_defs.AddApplicationVpcConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")

    @cached_property
    def VpcConfigurationDescription(self):  # pragma: no cover
        return VpcConfigurationDescription.make_one(
            self.boto3_raw_data["VpcConfigurationDescription"]
        )

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationVpcConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationVpcConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotDetails:
    boto3_raw_data: "type_defs.SnapshotDetailsTypeDef" = dataclasses.field()

    SnapshotName = field("SnapshotName")
    SnapshotStatus = field("SnapshotStatus")
    ApplicationVersionId = field("ApplicationVersionId")
    SnapshotCreationTimestamp = field("SnapshotCreationTimestamp")
    RuntimeEnvironment = field("RuntimeEnvironment")

    @cached_property
    def ApplicationEncryptionConfigurationDescription(self):  # pragma: no cover
        return ApplicationEncryptionConfigurationDescription.make_one(
            self.boto3_raw_data["ApplicationEncryptionConfigurationDescription"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapshotDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationMaintenanceConfigurationResponse:
    boto3_raw_data: (
        "type_defs.UpdateApplicationMaintenanceConfigurationResponseTypeDef"
    ) = dataclasses.field()

    ApplicationARN = field("ApplicationARN")

    @cached_property
    def ApplicationMaintenanceConfigurationDescription(self):  # pragma: no cover
        return ApplicationMaintenanceConfigurationDescription.make_one(
            self.boto3_raw_data["ApplicationMaintenanceConfigurationDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApplicationMaintenanceConfigurationResponseTypeDef"
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
                "type_defs.UpdateApplicationMaintenanceConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationMaintenanceConfigurationRequest:
    boto3_raw_data: (
        "type_defs.UpdateApplicationMaintenanceConfigurationRequestTypeDef"
    ) = dataclasses.field()

    ApplicationName = field("ApplicationName")

    @cached_property
    def ApplicationMaintenanceConfigurationUpdate(self):  # pragma: no cover
        return ApplicationMaintenanceConfigurationUpdate.make_one(
            self.boto3_raw_data["ApplicationMaintenanceConfigurationUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApplicationMaintenanceConfigurationRequestTypeDef"
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
                "type_defs.UpdateApplicationMaintenanceConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationOperationsResponse:
    boto3_raw_data: "type_defs.ListApplicationOperationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationOperationInfoList(self):  # pragma: no cover
        return ApplicationOperationInfo.make_many(
            self.boto3_raw_data["ApplicationOperationInfoList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationOperationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationOperationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsResponse:
    boto3_raw_data: "type_defs.ListApplicationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationSummaries(self):  # pragma: no cover
        return ApplicationSummary.make_many(self.boto3_raw_data["ApplicationSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationVersionsResponse:
    boto3_raw_data: "type_defs.ListApplicationVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationVersionSummaries(self):  # pragma: no cover
        return ApplicationVersionSummary.make_many(
            self.boto3_raw_data["ApplicationVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CatalogConfigurationDescription:
    boto3_raw_data: "type_defs.CatalogConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlueDataCatalogConfigurationDescription(self):  # pragma: no cover
        return GlueDataCatalogConfigurationDescription.make_one(
            self.boto3_raw_data["GlueDataCatalogConfigurationDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CatalogConfigurationDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CatalogConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CatalogConfiguration:
    boto3_raw_data: "type_defs.CatalogConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def GlueDataCatalogConfiguration(self):  # pragma: no cover
        return GlueDataCatalogConfiguration.make_one(
            self.boto3_raw_data["GlueDataCatalogConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CatalogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CatalogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CatalogConfigurationUpdate:
    boto3_raw_data: "type_defs.CatalogConfigurationUpdateTypeDef" = dataclasses.field()

    @cached_property
    def GlueDataCatalogConfigurationUpdate(self):  # pragma: no cover
        return GlueDataCatalogConfigurationUpdate.make_one(
            self.boto3_raw_data["GlueDataCatalogConfigurationUpdate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CatalogConfigurationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CatalogConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeContentDescription:
    boto3_raw_data: "type_defs.CodeContentDescriptionTypeDef" = dataclasses.field()

    TextContent = field("TextContent")
    CodeMD5 = field("CodeMD5")
    CodeSize = field("CodeSize")

    @cached_property
    def S3ApplicationCodeLocationDescription(self):  # pragma: no cover
        return S3ApplicationCodeLocationDescription.make_one(
            self.boto3_raw_data["S3ApplicationCodeLocationDescription"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeContentDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeContentDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeContent:
    boto3_raw_data: "type_defs.CodeContentTypeDef" = dataclasses.field()

    TextContent = field("TextContent")
    ZipFileContent = field("ZipFileContent")

    @cached_property
    def S3ContentLocation(self):  # pragma: no cover
        return S3ContentLocation.make_one(self.boto3_raw_data["S3ContentLocation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeContentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeContentUpdate:
    boto3_raw_data: "type_defs.CodeContentUpdateTypeDef" = dataclasses.field()

    TextContentUpdate = field("TextContentUpdate")
    ZipFileContentUpdate = field("ZipFileContentUpdate")

    @cached_property
    def S3ContentLocationUpdate(self):  # pragma: no cover
        return S3ContentLocationUpdate.make_one(
            self.boto3_raw_data["S3ContentLocationUpdate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeContentUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeContentUpdateTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CustomArtifactConfigurationDescription:
    boto3_raw_data: "type_defs.CustomArtifactConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    ArtifactType = field("ArtifactType")

    @cached_property
    def S3ContentLocationDescription(self):  # pragma: no cover
        return S3ContentLocation.make_one(
            self.boto3_raw_data["S3ContentLocationDescription"]
        )

    @cached_property
    def MavenReferenceDescription(self):  # pragma: no cover
        return MavenReference.make_one(self.boto3_raw_data["MavenReferenceDescription"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomArtifactConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomArtifactConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomArtifactConfiguration:
    boto3_raw_data: "type_defs.CustomArtifactConfigurationTypeDef" = dataclasses.field()

    ArtifactType = field("ArtifactType")

    @cached_property
    def S3ContentLocation(self):  # pragma: no cover
        return S3ContentLocation.make_one(self.boto3_raw_data["S3ContentLocation"])

    @cached_property
    def MavenReference(self):  # pragma: no cover
        return MavenReference.make_one(self.boto3_raw_data["MavenReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomArtifactConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomArtifactConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationRequest:
    boto3_raw_data: "type_defs.DeleteApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CreateTimestamp = field("CreateTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationSnapshotRequest:
    boto3_raw_data: "type_defs.DeleteApplicationSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    SnapshotName = field("SnapshotName")
    SnapshotCreationTimestamp = field("SnapshotCreationTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApplicationSnapshotRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeployAsApplicationConfigurationDescription:
    boto3_raw_data: "type_defs.DeployAsApplicationConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3ContentLocationDescription(self):  # pragma: no cover
        return S3ContentBaseLocationDescription.make_one(
            self.boto3_raw_data["S3ContentLocationDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeployAsApplicationConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeployAsApplicationConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeployAsApplicationConfiguration:
    boto3_raw_data: "type_defs.DeployAsApplicationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3ContentLocation(self):  # pragma: no cover
        return S3ContentBaseLocation.make_one(self.boto3_raw_data["S3ContentLocation"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeployAsApplicationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeployAsApplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeployAsApplicationConfigurationUpdate:
    boto3_raw_data: "type_defs.DeployAsApplicationConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3ContentLocationUpdate(self):  # pragma: no cover
        return S3ContentBaseLocationUpdate.make_one(
            self.boto3_raw_data["S3ContentLocationUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeployAsApplicationConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeployAsApplicationConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlRunConfiguration:
    boto3_raw_data: "type_defs.SqlRunConfigurationTypeDef" = dataclasses.field()

    InputId = field("InputId")

    @cached_property
    def InputStartingPositionConfiguration(self):  # pragma: no cover
        return InputStartingPositionConfiguration.make_one(
            self.boto3_raw_data["InputStartingPositionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SqlRunConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlRunConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentPropertyDescriptions:
    boto3_raw_data: "type_defs.EnvironmentPropertyDescriptionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PropertyGroupDescriptions(self):  # pragma: no cover
        return PropertyGroupOutput.make_many(
            self.boto3_raw_data["PropertyGroupDescriptions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnvironmentPropertyDescriptionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentPropertyDescriptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperationFailureDetails:
    boto3_raw_data: "type_defs.OperationFailureDetailsTypeDef" = dataclasses.field()

    RollbackOperationId = field("RollbackOperationId")

    @cached_property
    def ErrorInfo(self):  # pragma: no cover
        return ErrorInfo.make_one(self.boto3_raw_data["ErrorInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OperationFailureDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OperationFailureDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlinkApplicationConfigurationDescription:
    boto3_raw_data: "type_defs.FlinkApplicationConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CheckpointConfigurationDescription(self):  # pragma: no cover
        return CheckpointConfigurationDescription.make_one(
            self.boto3_raw_data["CheckpointConfigurationDescription"]
        )

    @cached_property
    def MonitoringConfigurationDescription(self):  # pragma: no cover
        return MonitoringConfigurationDescription.make_one(
            self.boto3_raw_data["MonitoringConfigurationDescription"]
        )

    @cached_property
    def ParallelismConfigurationDescription(self):  # pragma: no cover
        return ParallelismConfigurationDescription.make_one(
            self.boto3_raw_data["ParallelismConfigurationDescription"]
        )

    JobPlanDescription = field("JobPlanDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FlinkApplicationConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlinkApplicationConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlinkApplicationConfiguration:
    boto3_raw_data: "type_defs.FlinkApplicationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CheckpointConfiguration(self):  # pragma: no cover
        return CheckpointConfiguration.make_one(
            self.boto3_raw_data["CheckpointConfiguration"]
        )

    @cached_property
    def MonitoringConfiguration(self):  # pragma: no cover
        return MonitoringConfiguration.make_one(
            self.boto3_raw_data["MonitoringConfiguration"]
        )

    @cached_property
    def ParallelismConfiguration(self):  # pragma: no cover
        return ParallelismConfiguration.make_one(
            self.boto3_raw_data["ParallelismConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FlinkApplicationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlinkApplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlinkApplicationConfigurationUpdate:
    boto3_raw_data: "type_defs.FlinkApplicationConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CheckpointConfigurationUpdate(self):  # pragma: no cover
        return CheckpointConfigurationUpdate.make_one(
            self.boto3_raw_data["CheckpointConfigurationUpdate"]
        )

    @cached_property
    def MonitoringConfigurationUpdate(self):  # pragma: no cover
        return MonitoringConfigurationUpdate.make_one(
            self.boto3_raw_data["MonitoringConfigurationUpdate"]
        )

    @cached_property
    def ParallelismConfigurationUpdate(self):  # pragma: no cover
        return ParallelismConfigurationUpdate.make_one(
            self.boto3_raw_data["ParallelismConfigurationUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FlinkApplicationConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlinkApplicationConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunConfigurationDescription:
    boto3_raw_data: "type_defs.RunConfigurationDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationRestoreConfigurationDescription(self):  # pragma: no cover
        return ApplicationRestoreConfiguration.make_one(
            self.boto3_raw_data["ApplicationRestoreConfigurationDescription"]
        )

    @cached_property
    def FlinkRunConfigurationDescription(self):  # pragma: no cover
        return FlinkRunConfiguration.make_one(
            self.boto3_raw_data["FlinkRunConfigurationDescription"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RunConfigurationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunConfigurationUpdate:
    boto3_raw_data: "type_defs.RunConfigurationUpdateTypeDef" = dataclasses.field()

    @cached_property
    def FlinkRunConfiguration(self):  # pragma: no cover
        return FlinkRunConfiguration.make_one(
            self.boto3_raw_data["FlinkRunConfiguration"]
        )

    @cached_property
    def ApplicationRestoreConfiguration(self):  # pragma: no cover
        return ApplicationRestoreConfiguration.make_one(
            self.boto3_raw_data["ApplicationRestoreConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RunConfigurationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputProcessingConfigurationDescription:
    boto3_raw_data: "type_defs.InputProcessingConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputLambdaProcessorDescription(self):  # pragma: no cover
        return InputLambdaProcessorDescription.make_one(
            self.boto3_raw_data["InputLambdaProcessorDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputProcessingConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputProcessingConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputProcessingConfiguration:
    boto3_raw_data: "type_defs.InputProcessingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputLambdaProcessor(self):  # pragma: no cover
        return InputLambdaProcessor.make_one(
            self.boto3_raw_data["InputLambdaProcessor"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputProcessingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputProcessingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputProcessingConfigurationUpdate:
    boto3_raw_data: "type_defs.InputProcessingConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputLambdaProcessorUpdate(self):  # pragma: no cover
        return InputLambdaProcessorUpdate.make_one(
            self.boto3_raw_data["InputLambdaProcessorUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputProcessingConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputProcessingConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MappingParameters:
    boto3_raw_data: "type_defs.MappingParametersTypeDef" = dataclasses.field()

    @cached_property
    def JSONMappingParameters(self):  # pragma: no cover
        return JSONMappingParameters.make_one(
            self.boto3_raw_data["JSONMappingParameters"]
        )

    @cached_property
    def CSVMappingParameters(self):  # pragma: no cover
        return CSVMappingParameters.make_one(
            self.boto3_raw_data["CSVMappingParameters"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MappingParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MappingParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDescription:
    boto3_raw_data: "type_defs.OutputDescriptionTypeDef" = dataclasses.field()

    OutputId = field("OutputId")
    Name = field("Name")

    @cached_property
    def KinesisStreamsOutputDescription(self):  # pragma: no cover
        return KinesisStreamsOutputDescription.make_one(
            self.boto3_raw_data["KinesisStreamsOutputDescription"]
        )

    @cached_property
    def KinesisFirehoseOutputDescription(self):  # pragma: no cover
        return KinesisFirehoseOutputDescription.make_one(
            self.boto3_raw_data["KinesisFirehoseOutputDescription"]
        )

    @cached_property
    def LambdaOutputDescription(self):  # pragma: no cover
        return LambdaOutputDescription.make_one(
            self.boto3_raw_data["LambdaOutputDescription"]
        )

    @cached_property
    def DestinationSchema(self):  # pragma: no cover
        return DestinationSchema.make_one(self.boto3_raw_data["DestinationSchema"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputDescriptionTypeDef"]
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

    Name = field("Name")

    @cached_property
    def DestinationSchema(self):  # pragma: no cover
        return DestinationSchema.make_one(self.boto3_raw_data["DestinationSchema"])

    @cached_property
    def KinesisStreamsOutput(self):  # pragma: no cover
        return KinesisStreamsOutput.make_one(
            self.boto3_raw_data["KinesisStreamsOutput"]
        )

    @cached_property
    def KinesisFirehoseOutput(self):  # pragma: no cover
        return KinesisFirehoseOutput.make_one(
            self.boto3_raw_data["KinesisFirehoseOutput"]
        )

    @cached_property
    def LambdaOutput(self):  # pragma: no cover
        return LambdaOutput.make_one(self.boto3_raw_data["LambdaOutput"])

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
class OutputUpdate:
    boto3_raw_data: "type_defs.OutputUpdateTypeDef" = dataclasses.field()

    OutputId = field("OutputId")
    NameUpdate = field("NameUpdate")

    @cached_property
    def KinesisStreamsOutputUpdate(self):  # pragma: no cover
        return KinesisStreamsOutputUpdate.make_one(
            self.boto3_raw_data["KinesisStreamsOutputUpdate"]
        )

    @cached_property
    def KinesisFirehoseOutputUpdate(self):  # pragma: no cover
        return KinesisFirehoseOutputUpdate.make_one(
            self.boto3_raw_data["KinesisFirehoseOutputUpdate"]
        )

    @cached_property
    def LambdaOutputUpdate(self):  # pragma: no cover
        return LambdaOutputUpdate.make_one(self.boto3_raw_data["LambdaOutputUpdate"])

    @cached_property
    def DestinationSchemaUpdate(self):  # pragma: no cover
        return DestinationSchema.make_one(
            self.boto3_raw_data["DestinationSchemaUpdate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationOperationsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationOperationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    Operation = field("Operation")
    OperationStatus = field("OperationStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationOperationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationOperationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationSnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationSnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationSnapshotsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationSnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationSnapshotResponse:
    boto3_raw_data: "type_defs.DescribeApplicationSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SnapshotDetails(self):  # pragma: no cover
        return SnapshotDetails.make_one(self.boto3_raw_data["SnapshotDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationSnapshotResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationSnapshotsResponse:
    boto3_raw_data: "type_defs.ListApplicationSnapshotsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SnapshotSummaries(self):  # pragma: no cover
        return SnapshotDetails.make_many(self.boto3_raw_data["SnapshotSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationSnapshotsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationSnapshotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationCodeConfigurationDescription:
    boto3_raw_data: "type_defs.ApplicationCodeConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    CodeContentType = field("CodeContentType")

    @cached_property
    def CodeContentDescription(self):  # pragma: no cover
        return CodeContentDescription.make_one(
            self.boto3_raw_data["CodeContentDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationCodeConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationCodeConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationCodeConfiguration:
    boto3_raw_data: "type_defs.ApplicationCodeConfigurationTypeDef" = (
        dataclasses.field()
    )

    CodeContentType = field("CodeContentType")

    @cached_property
    def CodeContent(self):  # pragma: no cover
        return CodeContent.make_one(self.boto3_raw_data["CodeContent"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationCodeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationCodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationCodeConfigurationUpdate:
    boto3_raw_data: "type_defs.ApplicationCodeConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    CodeContentTypeUpdate = field("CodeContentTypeUpdate")

    @cached_property
    def CodeContentUpdate(self):  # pragma: no cover
        return CodeContentUpdate.make_one(self.boto3_raw_data["CodeContentUpdate"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationCodeConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationCodeConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZeppelinApplicationConfigurationDescription:
    boto3_raw_data: "type_defs.ZeppelinApplicationConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MonitoringConfigurationDescription(self):  # pragma: no cover
        return ZeppelinMonitoringConfigurationDescription.make_one(
            self.boto3_raw_data["MonitoringConfigurationDescription"]
        )

    @cached_property
    def CatalogConfigurationDescription(self):  # pragma: no cover
        return CatalogConfigurationDescription.make_one(
            self.boto3_raw_data["CatalogConfigurationDescription"]
        )

    @cached_property
    def DeployAsApplicationConfigurationDescription(self):  # pragma: no cover
        return DeployAsApplicationConfigurationDescription.make_one(
            self.boto3_raw_data["DeployAsApplicationConfigurationDescription"]
        )

    @cached_property
    def CustomArtifactsConfigurationDescription(self):  # pragma: no cover
        return CustomArtifactConfigurationDescription.make_many(
            self.boto3_raw_data["CustomArtifactsConfigurationDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ZeppelinApplicationConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZeppelinApplicationConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZeppelinApplicationConfiguration:
    boto3_raw_data: "type_defs.ZeppelinApplicationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MonitoringConfiguration(self):  # pragma: no cover
        return ZeppelinMonitoringConfiguration.make_one(
            self.boto3_raw_data["MonitoringConfiguration"]
        )

    @cached_property
    def CatalogConfiguration(self):  # pragma: no cover
        return CatalogConfiguration.make_one(
            self.boto3_raw_data["CatalogConfiguration"]
        )

    @cached_property
    def DeployAsApplicationConfiguration(self):  # pragma: no cover
        return DeployAsApplicationConfiguration.make_one(
            self.boto3_raw_data["DeployAsApplicationConfiguration"]
        )

    @cached_property
    def CustomArtifactsConfiguration(self):  # pragma: no cover
        return CustomArtifactConfiguration.make_many(
            self.boto3_raw_data["CustomArtifactsConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ZeppelinApplicationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZeppelinApplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZeppelinApplicationConfigurationUpdate:
    boto3_raw_data: "type_defs.ZeppelinApplicationConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MonitoringConfigurationUpdate(self):  # pragma: no cover
        return ZeppelinMonitoringConfigurationUpdate.make_one(
            self.boto3_raw_data["MonitoringConfigurationUpdate"]
        )

    @cached_property
    def CatalogConfigurationUpdate(self):  # pragma: no cover
        return CatalogConfigurationUpdate.make_one(
            self.boto3_raw_data["CatalogConfigurationUpdate"]
        )

    @cached_property
    def DeployAsApplicationConfigurationUpdate(self):  # pragma: no cover
        return DeployAsApplicationConfigurationUpdate.make_one(
            self.boto3_raw_data["DeployAsApplicationConfigurationUpdate"]
        )

    @cached_property
    def CustomArtifactsConfigurationUpdate(self):  # pragma: no cover
        return CustomArtifactConfiguration.make_many(
            self.boto3_raw_data["CustomArtifactsConfigurationUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ZeppelinApplicationConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZeppelinApplicationConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunConfiguration:
    boto3_raw_data: "type_defs.RunConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def FlinkRunConfiguration(self):  # pragma: no cover
        return FlinkRunConfiguration.make_one(
            self.boto3_raw_data["FlinkRunConfiguration"]
        )

    @cached_property
    def SqlRunConfigurations(self):  # pragma: no cover
        return SqlRunConfiguration.make_many(
            self.boto3_raw_data["SqlRunConfigurations"]
        )

    @cached_property
    def ApplicationRestoreConfiguration(self):  # pragma: no cover
        return ApplicationRestoreConfiguration.make_one(
            self.boto3_raw_data["ApplicationRestoreConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationOperationInfoDetails:
    boto3_raw_data: "type_defs.ApplicationOperationInfoDetailsTypeDef" = (
        dataclasses.field()
    )

    Operation = field("Operation")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    OperationStatus = field("OperationStatus")

    @cached_property
    def ApplicationVersionChangeDetails(self):  # pragma: no cover
        return ApplicationVersionChangeDetails.make_one(
            self.boto3_raw_data["ApplicationVersionChangeDetails"]
        )

    @cached_property
    def OperationFailureDetails(self):  # pragma: no cover
        return OperationFailureDetails.make_one(
            self.boto3_raw_data["OperationFailureDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationOperationInfoDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationOperationInfoDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationInputProcessingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.AddApplicationInputProcessingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")
    InputId = field("InputId")

    @cached_property
    def InputProcessingConfigurationDescription(self):  # pragma: no cover
        return InputProcessingConfigurationDescription.make_one(
            self.boto3_raw_data["InputProcessingConfigurationDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationInputProcessingConfigurationResponseTypeDef"
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
                "type_defs.AddApplicationInputProcessingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationInputProcessingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.AddApplicationInputProcessingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")
    InputId = field("InputId")

    @cached_property
    def InputProcessingConfiguration(self):  # pragma: no cover
        return InputProcessingConfiguration.make_one(
            self.boto3_raw_data["InputProcessingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationInputProcessingConfigurationRequestTypeDef"
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
                "type_defs.AddApplicationInputProcessingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscoverInputSchemaRequest:
    boto3_raw_data: "type_defs.DiscoverInputSchemaRequestTypeDef" = dataclasses.field()

    ServiceExecutionRole = field("ServiceExecutionRole")
    ResourceARN = field("ResourceARN")

    @cached_property
    def InputStartingPositionConfiguration(self):  # pragma: no cover
        return InputStartingPositionConfiguration.make_one(
            self.boto3_raw_data["InputStartingPositionConfiguration"]
        )

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3Configuration.make_one(self.boto3_raw_data["S3Configuration"])

    @cached_property
    def InputProcessingConfiguration(self):  # pragma: no cover
        return InputProcessingConfiguration.make_one(
            self.boto3_raw_data["InputProcessingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiscoverInputSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscoverInputSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordFormat:
    boto3_raw_data: "type_defs.RecordFormatTypeDef" = dataclasses.field()

    RecordFormatType = field("RecordFormatType")

    @cached_property
    def MappingParameters(self):  # pragma: no cover
        return MappingParameters.make_one(self.boto3_raw_data["MappingParameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordFormatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordFormatTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationOutputResponse:
    boto3_raw_data: "type_defs.AddApplicationOutputResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")

    @cached_property
    def OutputDescriptions(self):  # pragma: no cover
        return OutputDescription.make_many(self.boto3_raw_data["OutputDescriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddApplicationOutputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationOutputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationOutputRequest:
    boto3_raw_data: "type_defs.AddApplicationOutputRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @cached_property
    def Output(self):  # pragma: no cover
        return Output.make_one(self.boto3_raw_data["Output"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddApplicationOutputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentProperties:
    boto3_raw_data: "type_defs.EnvironmentPropertiesTypeDef" = dataclasses.field()

    PropertyGroups = field("PropertyGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentPropertyUpdates:
    boto3_raw_data: "type_defs.EnvironmentPropertyUpdatesTypeDef" = dataclasses.field()

    PropertyGroups = field("PropertyGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentPropertyUpdatesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentPropertyUpdatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartApplicationRequest:
    boto3_raw_data: "type_defs.StartApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")

    @cached_property
    def RunConfiguration(self):  # pragma: no cover
        return RunConfiguration.make_one(self.boto3_raw_data["RunConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationOperationResponse:
    boto3_raw_data: "type_defs.DescribeApplicationOperationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationOperationInfoDetails(self):  # pragma: no cover
        return ApplicationOperationInfoDetails.make_one(
            self.boto3_raw_data["ApplicationOperationInfoDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationOperationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationOperationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSchemaUpdate:
    boto3_raw_data: "type_defs.InputSchemaUpdateTypeDef" = dataclasses.field()

    @cached_property
    def RecordFormatUpdate(self):  # pragma: no cover
        return RecordFormat.make_one(self.boto3_raw_data["RecordFormatUpdate"])

    RecordEncodingUpdate = field("RecordEncodingUpdate")

    @cached_property
    def RecordColumnUpdates(self):  # pragma: no cover
        return RecordColumn.make_many(self.boto3_raw_data["RecordColumnUpdates"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputSchemaUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSchemaUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceSchemaOutput:
    boto3_raw_data: "type_defs.SourceSchemaOutputTypeDef" = dataclasses.field()

    @cached_property
    def RecordFormat(self):  # pragma: no cover
        return RecordFormat.make_one(self.boto3_raw_data["RecordFormat"])

    @cached_property
    def RecordColumns(self):  # pragma: no cover
        return RecordColumn.make_many(self.boto3_raw_data["RecordColumns"])

    RecordEncoding = field("RecordEncoding")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceSchema:
    boto3_raw_data: "type_defs.SourceSchemaTypeDef" = dataclasses.field()

    @cached_property
    def RecordFormat(self):  # pragma: no cover
        return RecordFormat.make_one(self.boto3_raw_data["RecordFormat"])

    @cached_property
    def RecordColumns(self):  # pragma: no cover
        return RecordColumn.make_many(self.boto3_raw_data["RecordColumns"])

    RecordEncoding = field("RecordEncoding")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceSchemaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputUpdate:
    boto3_raw_data: "type_defs.InputUpdateTypeDef" = dataclasses.field()

    InputId = field("InputId")
    NamePrefixUpdate = field("NamePrefixUpdate")

    @cached_property
    def InputProcessingConfigurationUpdate(self):  # pragma: no cover
        return InputProcessingConfigurationUpdate.make_one(
            self.boto3_raw_data["InputProcessingConfigurationUpdate"]
        )

    @cached_property
    def KinesisStreamsInputUpdate(self):  # pragma: no cover
        return KinesisStreamsInputUpdate.make_one(
            self.boto3_raw_data["KinesisStreamsInputUpdate"]
        )

    @cached_property
    def KinesisFirehoseInputUpdate(self):  # pragma: no cover
        return KinesisFirehoseInputUpdate.make_one(
            self.boto3_raw_data["KinesisFirehoseInputUpdate"]
        )

    @cached_property
    def InputSchemaUpdate(self):  # pragma: no cover
        return InputSchemaUpdate.make_one(self.boto3_raw_data["InputSchemaUpdate"])

    @cached_property
    def InputParallelismUpdate(self):  # pragma: no cover
        return InputParallelismUpdate.make_one(
            self.boto3_raw_data["InputParallelismUpdate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputUpdateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscoverInputSchemaResponse:
    boto3_raw_data: "type_defs.DiscoverInputSchemaResponseTypeDef" = dataclasses.field()

    @cached_property
    def InputSchema(self):  # pragma: no cover
        return SourceSchemaOutput.make_one(self.boto3_raw_data["InputSchema"])

    ParsedInputRecords = field("ParsedInputRecords")
    ProcessedInputRecords = field("ProcessedInputRecords")
    RawInputRecords = field("RawInputRecords")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiscoverInputSchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscoverInputSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDescription:
    boto3_raw_data: "type_defs.InputDescriptionTypeDef" = dataclasses.field()

    InputId = field("InputId")
    NamePrefix = field("NamePrefix")
    InAppStreamNames = field("InAppStreamNames")

    @cached_property
    def InputProcessingConfigurationDescription(self):  # pragma: no cover
        return InputProcessingConfigurationDescription.make_one(
            self.boto3_raw_data["InputProcessingConfigurationDescription"]
        )

    @cached_property
    def KinesisStreamsInputDescription(self):  # pragma: no cover
        return KinesisStreamsInputDescription.make_one(
            self.boto3_raw_data["KinesisStreamsInputDescription"]
        )

    @cached_property
    def KinesisFirehoseInputDescription(self):  # pragma: no cover
        return KinesisFirehoseInputDescription.make_one(
            self.boto3_raw_data["KinesisFirehoseInputDescription"]
        )

    @cached_property
    def InputSchema(self):  # pragma: no cover
        return SourceSchemaOutput.make_one(self.boto3_raw_data["InputSchema"])

    @cached_property
    def InputParallelism(self):  # pragma: no cover
        return InputParallelism.make_one(self.boto3_raw_data["InputParallelism"])

    @cached_property
    def InputStartingPositionConfiguration(self):  # pragma: no cover
        return InputStartingPositionConfiguration.make_one(
            self.boto3_raw_data["InputStartingPositionConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceDataSourceDescription:
    boto3_raw_data: "type_defs.ReferenceDataSourceDescriptionTypeDef" = (
        dataclasses.field()
    )

    ReferenceId = field("ReferenceId")
    TableName = field("TableName")

    @cached_property
    def S3ReferenceDataSourceDescription(self):  # pragma: no cover
        return S3ReferenceDataSourceDescription.make_one(
            self.boto3_raw_data["S3ReferenceDataSourceDescription"]
        )

    @cached_property
    def ReferenceSchema(self):  # pragma: no cover
        return SourceSchemaOutput.make_one(self.boto3_raw_data["ReferenceSchema"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReferenceDataSourceDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceDataSourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationInputResponse:
    boto3_raw_data: "type_defs.AddApplicationInputResponseTypeDef" = dataclasses.field()

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")

    @cached_property
    def InputDescriptions(self):  # pragma: no cover
        return InputDescription.make_many(self.boto3_raw_data["InputDescriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddApplicationInputResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationInputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationReferenceDataSourceResponse:
    boto3_raw_data: "type_defs.AddApplicationReferenceDataSourceResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationARN = field("ApplicationARN")
    ApplicationVersionId = field("ApplicationVersionId")

    @cached_property
    def ReferenceDataSourceDescriptions(self):  # pragma: no cover
        return ReferenceDataSourceDescription.make_many(
            self.boto3_raw_data["ReferenceDataSourceDescriptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationReferenceDataSourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationReferenceDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlApplicationConfigurationDescription:
    boto3_raw_data: "type_defs.SqlApplicationConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputDescriptions(self):  # pragma: no cover
        return InputDescription.make_many(self.boto3_raw_data["InputDescriptions"])

    @cached_property
    def OutputDescriptions(self):  # pragma: no cover
        return OutputDescription.make_many(self.boto3_raw_data["OutputDescriptions"])

    @cached_property
    def ReferenceDataSourceDescriptions(self):  # pragma: no cover
        return ReferenceDataSourceDescription.make_many(
            self.boto3_raw_data["ReferenceDataSourceDescriptions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SqlApplicationConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlApplicationConfigurationDescriptionTypeDef"]
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

    NamePrefix = field("NamePrefix")
    InputSchema = field("InputSchema")

    @cached_property
    def InputProcessingConfiguration(self):  # pragma: no cover
        return InputProcessingConfiguration.make_one(
            self.boto3_raw_data["InputProcessingConfiguration"]
        )

    @cached_property
    def KinesisStreamsInput(self):  # pragma: no cover
        return KinesisStreamsInput.make_one(self.boto3_raw_data["KinesisStreamsInput"])

    @cached_property
    def KinesisFirehoseInput(self):  # pragma: no cover
        return KinesisFirehoseInput.make_one(
            self.boto3_raw_data["KinesisFirehoseInput"]
        )

    @cached_property
    def InputParallelism(self):  # pragma: no cover
        return InputParallelism.make_one(self.boto3_raw_data["InputParallelism"])

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
class ReferenceDataSource:
    boto3_raw_data: "type_defs.ReferenceDataSourceTypeDef" = dataclasses.field()

    TableName = field("TableName")
    ReferenceSchema = field("ReferenceSchema")

    @cached_property
    def S3ReferenceDataSource(self):  # pragma: no cover
        return S3ReferenceDataSource.make_one(
            self.boto3_raw_data["S3ReferenceDataSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReferenceDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceDataSourceUpdate:
    boto3_raw_data: "type_defs.ReferenceDataSourceUpdateTypeDef" = dataclasses.field()

    ReferenceId = field("ReferenceId")
    TableNameUpdate = field("TableNameUpdate")

    @cached_property
    def S3ReferenceDataSourceUpdate(self):  # pragma: no cover
        return S3ReferenceDataSourceUpdate.make_one(
            self.boto3_raw_data["S3ReferenceDataSourceUpdate"]
        )

    ReferenceSchemaUpdate = field("ReferenceSchemaUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReferenceDataSourceUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceDataSourceUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationConfigurationDescription:
    boto3_raw_data: "type_defs.ApplicationConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SqlApplicationConfigurationDescription(self):  # pragma: no cover
        return SqlApplicationConfigurationDescription.make_one(
            self.boto3_raw_data["SqlApplicationConfigurationDescription"]
        )

    @cached_property
    def ApplicationCodeConfigurationDescription(self):  # pragma: no cover
        return ApplicationCodeConfigurationDescription.make_one(
            self.boto3_raw_data["ApplicationCodeConfigurationDescription"]
        )

    @cached_property
    def RunConfigurationDescription(self):  # pragma: no cover
        return RunConfigurationDescription.make_one(
            self.boto3_raw_data["RunConfigurationDescription"]
        )

    @cached_property
    def FlinkApplicationConfigurationDescription(self):  # pragma: no cover
        return FlinkApplicationConfigurationDescription.make_one(
            self.boto3_raw_data["FlinkApplicationConfigurationDescription"]
        )

    @cached_property
    def EnvironmentPropertyDescriptions(self):  # pragma: no cover
        return EnvironmentPropertyDescriptions.make_one(
            self.boto3_raw_data["EnvironmentPropertyDescriptions"]
        )

    @cached_property
    def ApplicationSnapshotConfigurationDescription(self):  # pragma: no cover
        return ApplicationSnapshotConfigurationDescription.make_one(
            self.boto3_raw_data["ApplicationSnapshotConfigurationDescription"]
        )

    @cached_property
    def ApplicationSystemRollbackConfigurationDescription(self):  # pragma: no cover
        return ApplicationSystemRollbackConfigurationDescription.make_one(
            self.boto3_raw_data["ApplicationSystemRollbackConfigurationDescription"]
        )

    @cached_property
    def VpcConfigurationDescriptions(self):  # pragma: no cover
        return VpcConfigurationDescription.make_many(
            self.boto3_raw_data["VpcConfigurationDescriptions"]
        )

    @cached_property
    def ZeppelinApplicationConfigurationDescription(self):  # pragma: no cover
        return ZeppelinApplicationConfigurationDescription.make_one(
            self.boto3_raw_data["ZeppelinApplicationConfigurationDescription"]
        )

    @cached_property
    def ApplicationEncryptionConfigurationDescription(self):  # pragma: no cover
        return ApplicationEncryptionConfigurationDescription.make_one(
            self.boto3_raw_data["ApplicationEncryptionConfigurationDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationInputRequest:
    boto3_raw_data: "type_defs.AddApplicationInputRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @cached_property
    def Input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["Input"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddApplicationInputRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddApplicationReferenceDataSourceRequest:
    boto3_raw_data: "type_defs.AddApplicationReferenceDataSourceRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @cached_property
    def ReferenceDataSource(self):  # pragma: no cover
        return ReferenceDataSource.make_one(self.boto3_raw_data["ReferenceDataSource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddApplicationReferenceDataSourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddApplicationReferenceDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlApplicationConfiguration:
    boto3_raw_data: "type_defs.SqlApplicationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def Inputs(self):  # pragma: no cover
        return Input.make_many(self.boto3_raw_data["Inputs"])

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def ReferenceDataSources(self):  # pragma: no cover
        return ReferenceDataSource.make_many(
            self.boto3_raw_data["ReferenceDataSources"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SqlApplicationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlApplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlApplicationConfigurationUpdate:
    boto3_raw_data: "type_defs.SqlApplicationConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputUpdates(self):  # pragma: no cover
        return InputUpdate.make_many(self.boto3_raw_data["InputUpdates"])

    @cached_property
    def OutputUpdates(self):  # pragma: no cover
        return OutputUpdate.make_many(self.boto3_raw_data["OutputUpdates"])

    @cached_property
    def ReferenceDataSourceUpdates(self):  # pragma: no cover
        return ReferenceDataSourceUpdate.make_many(
            self.boto3_raw_data["ReferenceDataSourceUpdates"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SqlApplicationConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlApplicationConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationDetail:
    boto3_raw_data: "type_defs.ApplicationDetailTypeDef" = dataclasses.field()

    ApplicationARN = field("ApplicationARN")
    ApplicationName = field("ApplicationName")
    RuntimeEnvironment = field("RuntimeEnvironment")
    ApplicationStatus = field("ApplicationStatus")
    ApplicationVersionId = field("ApplicationVersionId")
    ApplicationDescription = field("ApplicationDescription")
    ServiceExecutionRole = field("ServiceExecutionRole")
    CreateTimestamp = field("CreateTimestamp")
    LastUpdateTimestamp = field("LastUpdateTimestamp")

    @cached_property
    def ApplicationConfigurationDescription(self):  # pragma: no cover
        return ApplicationConfigurationDescription.make_one(
            self.boto3_raw_data["ApplicationConfigurationDescription"]
        )

    @cached_property
    def CloudWatchLoggingOptionDescriptions(self):  # pragma: no cover
        return CloudWatchLoggingOptionDescription.make_many(
            self.boto3_raw_data["CloudWatchLoggingOptionDescriptions"]
        )

    @cached_property
    def ApplicationMaintenanceConfigurationDescription(self):  # pragma: no cover
        return ApplicationMaintenanceConfigurationDescription.make_one(
            self.boto3_raw_data["ApplicationMaintenanceConfigurationDescription"]
        )

    ApplicationVersionUpdatedFrom = field("ApplicationVersionUpdatedFrom")
    ApplicationVersionRolledBackFrom = field("ApplicationVersionRolledBackFrom")
    ApplicationVersionCreateTimestamp = field("ApplicationVersionCreateTimestamp")
    ConditionalToken = field("ConditionalToken")
    ApplicationVersionRolledBackTo = field("ApplicationVersionRolledBackTo")
    ApplicationMode = field("ApplicationMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationConfiguration:
    boto3_raw_data: "type_defs.ApplicationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def SqlApplicationConfiguration(self):  # pragma: no cover
        return SqlApplicationConfiguration.make_one(
            self.boto3_raw_data["SqlApplicationConfiguration"]
        )

    @cached_property
    def FlinkApplicationConfiguration(self):  # pragma: no cover
        return FlinkApplicationConfiguration.make_one(
            self.boto3_raw_data["FlinkApplicationConfiguration"]
        )

    @cached_property
    def EnvironmentProperties(self):  # pragma: no cover
        return EnvironmentProperties.make_one(
            self.boto3_raw_data["EnvironmentProperties"]
        )

    @cached_property
    def ApplicationCodeConfiguration(self):  # pragma: no cover
        return ApplicationCodeConfiguration.make_one(
            self.boto3_raw_data["ApplicationCodeConfiguration"]
        )

    @cached_property
    def ApplicationSnapshotConfiguration(self):  # pragma: no cover
        return ApplicationSnapshotConfiguration.make_one(
            self.boto3_raw_data["ApplicationSnapshotConfiguration"]
        )

    @cached_property
    def ApplicationSystemRollbackConfiguration(self):  # pragma: no cover
        return ApplicationSystemRollbackConfiguration.make_one(
            self.boto3_raw_data["ApplicationSystemRollbackConfiguration"]
        )

    @cached_property
    def VpcConfigurations(self):  # pragma: no cover
        return VpcConfiguration.make_many(self.boto3_raw_data["VpcConfigurations"])

    @cached_property
    def ZeppelinApplicationConfiguration(self):  # pragma: no cover
        return ZeppelinApplicationConfiguration.make_one(
            self.boto3_raw_data["ZeppelinApplicationConfiguration"]
        )

    @cached_property
    def ApplicationEncryptionConfiguration(self):  # pragma: no cover
        return ApplicationEncryptionConfiguration.make_one(
            self.boto3_raw_data["ApplicationEncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationConfigurationUpdate:
    boto3_raw_data: "type_defs.ApplicationConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SqlApplicationConfigurationUpdate(self):  # pragma: no cover
        return SqlApplicationConfigurationUpdate.make_one(
            self.boto3_raw_data["SqlApplicationConfigurationUpdate"]
        )

    @cached_property
    def ApplicationCodeConfigurationUpdate(self):  # pragma: no cover
        return ApplicationCodeConfigurationUpdate.make_one(
            self.boto3_raw_data["ApplicationCodeConfigurationUpdate"]
        )

    @cached_property
    def FlinkApplicationConfigurationUpdate(self):  # pragma: no cover
        return FlinkApplicationConfigurationUpdate.make_one(
            self.boto3_raw_data["FlinkApplicationConfigurationUpdate"]
        )

    @cached_property
    def EnvironmentPropertyUpdates(self):  # pragma: no cover
        return EnvironmentPropertyUpdates.make_one(
            self.boto3_raw_data["EnvironmentPropertyUpdates"]
        )

    @cached_property
    def ApplicationSnapshotConfigurationUpdate(self):  # pragma: no cover
        return ApplicationSnapshotConfigurationUpdate.make_one(
            self.boto3_raw_data["ApplicationSnapshotConfigurationUpdate"]
        )

    @cached_property
    def ApplicationSystemRollbackConfigurationUpdate(self):  # pragma: no cover
        return ApplicationSystemRollbackConfigurationUpdate.make_one(
            self.boto3_raw_data["ApplicationSystemRollbackConfigurationUpdate"]
        )

    @cached_property
    def VpcConfigurationUpdates(self):  # pragma: no cover
        return VpcConfigurationUpdate.make_many(
            self.boto3_raw_data["VpcConfigurationUpdates"]
        )

    @cached_property
    def ZeppelinApplicationConfigurationUpdate(self):  # pragma: no cover
        return ZeppelinApplicationConfigurationUpdate.make_one(
            self.boto3_raw_data["ZeppelinApplicationConfigurationUpdate"]
        )

    @cached_property
    def ApplicationEncryptionConfigurationUpdate(self):  # pragma: no cover
        return ApplicationEncryptionConfigurationUpdate.make_one(
            self.boto3_raw_data["ApplicationEncryptionConfigurationUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationConfigurationUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationResponse:
    boto3_raw_data: "type_defs.CreateApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationDetail(self):  # pragma: no cover
        return ApplicationDetail.make_one(self.boto3_raw_data["ApplicationDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationResponse:
    boto3_raw_data: "type_defs.DescribeApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationDetail(self):  # pragma: no cover
        return ApplicationDetail.make_one(self.boto3_raw_data["ApplicationDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationVersionResponse:
    boto3_raw_data: "type_defs.DescribeApplicationVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationVersionDetail(self):  # pragma: no cover
        return ApplicationDetail.make_one(
            self.boto3_raw_data["ApplicationVersionDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackApplicationResponse:
    boto3_raw_data: "type_defs.RollbackApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationDetail(self):  # pragma: no cover
        return ApplicationDetail.make_one(self.boto3_raw_data["ApplicationDetail"])

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationResponse:
    boto3_raw_data: "type_defs.UpdateApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationDetail(self):  # pragma: no cover
        return ApplicationDetail.make_one(self.boto3_raw_data["ApplicationDetail"])

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    RuntimeEnvironment = field("RuntimeEnvironment")
    ServiceExecutionRole = field("ServiceExecutionRole")
    ApplicationDescription = field("ApplicationDescription")

    @cached_property
    def ApplicationConfiguration(self):  # pragma: no cover
        return ApplicationConfiguration.make_one(
            self.boto3_raw_data["ApplicationConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOption.make_many(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ApplicationMode = field("ApplicationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    CurrentApplicationVersionId = field("CurrentApplicationVersionId")

    @cached_property
    def ApplicationConfigurationUpdate(self):  # pragma: no cover
        return ApplicationConfigurationUpdate.make_one(
            self.boto3_raw_data["ApplicationConfigurationUpdate"]
        )

    ServiceExecutionRoleUpdate = field("ServiceExecutionRoleUpdate")

    @cached_property
    def RunConfigurationUpdate(self):  # pragma: no cover
        return RunConfigurationUpdate.make_one(
            self.boto3_raw_data["RunConfigurationUpdate"]
        )

    @cached_property
    def CloudWatchLoggingOptionUpdates(self):  # pragma: no cover
        return CloudWatchLoggingOptionUpdate.make_many(
            self.boto3_raw_data["CloudWatchLoggingOptionUpdates"]
        )

    ConditionalToken = field("ConditionalToken")
    RuntimeEnvironmentUpdate = field("RuntimeEnvironmentUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
