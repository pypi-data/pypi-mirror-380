# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sms import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class LaunchDetails:
    boto3_raw_data: "type_defs.LaunchDetailsTypeDef" = dataclasses.field()

    latestLaunchTime = field("latestLaunchTime")
    stackName = field("stackName")
    stackId = field("stackId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Connector:
    boto3_raw_data: "type_defs.ConnectorTypeDef" = dataclasses.field()

    connectorId = field("connectorId")
    version = field("version")
    status = field("status")
    capabilityList = field("capabilityList")
    vmManagerName = field("vmManagerName")
    vmManagerType = field("vmManagerType")
    vmManagerId = field("vmManagerId")
    ipAddress = field("ipAddress")
    macAddress = field("macAddress")
    associatedOn = field("associatedOn")

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
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

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
class DeleteAppLaunchConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteAppLaunchConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAppLaunchConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppLaunchConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteAppReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAppReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppRequest:
    boto3_raw_data: "type_defs.DeleteAppRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    forceStopAppReplication = field("forceStopAppReplication")
    forceTerminateApp = field("forceTerminateApp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppValidationConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteAppValidationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAppValidationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppValidationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationJobRequest:
    boto3_raw_data: "type_defs.DeleteReplicationJobRequestTypeDef" = dataclasses.field()

    replicationJobId = field("replicationJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReplicationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateConnectorRequest:
    boto3_raw_data: "type_defs.DisassociateConnectorRequestTypeDef" = (
        dataclasses.field()
    )

    connectorId = field("connectorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateChangeSetRequest:
    boto3_raw_data: "type_defs.GenerateChangeSetRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    changesetFormat = field("changesetFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateChangeSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateChangeSetRequestTypeDef"]
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

    bucket = field("bucket")
    key = field("key")

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
class GenerateTemplateRequest:
    boto3_raw_data: "type_defs.GenerateTemplateRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    templateFormat = field("templateFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppLaunchConfigurationRequest:
    boto3_raw_data: "type_defs.GetAppLaunchConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAppLaunchConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppLaunchConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.GetAppReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAppReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppRequest:
    boto3_raw_data: "type_defs.GetAppRequestTypeDef" = dataclasses.field()

    appId = field("appId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAppRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppValidationConfigurationRequest:
    boto3_raw_data: "type_defs.GetAppValidationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAppValidationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppValidationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppValidationOutputRequest:
    boto3_raw_data: "type_defs.GetAppValidationOutputRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAppValidationOutputRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppValidationOutputRequestTypeDef"]
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
class GetConnectorsRequest:
    boto3_raw_data: "type_defs.GetConnectorsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReplicationJobsRequest:
    boto3_raw_data: "type_defs.GetReplicationJobsRequestTypeDef" = dataclasses.field()

    replicationJobId = field("replicationJobId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReplicationJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReplicationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReplicationRunsRequest:
    boto3_raw_data: "type_defs.GetReplicationRunsRequestTypeDef" = dataclasses.field()

    replicationJobId = field("replicationJobId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReplicationRunsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReplicationRunsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VmServerAddress:
    boto3_raw_data: "type_defs.VmServerAddressTypeDef" = dataclasses.field()

    vmManagerId = field("vmManagerId")
    vmId = field("vmId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VmServerAddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VmServerAddressTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAppCatalogRequest:
    boto3_raw_data: "type_defs.ImportAppCatalogRequestTypeDef" = dataclasses.field()

    roleName = field("roleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportAppCatalogRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAppCatalogRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchAppRequest:
    boto3_raw_data: "type_defs.LaunchAppRequestTypeDef" = dataclasses.field()

    appId = field("appId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsRequest:
    boto3_raw_data: "type_defs.ListAppsRequestTypeDef" = dataclasses.field()

    appIds = field("appIds")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAppsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListAppsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationContext:
    boto3_raw_data: "type_defs.NotificationContextTypeDef" = dataclasses.field()

    validationId = field("validationId")
    status = field("status")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRunStageDetails:
    boto3_raw_data: "type_defs.ReplicationRunStageDetailsTypeDef" = dataclasses.field()

    stage = field("stage")
    stageProgress = field("stageProgress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRunStageDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRunStageDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerReplicationParametersOutput:
    boto3_raw_data: "type_defs.ServerReplicationParametersOutputTypeDef" = (
        dataclasses.field()
    )

    seedTime = field("seedTime")
    frequency = field("frequency")
    runOnce = field("runOnce")
    licenseType = field("licenseType")
    numberOfRecentAmisToKeep = field("numberOfRecentAmisToKeep")
    encrypted = field("encrypted")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerReplicationParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerReplicationParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAppReplicationRequest:
    boto3_raw_data: "type_defs.StartAppReplicationRequestTypeDef" = dataclasses.field()

    appId = field("appId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAppReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAppReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOnDemandAppReplicationRequest:
    boto3_raw_data: "type_defs.StartOnDemandAppReplicationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartOnDemandAppReplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOnDemandAppReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOnDemandReplicationRunRequest:
    boto3_raw_data: "type_defs.StartOnDemandReplicationRunRequestTypeDef" = (
        dataclasses.field()
    )

    replicationJobId = field("replicationJobId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartOnDemandReplicationRunRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOnDemandReplicationRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopAppReplicationRequest:
    boto3_raw_data: "type_defs.StopAppReplicationRequestTypeDef" = dataclasses.field()

    appId = field("appId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopAppReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopAppReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateAppRequest:
    boto3_raw_data: "type_defs.TerminateAppRequestTypeDef" = dataclasses.field()

    appId = field("appId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateAppRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppSummary:
    boto3_raw_data: "type_defs.AppSummaryTypeDef" = dataclasses.field()

    appId = field("appId")
    importedAppId = field("importedAppId")
    name = field("name")
    description = field("description")
    status = field("status")
    statusMessage = field("statusMessage")
    replicationConfigurationStatus = field("replicationConfigurationStatus")
    replicationStatus = field("replicationStatus")
    replicationStatusMessage = field("replicationStatusMessage")
    latestReplicationTime = field("latestReplicationTime")
    launchConfigurationStatus = field("launchConfigurationStatus")
    launchStatus = field("launchStatus")
    launchStatusMessage = field("launchStatusMessage")

    @cached_property
    def launchDetails(self):  # pragma: no cover
        return LaunchDetails.make_one(self.boto3_raw_data["launchDetails"])

    creationTime = field("creationTime")
    lastModified = field("lastModified")
    roleName = field("roleName")
    totalServerGroups = field("totalServerGroups")
    totalServers = field("totalServers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationJobResponse:
    boto3_raw_data: "type_defs.CreateReplicationJobResponseTypeDef" = (
        dataclasses.field()
    )

    replicationJobId = field("replicationJobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReplicationJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectorsResponse:
    boto3_raw_data: "type_defs.GetConnectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def connectorList(self):  # pragma: no cover
        return Connector.make_many(self.boto3_raw_data["connectorList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOnDemandReplicationRunResponse:
    boto3_raw_data: "type_defs.StartOnDemandReplicationRunResponseTypeDef" = (
        dataclasses.field()
    )

    replicationRunId = field("replicationRunId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartOnDemandReplicationRunResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOnDemandReplicationRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationJobRequest:
    boto3_raw_data: "type_defs.CreateReplicationJobRequestTypeDef" = dataclasses.field()

    serverId = field("serverId")
    seedReplicationTime = field("seedReplicationTime")
    frequency = field("frequency")
    runOnce = field("runOnce")
    licenseType = field("licenseType")
    roleName = field("roleName")
    description = field("description")
    numberOfRecentAmisToKeep = field("numberOfRecentAmisToKeep")
    encrypted = field("encrypted")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReplicationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerReplicationParameters:
    boto3_raw_data: "type_defs.ServerReplicationParametersTypeDef" = dataclasses.field()

    seedTime = field("seedTime")
    frequency = field("frequency")
    runOnce = field("runOnce")
    licenseType = field("licenseType")
    numberOfRecentAmisToKeep = field("numberOfRecentAmisToKeep")
    encrypted = field("encrypted")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerReplicationParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerReplicationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReplicationJobRequest:
    boto3_raw_data: "type_defs.UpdateReplicationJobRequestTypeDef" = dataclasses.field()

    replicationJobId = field("replicationJobId")
    frequency = field("frequency")
    nextReplicationRunStartTime = field("nextReplicationRunStartTime")
    licenseType = field("licenseType")
    roleName = field("roleName")
    description = field("description")
    numberOfRecentAmisToKeep = field("numberOfRecentAmisToKeep")
    encrypted = field("encrypted")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReplicationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReplicationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateChangeSetResponse:
    boto3_raw_data: "type_defs.GenerateChangeSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateChangeSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateChangeSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateTemplateResponse:
    boto3_raw_data: "type_defs.GenerateTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSMOutput:
    boto3_raw_data: "type_defs.SSMOutputTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSMOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSMOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Source:
    boto3_raw_data: "type_defs.SourceTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserData:
    boto3_raw_data: "type_defs.UserDataTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectorsRequestPaginate:
    boto3_raw_data: "type_defs.GetConnectorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectorsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReplicationJobsRequestPaginate:
    boto3_raw_data: "type_defs.GetReplicationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    replicationJobId = field("replicationJobId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReplicationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReplicationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReplicationRunsRequestPaginate:
    boto3_raw_data: "type_defs.GetReplicationRunsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    replicationJobId = field("replicationJobId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReplicationRunsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReplicationRunsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsRequestPaginate:
    boto3_raw_data: "type_defs.ListAppsRequestPaginateTypeDef" = dataclasses.field()

    appIds = field("appIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServersRequestPaginate:
    boto3_raw_data: "type_defs.GetServersRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def vmServerAddressList(self):  # pragma: no cover
        return VmServerAddress.make_many(self.boto3_raw_data["vmServerAddressList"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServersRequest:
    boto3_raw_data: "type_defs.GetServersRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def vmServerAddressList(self):  # pragma: no cover
        return VmServerAddress.make_many(self.boto3_raw_data["vmServerAddressList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetServersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VmServer:
    boto3_raw_data: "type_defs.VmServerTypeDef" = dataclasses.field()

    @cached_property
    def vmServerAddress(self):  # pragma: no cover
        return VmServerAddress.make_one(self.boto3_raw_data["vmServerAddress"])

    vmName = field("vmName")
    vmManagerName = field("vmManagerName")
    vmManagerType = field("vmManagerType")
    vmPath = field("vmPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VmServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VmServerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyAppValidationOutputRequest:
    boto3_raw_data: "type_defs.NotifyAppValidationOutputRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @cached_property
    def notificationContext(self):  # pragma: no cover
        return NotificationContext.make_one(self.boto3_raw_data["notificationContext"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NotifyAppValidationOutputRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyAppValidationOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRun:
    boto3_raw_data: "type_defs.ReplicationRunTypeDef" = dataclasses.field()

    replicationRunId = field("replicationRunId")
    state = field("state")
    type = field("type")

    @cached_property
    def stageDetails(self):  # pragma: no cover
        return ReplicationRunStageDetails.make_one(self.boto3_raw_data["stageDetails"])

    statusMessage = field("statusMessage")
    amiId = field("amiId")
    scheduledStartTime = field("scheduledStartTime")
    completedTime = field("completedTime")
    description = field("description")
    encrypted = field("encrypted")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationRunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationRunTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsResponse:
    boto3_raw_data: "type_defs.ListAppsResponseTypeDef" = dataclasses.field()

    @cached_property
    def apps(self):  # pragma: no cover
        return AppSummary.make_many(self.boto3_raw_data["apps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAppsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppValidationOutput:
    boto3_raw_data: "type_defs.AppValidationOutputTypeDef" = dataclasses.field()

    @cached_property
    def ssmOutput(self):  # pragma: no cover
        return SSMOutput.make_one(self.boto3_raw_data["ssmOutput"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppValidationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppValidationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSMValidationParameters:
    boto3_raw_data: "type_defs.SSMValidationParametersTypeDef" = dataclasses.field()

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    instanceId = field("instanceId")
    scriptType = field("scriptType")
    command = field("command")
    executionTimeoutSeconds = field("executionTimeoutSeconds")
    outputS3BucketName = field("outputS3BucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SSMValidationParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SSMValidationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserDataValidationParameters:
    boto3_raw_data: "type_defs.UserDataValidationParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    scriptType = field("scriptType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserDataValidationParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserDataValidationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Server:
    boto3_raw_data: "type_defs.ServerTypeDef" = dataclasses.field()

    serverId = field("serverId")
    serverType = field("serverType")

    @cached_property
    def vmServer(self):  # pragma: no cover
        return VmServer.make_one(self.boto3_raw_data["vmServer"])

    replicationJobId = field("replicationJobId")
    replicationJobTerminated = field("replicationJobTerminated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationJob:
    boto3_raw_data: "type_defs.ReplicationJobTypeDef" = dataclasses.field()

    replicationJobId = field("replicationJobId")
    serverId = field("serverId")
    serverType = field("serverType")

    @cached_property
    def vmServer(self):  # pragma: no cover
        return VmServer.make_one(self.boto3_raw_data["vmServer"])

    seedReplicationTime = field("seedReplicationTime")
    frequency = field("frequency")
    runOnce = field("runOnce")
    nextReplicationRunStartTime = field("nextReplicationRunStartTime")
    licenseType = field("licenseType")
    roleName = field("roleName")
    latestAmiId = field("latestAmiId")
    state = field("state")
    statusMessage = field("statusMessage")
    description = field("description")
    numberOfRecentAmisToKeep = field("numberOfRecentAmisToKeep")
    encrypted = field("encrypted")
    kmsKeyId = field("kmsKeyId")

    @cached_property
    def replicationRunList(self):  # pragma: no cover
        return ReplicationRun.make_many(self.boto3_raw_data["replicationRunList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppValidationConfiguration:
    boto3_raw_data: "type_defs.AppValidationConfigurationTypeDef" = dataclasses.field()

    validationId = field("validationId")
    name = field("name")
    appValidationStrategy = field("appValidationStrategy")

    @cached_property
    def ssmValidationParameters(self):  # pragma: no cover
        return SSMValidationParameters.make_one(
            self.boto3_raw_data["ssmValidationParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppValidationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppValidationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServersResponse:
    boto3_raw_data: "type_defs.GetServersResponseTypeDef" = dataclasses.field()

    lastModifiedOn = field("lastModifiedOn")
    serverCatalogStatus = field("serverCatalogStatus")

    @cached_property
    def serverList(self):  # pragma: no cover
        return Server.make_many(self.boto3_raw_data["serverList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerGroupOutput:
    boto3_raw_data: "type_defs.ServerGroupOutputTypeDef" = dataclasses.field()

    serverGroupId = field("serverGroupId")
    name = field("name")

    @cached_property
    def serverList(self):  # pragma: no cover
        return Server.make_many(self.boto3_raw_data["serverList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerGroupOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerGroup:
    boto3_raw_data: "type_defs.ServerGroupTypeDef" = dataclasses.field()

    serverGroupId = field("serverGroupId")
    name = field("name")

    @cached_property
    def serverList(self):  # pragma: no cover
        return Server.make_many(self.boto3_raw_data["serverList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerLaunchConfiguration:
    boto3_raw_data: "type_defs.ServerLaunchConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def server(self):  # pragma: no cover
        return Server.make_one(self.boto3_raw_data["server"])

    logicalId = field("logicalId")
    vpc = field("vpc")
    subnet = field("subnet")
    securityGroup = field("securityGroup")
    ec2KeyName = field("ec2KeyName")

    @cached_property
    def userData(self):  # pragma: no cover
        return UserData.make_one(self.boto3_raw_data["userData"])

    instanceType = field("instanceType")
    associatePublicIpAddress = field("associatePublicIpAddress")
    iamInstanceProfileName = field("iamInstanceProfileName")

    @cached_property
    def configureScript(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["configureScript"])

    configureScriptType = field("configureScriptType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerLaunchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerLaunchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerReplicationConfigurationOutput:
    boto3_raw_data: "type_defs.ServerReplicationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def server(self):  # pragma: no cover
        return Server.make_one(self.boto3_raw_data["server"])

    @cached_property
    def serverReplicationParameters(self):  # pragma: no cover
        return ServerReplicationParametersOutput.make_one(
            self.boto3_raw_data["serverReplicationParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerReplicationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerReplicationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerReplicationConfiguration:
    boto3_raw_data: "type_defs.ServerReplicationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def server(self):  # pragma: no cover
        return Server.make_one(self.boto3_raw_data["server"])

    serverReplicationParameters = field("serverReplicationParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServerReplicationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerReplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerValidationConfiguration:
    boto3_raw_data: "type_defs.ServerValidationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def server(self):  # pragma: no cover
        return Server.make_one(self.boto3_raw_data["server"])

    validationId = field("validationId")
    name = field("name")
    serverValidationStrategy = field("serverValidationStrategy")

    @cached_property
    def userDataValidationParameters(self):  # pragma: no cover
        return UserDataValidationParameters.make_one(
            self.boto3_raw_data["userDataValidationParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServerValidationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerValidationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerValidationOutput:
    boto3_raw_data: "type_defs.ServerValidationOutputTypeDef" = dataclasses.field()

    @cached_property
    def server(self):  # pragma: no cover
        return Server.make_one(self.boto3_raw_data["server"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerValidationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerValidationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReplicationJobsResponse:
    boto3_raw_data: "type_defs.GetReplicationJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def replicationJobList(self):  # pragma: no cover
        return ReplicationJob.make_many(self.boto3_raw_data["replicationJobList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReplicationJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReplicationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReplicationRunsResponse:
    boto3_raw_data: "type_defs.GetReplicationRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def replicationJob(self):  # pragma: no cover
        return ReplicationJob.make_one(self.boto3_raw_data["replicationJob"])

    @cached_property
    def replicationRunList(self):  # pragma: no cover
        return ReplicationRun.make_many(self.boto3_raw_data["replicationRunList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReplicationRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReplicationRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppResponse:
    boto3_raw_data: "type_defs.CreateAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def appSummary(self):  # pragma: no cover
        return AppSummary.make_one(self.boto3_raw_data["appSummary"])

    @cached_property
    def serverGroups(self):  # pragma: no cover
        return ServerGroupOutput.make_many(self.boto3_raw_data["serverGroups"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppResponse:
    boto3_raw_data: "type_defs.GetAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def appSummary(self):  # pragma: no cover
        return AppSummary.make_one(self.boto3_raw_data["appSummary"])

    @cached_property
    def serverGroups(self):  # pragma: no cover
        return ServerGroupOutput.make_many(self.boto3_raw_data["serverGroups"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAppResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAppResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppResponse:
    boto3_raw_data: "type_defs.UpdateAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def appSummary(self):  # pragma: no cover
        return AppSummary.make_one(self.boto3_raw_data["appSummary"])

    @cached_property
    def serverGroups(self):  # pragma: no cover
        return ServerGroupOutput.make_many(self.boto3_raw_data["serverGroups"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAppResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerGroupLaunchConfigurationOutput:
    boto3_raw_data: "type_defs.ServerGroupLaunchConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    serverGroupId = field("serverGroupId")
    launchOrder = field("launchOrder")

    @cached_property
    def serverLaunchConfigurations(self):  # pragma: no cover
        return ServerLaunchConfiguration.make_many(
            self.boto3_raw_data["serverLaunchConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerGroupLaunchConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerGroupLaunchConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerGroupLaunchConfiguration:
    boto3_raw_data: "type_defs.ServerGroupLaunchConfigurationTypeDef" = (
        dataclasses.field()
    )

    serverGroupId = field("serverGroupId")
    launchOrder = field("launchOrder")

    @cached_property
    def serverLaunchConfigurations(self):  # pragma: no cover
        return ServerLaunchConfiguration.make_many(
            self.boto3_raw_data["serverLaunchConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServerGroupLaunchConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerGroupLaunchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerGroupReplicationConfigurationOutput:
    boto3_raw_data: "type_defs.ServerGroupReplicationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    serverGroupId = field("serverGroupId")

    @cached_property
    def serverReplicationConfigurations(self):  # pragma: no cover
        return ServerReplicationConfigurationOutput.make_many(
            self.boto3_raw_data["serverReplicationConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerGroupReplicationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerGroupReplicationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerGroupValidationConfigurationOutput:
    boto3_raw_data: "type_defs.ServerGroupValidationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    serverGroupId = field("serverGroupId")

    @cached_property
    def serverValidationConfigurations(self):  # pragma: no cover
        return ServerValidationConfiguration.make_many(
            self.boto3_raw_data["serverValidationConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerGroupValidationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerGroupValidationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerGroupValidationConfiguration:
    boto3_raw_data: "type_defs.ServerGroupValidationConfigurationTypeDef" = (
        dataclasses.field()
    )

    serverGroupId = field("serverGroupId")

    @cached_property
    def serverValidationConfigurations(self):  # pragma: no cover
        return ServerValidationConfiguration.make_many(
            self.boto3_raw_data["serverValidationConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerGroupValidationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerGroupValidationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationOutput:
    boto3_raw_data: "type_defs.ValidationOutputTypeDef" = dataclasses.field()

    validationId = field("validationId")
    name = field("name")
    status = field("status")
    statusMessage = field("statusMessage")
    latestValidationTime = field("latestValidationTime")

    @cached_property
    def appValidationOutput(self):  # pragma: no cover
        return AppValidationOutput.make_one(self.boto3_raw_data["appValidationOutput"])

    @cached_property
    def serverValidationOutput(self):  # pragma: no cover
        return ServerValidationOutput.make_one(
            self.boto3_raw_data["serverValidationOutput"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidationOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppRequest:
    boto3_raw_data: "type_defs.CreateAppRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    roleName = field("roleName")
    clientToken = field("clientToken")
    serverGroups = field("serverGroups")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppRequest:
    boto3_raw_data: "type_defs.UpdateAppRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    name = field("name")
    description = field("description")
    roleName = field("roleName")
    serverGroups = field("serverGroups")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppLaunchConfigurationResponse:
    boto3_raw_data: "type_defs.GetAppLaunchConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    roleName = field("roleName")
    autoLaunch = field("autoLaunch")

    @cached_property
    def serverGroupLaunchConfigurations(self):  # pragma: no cover
        return ServerGroupLaunchConfigurationOutput.make_many(
            self.boto3_raw_data["serverGroupLaunchConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAppLaunchConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppLaunchConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppReplicationConfigurationResponse:
    boto3_raw_data: "type_defs.GetAppReplicationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serverGroupReplicationConfigurations(self):  # pragma: no cover
        return ServerGroupReplicationConfigurationOutput.make_many(
            self.boto3_raw_data["serverGroupReplicationConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAppReplicationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppReplicationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerGroupReplicationConfiguration:
    boto3_raw_data: "type_defs.ServerGroupReplicationConfigurationTypeDef" = (
        dataclasses.field()
    )

    serverGroupId = field("serverGroupId")
    serverReplicationConfigurations = field("serverReplicationConfigurations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerGroupReplicationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerGroupReplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppValidationConfigurationResponse:
    boto3_raw_data: "type_defs.GetAppValidationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def appValidationConfigurations(self):  # pragma: no cover
        return AppValidationConfiguration.make_many(
            self.boto3_raw_data["appValidationConfigurations"]
        )

    @cached_property
    def serverGroupValidationConfigurations(self):  # pragma: no cover
        return ServerGroupValidationConfigurationOutput.make_many(
            self.boto3_raw_data["serverGroupValidationConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAppValidationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppValidationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppValidationOutputResponse:
    boto3_raw_data: "type_defs.GetAppValidationOutputResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def validationOutputList(self):  # pragma: no cover
        return ValidationOutput.make_many(self.boto3_raw_data["validationOutputList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAppValidationOutputResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppValidationOutputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAppLaunchConfigurationRequest:
    boto3_raw_data: "type_defs.PutAppLaunchConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    roleName = field("roleName")
    autoLaunch = field("autoLaunch")
    serverGroupLaunchConfigurations = field("serverGroupLaunchConfigurations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutAppLaunchConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAppLaunchConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAppValidationConfigurationRequest:
    boto3_raw_data: "type_defs.PutAppValidationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @cached_property
    def appValidationConfigurations(self):  # pragma: no cover
        return AppValidationConfiguration.make_many(
            self.boto3_raw_data["appValidationConfigurations"]
        )

    serverGroupValidationConfigurations = field("serverGroupValidationConfigurations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAppValidationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAppValidationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAppReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.PutAppReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    serverGroupReplicationConfigurations = field("serverGroupReplicationConfigurations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAppReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAppReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
