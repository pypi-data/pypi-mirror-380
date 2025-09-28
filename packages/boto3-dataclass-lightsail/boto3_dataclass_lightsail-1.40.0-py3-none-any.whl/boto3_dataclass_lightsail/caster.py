# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lightsail import type_defs as bs_td


class LIGHTSAILCaster:

    def allocate_static_ip(
        self,
        res: "bs_td.AllocateStaticIpResultTypeDef",
    ) -> "dc_td.AllocateStaticIpResult":
        return dc_td.AllocateStaticIpResult.make_one(res)

    def attach_certificate_to_distribution(
        self,
        res: "bs_td.AttachCertificateToDistributionResultTypeDef",
    ) -> "dc_td.AttachCertificateToDistributionResult":
        return dc_td.AttachCertificateToDistributionResult.make_one(res)

    def attach_disk(
        self,
        res: "bs_td.AttachDiskResultTypeDef",
    ) -> "dc_td.AttachDiskResult":
        return dc_td.AttachDiskResult.make_one(res)

    def attach_instances_to_load_balancer(
        self,
        res: "bs_td.AttachInstancesToLoadBalancerResultTypeDef",
    ) -> "dc_td.AttachInstancesToLoadBalancerResult":
        return dc_td.AttachInstancesToLoadBalancerResult.make_one(res)

    def attach_load_balancer_tls_certificate(
        self,
        res: "bs_td.AttachLoadBalancerTlsCertificateResultTypeDef",
    ) -> "dc_td.AttachLoadBalancerTlsCertificateResult":
        return dc_td.AttachLoadBalancerTlsCertificateResult.make_one(res)

    def attach_static_ip(
        self,
        res: "bs_td.AttachStaticIpResultTypeDef",
    ) -> "dc_td.AttachStaticIpResult":
        return dc_td.AttachStaticIpResult.make_one(res)

    def close_instance_public_ports(
        self,
        res: "bs_td.CloseInstancePublicPortsResultTypeDef",
    ) -> "dc_td.CloseInstancePublicPortsResult":
        return dc_td.CloseInstancePublicPortsResult.make_one(res)

    def copy_snapshot(
        self,
        res: "bs_td.CopySnapshotResultTypeDef",
    ) -> "dc_td.CopySnapshotResult":
        return dc_td.CopySnapshotResult.make_one(res)

    def create_bucket(
        self,
        res: "bs_td.CreateBucketResultTypeDef",
    ) -> "dc_td.CreateBucketResult":
        return dc_td.CreateBucketResult.make_one(res)

    def create_bucket_access_key(
        self,
        res: "bs_td.CreateBucketAccessKeyResultTypeDef",
    ) -> "dc_td.CreateBucketAccessKeyResult":
        return dc_td.CreateBucketAccessKeyResult.make_one(res)

    def create_certificate(
        self,
        res: "bs_td.CreateCertificateResultTypeDef",
    ) -> "dc_td.CreateCertificateResult":
        return dc_td.CreateCertificateResult.make_one(res)

    def create_cloud_formation_stack(
        self,
        res: "bs_td.CreateCloudFormationStackResultTypeDef",
    ) -> "dc_td.CreateCloudFormationStackResult":
        return dc_td.CreateCloudFormationStackResult.make_one(res)

    def create_contact_method(
        self,
        res: "bs_td.CreateContactMethodResultTypeDef",
    ) -> "dc_td.CreateContactMethodResult":
        return dc_td.CreateContactMethodResult.make_one(res)

    def create_container_service(
        self,
        res: "bs_td.CreateContainerServiceResultTypeDef",
    ) -> "dc_td.CreateContainerServiceResult":
        return dc_td.CreateContainerServiceResult.make_one(res)

    def create_container_service_deployment(
        self,
        res: "bs_td.CreateContainerServiceDeploymentResultTypeDef",
    ) -> "dc_td.CreateContainerServiceDeploymentResult":
        return dc_td.CreateContainerServiceDeploymentResult.make_one(res)

    def create_container_service_registry_login(
        self,
        res: "bs_td.CreateContainerServiceRegistryLoginResultTypeDef",
    ) -> "dc_td.CreateContainerServiceRegistryLoginResult":
        return dc_td.CreateContainerServiceRegistryLoginResult.make_one(res)

    def create_disk(
        self,
        res: "bs_td.CreateDiskResultTypeDef",
    ) -> "dc_td.CreateDiskResult":
        return dc_td.CreateDiskResult.make_one(res)

    def create_disk_from_snapshot(
        self,
        res: "bs_td.CreateDiskFromSnapshotResultTypeDef",
    ) -> "dc_td.CreateDiskFromSnapshotResult":
        return dc_td.CreateDiskFromSnapshotResult.make_one(res)

    def create_disk_snapshot(
        self,
        res: "bs_td.CreateDiskSnapshotResultTypeDef",
    ) -> "dc_td.CreateDiskSnapshotResult":
        return dc_td.CreateDiskSnapshotResult.make_one(res)

    def create_distribution(
        self,
        res: "bs_td.CreateDistributionResultTypeDef",
    ) -> "dc_td.CreateDistributionResult":
        return dc_td.CreateDistributionResult.make_one(res)

    def create_domain(
        self,
        res: "bs_td.CreateDomainResultTypeDef",
    ) -> "dc_td.CreateDomainResult":
        return dc_td.CreateDomainResult.make_one(res)

    def create_domain_entry(
        self,
        res: "bs_td.CreateDomainEntryResultTypeDef",
    ) -> "dc_td.CreateDomainEntryResult":
        return dc_td.CreateDomainEntryResult.make_one(res)

    def create_gui_session_access_details(
        self,
        res: "bs_td.CreateGUISessionAccessDetailsResultTypeDef",
    ) -> "dc_td.CreateGUISessionAccessDetailsResult":
        return dc_td.CreateGUISessionAccessDetailsResult.make_one(res)

    def create_instance_snapshot(
        self,
        res: "bs_td.CreateInstanceSnapshotResultTypeDef",
    ) -> "dc_td.CreateInstanceSnapshotResult":
        return dc_td.CreateInstanceSnapshotResult.make_one(res)

    def create_instances(
        self,
        res: "bs_td.CreateInstancesResultTypeDef",
    ) -> "dc_td.CreateInstancesResult":
        return dc_td.CreateInstancesResult.make_one(res)

    def create_instances_from_snapshot(
        self,
        res: "bs_td.CreateInstancesFromSnapshotResultTypeDef",
    ) -> "dc_td.CreateInstancesFromSnapshotResult":
        return dc_td.CreateInstancesFromSnapshotResult.make_one(res)

    def create_key_pair(
        self,
        res: "bs_td.CreateKeyPairResultTypeDef",
    ) -> "dc_td.CreateKeyPairResult":
        return dc_td.CreateKeyPairResult.make_one(res)

    def create_load_balancer(
        self,
        res: "bs_td.CreateLoadBalancerResultTypeDef",
    ) -> "dc_td.CreateLoadBalancerResult":
        return dc_td.CreateLoadBalancerResult.make_one(res)

    def create_load_balancer_tls_certificate(
        self,
        res: "bs_td.CreateLoadBalancerTlsCertificateResultTypeDef",
    ) -> "dc_td.CreateLoadBalancerTlsCertificateResult":
        return dc_td.CreateLoadBalancerTlsCertificateResult.make_one(res)

    def create_relational_database(
        self,
        res: "bs_td.CreateRelationalDatabaseResultTypeDef",
    ) -> "dc_td.CreateRelationalDatabaseResult":
        return dc_td.CreateRelationalDatabaseResult.make_one(res)

    def create_relational_database_from_snapshot(
        self,
        res: "bs_td.CreateRelationalDatabaseFromSnapshotResultTypeDef",
    ) -> "dc_td.CreateRelationalDatabaseFromSnapshotResult":
        return dc_td.CreateRelationalDatabaseFromSnapshotResult.make_one(res)

    def create_relational_database_snapshot(
        self,
        res: "bs_td.CreateRelationalDatabaseSnapshotResultTypeDef",
    ) -> "dc_td.CreateRelationalDatabaseSnapshotResult":
        return dc_td.CreateRelationalDatabaseSnapshotResult.make_one(res)

    def delete_alarm(
        self,
        res: "bs_td.DeleteAlarmResultTypeDef",
    ) -> "dc_td.DeleteAlarmResult":
        return dc_td.DeleteAlarmResult.make_one(res)

    def delete_auto_snapshot(
        self,
        res: "bs_td.DeleteAutoSnapshotResultTypeDef",
    ) -> "dc_td.DeleteAutoSnapshotResult":
        return dc_td.DeleteAutoSnapshotResult.make_one(res)

    def delete_bucket(
        self,
        res: "bs_td.DeleteBucketResultTypeDef",
    ) -> "dc_td.DeleteBucketResult":
        return dc_td.DeleteBucketResult.make_one(res)

    def delete_bucket_access_key(
        self,
        res: "bs_td.DeleteBucketAccessKeyResultTypeDef",
    ) -> "dc_td.DeleteBucketAccessKeyResult":
        return dc_td.DeleteBucketAccessKeyResult.make_one(res)

    def delete_certificate(
        self,
        res: "bs_td.DeleteCertificateResultTypeDef",
    ) -> "dc_td.DeleteCertificateResult":
        return dc_td.DeleteCertificateResult.make_one(res)

    def delete_contact_method(
        self,
        res: "bs_td.DeleteContactMethodResultTypeDef",
    ) -> "dc_td.DeleteContactMethodResult":
        return dc_td.DeleteContactMethodResult.make_one(res)

    def delete_disk(
        self,
        res: "bs_td.DeleteDiskResultTypeDef",
    ) -> "dc_td.DeleteDiskResult":
        return dc_td.DeleteDiskResult.make_one(res)

    def delete_disk_snapshot(
        self,
        res: "bs_td.DeleteDiskSnapshotResultTypeDef",
    ) -> "dc_td.DeleteDiskSnapshotResult":
        return dc_td.DeleteDiskSnapshotResult.make_one(res)

    def delete_distribution(
        self,
        res: "bs_td.DeleteDistributionResultTypeDef",
    ) -> "dc_td.DeleteDistributionResult":
        return dc_td.DeleteDistributionResult.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.DeleteDomainResultTypeDef",
    ) -> "dc_td.DeleteDomainResult":
        return dc_td.DeleteDomainResult.make_one(res)

    def delete_domain_entry(
        self,
        res: "bs_td.DeleteDomainEntryResultTypeDef",
    ) -> "dc_td.DeleteDomainEntryResult":
        return dc_td.DeleteDomainEntryResult.make_one(res)

    def delete_instance(
        self,
        res: "bs_td.DeleteInstanceResultTypeDef",
    ) -> "dc_td.DeleteInstanceResult":
        return dc_td.DeleteInstanceResult.make_one(res)

    def delete_instance_snapshot(
        self,
        res: "bs_td.DeleteInstanceSnapshotResultTypeDef",
    ) -> "dc_td.DeleteInstanceSnapshotResult":
        return dc_td.DeleteInstanceSnapshotResult.make_one(res)

    def delete_key_pair(
        self,
        res: "bs_td.DeleteKeyPairResultTypeDef",
    ) -> "dc_td.DeleteKeyPairResult":
        return dc_td.DeleteKeyPairResult.make_one(res)

    def delete_known_host_keys(
        self,
        res: "bs_td.DeleteKnownHostKeysResultTypeDef",
    ) -> "dc_td.DeleteKnownHostKeysResult":
        return dc_td.DeleteKnownHostKeysResult.make_one(res)

    def delete_load_balancer(
        self,
        res: "bs_td.DeleteLoadBalancerResultTypeDef",
    ) -> "dc_td.DeleteLoadBalancerResult":
        return dc_td.DeleteLoadBalancerResult.make_one(res)

    def delete_load_balancer_tls_certificate(
        self,
        res: "bs_td.DeleteLoadBalancerTlsCertificateResultTypeDef",
    ) -> "dc_td.DeleteLoadBalancerTlsCertificateResult":
        return dc_td.DeleteLoadBalancerTlsCertificateResult.make_one(res)

    def delete_relational_database(
        self,
        res: "bs_td.DeleteRelationalDatabaseResultTypeDef",
    ) -> "dc_td.DeleteRelationalDatabaseResult":
        return dc_td.DeleteRelationalDatabaseResult.make_one(res)

    def delete_relational_database_snapshot(
        self,
        res: "bs_td.DeleteRelationalDatabaseSnapshotResultTypeDef",
    ) -> "dc_td.DeleteRelationalDatabaseSnapshotResult":
        return dc_td.DeleteRelationalDatabaseSnapshotResult.make_one(res)

    def detach_certificate_from_distribution(
        self,
        res: "bs_td.DetachCertificateFromDistributionResultTypeDef",
    ) -> "dc_td.DetachCertificateFromDistributionResult":
        return dc_td.DetachCertificateFromDistributionResult.make_one(res)

    def detach_disk(
        self,
        res: "bs_td.DetachDiskResultTypeDef",
    ) -> "dc_td.DetachDiskResult":
        return dc_td.DetachDiskResult.make_one(res)

    def detach_instances_from_load_balancer(
        self,
        res: "bs_td.DetachInstancesFromLoadBalancerResultTypeDef",
    ) -> "dc_td.DetachInstancesFromLoadBalancerResult":
        return dc_td.DetachInstancesFromLoadBalancerResult.make_one(res)

    def detach_static_ip(
        self,
        res: "bs_td.DetachStaticIpResultTypeDef",
    ) -> "dc_td.DetachStaticIpResult":
        return dc_td.DetachStaticIpResult.make_one(res)

    def disable_add_on(
        self,
        res: "bs_td.DisableAddOnResultTypeDef",
    ) -> "dc_td.DisableAddOnResult":
        return dc_td.DisableAddOnResult.make_one(res)

    def download_default_key_pair(
        self,
        res: "bs_td.DownloadDefaultKeyPairResultTypeDef",
    ) -> "dc_td.DownloadDefaultKeyPairResult":
        return dc_td.DownloadDefaultKeyPairResult.make_one(res)

    def enable_add_on(
        self,
        res: "bs_td.EnableAddOnResultTypeDef",
    ) -> "dc_td.EnableAddOnResult":
        return dc_td.EnableAddOnResult.make_one(res)

    def export_snapshot(
        self,
        res: "bs_td.ExportSnapshotResultTypeDef",
    ) -> "dc_td.ExportSnapshotResult":
        return dc_td.ExportSnapshotResult.make_one(res)

    def get_active_names(
        self,
        res: "bs_td.GetActiveNamesResultTypeDef",
    ) -> "dc_td.GetActiveNamesResult":
        return dc_td.GetActiveNamesResult.make_one(res)

    def get_alarms(
        self,
        res: "bs_td.GetAlarmsResultTypeDef",
    ) -> "dc_td.GetAlarmsResult":
        return dc_td.GetAlarmsResult.make_one(res)

    def get_auto_snapshots(
        self,
        res: "bs_td.GetAutoSnapshotsResultTypeDef",
    ) -> "dc_td.GetAutoSnapshotsResult":
        return dc_td.GetAutoSnapshotsResult.make_one(res)

    def get_blueprints(
        self,
        res: "bs_td.GetBlueprintsResultTypeDef",
    ) -> "dc_td.GetBlueprintsResult":
        return dc_td.GetBlueprintsResult.make_one(res)

    def get_bucket_access_keys(
        self,
        res: "bs_td.GetBucketAccessKeysResultTypeDef",
    ) -> "dc_td.GetBucketAccessKeysResult":
        return dc_td.GetBucketAccessKeysResult.make_one(res)

    def get_bucket_bundles(
        self,
        res: "bs_td.GetBucketBundlesResultTypeDef",
    ) -> "dc_td.GetBucketBundlesResult":
        return dc_td.GetBucketBundlesResult.make_one(res)

    def get_bucket_metric_data(
        self,
        res: "bs_td.GetBucketMetricDataResultTypeDef",
    ) -> "dc_td.GetBucketMetricDataResult":
        return dc_td.GetBucketMetricDataResult.make_one(res)

    def get_buckets(
        self,
        res: "bs_td.GetBucketsResultTypeDef",
    ) -> "dc_td.GetBucketsResult":
        return dc_td.GetBucketsResult.make_one(res)

    def get_bundles(
        self,
        res: "bs_td.GetBundlesResultTypeDef",
    ) -> "dc_td.GetBundlesResult":
        return dc_td.GetBundlesResult.make_one(res)

    def get_certificates(
        self,
        res: "bs_td.GetCertificatesResultTypeDef",
    ) -> "dc_td.GetCertificatesResult":
        return dc_td.GetCertificatesResult.make_one(res)

    def get_cloud_formation_stack_records(
        self,
        res: "bs_td.GetCloudFormationStackRecordsResultTypeDef",
    ) -> "dc_td.GetCloudFormationStackRecordsResult":
        return dc_td.GetCloudFormationStackRecordsResult.make_one(res)

    def get_contact_methods(
        self,
        res: "bs_td.GetContactMethodsResultTypeDef",
    ) -> "dc_td.GetContactMethodsResult":
        return dc_td.GetContactMethodsResult.make_one(res)

    def get_container_api_metadata(
        self,
        res: "bs_td.GetContainerAPIMetadataResultTypeDef",
    ) -> "dc_td.GetContainerAPIMetadataResult":
        return dc_td.GetContainerAPIMetadataResult.make_one(res)

    def get_container_images(
        self,
        res: "bs_td.GetContainerImagesResultTypeDef",
    ) -> "dc_td.GetContainerImagesResult":
        return dc_td.GetContainerImagesResult.make_one(res)

    def get_container_log(
        self,
        res: "bs_td.GetContainerLogResultTypeDef",
    ) -> "dc_td.GetContainerLogResult":
        return dc_td.GetContainerLogResult.make_one(res)

    def get_container_service_deployments(
        self,
        res: "bs_td.GetContainerServiceDeploymentsResultTypeDef",
    ) -> "dc_td.GetContainerServiceDeploymentsResult":
        return dc_td.GetContainerServiceDeploymentsResult.make_one(res)

    def get_container_service_metric_data(
        self,
        res: "bs_td.GetContainerServiceMetricDataResultTypeDef",
    ) -> "dc_td.GetContainerServiceMetricDataResult":
        return dc_td.GetContainerServiceMetricDataResult.make_one(res)

    def get_container_service_powers(
        self,
        res: "bs_td.GetContainerServicePowersResultTypeDef",
    ) -> "dc_td.GetContainerServicePowersResult":
        return dc_td.GetContainerServicePowersResult.make_one(res)

    def get_container_services(
        self,
        res: "bs_td.ContainerServicesListResultTypeDef",
    ) -> "dc_td.ContainerServicesListResult":
        return dc_td.ContainerServicesListResult.make_one(res)

    def get_cost_estimate(
        self,
        res: "bs_td.GetCostEstimateResultTypeDef",
    ) -> "dc_td.GetCostEstimateResult":
        return dc_td.GetCostEstimateResult.make_one(res)

    def get_disk(
        self,
        res: "bs_td.GetDiskResultTypeDef",
    ) -> "dc_td.GetDiskResult":
        return dc_td.GetDiskResult.make_one(res)

    def get_disk_snapshot(
        self,
        res: "bs_td.GetDiskSnapshotResultTypeDef",
    ) -> "dc_td.GetDiskSnapshotResult":
        return dc_td.GetDiskSnapshotResult.make_one(res)

    def get_disk_snapshots(
        self,
        res: "bs_td.GetDiskSnapshotsResultTypeDef",
    ) -> "dc_td.GetDiskSnapshotsResult":
        return dc_td.GetDiskSnapshotsResult.make_one(res)

    def get_disks(
        self,
        res: "bs_td.GetDisksResultTypeDef",
    ) -> "dc_td.GetDisksResult":
        return dc_td.GetDisksResult.make_one(res)

    def get_distribution_bundles(
        self,
        res: "bs_td.GetDistributionBundlesResultTypeDef",
    ) -> "dc_td.GetDistributionBundlesResult":
        return dc_td.GetDistributionBundlesResult.make_one(res)

    def get_distribution_latest_cache_reset(
        self,
        res: "bs_td.GetDistributionLatestCacheResetResultTypeDef",
    ) -> "dc_td.GetDistributionLatestCacheResetResult":
        return dc_td.GetDistributionLatestCacheResetResult.make_one(res)

    def get_distribution_metric_data(
        self,
        res: "bs_td.GetDistributionMetricDataResultTypeDef",
    ) -> "dc_td.GetDistributionMetricDataResult":
        return dc_td.GetDistributionMetricDataResult.make_one(res)

    def get_distributions(
        self,
        res: "bs_td.GetDistributionsResultTypeDef",
    ) -> "dc_td.GetDistributionsResult":
        return dc_td.GetDistributionsResult.make_one(res)

    def get_domain(
        self,
        res: "bs_td.GetDomainResultTypeDef",
    ) -> "dc_td.GetDomainResult":
        return dc_td.GetDomainResult.make_one(res)

    def get_domains(
        self,
        res: "bs_td.GetDomainsResultTypeDef",
    ) -> "dc_td.GetDomainsResult":
        return dc_td.GetDomainsResult.make_one(res)

    def get_export_snapshot_records(
        self,
        res: "bs_td.GetExportSnapshotRecordsResultTypeDef",
    ) -> "dc_td.GetExportSnapshotRecordsResult":
        return dc_td.GetExportSnapshotRecordsResult.make_one(res)

    def get_instance(
        self,
        res: "bs_td.GetInstanceResultTypeDef",
    ) -> "dc_td.GetInstanceResult":
        return dc_td.GetInstanceResult.make_one(res)

    def get_instance_access_details(
        self,
        res: "bs_td.GetInstanceAccessDetailsResultTypeDef",
    ) -> "dc_td.GetInstanceAccessDetailsResult":
        return dc_td.GetInstanceAccessDetailsResult.make_one(res)

    def get_instance_metric_data(
        self,
        res: "bs_td.GetInstanceMetricDataResultTypeDef",
    ) -> "dc_td.GetInstanceMetricDataResult":
        return dc_td.GetInstanceMetricDataResult.make_one(res)

    def get_instance_port_states(
        self,
        res: "bs_td.GetInstancePortStatesResultTypeDef",
    ) -> "dc_td.GetInstancePortStatesResult":
        return dc_td.GetInstancePortStatesResult.make_one(res)

    def get_instance_snapshot(
        self,
        res: "bs_td.GetInstanceSnapshotResultTypeDef",
    ) -> "dc_td.GetInstanceSnapshotResult":
        return dc_td.GetInstanceSnapshotResult.make_one(res)

    def get_instance_snapshots(
        self,
        res: "bs_td.GetInstanceSnapshotsResultTypeDef",
    ) -> "dc_td.GetInstanceSnapshotsResult":
        return dc_td.GetInstanceSnapshotsResult.make_one(res)

    def get_instance_state(
        self,
        res: "bs_td.GetInstanceStateResultTypeDef",
    ) -> "dc_td.GetInstanceStateResult":
        return dc_td.GetInstanceStateResult.make_one(res)

    def get_instances(
        self,
        res: "bs_td.GetInstancesResultTypeDef",
    ) -> "dc_td.GetInstancesResult":
        return dc_td.GetInstancesResult.make_one(res)

    def get_key_pair(
        self,
        res: "bs_td.GetKeyPairResultTypeDef",
    ) -> "dc_td.GetKeyPairResult":
        return dc_td.GetKeyPairResult.make_one(res)

    def get_key_pairs(
        self,
        res: "bs_td.GetKeyPairsResultTypeDef",
    ) -> "dc_td.GetKeyPairsResult":
        return dc_td.GetKeyPairsResult.make_one(res)

    def get_load_balancer(
        self,
        res: "bs_td.GetLoadBalancerResultTypeDef",
    ) -> "dc_td.GetLoadBalancerResult":
        return dc_td.GetLoadBalancerResult.make_one(res)

    def get_load_balancer_metric_data(
        self,
        res: "bs_td.GetLoadBalancerMetricDataResultTypeDef",
    ) -> "dc_td.GetLoadBalancerMetricDataResult":
        return dc_td.GetLoadBalancerMetricDataResult.make_one(res)

    def get_load_balancer_tls_certificates(
        self,
        res: "bs_td.GetLoadBalancerTlsCertificatesResultTypeDef",
    ) -> "dc_td.GetLoadBalancerTlsCertificatesResult":
        return dc_td.GetLoadBalancerTlsCertificatesResult.make_one(res)

    def get_load_balancer_tls_policies(
        self,
        res: "bs_td.GetLoadBalancerTlsPoliciesResultTypeDef",
    ) -> "dc_td.GetLoadBalancerTlsPoliciesResult":
        return dc_td.GetLoadBalancerTlsPoliciesResult.make_one(res)

    def get_load_balancers(
        self,
        res: "bs_td.GetLoadBalancersResultTypeDef",
    ) -> "dc_td.GetLoadBalancersResult":
        return dc_td.GetLoadBalancersResult.make_one(res)

    def get_operation(
        self,
        res: "bs_td.GetOperationResultTypeDef",
    ) -> "dc_td.GetOperationResult":
        return dc_td.GetOperationResult.make_one(res)

    def get_operations(
        self,
        res: "bs_td.GetOperationsResultTypeDef",
    ) -> "dc_td.GetOperationsResult":
        return dc_td.GetOperationsResult.make_one(res)

    def get_operations_for_resource(
        self,
        res: "bs_td.GetOperationsForResourceResultTypeDef",
    ) -> "dc_td.GetOperationsForResourceResult":
        return dc_td.GetOperationsForResourceResult.make_one(res)

    def get_regions(
        self,
        res: "bs_td.GetRegionsResultTypeDef",
    ) -> "dc_td.GetRegionsResult":
        return dc_td.GetRegionsResult.make_one(res)

    def get_relational_database(
        self,
        res: "bs_td.GetRelationalDatabaseResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseResult":
        return dc_td.GetRelationalDatabaseResult.make_one(res)

    def get_relational_database_blueprints(
        self,
        res: "bs_td.GetRelationalDatabaseBlueprintsResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseBlueprintsResult":
        return dc_td.GetRelationalDatabaseBlueprintsResult.make_one(res)

    def get_relational_database_bundles(
        self,
        res: "bs_td.GetRelationalDatabaseBundlesResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseBundlesResult":
        return dc_td.GetRelationalDatabaseBundlesResult.make_one(res)

    def get_relational_database_events(
        self,
        res: "bs_td.GetRelationalDatabaseEventsResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseEventsResult":
        return dc_td.GetRelationalDatabaseEventsResult.make_one(res)

    def get_relational_database_log_events(
        self,
        res: "bs_td.GetRelationalDatabaseLogEventsResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseLogEventsResult":
        return dc_td.GetRelationalDatabaseLogEventsResult.make_one(res)

    def get_relational_database_log_streams(
        self,
        res: "bs_td.GetRelationalDatabaseLogStreamsResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseLogStreamsResult":
        return dc_td.GetRelationalDatabaseLogStreamsResult.make_one(res)

    def get_relational_database_master_user_password(
        self,
        res: "bs_td.GetRelationalDatabaseMasterUserPasswordResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseMasterUserPasswordResult":
        return dc_td.GetRelationalDatabaseMasterUserPasswordResult.make_one(res)

    def get_relational_database_metric_data(
        self,
        res: "bs_td.GetRelationalDatabaseMetricDataResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseMetricDataResult":
        return dc_td.GetRelationalDatabaseMetricDataResult.make_one(res)

    def get_relational_database_parameters(
        self,
        res: "bs_td.GetRelationalDatabaseParametersResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseParametersResult":
        return dc_td.GetRelationalDatabaseParametersResult.make_one(res)

    def get_relational_database_snapshot(
        self,
        res: "bs_td.GetRelationalDatabaseSnapshotResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseSnapshotResult":
        return dc_td.GetRelationalDatabaseSnapshotResult.make_one(res)

    def get_relational_database_snapshots(
        self,
        res: "bs_td.GetRelationalDatabaseSnapshotsResultTypeDef",
    ) -> "dc_td.GetRelationalDatabaseSnapshotsResult":
        return dc_td.GetRelationalDatabaseSnapshotsResult.make_one(res)

    def get_relational_databases(
        self,
        res: "bs_td.GetRelationalDatabasesResultTypeDef",
    ) -> "dc_td.GetRelationalDatabasesResult":
        return dc_td.GetRelationalDatabasesResult.make_one(res)

    def get_setup_history(
        self,
        res: "bs_td.GetSetupHistoryResultTypeDef",
    ) -> "dc_td.GetSetupHistoryResult":
        return dc_td.GetSetupHistoryResult.make_one(res)

    def get_static_ip(
        self,
        res: "bs_td.GetStaticIpResultTypeDef",
    ) -> "dc_td.GetStaticIpResult":
        return dc_td.GetStaticIpResult.make_one(res)

    def get_static_ips(
        self,
        res: "bs_td.GetStaticIpsResultTypeDef",
    ) -> "dc_td.GetStaticIpsResult":
        return dc_td.GetStaticIpsResult.make_one(res)

    def import_key_pair(
        self,
        res: "bs_td.ImportKeyPairResultTypeDef",
    ) -> "dc_td.ImportKeyPairResult":
        return dc_td.ImportKeyPairResult.make_one(res)

    def is_vpc_peered(
        self,
        res: "bs_td.IsVpcPeeredResultTypeDef",
    ) -> "dc_td.IsVpcPeeredResult":
        return dc_td.IsVpcPeeredResult.make_one(res)

    def open_instance_public_ports(
        self,
        res: "bs_td.OpenInstancePublicPortsResultTypeDef",
    ) -> "dc_td.OpenInstancePublicPortsResult":
        return dc_td.OpenInstancePublicPortsResult.make_one(res)

    def peer_vpc(
        self,
        res: "bs_td.PeerVpcResultTypeDef",
    ) -> "dc_td.PeerVpcResult":
        return dc_td.PeerVpcResult.make_one(res)

    def put_alarm(
        self,
        res: "bs_td.PutAlarmResultTypeDef",
    ) -> "dc_td.PutAlarmResult":
        return dc_td.PutAlarmResult.make_one(res)

    def put_instance_public_ports(
        self,
        res: "bs_td.PutInstancePublicPortsResultTypeDef",
    ) -> "dc_td.PutInstancePublicPortsResult":
        return dc_td.PutInstancePublicPortsResult.make_one(res)

    def reboot_instance(
        self,
        res: "bs_td.RebootInstanceResultTypeDef",
    ) -> "dc_td.RebootInstanceResult":
        return dc_td.RebootInstanceResult.make_one(res)

    def reboot_relational_database(
        self,
        res: "bs_td.RebootRelationalDatabaseResultTypeDef",
    ) -> "dc_td.RebootRelationalDatabaseResult":
        return dc_td.RebootRelationalDatabaseResult.make_one(res)

    def register_container_image(
        self,
        res: "bs_td.RegisterContainerImageResultTypeDef",
    ) -> "dc_td.RegisterContainerImageResult":
        return dc_td.RegisterContainerImageResult.make_one(res)

    def release_static_ip(
        self,
        res: "bs_td.ReleaseStaticIpResultTypeDef",
    ) -> "dc_td.ReleaseStaticIpResult":
        return dc_td.ReleaseStaticIpResult.make_one(res)

    def reset_distribution_cache(
        self,
        res: "bs_td.ResetDistributionCacheResultTypeDef",
    ) -> "dc_td.ResetDistributionCacheResult":
        return dc_td.ResetDistributionCacheResult.make_one(res)

    def send_contact_method_verification(
        self,
        res: "bs_td.SendContactMethodVerificationResultTypeDef",
    ) -> "dc_td.SendContactMethodVerificationResult":
        return dc_td.SendContactMethodVerificationResult.make_one(res)

    def set_ip_address_type(
        self,
        res: "bs_td.SetIpAddressTypeResultTypeDef",
    ) -> "dc_td.SetIpAddressTypeResult":
        return dc_td.SetIpAddressTypeResult.make_one(res)

    def set_resource_access_for_bucket(
        self,
        res: "bs_td.SetResourceAccessForBucketResultTypeDef",
    ) -> "dc_td.SetResourceAccessForBucketResult":
        return dc_td.SetResourceAccessForBucketResult.make_one(res)

    def setup_instance_https(
        self,
        res: "bs_td.SetupInstanceHttpsResultTypeDef",
    ) -> "dc_td.SetupInstanceHttpsResult":
        return dc_td.SetupInstanceHttpsResult.make_one(res)

    def start_gui_session(
        self,
        res: "bs_td.StartGUISessionResultTypeDef",
    ) -> "dc_td.StartGUISessionResult":
        return dc_td.StartGUISessionResult.make_one(res)

    def start_instance(
        self,
        res: "bs_td.StartInstanceResultTypeDef",
    ) -> "dc_td.StartInstanceResult":
        return dc_td.StartInstanceResult.make_one(res)

    def start_relational_database(
        self,
        res: "bs_td.StartRelationalDatabaseResultTypeDef",
    ) -> "dc_td.StartRelationalDatabaseResult":
        return dc_td.StartRelationalDatabaseResult.make_one(res)

    def stop_gui_session(
        self,
        res: "bs_td.StopGUISessionResultTypeDef",
    ) -> "dc_td.StopGUISessionResult":
        return dc_td.StopGUISessionResult.make_one(res)

    def stop_instance(
        self,
        res: "bs_td.StopInstanceResultTypeDef",
    ) -> "dc_td.StopInstanceResult":
        return dc_td.StopInstanceResult.make_one(res)

    def stop_relational_database(
        self,
        res: "bs_td.StopRelationalDatabaseResultTypeDef",
    ) -> "dc_td.StopRelationalDatabaseResult":
        return dc_td.StopRelationalDatabaseResult.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.TagResourceResultTypeDef",
    ) -> "dc_td.TagResourceResult":
        return dc_td.TagResourceResult.make_one(res)

    def test_alarm(
        self,
        res: "bs_td.TestAlarmResultTypeDef",
    ) -> "dc_td.TestAlarmResult":
        return dc_td.TestAlarmResult.make_one(res)

    def unpeer_vpc(
        self,
        res: "bs_td.UnpeerVpcResultTypeDef",
    ) -> "dc_td.UnpeerVpcResult":
        return dc_td.UnpeerVpcResult.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.UntagResourceResultTypeDef",
    ) -> "dc_td.UntagResourceResult":
        return dc_td.UntagResourceResult.make_one(res)

    def update_bucket(
        self,
        res: "bs_td.UpdateBucketResultTypeDef",
    ) -> "dc_td.UpdateBucketResult":
        return dc_td.UpdateBucketResult.make_one(res)

    def update_bucket_bundle(
        self,
        res: "bs_td.UpdateBucketBundleResultTypeDef",
    ) -> "dc_td.UpdateBucketBundleResult":
        return dc_td.UpdateBucketBundleResult.make_one(res)

    def update_container_service(
        self,
        res: "bs_td.UpdateContainerServiceResultTypeDef",
    ) -> "dc_td.UpdateContainerServiceResult":
        return dc_td.UpdateContainerServiceResult.make_one(res)

    def update_distribution(
        self,
        res: "bs_td.UpdateDistributionResultTypeDef",
    ) -> "dc_td.UpdateDistributionResult":
        return dc_td.UpdateDistributionResult.make_one(res)

    def update_distribution_bundle(
        self,
        res: "bs_td.UpdateDistributionBundleResultTypeDef",
    ) -> "dc_td.UpdateDistributionBundleResult":
        return dc_td.UpdateDistributionBundleResult.make_one(res)

    def update_domain_entry(
        self,
        res: "bs_td.UpdateDomainEntryResultTypeDef",
    ) -> "dc_td.UpdateDomainEntryResult":
        return dc_td.UpdateDomainEntryResult.make_one(res)

    def update_instance_metadata_options(
        self,
        res: "bs_td.UpdateInstanceMetadataOptionsResultTypeDef",
    ) -> "dc_td.UpdateInstanceMetadataOptionsResult":
        return dc_td.UpdateInstanceMetadataOptionsResult.make_one(res)

    def update_load_balancer_attribute(
        self,
        res: "bs_td.UpdateLoadBalancerAttributeResultTypeDef",
    ) -> "dc_td.UpdateLoadBalancerAttributeResult":
        return dc_td.UpdateLoadBalancerAttributeResult.make_one(res)

    def update_relational_database(
        self,
        res: "bs_td.UpdateRelationalDatabaseResultTypeDef",
    ) -> "dc_td.UpdateRelationalDatabaseResult":
        return dc_td.UpdateRelationalDatabaseResult.make_one(res)

    def update_relational_database_parameters(
        self,
        res: "bs_td.UpdateRelationalDatabaseParametersResultTypeDef",
    ) -> "dc_td.UpdateRelationalDatabaseParametersResult":
        return dc_td.UpdateRelationalDatabaseParametersResult.make_one(res)


lightsail_caster = LIGHTSAILCaster()
