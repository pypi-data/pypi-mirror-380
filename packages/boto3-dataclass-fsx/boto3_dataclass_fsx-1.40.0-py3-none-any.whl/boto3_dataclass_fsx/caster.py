# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_fsx import type_defs as bs_td


class FSXCaster:

    def associate_file_system_aliases(
        self,
        res: "bs_td.AssociateFileSystemAliasesResponseTypeDef",
    ) -> "dc_td.AssociateFileSystemAliasesResponse":
        return dc_td.AssociateFileSystemAliasesResponse.make_one(res)

    def cancel_data_repository_task(
        self,
        res: "bs_td.CancelDataRepositoryTaskResponseTypeDef",
    ) -> "dc_td.CancelDataRepositoryTaskResponse":
        return dc_td.CancelDataRepositoryTaskResponse.make_one(res)

    def copy_backup(
        self,
        res: "bs_td.CopyBackupResponseTypeDef",
    ) -> "dc_td.CopyBackupResponse":
        return dc_td.CopyBackupResponse.make_one(res)

    def copy_snapshot_and_update_volume(
        self,
        res: "bs_td.CopySnapshotAndUpdateVolumeResponseTypeDef",
    ) -> "dc_td.CopySnapshotAndUpdateVolumeResponse":
        return dc_td.CopySnapshotAndUpdateVolumeResponse.make_one(res)

    def create_and_attach_s3_access_point(
        self,
        res: "bs_td.CreateAndAttachS3AccessPointResponseTypeDef",
    ) -> "dc_td.CreateAndAttachS3AccessPointResponse":
        return dc_td.CreateAndAttachS3AccessPointResponse.make_one(res)

    def create_backup(
        self,
        res: "bs_td.CreateBackupResponseTypeDef",
    ) -> "dc_td.CreateBackupResponse":
        return dc_td.CreateBackupResponse.make_one(res)

    def create_data_repository_association(
        self,
        res: "bs_td.CreateDataRepositoryAssociationResponseTypeDef",
    ) -> "dc_td.CreateDataRepositoryAssociationResponse":
        return dc_td.CreateDataRepositoryAssociationResponse.make_one(res)

    def create_data_repository_task(
        self,
        res: "bs_td.CreateDataRepositoryTaskResponseTypeDef",
    ) -> "dc_td.CreateDataRepositoryTaskResponse":
        return dc_td.CreateDataRepositoryTaskResponse.make_one(res)

    def create_file_cache(
        self,
        res: "bs_td.CreateFileCacheResponseTypeDef",
    ) -> "dc_td.CreateFileCacheResponse":
        return dc_td.CreateFileCacheResponse.make_one(res)

    def create_file_system(
        self,
        res: "bs_td.CreateFileSystemResponseTypeDef",
    ) -> "dc_td.CreateFileSystemResponse":
        return dc_td.CreateFileSystemResponse.make_one(res)

    def create_file_system_from_backup(
        self,
        res: "bs_td.CreateFileSystemFromBackupResponseTypeDef",
    ) -> "dc_td.CreateFileSystemFromBackupResponse":
        return dc_td.CreateFileSystemFromBackupResponse.make_one(res)

    def create_snapshot(
        self,
        res: "bs_td.CreateSnapshotResponseTypeDef",
    ) -> "dc_td.CreateSnapshotResponse":
        return dc_td.CreateSnapshotResponse.make_one(res)

    def create_storage_virtual_machine(
        self,
        res: "bs_td.CreateStorageVirtualMachineResponseTypeDef",
    ) -> "dc_td.CreateStorageVirtualMachineResponse":
        return dc_td.CreateStorageVirtualMachineResponse.make_one(res)

    def create_volume(
        self,
        res: "bs_td.CreateVolumeResponseTypeDef",
    ) -> "dc_td.CreateVolumeResponse":
        return dc_td.CreateVolumeResponse.make_one(res)

    def create_volume_from_backup(
        self,
        res: "bs_td.CreateVolumeFromBackupResponseTypeDef",
    ) -> "dc_td.CreateVolumeFromBackupResponse":
        return dc_td.CreateVolumeFromBackupResponse.make_one(res)

    def delete_backup(
        self,
        res: "bs_td.DeleteBackupResponseTypeDef",
    ) -> "dc_td.DeleteBackupResponse":
        return dc_td.DeleteBackupResponse.make_one(res)

    def delete_data_repository_association(
        self,
        res: "bs_td.DeleteDataRepositoryAssociationResponseTypeDef",
    ) -> "dc_td.DeleteDataRepositoryAssociationResponse":
        return dc_td.DeleteDataRepositoryAssociationResponse.make_one(res)

    def delete_file_cache(
        self,
        res: "bs_td.DeleteFileCacheResponseTypeDef",
    ) -> "dc_td.DeleteFileCacheResponse":
        return dc_td.DeleteFileCacheResponse.make_one(res)

    def delete_file_system(
        self,
        res: "bs_td.DeleteFileSystemResponseTypeDef",
    ) -> "dc_td.DeleteFileSystemResponse":
        return dc_td.DeleteFileSystemResponse.make_one(res)

    def delete_snapshot(
        self,
        res: "bs_td.DeleteSnapshotResponseTypeDef",
    ) -> "dc_td.DeleteSnapshotResponse":
        return dc_td.DeleteSnapshotResponse.make_one(res)

    def delete_storage_virtual_machine(
        self,
        res: "bs_td.DeleteStorageVirtualMachineResponseTypeDef",
    ) -> "dc_td.DeleteStorageVirtualMachineResponse":
        return dc_td.DeleteStorageVirtualMachineResponse.make_one(res)

    def delete_volume(
        self,
        res: "bs_td.DeleteVolumeResponseTypeDef",
    ) -> "dc_td.DeleteVolumeResponse":
        return dc_td.DeleteVolumeResponse.make_one(res)

    def describe_backups(
        self,
        res: "bs_td.DescribeBackupsResponseTypeDef",
    ) -> "dc_td.DescribeBackupsResponse":
        return dc_td.DescribeBackupsResponse.make_one(res)

    def describe_data_repository_associations(
        self,
        res: "bs_td.DescribeDataRepositoryAssociationsResponseTypeDef",
    ) -> "dc_td.DescribeDataRepositoryAssociationsResponse":
        return dc_td.DescribeDataRepositoryAssociationsResponse.make_one(res)

    def describe_data_repository_tasks(
        self,
        res: "bs_td.DescribeDataRepositoryTasksResponseTypeDef",
    ) -> "dc_td.DescribeDataRepositoryTasksResponse":
        return dc_td.DescribeDataRepositoryTasksResponse.make_one(res)

    def describe_file_caches(
        self,
        res: "bs_td.DescribeFileCachesResponseTypeDef",
    ) -> "dc_td.DescribeFileCachesResponse":
        return dc_td.DescribeFileCachesResponse.make_one(res)

    def describe_file_system_aliases(
        self,
        res: "bs_td.DescribeFileSystemAliasesResponseTypeDef",
    ) -> "dc_td.DescribeFileSystemAliasesResponse":
        return dc_td.DescribeFileSystemAliasesResponse.make_one(res)

    def describe_file_systems(
        self,
        res: "bs_td.DescribeFileSystemsResponseTypeDef",
    ) -> "dc_td.DescribeFileSystemsResponse":
        return dc_td.DescribeFileSystemsResponse.make_one(res)

    def describe_s3_access_point_attachments(
        self,
        res: "bs_td.DescribeS3AccessPointAttachmentsResponseTypeDef",
    ) -> "dc_td.DescribeS3AccessPointAttachmentsResponse":
        return dc_td.DescribeS3AccessPointAttachmentsResponse.make_one(res)

    def describe_shared_vpc_configuration(
        self,
        res: "bs_td.DescribeSharedVpcConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeSharedVpcConfigurationResponse":
        return dc_td.DescribeSharedVpcConfigurationResponse.make_one(res)

    def describe_snapshots(
        self,
        res: "bs_td.DescribeSnapshotsResponseTypeDef",
    ) -> "dc_td.DescribeSnapshotsResponse":
        return dc_td.DescribeSnapshotsResponse.make_one(res)

    def describe_storage_virtual_machines(
        self,
        res: "bs_td.DescribeStorageVirtualMachinesResponseTypeDef",
    ) -> "dc_td.DescribeStorageVirtualMachinesResponse":
        return dc_td.DescribeStorageVirtualMachinesResponse.make_one(res)

    def describe_volumes(
        self,
        res: "bs_td.DescribeVolumesResponseTypeDef",
    ) -> "dc_td.DescribeVolumesResponse":
        return dc_td.DescribeVolumesResponse.make_one(res)

    def detach_and_delete_s3_access_point(
        self,
        res: "bs_td.DetachAndDeleteS3AccessPointResponseTypeDef",
    ) -> "dc_td.DetachAndDeleteS3AccessPointResponse":
        return dc_td.DetachAndDeleteS3AccessPointResponse.make_one(res)

    def disassociate_file_system_aliases(
        self,
        res: "bs_td.DisassociateFileSystemAliasesResponseTypeDef",
    ) -> "dc_td.DisassociateFileSystemAliasesResponse":
        return dc_td.DisassociateFileSystemAliasesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def release_file_system_nfs_v3_locks(
        self,
        res: "bs_td.ReleaseFileSystemNfsV3LocksResponseTypeDef",
    ) -> "dc_td.ReleaseFileSystemNfsV3LocksResponse":
        return dc_td.ReleaseFileSystemNfsV3LocksResponse.make_one(res)

    def restore_volume_from_snapshot(
        self,
        res: "bs_td.RestoreVolumeFromSnapshotResponseTypeDef",
    ) -> "dc_td.RestoreVolumeFromSnapshotResponse":
        return dc_td.RestoreVolumeFromSnapshotResponse.make_one(res)

    def start_misconfigured_state_recovery(
        self,
        res: "bs_td.StartMisconfiguredStateRecoveryResponseTypeDef",
    ) -> "dc_td.StartMisconfiguredStateRecoveryResponse":
        return dc_td.StartMisconfiguredStateRecoveryResponse.make_one(res)

    def update_data_repository_association(
        self,
        res: "bs_td.UpdateDataRepositoryAssociationResponseTypeDef",
    ) -> "dc_td.UpdateDataRepositoryAssociationResponse":
        return dc_td.UpdateDataRepositoryAssociationResponse.make_one(res)

    def update_file_cache(
        self,
        res: "bs_td.UpdateFileCacheResponseTypeDef",
    ) -> "dc_td.UpdateFileCacheResponse":
        return dc_td.UpdateFileCacheResponse.make_one(res)

    def update_file_system(
        self,
        res: "bs_td.UpdateFileSystemResponseTypeDef",
    ) -> "dc_td.UpdateFileSystemResponse":
        return dc_td.UpdateFileSystemResponse.make_one(res)

    def update_shared_vpc_configuration(
        self,
        res: "bs_td.UpdateSharedVpcConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateSharedVpcConfigurationResponse":
        return dc_td.UpdateSharedVpcConfigurationResponse.make_one(res)

    def update_snapshot(
        self,
        res: "bs_td.UpdateSnapshotResponseTypeDef",
    ) -> "dc_td.UpdateSnapshotResponse":
        return dc_td.UpdateSnapshotResponse.make_one(res)

    def update_storage_virtual_machine(
        self,
        res: "bs_td.UpdateStorageVirtualMachineResponseTypeDef",
    ) -> "dc_td.UpdateStorageVirtualMachineResponse":
        return dc_td.UpdateStorageVirtualMachineResponse.make_one(res)

    def update_volume(
        self,
        res: "bs_td.UpdateVolumeResponseTypeDef",
    ) -> "dc_td.UpdateVolumeResponse":
        return dc_td.UpdateVolumeResponse.make_one(res)


fsx_caster = FSXCaster()
