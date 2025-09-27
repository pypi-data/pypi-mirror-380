# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_greengrass import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssociateRoleToGroupRequest:
    boto3_raw_data: "type_defs.AssociateRoleToGroupRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateRoleToGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateRoleToGroupRequestTypeDef"]
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
class AssociateServiceRoleToAccountRequest:
    boto3_raw_data: "type_defs.AssociateServiceRoleToAccountRequestTypeDef" = (
        dataclasses.field()
    )

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateServiceRoleToAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateServiceRoleToAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BulkDeploymentMetrics:
    boto3_raw_data: "type_defs.BulkDeploymentMetricsTypeDef" = dataclasses.field()

    InvalidInputRecords = field("InvalidInputRecords")
    RecordsProcessed = field("RecordsProcessed")
    RetryAttempts = field("RetryAttempts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BulkDeploymentMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BulkDeploymentMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetail:
    boto3_raw_data: "type_defs.ErrorDetailTypeDef" = dataclasses.field()

    DetailedErrorCode = field("DetailedErrorCode")
    DetailedErrorMessage = field("DetailedErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BulkDeployment:
    boto3_raw_data: "type_defs.BulkDeploymentTypeDef" = dataclasses.field()

    BulkDeploymentArn = field("BulkDeploymentArn")
    BulkDeploymentId = field("BulkDeploymentId")
    CreatedAt = field("CreatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BulkDeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BulkDeploymentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectivityInfo:
    boto3_raw_data: "type_defs.ConnectivityInfoTypeDef" = dataclasses.field()

    HostAddress = field("HostAddress")
    Id = field("Id")
    Metadata = field("Metadata")
    PortNumber = field("PortNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectivityInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectivityInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorOutput:
    boto3_raw_data: "type_defs.ConnectorOutputTypeDef" = dataclasses.field()

    ConnectorArn = field("ConnectorArn")
    Id = field("Id")
    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectorOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Connector:
    boto3_raw_data: "type_defs.ConnectorTypeDef" = dataclasses.field()

    ConnectorArn = field("ConnectorArn")
    Id = field("Id")
    Parameters = field("Parameters")

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
class Core:
    boto3_raw_data: "type_defs.CoreTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")
    Id = field("Id")
    ThingArn = field("ThingArn")
    SyncShadow = field("SyncShadow")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoreTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentRequest:
    boto3_raw_data: "type_defs.CreateDeploymentRequestTypeDef" = dataclasses.field()

    DeploymentType = field("DeploymentType")
    GroupId = field("GroupId")
    AmznClientToken = field("AmznClientToken")
    DeploymentId = field("DeploymentId")
    GroupVersionId = field("GroupVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentRequestTypeDef"]
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

    CertificateArn = field("CertificateArn")
    Id = field("Id")
    ThingArn = field("ThingArn")
    SyncShadow = field("SyncShadow")

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
class CreateGroupCertificateAuthorityRequest:
    boto3_raw_data: "type_defs.CreateGroupCertificateAuthorityRequestTypeDef" = (
        dataclasses.field()
    )

    GroupId = field("GroupId")
    AmznClientToken = field("AmznClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateGroupCertificateAuthorityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupCertificateAuthorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupVersion:
    boto3_raw_data: "type_defs.GroupVersionTypeDef" = dataclasses.field()

    ConnectorDefinitionVersionArn = field("ConnectorDefinitionVersionArn")
    CoreDefinitionVersionArn = field("CoreDefinitionVersionArn")
    DeviceDefinitionVersionArn = field("DeviceDefinitionVersionArn")
    FunctionDefinitionVersionArn = field("FunctionDefinitionVersionArn")
    LoggerDefinitionVersionArn = field("LoggerDefinitionVersionArn")
    ResourceDefinitionVersionArn = field("ResourceDefinitionVersionArn")
    SubscriptionDefinitionVersionArn = field("SubscriptionDefinitionVersionArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupVersionRequest:
    boto3_raw_data: "type_defs.CreateGroupVersionRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    AmznClientToken = field("AmznClientToken")
    ConnectorDefinitionVersionArn = field("ConnectorDefinitionVersionArn")
    CoreDefinitionVersionArn = field("CoreDefinitionVersionArn")
    DeviceDefinitionVersionArn = field("DeviceDefinitionVersionArn")
    FunctionDefinitionVersionArn = field("FunctionDefinitionVersionArn")
    LoggerDefinitionVersionArn = field("LoggerDefinitionVersionArn")
    ResourceDefinitionVersionArn = field("ResourceDefinitionVersionArn")
    SubscriptionDefinitionVersionArn = field("SubscriptionDefinitionVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Logger:
    boto3_raw_data: "type_defs.LoggerTypeDef" = dataclasses.field()

    Component = field("Component")
    Id = field("Id")
    Level = field("Level")
    Type = field("Type")
    Space = field("Space")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSoftwareUpdateJobRequest:
    boto3_raw_data: "type_defs.CreateSoftwareUpdateJobRequestTypeDef" = (
        dataclasses.field()
    )

    S3UrlSignerRole = field("S3UrlSignerRole")
    SoftwareToUpdate = field("SoftwareToUpdate")
    UpdateTargets = field("UpdateTargets")
    UpdateTargetsArchitecture = field("UpdateTargetsArchitecture")
    UpdateTargetsOperatingSystem = field("UpdateTargetsOperatingSystem")
    AmznClientToken = field("AmznClientToken")
    UpdateAgentLogLevel = field("UpdateAgentLogLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSoftwareUpdateJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSoftwareUpdateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subscription:
    boto3_raw_data: "type_defs.SubscriptionTypeDef" = dataclasses.field()

    Id = field("Id")
    Source = field("Source")
    Subject = field("Subject")
    Target = field("Target")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubscriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefinitionInformation:
    boto3_raw_data: "type_defs.DefinitionInformationTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefinitionInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefinitionInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectorDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteConnectorDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorDefinitionId = field("ConnectorDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteConnectorDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectorDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCoreDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteCoreDefinitionRequestTypeDef" = dataclasses.field()

    CoreDefinitionId = field("CoreDefinitionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCoreDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCoreDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeviceDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteDeviceDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    DeviceDefinitionId = field("DeviceDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDeviceDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeviceDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFunctionDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteFunctionDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionDefinitionId = field("FunctionDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFunctionDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFunctionDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGroupRequest:
    boto3_raw_data: "type_defs.DeleteGroupRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoggerDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteLoggerDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    LoggerDefinitionId = field("LoggerDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteLoggerDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoggerDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteResourceDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceDefinitionId = field("ResourceDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteResourceDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubscriptionDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteSubscriptionDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionDefinitionId = field("SubscriptionDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSubscriptionDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubscriptionDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Deployment:
    boto3_raw_data: "type_defs.DeploymentTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    DeploymentArn = field("DeploymentArn")
    DeploymentId = field("DeploymentId")
    DeploymentType = field("DeploymentType")
    GroupArn = field("GroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateRoleFromGroupRequest:
    boto3_raw_data: "type_defs.DisassociateRoleFromGroupRequestTypeDef" = (
        dataclasses.field()
    )

    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateRoleFromGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateRoleFromGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceAccessPolicy:
    boto3_raw_data: "type_defs.ResourceAccessPolicyTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    Permission = field("Permission")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceAccessPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceAccessPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionRunAsConfig:
    boto3_raw_data: "type_defs.FunctionRunAsConfigTypeDef" = dataclasses.field()

    Gid = field("Gid")
    Uid = field("Uid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionRunAsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionRunAsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssociatedRoleRequest:
    boto3_raw_data: "type_defs.GetAssociatedRoleRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssociatedRoleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssociatedRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBulkDeploymentStatusRequest:
    boto3_raw_data: "type_defs.GetBulkDeploymentStatusRequestTypeDef" = (
        dataclasses.field()
    )

    BulkDeploymentId = field("BulkDeploymentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBulkDeploymentStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBulkDeploymentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectivityInfoRequest:
    boto3_raw_data: "type_defs.GetConnectivityInfoRequestTypeDef" = dataclasses.field()

    ThingName = field("ThingName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectivityInfoRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectivityInfoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectorDefinitionRequest:
    boto3_raw_data: "type_defs.GetConnectorDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorDefinitionId = field("ConnectorDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetConnectorDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectorDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectorDefinitionVersionRequest:
    boto3_raw_data: "type_defs.GetConnectorDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorDefinitionId = field("ConnectorDefinitionId")
    ConnectorDefinitionVersionId = field("ConnectorDefinitionVersionId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConnectorDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectorDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreDefinitionRequest:
    boto3_raw_data: "type_defs.GetCoreDefinitionRequestTypeDef" = dataclasses.field()

    CoreDefinitionId = field("CoreDefinitionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCoreDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreDefinitionVersionRequest:
    boto3_raw_data: "type_defs.GetCoreDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    CoreDefinitionId = field("CoreDefinitionId")
    CoreDefinitionVersionId = field("CoreDefinitionVersionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCoreDefinitionVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentStatusRequest:
    boto3_raw_data: "type_defs.GetDeploymentStatusRequestTypeDef" = dataclasses.field()

    DeploymentId = field("DeploymentId")
    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceDefinitionRequest:
    boto3_raw_data: "type_defs.GetDeviceDefinitionRequestTypeDef" = dataclasses.field()

    DeviceDefinitionId = field("DeviceDefinitionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeviceDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceDefinitionVersionRequest:
    boto3_raw_data: "type_defs.GetDeviceDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    DeviceDefinitionId = field("DeviceDefinitionId")
    DeviceDefinitionVersionId = field("DeviceDefinitionVersionId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeviceDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionDefinitionRequest:
    boto3_raw_data: "type_defs.GetFunctionDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionDefinitionId = field("FunctionDefinitionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFunctionDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionDefinitionVersionRequest:
    boto3_raw_data: "type_defs.GetFunctionDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionDefinitionId = field("FunctionDefinitionId")
    FunctionDefinitionVersionId = field("FunctionDefinitionVersionId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupCertificateAuthorityRequest:
    boto3_raw_data: "type_defs.GetGroupCertificateAuthorityRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityId = field("CertificateAuthorityId")
    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetGroupCertificateAuthorityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupCertificateAuthorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupCertificateConfigurationRequest:
    boto3_raw_data: "type_defs.GetGroupCertificateConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetGroupCertificateConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupCertificateConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupRequest:
    boto3_raw_data: "type_defs.GetGroupRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGroupRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupVersionRequest:
    boto3_raw_data: "type_defs.GetGroupVersionRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    GroupVersionId = field("GroupVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoggerDefinitionRequest:
    boto3_raw_data: "type_defs.GetLoggerDefinitionRequestTypeDef" = dataclasses.field()

    LoggerDefinitionId = field("LoggerDefinitionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoggerDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoggerDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoggerDefinitionVersionRequest:
    boto3_raw_data: "type_defs.GetLoggerDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    LoggerDefinitionId = field("LoggerDefinitionId")
    LoggerDefinitionVersionId = field("LoggerDefinitionVersionId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLoggerDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoggerDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceDefinitionRequest:
    boto3_raw_data: "type_defs.GetResourceDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceDefinitionId = field("ResourceDefinitionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceDefinitionVersionRequest:
    boto3_raw_data: "type_defs.GetResourceDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceDefinitionId = field("ResourceDefinitionId")
    ResourceDefinitionVersionId = field("ResourceDefinitionVersionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResourceDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionDefinitionRequest:
    boto3_raw_data: "type_defs.GetSubscriptionDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionDefinitionId = field("SubscriptionDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSubscriptionDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionDefinitionVersionRequest:
    boto3_raw_data: "type_defs.GetSubscriptionDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionDefinitionId = field("SubscriptionDefinitionId")
    SubscriptionDefinitionVersionId = field("SubscriptionDefinitionVersionId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSubscriptionDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThingRuntimeConfigurationRequest:
    boto3_raw_data: "type_defs.GetThingRuntimeConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ThingName = field("ThingName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetThingRuntimeConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThingRuntimeConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupCertificateAuthorityProperties:
    boto3_raw_data: "type_defs.GroupCertificateAuthorityPropertiesTypeDef" = (
        dataclasses.field()
    )

    GroupCertificateAuthorityArn = field("GroupCertificateAuthorityArn")
    GroupCertificateAuthorityId = field("GroupCertificateAuthorityId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GroupCertificateAuthorityPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupCertificateAuthorityPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupInformation:
    boto3_raw_data: "type_defs.GroupInformationTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupOwnerSetting:
    boto3_raw_data: "type_defs.GroupOwnerSettingTypeDef" = dataclasses.field()

    AutoAddGroupOwner = field("AutoAddGroupOwner")
    GroupOwner = field("GroupOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupOwnerSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupOwnerSettingTypeDef"]
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
class ListBulkDeploymentDetailedReportsRequest:
    boto3_raw_data: "type_defs.ListBulkDeploymentDetailedReportsRequestTypeDef" = (
        dataclasses.field()
    )

    BulkDeploymentId = field("BulkDeploymentId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBulkDeploymentDetailedReportsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBulkDeploymentDetailedReportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBulkDeploymentsRequest:
    boto3_raw_data: "type_defs.ListBulkDeploymentsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBulkDeploymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBulkDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorDefinitionVersionsRequest:
    boto3_raw_data: "type_defs.ListConnectorDefinitionVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorDefinitionId = field("ConnectorDefinitionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConnectorDefinitionVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorDefinitionVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionInformation:
    boto3_raw_data: "type_defs.VersionInformationTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VersionInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersionInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorDefinitionsRequest:
    boto3_raw_data: "type_defs.ListConnectorDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConnectorDefinitionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreDefinitionVersionsRequest:
    boto3_raw_data: "type_defs.ListCoreDefinitionVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    CoreDefinitionId = field("CoreDefinitionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCoreDefinitionVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreDefinitionVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreDefinitionsRequest:
    boto3_raw_data: "type_defs.ListCoreDefinitionsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoreDefinitionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsRequest:
    boto3_raw_data: "type_defs.ListDeploymentsRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeviceDefinitionVersionsRequest:
    boto3_raw_data: "type_defs.ListDeviceDefinitionVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    DeviceDefinitionId = field("DeviceDefinitionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeviceDefinitionVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeviceDefinitionVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeviceDefinitionsRequest:
    boto3_raw_data: "type_defs.ListDeviceDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeviceDefinitionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeviceDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionDefinitionVersionsRequest:
    boto3_raw_data: "type_defs.ListFunctionDefinitionVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionDefinitionId = field("FunctionDefinitionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionDefinitionVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionDefinitionVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionDefinitionsRequest:
    boto3_raw_data: "type_defs.ListFunctionDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFunctionDefinitionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupCertificateAuthoritiesRequest:
    boto3_raw_data: "type_defs.ListGroupCertificateAuthoritiesRequestTypeDef" = (
        dataclasses.field()
    )

    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroupCertificateAuthoritiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupCertificateAuthoritiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupVersionsRequest:
    boto3_raw_data: "type_defs.ListGroupVersionsRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequest:
    boto3_raw_data: "type_defs.ListGroupsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoggerDefinitionVersionsRequest:
    boto3_raw_data: "type_defs.ListLoggerDefinitionVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    LoggerDefinitionId = field("LoggerDefinitionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLoggerDefinitionVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoggerDefinitionVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoggerDefinitionsRequest:
    boto3_raw_data: "type_defs.ListLoggerDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLoggerDefinitionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoggerDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDefinitionVersionsRequest:
    boto3_raw_data: "type_defs.ListResourceDefinitionVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceDefinitionId = field("ResourceDefinitionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceDefinitionVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDefinitionVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDefinitionsRequest:
    boto3_raw_data: "type_defs.ListResourceDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceDefinitionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionDefinitionVersionsRequest:
    boto3_raw_data: "type_defs.ListSubscriptionDefinitionVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionDefinitionId = field("SubscriptionDefinitionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubscriptionDefinitionVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionDefinitionVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionDefinitionsRequest:
    boto3_raw_data: "type_defs.ListSubscriptionDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubscriptionDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionDefinitionsRequestTypeDef"]
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
class ResetDeploymentsRequest:
    boto3_raw_data: "type_defs.ResetDeploymentsRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    AmznClientToken = field("AmznClientToken")
    Force = field("Force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetDeploymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecretsManagerSecretResourceDataOutput:
    boto3_raw_data: "type_defs.SecretsManagerSecretResourceDataOutputTypeDef" = (
        dataclasses.field()
    )

    ARN = field("ARN")
    AdditionalStagingLabelsToDownload = field("AdditionalStagingLabelsToDownload")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SecretsManagerSecretResourceDataOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecretsManagerSecretResourceDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDownloadOwnerSetting:
    boto3_raw_data: "type_defs.ResourceDownloadOwnerSettingTypeDef" = (
        dataclasses.field()
    )

    GroupOwner = field("GroupOwner")
    GroupPermission = field("GroupPermission")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceDownloadOwnerSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDownloadOwnerSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelemetryConfiguration:
    boto3_raw_data: "type_defs.TelemetryConfigurationTypeDef" = dataclasses.field()

    Telemetry = field("Telemetry")
    ConfigurationSyncStatus = field("ConfigurationSyncStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TelemetryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelemetryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecretsManagerSecretResourceData:
    boto3_raw_data: "type_defs.SecretsManagerSecretResourceDataTypeDef" = (
        dataclasses.field()
    )

    ARN = field("ARN")
    AdditionalStagingLabelsToDownload = field("AdditionalStagingLabelsToDownload")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SecretsManagerSecretResourceDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecretsManagerSecretResourceDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBulkDeploymentRequest:
    boto3_raw_data: "type_defs.StartBulkDeploymentRequestTypeDef" = dataclasses.field()

    ExecutionRoleArn = field("ExecutionRoleArn")
    InputFileUri = field("InputFileUri")
    AmznClientToken = field("AmznClientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBulkDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBulkDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBulkDeploymentRequest:
    boto3_raw_data: "type_defs.StopBulkDeploymentRequestTypeDef" = dataclasses.field()

    BulkDeploymentId = field("BulkDeploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopBulkDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBulkDeploymentRequestTypeDef"]
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
class TelemetryConfigurationUpdate:
    boto3_raw_data: "type_defs.TelemetryConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    Telemetry = field("Telemetry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TelemetryConfigurationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelemetryConfigurationUpdateTypeDef"]
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
class UpdateConnectorDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateConnectorDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorDefinitionId = field("ConnectorDefinitionId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateConnectorDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCoreDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateCoreDefinitionRequestTypeDef" = dataclasses.field()

    CoreDefinitionId = field("CoreDefinitionId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCoreDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCoreDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeviceDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateDeviceDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    DeviceDefinitionId = field("DeviceDefinitionId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDeviceDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeviceDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFunctionDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateFunctionDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionDefinitionId = field("FunctionDefinitionId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFunctionDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupCertificateConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateGroupCertificateConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    GroupId = field("GroupId")
    CertificateExpiryInMilliseconds = field("CertificateExpiryInMilliseconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateGroupCertificateConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupCertificateConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupRequest:
    boto3_raw_data: "type_defs.UpdateGroupRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLoggerDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateLoggerDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    LoggerDefinitionId = field("LoggerDefinitionId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLoggerDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLoggerDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateResourceDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceDefinitionId = field("ResourceDefinitionId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResourceDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateSubscriptionDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionDefinitionId = field("SubscriptionDefinitionId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSubscriptionDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateRoleToGroupResponse:
    boto3_raw_data: "type_defs.AssociateRoleToGroupResponseTypeDef" = (
        dataclasses.field()
    )

    AssociatedAt = field("AssociatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateRoleToGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateRoleToGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateServiceRoleToAccountResponse:
    boto3_raw_data: "type_defs.AssociateServiceRoleToAccountResponseTypeDef" = (
        dataclasses.field()
    )

    AssociatedAt = field("AssociatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateServiceRoleToAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateServiceRoleToAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorDefinitionResponse:
    boto3_raw_data: "type_defs.CreateConnectorDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConnectorDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorDefinitionVersionResponse:
    boto3_raw_data: "type_defs.CreateConnectorDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConnectorDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCoreDefinitionResponse:
    boto3_raw_data: "type_defs.CreateCoreDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCoreDefinitionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCoreDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCoreDefinitionVersionResponse:
    boto3_raw_data: "type_defs.CreateCoreDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCoreDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCoreDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentResponse:
    boto3_raw_data: "type_defs.CreateDeploymentResponseTypeDef" = dataclasses.field()

    DeploymentArn = field("DeploymentArn")
    DeploymentId = field("DeploymentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeviceDefinitionResponse:
    boto3_raw_data: "type_defs.CreateDeviceDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDeviceDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeviceDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeviceDefinitionVersionResponse:
    boto3_raw_data: "type_defs.CreateDeviceDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDeviceDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeviceDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionDefinitionResponse:
    boto3_raw_data: "type_defs.CreateFunctionDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFunctionDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionDefinitionVersionResponse:
    boto3_raw_data: "type_defs.CreateFunctionDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFunctionDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupCertificateAuthorityResponse:
    boto3_raw_data: "type_defs.CreateGroupCertificateAuthorityResponseTypeDef" = (
        dataclasses.field()
    )

    GroupCertificateAuthorityArn = field("GroupCertificateAuthorityArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateGroupCertificateAuthorityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupCertificateAuthorityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupResponse:
    boto3_raw_data: "type_defs.CreateGroupResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupVersionResponse:
    boto3_raw_data: "type_defs.CreateGroupVersionResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoggerDefinitionResponse:
    boto3_raw_data: "type_defs.CreateLoggerDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLoggerDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoggerDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoggerDefinitionVersionResponse:
    boto3_raw_data: "type_defs.CreateLoggerDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLoggerDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoggerDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceDefinitionResponse:
    boto3_raw_data: "type_defs.CreateResourceDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResourceDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceDefinitionVersionResponse:
    boto3_raw_data: "type_defs.CreateResourceDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResourceDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSoftwareUpdateJobResponse:
    boto3_raw_data: "type_defs.CreateSoftwareUpdateJobResponseTypeDef" = (
        dataclasses.field()
    )

    IotJobArn = field("IotJobArn")
    IotJobId = field("IotJobId")
    PlatformSoftwareVersion = field("PlatformSoftwareVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSoftwareUpdateJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSoftwareUpdateJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionDefinitionResponse:
    boto3_raw_data: "type_defs.CreateSubscriptionDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSubscriptionDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionDefinitionVersionResponse:
    boto3_raw_data: "type_defs.CreateSubscriptionDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSubscriptionDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateRoleFromGroupResponse:
    boto3_raw_data: "type_defs.DisassociateRoleFromGroupResponseTypeDef" = (
        dataclasses.field()
    )

    DisassociatedAt = field("DisassociatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateRoleFromGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateRoleFromGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateServiceRoleFromAccountResponse:
    boto3_raw_data: "type_defs.DisassociateServiceRoleFromAccountResponseTypeDef" = (
        dataclasses.field()
    )

    DisassociatedAt = field("DisassociatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateServiceRoleFromAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateServiceRoleFromAccountResponseTypeDef"]
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
class GetAssociatedRoleResponse:
    boto3_raw_data: "type_defs.GetAssociatedRoleResponseTypeDef" = dataclasses.field()

    AssociatedAt = field("AssociatedAt")
    RoleArn = field("RoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssociatedRoleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssociatedRoleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectorDefinitionResponse:
    boto3_raw_data: "type_defs.GetConnectorDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetConnectorDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectorDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreDefinitionResponse:
    boto3_raw_data: "type_defs.GetCoreDefinitionResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCoreDefinitionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceDefinitionResponse:
    boto3_raw_data: "type_defs.GetDeviceDefinitionResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeviceDefinitionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionDefinitionResponse:
    boto3_raw_data: "type_defs.GetFunctionDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFunctionDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupCertificateAuthorityResponse:
    boto3_raw_data: "type_defs.GetGroupCertificateAuthorityResponseTypeDef" = (
        dataclasses.field()
    )

    GroupCertificateAuthorityArn = field("GroupCertificateAuthorityArn")
    GroupCertificateAuthorityId = field("GroupCertificateAuthorityId")
    PemEncodedCertificate = field("PemEncodedCertificate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetGroupCertificateAuthorityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupCertificateAuthorityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupCertificateConfigurationResponse:
    boto3_raw_data: "type_defs.GetGroupCertificateConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityExpiryInMilliseconds = field(
        "CertificateAuthorityExpiryInMilliseconds"
    )
    CertificateExpiryInMilliseconds = field("CertificateExpiryInMilliseconds")
    GroupId = field("GroupId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetGroupCertificateConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupCertificateConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupResponse:
    boto3_raw_data: "type_defs.GetGroupResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoggerDefinitionResponse:
    boto3_raw_data: "type_defs.GetLoggerDefinitionResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoggerDefinitionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoggerDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceDefinitionResponse:
    boto3_raw_data: "type_defs.GetResourceDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceRoleForAccountResponse:
    boto3_raw_data: "type_defs.GetServiceRoleForAccountResponseTypeDef" = (
        dataclasses.field()
    )

    AssociatedAt = field("AssociatedAt")
    RoleArn = field("RoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServiceRoleForAccountResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceRoleForAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionDefinitionResponse:
    boto3_raw_data: "type_defs.GetSubscriptionDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")
    Id = field("Id")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LatestVersion = field("LatestVersion")
    LatestVersionArn = field("LatestVersionArn")
    Name = field("Name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSubscriptionDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionDefinitionResponseTypeDef"]
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
class ResetDeploymentsResponse:
    boto3_raw_data: "type_defs.ResetDeploymentsResponseTypeDef" = dataclasses.field()

    DeploymentArn = field("DeploymentArn")
    DeploymentId = field("DeploymentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetDeploymentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBulkDeploymentResponse:
    boto3_raw_data: "type_defs.StartBulkDeploymentResponseTypeDef" = dataclasses.field()

    BulkDeploymentArn = field("BulkDeploymentArn")
    BulkDeploymentId = field("BulkDeploymentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBulkDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBulkDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectivityInfoResponse:
    boto3_raw_data: "type_defs.UpdateConnectivityInfoResponseTypeDef" = (
        dataclasses.field()
    )

    Message = field("Message")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateConnectivityInfoResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectivityInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupCertificateConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateGroupCertificateConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityExpiryInMilliseconds = field(
        "CertificateAuthorityExpiryInMilliseconds"
    )
    CertificateExpiryInMilliseconds = field("CertificateExpiryInMilliseconds")
    GroupId = field("GroupId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateGroupCertificateConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupCertificateConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BulkDeploymentResult:
    boto3_raw_data: "type_defs.BulkDeploymentResultTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    DeploymentArn = field("DeploymentArn")
    DeploymentId = field("DeploymentId")
    DeploymentStatus = field("DeploymentStatus")
    DeploymentType = field("DeploymentType")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return ErrorDetail.make_many(self.boto3_raw_data["ErrorDetails"])

    ErrorMessage = field("ErrorMessage")
    GroupArn = field("GroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BulkDeploymentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BulkDeploymentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBulkDeploymentStatusResponse:
    boto3_raw_data: "type_defs.GetBulkDeploymentStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BulkDeploymentMetrics(self):  # pragma: no cover
        return BulkDeploymentMetrics.make_one(
            self.boto3_raw_data["BulkDeploymentMetrics"]
        )

    BulkDeploymentStatus = field("BulkDeploymentStatus")
    CreatedAt = field("CreatedAt")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return ErrorDetail.make_many(self.boto3_raw_data["ErrorDetails"])

    ErrorMessage = field("ErrorMessage")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBulkDeploymentStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBulkDeploymentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentStatusResponse:
    boto3_raw_data: "type_defs.GetDeploymentStatusResponseTypeDef" = dataclasses.field()

    DeploymentStatus = field("DeploymentStatus")
    DeploymentType = field("DeploymentType")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return ErrorDetail.make_many(self.boto3_raw_data["ErrorDetails"])

    ErrorMessage = field("ErrorMessage")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBulkDeploymentsResponse:
    boto3_raw_data: "type_defs.ListBulkDeploymentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def BulkDeployments(self):  # pragma: no cover
        return BulkDeployment.make_many(self.boto3_raw_data["BulkDeployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBulkDeploymentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBulkDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectivityInfoResponse:
    boto3_raw_data: "type_defs.GetConnectivityInfoResponseTypeDef" = dataclasses.field()

    @cached_property
    def ConnectivityInfo(self):  # pragma: no cover
        return ConnectivityInfo.make_many(self.boto3_raw_data["ConnectivityInfo"])

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectivityInfoResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectivityInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectivityInfoRequest:
    boto3_raw_data: "type_defs.UpdateConnectivityInfoRequestTypeDef" = (
        dataclasses.field()
    )

    ThingName = field("ThingName")

    @cached_property
    def ConnectivityInfo(self):  # pragma: no cover
        return ConnectivityInfo.make_many(self.boto3_raw_data["ConnectivityInfo"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateConnectivityInfoRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectivityInfoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorDefinitionVersionOutput:
    boto3_raw_data: "type_defs.ConnectorDefinitionVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Connectors(self):  # pragma: no cover
        return ConnectorOutput.make_many(self.boto3_raw_data["Connectors"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConnectorDefinitionVersionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorDefinitionVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorDefinitionVersion:
    boto3_raw_data: "type_defs.ConnectorDefinitionVersionTypeDef" = dataclasses.field()

    @cached_property
    def Connectors(self):  # pragma: no cover
        return Connector.make_many(self.boto3_raw_data["Connectors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorDefinitionVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorDefinitionVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreDefinitionVersionOutput:
    boto3_raw_data: "type_defs.CoreDefinitionVersionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Cores(self):  # pragma: no cover
        return Core.make_many(self.boto3_raw_data["Cores"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoreDefinitionVersionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreDefinitionVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoreDefinitionVersion:
    boto3_raw_data: "type_defs.CoreDefinitionVersionTypeDef" = dataclasses.field()

    @cached_property
    def Cores(self):  # pragma: no cover
        return Core.make_many(self.boto3_raw_data["Cores"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoreDefinitionVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoreDefinitionVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCoreDefinitionVersionRequest:
    boto3_raw_data: "type_defs.CreateCoreDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    CoreDefinitionId = field("CoreDefinitionId")
    AmznClientToken = field("AmznClientToken")

    @cached_property
    def Cores(self):  # pragma: no cover
        return Core.make_many(self.boto3_raw_data["Cores"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCoreDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCoreDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeviceDefinitionVersionRequest:
    boto3_raw_data: "type_defs.CreateDeviceDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    DeviceDefinitionId = field("DeviceDefinitionId")
    AmznClientToken = field("AmznClientToken")

    @cached_property
    def Devices(self):  # pragma: no cover
        return Device.make_many(self.boto3_raw_data["Devices"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDeviceDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeviceDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceDefinitionVersionOutput:
    boto3_raw_data: "type_defs.DeviceDefinitionVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Devices(self):  # pragma: no cover
        return Device.make_many(self.boto3_raw_data["Devices"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeviceDefinitionVersionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeviceDefinitionVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceDefinitionVersion:
    boto3_raw_data: "type_defs.DeviceDefinitionVersionTypeDef" = dataclasses.field()

    @cached_property
    def Devices(self):  # pragma: no cover
        return Device.make_many(self.boto3_raw_data["Devices"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeviceDefinitionVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeviceDefinitionVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupRequest:
    boto3_raw_data: "type_defs.CreateGroupRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    AmznClientToken = field("AmznClientToken")

    @cached_property
    def InitialVersion(self):  # pragma: no cover
        return GroupVersion.make_one(self.boto3_raw_data["InitialVersion"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupVersionResponse:
    boto3_raw_data: "type_defs.GetGroupVersionResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def Definition(self):  # pragma: no cover
        return GroupVersion.make_one(self.boto3_raw_data["Definition"])

    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoggerDefinitionVersionRequest:
    boto3_raw_data: "type_defs.CreateLoggerDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    LoggerDefinitionId = field("LoggerDefinitionId")
    AmznClientToken = field("AmznClientToken")

    @cached_property
    def Loggers(self):  # pragma: no cover
        return Logger.make_many(self.boto3_raw_data["Loggers"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLoggerDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoggerDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggerDefinitionVersionOutput:
    boto3_raw_data: "type_defs.LoggerDefinitionVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Loggers(self):  # pragma: no cover
        return Logger.make_many(self.boto3_raw_data["Loggers"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LoggerDefinitionVersionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggerDefinitionVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggerDefinitionVersion:
    boto3_raw_data: "type_defs.LoggerDefinitionVersionTypeDef" = dataclasses.field()

    @cached_property
    def Loggers(self):  # pragma: no cover
        return Logger.make_many(self.boto3_raw_data["Loggers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggerDefinitionVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggerDefinitionVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionDefinitionVersionRequest:
    boto3_raw_data: "type_defs.CreateSubscriptionDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionDefinitionId = field("SubscriptionDefinitionId")
    AmznClientToken = field("AmznClientToken")

    @cached_property
    def Subscriptions(self):  # pragma: no cover
        return Subscription.make_many(self.boto3_raw_data["Subscriptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSubscriptionDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionDefinitionVersionOutput:
    boto3_raw_data: "type_defs.SubscriptionDefinitionVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Subscriptions(self):  # pragma: no cover
        return Subscription.make_many(self.boto3_raw_data["Subscriptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SubscriptionDefinitionVersionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionDefinitionVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionDefinitionVersion:
    boto3_raw_data: "type_defs.SubscriptionDefinitionVersionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Subscriptions(self):  # pragma: no cover
        return Subscription.make_many(self.boto3_raw_data["Subscriptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SubscriptionDefinitionVersionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionDefinitionVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorDefinitionsResponse:
    boto3_raw_data: "type_defs.ListConnectorDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Definitions(self):  # pragma: no cover
        return DefinitionInformation.make_many(self.boto3_raw_data["Definitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConnectorDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreDefinitionsResponse:
    boto3_raw_data: "type_defs.ListCoreDefinitionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Definitions(self):  # pragma: no cover
        return DefinitionInformation.make_many(self.boto3_raw_data["Definitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoreDefinitionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeviceDefinitionsResponse:
    boto3_raw_data: "type_defs.ListDeviceDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Definitions(self):  # pragma: no cover
        return DefinitionInformation.make_many(self.boto3_raw_data["Definitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDeviceDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeviceDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionDefinitionsResponse:
    boto3_raw_data: "type_defs.ListFunctionDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Definitions(self):  # pragma: no cover
        return DefinitionInformation.make_many(self.boto3_raw_data["Definitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFunctionDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoggerDefinitionsResponse:
    boto3_raw_data: "type_defs.ListLoggerDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Definitions(self):  # pragma: no cover
        return DefinitionInformation.make_many(self.boto3_raw_data["Definitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLoggerDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoggerDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDefinitionsResponse:
    boto3_raw_data: "type_defs.ListResourceDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Definitions(self):  # pragma: no cover
        return DefinitionInformation.make_many(self.boto3_raw_data["Definitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionDefinitionsResponse:
    boto3_raw_data: "type_defs.ListSubscriptionDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Definitions(self):  # pragma: no cover
        return DefinitionInformation.make_many(self.boto3_raw_data["Definitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubscriptionDefinitionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsResponse:
    boto3_raw_data: "type_defs.ListDeploymentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Deployments(self):  # pragma: no cover
        return Deployment.make_many(self.boto3_raw_data["Deployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionDefaultExecutionConfig:
    boto3_raw_data: "type_defs.FunctionDefaultExecutionConfigTypeDef" = (
        dataclasses.field()
    )

    IsolationMode = field("IsolationMode")

    @cached_property
    def RunAs(self):  # pragma: no cover
        return FunctionRunAsConfig.make_one(self.boto3_raw_data["RunAs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FunctionDefaultExecutionConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionDefaultExecutionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionExecutionConfig:
    boto3_raw_data: "type_defs.FunctionExecutionConfigTypeDef" = dataclasses.field()

    IsolationMode = field("IsolationMode")

    @cached_property
    def RunAs(self):  # pragma: no cover
        return FunctionRunAsConfig.make_one(self.boto3_raw_data["RunAs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionExecutionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionExecutionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupCertificateAuthoritiesResponse:
    boto3_raw_data: "type_defs.ListGroupCertificateAuthoritiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GroupCertificateAuthorities(self):  # pragma: no cover
        return GroupCertificateAuthorityProperties.make_many(
            self.boto3_raw_data["GroupCertificateAuthorities"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroupCertificateAuthoritiesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupCertificateAuthoritiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsResponse:
    boto3_raw_data: "type_defs.ListGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupInformation.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalDeviceResourceData:
    boto3_raw_data: "type_defs.LocalDeviceResourceDataTypeDef" = dataclasses.field()

    @cached_property
    def GroupOwnerSetting(self):  # pragma: no cover
        return GroupOwnerSetting.make_one(self.boto3_raw_data["GroupOwnerSetting"])

    SourcePath = field("SourcePath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocalDeviceResourceDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocalDeviceResourceDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalVolumeResourceData:
    boto3_raw_data: "type_defs.LocalVolumeResourceDataTypeDef" = dataclasses.field()

    DestinationPath = field("DestinationPath")

    @cached_property
    def GroupOwnerSetting(self):  # pragma: no cover
        return GroupOwnerSetting.make_one(self.boto3_raw_data["GroupOwnerSetting"])

    SourcePath = field("SourcePath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocalVolumeResourceDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocalVolumeResourceDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBulkDeploymentDetailedReportsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListBulkDeploymentDetailedReportsRequestPaginateTypeDef"
    ) = dataclasses.field()

    BulkDeploymentId = field("BulkDeploymentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBulkDeploymentDetailedReportsRequestPaginateTypeDef"
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
                "type_defs.ListBulkDeploymentDetailedReportsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBulkDeploymentsRequestPaginate:
    boto3_raw_data: "type_defs.ListBulkDeploymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBulkDeploymentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBulkDeploymentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorDefinitionVersionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListConnectorDefinitionVersionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConnectorDefinitionId = field("ConnectorDefinitionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConnectorDefinitionVersionsRequestPaginateTypeDef"
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
                "type_defs.ListConnectorDefinitionVersionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListConnectorDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConnectorDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreDefinitionVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListCoreDefinitionVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CoreDefinitionId = field("CoreDefinitionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCoreDefinitionVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreDefinitionVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListCoreDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCoreDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsRequestPaginate:
    boto3_raw_data: "type_defs.ListDeploymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GroupId = field("GroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDeploymentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeviceDefinitionVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListDeviceDefinitionVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DeviceDefinitionId = field("DeviceDefinitionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeviceDefinitionVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeviceDefinitionVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeviceDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListDeviceDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeviceDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeviceDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionDefinitionVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListFunctionDefinitionVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FunctionDefinitionId = field("FunctionDefinitionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionDefinitionVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionDefinitionVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListFunctionDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GroupId = field("GroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGroupVersionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoggerDefinitionVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListLoggerDefinitionVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    LoggerDefinitionId = field("LoggerDefinitionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLoggerDefinitionVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoggerDefinitionVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoggerDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListLoggerDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLoggerDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoggerDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDefinitionVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceDefinitionVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceDefinitionId = field("ResourceDefinitionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceDefinitionVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDefinitionVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionDefinitionVersionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListSubscriptionDefinitionVersionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    SubscriptionDefinitionId = field("SubscriptionDefinitionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubscriptionDefinitionVersionsRequestPaginateTypeDef"
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
                "type_defs.ListSubscriptionDefinitionVersionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSubscriptionDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubscriptionDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorDefinitionVersionsResponse:
    boto3_raw_data: "type_defs.ListConnectorDefinitionVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Versions(self):  # pragma: no cover
        return VersionInformation.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConnectorDefinitionVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorDefinitionVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoreDefinitionVersionsResponse:
    boto3_raw_data: "type_defs.ListCoreDefinitionVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Versions(self):  # pragma: no cover
        return VersionInformation.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCoreDefinitionVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreDefinitionVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeviceDefinitionVersionsResponse:
    boto3_raw_data: "type_defs.ListDeviceDefinitionVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Versions(self):  # pragma: no cover
        return VersionInformation.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeviceDefinitionVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeviceDefinitionVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionDefinitionVersionsResponse:
    boto3_raw_data: "type_defs.ListFunctionDefinitionVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Versions(self):  # pragma: no cover
        return VersionInformation.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionDefinitionVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionDefinitionVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupVersionsResponse:
    boto3_raw_data: "type_defs.ListGroupVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Versions(self):  # pragma: no cover
        return VersionInformation.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoggerDefinitionVersionsResponse:
    boto3_raw_data: "type_defs.ListLoggerDefinitionVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Versions(self):  # pragma: no cover
        return VersionInformation.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLoggerDefinitionVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoggerDefinitionVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDefinitionVersionsResponse:
    boto3_raw_data: "type_defs.ListResourceDefinitionVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Versions(self):  # pragma: no cover
        return VersionInformation.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceDefinitionVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDefinitionVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionDefinitionVersionsResponse:
    boto3_raw_data: "type_defs.ListSubscriptionDefinitionVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Versions(self):  # pragma: no cover
        return VersionInformation.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubscriptionDefinitionVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionDefinitionVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3MachineLearningModelResourceData:
    boto3_raw_data: "type_defs.S3MachineLearningModelResourceDataTypeDef" = (
        dataclasses.field()
    )

    DestinationPath = field("DestinationPath")

    @cached_property
    def OwnerSetting(self):  # pragma: no cover
        return ResourceDownloadOwnerSetting.make_one(
            self.boto3_raw_data["OwnerSetting"]
        )

    S3Uri = field("S3Uri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3MachineLearningModelResourceDataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3MachineLearningModelResourceDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerMachineLearningModelResourceData:
    boto3_raw_data: "type_defs.SageMakerMachineLearningModelResourceDataTypeDef" = (
        dataclasses.field()
    )

    DestinationPath = field("DestinationPath")

    @cached_property
    def OwnerSetting(self):  # pragma: no cover
        return ResourceDownloadOwnerSetting.make_one(
            self.boto3_raw_data["OwnerSetting"]
        )

    SageMakerJobArn = field("SageMakerJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SageMakerMachineLearningModelResourceDataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerMachineLearningModelResourceDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeConfiguration:
    boto3_raw_data: "type_defs.RuntimeConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def TelemetryConfiguration(self):  # pragma: no cover
        return TelemetryConfiguration.make_one(
            self.boto3_raw_data["TelemetryConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThingRuntimeConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateThingRuntimeConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ThingName = field("ThingName")

    @cached_property
    def TelemetryConfiguration(self):  # pragma: no cover
        return TelemetryConfigurationUpdate.make_one(
            self.boto3_raw_data["TelemetryConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateThingRuntimeConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThingRuntimeConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBulkDeploymentDetailedReportsResponse:
    boto3_raw_data: "type_defs.ListBulkDeploymentDetailedReportsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Deployments(self):  # pragma: no cover
        return BulkDeploymentResult.make_many(self.boto3_raw_data["Deployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBulkDeploymentDetailedReportsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBulkDeploymentDetailedReportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectorDefinitionVersionResponse:
    boto3_raw_data: "type_defs.GetConnectorDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def Definition(self):  # pragma: no cover
        return ConnectorDefinitionVersionOutput.make_one(
            self.boto3_raw_data["Definition"]
        )

    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConnectorDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectorDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorDefinitionVersionRequest:
    boto3_raw_data: "type_defs.CreateConnectorDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectorDefinitionId = field("ConnectorDefinitionId")
    AmznClientToken = field("AmznClientToken")
    Connectors = field("Connectors")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConnectorDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreDefinitionVersionResponse:
    boto3_raw_data: "type_defs.GetCoreDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def Definition(self):  # pragma: no cover
        return CoreDefinitionVersionOutput.make_one(self.boto3_raw_data["Definition"])

    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCoreDefinitionVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceDefinitionVersionResponse:
    boto3_raw_data: "type_defs.GetDeviceDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def Definition(self):  # pragma: no cover
        return DeviceDefinitionVersionOutput.make_one(self.boto3_raw_data["Definition"])

    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeviceDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoggerDefinitionVersionResponse:
    boto3_raw_data: "type_defs.GetLoggerDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def Definition(self):  # pragma: no cover
        return LoggerDefinitionVersionOutput.make_one(self.boto3_raw_data["Definition"])

    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLoggerDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoggerDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionDefinitionVersionResponse:
    boto3_raw_data: "type_defs.GetSubscriptionDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def Definition(self):  # pragma: no cover
        return SubscriptionDefinitionVersionOutput.make_one(
            self.boto3_raw_data["Definition"]
        )

    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSubscriptionDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionDefaultConfig:
    boto3_raw_data: "type_defs.FunctionDefaultConfigTypeDef" = dataclasses.field()

    @cached_property
    def Execution(self):  # pragma: no cover
        return FunctionDefaultExecutionConfig.make_one(self.boto3_raw_data["Execution"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionDefaultConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionDefaultConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionConfigurationEnvironmentOutput:
    boto3_raw_data: "type_defs.FunctionConfigurationEnvironmentOutputTypeDef" = (
        dataclasses.field()
    )

    AccessSysfs = field("AccessSysfs")

    @cached_property
    def Execution(self):  # pragma: no cover
        return FunctionExecutionConfig.make_one(self.boto3_raw_data["Execution"])

    @cached_property
    def ResourceAccessPolicies(self):  # pragma: no cover
        return ResourceAccessPolicy.make_many(
            self.boto3_raw_data["ResourceAccessPolicies"]
        )

    Variables = field("Variables")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FunctionConfigurationEnvironmentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionConfigurationEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionConfigurationEnvironment:
    boto3_raw_data: "type_defs.FunctionConfigurationEnvironmentTypeDef" = (
        dataclasses.field()
    )

    AccessSysfs = field("AccessSysfs")

    @cached_property
    def Execution(self):  # pragma: no cover
        return FunctionExecutionConfig.make_one(self.boto3_raw_data["Execution"])

    @cached_property
    def ResourceAccessPolicies(self):  # pragma: no cover
        return ResourceAccessPolicy.make_many(
            self.boto3_raw_data["ResourceAccessPolicies"]
        )

    Variables = field("Variables")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FunctionConfigurationEnvironmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionConfigurationEnvironmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataContainerOutput:
    boto3_raw_data: "type_defs.ResourceDataContainerOutputTypeDef" = dataclasses.field()

    @cached_property
    def LocalDeviceResourceData(self):  # pragma: no cover
        return LocalDeviceResourceData.make_one(
            self.boto3_raw_data["LocalDeviceResourceData"]
        )

    @cached_property
    def LocalVolumeResourceData(self):  # pragma: no cover
        return LocalVolumeResourceData.make_one(
            self.boto3_raw_data["LocalVolumeResourceData"]
        )

    @cached_property
    def S3MachineLearningModelResourceData(self):  # pragma: no cover
        return S3MachineLearningModelResourceData.make_one(
            self.boto3_raw_data["S3MachineLearningModelResourceData"]
        )

    @cached_property
    def SageMakerMachineLearningModelResourceData(self):  # pragma: no cover
        return SageMakerMachineLearningModelResourceData.make_one(
            self.boto3_raw_data["SageMakerMachineLearningModelResourceData"]
        )

    @cached_property
    def SecretsManagerSecretResourceData(self):  # pragma: no cover
        return SecretsManagerSecretResourceDataOutput.make_one(
            self.boto3_raw_data["SecretsManagerSecretResourceData"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceDataContainerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataContainerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThingRuntimeConfigurationResponse:
    boto3_raw_data: "type_defs.GetThingRuntimeConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RuntimeConfiguration(self):  # pragma: no cover
        return RuntimeConfiguration.make_one(
            self.boto3_raw_data["RuntimeConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetThingRuntimeConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThingRuntimeConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataContainer:
    boto3_raw_data: "type_defs.ResourceDataContainerTypeDef" = dataclasses.field()

    @cached_property
    def LocalDeviceResourceData(self):  # pragma: no cover
        return LocalDeviceResourceData.make_one(
            self.boto3_raw_data["LocalDeviceResourceData"]
        )

    @cached_property
    def LocalVolumeResourceData(self):  # pragma: no cover
        return LocalVolumeResourceData.make_one(
            self.boto3_raw_data["LocalVolumeResourceData"]
        )

    @cached_property
    def S3MachineLearningModelResourceData(self):  # pragma: no cover
        return S3MachineLearningModelResourceData.make_one(
            self.boto3_raw_data["S3MachineLearningModelResourceData"]
        )

    @cached_property
    def SageMakerMachineLearningModelResourceData(self):  # pragma: no cover
        return SageMakerMachineLearningModelResourceData.make_one(
            self.boto3_raw_data["SageMakerMachineLearningModelResourceData"]
        )

    SecretsManagerSecretResourceData = field("SecretsManagerSecretResourceData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceDataContainerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataContainerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorDefinitionRequest:
    boto3_raw_data: "type_defs.CreateConnectorDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    AmznClientToken = field("AmznClientToken")
    InitialVersion = field("InitialVersion")
    Name = field("Name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConnectorDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCoreDefinitionRequest:
    boto3_raw_data: "type_defs.CreateCoreDefinitionRequestTypeDef" = dataclasses.field()

    AmznClientToken = field("AmznClientToken")
    InitialVersion = field("InitialVersion")
    Name = field("Name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCoreDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCoreDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeviceDefinitionRequest:
    boto3_raw_data: "type_defs.CreateDeviceDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    AmznClientToken = field("AmznClientToken")
    InitialVersion = field("InitialVersion")
    Name = field("Name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDeviceDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeviceDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoggerDefinitionRequest:
    boto3_raw_data: "type_defs.CreateLoggerDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    AmznClientToken = field("AmznClientToken")
    InitialVersion = field("InitialVersion")
    Name = field("Name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLoggerDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoggerDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionDefinitionRequest:
    boto3_raw_data: "type_defs.CreateSubscriptionDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    AmznClientToken = field("AmznClientToken")
    InitialVersion = field("InitialVersion")
    Name = field("Name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSubscriptionDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionConfigurationOutput:
    boto3_raw_data: "type_defs.FunctionConfigurationOutputTypeDef" = dataclasses.field()

    EncodingType = field("EncodingType")

    @cached_property
    def Environment(self):  # pragma: no cover
        return FunctionConfigurationEnvironmentOutput.make_one(
            self.boto3_raw_data["Environment"]
        )

    ExecArgs = field("ExecArgs")
    Executable = field("Executable")
    MemorySize = field("MemorySize")
    Pinned = field("Pinned")
    Timeout = field("Timeout")
    FunctionRuntimeOverride = field("FunctionRuntimeOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceOutput:
    boto3_raw_data: "type_defs.ResourceOutputTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def ResourceDataContainer(self):  # pragma: no cover
        return ResourceDataContainerOutput.make_one(
            self.boto3_raw_data["ResourceDataContainer"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionOutput:
    boto3_raw_data: "type_defs.FunctionOutputTypeDef" = dataclasses.field()

    Id = field("Id")
    FunctionArn = field("FunctionArn")

    @cached_property
    def FunctionConfiguration(self):  # pragma: no cover
        return FunctionConfigurationOutput.make_one(
            self.boto3_raw_data["FunctionConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionConfiguration:
    boto3_raw_data: "type_defs.FunctionConfigurationTypeDef" = dataclasses.field()

    EncodingType = field("EncodingType")
    Environment = field("Environment")
    ExecArgs = field("ExecArgs")
    Executable = field("Executable")
    MemorySize = field("MemorySize")
    Pinned = field("Pinned")
    Timeout = field("Timeout")
    FunctionRuntimeOverride = field("FunctionRuntimeOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDefinitionVersionOutput:
    boto3_raw_data: "type_defs.ResourceDefinitionVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Resources(self):  # pragma: no cover
        return ResourceOutput.make_many(self.boto3_raw_data["Resources"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResourceDefinitionVersionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDefinitionVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    ResourceDataContainer = field("ResourceDataContainer")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionDefinitionVersionOutput:
    boto3_raw_data: "type_defs.FunctionDefinitionVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DefaultConfig(self):  # pragma: no cover
        return FunctionDefaultConfig.make_one(self.boto3_raw_data["DefaultConfig"])

    @cached_property
    def Functions(self):  # pragma: no cover
        return FunctionOutput.make_many(self.boto3_raw_data["Functions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FunctionDefinitionVersionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionDefinitionVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceDefinitionVersionResponse:
    boto3_raw_data: "type_defs.GetResourceDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def Definition(self):  # pragma: no cover
        return ResourceDefinitionVersionOutput.make_one(
            self.boto3_raw_data["Definition"]
        )

    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResourceDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDefinitionVersion:
    boto3_raw_data: "type_defs.ResourceDefinitionVersionTypeDef" = dataclasses.field()

    @cached_property
    def Resources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["Resources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceDefinitionVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDefinitionVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionDefinitionVersionResponse:
    boto3_raw_data: "type_defs.GetFunctionDefinitionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def Definition(self):  # pragma: no cover
        return FunctionDefinitionVersionOutput.make_one(
            self.boto3_raw_data["Definition"]
        )

    Id = field("Id")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionDefinitionVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionDefinitionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Function:
    boto3_raw_data: "type_defs.FunctionTypeDef" = dataclasses.field()

    Id = field("Id")
    FunctionArn = field("FunctionArn")
    FunctionConfiguration = field("FunctionConfiguration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceDefinitionVersionRequest:
    boto3_raw_data: "type_defs.CreateResourceDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceDefinitionId = field("ResourceDefinitionId")
    AmznClientToken = field("AmznClientToken")
    Resources = field("Resources")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResourceDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionDefinitionVersion:
    boto3_raw_data: "type_defs.FunctionDefinitionVersionTypeDef" = dataclasses.field()

    @cached_property
    def DefaultConfig(self):  # pragma: no cover
        return FunctionDefaultConfig.make_one(self.boto3_raw_data["DefaultConfig"])

    @cached_property
    def Functions(self):  # pragma: no cover
        return Function.make_many(self.boto3_raw_data["Functions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionDefinitionVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionDefinitionVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceDefinitionRequest:
    boto3_raw_data: "type_defs.CreateResourceDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    AmznClientToken = field("AmznClientToken")
    InitialVersion = field("InitialVersion")
    Name = field("Name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResourceDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionDefinitionVersionRequest:
    boto3_raw_data: "type_defs.CreateFunctionDefinitionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionDefinitionId = field("FunctionDefinitionId")
    AmznClientToken = field("AmznClientToken")

    @cached_property
    def DefaultConfig(self):  # pragma: no cover
        return FunctionDefaultConfig.make_one(self.boto3_raw_data["DefaultConfig"])

    Functions = field("Functions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFunctionDefinitionVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionDefinitionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionDefinitionRequest:
    boto3_raw_data: "type_defs.CreateFunctionDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    AmznClientToken = field("AmznClientToken")
    InitialVersion = field("InitialVersion")
    Name = field("Name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFunctionDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
