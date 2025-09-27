# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_fsx import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActiveDirectoryBackupAttributes:
    boto3_raw_data: "type_defs.ActiveDirectoryBackupAttributesTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ActiveDirectoryId = field("ActiveDirectoryId")
    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActiveDirectoryBackupAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveDirectoryBackupAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdministrativeActionFailureDetails:
    boto3_raw_data: "type_defs.AdministrativeActionFailureDetailsTypeDef" = (
        dataclasses.field()
    )

    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AdministrativeActionFailureDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdministrativeActionFailureDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateConfiguration:
    boto3_raw_data: "type_defs.AggregateConfigurationTypeDef" = dataclasses.field()

    Aggregates = field("Aggregates")
    TotalConstituents = field("TotalConstituents")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Alias:
    boto3_raw_data: "type_defs.AliasTypeDef" = dataclasses.field()

    Name = field("Name")
    Lifecycle = field("Lifecycle")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AliasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AliasTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFileSystemAliasesRequest:
    boto3_raw_data: "type_defs.AssociateFileSystemAliasesRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    Aliases = field("Aliases")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateFileSystemAliasesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFileSystemAliasesRequestTypeDef"]
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
class AutoExportPolicyOutput:
    boto3_raw_data: "type_defs.AutoExportPolicyOutputTypeDef" = dataclasses.field()

    Events = field("Events")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoExportPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoExportPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoExportPolicy:
    boto3_raw_data: "type_defs.AutoExportPolicyTypeDef" = dataclasses.field()

    Events = field("Events")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoExportPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoExportPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoImportPolicyOutput:
    boto3_raw_data: "type_defs.AutoImportPolicyOutputTypeDef" = dataclasses.field()

    Events = field("Events")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoImportPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoImportPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoImportPolicy:
    boto3_raw_data: "type_defs.AutoImportPolicyTypeDef" = dataclasses.field()

    Events = field("Events")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoImportPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoImportPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutocommitPeriod:
    boto3_raw_data: "type_defs.AutocommitPeriodTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutocommitPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutocommitPeriodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupFailureDetails:
    boto3_raw_data: "type_defs.BackupFailureDetailsTypeDef" = dataclasses.field()

    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackupFailureDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupFailureDetailsTypeDef"]
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
class CancelDataRepositoryTaskRequest:
    boto3_raw_data: "type_defs.CancelDataRepositoryTaskRequestTypeDef" = (
        dataclasses.field()
    )

    TaskId = field("TaskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelDataRepositoryTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelDataRepositoryTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompletionReport:
    boto3_raw_data: "type_defs.CompletionReportTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Path = field("Path")
    Format = field("Format")
    Scope = field("Scope")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CompletionReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompletionReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySnapshotAndUpdateVolumeRequest:
    boto3_raw_data: "type_defs.CopySnapshotAndUpdateVolumeRequestTypeDef" = (
        dataclasses.field()
    )

    VolumeId = field("VolumeId")
    SourceSnapshotARN = field("SourceSnapshotARN")
    ClientRequestToken = field("ClientRequestToken")
    CopyStrategy = field("CopyStrategy")
    Options = field("Options")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopySnapshotAndUpdateVolumeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySnapshotAndUpdateVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAggregateConfiguration:
    boto3_raw_data: "type_defs.CreateAggregateConfigurationTypeDef" = (
        dataclasses.field()
    )

    Aggregates = field("Aggregates")
    ConstituentsPerAggregate = field("ConstituentsPerAggregate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAggregateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAggregateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessPointVpcConfiguration:
    boto3_raw_data: "type_defs.S3AccessPointVpcConfigurationTypeDef" = (
        dataclasses.field()
    )

    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3AccessPointVpcConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessPointVpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileCacheLustreMetadataConfiguration:
    boto3_raw_data: "type_defs.FileCacheLustreMetadataConfigurationTypeDef" = (
        dataclasses.field()
    )

    StorageCapacity = field("StorageCapacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FileCacheLustreMetadataConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileCacheLustreMetadataConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemLustreMetadataConfiguration:
    boto3_raw_data: "type_defs.CreateFileSystemLustreMetadataConfigurationTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    Iops = field("Iops")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFileSystemLustreMetadataConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemLustreMetadataConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LustreLogCreateConfiguration:
    boto3_raw_data: "type_defs.LustreLogCreateConfigurationTypeDef" = (
        dataclasses.field()
    )

    Level = field("Level")
    Destination = field("Destination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LustreLogCreateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LustreLogCreateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LustreReadCacheConfiguration:
    boto3_raw_data: "type_defs.LustreReadCacheConfigurationTypeDef" = (
        dataclasses.field()
    )

    SizingMode = field("SizingMode")
    SizeGiB = field("SizeGiB")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LustreReadCacheConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LustreReadCacheConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiskIopsConfiguration:
    boto3_raw_data: "type_defs.DiskIopsConfigurationTypeDef" = dataclasses.field()

    Mode = field("Mode")
    Iops = field("Iops")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiskIopsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiskIopsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSReadCacheConfiguration:
    boto3_raw_data: "type_defs.OpenZFSReadCacheConfigurationTypeDef" = (
        dataclasses.field()
    )

    SizingMode = field("SizingMode")
    SizeGiB = field("SizeGiB")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenZFSReadCacheConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSReadCacheConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedActiveDirectoryConfiguration:
    boto3_raw_data: "type_defs.SelfManagedActiveDirectoryConfigurationTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    UserName = field("UserName")
    Password = field("Password")
    DnsIps = field("DnsIps")
    OrganizationalUnitDistinguishedName = field("OrganizationalUnitDistinguishedName")
    FileSystemAdministratorsGroup = field("FileSystemAdministratorsGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelfManagedActiveDirectoryConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManagedActiveDirectoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WindowsAuditLogCreateConfiguration:
    boto3_raw_data: "type_defs.WindowsAuditLogCreateConfigurationTypeDef" = (
        dataclasses.field()
    )

    FileAccessAuditLogLevel = field("FileAccessAuditLogLevel")
    FileShareAccessAuditLogLevel = field("FileShareAccessAuditLogLevel")
    AuditLogDestination = field("AuditLogDestination")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WindowsAuditLogCreateConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WindowsAuditLogCreateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TieringPolicy:
    boto3_raw_data: "type_defs.TieringPolicyTypeDef" = dataclasses.field()

    CoolingPeriod = field("CoolingPeriod")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TieringPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TieringPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpenZFSOriginSnapshotConfiguration:
    boto3_raw_data: "type_defs.CreateOpenZFSOriginSnapshotConfigurationTypeDef" = (
        dataclasses.field()
    )

    SnapshotARN = field("SnapshotARN")
    CopyStrategy = field("CopyStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateOpenZFSOriginSnapshotConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpenZFSOriginSnapshotConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSUserOrGroupQuota:
    boto3_raw_data: "type_defs.OpenZFSUserOrGroupQuotaTypeDef" = dataclasses.field()

    Type = field("Type")
    Id = field("Id")
    StorageCapacityQuotaGiB = field("StorageCapacityQuotaGiB")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenZFSUserOrGroupQuotaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSUserOrGroupQuotaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRepositoryFailureDetails:
    boto3_raw_data: "type_defs.DataRepositoryFailureDetailsTypeDef" = (
        dataclasses.field()
    )

    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataRepositoryFailureDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRepositoryFailureDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRepositoryTaskFailureDetails:
    boto3_raw_data: "type_defs.DataRepositoryTaskFailureDetailsTypeDef" = (
        dataclasses.field()
    )

    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataRepositoryTaskFailureDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRepositoryTaskFailureDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRepositoryTaskFilter:
    boto3_raw_data: "type_defs.DataRepositoryTaskFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataRepositoryTaskFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRepositoryTaskFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRepositoryTaskStatus:
    boto3_raw_data: "type_defs.DataRepositoryTaskStatusTypeDef" = dataclasses.field()

    TotalCount = field("TotalCount")
    SucceededCount = field("SucceededCount")
    FailedCount = field("FailedCount")
    LastUpdatedTime = field("LastUpdatedTime")
    ReleasedCapacity = field("ReleasedCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataRepositoryTaskStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRepositoryTaskStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupRequest:
    boto3_raw_data: "type_defs.DeleteBackupRequestTypeDef" = dataclasses.field()

    BackupId = field("BackupId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataRepositoryAssociationRequest:
    boto3_raw_data: "type_defs.DeleteDataRepositoryAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")
    ClientRequestToken = field("ClientRequestToken")
    DeleteDataInFileSystem = field("DeleteDataInFileSystem")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDataRepositoryAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataRepositoryAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileCacheRequest:
    boto3_raw_data: "type_defs.DeleteFileCacheRequestTypeDef" = dataclasses.field()

    FileCacheId = field("FileCacheId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFileCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotRequest:
    boto3_raw_data: "type_defs.DeleteSnapshotRequestTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStorageVirtualMachineRequest:
    boto3_raw_data: "type_defs.DeleteStorageVirtualMachineRequestTypeDef" = (
        dataclasses.field()
    )

    StorageVirtualMachineId = field("StorageVirtualMachineId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteStorageVirtualMachineRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStorageVirtualMachineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVolumeOpenZFSConfiguration:
    boto3_raw_data: "type_defs.DeleteVolumeOpenZFSConfigurationTypeDef" = (
        dataclasses.field()
    )

    Options = field("Options")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVolumeOpenZFSConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVolumeOpenZFSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
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
class DescribeFileCachesRequest:
    boto3_raw_data: "type_defs.DescribeFileCachesRequestTypeDef" = dataclasses.field()

    FileCacheIds = field("FileCacheIds")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFileCachesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileCachesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemAliasesRequest:
    boto3_raw_data: "type_defs.DescribeFileSystemAliasesRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    ClientRequestToken = field("ClientRequestToken")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFileSystemAliasesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemsRequest:
    boto3_raw_data: "type_defs.DescribeFileSystemsRequestTypeDef" = dataclasses.field()

    FileSystemIds = field("FileSystemIds")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFileSystemsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessPointAttachmentsFilter:
    boto3_raw_data: "type_defs.S3AccessPointAttachmentsFilterTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3AccessPointAttachmentsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessPointAttachmentsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotFilter:
    boto3_raw_data: "type_defs.SnapshotFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapshotFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageVirtualMachineFilter:
    boto3_raw_data: "type_defs.StorageVirtualMachineFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageVirtualMachineFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageVirtualMachineFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeFilter:
    boto3_raw_data: "type_defs.VolumeFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachAndDeleteS3AccessPointRequest:
    boto3_raw_data: "type_defs.DetachAndDeleteS3AccessPointRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachAndDeleteS3AccessPointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachAndDeleteS3AccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFileSystemAliasesRequest:
    boto3_raw_data: "type_defs.DisassociateFileSystemAliasesRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    Aliases = field("Aliases")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateFileSystemAliasesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFileSystemAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DurationSinceLastAccess:
    boto3_raw_data: "type_defs.DurationSinceLastAccessTypeDef" = dataclasses.field()

    Unit = field("Unit")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DurationSinceLastAccessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DurationSinceLastAccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileCacheFailureDetails:
    boto3_raw_data: "type_defs.FileCacheFailureDetailsTypeDef" = dataclasses.field()

    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileCacheFailureDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileCacheFailureDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileCacheNFSConfiguration:
    boto3_raw_data: "type_defs.FileCacheNFSConfigurationTypeDef" = dataclasses.field()

    Version = field("Version")
    DnsIps = field("DnsIps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileCacheNFSConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileCacheNFSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LustreLogConfiguration:
    boto3_raw_data: "type_defs.LustreLogConfigurationTypeDef" = dataclasses.field()

    Level = field("Level")
    Destination = field("Destination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LustreLogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LustreLogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemEndpoint:
    boto3_raw_data: "type_defs.FileSystemEndpointTypeDef" = dataclasses.field()

    DNSName = field("DNSName")
    IpAddresses = field("IpAddresses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSystemEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemFailureDetails:
    boto3_raw_data: "type_defs.FileSystemFailureDetailsTypeDef" = dataclasses.field()

    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSystemFailureDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemFailureDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemLustreMetadataConfiguration:
    boto3_raw_data: "type_defs.FileSystemLustreMetadataConfigurationTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    Iops = field("Iops")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FileSystemLustreMetadataConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemLustreMetadataConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleTransitionReason:
    boto3_raw_data: "type_defs.LifecycleTransitionReasonTypeDef" = dataclasses.field()

    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleTransitionReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleTransitionReasonTypeDef"]
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
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class LustreRootSquashConfigurationOutput:
    boto3_raw_data: "type_defs.LustreRootSquashConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    RootSquash = field("RootSquash")
    NoSquashNids = field("NoSquashNids")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LustreRootSquashConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LustreRootSquashConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LustreRootSquashConfiguration:
    boto3_raw_data: "type_defs.LustreRootSquashConfigurationTypeDef" = (
        dataclasses.field()
    )

    RootSquash = field("RootSquash")
    NoSquashNids = field("NoSquashNids")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LustreRootSquashConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LustreRootSquashConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSClientConfigurationOutput:
    boto3_raw_data: "type_defs.OpenZFSClientConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Clients = field("Clients")
    Options = field("Options")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenZFSClientConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSClientConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSClientConfiguration:
    boto3_raw_data: "type_defs.OpenZFSClientConfigurationTypeDef" = dataclasses.field()

    Clients = field("Clients")
    Options = field("Options")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenZFSClientConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSClientConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSPosixFileSystemUserOutput:
    boto3_raw_data: "type_defs.OpenZFSPosixFileSystemUserOutputTypeDef" = (
        dataclasses.field()
    )

    Uid = field("Uid")
    Gid = field("Gid")
    SecondaryGids = field("SecondaryGids")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenZFSPosixFileSystemUserOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSPosixFileSystemUserOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSOriginSnapshotConfiguration:
    boto3_raw_data: "type_defs.OpenZFSOriginSnapshotConfigurationTypeDef" = (
        dataclasses.field()
    )

    SnapshotARN = field("SnapshotARN")
    CopyStrategy = field("CopyStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenZFSOriginSnapshotConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSOriginSnapshotConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSPosixFileSystemUser:
    boto3_raw_data: "type_defs.OpenZFSPosixFileSystemUserTypeDef" = dataclasses.field()

    Uid = field("Uid")
    Gid = field("Gid")
    SecondaryGids = field("SecondaryGids")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenZFSPosixFileSystemUserTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSPosixFileSystemUserTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleaseFileSystemNfsV3LocksRequest:
    boto3_raw_data: "type_defs.ReleaseFileSystemNfsV3LocksRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReleaseFileSystemNfsV3LocksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleaseFileSystemNfsV3LocksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreVolumeFromSnapshotRequest:
    boto3_raw_data: "type_defs.RestoreVolumeFromSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    VolumeId = field("VolumeId")
    SnapshotId = field("SnapshotId")
    ClientRequestToken = field("ClientRequestToken")
    Options = field("Options")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreVolumeFromSnapshotRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreVolumeFromSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetentionPeriod:
    boto3_raw_data: "type_defs.RetentionPeriodTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetentionPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetentionPeriodTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedActiveDirectoryAttributes:
    boto3_raw_data: "type_defs.SelfManagedActiveDirectoryAttributesTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    OrganizationalUnitDistinguishedName = field("OrganizationalUnitDistinguishedName")
    FileSystemAdministratorsGroup = field("FileSystemAdministratorsGroup")
    UserName = field("UserName")
    DnsIps = field("DnsIps")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelfManagedActiveDirectoryAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManagedActiveDirectoryAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedActiveDirectoryConfigurationUpdates:
    boto3_raw_data: (
        "type_defs.SelfManagedActiveDirectoryConfigurationUpdatesTypeDef"
    ) = dataclasses.field()

    UserName = field("UserName")
    Password = field("Password")
    DnsIps = field("DnsIps")
    DomainName = field("DomainName")
    OrganizationalUnitDistinguishedName = field("OrganizationalUnitDistinguishedName")
    FileSystemAdministratorsGroup = field("FileSystemAdministratorsGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelfManagedActiveDirectoryConfigurationUpdatesTypeDef"
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
                "type_defs.SelfManagedActiveDirectoryConfigurationUpdatesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMisconfiguredStateRecoveryRequest:
    boto3_raw_data: "type_defs.StartMisconfiguredStateRecoveryRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMisconfiguredStateRecoveryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMisconfiguredStateRecoveryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SvmEndpoint:
    boto3_raw_data: "type_defs.SvmEndpointTypeDef" = dataclasses.field()

    DNSName = field("DNSName")
    IpAddresses = field("IpAddresses")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SvmEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SvmEndpointTypeDef"]]
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
class UpdateFileCacheLustreConfiguration:
    boto3_raw_data: "type_defs.UpdateFileCacheLustreConfigurationTypeDef" = (
        dataclasses.field()
    )

    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFileCacheLustreConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileCacheLustreConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemLustreMetadataConfiguration:
    boto3_raw_data: "type_defs.UpdateFileSystemLustreMetadataConfigurationTypeDef" = (
        dataclasses.field()
    )

    Iops = field("Iops")
    Mode = field("Mode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFileSystemLustreMetadataConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemLustreMetadataConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSharedVpcConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateSharedVpcConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    EnableFsxRouteTableUpdatesFromParticipantAccounts = field(
        "EnableFsxRouteTableUpdatesFromParticipantAccounts"
    )
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSharedVpcConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSharedVpcConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSnapshotRequest:
    boto3_raw_data: "type_defs.UpdateSnapshotRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    SnapshotId = field("SnapshotId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WindowsAuditLogConfiguration:
    boto3_raw_data: "type_defs.WindowsAuditLogConfigurationTypeDef" = (
        dataclasses.field()
    )

    FileAccessAuditLogLevel = field("FileAccessAuditLogLevel")
    FileShareAccessAuditLogLevel = field("FileShareAccessAuditLogLevel")
    AuditLogDestination = field("AuditLogDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WindowsAuditLogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WindowsAuditLogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFileSystemAliasesResponse:
    boto3_raw_data: "type_defs.AssociateFileSystemAliasesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Aliases(self):  # pragma: no cover
        return Alias.make_many(self.boto3_raw_data["Aliases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateFileSystemAliasesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFileSystemAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelDataRepositoryTaskResponse:
    boto3_raw_data: "type_defs.CancelDataRepositoryTaskResponseTypeDef" = (
        dataclasses.field()
    )

    Lifecycle = field("Lifecycle")
    TaskId = field("TaskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelDataRepositoryTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelDataRepositoryTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupResponse:
    boto3_raw_data: "type_defs.DeleteBackupResponseTypeDef" = dataclasses.field()

    BackupId = field("BackupId")
    Lifecycle = field("Lifecycle")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataRepositoryAssociationResponse:
    boto3_raw_data: "type_defs.DeleteDataRepositoryAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")
    Lifecycle = field("Lifecycle")
    DeleteDataInFileSystem = field("DeleteDataInFileSystem")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDataRepositoryAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataRepositoryAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileCacheResponse:
    boto3_raw_data: "type_defs.DeleteFileCacheResponseTypeDef" = dataclasses.field()

    FileCacheId = field("FileCacheId")
    Lifecycle = field("Lifecycle")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFileCacheResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotResponse:
    boto3_raw_data: "type_defs.DeleteSnapshotResponseTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")
    Lifecycle = field("Lifecycle")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStorageVirtualMachineResponse:
    boto3_raw_data: "type_defs.DeleteStorageVirtualMachineResponseTypeDef" = (
        dataclasses.field()
    )

    StorageVirtualMachineId = field("StorageVirtualMachineId")
    Lifecycle = field("Lifecycle")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteStorageVirtualMachineResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStorageVirtualMachineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemAliasesResponse:
    boto3_raw_data: "type_defs.DescribeFileSystemAliasesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Aliases(self):  # pragma: no cover
        return Alias.make_many(self.boto3_raw_data["Aliases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFileSystemAliasesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSharedVpcConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeSharedVpcConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    EnableFsxRouteTableUpdatesFromParticipantAccounts = field(
        "EnableFsxRouteTableUpdatesFromParticipantAccounts"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSharedVpcConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSharedVpcConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachAndDeleteS3AccessPointResponse:
    boto3_raw_data: "type_defs.DetachAndDeleteS3AccessPointResponseTypeDef" = (
        dataclasses.field()
    )

    Lifecycle = field("Lifecycle")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachAndDeleteS3AccessPointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachAndDeleteS3AccessPointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFileSystemAliasesResponse:
    boto3_raw_data: "type_defs.DisassociateFileSystemAliasesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Aliases(self):  # pragma: no cover
        return Alias.make_many(self.boto3_raw_data["Aliases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateFileSystemAliasesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFileSystemAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSharedVpcConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateSharedVpcConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    EnableFsxRouteTableUpdatesFromParticipantAccounts = field(
        "EnableFsxRouteTableUpdatesFromParticipantAccounts"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSharedVpcConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSharedVpcConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NFSDataRepositoryConfiguration:
    boto3_raw_data: "type_defs.NFSDataRepositoryConfigurationTypeDef" = (
        dataclasses.field()
    )

    Version = field("Version")
    DnsIps = field("DnsIps")

    @cached_property
    def AutoExportPolicy(self):  # pragma: no cover
        return AutoExportPolicyOutput.make_one(self.boto3_raw_data["AutoExportPolicy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NFSDataRepositoryConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NFSDataRepositoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataRepositoryConfigurationOutput:
    boto3_raw_data: "type_defs.S3DataRepositoryConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoImportPolicy(self):  # pragma: no cover
        return AutoImportPolicyOutput.make_one(self.boto3_raw_data["AutoImportPolicy"])

    @cached_property
    def AutoExportPolicy(self):  # pragma: no cover
        return AutoExportPolicyOutput.make_one(self.boto3_raw_data["AutoExportPolicy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3DataRepositoryConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataRepositoryConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataRepositoryConfiguration:
    boto3_raw_data: "type_defs.S3DataRepositoryConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoImportPolicy(self):  # pragma: no cover
        return AutoImportPolicy.make_one(self.boto3_raw_data["AutoImportPolicy"])

    @cached_property
    def AutoExportPolicy(self):  # pragma: no cover
        return AutoExportPolicy.make_one(self.boto3_raw_data["AutoExportPolicy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3DataRepositoryConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataRepositoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyBackupRequest:
    boto3_raw_data: "type_defs.CopyBackupRequestTypeDef" = dataclasses.field()

    SourceBackupId = field("SourceBackupId")
    ClientRequestToken = field("ClientRequestToken")
    SourceRegion = field("SourceRegion")
    KmsKeyId = field("KmsKeyId")
    CopyTags = field("CopyTags")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyBackupRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyBackupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackupRequest:
    boto3_raw_data: "type_defs.CreateBackupRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    VolumeId = field("VolumeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotRequest:
    boto3_raw_data: "type_defs.CreateSnapshotRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    VolumeId = field("VolumeId")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemLustreConfiguration:
    boto3_raw_data: "type_defs.DeleteFileSystemLustreConfigurationTypeDef" = (
        dataclasses.field()
    )

    SkipFinalBackup = field("SkipFinalBackup")

    @cached_property
    def FinalBackupTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["FinalBackupTags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFileSystemLustreConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemLustreConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemLustreResponse:
    boto3_raw_data: "type_defs.DeleteFileSystemLustreResponseTypeDef" = (
        dataclasses.field()
    )

    FinalBackupId = field("FinalBackupId")

    @cached_property
    def FinalBackupTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["FinalBackupTags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFileSystemLustreResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemLustreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemOpenZFSConfiguration:
    boto3_raw_data: "type_defs.DeleteFileSystemOpenZFSConfigurationTypeDef" = (
        dataclasses.field()
    )

    SkipFinalBackup = field("SkipFinalBackup")

    @cached_property
    def FinalBackupTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["FinalBackupTags"])

    Options = field("Options")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFileSystemOpenZFSConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemOpenZFSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemOpenZFSResponse:
    boto3_raw_data: "type_defs.DeleteFileSystemOpenZFSResponseTypeDef" = (
        dataclasses.field()
    )

    FinalBackupId = field("FinalBackupId")

    @cached_property
    def FinalBackupTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["FinalBackupTags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFileSystemOpenZFSResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemOpenZFSResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemWindowsConfiguration:
    boto3_raw_data: "type_defs.DeleteFileSystemWindowsConfigurationTypeDef" = (
        dataclasses.field()
    )

    SkipFinalBackup = field("SkipFinalBackup")

    @cached_property
    def FinalBackupTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["FinalBackupTags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFileSystemWindowsConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemWindowsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemWindowsResponse:
    boto3_raw_data: "type_defs.DeleteFileSystemWindowsResponseTypeDef" = (
        dataclasses.field()
    )

    FinalBackupId = field("FinalBackupId")

    @cached_property
    def FinalBackupTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["FinalBackupTags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFileSystemWindowsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemWindowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVolumeOntapConfiguration:
    boto3_raw_data: "type_defs.DeleteVolumeOntapConfigurationTypeDef" = (
        dataclasses.field()
    )

    SkipFinalBackup = field("SkipFinalBackup")

    @cached_property
    def FinalBackupTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["FinalBackupTags"])

    BypassSnaplockEnterpriseRetention = field("BypassSnaplockEnterpriseRetention")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVolumeOntapConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVolumeOntapConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVolumeOntapResponse:
    boto3_raw_data: "type_defs.DeleteVolumeOntapResponseTypeDef" = dataclasses.field()

    FinalBackupId = field("FinalBackupId")

    @cached_property
    def FinalBackupTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["FinalBackupTags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVolumeOntapResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVolumeOntapResponseTypeDef"]
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

    NextToken = field("NextToken")

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
class CreateAndAttachS3AccessPointS3Configuration:
    boto3_raw_data: "type_defs.CreateAndAttachS3AccessPointS3ConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return S3AccessPointVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    Policy = field("Policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAndAttachS3AccessPointS3ConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAndAttachS3AccessPointS3ConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessPoint:
    boto3_raw_data: "type_defs.S3AccessPointTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    Alias = field("Alias")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return S3AccessPointVpcConfiguration.make_one(
            self.boto3_raw_data["VpcConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3AccessPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3AccessPointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileCacheLustreConfiguration:
    boto3_raw_data: "type_defs.CreateFileCacheLustreConfigurationTypeDef" = (
        dataclasses.field()
    )

    PerUnitStorageThroughput = field("PerUnitStorageThroughput")
    DeploymentType = field("DeploymentType")

    @cached_property
    def MetadataConfiguration(self):  # pragma: no cover
        return FileCacheLustreMetadataConfiguration.make_one(
            self.boto3_raw_data["MetadataConfiguration"]
        )

    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFileCacheLustreConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileCacheLustreConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemOntapConfiguration:
    boto3_raw_data: "type_defs.CreateFileSystemOntapConfigurationTypeDef" = (
        dataclasses.field()
    )

    DeploymentType = field("DeploymentType")
    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    EndpointIpAddressRange = field("EndpointIpAddressRange")
    FsxAdminPassword = field("FsxAdminPassword")

    @cached_property
    def DiskIopsConfiguration(self):  # pragma: no cover
        return DiskIopsConfiguration.make_one(
            self.boto3_raw_data["DiskIopsConfiguration"]
        )

    PreferredSubnetId = field("PreferredSubnetId")
    RouteTableIds = field("RouteTableIds")
    ThroughputCapacity = field("ThroughputCapacity")
    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")
    HAPairs = field("HAPairs")
    ThroughputCapacityPerHAPair = field("ThroughputCapacityPerHAPair")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFileSystemOntapConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemOntapConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemOntapConfiguration:
    boto3_raw_data: "type_defs.UpdateFileSystemOntapConfigurationTypeDef" = (
        dataclasses.field()
    )

    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    FsxAdminPassword = field("FsxAdminPassword")
    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")

    @cached_property
    def DiskIopsConfiguration(self):  # pragma: no cover
        return DiskIopsConfiguration.make_one(
            self.boto3_raw_data["DiskIopsConfiguration"]
        )

    ThroughputCapacity = field("ThroughputCapacity")
    AddRouteTableIds = field("AddRouteTableIds")
    RemoveRouteTableIds = field("RemoveRouteTableIds")
    ThroughputCapacityPerHAPair = field("ThroughputCapacityPerHAPair")
    HAPairs = field("HAPairs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFileSystemOntapConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemOntapConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSFileSystemConfiguration:
    boto3_raw_data: "type_defs.OpenZFSFileSystemConfigurationTypeDef" = (
        dataclasses.field()
    )

    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    CopyTagsToBackups = field("CopyTagsToBackups")
    CopyTagsToVolumes = field("CopyTagsToVolumes")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    DeploymentType = field("DeploymentType")
    ThroughputCapacity = field("ThroughputCapacity")
    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")

    @cached_property
    def DiskIopsConfiguration(self):  # pragma: no cover
        return DiskIopsConfiguration.make_one(
            self.boto3_raw_data["DiskIopsConfiguration"]
        )

    RootVolumeId = field("RootVolumeId")
    PreferredSubnetId = field("PreferredSubnetId")
    EndpointIpAddressRange = field("EndpointIpAddressRange")
    EndpointIpv6AddressRange = field("EndpointIpv6AddressRange")
    RouteTableIds = field("RouteTableIds")
    EndpointIpAddress = field("EndpointIpAddress")
    EndpointIpv6Address = field("EndpointIpv6Address")

    @cached_property
    def ReadCacheConfiguration(self):  # pragma: no cover
        return OpenZFSReadCacheConfiguration.make_one(
            self.boto3_raw_data["ReadCacheConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenZFSFileSystemConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSFileSystemConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemOpenZFSConfiguration:
    boto3_raw_data: "type_defs.UpdateFileSystemOpenZFSConfigurationTypeDef" = (
        dataclasses.field()
    )

    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    CopyTagsToBackups = field("CopyTagsToBackups")
    CopyTagsToVolumes = field("CopyTagsToVolumes")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    ThroughputCapacity = field("ThroughputCapacity")
    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")

    @cached_property
    def DiskIopsConfiguration(self):  # pragma: no cover
        return DiskIopsConfiguration.make_one(
            self.boto3_raw_data["DiskIopsConfiguration"]
        )

    AddRouteTableIds = field("AddRouteTableIds")
    RemoveRouteTableIds = field("RemoveRouteTableIds")

    @cached_property
    def ReadCacheConfiguration(self):  # pragma: no cover
        return OpenZFSReadCacheConfiguration.make_one(
            self.boto3_raw_data["ReadCacheConfiguration"]
        )

    EndpointIpv6AddressRange = field("EndpointIpv6AddressRange")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFileSystemOpenZFSConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemOpenZFSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSvmActiveDirectoryConfiguration:
    boto3_raw_data: "type_defs.CreateSvmActiveDirectoryConfigurationTypeDef" = (
        dataclasses.field()
    )

    NetBiosName = field("NetBiosName")

    @cached_property
    def SelfManagedActiveDirectoryConfiguration(self):  # pragma: no cover
        return SelfManagedActiveDirectoryConfiguration.make_one(
            self.boto3_raw_data["SelfManagedActiveDirectoryConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSvmActiveDirectoryConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSvmActiveDirectoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemWindowsConfiguration:
    boto3_raw_data: "type_defs.CreateFileSystemWindowsConfigurationTypeDef" = (
        dataclasses.field()
    )

    ThroughputCapacity = field("ThroughputCapacity")
    ActiveDirectoryId = field("ActiveDirectoryId")

    @cached_property
    def SelfManagedActiveDirectoryConfiguration(self):  # pragma: no cover
        return SelfManagedActiveDirectoryConfiguration.make_one(
            self.boto3_raw_data["SelfManagedActiveDirectoryConfiguration"]
        )

    DeploymentType = field("DeploymentType")
    PreferredSubnetId = field("PreferredSubnetId")
    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    CopyTagsToBackups = field("CopyTagsToBackups")
    Aliases = field("Aliases")

    @cached_property
    def AuditLogConfiguration(self):  # pragma: no cover
        return WindowsAuditLogCreateConfiguration.make_one(
            self.boto3_raw_data["AuditLogConfiguration"]
        )

    @cached_property
    def DiskIopsConfiguration(self):  # pragma: no cover
        return DiskIopsConfiguration.make_one(
            self.boto3_raw_data["DiskIopsConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFileSystemWindowsConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemWindowsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRepositoryConfiguration:
    boto3_raw_data: "type_defs.DataRepositoryConfigurationTypeDef" = dataclasses.field()

    Lifecycle = field("Lifecycle")
    ImportPath = field("ImportPath")
    ExportPath = field("ExportPath")
    ImportedFileChunkSize = field("ImportedFileChunkSize")
    AutoImportPolicy = field("AutoImportPolicy")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return DataRepositoryFailureDetails.make_one(
            self.boto3_raw_data["FailureDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataRepositoryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRepositoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataRepositoryTasksRequest:
    boto3_raw_data: "type_defs.DescribeDataRepositoryTasksRequestTypeDef" = (
        dataclasses.field()
    )

    TaskIds = field("TaskIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return DataRepositoryTaskFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataRepositoryTasksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataRepositoryTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupsRequest:
    boto3_raw_data: "type_defs.DescribeBackupsRequestTypeDef" = dataclasses.field()

    BackupIds = field("BackupIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBackupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataRepositoryAssociationsRequest:
    boto3_raw_data: "type_defs.DescribeDataRepositoryAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    AssociationIds = field("AssociationIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataRepositoryAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataRepositoryAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeBackupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    BackupIds = field("BackupIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBackupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeFileSystemsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FileSystemIds = field("FileSystemIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFileSystemsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTagsForResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeS3AccessPointAttachmentsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeS3AccessPointAttachmentsRequestPaginateTypeDef"
    ) = dataclasses.field()

    Names = field("Names")

    @cached_property
    def Filters(self):  # pragma: no cover
        return S3AccessPointAttachmentsFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeS3AccessPointAttachmentsRequestPaginateTypeDef"
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
                "type_defs.DescribeS3AccessPointAttachmentsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeS3AccessPointAttachmentsRequest:
    boto3_raw_data: "type_defs.DescribeS3AccessPointAttachmentsRequestTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")

    @cached_property
    def Filters(self):  # pragma: no cover
        return S3AccessPointAttachmentsFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeS3AccessPointAttachmentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeS3AccessPointAttachmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SnapshotIds = field("SnapshotIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return SnapshotFilter.make_many(self.boto3_raw_data["Filters"])

    IncludeShared = field("IncludeShared")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsRequest:
    boto3_raw_data: "type_defs.DescribeSnapshotsRequestTypeDef" = dataclasses.field()

    SnapshotIds = field("SnapshotIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return SnapshotFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    IncludeShared = field("IncludeShared")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStorageVirtualMachinesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeStorageVirtualMachinesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    StorageVirtualMachineIds = field("StorageVirtualMachineIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StorageVirtualMachineFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStorageVirtualMachinesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStorageVirtualMachinesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStorageVirtualMachinesRequest:
    boto3_raw_data: "type_defs.DescribeStorageVirtualMachinesRequestTypeDef" = (
        dataclasses.field()
    )

    StorageVirtualMachineIds = field("StorageVirtualMachineIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StorageVirtualMachineFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStorageVirtualMachinesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStorageVirtualMachinesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVolumesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeVolumesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    VolumeIds = field("VolumeIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return VolumeFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeVolumesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVolumesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVolumesRequest:
    boto3_raw_data: "type_defs.DescribeVolumesRequestTypeDef" = dataclasses.field()

    VolumeIds = field("VolumeIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return VolumeFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVolumesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVolumesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleaseConfiguration:
    boto3_raw_data: "type_defs.ReleaseConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def DurationSinceLastAccess(self):  # pragma: no cover
        return DurationSinceLastAccess.make_one(
            self.boto3_raw_data["DurationSinceLastAccess"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReleaseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleaseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileCacheDataRepositoryAssociation:
    boto3_raw_data: "type_defs.FileCacheDataRepositoryAssociationTypeDef" = (
        dataclasses.field()
    )

    FileCachePath = field("FileCachePath")
    DataRepositoryPath = field("DataRepositoryPath")
    DataRepositorySubdirectories = field("DataRepositorySubdirectories")

    @cached_property
    def NFS(self):  # pragma: no cover
        return FileCacheNFSConfiguration.make_one(self.boto3_raw_data["NFS"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FileCacheDataRepositoryAssociationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileCacheDataRepositoryAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileCacheLustreConfiguration:
    boto3_raw_data: "type_defs.FileCacheLustreConfigurationTypeDef" = (
        dataclasses.field()
    )

    PerUnitStorageThroughput = field("PerUnitStorageThroughput")
    DeploymentType = field("DeploymentType")
    MountName = field("MountName")
    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")

    @cached_property
    def MetadataConfiguration(self):  # pragma: no cover
        return FileCacheLustreMetadataConfiguration.make_one(
            self.boto3_raw_data["MetadataConfiguration"]
        )

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LustreLogConfiguration.make_one(self.boto3_raw_data["LogConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileCacheLustreConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileCacheLustreConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemEndpoints:
    boto3_raw_data: "type_defs.FileSystemEndpointsTypeDef" = dataclasses.field()

    @cached_property
    def Intercluster(self):  # pragma: no cover
        return FileSystemEndpoint.make_one(self.boto3_raw_data["Intercluster"])

    @cached_property
    def Management(self):  # pragma: no cover
        return FileSystemEndpoint.make_one(self.boto3_raw_data["Management"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSystemEndpointsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemEndpointsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotPaginator:
    boto3_raw_data: "type_defs.SnapshotPaginatorTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    SnapshotId = field("SnapshotId")
    Name = field("Name")
    VolumeId = field("VolumeId")
    CreationTime = field("CreationTime")
    Lifecycle = field("Lifecycle")

    @cached_property
    def LifecycleTransitionReason(self):  # pragma: no cover
        return LifecycleTransitionReason.make_one(
            self.boto3_raw_data["LifecycleTransitionReason"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AdministrativeActions = field("AdministrativeActions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapshotPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Snapshot:
    boto3_raw_data: "type_defs.SnapshotTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    SnapshotId = field("SnapshotId")
    Name = field("Name")
    VolumeId = field("VolumeId")
    CreationTime = field("CreationTime")
    Lifecycle = field("Lifecycle")

    @cached_property
    def LifecycleTransitionReason(self):  # pragma: no cover
        return LifecycleTransitionReason.make_one(
            self.boto3_raw_data["LifecycleTransitionReason"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AdministrativeActions = field("AdministrativeActions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapshotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSNfsExportOutput:
    boto3_raw_data: "type_defs.OpenZFSNfsExportOutputTypeDef" = dataclasses.field()

    @cached_property
    def ClientConfigurations(self):  # pragma: no cover
        return OpenZFSClientConfigurationOutput.make_many(
            self.boto3_raw_data["ClientConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenZFSNfsExportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSNfsExportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSFileSystemIdentityOutput:
    boto3_raw_data: "type_defs.OpenZFSFileSystemIdentityOutputTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")

    @cached_property
    def PosixUser(self):  # pragma: no cover
        return OpenZFSPosixFileSystemUserOutput.make_one(
            self.boto3_raw_data["PosixUser"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenZFSFileSystemIdentityOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSFileSystemIdentityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnaplockRetentionPeriod:
    boto3_raw_data: "type_defs.SnaplockRetentionPeriodTypeDef" = dataclasses.field()

    @cached_property
    def DefaultRetention(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["DefaultRetention"])

    @cached_property
    def MinimumRetention(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["MinimumRetention"])

    @cached_property
    def MaximumRetention(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["MaximumRetention"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnaplockRetentionPeriodTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnaplockRetentionPeriodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SvmActiveDirectoryConfiguration:
    boto3_raw_data: "type_defs.SvmActiveDirectoryConfigurationTypeDef" = (
        dataclasses.field()
    )

    NetBiosName = field("NetBiosName")

    @cached_property
    def SelfManagedActiveDirectoryConfiguration(self):  # pragma: no cover
        return SelfManagedActiveDirectoryAttributes.make_one(
            self.boto3_raw_data["SelfManagedActiveDirectoryConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SvmActiveDirectoryConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SvmActiveDirectoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemWindowsConfiguration:
    boto3_raw_data: "type_defs.UpdateFileSystemWindowsConfigurationTypeDef" = (
        dataclasses.field()
    )

    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    ThroughputCapacity = field("ThroughputCapacity")

    @cached_property
    def SelfManagedActiveDirectoryConfiguration(self):  # pragma: no cover
        return SelfManagedActiveDirectoryConfigurationUpdates.make_one(
            self.boto3_raw_data["SelfManagedActiveDirectoryConfiguration"]
        )

    @cached_property
    def AuditLogConfiguration(self):  # pragma: no cover
        return WindowsAuditLogCreateConfiguration.make_one(
            self.boto3_raw_data["AuditLogConfiguration"]
        )

    @cached_property
    def DiskIopsConfiguration(self):  # pragma: no cover
        return DiskIopsConfiguration.make_one(
            self.boto3_raw_data["DiskIopsConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFileSystemWindowsConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemWindowsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSvmActiveDirectoryConfiguration:
    boto3_raw_data: "type_defs.UpdateSvmActiveDirectoryConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SelfManagedActiveDirectoryConfiguration(self):  # pragma: no cover
        return SelfManagedActiveDirectoryConfigurationUpdates.make_one(
            self.boto3_raw_data["SelfManagedActiveDirectoryConfiguration"]
        )

    NetBiosName = field("NetBiosName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSvmActiveDirectoryConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSvmActiveDirectoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SvmEndpoints:
    boto3_raw_data: "type_defs.SvmEndpointsTypeDef" = dataclasses.field()

    @cached_property
    def Iscsi(self):  # pragma: no cover
        return SvmEndpoint.make_one(self.boto3_raw_data["Iscsi"])

    @cached_property
    def Management(self):  # pragma: no cover
        return SvmEndpoint.make_one(self.boto3_raw_data["Management"])

    @cached_property
    def Nfs(self):  # pragma: no cover
        return SvmEndpoint.make_one(self.boto3_raw_data["Nfs"])

    @cached_property
    def Smb(self):  # pragma: no cover
        return SvmEndpoint.make_one(self.boto3_raw_data["Smb"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SvmEndpointsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SvmEndpointsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileCacheRequest:
    boto3_raw_data: "type_defs.UpdateFileCacheRequestTypeDef" = dataclasses.field()

    FileCacheId = field("FileCacheId")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return UpdateFileCacheLustreConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFileCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WindowsFileSystemConfiguration:
    boto3_raw_data: "type_defs.WindowsFileSystemConfigurationTypeDef" = (
        dataclasses.field()
    )

    ActiveDirectoryId = field("ActiveDirectoryId")

    @cached_property
    def SelfManagedActiveDirectoryConfiguration(self):  # pragma: no cover
        return SelfManagedActiveDirectoryAttributes.make_one(
            self.boto3_raw_data["SelfManagedActiveDirectoryConfiguration"]
        )

    DeploymentType = field("DeploymentType")
    RemoteAdministrationEndpoint = field("RemoteAdministrationEndpoint")
    PreferredSubnetId = field("PreferredSubnetId")
    PreferredFileServerIp = field("PreferredFileServerIp")
    ThroughputCapacity = field("ThroughputCapacity")
    MaintenanceOperationsInProgress = field("MaintenanceOperationsInProgress")
    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    CopyTagsToBackups = field("CopyTagsToBackups")

    @cached_property
    def Aliases(self):  # pragma: no cover
        return Alias.make_many(self.boto3_raw_data["Aliases"])

    @cached_property
    def AuditLogConfiguration(self):  # pragma: no cover
        return WindowsAuditLogConfiguration.make_one(
            self.boto3_raw_data["AuditLogConfiguration"]
        )

    @cached_property
    def DiskIopsConfiguration(self):  # pragma: no cover
        return DiskIopsConfiguration.make_one(
            self.boto3_raw_data["DiskIopsConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WindowsFileSystemConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WindowsFileSystemConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRepositoryAssociation:
    boto3_raw_data: "type_defs.DataRepositoryAssociationTypeDef" = dataclasses.field()

    AssociationId = field("AssociationId")
    ResourceARN = field("ResourceARN")
    FileSystemId = field("FileSystemId")
    Lifecycle = field("Lifecycle")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return DataRepositoryFailureDetails.make_one(
            self.boto3_raw_data["FailureDetails"]
        )

    FileSystemPath = field("FileSystemPath")
    DataRepositoryPath = field("DataRepositoryPath")
    BatchImportMetaDataOnCreate = field("BatchImportMetaDataOnCreate")
    ImportedFileChunkSize = field("ImportedFileChunkSize")

    @cached_property
    def S3(self):  # pragma: no cover
        return S3DataRepositoryConfigurationOutput.make_one(self.boto3_raw_data["S3"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreationTime = field("CreationTime")
    FileCacheId = field("FileCacheId")
    FileCachePath = field("FileCachePath")
    DataRepositorySubdirectories = field("DataRepositorySubdirectories")

    @cached_property
    def NFS(self):  # pragma: no cover
        return NFSDataRepositoryConfiguration.make_one(self.boto3_raw_data["NFS"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataRepositoryAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRepositoryAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemRequest:
    boto3_raw_data: "type_defs.DeleteFileSystemRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def WindowsConfiguration(self):  # pragma: no cover
        return DeleteFileSystemWindowsConfiguration.make_one(
            self.boto3_raw_data["WindowsConfiguration"]
        )

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return DeleteFileSystemLustreConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return DeleteFileSystemOpenZFSConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFileSystemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemResponse:
    boto3_raw_data: "type_defs.DeleteFileSystemResponseTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    Lifecycle = field("Lifecycle")

    @cached_property
    def WindowsResponse(self):  # pragma: no cover
        return DeleteFileSystemWindowsResponse.make_one(
            self.boto3_raw_data["WindowsResponse"]
        )

    @cached_property
    def LustreResponse(self):  # pragma: no cover
        return DeleteFileSystemLustreResponse.make_one(
            self.boto3_raw_data["LustreResponse"]
        )

    @cached_property
    def OpenZFSResponse(self):  # pragma: no cover
        return DeleteFileSystemOpenZFSResponse.make_one(
            self.boto3_raw_data["OpenZFSResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFileSystemResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVolumeRequest:
    boto3_raw_data: "type_defs.DeleteVolumeRequestTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return DeleteVolumeOntapConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return DeleteVolumeOpenZFSConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVolumeResponse:
    boto3_raw_data: "type_defs.DeleteVolumeResponseTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")
    Lifecycle = field("Lifecycle")

    @cached_property
    def OntapResponse(self):  # pragma: no cover
        return DeleteVolumeOntapResponse.make_one(self.boto3_raw_data["OntapResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVolumeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVolumeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorageVirtualMachineRequest:
    boto3_raw_data: "type_defs.CreateStorageVirtualMachineRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    Name = field("Name")

    @cached_property
    def ActiveDirectoryConfiguration(self):  # pragma: no cover
        return CreateSvmActiveDirectoryConfiguration.make_one(
            self.boto3_raw_data["ActiveDirectoryConfiguration"]
        )

    ClientRequestToken = field("ClientRequestToken")
    SvmAdminPassword = field("SvmAdminPassword")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    RootVolumeSecurityStyle = field("RootVolumeSecurityStyle")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStorageVirtualMachineRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorageVirtualMachineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LustreFileSystemConfiguration:
    boto3_raw_data: "type_defs.LustreFileSystemConfigurationTypeDef" = (
        dataclasses.field()
    )

    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")

    @cached_property
    def DataRepositoryConfiguration(self):  # pragma: no cover
        return DataRepositoryConfiguration.make_one(
            self.boto3_raw_data["DataRepositoryConfiguration"]
        )

    DeploymentType = field("DeploymentType")
    PerUnitStorageThroughput = field("PerUnitStorageThroughput")
    MountName = field("MountName")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    CopyTagsToBackups = field("CopyTagsToBackups")
    DriveCacheType = field("DriveCacheType")
    DataCompressionType = field("DataCompressionType")

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LustreLogConfiguration.make_one(self.boto3_raw_data["LogConfiguration"])

    @cached_property
    def RootSquashConfiguration(self):  # pragma: no cover
        return LustreRootSquashConfigurationOutput.make_one(
            self.boto3_raw_data["RootSquashConfiguration"]
        )

    @cached_property
    def MetadataConfiguration(self):  # pragma: no cover
        return FileSystemLustreMetadataConfiguration.make_one(
            self.boto3_raw_data["MetadataConfiguration"]
        )

    EfaEnabled = field("EfaEnabled")
    ThroughputCapacity = field("ThroughputCapacity")

    @cached_property
    def DataReadCacheConfiguration(self):  # pragma: no cover
        return LustreReadCacheConfiguration.make_one(
            self.boto3_raw_data["DataReadCacheConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LustreFileSystemConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LustreFileSystemConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataRepositoryTaskRequest:
    boto3_raw_data: "type_defs.CreateDataRepositoryTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    FileSystemId = field("FileSystemId")

    @cached_property
    def Report(self):  # pragma: no cover
        return CompletionReport.make_one(self.boto3_raw_data["Report"])

    Paths = field("Paths")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CapacityToRelease = field("CapacityToRelease")

    @cached_property
    def ReleaseConfiguration(self):  # pragma: no cover
        return ReleaseConfiguration.make_one(
            self.boto3_raw_data["ReleaseConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataRepositoryTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataRepositoryTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataRepositoryTask:
    boto3_raw_data: "type_defs.DataRepositoryTaskTypeDef" = dataclasses.field()

    TaskId = field("TaskId")
    Lifecycle = field("Lifecycle")
    Type = field("Type")
    CreationTime = field("CreationTime")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    FileSystemId = field("FileSystemId")
    Paths = field("Paths")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return DataRepositoryTaskFailureDetails.make_one(
            self.boto3_raw_data["FailureDetails"]
        )

    @cached_property
    def Status(self):  # pragma: no cover
        return DataRepositoryTaskStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Report(self):  # pragma: no cover
        return CompletionReport.make_one(self.boto3_raw_data["Report"])

    CapacityToRelease = field("CapacityToRelease")
    FileCacheId = field("FileCacheId")

    @cached_property
    def ReleaseConfiguration(self):  # pragma: no cover
        return ReleaseConfiguration.make_one(
            self.boto3_raw_data["ReleaseConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataRepositoryTaskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataRepositoryTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileCacheRequest:
    boto3_raw_data: "type_defs.CreateFileCacheRequestTypeDef" = dataclasses.field()

    FileCacheType = field("FileCacheType")
    FileCacheTypeVersion = field("FileCacheTypeVersion")
    StorageCapacity = field("StorageCapacity")
    SubnetIds = field("SubnetIds")
    ClientRequestToken = field("ClientRequestToken")
    SecurityGroupIds = field("SecurityGroupIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CopyTagsToDataRepositoryAssociations = field("CopyTagsToDataRepositoryAssociations")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return CreateFileCacheLustreConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    @cached_property
    def DataRepositoryAssociations(self):  # pragma: no cover
        return FileCacheDataRepositoryAssociation.make_many(
            self.boto3_raw_data["DataRepositoryAssociations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFileCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileCacheCreating:
    boto3_raw_data: "type_defs.FileCacheCreatingTypeDef" = dataclasses.field()

    OwnerId = field("OwnerId")
    CreationTime = field("CreationTime")
    FileCacheId = field("FileCacheId")
    FileCacheType = field("FileCacheType")
    FileCacheTypeVersion = field("FileCacheTypeVersion")
    Lifecycle = field("Lifecycle")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FileCacheFailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    StorageCapacity = field("StorageCapacity")
    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    NetworkInterfaceIds = field("NetworkInterfaceIds")
    DNSName = field("DNSName")
    KmsKeyId = field("KmsKeyId")
    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CopyTagsToDataRepositoryAssociations = field("CopyTagsToDataRepositoryAssociations")

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return FileCacheLustreConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    DataRepositoryAssociationIds = field("DataRepositoryAssociationIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileCacheCreatingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileCacheCreatingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileCache:
    boto3_raw_data: "type_defs.FileCacheTypeDef" = dataclasses.field()

    OwnerId = field("OwnerId")
    CreationTime = field("CreationTime")
    FileCacheId = field("FileCacheId")
    FileCacheType = field("FileCacheType")
    FileCacheTypeVersion = field("FileCacheTypeVersion")
    Lifecycle = field("Lifecycle")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FileCacheFailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    StorageCapacity = field("StorageCapacity")
    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    NetworkInterfaceIds = field("NetworkInterfaceIds")
    DNSName = field("DNSName")
    KmsKeyId = field("KmsKeyId")
    ResourceARN = field("ResourceARN")

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return FileCacheLustreConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    DataRepositoryAssociationIds = field("DataRepositoryAssociationIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileCacheTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileCacheTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OntapFileSystemConfiguration:
    boto3_raw_data: "type_defs.OntapFileSystemConfigurationTypeDef" = (
        dataclasses.field()
    )

    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    DeploymentType = field("DeploymentType")
    EndpointIpAddressRange = field("EndpointIpAddressRange")

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return FileSystemEndpoints.make_one(self.boto3_raw_data["Endpoints"])

    @cached_property
    def DiskIopsConfiguration(self):  # pragma: no cover
        return DiskIopsConfiguration.make_one(
            self.boto3_raw_data["DiskIopsConfiguration"]
        )

    PreferredSubnetId = field("PreferredSubnetId")
    RouteTableIds = field("RouteTableIds")
    ThroughputCapacity = field("ThroughputCapacity")
    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")
    FsxAdminPassword = field("FsxAdminPassword")
    HAPairs = field("HAPairs")
    ThroughputCapacityPerHAPair = field("ThroughputCapacityPerHAPair")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OntapFileSystemConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OntapFileSystemConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsResponsePaginator:
    boto3_raw_data: "type_defs.DescribeSnapshotsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Snapshots(self):  # pragma: no cover
        return SnapshotPaginator.make_many(self.boto3_raw_data["Snapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSnapshotsResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotResponse:
    boto3_raw_data: "type_defs.CreateSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsResponse:
    boto3_raw_data: "type_defs.DescribeSnapshotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Snapshots(self):  # pragma: no cover
        return Snapshot.make_many(self.boto3_raw_data["Snapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSnapshotResponse:
    boto3_raw_data: "type_defs.UpdateSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemLustreConfiguration:
    boto3_raw_data: "type_defs.CreateFileSystemLustreConfigurationTypeDef" = (
        dataclasses.field()
    )

    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")
    ImportPath = field("ImportPath")
    ExportPath = field("ExportPath")
    ImportedFileChunkSize = field("ImportedFileChunkSize")
    DeploymentType = field("DeploymentType")
    AutoImportPolicy = field("AutoImportPolicy")
    PerUnitStorageThroughput = field("PerUnitStorageThroughput")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    CopyTagsToBackups = field("CopyTagsToBackups")
    DriveCacheType = field("DriveCacheType")
    DataCompressionType = field("DataCompressionType")
    EfaEnabled = field("EfaEnabled")

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LustreLogCreateConfiguration.make_one(
            self.boto3_raw_data["LogConfiguration"]
        )

    RootSquashConfiguration = field("RootSquashConfiguration")

    @cached_property
    def MetadataConfiguration(self):  # pragma: no cover
        return CreateFileSystemLustreMetadataConfiguration.make_one(
            self.boto3_raw_data["MetadataConfiguration"]
        )

    ThroughputCapacity = field("ThroughputCapacity")

    @cached_property
    def DataReadCacheConfiguration(self):  # pragma: no cover
        return LustreReadCacheConfiguration.make_one(
            self.boto3_raw_data["DataReadCacheConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFileSystemLustreConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemLustreConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemLustreConfiguration:
    boto3_raw_data: "type_defs.UpdateFileSystemLustreConfigurationTypeDef" = (
        dataclasses.field()
    )

    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    AutoImportPolicy = field("AutoImportPolicy")
    DataCompressionType = field("DataCompressionType")

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return LustreLogCreateConfiguration.make_one(
            self.boto3_raw_data["LogConfiguration"]
        )

    RootSquashConfiguration = field("RootSquashConfiguration")
    PerUnitStorageThroughput = field("PerUnitStorageThroughput")

    @cached_property
    def MetadataConfiguration(self):  # pragma: no cover
        return UpdateFileSystemLustreMetadataConfiguration.make_one(
            self.boto3_raw_data["MetadataConfiguration"]
        )

    ThroughputCapacity = field("ThroughputCapacity")

    @cached_property
    def DataReadCacheConfiguration(self):  # pragma: no cover
        return LustreReadCacheConfiguration.make_one(
            self.boto3_raw_data["DataReadCacheConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFileSystemLustreConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemLustreConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSVolumeConfiguration:
    boto3_raw_data: "type_defs.OpenZFSVolumeConfigurationTypeDef" = dataclasses.field()

    ParentVolumeId = field("ParentVolumeId")
    VolumePath = field("VolumePath")
    StorageCapacityReservationGiB = field("StorageCapacityReservationGiB")
    StorageCapacityQuotaGiB = field("StorageCapacityQuotaGiB")
    RecordSizeKiB = field("RecordSizeKiB")
    DataCompressionType = field("DataCompressionType")
    CopyTagsToSnapshots = field("CopyTagsToSnapshots")

    @cached_property
    def OriginSnapshot(self):  # pragma: no cover
        return OpenZFSOriginSnapshotConfiguration.make_one(
            self.boto3_raw_data["OriginSnapshot"]
        )

    ReadOnly = field("ReadOnly")

    @cached_property
    def NfsExports(self):  # pragma: no cover
        return OpenZFSNfsExportOutput.make_many(self.boto3_raw_data["NfsExports"])

    @cached_property
    def UserAndGroupQuotas(self):  # pragma: no cover
        return OpenZFSUserOrGroupQuota.make_many(
            self.boto3_raw_data["UserAndGroupQuotas"]
        )

    RestoreToSnapshot = field("RestoreToSnapshot")
    DeleteIntermediateSnaphots = field("DeleteIntermediateSnaphots")
    DeleteClonedVolumes = field("DeleteClonedVolumes")
    DeleteIntermediateData = field("DeleteIntermediateData")
    SourceSnapshotARN = field("SourceSnapshotARN")
    DestinationSnapshot = field("DestinationSnapshot")
    CopyStrategy = field("CopyStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenZFSVolumeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSNfsExport:
    boto3_raw_data: "type_defs.OpenZFSNfsExportTypeDef" = dataclasses.field()

    ClientConfigurations = field("ClientConfigurations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpenZFSNfsExportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSNfsExportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessPointOpenZFSConfiguration:
    boto3_raw_data: "type_defs.S3AccessPointOpenZFSConfigurationTypeDef" = (
        dataclasses.field()
    )

    VolumeId = field("VolumeId")

    @cached_property
    def FileSystemIdentity(self):  # pragma: no cover
        return OpenZFSFileSystemIdentityOutput.make_one(
            self.boto3_raw_data["FileSystemIdentity"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3AccessPointOpenZFSConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessPointOpenZFSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSFileSystemIdentity:
    boto3_raw_data: "type_defs.OpenZFSFileSystemIdentityTypeDef" = dataclasses.field()

    Type = field("Type")
    PosixUser = field("PosixUser")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenZFSFileSystemIdentityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSFileSystemIdentityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnaplockConfiguration:
    boto3_raw_data: "type_defs.CreateSnaplockConfigurationTypeDef" = dataclasses.field()

    SnaplockType = field("SnaplockType")
    AuditLogVolume = field("AuditLogVolume")

    @cached_property
    def AutocommitPeriod(self):  # pragma: no cover
        return AutocommitPeriod.make_one(self.boto3_raw_data["AutocommitPeriod"])

    PrivilegedDelete = field("PrivilegedDelete")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return SnaplockRetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    VolumeAppendModeEnabled = field("VolumeAppendModeEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnaplockConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnaplockConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnaplockConfiguration:
    boto3_raw_data: "type_defs.SnaplockConfigurationTypeDef" = dataclasses.field()

    AuditLogVolume = field("AuditLogVolume")

    @cached_property
    def AutocommitPeriod(self):  # pragma: no cover
        return AutocommitPeriod.make_one(self.boto3_raw_data["AutocommitPeriod"])

    PrivilegedDelete = field("PrivilegedDelete")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return SnaplockRetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    SnaplockType = field("SnaplockType")
    VolumeAppendModeEnabled = field("VolumeAppendModeEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnaplockConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnaplockConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSnaplockConfiguration:
    boto3_raw_data: "type_defs.UpdateSnaplockConfigurationTypeDef" = dataclasses.field()

    AuditLogVolume = field("AuditLogVolume")

    @cached_property
    def AutocommitPeriod(self):  # pragma: no cover
        return AutocommitPeriod.make_one(self.boto3_raw_data["AutocommitPeriod"])

    PrivilegedDelete = field("PrivilegedDelete")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return SnaplockRetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    VolumeAppendModeEnabled = field("VolumeAppendModeEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSnaplockConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSnaplockConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStorageVirtualMachineRequest:
    boto3_raw_data: "type_defs.UpdateStorageVirtualMachineRequestTypeDef" = (
        dataclasses.field()
    )

    StorageVirtualMachineId = field("StorageVirtualMachineId")

    @cached_property
    def ActiveDirectoryConfiguration(self):  # pragma: no cover
        return UpdateSvmActiveDirectoryConfiguration.make_one(
            self.boto3_raw_data["ActiveDirectoryConfiguration"]
        )

    ClientRequestToken = field("ClientRequestToken")
    SvmAdminPassword = field("SvmAdminPassword")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateStorageVirtualMachineRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStorageVirtualMachineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageVirtualMachine:
    boto3_raw_data: "type_defs.StorageVirtualMachineTypeDef" = dataclasses.field()

    @cached_property
    def ActiveDirectoryConfiguration(self):  # pragma: no cover
        return SvmActiveDirectoryConfiguration.make_one(
            self.boto3_raw_data["ActiveDirectoryConfiguration"]
        )

    CreationTime = field("CreationTime")

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return SvmEndpoints.make_one(self.boto3_raw_data["Endpoints"])

    FileSystemId = field("FileSystemId")
    Lifecycle = field("Lifecycle")
    Name = field("Name")
    ResourceARN = field("ResourceARN")
    StorageVirtualMachineId = field("StorageVirtualMachineId")
    Subtype = field("Subtype")
    UUID = field("UUID")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def LifecycleTransitionReason(self):  # pragma: no cover
        return LifecycleTransitionReason.make_one(
            self.boto3_raw_data["LifecycleTransitionReason"]
        )

    RootVolumeSecurityStyle = field("RootVolumeSecurityStyle")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageVirtualMachineTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageVirtualMachineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataRepositoryAssociationResponse:
    boto3_raw_data: "type_defs.CreateDataRepositoryAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Association(self):  # pragma: no cover
        return DataRepositoryAssociation.make_one(self.boto3_raw_data["Association"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataRepositoryAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataRepositoryAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataRepositoryAssociationsResponse:
    boto3_raw_data: "type_defs.DescribeDataRepositoryAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Associations(self):  # pragma: no cover
        return DataRepositoryAssociation.make_many(self.boto3_raw_data["Associations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataRepositoryAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataRepositoryAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataRepositoryAssociationResponse:
    boto3_raw_data: "type_defs.UpdateDataRepositoryAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Association(self):  # pragma: no cover
        return DataRepositoryAssociation.make_one(self.boto3_raw_data["Association"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDataRepositoryAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataRepositoryAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataRepositoryAssociationRequest:
    boto3_raw_data: "type_defs.CreateDataRepositoryAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    DataRepositoryPath = field("DataRepositoryPath")
    FileSystemPath = field("FileSystemPath")
    BatchImportMetaDataOnCreate = field("BatchImportMetaDataOnCreate")
    ImportedFileChunkSize = field("ImportedFileChunkSize")
    S3 = field("S3")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataRepositoryAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataRepositoryAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataRepositoryAssociationRequest:
    boto3_raw_data: "type_defs.UpdateDataRepositoryAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")
    ClientRequestToken = field("ClientRequestToken")
    ImportedFileChunkSize = field("ImportedFileChunkSize")
    S3 = field("S3")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDataRepositoryAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataRepositoryAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataRepositoryTaskResponse:
    boto3_raw_data: "type_defs.CreateDataRepositoryTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DataRepositoryTask(self):  # pragma: no cover
        return DataRepositoryTask.make_one(self.boto3_raw_data["DataRepositoryTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataRepositoryTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataRepositoryTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataRepositoryTasksResponse:
    boto3_raw_data: "type_defs.DescribeDataRepositoryTasksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DataRepositoryTasks(self):  # pragma: no cover
        return DataRepositoryTask.make_many(self.boto3_raw_data["DataRepositoryTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataRepositoryTasksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataRepositoryTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileCacheResponse:
    boto3_raw_data: "type_defs.CreateFileCacheResponseTypeDef" = dataclasses.field()

    @cached_property
    def FileCache(self):  # pragma: no cover
        return FileCacheCreating.make_one(self.boto3_raw_data["FileCache"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFileCacheResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileCachesResponse:
    boto3_raw_data: "type_defs.DescribeFileCachesResponseTypeDef" = dataclasses.field()

    @cached_property
    def FileCaches(self):  # pragma: no cover
        return FileCache.make_many(self.boto3_raw_data["FileCaches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFileCachesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileCachesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileCacheResponse:
    boto3_raw_data: "type_defs.UpdateFileCacheResponseTypeDef" = dataclasses.field()

    @cached_property
    def FileCache(self):  # pragma: no cover
        return FileCache.make_one(self.boto3_raw_data["FileCache"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFileCacheResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemRequest:
    boto3_raw_data: "type_defs.UpdateFileSystemRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    ClientRequestToken = field("ClientRequestToken")
    StorageCapacity = field("StorageCapacity")

    @cached_property
    def WindowsConfiguration(self):  # pragma: no cover
        return UpdateFileSystemWindowsConfiguration.make_one(
            self.boto3_raw_data["WindowsConfiguration"]
        )

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return UpdateFileSystemLustreConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return UpdateFileSystemOntapConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return UpdateFileSystemOpenZFSConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    StorageType = field("StorageType")
    FileSystemTypeVersion = field("FileSystemTypeVersion")
    NetworkType = field("NetworkType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFileSystemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessPointAttachment:
    boto3_raw_data: "type_defs.S3AccessPointAttachmentTypeDef" = dataclasses.field()

    Lifecycle = field("Lifecycle")

    @cached_property
    def LifecycleTransitionReason(self):  # pragma: no cover
        return LifecycleTransitionReason.make_one(
            self.boto3_raw_data["LifecycleTransitionReason"]
        )

    CreationTime = field("CreationTime")
    Name = field("Name")
    Type = field("Type")

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return S3AccessPointOpenZFSConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    @cached_property
    def S3AccessPoint(self):  # pragma: no cover
        return S3AccessPoint.make_one(self.boto3_raw_data["S3AccessPoint"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3AccessPointAttachmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessPointAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOntapVolumeConfiguration:
    boto3_raw_data: "type_defs.CreateOntapVolumeConfigurationTypeDef" = (
        dataclasses.field()
    )

    StorageVirtualMachineId = field("StorageVirtualMachineId")
    JunctionPath = field("JunctionPath")
    SecurityStyle = field("SecurityStyle")
    SizeInMegabytes = field("SizeInMegabytes")
    StorageEfficiencyEnabled = field("StorageEfficiencyEnabled")

    @cached_property
    def TieringPolicy(self):  # pragma: no cover
        return TieringPolicy.make_one(self.boto3_raw_data["TieringPolicy"])

    OntapVolumeType = field("OntapVolumeType")
    SnapshotPolicy = field("SnapshotPolicy")
    CopyTagsToBackups = field("CopyTagsToBackups")

    @cached_property
    def SnaplockConfiguration(self):  # pragma: no cover
        return CreateSnaplockConfiguration.make_one(
            self.boto3_raw_data["SnaplockConfiguration"]
        )

    VolumeStyle = field("VolumeStyle")

    @cached_property
    def AggregateConfiguration(self):  # pragma: no cover
        return CreateAggregateConfiguration.make_one(
            self.boto3_raw_data["AggregateConfiguration"]
        )

    SizeInBytes = field("SizeInBytes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOntapVolumeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOntapVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OntapVolumeConfiguration:
    boto3_raw_data: "type_defs.OntapVolumeConfigurationTypeDef" = dataclasses.field()

    FlexCacheEndpointType = field("FlexCacheEndpointType")
    JunctionPath = field("JunctionPath")
    SecurityStyle = field("SecurityStyle")
    SizeInMegabytes = field("SizeInMegabytes")
    StorageEfficiencyEnabled = field("StorageEfficiencyEnabled")
    StorageVirtualMachineId = field("StorageVirtualMachineId")
    StorageVirtualMachineRoot = field("StorageVirtualMachineRoot")

    @cached_property
    def TieringPolicy(self):  # pragma: no cover
        return TieringPolicy.make_one(self.boto3_raw_data["TieringPolicy"])

    UUID = field("UUID")
    OntapVolumeType = field("OntapVolumeType")
    SnapshotPolicy = field("SnapshotPolicy")
    CopyTagsToBackups = field("CopyTagsToBackups")

    @cached_property
    def SnaplockConfiguration(self):  # pragma: no cover
        return SnaplockConfiguration.make_one(
            self.boto3_raw_data["SnaplockConfiguration"]
        )

    VolumeStyle = field("VolumeStyle")

    @cached_property
    def AggregateConfiguration(self):  # pragma: no cover
        return AggregateConfiguration.make_one(
            self.boto3_raw_data["AggregateConfiguration"]
        )

    SizeInBytes = field("SizeInBytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OntapVolumeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OntapVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOntapVolumeConfiguration:
    boto3_raw_data: "type_defs.UpdateOntapVolumeConfigurationTypeDef" = (
        dataclasses.field()
    )

    JunctionPath = field("JunctionPath")
    SecurityStyle = field("SecurityStyle")
    SizeInMegabytes = field("SizeInMegabytes")
    StorageEfficiencyEnabled = field("StorageEfficiencyEnabled")

    @cached_property
    def TieringPolicy(self):  # pragma: no cover
        return TieringPolicy.make_one(self.boto3_raw_data["TieringPolicy"])

    SnapshotPolicy = field("SnapshotPolicy")
    CopyTagsToBackups = field("CopyTagsToBackups")

    @cached_property
    def SnaplockConfiguration(self):  # pragma: no cover
        return UpdateSnaplockConfiguration.make_one(
            self.boto3_raw_data["SnaplockConfiguration"]
        )

    SizeInBytes = field("SizeInBytes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateOntapVolumeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOntapVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorageVirtualMachineResponse:
    boto3_raw_data: "type_defs.CreateStorageVirtualMachineResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StorageVirtualMachine(self):  # pragma: no cover
        return StorageVirtualMachine.make_one(
            self.boto3_raw_data["StorageVirtualMachine"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStorageVirtualMachineResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorageVirtualMachineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStorageVirtualMachinesResponse:
    boto3_raw_data: "type_defs.DescribeStorageVirtualMachinesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StorageVirtualMachines(self):  # pragma: no cover
        return StorageVirtualMachine.make_many(
            self.boto3_raw_data["StorageVirtualMachines"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStorageVirtualMachinesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStorageVirtualMachinesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStorageVirtualMachineResponse:
    boto3_raw_data: "type_defs.UpdateStorageVirtualMachineResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StorageVirtualMachine(self):  # pragma: no cover
        return StorageVirtualMachine.make_one(
            self.boto3_raw_data["StorageVirtualMachine"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateStorageVirtualMachineResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStorageVirtualMachineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpenZFSVolumeConfiguration:
    boto3_raw_data: "type_defs.CreateOpenZFSVolumeConfigurationTypeDef" = (
        dataclasses.field()
    )

    ParentVolumeId = field("ParentVolumeId")
    StorageCapacityReservationGiB = field("StorageCapacityReservationGiB")
    StorageCapacityQuotaGiB = field("StorageCapacityQuotaGiB")
    RecordSizeKiB = field("RecordSizeKiB")
    DataCompressionType = field("DataCompressionType")
    CopyTagsToSnapshots = field("CopyTagsToSnapshots")

    @cached_property
    def OriginSnapshot(self):  # pragma: no cover
        return CreateOpenZFSOriginSnapshotConfiguration.make_one(
            self.boto3_raw_data["OriginSnapshot"]
        )

    ReadOnly = field("ReadOnly")
    NfsExports = field("NfsExports")

    @cached_property
    def UserAndGroupQuotas(self):  # pragma: no cover
        return OpenZFSUserOrGroupQuota.make_many(
            self.boto3_raw_data["UserAndGroupQuotas"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOpenZFSVolumeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpenZFSVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenZFSCreateRootVolumeConfiguration:
    boto3_raw_data: "type_defs.OpenZFSCreateRootVolumeConfigurationTypeDef" = (
        dataclasses.field()
    )

    RecordSizeKiB = field("RecordSizeKiB")
    DataCompressionType = field("DataCompressionType")
    NfsExports = field("NfsExports")

    @cached_property
    def UserAndGroupQuotas(self):  # pragma: no cover
        return OpenZFSUserOrGroupQuota.make_many(
            self.boto3_raw_data["UserAndGroupQuotas"]
        )

    CopyTagsToSnapshots = field("CopyTagsToSnapshots")
    ReadOnly = field("ReadOnly")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenZFSCreateRootVolumeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenZFSCreateRootVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpenZFSVolumeConfiguration:
    boto3_raw_data: "type_defs.UpdateOpenZFSVolumeConfigurationTypeDef" = (
        dataclasses.field()
    )

    StorageCapacityReservationGiB = field("StorageCapacityReservationGiB")
    StorageCapacityQuotaGiB = field("StorageCapacityQuotaGiB")
    RecordSizeKiB = field("RecordSizeKiB")
    DataCompressionType = field("DataCompressionType")
    NfsExports = field("NfsExports")

    @cached_property
    def UserAndGroupQuotas(self):  # pragma: no cover
        return OpenZFSUserOrGroupQuota.make_many(
            self.boto3_raw_data["UserAndGroupQuotas"]
        )

    ReadOnly = field("ReadOnly")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateOpenZFSVolumeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpenZFSVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAndAttachS3AccessPointResponse:
    boto3_raw_data: "type_defs.CreateAndAttachS3AccessPointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3AccessPointAttachment(self):  # pragma: no cover
        return S3AccessPointAttachment.make_one(
            self.boto3_raw_data["S3AccessPointAttachment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAndAttachS3AccessPointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAndAttachS3AccessPointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeS3AccessPointAttachmentsResponse:
    boto3_raw_data: "type_defs.DescribeS3AccessPointAttachmentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3AccessPointAttachments(self):  # pragma: no cover
        return S3AccessPointAttachment.make_many(
            self.boto3_raw_data["S3AccessPointAttachments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeS3AccessPointAttachmentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeS3AccessPointAttachmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAndAttachS3AccessPointOpenZFSConfiguration:
    boto3_raw_data: (
        "type_defs.CreateAndAttachS3AccessPointOpenZFSConfigurationTypeDef"
    ) = dataclasses.field()

    VolumeId = field("VolumeId")
    FileSystemIdentity = field("FileSystemIdentity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAndAttachS3AccessPointOpenZFSConfigurationTypeDef"
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
                "type_defs.CreateAndAttachS3AccessPointOpenZFSConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVolumeFromBackupRequest:
    boto3_raw_data: "type_defs.CreateVolumeFromBackupRequestTypeDef" = (
        dataclasses.field()
    )

    BackupId = field("BackupId")
    Name = field("Name")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return CreateOntapVolumeConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVolumeFromBackupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVolumeFromBackupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumePaginator:
    boto3_raw_data: "type_defs.VolumePaginatorTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    FileSystemId = field("FileSystemId")
    Lifecycle = field("Lifecycle")
    Name = field("Name")

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return OntapVolumeConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    VolumeId = field("VolumeId")
    VolumeType = field("VolumeType")

    @cached_property
    def LifecycleTransitionReason(self):  # pragma: no cover
        return LifecycleTransitionReason.make_one(
            self.boto3_raw_data["LifecycleTransitionReason"]
        )

    AdministrativeActions = field("AdministrativeActions")

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return OpenZFSVolumeConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumePaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumePaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Volume:
    boto3_raw_data: "type_defs.VolumeTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    FileSystemId = field("FileSystemId")
    Lifecycle = field("Lifecycle")
    Name = field("Name")

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return OntapVolumeConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    VolumeId = field("VolumeId")
    VolumeType = field("VolumeType")

    @cached_property
    def LifecycleTransitionReason(self):  # pragma: no cover
        return LifecycleTransitionReason.make_one(
            self.boto3_raw_data["LifecycleTransitionReason"]
        )

    AdministrativeActions = field("AdministrativeActions")

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return OpenZFSVolumeConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVolumeRequest:
    boto3_raw_data: "type_defs.CreateVolumeRequestTypeDef" = dataclasses.field()

    VolumeType = field("VolumeType")
    Name = field("Name")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return CreateOntapVolumeConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return CreateOpenZFSVolumeConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemOpenZFSConfiguration:
    boto3_raw_data: "type_defs.CreateFileSystemOpenZFSConfigurationTypeDef" = (
        dataclasses.field()
    )

    DeploymentType = field("DeploymentType")
    ThroughputCapacity = field("ThroughputCapacity")
    AutomaticBackupRetentionDays = field("AutomaticBackupRetentionDays")
    CopyTagsToBackups = field("CopyTagsToBackups")
    CopyTagsToVolumes = field("CopyTagsToVolumes")
    DailyAutomaticBackupStartTime = field("DailyAutomaticBackupStartTime")
    WeeklyMaintenanceStartTime = field("WeeklyMaintenanceStartTime")

    @cached_property
    def DiskIopsConfiguration(self):  # pragma: no cover
        return DiskIopsConfiguration.make_one(
            self.boto3_raw_data["DiskIopsConfiguration"]
        )

    @cached_property
    def RootVolumeConfiguration(self):  # pragma: no cover
        return OpenZFSCreateRootVolumeConfiguration.make_one(
            self.boto3_raw_data["RootVolumeConfiguration"]
        )

    PreferredSubnetId = field("PreferredSubnetId")
    EndpointIpAddressRange = field("EndpointIpAddressRange")
    EndpointIpv6AddressRange = field("EndpointIpv6AddressRange")
    RouteTableIds = field("RouteTableIds")

    @cached_property
    def ReadCacheConfiguration(self):  # pragma: no cover
        return OpenZFSReadCacheConfiguration.make_one(
            self.boto3_raw_data["ReadCacheConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFileSystemOpenZFSConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemOpenZFSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVolumeRequest:
    boto3_raw_data: "type_defs.UpdateVolumeRequestTypeDef" = dataclasses.field()

    VolumeId = field("VolumeId")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return UpdateOntapVolumeConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    Name = field("Name")

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return UpdateOpenZFSVolumeConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAndAttachS3AccessPointRequest:
    boto3_raw_data: "type_defs.CreateAndAttachS3AccessPointRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Type = field("Type")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return CreateAndAttachS3AccessPointOpenZFSConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    @cached_property
    def S3AccessPoint(self):  # pragma: no cover
        return CreateAndAttachS3AccessPointS3Configuration.make_one(
            self.boto3_raw_data["S3AccessPoint"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAndAttachS3AccessPointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAndAttachS3AccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdministrativeActionPaginator:
    boto3_raw_data: "type_defs.AdministrativeActionPaginatorTypeDef" = (
        dataclasses.field()
    )

    AdministrativeActionType = field("AdministrativeActionType")
    ProgressPercent = field("ProgressPercent")
    RequestTime = field("RequestTime")
    Status = field("Status")
    TargetFileSystemValues = field("TargetFileSystemValues")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return AdministrativeActionFailureDetails.make_one(
            self.boto3_raw_data["FailureDetails"]
        )

    @cached_property
    def TargetVolumeValues(self):  # pragma: no cover
        return VolumePaginator.make_one(self.boto3_raw_data["TargetVolumeValues"])

    @cached_property
    def TargetSnapshotValues(self):  # pragma: no cover
        return SnapshotPaginator.make_one(self.boto3_raw_data["TargetSnapshotValues"])

    TotalTransferBytes = field("TotalTransferBytes")
    RemainingTransferBytes = field("RemainingTransferBytes")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdministrativeActionPaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdministrativeActionPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVolumesResponsePaginator:
    boto3_raw_data: "type_defs.DescribeVolumesResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Volumes(self):  # pragma: no cover
        return VolumePaginator.make_many(self.boto3_raw_data["Volumes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeVolumesResponsePaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVolumesResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdministrativeAction:
    boto3_raw_data: "type_defs.AdministrativeActionTypeDef" = dataclasses.field()

    AdministrativeActionType = field("AdministrativeActionType")
    ProgressPercent = field("ProgressPercent")
    RequestTime = field("RequestTime")
    Status = field("Status")
    TargetFileSystemValues = field("TargetFileSystemValues")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return AdministrativeActionFailureDetails.make_one(
            self.boto3_raw_data["FailureDetails"]
        )

    @cached_property
    def TargetVolumeValues(self):  # pragma: no cover
        return Volume.make_one(self.boto3_raw_data["TargetVolumeValues"])

    @cached_property
    def TargetSnapshotValues(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["TargetSnapshotValues"])

    TotalTransferBytes = field("TotalTransferBytes")
    RemainingTransferBytes = field("RemainingTransferBytes")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdministrativeActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdministrativeActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVolumeFromBackupResponse:
    boto3_raw_data: "type_defs.CreateVolumeFromBackupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Volume(self):  # pragma: no cover
        return Volume.make_one(self.boto3_raw_data["Volume"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVolumeFromBackupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVolumeFromBackupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVolumeResponse:
    boto3_raw_data: "type_defs.CreateVolumeResponseTypeDef" = dataclasses.field()

    @cached_property
    def Volume(self):  # pragma: no cover
        return Volume.make_one(self.boto3_raw_data["Volume"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVolumeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVolumeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVolumesResponse:
    boto3_raw_data: "type_defs.DescribeVolumesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["Volumes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVolumesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVolumesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVolumeResponse:
    boto3_raw_data: "type_defs.UpdateVolumeResponseTypeDef" = dataclasses.field()

    @cached_property
    def Volume(self):  # pragma: no cover
        return Volume.make_one(self.boto3_raw_data["Volume"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVolumeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVolumeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemFromBackupRequest:
    boto3_raw_data: "type_defs.CreateFileSystemFromBackupRequestTypeDef" = (
        dataclasses.field()
    )

    BackupId = field("BackupId")
    SubnetIds = field("SubnetIds")
    ClientRequestToken = field("ClientRequestToken")
    SecurityGroupIds = field("SecurityGroupIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def WindowsConfiguration(self):  # pragma: no cover
        return CreateFileSystemWindowsConfiguration.make_one(
            self.boto3_raw_data["WindowsConfiguration"]
        )

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return CreateFileSystemLustreConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    StorageType = field("StorageType")
    KmsKeyId = field("KmsKeyId")
    FileSystemTypeVersion = field("FileSystemTypeVersion")

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return CreateFileSystemOpenZFSConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    StorageCapacity = field("StorageCapacity")
    NetworkType = field("NetworkType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFileSystemFromBackupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemFromBackupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemRequest:
    boto3_raw_data: "type_defs.CreateFileSystemRequestTypeDef" = dataclasses.field()

    FileSystemType = field("FileSystemType")
    SubnetIds = field("SubnetIds")
    ClientRequestToken = field("ClientRequestToken")
    StorageCapacity = field("StorageCapacity")
    StorageType = field("StorageType")
    SecurityGroupIds = field("SecurityGroupIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KmsKeyId = field("KmsKeyId")

    @cached_property
    def WindowsConfiguration(self):  # pragma: no cover
        return CreateFileSystemWindowsConfiguration.make_one(
            self.boto3_raw_data["WindowsConfiguration"]
        )

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return CreateFileSystemLustreConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return CreateFileSystemOntapConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    FileSystemTypeVersion = field("FileSystemTypeVersion")

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return CreateFileSystemOpenZFSConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    NetworkType = field("NetworkType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFileSystemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemPaginator:
    boto3_raw_data: "type_defs.FileSystemPaginatorTypeDef" = dataclasses.field()

    OwnerId = field("OwnerId")
    CreationTime = field("CreationTime")
    FileSystemId = field("FileSystemId")
    FileSystemType = field("FileSystemType")
    Lifecycle = field("Lifecycle")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FileSystemFailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    StorageCapacity = field("StorageCapacity")
    StorageType = field("StorageType")
    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    NetworkInterfaceIds = field("NetworkInterfaceIds")
    DNSName = field("DNSName")
    KmsKeyId = field("KmsKeyId")
    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def WindowsConfiguration(self):  # pragma: no cover
        return WindowsFileSystemConfiguration.make_one(
            self.boto3_raw_data["WindowsConfiguration"]
        )

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return LustreFileSystemConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    @cached_property
    def AdministrativeActions(self):  # pragma: no cover
        return AdministrativeActionPaginator.make_many(
            self.boto3_raw_data["AdministrativeActions"]
        )

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return OntapFileSystemConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    FileSystemTypeVersion = field("FileSystemTypeVersion")

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return OpenZFSFileSystemConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    NetworkType = field("NetworkType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSystemPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySnapshotAndUpdateVolumeResponse:
    boto3_raw_data: "type_defs.CopySnapshotAndUpdateVolumeResponseTypeDef" = (
        dataclasses.field()
    )

    VolumeId = field("VolumeId")
    Lifecycle = field("Lifecycle")

    @cached_property
    def AdministrativeActions(self):  # pragma: no cover
        return AdministrativeAction.make_many(
            self.boto3_raw_data["AdministrativeActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopySnapshotAndUpdateVolumeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySnapshotAndUpdateVolumeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystem:
    boto3_raw_data: "type_defs.FileSystemTypeDef" = dataclasses.field()

    OwnerId = field("OwnerId")
    CreationTime = field("CreationTime")
    FileSystemId = field("FileSystemId")
    FileSystemType = field("FileSystemType")
    Lifecycle = field("Lifecycle")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FileSystemFailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    StorageCapacity = field("StorageCapacity")
    StorageType = field("StorageType")
    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    NetworkInterfaceIds = field("NetworkInterfaceIds")
    DNSName = field("DNSName")
    KmsKeyId = field("KmsKeyId")
    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def WindowsConfiguration(self):  # pragma: no cover
        return WindowsFileSystemConfiguration.make_one(
            self.boto3_raw_data["WindowsConfiguration"]
        )

    @cached_property
    def LustreConfiguration(self):  # pragma: no cover
        return LustreFileSystemConfiguration.make_one(
            self.boto3_raw_data["LustreConfiguration"]
        )

    @cached_property
    def AdministrativeActions(self):  # pragma: no cover
        return AdministrativeAction.make_many(
            self.boto3_raw_data["AdministrativeActions"]
        )

    @cached_property
    def OntapConfiguration(self):  # pragma: no cover
        return OntapFileSystemConfiguration.make_one(
            self.boto3_raw_data["OntapConfiguration"]
        )

    FileSystemTypeVersion = field("FileSystemTypeVersion")

    @cached_property
    def OpenZFSConfiguration(self):  # pragma: no cover
        return OpenZFSFileSystemConfiguration.make_one(
            self.boto3_raw_data["OpenZFSConfiguration"]
        )

    NetworkType = field("NetworkType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileSystemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileSystemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreVolumeFromSnapshotResponse:
    boto3_raw_data: "type_defs.RestoreVolumeFromSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    VolumeId = field("VolumeId")
    Lifecycle = field("Lifecycle")

    @cached_property
    def AdministrativeActions(self):  # pragma: no cover
        return AdministrativeAction.make_many(
            self.boto3_raw_data["AdministrativeActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreVolumeFromSnapshotResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreVolumeFromSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupPaginator:
    boto3_raw_data: "type_defs.BackupPaginatorTypeDef" = dataclasses.field()

    BackupId = field("BackupId")
    Lifecycle = field("Lifecycle")
    Type = field("Type")
    CreationTime = field("CreationTime")

    @cached_property
    def FileSystem(self):  # pragma: no cover
        return FileSystemPaginator.make_one(self.boto3_raw_data["FileSystem"])

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return BackupFailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    ProgressPercent = field("ProgressPercent")
    KmsKeyId = field("KmsKeyId")
    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def DirectoryInformation(self):  # pragma: no cover
        return ActiveDirectoryBackupAttributes.make_one(
            self.boto3_raw_data["DirectoryInformation"]
        )

    OwnerId = field("OwnerId")
    SourceBackupId = field("SourceBackupId")
    SourceBackupRegion = field("SourceBackupRegion")
    ResourceType = field("ResourceType")

    @cached_property
    def Volume(self):  # pragma: no cover
        return VolumePaginator.make_one(self.boto3_raw_data["Volume"])

    SizeInBytes = field("SizeInBytes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupPaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemsResponsePaginator:
    boto3_raw_data: "type_defs.DescribeFileSystemsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FileSystems(self):  # pragma: no cover
        return FileSystemPaginator.make_many(self.boto3_raw_data["FileSystems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFileSystemsResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Backup:
    boto3_raw_data: "type_defs.BackupTypeDef" = dataclasses.field()

    BackupId = field("BackupId")
    Lifecycle = field("Lifecycle")
    Type = field("Type")
    CreationTime = field("CreationTime")

    @cached_property
    def FileSystem(self):  # pragma: no cover
        return FileSystem.make_one(self.boto3_raw_data["FileSystem"])

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return BackupFailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    ProgressPercent = field("ProgressPercent")
    KmsKeyId = field("KmsKeyId")
    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def DirectoryInformation(self):  # pragma: no cover
        return ActiveDirectoryBackupAttributes.make_one(
            self.boto3_raw_data["DirectoryInformation"]
        )

    OwnerId = field("OwnerId")
    SourceBackupId = field("SourceBackupId")
    SourceBackupRegion = field("SourceBackupRegion")
    ResourceType = field("ResourceType")

    @cached_property
    def Volume(self):  # pragma: no cover
        return Volume.make_one(self.boto3_raw_data["Volume"])

    SizeInBytes = field("SizeInBytes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemFromBackupResponse:
    boto3_raw_data: "type_defs.CreateFileSystemFromBackupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FileSystem(self):  # pragma: no cover
        return FileSystem.make_one(self.boto3_raw_data["FileSystem"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFileSystemFromBackupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemFromBackupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemResponse:
    boto3_raw_data: "type_defs.CreateFileSystemResponseTypeDef" = dataclasses.field()

    @cached_property
    def FileSystem(self):  # pragma: no cover
        return FileSystem.make_one(self.boto3_raw_data["FileSystem"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFileSystemResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemsResponse:
    boto3_raw_data: "type_defs.DescribeFileSystemsResponseTypeDef" = dataclasses.field()

    @cached_property
    def FileSystems(self):  # pragma: no cover
        return FileSystem.make_many(self.boto3_raw_data["FileSystems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFileSystemsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleaseFileSystemNfsV3LocksResponse:
    boto3_raw_data: "type_defs.ReleaseFileSystemNfsV3LocksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FileSystem(self):  # pragma: no cover
        return FileSystem.make_one(self.boto3_raw_data["FileSystem"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReleaseFileSystemNfsV3LocksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleaseFileSystemNfsV3LocksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMisconfiguredStateRecoveryResponse:
    boto3_raw_data: "type_defs.StartMisconfiguredStateRecoveryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FileSystem(self):  # pragma: no cover
        return FileSystem.make_one(self.boto3_raw_data["FileSystem"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMisconfiguredStateRecoveryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMisconfiguredStateRecoveryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemResponse:
    boto3_raw_data: "type_defs.UpdateFileSystemResponseTypeDef" = dataclasses.field()

    @cached_property
    def FileSystem(self):  # pragma: no cover
        return FileSystem.make_one(self.boto3_raw_data["FileSystem"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFileSystemResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupsResponsePaginator:
    boto3_raw_data: "type_defs.DescribeBackupsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Backups(self):  # pragma: no cover
        return BackupPaginator.make_many(self.boto3_raw_data["Backups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBackupsResponsePaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyBackupResponse:
    boto3_raw_data: "type_defs.CopyBackupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Backup(self):  # pragma: no cover
        return Backup.make_one(self.boto3_raw_data["Backup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyBackupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyBackupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackupResponse:
    boto3_raw_data: "type_defs.CreateBackupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Backup(self):  # pragma: no cover
        return Backup.make_one(self.boto3_raw_data["Backup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupsResponse:
    boto3_raw_data: "type_defs.DescribeBackupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Backups(self):  # pragma: no cover
        return Backup.make_many(self.boto3_raw_data["Backups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBackupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
