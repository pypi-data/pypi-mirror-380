# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesisanalyticsv2 import type_defs as bs_td


class KINESISANALYTICSV2Caster:

    def add_application_cloud_watch_logging_option(
        self,
        res: "bs_td.AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    ) -> "dc_td.AddApplicationCloudWatchLoggingOptionResponse":
        return dc_td.AddApplicationCloudWatchLoggingOptionResponse.make_one(res)

    def add_application_input(
        self,
        res: "bs_td.AddApplicationInputResponseTypeDef",
    ) -> "dc_td.AddApplicationInputResponse":
        return dc_td.AddApplicationInputResponse.make_one(res)

    def add_application_input_processing_configuration(
        self,
        res: "bs_td.AddApplicationInputProcessingConfigurationResponseTypeDef",
    ) -> "dc_td.AddApplicationInputProcessingConfigurationResponse":
        return dc_td.AddApplicationInputProcessingConfigurationResponse.make_one(res)

    def add_application_output(
        self,
        res: "bs_td.AddApplicationOutputResponseTypeDef",
    ) -> "dc_td.AddApplicationOutputResponse":
        return dc_td.AddApplicationOutputResponse.make_one(res)

    def add_application_reference_data_source(
        self,
        res: "bs_td.AddApplicationReferenceDataSourceResponseTypeDef",
    ) -> "dc_td.AddApplicationReferenceDataSourceResponse":
        return dc_td.AddApplicationReferenceDataSourceResponse.make_one(res)

    def add_application_vpc_configuration(
        self,
        res: "bs_td.AddApplicationVpcConfigurationResponseTypeDef",
    ) -> "dc_td.AddApplicationVpcConfigurationResponse":
        return dc_td.AddApplicationVpcConfigurationResponse.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_application_presigned_url(
        self,
        res: "bs_td.CreateApplicationPresignedUrlResponseTypeDef",
    ) -> "dc_td.CreateApplicationPresignedUrlResponse":
        return dc_td.CreateApplicationPresignedUrlResponse.make_one(res)

    def delete_application_cloud_watch_logging_option(
        self,
        res: "bs_td.DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    ) -> "dc_td.DeleteApplicationCloudWatchLoggingOptionResponse":
        return dc_td.DeleteApplicationCloudWatchLoggingOptionResponse.make_one(res)

    def delete_application_input_processing_configuration(
        self,
        res: "bs_td.DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteApplicationInputProcessingConfigurationResponse":
        return dc_td.DeleteApplicationInputProcessingConfigurationResponse.make_one(res)

    def delete_application_output(
        self,
        res: "bs_td.DeleteApplicationOutputResponseTypeDef",
    ) -> "dc_td.DeleteApplicationOutputResponse":
        return dc_td.DeleteApplicationOutputResponse.make_one(res)

    def delete_application_reference_data_source(
        self,
        res: "bs_td.DeleteApplicationReferenceDataSourceResponseTypeDef",
    ) -> "dc_td.DeleteApplicationReferenceDataSourceResponse":
        return dc_td.DeleteApplicationReferenceDataSourceResponse.make_one(res)

    def delete_application_vpc_configuration(
        self,
        res: "bs_td.DeleteApplicationVpcConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteApplicationVpcConfigurationResponse":
        return dc_td.DeleteApplicationVpcConfigurationResponse.make_one(res)

    def describe_application(
        self,
        res: "bs_td.DescribeApplicationResponseTypeDef",
    ) -> "dc_td.DescribeApplicationResponse":
        return dc_td.DescribeApplicationResponse.make_one(res)

    def describe_application_operation(
        self,
        res: "bs_td.DescribeApplicationOperationResponseTypeDef",
    ) -> "dc_td.DescribeApplicationOperationResponse":
        return dc_td.DescribeApplicationOperationResponse.make_one(res)

    def describe_application_snapshot(
        self,
        res: "bs_td.DescribeApplicationSnapshotResponseTypeDef",
    ) -> "dc_td.DescribeApplicationSnapshotResponse":
        return dc_td.DescribeApplicationSnapshotResponse.make_one(res)

    def describe_application_version(
        self,
        res: "bs_td.DescribeApplicationVersionResponseTypeDef",
    ) -> "dc_td.DescribeApplicationVersionResponse":
        return dc_td.DescribeApplicationVersionResponse.make_one(res)

    def discover_input_schema(
        self,
        res: "bs_td.DiscoverInputSchemaResponseTypeDef",
    ) -> "dc_td.DiscoverInputSchemaResponse":
        return dc_td.DiscoverInputSchemaResponse.make_one(res)

    def list_application_operations(
        self,
        res: "bs_td.ListApplicationOperationsResponseTypeDef",
    ) -> "dc_td.ListApplicationOperationsResponse":
        return dc_td.ListApplicationOperationsResponse.make_one(res)

    def list_application_snapshots(
        self,
        res: "bs_td.ListApplicationSnapshotsResponseTypeDef",
    ) -> "dc_td.ListApplicationSnapshotsResponse":
        return dc_td.ListApplicationSnapshotsResponse.make_one(res)

    def list_application_versions(
        self,
        res: "bs_td.ListApplicationVersionsResponseTypeDef",
    ) -> "dc_td.ListApplicationVersionsResponse":
        return dc_td.ListApplicationVersionsResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def rollback_application(
        self,
        res: "bs_td.RollbackApplicationResponseTypeDef",
    ) -> "dc_td.RollbackApplicationResponse":
        return dc_td.RollbackApplicationResponse.make_one(res)

    def start_application(
        self,
        res: "bs_td.StartApplicationResponseTypeDef",
    ) -> "dc_td.StartApplicationResponse":
        return dc_td.StartApplicationResponse.make_one(res)

    def stop_application(
        self,
        res: "bs_td.StopApplicationResponseTypeDef",
    ) -> "dc_td.StopApplicationResponse":
        return dc_td.StopApplicationResponse.make_one(res)

    def update_application(
        self,
        res: "bs_td.UpdateApplicationResponseTypeDef",
    ) -> "dc_td.UpdateApplicationResponse":
        return dc_td.UpdateApplicationResponse.make_one(res)

    def update_application_maintenance_configuration(
        self,
        res: "bs_td.UpdateApplicationMaintenanceConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateApplicationMaintenanceConfigurationResponse":
        return dc_td.UpdateApplicationMaintenanceConfigurationResponse.make_one(res)


kinesisanalyticsv2_caster = KINESISANALYTICSV2Caster()
