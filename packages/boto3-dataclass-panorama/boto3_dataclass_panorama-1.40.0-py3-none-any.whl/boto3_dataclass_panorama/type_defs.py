# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_panorama import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AlternateSoftwareMetadata:
    boto3_raw_data: "type_defs.AlternateSoftwareMetadataTypeDef" = dataclasses.field()

    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlternateSoftwareMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlternateSoftwareMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportedRuntimeContextState:
    boto3_raw_data: "type_defs.ReportedRuntimeContextStateTypeDef" = dataclasses.field()

    DesiredState = field("DesiredState")
    DeviceReportedStatus = field("DeviceReportedStatus")
    DeviceReportedTime = field("DeviceReportedTime")
    RuntimeContextName = field("RuntimeContextName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportedRuntimeContextStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportedRuntimeContextStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManifestOverridesPayload:
    boto3_raw_data: "type_defs.ManifestOverridesPayloadTypeDef" = dataclasses.field()

    PayloadData = field("PayloadData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManifestOverridesPayloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManifestOverridesPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManifestPayload:
    boto3_raw_data: "type_defs.ManifestPayloadTypeDef" = dataclasses.field()

    PayloadData = field("PayloadData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManifestPayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManifestPayloadTypeDef"]],
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
class Job:
    boto3_raw_data: "type_defs.JobTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")
    JobId = field("JobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageRequest:
    boto3_raw_data: "type_defs.CreatePackageRequestTypeDef" = dataclasses.field()

    PackageName = field("PackageName")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLocation:
    boto3_raw_data: "type_defs.StorageLocationTypeDef" = dataclasses.field()

    BinaryPrefixLocation = field("BinaryPrefixLocation")
    Bucket = field("Bucket")
    GeneratedPrefixLocation = field("GeneratedPrefixLocation")
    ManifestPrefixLocation = field("ManifestPrefixLocation")
    RepoPrefixLocation = field("RepoPrefixLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StorageLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeviceRequest:
    boto3_raw_data: "type_defs.DeleteDeviceRequestTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageRequest:
    boto3_raw_data: "type_defs.DeletePackageRequestTypeDef" = dataclasses.field()

    PackageId = field("PackageId")
    ForceDelete = field("ForceDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterPackageVersionRequest:
    boto3_raw_data: "type_defs.DeregisterPackageVersionRequestTypeDef" = (
        dataclasses.field()
    )

    PackageId = field("PackageId")
    PackageVersion = field("PackageVersion")
    PatchVersion = field("PatchVersion")
    OwnerAccount = field("OwnerAccount")
    UpdatedLatestPatchVersion = field("UpdatedLatestPatchVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterPackageVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterPackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationInstanceDetailsRequest:
    boto3_raw_data: "type_defs.DescribeApplicationInstanceDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationInstanceId = field("ApplicationInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationInstanceDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationInstanceDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationInstanceRequest:
    boto3_raw_data: "type_defs.DescribeApplicationInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationInstanceId = field("ApplicationInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeviceJobRequest:
    boto3_raw_data: "type_defs.DescribeDeviceJobRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeviceJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeviceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeviceRequest:
    boto3_raw_data: "type_defs.DescribeDeviceRequestTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LatestDeviceJob:
    boto3_raw_data: "type_defs.LatestDeviceJobTypeDef" = dataclasses.field()

    ImageVersion = field("ImageVersion")
    JobType = field("JobType")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LatestDeviceJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LatestDeviceJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodeFromTemplateJobRequest:
    boto3_raw_data: "type_defs.DescribeNodeFromTemplateJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNodeFromTemplateJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodeFromTemplateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobResourceTagsOutput:
    boto3_raw_data: "type_defs.JobResourceTagsOutputTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobResourceTagsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobResourceTagsOutputTypeDef"]
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

    NodeId = field("NodeId")
    OwnerAccount = field("OwnerAccount")

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
class DescribePackageImportJobRequest:
    boto3_raw_data: "type_defs.DescribePackageImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePackageImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageRequest:
    boto3_raw_data: "type_defs.DescribePackageRequestTypeDef" = dataclasses.field()

    PackageId = field("PackageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageVersionRequest:
    boto3_raw_data: "type_defs.DescribePackageVersionRequestTypeDef" = (
        dataclasses.field()
    )

    PackageId = field("PackageId")
    PackageVersion = field("PackageVersion")
    OwnerAccount = field("OwnerAccount")
    PatchVersion = field("PatchVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePackageVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OTAJobConfig:
    boto3_raw_data: "type_defs.OTAJobConfigTypeDef" = dataclasses.field()

    ImageVersion = field("ImageVersion")
    AllowMajorVersionUpdate = field("AllowMajorVersionUpdate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OTAJobConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OTAJobConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceJob:
    boto3_raw_data: "type_defs.DeviceJobTypeDef" = dataclasses.field()

    CreatedTime = field("CreatedTime")
    DeviceId = field("DeviceId")
    DeviceName = field("DeviceName")
    JobId = field("JobId")
    JobType = field("JobType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceJobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticIpConnectionInfoOutput:
    boto3_raw_data: "type_defs.StaticIpConnectionInfoOutputTypeDef" = (
        dataclasses.field()
    )

    DefaultGateway = field("DefaultGateway")
    Dns = field("Dns")
    IpAddress = field("IpAddress")
    Mask = field("Mask")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StaticIpConnectionInfoOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticIpConnectionInfoOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticIpConnectionInfo:
    boto3_raw_data: "type_defs.StaticIpConnectionInfoTypeDef" = dataclasses.field()

    DefaultGateway = field("DefaultGateway")
    Dns = field("Dns")
    IpAddress = field("IpAddress")
    Mask = field("Mask")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StaticIpConnectionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticIpConnectionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EthernetStatus:
    boto3_raw_data: "type_defs.EthernetStatusTypeDef" = dataclasses.field()

    ConnectionStatus = field("ConnectionStatus")
    HwAddress = field("HwAddress")
    IpAddress = field("IpAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EthernetStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EthernetStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobResourceTags:
    boto3_raw_data: "type_defs.JobResourceTagsTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobResourceTagsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobResourceTagsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationInstanceDependenciesRequest:
    boto3_raw_data: "type_defs.ListApplicationInstanceDependenciesRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationInstanceId = field("ApplicationInstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationInstanceDependenciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationInstanceDependenciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageObject:
    boto3_raw_data: "type_defs.PackageObjectTypeDef" = dataclasses.field()

    Name = field("Name")
    PackageVersion = field("PackageVersion")
    PatchVersion = field("PatchVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackageObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PackageObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationInstanceNodeInstancesRequest:
    boto3_raw_data: "type_defs.ListApplicationInstanceNodeInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationInstanceId = field("ApplicationInstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationInstanceNodeInstancesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationInstanceNodeInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeInstance:
    boto3_raw_data: "type_defs.NodeInstanceTypeDef" = dataclasses.field()

    CurrentStatus = field("CurrentStatus")
    NodeInstanceId = field("NodeInstanceId")
    NodeId = field("NodeId")
    NodeName = field("NodeName")
    PackageName = field("PackageName")
    PackagePatchVersion = field("PackagePatchVersion")
    PackageVersion = field("PackageVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationInstancesRequest:
    boto3_raw_data: "type_defs.ListApplicationInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    DeviceId = field("DeviceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    StatusFilter = field("StatusFilter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationInstancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicesJobsRequest:
    boto3_raw_data: "type_defs.ListDevicesJobsRequestTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDevicesJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicesJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicesRequest:
    boto3_raw_data: "type_defs.ListDevicesRequestTypeDef" = dataclasses.field()

    DeviceAggregatedStatusFilter = field("DeviceAggregatedStatusFilter")
    MaxResults = field("MaxResults")
    NameFilter = field("NameFilter")
    NextToken = field("NextToken")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodeFromTemplateJobsRequest:
    boto3_raw_data: "type_defs.ListNodeFromTemplateJobsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNodeFromTemplateJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodeFromTemplateJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeFromTemplateJob:
    boto3_raw_data: "type_defs.NodeFromTemplateJobTypeDef" = dataclasses.field()

    CreatedTime = field("CreatedTime")
    JobId = field("JobId")
    NodeName = field("NodeName")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    TemplateType = field("TemplateType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeFromTemplateJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeFromTemplateJobTypeDef"]
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

    Category = field("Category")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    OwnerAccount = field("OwnerAccount")
    PackageName = field("PackageName")
    PackageVersion = field("PackageVersion")
    PatchVersion = field("PatchVersion")

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
class Node:
    boto3_raw_data: "type_defs.NodeTypeDef" = dataclasses.field()

    Category = field("Category")
    CreatedTime = field("CreatedTime")
    Name = field("Name")
    NodeId = field("NodeId")
    PackageId = field("PackageId")
    PackageName = field("PackageName")
    PackageVersion = field("PackageVersion")
    PatchVersion = field("PatchVersion")
    Description = field("Description")
    OwnerAccount = field("OwnerAccount")
    PackageArn = field("PackageArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageImportJobsRequest:
    boto3_raw_data: "type_defs.ListPackageImportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackageImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageImportJob:
    boto3_raw_data: "type_defs.PackageImportJobTypeDef" = dataclasses.field()

    CreatedTime = field("CreatedTime")
    JobId = field("JobId")
    JobType = field("JobType")
    LastUpdatedTime = field("LastUpdatedTime")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackageImportJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageImportJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesRequest:
    boto3_raw_data: "type_defs.ListPackagesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageListItem:
    boto3_raw_data: "type_defs.PackageListItemTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedTime = field("CreatedTime")
    PackageId = field("PackageId")
    PackageName = field("PackageName")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackageListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PackageListItemTypeDef"]],
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
class NtpPayloadOutput:
    boto3_raw_data: "type_defs.NtpPayloadOutputTypeDef" = dataclasses.field()

    NtpServers = field("NtpServers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NtpPayloadOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NtpPayloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NtpPayload:
    boto3_raw_data: "type_defs.NtpPayloadTypeDef" = dataclasses.field()

    NtpServers = field("NtpServers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NtpPayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NtpPayloadTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NtpStatus:
    boto3_raw_data: "type_defs.NtpStatusTypeDef" = dataclasses.field()

    ConnectionStatus = field("ConnectionStatus")
    IpAddress = field("IpAddress")
    NtpServerName = field("NtpServerName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NtpStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NtpStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeInputPort:
    boto3_raw_data: "type_defs.NodeInputPortTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    Description = field("Description")
    MaxConnections = field("MaxConnections")
    Name = field("Name")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeInputPortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeInputPortTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeOutputPort:
    boto3_raw_data: "type_defs.NodeOutputPortTypeDef" = dataclasses.field()

    Description = field("Description")
    Name = field("Name")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeOutputPortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeOutputPortTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeSignal:
    boto3_raw_data: "type_defs.NodeSignalTypeDef" = dataclasses.field()

    NodeInstanceId = field("NodeInstanceId")
    Signal = field("Signal")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeSignalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeSignalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutPutS3Location:
    boto3_raw_data: "type_defs.OutPutS3LocationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKey = field("ObjectKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutPutS3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutPutS3LocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVersionOutputConfig:
    boto3_raw_data: "type_defs.PackageVersionOutputConfigTypeDef" = dataclasses.field()

    PackageName = field("PackageName")
    PackageVersion = field("PackageVersion")
    MarkLatest = field("MarkLatest")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVersionOutputConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVersionOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKey = field("ObjectKey")
    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterPackageVersionRequest:
    boto3_raw_data: "type_defs.RegisterPackageVersionRequestTypeDef" = (
        dataclasses.field()
    )

    PackageId = field("PackageId")
    PackageVersion = field("PackageVersion")
    PatchVersion = field("PatchVersion")
    MarkLatest = field("MarkLatest")
    OwnerAccount = field("OwnerAccount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterPackageVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterPackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveApplicationInstanceRequest:
    boto3_raw_data: "type_defs.RemoveApplicationInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationInstanceId = field("ApplicationInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveApplicationInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveApplicationInstanceRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
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
class UpdateDeviceMetadataRequest:
    boto3_raw_data: "type_defs.UpdateDeviceMetadataRequestTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeviceMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeviceMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationInstance:
    boto3_raw_data: "type_defs.ApplicationInstanceTypeDef" = dataclasses.field()

    ApplicationInstanceId = field("ApplicationInstanceId")
    Arn = field("Arn")
    CreatedTime = field("CreatedTime")
    DefaultRuntimeContextDevice = field("DefaultRuntimeContextDevice")
    DefaultRuntimeContextDeviceName = field("DefaultRuntimeContextDeviceName")
    Description = field("Description")
    HealthStatus = field("HealthStatus")
    Name = field("Name")

    @cached_property
    def RuntimeContextStates(self):  # pragma: no cover
        return ReportedRuntimeContextState.make_many(
            self.boto3_raw_data["RuntimeContextStates"]
        )

    Status = field("Status")
    StatusDescription = field("StatusDescription")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationInstanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationInstanceRequest:
    boto3_raw_data: "type_defs.CreateApplicationInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    DefaultRuntimeContextDevice = field("DefaultRuntimeContextDevice")

    @cached_property
    def ManifestPayload(self):  # pragma: no cover
        return ManifestPayload.make_one(self.boto3_raw_data["ManifestPayload"])

    ApplicationInstanceIdToReplace = field("ApplicationInstanceIdToReplace")
    Description = field("Description")

    @cached_property
    def ManifestOverridesPayload(self):  # pragma: no cover
        return ManifestOverridesPayload.make_one(
            self.boto3_raw_data["ManifestOverridesPayload"]
        )

    Name = field("Name")
    RuntimeRoleArn = field("RuntimeRoleArn")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateApplicationInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationInstanceResponse:
    boto3_raw_data: "type_defs.CreateApplicationInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationInstanceId = field("ApplicationInstanceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateApplicationInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodeFromTemplateJobResponse:
    boto3_raw_data: "type_defs.CreateNodeFromTemplateJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateNodeFromTemplateJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNodeFromTemplateJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageImportJobResponse:
    boto3_raw_data: "type_defs.CreatePackageImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePackageImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeviceResponse:
    boto3_raw_data: "type_defs.DeleteDeviceResponseTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationInstanceDetailsResponse:
    boto3_raw_data: "type_defs.DescribeApplicationInstanceDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationInstanceId = field("ApplicationInstanceId")
    ApplicationInstanceIdToReplace = field("ApplicationInstanceIdToReplace")
    CreatedTime = field("CreatedTime")
    DefaultRuntimeContextDevice = field("DefaultRuntimeContextDevice")
    Description = field("Description")

    @cached_property
    def ManifestOverridesPayload(self):  # pragma: no cover
        return ManifestOverridesPayload.make_one(
            self.boto3_raw_data["ManifestOverridesPayload"]
        )

    @cached_property
    def ManifestPayload(self):  # pragma: no cover
        return ManifestPayload.make_one(self.boto3_raw_data["ManifestPayload"])

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationInstanceDetailsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationInstanceDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationInstanceResponse:
    boto3_raw_data: "type_defs.DescribeApplicationInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationInstanceId = field("ApplicationInstanceId")
    ApplicationInstanceIdToReplace = field("ApplicationInstanceIdToReplace")
    Arn = field("Arn")
    CreatedTime = field("CreatedTime")
    DefaultRuntimeContextDevice = field("DefaultRuntimeContextDevice")
    DefaultRuntimeContextDeviceName = field("DefaultRuntimeContextDeviceName")
    Description = field("Description")
    HealthStatus = field("HealthStatus")
    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")

    @cached_property
    def RuntimeContextStates(self):  # pragma: no cover
        return ReportedRuntimeContextState.make_many(
            self.boto3_raw_data["RuntimeContextStates"]
        )

    RuntimeRoleArn = field("RuntimeRoleArn")
    Status = field("Status")
    StatusDescription = field("StatusDescription")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeviceJobResponse:
    boto3_raw_data: "type_defs.DescribeDeviceJobResponseTypeDef" = dataclasses.field()

    CreatedTime = field("CreatedTime")
    DeviceArn = field("DeviceArn")
    DeviceId = field("DeviceId")
    DeviceName = field("DeviceName")
    DeviceType = field("DeviceType")
    ImageVersion = field("ImageVersion")
    JobId = field("JobId")
    JobType = field("JobType")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeviceJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeviceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageVersionResponse:
    boto3_raw_data: "type_defs.DescribePackageVersionResponseTypeDef" = (
        dataclasses.field()
    )

    IsLatestPatch = field("IsLatestPatch")
    OwnerAccount = field("OwnerAccount")
    PackageArn = field("PackageArn")
    PackageId = field("PackageId")
    PackageName = field("PackageName")
    PackageVersion = field("PackageVersion")
    PatchVersion = field("PatchVersion")
    RegisteredTime = field("RegisteredTime")
    Status = field("Status")
    StatusDescription = field("StatusDescription")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePackageVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageVersionResponseTypeDef"]
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
class ProvisionDeviceResponse:
    boto3_raw_data: "type_defs.ProvisionDeviceResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Certificates = field("Certificates")
    DeviceId = field("DeviceId")
    IotThingName = field("IotThingName")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalApplicationInstanceNodeInstancesResponse:
    boto3_raw_data: (
        "type_defs.SignalApplicationInstanceNodeInstancesResponseTypeDef"
    ) = dataclasses.field()

    ApplicationInstanceId = field("ApplicationInstanceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SignalApplicationInstanceNodeInstancesResponseTypeDef"
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
                "type_defs.SignalApplicationInstanceNodeInstancesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeviceMetadataResponse:
    boto3_raw_data: "type_defs.UpdateDeviceMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    DeviceId = field("DeviceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeviceMetadataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeviceMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobForDevicesResponse:
    boto3_raw_data: "type_defs.CreateJobForDevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["Jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobForDevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobForDevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageResponse:
    boto3_raw_data: "type_defs.CreatePackageResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    PackageId = field("PackageId")

    @cached_property
    def StorageLocation(self):  # pragma: no cover
        return StorageLocation.make_one(self.boto3_raw_data["StorageLocation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageResponse:
    boto3_raw_data: "type_defs.DescribePackageResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedTime = field("CreatedTime")
    PackageId = field("PackageId")
    PackageName = field("PackageName")
    ReadAccessPrincipalArns = field("ReadAccessPrincipalArns")

    @cached_property
    def StorageLocation(self):  # pragma: no cover
        return StorageLocation.make_one(self.boto3_raw_data["StorageLocation"])

    Tags = field("Tags")
    WriteAccessPrincipalArns = field("WriteAccessPrincipalArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Device:
    boto3_raw_data: "type_defs.DeviceTypeDef" = dataclasses.field()

    Brand = field("Brand")
    CreatedTime = field("CreatedTime")
    CurrentSoftware = field("CurrentSoftware")
    Description = field("Description")
    DeviceAggregatedStatus = field("DeviceAggregatedStatus")
    DeviceId = field("DeviceId")
    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def LatestDeviceJob(self):  # pragma: no cover
        return LatestDeviceJob.make_one(self.boto3_raw_data["LatestDeviceJob"])

    LeaseExpirationTime = field("LeaseExpirationTime")
    Name = field("Name")
    ProvisioningStatus = field("ProvisioningStatus")
    Tags = field("Tags")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodeFromTemplateJobResponse:
    boto3_raw_data: "type_defs.DescribeNodeFromTemplateJobResponseTypeDef" = (
        dataclasses.field()
    )

    CreatedTime = field("CreatedTime")
    JobId = field("JobId")

    @cached_property
    def JobTags(self):  # pragma: no cover
        return JobResourceTagsOutput.make_many(self.boto3_raw_data["JobTags"])

    LastUpdatedTime = field("LastUpdatedTime")
    NodeDescription = field("NodeDescription")
    NodeName = field("NodeName")
    OutputPackageName = field("OutputPackageName")
    OutputPackageVersion = field("OutputPackageVersion")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    TemplateParameters = field("TemplateParameters")
    TemplateType = field("TemplateType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNodeFromTemplateJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodeFromTemplateJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceJobConfig:
    boto3_raw_data: "type_defs.DeviceJobConfigTypeDef" = dataclasses.field()

    @cached_property
    def OTAJobConfig(self):  # pragma: no cover
        return OTAJobConfig.make_one(self.boto3_raw_data["OTAJobConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceJobConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceJobConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicesJobsResponse:
    boto3_raw_data: "type_defs.ListDevicesJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DeviceJobs(self):  # pragma: no cover
        return DeviceJob.make_many(self.boto3_raw_data["DeviceJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDevicesJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicesJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EthernetPayloadOutput:
    boto3_raw_data: "type_defs.EthernetPayloadOutputTypeDef" = dataclasses.field()

    ConnectionType = field("ConnectionType")

    @cached_property
    def StaticIpConnectionInfo(self):  # pragma: no cover
        return StaticIpConnectionInfoOutput.make_one(
            self.boto3_raw_data["StaticIpConnectionInfo"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EthernetPayloadOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EthernetPayloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EthernetPayload:
    boto3_raw_data: "type_defs.EthernetPayloadTypeDef" = dataclasses.field()

    ConnectionType = field("ConnectionType")

    @cached_property
    def StaticIpConnectionInfo(self):  # pragma: no cover
        return StaticIpConnectionInfo.make_one(
            self.boto3_raw_data["StaticIpConnectionInfo"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EthernetPayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EthernetPayloadTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationInstanceDependenciesResponse:
    boto3_raw_data: "type_defs.ListApplicationInstanceDependenciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PackageObjects(self):  # pragma: no cover
        return PackageObject.make_many(self.boto3_raw_data["PackageObjects"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationInstanceDependenciesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationInstanceDependenciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationInstanceNodeInstancesResponse:
    boto3_raw_data: "type_defs.ListApplicationInstanceNodeInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NodeInstances(self):  # pragma: no cover
        return NodeInstance.make_many(self.boto3_raw_data["NodeInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationInstanceNodeInstancesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationInstanceNodeInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodeFromTemplateJobsResponse:
    boto3_raw_data: "type_defs.ListNodeFromTemplateJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NodeFromTemplateJobs(self):  # pragma: no cover
        return NodeFromTemplateJob.make_many(
            self.boto3_raw_data["NodeFromTemplateJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNodeFromTemplateJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodeFromTemplateJobsResponseTypeDef"]
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
        return Node.make_many(self.boto3_raw_data["Nodes"])

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
class ListPackageImportJobsResponse:
    boto3_raw_data: "type_defs.ListPackageImportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PackageImportJobs(self):  # pragma: no cover
        return PackageImportJob.make_many(self.boto3_raw_data["PackageImportJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPackageImportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesResponse:
    boto3_raw_data: "type_defs.ListPackagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Packages(self):  # pragma: no cover
        return PackageListItem.make_many(self.boto3_raw_data["Packages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkStatus:
    boto3_raw_data: "type_defs.NetworkStatusTypeDef" = dataclasses.field()

    @cached_property
    def Ethernet0Status(self):  # pragma: no cover
        return EthernetStatus.make_one(self.boto3_raw_data["Ethernet0Status"])

    @cached_property
    def Ethernet1Status(self):  # pragma: no cover
        return EthernetStatus.make_one(self.boto3_raw_data["Ethernet1Status"])

    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def NtpStatus(self):  # pragma: no cover
        return NtpStatus.make_one(self.boto3_raw_data["NtpStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeInterface:
    boto3_raw_data: "type_defs.NodeInterfaceTypeDef" = dataclasses.field()

    @cached_property
    def Inputs(self):  # pragma: no cover
        return NodeInputPort.make_many(self.boto3_raw_data["Inputs"])

    @cached_property
    def Outputs(self):  # pragma: no cover
        return NodeOutputPort.make_many(self.boto3_raw_data["Outputs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeInterfaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalApplicationInstanceNodeInstancesRequest:
    boto3_raw_data: "type_defs.SignalApplicationInstanceNodeInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationInstanceId = field("ApplicationInstanceId")

    @cached_property
    def NodeSignals(self):  # pragma: no cover
        return NodeSignal.make_many(self.boto3_raw_data["NodeSignals"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SignalApplicationInstanceNodeInstancesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalApplicationInstanceNodeInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageImportJobOutput:
    boto3_raw_data: "type_defs.PackageImportJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def OutputS3Location(self):  # pragma: no cover
        return OutPutS3Location.make_one(self.boto3_raw_data["OutputS3Location"])

    PackageId = field("PackageId")
    PackageVersion = field("PackageVersion")
    PatchVersion = field("PatchVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageImportJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageImportJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageImportJobOutputConfig:
    boto3_raw_data: "type_defs.PackageImportJobOutputConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PackageVersionOutputConfig(self):  # pragma: no cover
        return PackageVersionOutputConfig.make_one(
            self.boto3_raw_data["PackageVersionOutputConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageImportJobOutputConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageImportJobOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVersionInputConfig:
    boto3_raw_data: "type_defs.PackageVersionInputConfigTypeDef" = dataclasses.field()

    @cached_property
    def S3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["S3Location"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVersionInputConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVersionInputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationInstancesResponse:
    boto3_raw_data: "type_defs.ListApplicationInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationInstances(self):  # pragma: no cover
        return ApplicationInstance.make_many(
            self.boto3_raw_data["ApplicationInstances"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationInstancesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicesResponse:
    boto3_raw_data: "type_defs.ListDevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Devices(self):  # pragma: no cover
        return Device.make_many(self.boto3_raw_data["Devices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobForDevicesRequest:
    boto3_raw_data: "type_defs.CreateJobForDevicesRequestTypeDef" = dataclasses.field()

    DeviceIds = field("DeviceIds")
    JobType = field("JobType")

    @cached_property
    def DeviceJobConfig(self):  # pragma: no cover
        return DeviceJobConfig.make_one(self.boto3_raw_data["DeviceJobConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobForDevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobForDevicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkPayloadOutput:
    boto3_raw_data: "type_defs.NetworkPayloadOutputTypeDef" = dataclasses.field()

    @cached_property
    def Ethernet0(self):  # pragma: no cover
        return EthernetPayloadOutput.make_one(self.boto3_raw_data["Ethernet0"])

    @cached_property
    def Ethernet1(self):  # pragma: no cover
        return EthernetPayloadOutput.make_one(self.boto3_raw_data["Ethernet1"])

    @cached_property
    def Ntp(self):  # pragma: no cover
        return NtpPayloadOutput.make_one(self.boto3_raw_data["Ntp"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkPayloadOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkPayloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkPayload:
    boto3_raw_data: "type_defs.NetworkPayloadTypeDef" = dataclasses.field()

    @cached_property
    def Ethernet0(self):  # pragma: no cover
        return EthernetPayload.make_one(self.boto3_raw_data["Ethernet0"])

    @cached_property
    def Ethernet1(self):  # pragma: no cover
        return EthernetPayload.make_one(self.boto3_raw_data["Ethernet1"])

    @cached_property
    def Ntp(self):  # pragma: no cover
        return NtpPayload.make_one(self.boto3_raw_data["Ntp"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkPayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkPayloadTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodeFromTemplateJobRequest:
    boto3_raw_data: "type_defs.CreateNodeFromTemplateJobRequestTypeDef" = (
        dataclasses.field()
    )

    NodeName = field("NodeName")
    OutputPackageName = field("OutputPackageName")
    OutputPackageVersion = field("OutputPackageVersion")
    TemplateParameters = field("TemplateParameters")
    TemplateType = field("TemplateType")
    JobTags = field("JobTags")
    NodeDescription = field("NodeDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateNodeFromTemplateJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNodeFromTemplateJobRequestTypeDef"]
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

    AssetName = field("AssetName")
    Category = field("Category")
    CreatedTime = field("CreatedTime")
    Description = field("Description")
    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    NodeId = field("NodeId")

    @cached_property
    def NodeInterface(self):  # pragma: no cover
        return NodeInterface.make_one(self.boto3_raw_data["NodeInterface"])

    OwnerAccount = field("OwnerAccount")
    PackageArn = field("PackageArn")
    PackageId = field("PackageId")
    PackageName = field("PackageName")
    PackageVersion = field("PackageVersion")
    PatchVersion = field("PatchVersion")

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
class PackageImportJobInputConfig:
    boto3_raw_data: "type_defs.PackageImportJobInputConfigTypeDef" = dataclasses.field()

    @cached_property
    def PackageVersionInputConfig(self):  # pragma: no cover
        return PackageVersionInputConfig.make_one(
            self.boto3_raw_data["PackageVersionInputConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageImportJobInputConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageImportJobInputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeviceResponse:
    boto3_raw_data: "type_defs.DescribeDeviceResponseTypeDef" = dataclasses.field()

    @cached_property
    def AlternateSoftwares(self):  # pragma: no cover
        return AlternateSoftwareMetadata.make_many(
            self.boto3_raw_data["AlternateSoftwares"]
        )

    Arn = field("Arn")
    Brand = field("Brand")
    CreatedTime = field("CreatedTime")

    @cached_property
    def CurrentNetworkingStatus(self):  # pragma: no cover
        return NetworkStatus.make_one(self.boto3_raw_data["CurrentNetworkingStatus"])

    CurrentSoftware = field("CurrentSoftware")
    Description = field("Description")
    DeviceAggregatedStatus = field("DeviceAggregatedStatus")
    DeviceConnectionStatus = field("DeviceConnectionStatus")
    DeviceId = field("DeviceId")
    LatestAlternateSoftware = field("LatestAlternateSoftware")

    @cached_property
    def LatestDeviceJob(self):  # pragma: no cover
        return LatestDeviceJob.make_one(self.boto3_raw_data["LatestDeviceJob"])

    LatestSoftware = field("LatestSoftware")
    LeaseExpirationTime = field("LeaseExpirationTime")
    Name = field("Name")

    @cached_property
    def NetworkingConfiguration(self):  # pragma: no cover
        return NetworkPayloadOutput.make_one(
            self.boto3_raw_data["NetworkingConfiguration"]
        )

    ProvisioningStatus = field("ProvisioningStatus")
    SerialNumber = field("SerialNumber")
    Tags = field("Tags")
    Type = field("Type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageImportJobRequest:
    boto3_raw_data: "type_defs.CreatePackageImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    ClientToken = field("ClientToken")

    @cached_property
    def InputConfig(self):  # pragma: no cover
        return PackageImportJobInputConfig.make_one(self.boto3_raw_data["InputConfig"])

    JobType = field("JobType")

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return PackageImportJobOutputConfig.make_one(
            self.boto3_raw_data["OutputConfig"]
        )

    JobTags = field("JobTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePackageImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageImportJobResponse:
    boto3_raw_data: "type_defs.DescribePackageImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    ClientToken = field("ClientToken")
    CreatedTime = field("CreatedTime")

    @cached_property
    def InputConfig(self):  # pragma: no cover
        return PackageImportJobInputConfig.make_one(self.boto3_raw_data["InputConfig"])

    JobId = field("JobId")

    @cached_property
    def JobTags(self):  # pragma: no cover
        return JobResourceTagsOutput.make_many(self.boto3_raw_data["JobTags"])

    JobType = field("JobType")
    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def Output(self):  # pragma: no cover
        return PackageImportJobOutput.make_one(self.boto3_raw_data["Output"])

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return PackageImportJobOutputConfig.make_one(
            self.boto3_raw_data["OutputConfig"]
        )

    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePackageImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionDeviceRequest:
    boto3_raw_data: "type_defs.ProvisionDeviceRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    NetworkingConfiguration = field("NetworkingConfiguration")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
