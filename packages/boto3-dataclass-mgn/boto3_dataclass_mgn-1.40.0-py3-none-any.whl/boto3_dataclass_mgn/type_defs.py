# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mgn import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ApplicationAggregatedStatus:
    boto3_raw_data: "type_defs.ApplicationAggregatedStatusTypeDef" = dataclasses.field()

    healthStatus = field("healthStatus")
    lastUpdateDateTime = field("lastUpdateDateTime")
    progressStatus = field("progressStatus")
    totalSourceServers = field("totalSourceServers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationAggregatedStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationAggregatedStatusTypeDef"]
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
class ArchiveApplicationRequest:
    boto3_raw_data: "type_defs.ArchiveApplicationRequestTypeDef" = dataclasses.field()

    applicationID = field("applicationID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveWaveRequest:
    boto3_raw_data: "type_defs.ArchiveWaveRequestTypeDef" = dataclasses.field()

    waveID = field("waveID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveWaveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveWaveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateApplicationsRequest:
    boto3_raw_data: "type_defs.AssociateApplicationsRequestTypeDef" = (
        dataclasses.field()
    )

    applicationIDs = field("applicationIDs")
    waveID = field("waveID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSourceServersRequest:
    boto3_raw_data: "type_defs.AssociateSourceServersRequestTypeDef" = (
        dataclasses.field()
    )

    applicationID = field("applicationID")
    sourceServerIDs = field("sourceServerIDs")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateSourceServersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSourceServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CPU:
    boto3_raw_data: "type_defs.CPUTypeDef" = dataclasses.field()

    cores = field("cores")
    modelName = field("modelName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CPUTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CPUTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeServerLifeCycleStateSourceServerLifecycle:
    boto3_raw_data: (
        "type_defs.ChangeServerLifeCycleStateSourceServerLifecycleTypeDef"
    ) = dataclasses.field()

    state = field("state")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangeServerLifeCycleStateSourceServerLifecycleTypeDef"
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
                "type_defs.ChangeServerLifeCycleStateSourceServerLifecycleTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorSsmCommandConfig:
    boto3_raw_data: "type_defs.ConnectorSsmCommandConfigTypeDef" = dataclasses.field()

    cloudWatchOutputEnabled = field("cloudWatchOutputEnabled")
    s3OutputEnabled = field("s3OutputEnabled")
    cloudWatchLogGroupName = field("cloudWatchLogGroupName")
    outputS3BucketName = field("outputS3BucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorSsmCommandConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorSsmCommandConfigTypeDef"]
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

    name = field("name")
    accountID = field("accountID")
    description = field("description")
    tags = field("tags")

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
class LaunchTemplateDiskConf:
    boto3_raw_data: "type_defs.LaunchTemplateDiskConfTypeDef" = dataclasses.field()

    iops = field("iops")
    throughput = field("throughput")
    volumeType = field("volumeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateDiskConfTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateDiskConfTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Licensing:
    boto3_raw_data: "type_defs.LicensingTypeDef" = dataclasses.field()

    osByol = field("osByol")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LicensingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LicensingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.CreateReplicationConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")
    tags = field("tags")
    useFipsEndpoint = field("useFipsEndpoint")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateReplicationConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWaveRequest:
    boto3_raw_data: "type_defs.CreateWaveRequestTypeDef" = dataclasses.field()

    name = field("name")
    accountID = field("accountID")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateWaveRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWaveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationError:
    boto3_raw_data: "type_defs.DataReplicationErrorTypeDef" = dataclasses.field()

    error = field("error")
    rawError = field("rawError")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataReplicationErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationInfoReplicatedDisk:
    boto3_raw_data: "type_defs.DataReplicationInfoReplicatedDiskTypeDef" = (
        dataclasses.field()
    )

    backloggedStorageBytes = field("backloggedStorageBytes")
    deviceName = field("deviceName")
    replicatedStorageBytes = field("replicatedStorageBytes")
    rescannedStorageBytes = field("rescannedStorageBytes")
    totalStorageBytes = field("totalStorageBytes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataReplicationInfoReplicatedDiskTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationInfoReplicatedDiskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationInitiationStep:
    boto3_raw_data: "type_defs.DataReplicationInitiationStepTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataReplicationInitiationStepTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationInitiationStepTypeDef"]
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

    applicationID = field("applicationID")
    accountID = field("accountID")

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
class DeleteConnectorRequest:
    boto3_raw_data: "type_defs.DeleteConnectorRequestTypeDef" = dataclasses.field()

    connectorID = field("connectorID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobRequest:
    boto3_raw_data: "type_defs.DeleteJobRequestTypeDef" = dataclasses.field()

    jobID = field("jobID")
    accountID = field("accountID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLaunchConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.DeleteLaunchConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    launchConfigurationTemplateID = field("launchConfigurationTemplateID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLaunchConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLaunchConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.DeleteReplicationConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    replicationConfigurationTemplateID = field("replicationConfigurationTemplateID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteReplicationConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSourceServerRequest:
    boto3_raw_data: "type_defs.DeleteSourceServerRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSourceServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSourceServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVcenterClientRequest:
    boto3_raw_data: "type_defs.DeleteVcenterClientRequestTypeDef" = dataclasses.field()

    vcenterClientID = field("vcenterClientID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVcenterClientRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVcenterClientRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWaveRequest:
    boto3_raw_data: "type_defs.DeleteWaveRequestTypeDef" = dataclasses.field()

    waveID = field("waveID")
    accountID = field("accountID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteWaveRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWaveRequestTypeDef"]
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
class DescribeJobLogItemsRequest:
    boto3_raw_data: "type_defs.DescribeJobLogItemsRequestTypeDef" = dataclasses.field()

    jobID = field("jobID")
    accountID = field("accountID")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobLogItemsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobLogItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobsRequestFilters:
    boto3_raw_data: "type_defs.DescribeJobsRequestFiltersTypeDef" = dataclasses.field()

    fromDate = field("fromDate")
    jobIDs = field("jobIDs")
    toDate = field("toDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsRequestFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLaunchConfigurationTemplatesRequest:
    boto3_raw_data: "type_defs.DescribeLaunchConfigurationTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    launchConfigurationTemplateIDs = field("launchConfigurationTemplateIDs")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLaunchConfigurationTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLaunchConfigurationTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigurationTemplatesRequest:
    boto3_raw_data: (
        "type_defs.DescribeReplicationConfigurationTemplatesRequestTypeDef"
    ) = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    replicationConfigurationTemplateIDs = field("replicationConfigurationTemplateIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigurationTemplatesRequestTypeDef"
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
                "type_defs.DescribeReplicationConfigurationTemplatesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationTemplate:
    boto3_raw_data: "type_defs.ReplicationConfigurationTemplateTypeDef" = (
        dataclasses.field()
    )

    replicationConfigurationTemplateID = field("replicationConfigurationTemplateID")
    arn = field("arn")
    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")
    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    tags = field("tags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")
    useFipsEndpoint = field("useFipsEndpoint")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicationConfigurationTemplateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceServersRequestFilters:
    boto3_raw_data: "type_defs.DescribeSourceServersRequestFiltersTypeDef" = (
        dataclasses.field()
    )

    applicationIDs = field("applicationIDs")
    isArchived = field("isArchived")
    lifeCycleStates = field("lifeCycleStates")
    replicationTypes = field("replicationTypes")
    sourceServerIDs = field("sourceServerIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSourceServersRequestFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceServersRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVcenterClientsRequest:
    boto3_raw_data: "type_defs.DescribeVcenterClientsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeVcenterClientsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVcenterClientsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VcenterClient:
    boto3_raw_data: "type_defs.VcenterClientTypeDef" = dataclasses.field()

    arn = field("arn")
    datacenterName = field("datacenterName")
    hostname = field("hostname")
    lastSeenDatetime = field("lastSeenDatetime")
    sourceServerTags = field("sourceServerTags")
    tags = field("tags")
    vcenterClientID = field("vcenterClientID")
    vcenterUUID = field("vcenterUUID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VcenterClientTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VcenterClientTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateApplicationsRequest:
    boto3_raw_data: "type_defs.DisassociateApplicationsRequestTypeDef" = (
        dataclasses.field()
    )

    applicationIDs = field("applicationIDs")
    waveID = field("waveID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateApplicationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateSourceServersRequest:
    boto3_raw_data: "type_defs.DisassociateSourceServersRequestTypeDef" = (
        dataclasses.field()
    )

    applicationID = field("applicationID")
    sourceServerIDs = field("sourceServerIDs")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateSourceServersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateSourceServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisconnectFromServiceRequest:
    boto3_raw_data: "type_defs.DisconnectFromServiceRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisconnectFromServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisconnectFromServiceRequestTypeDef"]
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

    bytes = field("bytes")
    deviceName = field("deviceName")

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
class ExportErrorData:
    boto3_raw_data: "type_defs.ExportErrorDataTypeDef" = dataclasses.field()

    rawError = field("rawError")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportErrorDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportErrorDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTaskSummary:
    boto3_raw_data: "type_defs.ExportTaskSummaryTypeDef" = dataclasses.field()

    applicationsCount = field("applicationsCount")
    serversCount = field("serversCount")
    wavesCount = field("wavesCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportTaskSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTaskSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FinalizeCutoverRequest:
    boto3_raw_data: "type_defs.FinalizeCutoverRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FinalizeCutoverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FinalizeCutoverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLaunchConfigurationRequest:
    boto3_raw_data: "type_defs.GetLaunchConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLaunchConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLaunchConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.GetReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentificationHints:
    boto3_raw_data: "type_defs.IdentificationHintsTypeDef" = dataclasses.field()

    awsInstanceID = field("awsInstanceID")
    fqdn = field("fqdn")
    hostname = field("hostname")
    vmPath = field("vmPath")
    vmWareUuid = field("vmWareUuid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentificationHintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentificationHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportErrorData:
    boto3_raw_data: "type_defs.ImportErrorDataTypeDef" = dataclasses.field()

    accountID = field("accountID")
    applicationID = field("applicationID")
    ec2LaunchTemplateID = field("ec2LaunchTemplateID")
    rawError = field("rawError")
    rowNumber = field("rowNumber")
    sourceServerID = field("sourceServerID")
    waveID = field("waveID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportErrorDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportErrorDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTaskSummaryApplications:
    boto3_raw_data: "type_defs.ImportTaskSummaryApplicationsTypeDef" = (
        dataclasses.field()
    )

    createdCount = field("createdCount")
    modifiedCount = field("modifiedCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportTaskSummaryApplicationsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTaskSummaryApplicationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTaskSummaryServers:
    boto3_raw_data: "type_defs.ImportTaskSummaryServersTypeDef" = dataclasses.field()

    createdCount = field("createdCount")
    modifiedCount = field("modifiedCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportTaskSummaryServersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTaskSummaryServersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTaskSummaryWaves:
    boto3_raw_data: "type_defs.ImportTaskSummaryWavesTypeDef" = dataclasses.field()

    createdCount = field("createdCount")
    modifiedCount = field("modifiedCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportTaskSummaryWavesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTaskSummaryWavesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketSource:
    boto3_raw_data: "type_defs.S3BucketSourceTypeDef" = dataclasses.field()

    s3Bucket = field("s3Bucket")
    s3Key = field("s3Key")
    s3BucketOwner = field("s3BucketOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3BucketSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3BucketSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobLogEventData:
    boto3_raw_data: "type_defs.JobLogEventDataTypeDef" = dataclasses.field()

    conversionServerID = field("conversionServerID")
    rawError = field("rawError")
    sourceServerID = field("sourceServerID")
    targetInstanceID = field("targetInstanceID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobLogEventDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobLogEventDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchedInstance:
    boto3_raw_data: "type_defs.LaunchedInstanceTypeDef" = dataclasses.field()

    ec2InstanceID = field("ec2InstanceID")
    firstBoot = field("firstBoot")
    jobID = field("jobID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchedInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchedInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastCutoverFinalized:
    boto3_raw_data: "type_defs.LifeCycleLastCutoverFinalizedTypeDef" = (
        dataclasses.field()
    )

    apiCallDateTime = field("apiCallDateTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LifeCycleLastCutoverFinalizedTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastCutoverFinalizedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastCutoverInitiated:
    boto3_raw_data: "type_defs.LifeCycleLastCutoverInitiatedTypeDef" = (
        dataclasses.field()
    )

    apiCallDateTime = field("apiCallDateTime")
    jobID = field("jobID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LifeCycleLastCutoverInitiatedTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastCutoverInitiatedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastCutoverReverted:
    boto3_raw_data: "type_defs.LifeCycleLastCutoverRevertedTypeDef" = (
        dataclasses.field()
    )

    apiCallDateTime = field("apiCallDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifeCycleLastCutoverRevertedTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastCutoverRevertedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastTestFinalized:
    boto3_raw_data: "type_defs.LifeCycleLastTestFinalizedTypeDef" = dataclasses.field()

    apiCallDateTime = field("apiCallDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifeCycleLastTestFinalizedTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastTestFinalizedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastTestInitiated:
    boto3_raw_data: "type_defs.LifeCycleLastTestInitiatedTypeDef" = dataclasses.field()

    apiCallDateTime = field("apiCallDateTime")
    jobID = field("jobID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifeCycleLastTestInitiatedTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastTestInitiatedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastTestReverted:
    boto3_raw_data: "type_defs.LifeCycleLastTestRevertedTypeDef" = dataclasses.field()

    apiCallDateTime = field("apiCallDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifeCycleLastTestRevertedTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastTestRevertedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequestFilters:
    boto3_raw_data: "type_defs.ListApplicationsRequestFiltersTypeDef" = (
        dataclasses.field()
    )

    applicationIDs = field("applicationIDs")
    isArchived = field("isArchived")
    waveIDs = field("waveIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestFiltersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorsRequestFilters:
    boto3_raw_data: "type_defs.ListConnectorsRequestFiltersTypeDef" = (
        dataclasses.field()
    )

    connectorIDs = field("connectorIDs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorsRequestFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportErrorsRequest:
    boto3_raw_data: "type_defs.ListExportErrorsRequestTypeDef" = dataclasses.field()

    exportID = field("exportID")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportErrorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportErrorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsRequestFilters:
    boto3_raw_data: "type_defs.ListExportsRequestFiltersTypeDef" = dataclasses.field()

    exportIDs = field("exportIDs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportsRequestFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportErrorsRequest:
    boto3_raw_data: "type_defs.ListImportErrorsRequestTypeDef" = dataclasses.field()

    importID = field("importID")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportErrorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportErrorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsRequestFilters:
    boto3_raw_data: "type_defs.ListImportsRequestFiltersTypeDef" = dataclasses.field()

    importIDs = field("importIDs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsRequestFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedAccountsRequest:
    boto3_raw_data: "type_defs.ListManagedAccountsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedAccountsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedAccount:
    boto3_raw_data: "type_defs.ManagedAccountTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedAccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManagedAccountTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceServerActionsRequestFilters:
    boto3_raw_data: "type_defs.SourceServerActionsRequestFiltersTypeDef" = (
        dataclasses.field()
    )

    actionIDs = field("actionIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SourceServerActionsRequestFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceServerActionsRequestFiltersTypeDef"]
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

    resourceArn = field("resourceArn")

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
class TemplateActionsRequestFilters:
    boto3_raw_data: "type_defs.TemplateActionsRequestFiltersTypeDef" = (
        dataclasses.field()
    )

    actionIDs = field("actionIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TemplateActionsRequestFiltersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateActionsRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWavesRequestFilters:
    boto3_raw_data: "type_defs.ListWavesRequestFiltersTypeDef" = dataclasses.field()

    isArchived = field("isArchived")
    waveIDs = field("waveIDs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWavesRequestFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWavesRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarkAsArchivedRequest:
    boto3_raw_data: "type_defs.MarkAsArchivedRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MarkAsArchivedRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MarkAsArchivedRequestTypeDef"]
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

    ips = field("ips")
    isPrimary = field("isPrimary")
    macAddress = field("macAddress")

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
class OS:
    boto3_raw_data: "type_defs.OSTypeDef" = dataclasses.field()

    fullString = field("fullString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OSTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OSTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseReplicationRequest:
    boto3_raw_data: "type_defs.PauseReplicationRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PauseReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SsmExternalParameter:
    boto3_raw_data: "type_defs.SsmExternalParameterTypeDef" = dataclasses.field()

    dynamicPath = field("dynamicPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SsmExternalParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SsmExternalParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SsmParameterStoreParameter:
    boto3_raw_data: "type_defs.SsmParameterStoreParameterTypeDef" = dataclasses.field()

    parameterName = field("parameterName")
    parameterType = field("parameterType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SsmParameterStoreParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SsmParameterStoreParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveSourceServerActionRequest:
    boto3_raw_data: "type_defs.RemoveSourceServerActionRequestTypeDef" = (
        dataclasses.field()
    )

    actionID = field("actionID")
    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveSourceServerActionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveSourceServerActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTemplateActionRequest:
    boto3_raw_data: "type_defs.RemoveTemplateActionRequestTypeDef" = dataclasses.field()

    actionID = field("actionID")
    launchConfigurationTemplateID = field("launchConfigurationTemplateID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveTemplateActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTemplateActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationReplicatedDisk:
    boto3_raw_data: "type_defs.ReplicationConfigurationReplicatedDiskTypeDef" = (
        dataclasses.field()
    )

    deviceName = field("deviceName")
    iops = field("iops")
    isBootDisk = field("isBootDisk")
    stagingDiskType = field("stagingDiskType")
    throughput = field("throughput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationConfigurationReplicatedDiskTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationReplicatedDiskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeReplicationRequest:
    boto3_raw_data: "type_defs.ResumeReplicationRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryDataReplicationRequest:
    boto3_raw_data: "type_defs.RetryDataReplicationRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryDataReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryDataReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceServerConnectorAction:
    boto3_raw_data: "type_defs.SourceServerConnectorActionTypeDef" = dataclasses.field()

    connectorArn = field("connectorArn")
    credentialsSecretArn = field("credentialsSecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceServerConnectorActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceServerConnectorActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCutoverRequest:
    boto3_raw_data: "type_defs.StartCutoverRequestTypeDef" = dataclasses.field()

    sourceServerIDs = field("sourceServerIDs")
    accountID = field("accountID")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCutoverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCutoverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExportRequest:
    boto3_raw_data: "type_defs.StartExportRequestTypeDef" = dataclasses.field()

    s3Bucket = field("s3Bucket")
    s3Key = field("s3Key")
    s3BucketOwner = field("s3BucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationRequest:
    boto3_raw_data: "type_defs.StartReplicationRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTestRequest:
    boto3_raw_data: "type_defs.StartTestRequestTypeDef" = dataclasses.field()

    sourceServerIDs = field("sourceServerIDs")
    accountID = field("accountID")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartTestRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopReplicationRequest:
    boto3_raw_data: "type_defs.StopReplicationRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopReplicationRequestTypeDef"]
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

    resourceArn = field("resourceArn")
    tags = field("tags")

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
class TerminateTargetInstancesRequest:
    boto3_raw_data: "type_defs.TerminateTargetInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerIDs = field("sourceServerIDs")
    accountID = field("accountID")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TerminateTargetInstancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateTargetInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnarchiveApplicationRequest:
    boto3_raw_data: "type_defs.UnarchiveApplicationRequestTypeDef" = dataclasses.field()

    applicationID = field("applicationID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnarchiveApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnarchiveApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnarchiveWaveRequest:
    boto3_raw_data: "type_defs.UnarchiveWaveRequestTypeDef" = dataclasses.field()

    waveID = field("waveID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnarchiveWaveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnarchiveWaveRequestTypeDef"]
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

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    applicationID = field("applicationID")
    accountID = field("accountID")
    description = field("description")
    name = field("name")

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


@dataclasses.dataclass(frozen=True)
class UpdateReplicationConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.UpdateReplicationConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    replicationConfigurationTemplateID = field("replicationConfigurationTemplateID")
    arn = field("arn")
    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")
    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")
    useFipsEndpoint = field("useFipsEndpoint")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateReplicationConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReplicationConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSourceServerReplicationTypeRequest:
    boto3_raw_data: "type_defs.UpdateSourceServerReplicationTypeRequestTypeDef" = (
        dataclasses.field()
    )

    replicationType = field("replicationType")
    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSourceServerReplicationTypeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSourceServerReplicationTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWaveRequest:
    boto3_raw_data: "type_defs.UpdateWaveRequestTypeDef" = dataclasses.field()

    waveID = field("waveID")
    accountID = field("accountID")
    description = field("description")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateWaveRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWaveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaveAggregatedStatus:
    boto3_raw_data: "type_defs.WaveAggregatedStatusTypeDef" = dataclasses.field()

    healthStatus = field("healthStatus")
    lastUpdateDateTime = field("lastUpdateDateTime")
    progressStatus = field("progressStatus")
    replicationStartedDateTime = field("replicationStartedDateTime")
    totalApplications = field("totalApplications")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WaveAggregatedStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaveAggregatedStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Application:
    boto3_raw_data: "type_defs.ApplicationTypeDef" = dataclasses.field()

    @cached_property
    def applicationAggregatedStatus(self):  # pragma: no cover
        return ApplicationAggregatedStatus.make_one(
            self.boto3_raw_data["applicationAggregatedStatus"]
        )

    applicationID = field("applicationID")
    arn = field("arn")
    creationDateTime = field("creationDateTime")
    description = field("description")
    isArchived = field("isArchived")
    lastModifiedDateTime = field("lastModifiedDateTime")
    name = field("name")
    tags = field("tags")
    waveID = field("waveID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApplicationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationResponse:
    boto3_raw_data: "type_defs.ApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def applicationAggregatedStatus(self):  # pragma: no cover
        return ApplicationAggregatedStatus.make_one(
            self.boto3_raw_data["applicationAggregatedStatus"]
        )

    applicationID = field("applicationID")
    arn = field("arn")
    creationDateTime = field("creationDateTime")
    description = field("description")
    isArchived = field("isArchived")
    lastModifiedDateTime = field("lastModifiedDateTime")
    name = field("name")
    tags = field("tags")
    waveID = field("waveID")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
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

    tags = field("tags")

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
class ReplicationConfigurationTemplateResponse:
    boto3_raw_data: "type_defs.ReplicationConfigurationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")
    replicationConfigurationTemplateID = field("replicationConfigurationTemplateID")
    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    tags = field("tags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")
    useFipsEndpoint = field("useFipsEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationConfigurationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeServerLifeCycleStateRequest:
    boto3_raw_data: "type_defs.ChangeServerLifeCycleStateRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lifeCycle(self):  # pragma: no cover
        return ChangeServerLifeCycleStateSourceServerLifecycle.make_one(
            self.boto3_raw_data["lifeCycle"]
        )

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangeServerLifeCycleStateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeServerLifeCycleStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorResponse:
    boto3_raw_data: "type_defs.ConnectorResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    connectorID = field("connectorID")
    name = field("name")

    @cached_property
    def ssmCommandConfig(self):  # pragma: no cover
        return ConnectorSsmCommandConfig.make_one(
            self.boto3_raw_data["ssmCommandConfig"]
        )

    ssmInstanceID = field("ssmInstanceID")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Connector:
    boto3_raw_data: "type_defs.ConnectorTypeDef" = dataclasses.field()

    arn = field("arn")
    connectorID = field("connectorID")
    name = field("name")

    @cached_property
    def ssmCommandConfig(self):  # pragma: no cover
        return ConnectorSsmCommandConfig.make_one(
            self.boto3_raw_data["ssmCommandConfig"]
        )

    ssmInstanceID = field("ssmInstanceID")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorRequest:
    boto3_raw_data: "type_defs.CreateConnectorRequestTypeDef" = dataclasses.field()

    name = field("name")
    ssmInstanceID = field("ssmInstanceID")

    @cached_property
    def ssmCommandConfig(self):  # pragma: no cover
        return ConnectorSsmCommandConfig.make_one(
            self.boto3_raw_data["ssmCommandConfig"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectorRequest:
    boto3_raw_data: "type_defs.UpdateConnectorRequestTypeDef" = dataclasses.field()

    connectorID = field("connectorID")
    name = field("name")

    @cached_property
    def ssmCommandConfig(self):  # pragma: no cover
        return ConnectorSsmCommandConfig.make_one(
            self.boto3_raw_data["ssmCommandConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationInitiation:
    boto3_raw_data: "type_defs.DataReplicationInitiationTypeDef" = dataclasses.field()

    nextAttemptDateTime = field("nextAttemptDateTime")
    startDateTime = field("startDateTime")

    @cached_property
    def steps(self):  # pragma: no cover
        return DataReplicationInitiationStep.make_many(self.boto3_raw_data["steps"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataReplicationInitiationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationInitiationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobLogItemsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeJobLogItemsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    jobID = field("jobID")
    accountID = field("accountID")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeJobLogItemsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobLogItemsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLaunchConfigurationTemplatesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef"
    ) = dataclasses.field()

    launchConfigurationTemplateIDs = field("launchConfigurationTemplateIDs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef"
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
                "type_defs.DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigurationTemplatesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef"
    ) = dataclasses.field()

    replicationConfigurationTemplateIDs = field("replicationConfigurationTemplateIDs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef"
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
                "type_defs.DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVcenterClientsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeVcenterClientsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVcenterClientsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVcenterClientsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportErrorsRequestPaginate:
    boto3_raw_data: "type_defs.ListExportErrorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    exportID = field("exportID")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExportErrorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportErrorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportErrorsRequestPaginate:
    boto3_raw_data: "type_defs.ListImportErrorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    importID = field("importID")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImportErrorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportErrorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListManagedAccountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedAccountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedAccountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeJobsRequestPaginateTypeDef" = dataclasses.field()

    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeJobsRequestFilters.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobsRequest:
    boto3_raw_data: "type_defs.DescribeJobsRequestTypeDef" = dataclasses.field()

    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeJobsRequestFilters.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigurationTemplatesResponse:
    boto3_raw_data: (
        "type_defs.DescribeReplicationConfigurationTemplatesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ReplicationConfigurationTemplate.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigurationTemplatesResponseTypeDef"
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
                "type_defs.DescribeReplicationConfigurationTemplatesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceServersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSourceServersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeSourceServersRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSourceServersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceServersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceServersRequest:
    boto3_raw_data: "type_defs.DescribeSourceServersRequestTypeDef" = (
        dataclasses.field()
    )

    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeSourceServersRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSourceServersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVcenterClientsResponse:
    boto3_raw_data: "type_defs.DescribeVcenterClientsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return VcenterClient.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeVcenterClientsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVcenterClientsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTaskError:
    boto3_raw_data: "type_defs.ExportTaskErrorTypeDef" = dataclasses.field()

    @cached_property
    def errorData(self):  # pragma: no cover
        return ExportErrorData.make_one(self.boto3_raw_data["errorData"])

    errorDateTime = field("errorDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportTaskErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportTaskErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTask:
    boto3_raw_data: "type_defs.ExportTaskTypeDef" = dataclasses.field()

    creationDateTime = field("creationDateTime")
    endDateTime = field("endDateTime")
    exportID = field("exportID")
    progressPercentage = field("progressPercentage")
    s3Bucket = field("s3Bucket")
    s3BucketOwner = field("s3BucketOwner")
    s3Key = field("s3Key")
    status = field("status")

    @cached_property
    def summary(self):  # pragma: no cover
        return ExportTaskSummary.make_one(self.boto3_raw_data["summary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportTaskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTaskError:
    boto3_raw_data: "type_defs.ImportTaskErrorTypeDef" = dataclasses.field()

    @cached_property
    def errorData(self):  # pragma: no cover
        return ImportErrorData.make_one(self.boto3_raw_data["errorData"])

    errorDateTime = field("errorDateTime")
    errorType = field("errorType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportTaskErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportTaskErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTaskSummary:
    boto3_raw_data: "type_defs.ImportTaskSummaryTypeDef" = dataclasses.field()

    @cached_property
    def applications(self):  # pragma: no cover
        return ImportTaskSummaryApplications.make_one(
            self.boto3_raw_data["applications"]
        )

    @cached_property
    def servers(self):  # pragma: no cover
        return ImportTaskSummaryServers.make_one(self.boto3_raw_data["servers"])

    @cached_property
    def waves(self):  # pragma: no cover
        return ImportTaskSummaryWaves.make_one(self.boto3_raw_data["waves"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportTaskSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTaskSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportRequest:
    boto3_raw_data: "type_defs.StartImportRequestTypeDef" = dataclasses.field()

    @cached_property
    def s3BucketSource(self):  # pragma: no cover
        return S3BucketSource.make_one(self.boto3_raw_data["s3BucketSource"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobLog:
    boto3_raw_data: "type_defs.JobLogTypeDef" = dataclasses.field()

    event = field("event")

    @cached_property
    def eventData(self):  # pragma: no cover
        return JobLogEventData.make_one(self.boto3_raw_data["eventData"])

    logDateTime = field("logDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobLogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobLogTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastCutover:
    boto3_raw_data: "type_defs.LifeCycleLastCutoverTypeDef" = dataclasses.field()

    @cached_property
    def finalized(self):  # pragma: no cover
        return LifeCycleLastCutoverFinalized.make_one(self.boto3_raw_data["finalized"])

    @cached_property
    def initiated(self):  # pragma: no cover
        return LifeCycleLastCutoverInitiated.make_one(self.boto3_raw_data["initiated"])

    @cached_property
    def reverted(self):  # pragma: no cover
        return LifeCycleLastCutoverReverted.make_one(self.boto3_raw_data["reverted"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifeCycleLastCutoverTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastCutoverTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastTest:
    boto3_raw_data: "type_defs.LifeCycleLastTestTypeDef" = dataclasses.field()

    @cached_property
    def finalized(self):  # pragma: no cover
        return LifeCycleLastTestFinalized.make_one(self.boto3_raw_data["finalized"])

    @cached_property
    def initiated(self):  # pragma: no cover
        return LifeCycleLastTestInitiated.make_one(self.boto3_raw_data["initiated"])

    @cached_property
    def reverted(self):  # pragma: no cover
        return LifeCycleLastTestReverted.make_one(self.boto3_raw_data["reverted"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifeCycleLastTestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastTestTypeDef"]
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

    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListApplicationsRequestFilters.make_one(self.boto3_raw_data["filters"])

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
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListApplicationsRequestFilters.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

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
class ListConnectorsRequestPaginate:
    boto3_raw_data: "type_defs.ListConnectorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return ListConnectorsRequestFilters.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConnectorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorsRequest:
    boto3_raw_data: "type_defs.ListConnectorsRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return ListConnectorsRequestFilters.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsRequestPaginate:
    boto3_raw_data: "type_defs.ListExportsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return ListExportsRequestFilters.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsRequest:
    boto3_raw_data: "type_defs.ListExportsRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return ListExportsRequestFilters.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsRequestPaginate:
    boto3_raw_data: "type_defs.ListImportsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return ListImportsRequestFilters.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsRequest:
    boto3_raw_data: "type_defs.ListImportsRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return ListImportsRequestFilters.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedAccountsResponse:
    boto3_raw_data: "type_defs.ListManagedAccountsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ManagedAccount.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedAccountsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceServerActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSourceServerActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return SourceServerActionsRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSourceServerActionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceServerActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceServerActionsRequest:
    boto3_raw_data: "type_defs.ListSourceServerActionsRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return SourceServerActionsRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSourceServerActionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceServerActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListTemplateActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    launchConfigurationTemplateID = field("launchConfigurationTemplateID")

    @cached_property
    def filters(self):  # pragma: no cover
        return TemplateActionsRequestFilters.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTemplateActionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateActionsRequest:
    boto3_raw_data: "type_defs.ListTemplateActionsRequestTypeDef" = dataclasses.field()

    launchConfigurationTemplateID = field("launchConfigurationTemplateID")

    @cached_property
    def filters(self):  # pragma: no cover
        return TemplateActionsRequestFilters.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplateActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWavesRequestPaginate:
    boto3_raw_data: "type_defs.ListWavesRequestPaginateTypeDef" = dataclasses.field()

    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListWavesRequestFilters.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWavesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWavesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWavesRequest:
    boto3_raw_data: "type_defs.ListWavesRequestTypeDef" = dataclasses.field()

    accountID = field("accountID")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListWavesRequestFilters.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListWavesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWavesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceProperties:
    boto3_raw_data: "type_defs.SourcePropertiesTypeDef" = dataclasses.field()

    @cached_property
    def cpus(self):  # pragma: no cover
        return CPU.make_many(self.boto3_raw_data["cpus"])

    @cached_property
    def disks(self):  # pragma: no cover
        return Disk.make_many(self.boto3_raw_data["disks"])

    @cached_property
    def identificationHints(self):  # pragma: no cover
        return IdentificationHints.make_one(self.boto3_raw_data["identificationHints"])

    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @cached_property
    def os(self):  # pragma: no cover
        return OS.make_one(self.boto3_raw_data["os"])

    ramBytes = field("ramBytes")
    recommendedInstanceType = field("recommendedInstanceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourcePropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSourceServerActionRequest:
    boto3_raw_data: "type_defs.PutSourceServerActionRequestTypeDef" = (
        dataclasses.field()
    )

    actionID = field("actionID")
    actionName = field("actionName")
    documentIdentifier = field("documentIdentifier")
    order = field("order")
    sourceServerID = field("sourceServerID")
    accountID = field("accountID")
    active = field("active")
    category = field("category")
    description = field("description")
    documentVersion = field("documentVersion")
    externalParameters = field("externalParameters")
    mustSucceedForCutover = field("mustSucceedForCutover")
    parameters = field("parameters")
    timeoutSeconds = field("timeoutSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSourceServerActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSourceServerActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTemplateActionRequest:
    boto3_raw_data: "type_defs.PutTemplateActionRequestTypeDef" = dataclasses.field()

    actionID = field("actionID")
    actionName = field("actionName")
    documentIdentifier = field("documentIdentifier")
    launchConfigurationTemplateID = field("launchConfigurationTemplateID")
    order = field("order")
    active = field("active")
    category = field("category")
    description = field("description")
    documentVersion = field("documentVersion")
    externalParameters = field("externalParameters")
    mustSucceedForCutover = field("mustSucceedForCutover")
    operatingSystem = field("operatingSystem")
    parameters = field("parameters")
    timeoutSeconds = field("timeoutSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTemplateActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTemplateActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceServerActionDocumentResponse:
    boto3_raw_data: "type_defs.SourceServerActionDocumentResponseTypeDef" = (
        dataclasses.field()
    )

    actionID = field("actionID")
    actionName = field("actionName")
    active = field("active")
    category = field("category")
    description = field("description")
    documentIdentifier = field("documentIdentifier")
    documentVersion = field("documentVersion")
    externalParameters = field("externalParameters")
    mustSucceedForCutover = field("mustSucceedForCutover")
    order = field("order")
    parameters = field("parameters")
    timeoutSeconds = field("timeoutSeconds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SourceServerActionDocumentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceServerActionDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceServerActionDocument:
    boto3_raw_data: "type_defs.SourceServerActionDocumentTypeDef" = dataclasses.field()

    actionID = field("actionID")
    actionName = field("actionName")
    active = field("active")
    category = field("category")
    description = field("description")
    documentIdentifier = field("documentIdentifier")
    documentVersion = field("documentVersion")
    externalParameters = field("externalParameters")
    mustSucceedForCutover = field("mustSucceedForCutover")
    order = field("order")
    parameters = field("parameters")
    timeoutSeconds = field("timeoutSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceServerActionDocumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceServerActionDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SsmDocumentOutput:
    boto3_raw_data: "type_defs.SsmDocumentOutputTypeDef" = dataclasses.field()

    actionName = field("actionName")
    ssmDocumentName = field("ssmDocumentName")
    externalParameters = field("externalParameters")
    mustSucceedForCutover = field("mustSucceedForCutover")
    parameters = field("parameters")
    timeoutSeconds = field("timeoutSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SsmDocumentOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SsmDocumentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SsmDocument:
    boto3_raw_data: "type_defs.SsmDocumentTypeDef" = dataclasses.field()

    actionName = field("actionName")
    ssmDocumentName = field("ssmDocumentName")
    externalParameters = field("externalParameters")
    mustSucceedForCutover = field("mustSucceedForCutover")
    parameters = field("parameters")
    timeoutSeconds = field("timeoutSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SsmDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SsmDocumentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateActionDocumentResponse:
    boto3_raw_data: "type_defs.TemplateActionDocumentResponseTypeDef" = (
        dataclasses.field()
    )

    actionID = field("actionID")
    actionName = field("actionName")
    active = field("active")
    category = field("category")
    description = field("description")
    documentIdentifier = field("documentIdentifier")
    documentVersion = field("documentVersion")
    externalParameters = field("externalParameters")
    mustSucceedForCutover = field("mustSucceedForCutover")
    operatingSystem = field("operatingSystem")
    order = field("order")
    parameters = field("parameters")
    timeoutSeconds = field("timeoutSeconds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TemplateActionDocumentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateActionDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateActionDocument:
    boto3_raw_data: "type_defs.TemplateActionDocumentTypeDef" = dataclasses.field()

    actionID = field("actionID")
    actionName = field("actionName")
    active = field("active")
    category = field("category")
    description = field("description")
    documentIdentifier = field("documentIdentifier")
    documentVersion = field("documentVersion")
    externalParameters = field("externalParameters")
    mustSucceedForCutover = field("mustSucceedForCutover")
    operatingSystem = field("operatingSystem")
    order = field("order")
    parameters = field("parameters")
    timeoutSeconds = field("timeoutSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateActionDocumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateActionDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfiguration:
    boto3_raw_data: "type_defs.ReplicationConfigurationTypeDef" = dataclasses.field()

    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")
    name = field("name")

    @cached_property
    def replicatedDisks(self):  # pragma: no cover
        return ReplicationConfigurationReplicatedDisk.make_many(
            self.boto3_raw_data["replicatedDisks"]
        )

    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    sourceServerID = field("sourceServerID")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")
    useFipsEndpoint = field("useFipsEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")
    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")
    name = field("name")

    @cached_property
    def replicatedDisks(self):  # pragma: no cover
        return ReplicationConfigurationReplicatedDisk.make_many(
            self.boto3_raw_data["replicatedDisks"]
        )

    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")
    useFipsEndpoint = field("useFipsEndpoint")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSourceServerRequest:
    boto3_raw_data: "type_defs.UpdateSourceServerRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")

    @cached_property
    def connectorAction(self):  # pragma: no cover
        return SourceServerConnectorAction.make_one(
            self.boto3_raw_data["connectorAction"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSourceServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSourceServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaveResponse:
    boto3_raw_data: "type_defs.WaveResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    creationDateTime = field("creationDateTime")
    description = field("description")
    isArchived = field("isArchived")
    lastModifiedDateTime = field("lastModifiedDateTime")
    name = field("name")
    tags = field("tags")

    @cached_property
    def waveAggregatedStatus(self):  # pragma: no cover
        return WaveAggregatedStatus.make_one(
            self.boto3_raw_data["waveAggregatedStatus"]
        )

    waveID = field("waveID")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaveResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaveResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Wave:
    boto3_raw_data: "type_defs.WaveTypeDef" = dataclasses.field()

    arn = field("arn")
    creationDateTime = field("creationDateTime")
    description = field("description")
    isArchived = field("isArchived")
    lastModifiedDateTime = field("lastModifiedDateTime")
    name = field("name")
    tags = field("tags")

    @cached_property
    def waveAggregatedStatus(self):  # pragma: no cover
        return WaveAggregatedStatus.make_one(
            self.boto3_raw_data["waveAggregatedStatus"]
        )

    waveID = field("waveID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaveTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaveTypeDef"]]
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
    def items(self):  # pragma: no cover
        return Application.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

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
class ListConnectorsResponse:
    boto3_raw_data: "type_defs.ListConnectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return Connector.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationInfo:
    boto3_raw_data: "type_defs.DataReplicationInfoTypeDef" = dataclasses.field()

    @cached_property
    def dataReplicationError(self):  # pragma: no cover
        return DataReplicationError.make_one(
            self.boto3_raw_data["dataReplicationError"]
        )

    @cached_property
    def dataReplicationInitiation(self):  # pragma: no cover
        return DataReplicationInitiation.make_one(
            self.boto3_raw_data["dataReplicationInitiation"]
        )

    dataReplicationState = field("dataReplicationState")
    etaDateTime = field("etaDateTime")
    lagDuration = field("lagDuration")
    lastSnapshotDateTime = field("lastSnapshotDateTime")

    @cached_property
    def replicatedDisks(self):  # pragma: no cover
        return DataReplicationInfoReplicatedDisk.make_many(
            self.boto3_raw_data["replicatedDisks"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataReplicationInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportErrorsResponse:
    boto3_raw_data: "type_defs.ListExportErrorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ExportTaskError.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportErrorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportErrorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsResponse:
    boto3_raw_data: "type_defs.ListExportsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ExportTask.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExportResponse:
    boto3_raw_data: "type_defs.StartExportResponseTypeDef" = dataclasses.field()

    @cached_property
    def exportTask(self):  # pragma: no cover
        return ExportTask.make_one(self.boto3_raw_data["exportTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportErrorsResponse:
    boto3_raw_data: "type_defs.ListImportErrorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ImportTaskError.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportErrorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportErrorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTask:
    boto3_raw_data: "type_defs.ImportTaskTypeDef" = dataclasses.field()

    creationDateTime = field("creationDateTime")
    endDateTime = field("endDateTime")
    importID = field("importID")
    progressPercentage = field("progressPercentage")

    @cached_property
    def s3BucketSource(self):  # pragma: no cover
        return S3BucketSource.make_one(self.boto3_raw_data["s3BucketSource"])

    status = field("status")

    @cached_property
    def summary(self):  # pragma: no cover
        return ImportTaskSummary.make_one(self.boto3_raw_data["summary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportTaskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobLogItemsResponse:
    boto3_raw_data: "type_defs.DescribeJobLogItemsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return JobLog.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobLogItemsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobLogItemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycle:
    boto3_raw_data: "type_defs.LifeCycleTypeDef" = dataclasses.field()

    addedToServiceDateTime = field("addedToServiceDateTime")
    elapsedReplicationDuration = field("elapsedReplicationDuration")
    firstByteDateTime = field("firstByteDateTime")

    @cached_property
    def lastCutover(self):  # pragma: no cover
        return LifeCycleLastCutover.make_one(self.boto3_raw_data["lastCutover"])

    lastSeenByServiceDateTime = field("lastSeenByServiceDateTime")

    @cached_property
    def lastTest(self):  # pragma: no cover
        return LifeCycleLastTest.make_one(self.boto3_raw_data["lastTest"])

    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifeCycleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifeCycleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceServerActionsResponse:
    boto3_raw_data: "type_defs.ListSourceServerActionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return SourceServerActionDocument.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSourceServerActionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceServerActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobPostLaunchActionsLaunchStatus:
    boto3_raw_data: "type_defs.JobPostLaunchActionsLaunchStatusTypeDef" = (
        dataclasses.field()
    )

    executionID = field("executionID")
    executionStatus = field("executionStatus")
    failureReason = field("failureReason")

    @cached_property
    def ssmDocument(self):  # pragma: no cover
        return SsmDocumentOutput.make_one(self.boto3_raw_data["ssmDocument"])

    ssmDocumentType = field("ssmDocumentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.JobPostLaunchActionsLaunchStatusTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobPostLaunchActionsLaunchStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostLaunchActionsOutput:
    boto3_raw_data: "type_defs.PostLaunchActionsOutputTypeDef" = dataclasses.field()

    cloudWatchLogGroupName = field("cloudWatchLogGroupName")
    deployment = field("deployment")
    s3LogBucket = field("s3LogBucket")
    s3OutputKeyPrefix = field("s3OutputKeyPrefix")

    @cached_property
    def ssmDocuments(self):  # pragma: no cover
        return SsmDocumentOutput.make_many(self.boto3_raw_data["ssmDocuments"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostLaunchActionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostLaunchActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostLaunchActions:
    boto3_raw_data: "type_defs.PostLaunchActionsTypeDef" = dataclasses.field()

    cloudWatchLogGroupName = field("cloudWatchLogGroupName")
    deployment = field("deployment")
    s3LogBucket = field("s3LogBucket")
    s3OutputKeyPrefix = field("s3OutputKeyPrefix")

    @cached_property
    def ssmDocuments(self):  # pragma: no cover
        return SsmDocument.make_many(self.boto3_raw_data["ssmDocuments"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PostLaunchActionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostLaunchActionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateActionsResponse:
    boto3_raw_data: "type_defs.ListTemplateActionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return TemplateActionDocument.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplateActionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWavesResponse:
    boto3_raw_data: "type_defs.ListWavesResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return Wave.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListWavesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWavesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsResponse:
    boto3_raw_data: "type_defs.ListImportsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ImportTask.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportResponse:
    boto3_raw_data: "type_defs.StartImportResponseTypeDef" = dataclasses.field()

    @cached_property
    def importTask(self):  # pragma: no cover
        return ImportTask.make_one(self.boto3_raw_data["importTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceServerResponse:
    boto3_raw_data: "type_defs.SourceServerResponseTypeDef" = dataclasses.field()

    applicationID = field("applicationID")
    arn = field("arn")

    @cached_property
    def connectorAction(self):  # pragma: no cover
        return SourceServerConnectorAction.make_one(
            self.boto3_raw_data["connectorAction"]
        )

    @cached_property
    def dataReplicationInfo(self):  # pragma: no cover
        return DataReplicationInfo.make_one(self.boto3_raw_data["dataReplicationInfo"])

    fqdnForActionFramework = field("fqdnForActionFramework")
    isArchived = field("isArchived")

    @cached_property
    def launchedInstance(self):  # pragma: no cover
        return LaunchedInstance.make_one(self.boto3_raw_data["launchedInstance"])

    @cached_property
    def lifeCycle(self):  # pragma: no cover
        return LifeCycle.make_one(self.boto3_raw_data["lifeCycle"])

    replicationType = field("replicationType")

    @cached_property
    def sourceProperties(self):  # pragma: no cover
        return SourceProperties.make_one(self.boto3_raw_data["sourceProperties"])

    sourceServerID = field("sourceServerID")
    tags = field("tags")
    userProvidedID = field("userProvidedID")
    vcenterClientID = field("vcenterClientID")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceServerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceServerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceServer:
    boto3_raw_data: "type_defs.SourceServerTypeDef" = dataclasses.field()

    applicationID = field("applicationID")
    arn = field("arn")

    @cached_property
    def connectorAction(self):  # pragma: no cover
        return SourceServerConnectorAction.make_one(
            self.boto3_raw_data["connectorAction"]
        )

    @cached_property
    def dataReplicationInfo(self):  # pragma: no cover
        return DataReplicationInfo.make_one(self.boto3_raw_data["dataReplicationInfo"])

    fqdnForActionFramework = field("fqdnForActionFramework")
    isArchived = field("isArchived")

    @cached_property
    def launchedInstance(self):  # pragma: no cover
        return LaunchedInstance.make_one(self.boto3_raw_data["launchedInstance"])

    @cached_property
    def lifeCycle(self):  # pragma: no cover
        return LifeCycle.make_one(self.boto3_raw_data["lifeCycle"])

    replicationType = field("replicationType")

    @cached_property
    def sourceProperties(self):  # pragma: no cover
        return SourceProperties.make_one(self.boto3_raw_data["sourceProperties"])

    sourceServerID = field("sourceServerID")
    tags = field("tags")
    userProvidedID = field("userProvidedID")
    vcenterClientID = field("vcenterClientID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceServerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostLaunchActionsStatus:
    boto3_raw_data: "type_defs.PostLaunchActionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def postLaunchActionsLaunchStatusList(self):  # pragma: no cover
        return JobPostLaunchActionsLaunchStatus.make_many(
            self.boto3_raw_data["postLaunchActionsLaunchStatusList"]
        )

    ssmAgentDiscoveryDatetime = field("ssmAgentDiscoveryDatetime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostLaunchActionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostLaunchActionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfigurationTemplateResponse:
    boto3_raw_data: "type_defs.LaunchConfigurationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    associatePublicIpAddress = field("associatePublicIpAddress")
    bootMode = field("bootMode")
    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    ec2LaunchTemplateID = field("ec2LaunchTemplateID")
    enableMapAutoTagging = field("enableMapAutoTagging")

    @cached_property
    def largeVolumeConf(self):  # pragma: no cover
        return LaunchTemplateDiskConf.make_one(self.boto3_raw_data["largeVolumeConf"])

    launchConfigurationTemplateID = field("launchConfigurationTemplateID")
    launchDisposition = field("launchDisposition")

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    mapAutoTaggingMpeID = field("mapAutoTaggingMpeID")

    @cached_property
    def postLaunchActions(self):  # pragma: no cover
        return PostLaunchActionsOutput.make_one(
            self.boto3_raw_data["postLaunchActions"]
        )

    @cached_property
    def smallVolumeConf(self):  # pragma: no cover
        return LaunchTemplateDiskConf.make_one(self.boto3_raw_data["smallVolumeConf"])

    smallVolumeMaxSize = field("smallVolumeMaxSize")
    tags = field("tags")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LaunchConfigurationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfigurationTemplate:
    boto3_raw_data: "type_defs.LaunchConfigurationTemplateTypeDef" = dataclasses.field()

    launchConfigurationTemplateID = field("launchConfigurationTemplateID")
    arn = field("arn")
    associatePublicIpAddress = field("associatePublicIpAddress")
    bootMode = field("bootMode")
    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    ec2LaunchTemplateID = field("ec2LaunchTemplateID")
    enableMapAutoTagging = field("enableMapAutoTagging")

    @cached_property
    def largeVolumeConf(self):  # pragma: no cover
        return LaunchTemplateDiskConf.make_one(self.boto3_raw_data["largeVolumeConf"])

    launchDisposition = field("launchDisposition")

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    mapAutoTaggingMpeID = field("mapAutoTaggingMpeID")

    @cached_property
    def postLaunchActions(self):  # pragma: no cover
        return PostLaunchActionsOutput.make_one(
            self.boto3_raw_data["postLaunchActions"]
        )

    @cached_property
    def smallVolumeConf(self):  # pragma: no cover
        return LaunchTemplateDiskConf.make_one(self.boto3_raw_data["smallVolumeConf"])

    smallVolumeMaxSize = field("smallVolumeMaxSize")
    tags = field("tags")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigurationTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfiguration:
    boto3_raw_data: "type_defs.LaunchConfigurationTypeDef" = dataclasses.field()

    bootMode = field("bootMode")
    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    ec2LaunchTemplateID = field("ec2LaunchTemplateID")
    enableMapAutoTagging = field("enableMapAutoTagging")
    launchDisposition = field("launchDisposition")

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    mapAutoTaggingMpeID = field("mapAutoTaggingMpeID")
    name = field("name")

    @cached_property
    def postLaunchActions(self):  # pragma: no cover
        return PostLaunchActionsOutput.make_one(
            self.boto3_raw_data["postLaunchActions"]
        )

    sourceServerID = field("sourceServerID")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceServersResponse:
    boto3_raw_data: "type_defs.DescribeSourceServersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return SourceServer.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSourceServersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceServersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipatingServer:
    boto3_raw_data: "type_defs.ParticipatingServerTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")
    launchStatus = field("launchStatus")
    launchedEc2InstanceID = field("launchedEc2InstanceID")

    @cached_property
    def postLaunchActionsStatus(self):  # pragma: no cover
        return PostLaunchActionsStatus.make_one(
            self.boto3_raw_data["postLaunchActionsStatus"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipatingServerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipatingServerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLaunchConfigurationTemplatesResponse:
    boto3_raw_data: "type_defs.DescribeLaunchConfigurationTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return LaunchConfigurationTemplate.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLaunchConfigurationTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLaunchConfigurationTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLaunchConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.CreateLaunchConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    associatePublicIpAddress = field("associatePublicIpAddress")
    bootMode = field("bootMode")
    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    enableMapAutoTagging = field("enableMapAutoTagging")

    @cached_property
    def largeVolumeConf(self):  # pragma: no cover
        return LaunchTemplateDiskConf.make_one(self.boto3_raw_data["largeVolumeConf"])

    launchDisposition = field("launchDisposition")

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    mapAutoTaggingMpeID = field("mapAutoTaggingMpeID")
    postLaunchActions = field("postLaunchActions")

    @cached_property
    def smallVolumeConf(self):  # pragma: no cover
        return LaunchTemplateDiskConf.make_one(self.boto3_raw_data["smallVolumeConf"])

    smallVolumeMaxSize = field("smallVolumeMaxSize")
    tags = field("tags")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLaunchConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLaunchConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLaunchConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateLaunchConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    accountID = field("accountID")
    bootMode = field("bootMode")
    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    enableMapAutoTagging = field("enableMapAutoTagging")
    launchDisposition = field("launchDisposition")

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    mapAutoTaggingMpeID = field("mapAutoTaggingMpeID")
    name = field("name")
    postLaunchActions = field("postLaunchActions")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLaunchConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLaunchConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLaunchConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.UpdateLaunchConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    launchConfigurationTemplateID = field("launchConfigurationTemplateID")
    associatePublicIpAddress = field("associatePublicIpAddress")
    bootMode = field("bootMode")
    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    enableMapAutoTagging = field("enableMapAutoTagging")

    @cached_property
    def largeVolumeConf(self):  # pragma: no cover
        return LaunchTemplateDiskConf.make_one(self.boto3_raw_data["largeVolumeConf"])

    launchDisposition = field("launchDisposition")

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    mapAutoTaggingMpeID = field("mapAutoTaggingMpeID")
    postLaunchActions = field("postLaunchActions")

    @cached_property
    def smallVolumeConf(self):  # pragma: no cover
        return LaunchTemplateDiskConf.make_one(self.boto3_raw_data["smallVolumeConf"])

    smallVolumeMaxSize = field("smallVolumeMaxSize")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLaunchConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLaunchConfigurationTemplateRequestTypeDef"]
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

    jobID = field("jobID")
    arn = field("arn")
    creationDateTime = field("creationDateTime")
    endDateTime = field("endDateTime")
    initiatedBy = field("initiatedBy")

    @cached_property
    def participatingServers(self):  # pragma: no cover
        return ParticipatingServer.make_many(
            self.boto3_raw_data["participatingServers"]
        )

    status = field("status")
    tags = field("tags")
    type = field("type")

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
class DescribeJobsResponse:
    boto3_raw_data: "type_defs.DescribeJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCutoverResponse:
    boto3_raw_data: "type_defs.StartCutoverResponseTypeDef" = dataclasses.field()

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCutoverResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCutoverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTestResponse:
    boto3_raw_data: "type_defs.StartTestResponseTypeDef" = dataclasses.field()

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartTestResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateTargetInstancesResponse:
    boto3_raw_data: "type_defs.TerminateTargetInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TerminateTargetInstancesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateTargetInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
