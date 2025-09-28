# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_panorama import type_defs as bs_td


class PANORAMACaster:

    def create_application_instance(
        self,
        res: "bs_td.CreateApplicationInstanceResponseTypeDef",
    ) -> "dc_td.CreateApplicationInstanceResponse":
        return dc_td.CreateApplicationInstanceResponse.make_one(res)

    def create_job_for_devices(
        self,
        res: "bs_td.CreateJobForDevicesResponseTypeDef",
    ) -> "dc_td.CreateJobForDevicesResponse":
        return dc_td.CreateJobForDevicesResponse.make_one(res)

    def create_node_from_template_job(
        self,
        res: "bs_td.CreateNodeFromTemplateJobResponseTypeDef",
    ) -> "dc_td.CreateNodeFromTemplateJobResponse":
        return dc_td.CreateNodeFromTemplateJobResponse.make_one(res)

    def create_package(
        self,
        res: "bs_td.CreatePackageResponseTypeDef",
    ) -> "dc_td.CreatePackageResponse":
        return dc_td.CreatePackageResponse.make_one(res)

    def create_package_import_job(
        self,
        res: "bs_td.CreatePackageImportJobResponseTypeDef",
    ) -> "dc_td.CreatePackageImportJobResponse":
        return dc_td.CreatePackageImportJobResponse.make_one(res)

    def delete_device(
        self,
        res: "bs_td.DeleteDeviceResponseTypeDef",
    ) -> "dc_td.DeleteDeviceResponse":
        return dc_td.DeleteDeviceResponse.make_one(res)

    def describe_application_instance(
        self,
        res: "bs_td.DescribeApplicationInstanceResponseTypeDef",
    ) -> "dc_td.DescribeApplicationInstanceResponse":
        return dc_td.DescribeApplicationInstanceResponse.make_one(res)

    def describe_application_instance_details(
        self,
        res: "bs_td.DescribeApplicationInstanceDetailsResponseTypeDef",
    ) -> "dc_td.DescribeApplicationInstanceDetailsResponse":
        return dc_td.DescribeApplicationInstanceDetailsResponse.make_one(res)

    def describe_device(
        self,
        res: "bs_td.DescribeDeviceResponseTypeDef",
    ) -> "dc_td.DescribeDeviceResponse":
        return dc_td.DescribeDeviceResponse.make_one(res)

    def describe_device_job(
        self,
        res: "bs_td.DescribeDeviceJobResponseTypeDef",
    ) -> "dc_td.DescribeDeviceJobResponse":
        return dc_td.DescribeDeviceJobResponse.make_one(res)

    def describe_node(
        self,
        res: "bs_td.DescribeNodeResponseTypeDef",
    ) -> "dc_td.DescribeNodeResponse":
        return dc_td.DescribeNodeResponse.make_one(res)

    def describe_node_from_template_job(
        self,
        res: "bs_td.DescribeNodeFromTemplateJobResponseTypeDef",
    ) -> "dc_td.DescribeNodeFromTemplateJobResponse":
        return dc_td.DescribeNodeFromTemplateJobResponse.make_one(res)

    def describe_package(
        self,
        res: "bs_td.DescribePackageResponseTypeDef",
    ) -> "dc_td.DescribePackageResponse":
        return dc_td.DescribePackageResponse.make_one(res)

    def describe_package_import_job(
        self,
        res: "bs_td.DescribePackageImportJobResponseTypeDef",
    ) -> "dc_td.DescribePackageImportJobResponse":
        return dc_td.DescribePackageImportJobResponse.make_one(res)

    def describe_package_version(
        self,
        res: "bs_td.DescribePackageVersionResponseTypeDef",
    ) -> "dc_td.DescribePackageVersionResponse":
        return dc_td.DescribePackageVersionResponse.make_one(res)

    def list_application_instance_dependencies(
        self,
        res: "bs_td.ListApplicationInstanceDependenciesResponseTypeDef",
    ) -> "dc_td.ListApplicationInstanceDependenciesResponse":
        return dc_td.ListApplicationInstanceDependenciesResponse.make_one(res)

    def list_application_instance_node_instances(
        self,
        res: "bs_td.ListApplicationInstanceNodeInstancesResponseTypeDef",
    ) -> "dc_td.ListApplicationInstanceNodeInstancesResponse":
        return dc_td.ListApplicationInstanceNodeInstancesResponse.make_one(res)

    def list_application_instances(
        self,
        res: "bs_td.ListApplicationInstancesResponseTypeDef",
    ) -> "dc_td.ListApplicationInstancesResponse":
        return dc_td.ListApplicationInstancesResponse.make_one(res)

    def list_devices(
        self,
        res: "bs_td.ListDevicesResponseTypeDef",
    ) -> "dc_td.ListDevicesResponse":
        return dc_td.ListDevicesResponse.make_one(res)

    def list_devices_jobs(
        self,
        res: "bs_td.ListDevicesJobsResponseTypeDef",
    ) -> "dc_td.ListDevicesJobsResponse":
        return dc_td.ListDevicesJobsResponse.make_one(res)

    def list_node_from_template_jobs(
        self,
        res: "bs_td.ListNodeFromTemplateJobsResponseTypeDef",
    ) -> "dc_td.ListNodeFromTemplateJobsResponse":
        return dc_td.ListNodeFromTemplateJobsResponse.make_one(res)

    def list_nodes(
        self,
        res: "bs_td.ListNodesResponseTypeDef",
    ) -> "dc_td.ListNodesResponse":
        return dc_td.ListNodesResponse.make_one(res)

    def list_package_import_jobs(
        self,
        res: "bs_td.ListPackageImportJobsResponseTypeDef",
    ) -> "dc_td.ListPackageImportJobsResponse":
        return dc_td.ListPackageImportJobsResponse.make_one(res)

    def list_packages(
        self,
        res: "bs_td.ListPackagesResponseTypeDef",
    ) -> "dc_td.ListPackagesResponse":
        return dc_td.ListPackagesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def provision_device(
        self,
        res: "bs_td.ProvisionDeviceResponseTypeDef",
    ) -> "dc_td.ProvisionDeviceResponse":
        return dc_td.ProvisionDeviceResponse.make_one(res)

    def signal_application_instance_node_instances(
        self,
        res: "bs_td.SignalApplicationInstanceNodeInstancesResponseTypeDef",
    ) -> "dc_td.SignalApplicationInstanceNodeInstancesResponse":
        return dc_td.SignalApplicationInstanceNodeInstancesResponse.make_one(res)

    def update_device_metadata(
        self,
        res: "bs_td.UpdateDeviceMetadataResponseTypeDef",
    ) -> "dc_td.UpdateDeviceMetadataResponse":
        return dc_td.UpdateDeviceMetadataResponse.make_one(res)


panorama_caster = PANORAMACaster()
