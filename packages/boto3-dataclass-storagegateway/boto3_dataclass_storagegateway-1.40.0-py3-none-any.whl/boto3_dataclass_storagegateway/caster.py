# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_storagegateway import type_defs as bs_td


class STORAGEGATEWAYCaster:

    def activate_gateway(
        self,
        res: "bs_td.ActivateGatewayOutputTypeDef",
    ) -> "dc_td.ActivateGatewayOutput":
        return dc_td.ActivateGatewayOutput.make_one(res)

    def add_cache(
        self,
        res: "bs_td.AddCacheOutputTypeDef",
    ) -> "dc_td.AddCacheOutput":
        return dc_td.AddCacheOutput.make_one(res)

    def add_tags_to_resource(
        self,
        res: "bs_td.AddTagsToResourceOutputTypeDef",
    ) -> "dc_td.AddTagsToResourceOutput":
        return dc_td.AddTagsToResourceOutput.make_one(res)

    def add_upload_buffer(
        self,
        res: "bs_td.AddUploadBufferOutputTypeDef",
    ) -> "dc_td.AddUploadBufferOutput":
        return dc_td.AddUploadBufferOutput.make_one(res)

    def add_working_storage(
        self,
        res: "bs_td.AddWorkingStorageOutputTypeDef",
    ) -> "dc_td.AddWorkingStorageOutput":
        return dc_td.AddWorkingStorageOutput.make_one(res)

    def assign_tape_pool(
        self,
        res: "bs_td.AssignTapePoolOutputTypeDef",
    ) -> "dc_td.AssignTapePoolOutput":
        return dc_td.AssignTapePoolOutput.make_one(res)

    def associate_file_system(
        self,
        res: "bs_td.AssociateFileSystemOutputTypeDef",
    ) -> "dc_td.AssociateFileSystemOutput":
        return dc_td.AssociateFileSystemOutput.make_one(res)

    def attach_volume(
        self,
        res: "bs_td.AttachVolumeOutputTypeDef",
    ) -> "dc_td.AttachVolumeOutput":
        return dc_td.AttachVolumeOutput.make_one(res)

    def cancel_archival(
        self,
        res: "bs_td.CancelArchivalOutputTypeDef",
    ) -> "dc_td.CancelArchivalOutput":
        return dc_td.CancelArchivalOutput.make_one(res)

    def cancel_cache_report(
        self,
        res: "bs_td.CancelCacheReportOutputTypeDef",
    ) -> "dc_td.CancelCacheReportOutput":
        return dc_td.CancelCacheReportOutput.make_one(res)

    def cancel_retrieval(
        self,
        res: "bs_td.CancelRetrievalOutputTypeDef",
    ) -> "dc_td.CancelRetrievalOutput":
        return dc_td.CancelRetrievalOutput.make_one(res)

    def create_cached_iscsi_volume(
        self,
        res: "bs_td.CreateCachediSCSIVolumeOutputTypeDef",
    ) -> "dc_td.CreateCachediSCSIVolumeOutput":
        return dc_td.CreateCachediSCSIVolumeOutput.make_one(res)

    def create_nfs_file_share(
        self,
        res: "bs_td.CreateNFSFileShareOutputTypeDef",
    ) -> "dc_td.CreateNFSFileShareOutput":
        return dc_td.CreateNFSFileShareOutput.make_one(res)

    def create_smb_file_share(
        self,
        res: "bs_td.CreateSMBFileShareOutputTypeDef",
    ) -> "dc_td.CreateSMBFileShareOutput":
        return dc_td.CreateSMBFileShareOutput.make_one(res)

    def create_snapshot(
        self,
        res: "bs_td.CreateSnapshotOutputTypeDef",
    ) -> "dc_td.CreateSnapshotOutput":
        return dc_td.CreateSnapshotOutput.make_one(res)

    def create_snapshot_from_volume_recovery_point(
        self,
        res: "bs_td.CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    ) -> "dc_td.CreateSnapshotFromVolumeRecoveryPointOutput":
        return dc_td.CreateSnapshotFromVolumeRecoveryPointOutput.make_one(res)

    def create_stored_iscsi_volume(
        self,
        res: "bs_td.CreateStorediSCSIVolumeOutputTypeDef",
    ) -> "dc_td.CreateStorediSCSIVolumeOutput":
        return dc_td.CreateStorediSCSIVolumeOutput.make_one(res)

    def create_tape_pool(
        self,
        res: "bs_td.CreateTapePoolOutputTypeDef",
    ) -> "dc_td.CreateTapePoolOutput":
        return dc_td.CreateTapePoolOutput.make_one(res)

    def create_tape_with_barcode(
        self,
        res: "bs_td.CreateTapeWithBarcodeOutputTypeDef",
    ) -> "dc_td.CreateTapeWithBarcodeOutput":
        return dc_td.CreateTapeWithBarcodeOutput.make_one(res)

    def create_tapes(
        self,
        res: "bs_td.CreateTapesOutputTypeDef",
    ) -> "dc_td.CreateTapesOutput":
        return dc_td.CreateTapesOutput.make_one(res)

    def delete_automatic_tape_creation_policy(
        self,
        res: "bs_td.DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    ) -> "dc_td.DeleteAutomaticTapeCreationPolicyOutput":
        return dc_td.DeleteAutomaticTapeCreationPolicyOutput.make_one(res)

    def delete_bandwidth_rate_limit(
        self,
        res: "bs_td.DeleteBandwidthRateLimitOutputTypeDef",
    ) -> "dc_td.DeleteBandwidthRateLimitOutput":
        return dc_td.DeleteBandwidthRateLimitOutput.make_one(res)

    def delete_cache_report(
        self,
        res: "bs_td.DeleteCacheReportOutputTypeDef",
    ) -> "dc_td.DeleteCacheReportOutput":
        return dc_td.DeleteCacheReportOutput.make_one(res)

    def delete_chap_credentials(
        self,
        res: "bs_td.DeleteChapCredentialsOutputTypeDef",
    ) -> "dc_td.DeleteChapCredentialsOutput":
        return dc_td.DeleteChapCredentialsOutput.make_one(res)

    def delete_file_share(
        self,
        res: "bs_td.DeleteFileShareOutputTypeDef",
    ) -> "dc_td.DeleteFileShareOutput":
        return dc_td.DeleteFileShareOutput.make_one(res)

    def delete_gateway(
        self,
        res: "bs_td.DeleteGatewayOutputTypeDef",
    ) -> "dc_td.DeleteGatewayOutput":
        return dc_td.DeleteGatewayOutput.make_one(res)

    def delete_snapshot_schedule(
        self,
        res: "bs_td.DeleteSnapshotScheduleOutputTypeDef",
    ) -> "dc_td.DeleteSnapshotScheduleOutput":
        return dc_td.DeleteSnapshotScheduleOutput.make_one(res)

    def delete_tape(
        self,
        res: "bs_td.DeleteTapeOutputTypeDef",
    ) -> "dc_td.DeleteTapeOutput":
        return dc_td.DeleteTapeOutput.make_one(res)

    def delete_tape_archive(
        self,
        res: "bs_td.DeleteTapeArchiveOutputTypeDef",
    ) -> "dc_td.DeleteTapeArchiveOutput":
        return dc_td.DeleteTapeArchiveOutput.make_one(res)

    def delete_tape_pool(
        self,
        res: "bs_td.DeleteTapePoolOutputTypeDef",
    ) -> "dc_td.DeleteTapePoolOutput":
        return dc_td.DeleteTapePoolOutput.make_one(res)

    def delete_volume(
        self,
        res: "bs_td.DeleteVolumeOutputTypeDef",
    ) -> "dc_td.DeleteVolumeOutput":
        return dc_td.DeleteVolumeOutput.make_one(res)

    def describe_availability_monitor_test(
        self,
        res: "bs_td.DescribeAvailabilityMonitorTestOutputTypeDef",
    ) -> "dc_td.DescribeAvailabilityMonitorTestOutput":
        return dc_td.DescribeAvailabilityMonitorTestOutput.make_one(res)

    def describe_bandwidth_rate_limit(
        self,
        res: "bs_td.DescribeBandwidthRateLimitOutputTypeDef",
    ) -> "dc_td.DescribeBandwidthRateLimitOutput":
        return dc_td.DescribeBandwidthRateLimitOutput.make_one(res)

    def describe_bandwidth_rate_limit_schedule(
        self,
        res: "bs_td.DescribeBandwidthRateLimitScheduleOutputTypeDef",
    ) -> "dc_td.DescribeBandwidthRateLimitScheduleOutput":
        return dc_td.DescribeBandwidthRateLimitScheduleOutput.make_one(res)

    def describe_cache(
        self,
        res: "bs_td.DescribeCacheOutputTypeDef",
    ) -> "dc_td.DescribeCacheOutput":
        return dc_td.DescribeCacheOutput.make_one(res)

    def describe_cache_report(
        self,
        res: "bs_td.DescribeCacheReportOutputTypeDef",
    ) -> "dc_td.DescribeCacheReportOutput":
        return dc_td.DescribeCacheReportOutput.make_one(res)

    def describe_cached_iscsi_volumes(
        self,
        res: "bs_td.DescribeCachediSCSIVolumesOutputTypeDef",
    ) -> "dc_td.DescribeCachediSCSIVolumesOutput":
        return dc_td.DescribeCachediSCSIVolumesOutput.make_one(res)

    def describe_chap_credentials(
        self,
        res: "bs_td.DescribeChapCredentialsOutputTypeDef",
    ) -> "dc_td.DescribeChapCredentialsOutput":
        return dc_td.DescribeChapCredentialsOutput.make_one(res)

    def describe_file_system_associations(
        self,
        res: "bs_td.DescribeFileSystemAssociationsOutputTypeDef",
    ) -> "dc_td.DescribeFileSystemAssociationsOutput":
        return dc_td.DescribeFileSystemAssociationsOutput.make_one(res)

    def describe_gateway_information(
        self,
        res: "bs_td.DescribeGatewayInformationOutputTypeDef",
    ) -> "dc_td.DescribeGatewayInformationOutput":
        return dc_td.DescribeGatewayInformationOutput.make_one(res)

    def describe_maintenance_start_time(
        self,
        res: "bs_td.DescribeMaintenanceStartTimeOutputTypeDef",
    ) -> "dc_td.DescribeMaintenanceStartTimeOutput":
        return dc_td.DescribeMaintenanceStartTimeOutput.make_one(res)

    def describe_nfs_file_shares(
        self,
        res: "bs_td.DescribeNFSFileSharesOutputTypeDef",
    ) -> "dc_td.DescribeNFSFileSharesOutput":
        return dc_td.DescribeNFSFileSharesOutput.make_one(res)

    def describe_smb_file_shares(
        self,
        res: "bs_td.DescribeSMBFileSharesOutputTypeDef",
    ) -> "dc_td.DescribeSMBFileSharesOutput":
        return dc_td.DescribeSMBFileSharesOutput.make_one(res)

    def describe_smb_settings(
        self,
        res: "bs_td.DescribeSMBSettingsOutputTypeDef",
    ) -> "dc_td.DescribeSMBSettingsOutput":
        return dc_td.DescribeSMBSettingsOutput.make_one(res)

    def describe_snapshot_schedule(
        self,
        res: "bs_td.DescribeSnapshotScheduleOutputTypeDef",
    ) -> "dc_td.DescribeSnapshotScheduleOutput":
        return dc_td.DescribeSnapshotScheduleOutput.make_one(res)

    def describe_stored_iscsi_volumes(
        self,
        res: "bs_td.DescribeStorediSCSIVolumesOutputTypeDef",
    ) -> "dc_td.DescribeStorediSCSIVolumesOutput":
        return dc_td.DescribeStorediSCSIVolumesOutput.make_one(res)

    def describe_tape_archives(
        self,
        res: "bs_td.DescribeTapeArchivesOutputTypeDef",
    ) -> "dc_td.DescribeTapeArchivesOutput":
        return dc_td.DescribeTapeArchivesOutput.make_one(res)

    def describe_tape_recovery_points(
        self,
        res: "bs_td.DescribeTapeRecoveryPointsOutputTypeDef",
    ) -> "dc_td.DescribeTapeRecoveryPointsOutput":
        return dc_td.DescribeTapeRecoveryPointsOutput.make_one(res)

    def describe_tapes(
        self,
        res: "bs_td.DescribeTapesOutputTypeDef",
    ) -> "dc_td.DescribeTapesOutput":
        return dc_td.DescribeTapesOutput.make_one(res)

    def describe_upload_buffer(
        self,
        res: "bs_td.DescribeUploadBufferOutputTypeDef",
    ) -> "dc_td.DescribeUploadBufferOutput":
        return dc_td.DescribeUploadBufferOutput.make_one(res)

    def describe_vtl_devices(
        self,
        res: "bs_td.DescribeVTLDevicesOutputTypeDef",
    ) -> "dc_td.DescribeVTLDevicesOutput":
        return dc_td.DescribeVTLDevicesOutput.make_one(res)

    def describe_working_storage(
        self,
        res: "bs_td.DescribeWorkingStorageOutputTypeDef",
    ) -> "dc_td.DescribeWorkingStorageOutput":
        return dc_td.DescribeWorkingStorageOutput.make_one(res)

    def detach_volume(
        self,
        res: "bs_td.DetachVolumeOutputTypeDef",
    ) -> "dc_td.DetachVolumeOutput":
        return dc_td.DetachVolumeOutput.make_one(res)

    def disable_gateway(
        self,
        res: "bs_td.DisableGatewayOutputTypeDef",
    ) -> "dc_td.DisableGatewayOutput":
        return dc_td.DisableGatewayOutput.make_one(res)

    def disassociate_file_system(
        self,
        res: "bs_td.DisassociateFileSystemOutputTypeDef",
    ) -> "dc_td.DisassociateFileSystemOutput":
        return dc_td.DisassociateFileSystemOutput.make_one(res)

    def evict_files_failing_upload(
        self,
        res: "bs_td.EvictFilesFailingUploadOutputTypeDef",
    ) -> "dc_td.EvictFilesFailingUploadOutput":
        return dc_td.EvictFilesFailingUploadOutput.make_one(res)

    def join_domain(
        self,
        res: "bs_td.JoinDomainOutputTypeDef",
    ) -> "dc_td.JoinDomainOutput":
        return dc_td.JoinDomainOutput.make_one(res)

    def list_automatic_tape_creation_policies(
        self,
        res: "bs_td.ListAutomaticTapeCreationPoliciesOutputTypeDef",
    ) -> "dc_td.ListAutomaticTapeCreationPoliciesOutput":
        return dc_td.ListAutomaticTapeCreationPoliciesOutput.make_one(res)

    def list_cache_reports(
        self,
        res: "bs_td.ListCacheReportsOutputTypeDef",
    ) -> "dc_td.ListCacheReportsOutput":
        return dc_td.ListCacheReportsOutput.make_one(res)

    def list_file_shares(
        self,
        res: "bs_td.ListFileSharesOutputTypeDef",
    ) -> "dc_td.ListFileSharesOutput":
        return dc_td.ListFileSharesOutput.make_one(res)

    def list_file_system_associations(
        self,
        res: "bs_td.ListFileSystemAssociationsOutputTypeDef",
    ) -> "dc_td.ListFileSystemAssociationsOutput":
        return dc_td.ListFileSystemAssociationsOutput.make_one(res)

    def list_gateways(
        self,
        res: "bs_td.ListGatewaysOutputTypeDef",
    ) -> "dc_td.ListGatewaysOutput":
        return dc_td.ListGatewaysOutput.make_one(res)

    def list_local_disks(
        self,
        res: "bs_td.ListLocalDisksOutputTypeDef",
    ) -> "dc_td.ListLocalDisksOutput":
        return dc_td.ListLocalDisksOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_tape_pools(
        self,
        res: "bs_td.ListTapePoolsOutputTypeDef",
    ) -> "dc_td.ListTapePoolsOutput":
        return dc_td.ListTapePoolsOutput.make_one(res)

    def list_tapes(
        self,
        res: "bs_td.ListTapesOutputTypeDef",
    ) -> "dc_td.ListTapesOutput":
        return dc_td.ListTapesOutput.make_one(res)

    def list_volume_initiators(
        self,
        res: "bs_td.ListVolumeInitiatorsOutputTypeDef",
    ) -> "dc_td.ListVolumeInitiatorsOutput":
        return dc_td.ListVolumeInitiatorsOutput.make_one(res)

    def list_volume_recovery_points(
        self,
        res: "bs_td.ListVolumeRecoveryPointsOutputTypeDef",
    ) -> "dc_td.ListVolumeRecoveryPointsOutput":
        return dc_td.ListVolumeRecoveryPointsOutput.make_one(res)

    def list_volumes(
        self,
        res: "bs_td.ListVolumesOutputTypeDef",
    ) -> "dc_td.ListVolumesOutput":
        return dc_td.ListVolumesOutput.make_one(res)

    def notify_when_uploaded(
        self,
        res: "bs_td.NotifyWhenUploadedOutputTypeDef",
    ) -> "dc_td.NotifyWhenUploadedOutput":
        return dc_td.NotifyWhenUploadedOutput.make_one(res)

    def refresh_cache(
        self,
        res: "bs_td.RefreshCacheOutputTypeDef",
    ) -> "dc_td.RefreshCacheOutput":
        return dc_td.RefreshCacheOutput.make_one(res)

    def remove_tags_from_resource(
        self,
        res: "bs_td.RemoveTagsFromResourceOutputTypeDef",
    ) -> "dc_td.RemoveTagsFromResourceOutput":
        return dc_td.RemoveTagsFromResourceOutput.make_one(res)

    def reset_cache(
        self,
        res: "bs_td.ResetCacheOutputTypeDef",
    ) -> "dc_td.ResetCacheOutput":
        return dc_td.ResetCacheOutput.make_one(res)

    def retrieve_tape_archive(
        self,
        res: "bs_td.RetrieveTapeArchiveOutputTypeDef",
    ) -> "dc_td.RetrieveTapeArchiveOutput":
        return dc_td.RetrieveTapeArchiveOutput.make_one(res)

    def retrieve_tape_recovery_point(
        self,
        res: "bs_td.RetrieveTapeRecoveryPointOutputTypeDef",
    ) -> "dc_td.RetrieveTapeRecoveryPointOutput":
        return dc_td.RetrieveTapeRecoveryPointOutput.make_one(res)

    def set_local_console_password(
        self,
        res: "bs_td.SetLocalConsolePasswordOutputTypeDef",
    ) -> "dc_td.SetLocalConsolePasswordOutput":
        return dc_td.SetLocalConsolePasswordOutput.make_one(res)

    def set_smb_guest_password(
        self,
        res: "bs_td.SetSMBGuestPasswordOutputTypeDef",
    ) -> "dc_td.SetSMBGuestPasswordOutput":
        return dc_td.SetSMBGuestPasswordOutput.make_one(res)

    def shutdown_gateway(
        self,
        res: "bs_td.ShutdownGatewayOutputTypeDef",
    ) -> "dc_td.ShutdownGatewayOutput":
        return dc_td.ShutdownGatewayOutput.make_one(res)

    def start_availability_monitor_test(
        self,
        res: "bs_td.StartAvailabilityMonitorTestOutputTypeDef",
    ) -> "dc_td.StartAvailabilityMonitorTestOutput":
        return dc_td.StartAvailabilityMonitorTestOutput.make_one(res)

    def start_cache_report(
        self,
        res: "bs_td.StartCacheReportOutputTypeDef",
    ) -> "dc_td.StartCacheReportOutput":
        return dc_td.StartCacheReportOutput.make_one(res)

    def start_gateway(
        self,
        res: "bs_td.StartGatewayOutputTypeDef",
    ) -> "dc_td.StartGatewayOutput":
        return dc_td.StartGatewayOutput.make_one(res)

    def update_automatic_tape_creation_policy(
        self,
        res: "bs_td.UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    ) -> "dc_td.UpdateAutomaticTapeCreationPolicyOutput":
        return dc_td.UpdateAutomaticTapeCreationPolicyOutput.make_one(res)

    def update_bandwidth_rate_limit(
        self,
        res: "bs_td.UpdateBandwidthRateLimitOutputTypeDef",
    ) -> "dc_td.UpdateBandwidthRateLimitOutput":
        return dc_td.UpdateBandwidthRateLimitOutput.make_one(res)

    def update_bandwidth_rate_limit_schedule(
        self,
        res: "bs_td.UpdateBandwidthRateLimitScheduleOutputTypeDef",
    ) -> "dc_td.UpdateBandwidthRateLimitScheduleOutput":
        return dc_td.UpdateBandwidthRateLimitScheduleOutput.make_one(res)

    def update_chap_credentials(
        self,
        res: "bs_td.UpdateChapCredentialsOutputTypeDef",
    ) -> "dc_td.UpdateChapCredentialsOutput":
        return dc_td.UpdateChapCredentialsOutput.make_one(res)

    def update_file_system_association(
        self,
        res: "bs_td.UpdateFileSystemAssociationOutputTypeDef",
    ) -> "dc_td.UpdateFileSystemAssociationOutput":
        return dc_td.UpdateFileSystemAssociationOutput.make_one(res)

    def update_gateway_information(
        self,
        res: "bs_td.UpdateGatewayInformationOutputTypeDef",
    ) -> "dc_td.UpdateGatewayInformationOutput":
        return dc_td.UpdateGatewayInformationOutput.make_one(res)

    def update_gateway_software_now(
        self,
        res: "bs_td.UpdateGatewaySoftwareNowOutputTypeDef",
    ) -> "dc_td.UpdateGatewaySoftwareNowOutput":
        return dc_td.UpdateGatewaySoftwareNowOutput.make_one(res)

    def update_maintenance_start_time(
        self,
        res: "bs_td.UpdateMaintenanceStartTimeOutputTypeDef",
    ) -> "dc_td.UpdateMaintenanceStartTimeOutput":
        return dc_td.UpdateMaintenanceStartTimeOutput.make_one(res)

    def update_nfs_file_share(
        self,
        res: "bs_td.UpdateNFSFileShareOutputTypeDef",
    ) -> "dc_td.UpdateNFSFileShareOutput":
        return dc_td.UpdateNFSFileShareOutput.make_one(res)

    def update_smb_file_share(
        self,
        res: "bs_td.UpdateSMBFileShareOutputTypeDef",
    ) -> "dc_td.UpdateSMBFileShareOutput":
        return dc_td.UpdateSMBFileShareOutput.make_one(res)

    def update_smb_file_share_visibility(
        self,
        res: "bs_td.UpdateSMBFileShareVisibilityOutputTypeDef",
    ) -> "dc_td.UpdateSMBFileShareVisibilityOutput":
        return dc_td.UpdateSMBFileShareVisibilityOutput.make_one(res)

    def update_smb_local_groups(
        self,
        res: "bs_td.UpdateSMBLocalGroupsOutputTypeDef",
    ) -> "dc_td.UpdateSMBLocalGroupsOutput":
        return dc_td.UpdateSMBLocalGroupsOutput.make_one(res)

    def update_smb_security_strategy(
        self,
        res: "bs_td.UpdateSMBSecurityStrategyOutputTypeDef",
    ) -> "dc_td.UpdateSMBSecurityStrategyOutput":
        return dc_td.UpdateSMBSecurityStrategyOutput.make_one(res)

    def update_snapshot_schedule(
        self,
        res: "bs_td.UpdateSnapshotScheduleOutputTypeDef",
    ) -> "dc_td.UpdateSnapshotScheduleOutput":
        return dc_td.UpdateSnapshotScheduleOutput.make_one(res)

    def update_vtl_device_type(
        self,
        res: "bs_td.UpdateVTLDeviceTypeOutputTypeDef",
    ) -> "dc_td.UpdateVTLDeviceTypeOutput":
        return dc_td.UpdateVTLDeviceTypeOutput.make_one(res)


storagegateway_caster = STORAGEGATEWAYCaster()
