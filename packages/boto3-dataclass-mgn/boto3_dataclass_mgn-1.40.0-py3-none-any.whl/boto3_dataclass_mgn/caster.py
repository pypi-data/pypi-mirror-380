# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mgn import type_defs as bs_td


class MGNCaster:

    def archive_application(
        self,
        res: "bs_td.ApplicationResponseTypeDef",
    ) -> "dc_td.ApplicationResponse":
        return dc_td.ApplicationResponse.make_one(res)

    def archive_wave(
        self,
        res: "bs_td.WaveResponseTypeDef",
    ) -> "dc_td.WaveResponse":
        return dc_td.WaveResponse.make_one(res)

    def change_server_life_cycle_state(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def create_application(
        self,
        res: "bs_td.ApplicationResponseTypeDef",
    ) -> "dc_td.ApplicationResponse":
        return dc_td.ApplicationResponse.make_one(res)

    def create_connector(
        self,
        res: "bs_td.ConnectorResponseTypeDef",
    ) -> "dc_td.ConnectorResponse":
        return dc_td.ConnectorResponse.make_one(res)

    def create_launch_configuration_template(
        self,
        res: "bs_td.LaunchConfigurationTemplateResponseTypeDef",
    ) -> "dc_td.LaunchConfigurationTemplateResponse":
        return dc_td.LaunchConfigurationTemplateResponse.make_one(res)

    def create_replication_configuration_template(
        self,
        res: "bs_td.ReplicationConfigurationTemplateResponseTypeDef",
    ) -> "dc_td.ReplicationConfigurationTemplateResponse":
        return dc_td.ReplicationConfigurationTemplateResponse.make_one(res)

    def create_wave(
        self,
        res: "bs_td.WaveResponseTypeDef",
    ) -> "dc_td.WaveResponse":
        return dc_td.WaveResponse.make_one(res)

    def delete_connector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vcenter_client(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_job_log_items(
        self,
        res: "bs_td.DescribeJobLogItemsResponseTypeDef",
    ) -> "dc_td.DescribeJobLogItemsResponse":
        return dc_td.DescribeJobLogItemsResponse.make_one(res)

    def describe_jobs(
        self,
        res: "bs_td.DescribeJobsResponseTypeDef",
    ) -> "dc_td.DescribeJobsResponse":
        return dc_td.DescribeJobsResponse.make_one(res)

    def describe_launch_configuration_templates(
        self,
        res: "bs_td.DescribeLaunchConfigurationTemplatesResponseTypeDef",
    ) -> "dc_td.DescribeLaunchConfigurationTemplatesResponse":
        return dc_td.DescribeLaunchConfigurationTemplatesResponse.make_one(res)

    def describe_replication_configuration_templates(
        self,
        res: "bs_td.DescribeReplicationConfigurationTemplatesResponseTypeDef",
    ) -> "dc_td.DescribeReplicationConfigurationTemplatesResponse":
        return dc_td.DescribeReplicationConfigurationTemplatesResponse.make_one(res)

    def describe_source_servers(
        self,
        res: "bs_td.DescribeSourceServersResponseTypeDef",
    ) -> "dc_td.DescribeSourceServersResponse":
        return dc_td.DescribeSourceServersResponse.make_one(res)

    def describe_vcenter_clients(
        self,
        res: "bs_td.DescribeVcenterClientsResponseTypeDef",
    ) -> "dc_td.DescribeVcenterClientsResponse":
        return dc_td.DescribeVcenterClientsResponse.make_one(res)

    def disconnect_from_service(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def finalize_cutover(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def get_launch_configuration(
        self,
        res: "bs_td.LaunchConfigurationTypeDef",
    ) -> "dc_td.LaunchConfiguration":
        return dc_td.LaunchConfiguration.make_one(res)

    def get_replication_configuration(
        self,
        res: "bs_td.ReplicationConfigurationTypeDef",
    ) -> "dc_td.ReplicationConfiguration":
        return dc_td.ReplicationConfiguration.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_connectors(
        self,
        res: "bs_td.ListConnectorsResponseTypeDef",
    ) -> "dc_td.ListConnectorsResponse":
        return dc_td.ListConnectorsResponse.make_one(res)

    def list_export_errors(
        self,
        res: "bs_td.ListExportErrorsResponseTypeDef",
    ) -> "dc_td.ListExportErrorsResponse":
        return dc_td.ListExportErrorsResponse.make_one(res)

    def list_exports(
        self,
        res: "bs_td.ListExportsResponseTypeDef",
    ) -> "dc_td.ListExportsResponse":
        return dc_td.ListExportsResponse.make_one(res)

    def list_import_errors(
        self,
        res: "bs_td.ListImportErrorsResponseTypeDef",
    ) -> "dc_td.ListImportErrorsResponse":
        return dc_td.ListImportErrorsResponse.make_one(res)

    def list_imports(
        self,
        res: "bs_td.ListImportsResponseTypeDef",
    ) -> "dc_td.ListImportsResponse":
        return dc_td.ListImportsResponse.make_one(res)

    def list_managed_accounts(
        self,
        res: "bs_td.ListManagedAccountsResponseTypeDef",
    ) -> "dc_td.ListManagedAccountsResponse":
        return dc_td.ListManagedAccountsResponse.make_one(res)

    def list_source_server_actions(
        self,
        res: "bs_td.ListSourceServerActionsResponseTypeDef",
    ) -> "dc_td.ListSourceServerActionsResponse":
        return dc_td.ListSourceServerActionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_template_actions(
        self,
        res: "bs_td.ListTemplateActionsResponseTypeDef",
    ) -> "dc_td.ListTemplateActionsResponse":
        return dc_td.ListTemplateActionsResponse.make_one(res)

    def list_waves(
        self,
        res: "bs_td.ListWavesResponseTypeDef",
    ) -> "dc_td.ListWavesResponse":
        return dc_td.ListWavesResponse.make_one(res)

    def mark_as_archived(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def pause_replication(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def put_source_server_action(
        self,
        res: "bs_td.SourceServerActionDocumentResponseTypeDef",
    ) -> "dc_td.SourceServerActionDocumentResponse":
        return dc_td.SourceServerActionDocumentResponse.make_one(res)

    def put_template_action(
        self,
        res: "bs_td.TemplateActionDocumentResponseTypeDef",
    ) -> "dc_td.TemplateActionDocumentResponse":
        return dc_td.TemplateActionDocumentResponse.make_one(res)

    def resume_replication(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def retry_data_replication(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def start_cutover(
        self,
        res: "bs_td.StartCutoverResponseTypeDef",
    ) -> "dc_td.StartCutoverResponse":
        return dc_td.StartCutoverResponse.make_one(res)

    def start_export(
        self,
        res: "bs_td.StartExportResponseTypeDef",
    ) -> "dc_td.StartExportResponse":
        return dc_td.StartExportResponse.make_one(res)

    def start_import(
        self,
        res: "bs_td.StartImportResponseTypeDef",
    ) -> "dc_td.StartImportResponse":
        return dc_td.StartImportResponse.make_one(res)

    def start_replication(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def start_test(
        self,
        res: "bs_td.StartTestResponseTypeDef",
    ) -> "dc_td.StartTestResponse":
        return dc_td.StartTestResponse.make_one(res)

    def stop_replication(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def terminate_target_instances(
        self,
        res: "bs_td.TerminateTargetInstancesResponseTypeDef",
    ) -> "dc_td.TerminateTargetInstancesResponse":
        return dc_td.TerminateTargetInstancesResponse.make_one(res)

    def unarchive_application(
        self,
        res: "bs_td.ApplicationResponseTypeDef",
    ) -> "dc_td.ApplicationResponse":
        return dc_td.ApplicationResponse.make_one(res)

    def unarchive_wave(
        self,
        res: "bs_td.WaveResponseTypeDef",
    ) -> "dc_td.WaveResponse":
        return dc_td.WaveResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_application(
        self,
        res: "bs_td.ApplicationResponseTypeDef",
    ) -> "dc_td.ApplicationResponse":
        return dc_td.ApplicationResponse.make_one(res)

    def update_connector(
        self,
        res: "bs_td.ConnectorResponseTypeDef",
    ) -> "dc_td.ConnectorResponse":
        return dc_td.ConnectorResponse.make_one(res)

    def update_launch_configuration(
        self,
        res: "bs_td.LaunchConfigurationTypeDef",
    ) -> "dc_td.LaunchConfiguration":
        return dc_td.LaunchConfiguration.make_one(res)

    def update_launch_configuration_template(
        self,
        res: "bs_td.LaunchConfigurationTemplateResponseTypeDef",
    ) -> "dc_td.LaunchConfigurationTemplateResponse":
        return dc_td.LaunchConfigurationTemplateResponse.make_one(res)

    def update_replication_configuration(
        self,
        res: "bs_td.ReplicationConfigurationTypeDef",
    ) -> "dc_td.ReplicationConfiguration":
        return dc_td.ReplicationConfiguration.make_one(res)

    def update_replication_configuration_template(
        self,
        res: "bs_td.ReplicationConfigurationTemplateResponseTypeDef",
    ) -> "dc_td.ReplicationConfigurationTemplateResponse":
        return dc_td.ReplicationConfigurationTemplateResponse.make_one(res)

    def update_source_server(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def update_source_server_replication_type(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def update_wave(
        self,
        res: "bs_td.WaveResponseTypeDef",
    ) -> "dc_td.WaveResponse":
        return dc_td.WaveResponse.make_one(res)


mgn_caster = MGNCaster()
