# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_proton import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptEnvironmentAccountConnectionInput:
    boto3_raw_data: "type_defs.AcceptEnvironmentAccountConnectionInputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptEnvironmentAccountConnectionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptEnvironmentAccountConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentAccountConnection:
    boto3_raw_data: "type_defs.EnvironmentAccountConnectionTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    environmentAccountId = field("environmentAccountId")
    environmentName = field("environmentName")
    id = field("id")
    lastModifiedAt = field("lastModifiedAt")
    managementAccountId = field("managementAccountId")
    requestedAt = field("requestedAt")
    roleArn = field("roleArn")
    status = field("status")
    codebuildRoleArn = field("codebuildRoleArn")
    componentRoleArn = field("componentRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentAccountConnectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentAccountConnectionTypeDef"]
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
class RepositoryBranch:
    boto3_raw_data: "type_defs.RepositoryBranchTypeDef" = dataclasses.field()

    arn = field("arn")
    branch = field("branch")
    name = field("name")
    provider = field("provider")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RepositoryBranchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryBranchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelComponentDeploymentInput:
    boto3_raw_data: "type_defs.CancelComponentDeploymentInputTypeDef" = (
        dataclasses.field()
    )

    componentName = field("componentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelComponentDeploymentInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelComponentDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Component:
    boto3_raw_data: "type_defs.ComponentTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    deploymentStatus = field("deploymentStatus")
    environmentName = field("environmentName")
    lastModifiedAt = field("lastModifiedAt")
    name = field("name")
    deploymentStatusMessage = field("deploymentStatusMessage")
    description = field("description")
    lastAttemptedDeploymentId = field("lastAttemptedDeploymentId")
    lastClientRequestToken = field("lastClientRequestToken")
    lastDeploymentAttemptedAt = field("lastDeploymentAttemptedAt")
    lastDeploymentSucceededAt = field("lastDeploymentSucceededAt")
    lastSucceededDeploymentId = field("lastSucceededDeploymentId")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")
    serviceSpec = field("serviceSpec")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComponentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelEnvironmentDeploymentInput:
    boto3_raw_data: "type_defs.CancelEnvironmentDeploymentInputTypeDef" = (
        dataclasses.field()
    )

    environmentName = field("environmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelEnvironmentDeploymentInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelEnvironmentDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelServiceInstanceDeploymentInput:
    boto3_raw_data: "type_defs.CancelServiceInstanceDeploymentInputTypeDef" = (
        dataclasses.field()
    )

    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelServiceInstanceDeploymentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelServiceInstanceDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceInstance:
    boto3_raw_data: "type_defs.ServiceInstanceTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    deploymentStatus = field("deploymentStatus")
    environmentName = field("environmentName")
    lastDeploymentAttemptedAt = field("lastDeploymentAttemptedAt")
    lastDeploymentSucceededAt = field("lastDeploymentSucceededAt")
    name = field("name")
    serviceName = field("serviceName")
    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")
    templateName = field("templateName")
    deploymentStatusMessage = field("deploymentStatusMessage")
    lastAttemptedDeploymentId = field("lastAttemptedDeploymentId")
    lastClientRequestToken = field("lastClientRequestToken")
    lastSucceededDeploymentId = field("lastSucceededDeploymentId")
    spec = field("spec")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelServicePipelineDeploymentInput:
    boto3_raw_data: "type_defs.CancelServicePipelineDeploymentInputTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelServicePipelineDeploymentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelServicePipelineDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServicePipeline:
    boto3_raw_data: "type_defs.ServicePipelineTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    deploymentStatus = field("deploymentStatus")
    lastDeploymentAttemptedAt = field("lastDeploymentAttemptedAt")
    lastDeploymentSucceededAt = field("lastDeploymentSucceededAt")
    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")
    templateName = field("templateName")
    deploymentStatusMessage = field("deploymentStatusMessage")
    lastAttemptedDeploymentId = field("lastAttemptedDeploymentId")
    lastSucceededDeploymentId = field("lastSucceededDeploymentId")
    spec = field("spec")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServicePipelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServicePipelineTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompatibleEnvironmentTemplateInput:
    boto3_raw_data: "type_defs.CompatibleEnvironmentTemplateInputTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompatibleEnvironmentTemplateInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompatibleEnvironmentTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompatibleEnvironmentTemplate:
    boto3_raw_data: "type_defs.CompatibleEnvironmentTemplateTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CompatibleEnvironmentTemplateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompatibleEnvironmentTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentState:
    boto3_raw_data: "type_defs.ComponentStateTypeDef" = dataclasses.field()

    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")
    serviceSpec = field("serviceSpec")
    templateFile = field("templateFile")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComponentStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentSummary:
    boto3_raw_data: "type_defs.ComponentSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    deploymentStatus = field("deploymentStatus")
    environmentName = field("environmentName")
    lastModifiedAt = field("lastModifiedAt")
    name = field("name")
    deploymentStatusMessage = field("deploymentStatusMessage")
    lastAttemptedDeploymentId = field("lastAttemptedDeploymentId")
    lastDeploymentAttemptedAt = field("lastDeploymentAttemptedAt")
    lastDeploymentSucceededAt = field("lastDeploymentSucceededAt")
    lastSucceededDeploymentId = field("lastSucceededDeploymentId")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceCountsSummary:
    boto3_raw_data: "type_defs.ResourceCountsSummaryTypeDef" = dataclasses.field()

    total = field("total")
    behindMajor = field("behindMajor")
    behindMinor = field("behindMinor")
    failed = field("failed")
    upToDate = field("upToDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceCountsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceCountsSummaryTypeDef"]
        ],
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
class RepositoryBranchInput:
    boto3_raw_data: "type_defs.RepositoryBranchInputTypeDef" = dataclasses.field()

    branch = field("branch")
    name = field("name")
    provider = field("provider")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryBranchInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryBranchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentTemplate:
    boto3_raw_data: "type_defs.EnvironmentTemplateTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    name = field("name")
    description = field("description")
    displayName = field("displayName")
    encryptionKey = field("encryptionKey")
    provisioning = field("provisioning")
    recommendedVersion = field("recommendedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentTemplateVersion:
    boto3_raw_data: "type_defs.EnvironmentTemplateVersionTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    status = field("status")
    templateName = field("templateName")
    description = field("description")
    recommendedMinorVersion = field("recommendedMinorVersion")
    schema = field("schema")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentTemplateVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentTemplateVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Repository:
    boto3_raw_data: "type_defs.RepositoryTypeDef" = dataclasses.field()

    arn = field("arn")
    connectionArn = field("connectionArn")
    name = field("name")
    provider = field("provider")
    encryptionKey = field("encryptionKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RepositoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RepositoryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceSyncConfigInput:
    boto3_raw_data: "type_defs.CreateServiceSyncConfigInputTypeDef" = (
        dataclasses.field()
    )

    branch = field("branch")
    filePath = field("filePath")
    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceSyncConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceSyncConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSyncConfig:
    boto3_raw_data: "type_defs.ServiceSyncConfigTypeDef" = dataclasses.field()

    branch = field("branch")
    filePath = field("filePath")
    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    serviceName = field("serviceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceSyncConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceSyncConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceTemplate:
    boto3_raw_data: "type_defs.ServiceTemplateTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    name = field("name")
    description = field("description")
    displayName = field("displayName")
    encryptionKey = field("encryptionKey")
    pipelineProvisioning = field("pipelineProvisioning")
    recommendedVersion = field("recommendedVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceTemplateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateSyncConfigInput:
    boto3_raw_data: "type_defs.CreateTemplateSyncConfigInputTypeDef" = (
        dataclasses.field()
    )

    branch = field("branch")
    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    templateName = field("templateName")
    templateType = field("templateType")
    subdirectory = field("subdirectory")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateTemplateSyncConfigInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateSyncConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateSyncConfig:
    boto3_raw_data: "type_defs.TemplateSyncConfigTypeDef" = dataclasses.field()

    branch = field("branch")
    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    templateName = field("templateName")
    templateType = field("templateType")
    subdirectory = field("subdirectory")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateSyncConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateSyncConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComponentInput:
    boto3_raw_data: "type_defs.DeleteComponentInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteComponentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComponentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeploymentInput:
    boto3_raw_data: "type_defs.DeleteDeploymentInputTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeploymentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentAccountConnectionInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentAccountConnectionInputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEnvironmentAccountConnectionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentAccountConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentTemplateInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentTemplateInputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentTemplateVersionInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentTemplateVersionInputTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEnvironmentTemplateVersionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentTemplateVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryInput:
    boto3_raw_data: "type_defs.DeleteRepositoryInputTypeDef" = dataclasses.field()

    name = field("name")
    provider = field("provider")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRepositoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceInput:
    boto3_raw_data: "type_defs.DeleteServiceInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceSyncConfigInput:
    boto3_raw_data: "type_defs.DeleteServiceSyncConfigInputTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceSyncConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceSyncConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceTemplateInput:
    boto3_raw_data: "type_defs.DeleteServiceTemplateInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceTemplateVersionInput:
    boto3_raw_data: "type_defs.DeleteServiceTemplateVersionInputTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceTemplateVersionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceTemplateVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTemplateSyncConfigInput:
    boto3_raw_data: "type_defs.DeleteTemplateSyncConfigInputTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    templateType = field("templateType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTemplateSyncConfigInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTemplateSyncConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentState:
    boto3_raw_data: "type_defs.EnvironmentStateTypeDef" = dataclasses.field()

    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")
    templateName = field("templateName")
    spec = field("spec")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceInstanceState:
    boto3_raw_data: "type_defs.ServiceInstanceStateTypeDef" = dataclasses.field()

    spec = field("spec")
    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")
    templateName = field("templateName")
    lastSuccessfulComponentDeploymentIds = field("lastSuccessfulComponentDeploymentIds")
    lastSuccessfulEnvironmentDeploymentId = field(
        "lastSuccessfulEnvironmentDeploymentId"
    )
    lastSuccessfulServicePipelineDeploymentId = field(
        "lastSuccessfulServicePipelineDeploymentId"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceInstanceStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceInstanceStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServicePipelineState:
    boto3_raw_data: "type_defs.ServicePipelineStateTypeDef" = dataclasses.field()

    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")
    templateName = field("templateName")
    spec = field("spec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServicePipelineStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServicePipelineStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentSummary:
    boto3_raw_data: "type_defs.DeploymentSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    deploymentStatus = field("deploymentStatus")
    environmentName = field("environmentName")
    id = field("id")
    lastModifiedAt = field("lastModifiedAt")
    targetArn = field("targetArn")
    targetResourceCreatedAt = field("targetResourceCreatedAt")
    targetResourceType = field("targetResourceType")
    completedAt = field("completedAt")
    componentName = field("componentName")
    lastAttemptedDeploymentId = field("lastAttemptedDeploymentId")
    lastSucceededDeploymentId = field("lastSucceededDeploymentId")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentAccountConnectionSummary:
    boto3_raw_data: "type_defs.EnvironmentAccountConnectionSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    environmentAccountId = field("environmentAccountId")
    environmentName = field("environmentName")
    id = field("id")
    lastModifiedAt = field("lastModifiedAt")
    managementAccountId = field("managementAccountId")
    requestedAt = field("requestedAt")
    roleArn = field("roleArn")
    status = field("status")
    componentRoleArn = field("componentRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentAccountConnectionSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentAccountConnectionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentSummary:
    boto3_raw_data: "type_defs.EnvironmentSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    deploymentStatus = field("deploymentStatus")
    lastDeploymentAttemptedAt = field("lastDeploymentAttemptedAt")
    lastDeploymentSucceededAt = field("lastDeploymentSucceededAt")
    name = field("name")
    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")
    templateName = field("templateName")
    componentRoleArn = field("componentRoleArn")
    deploymentStatusMessage = field("deploymentStatusMessage")
    description = field("description")
    environmentAccountConnectionId = field("environmentAccountConnectionId")
    environmentAccountId = field("environmentAccountId")
    lastAttemptedDeploymentId = field("lastAttemptedDeploymentId")
    lastSucceededDeploymentId = field("lastSucceededDeploymentId")
    protonServiceRoleArn = field("protonServiceRoleArn")
    provisioning = field("provisioning")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentTemplateFilter:
    boto3_raw_data: "type_defs.EnvironmentTemplateFilterTypeDef" = dataclasses.field()

    majorVersion = field("majorVersion")
    templateName = field("templateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentTemplateFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentTemplateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentTemplateSummary:
    boto3_raw_data: "type_defs.EnvironmentTemplateSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    name = field("name")
    description = field("description")
    displayName = field("displayName")
    provisioning = field("provisioning")
    recommendedVersion = field("recommendedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentTemplateVersionSummary:
    boto3_raw_data: "type_defs.EnvironmentTemplateVersionSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    status = field("status")
    templateName = field("templateName")
    description = field("description")
    recommendedMinorVersion = field("recommendedMinorVersion")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentTemplateVersionSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentTemplateVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentInput:
    boto3_raw_data: "type_defs.GetComponentInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetComponentInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentInput:
    boto3_raw_data: "type_defs.GetDeploymentInputTypeDef" = dataclasses.field()

    id = field("id")
    componentName = field("componentName")
    environmentName = field("environmentName")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentAccountConnectionInput:
    boto3_raw_data: "type_defs.GetEnvironmentAccountConnectionInputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnvironmentAccountConnectionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentAccountConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentInput:
    boto3_raw_data: "type_defs.GetEnvironmentInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentTemplateInput:
    boto3_raw_data: "type_defs.GetEnvironmentTemplateInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentTemplateVersionInput:
    boto3_raw_data: "type_defs.GetEnvironmentTemplateVersionInputTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnvironmentTemplateVersionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentTemplateVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryInput:
    boto3_raw_data: "type_defs.GetRepositoryInputTypeDef" = dataclasses.field()

    name = field("name")
    provider = field("provider")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositorySyncStatusInput:
    boto3_raw_data: "type_defs.GetRepositorySyncStatusInputTypeDef" = (
        dataclasses.field()
    )

    branch = field("branch")
    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    syncType = field("syncType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositorySyncStatusInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositorySyncStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInput:
    boto3_raw_data: "type_defs.GetServiceInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetServiceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetServiceInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInstanceInput:
    boto3_raw_data: "type_defs.GetServiceInstanceInputTypeDef" = dataclasses.field()

    name = field("name")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInstanceSyncStatusInput:
    boto3_raw_data: "type_defs.GetServiceInstanceSyncStatusInputTypeDef" = (
        dataclasses.field()
    )

    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceInstanceSyncStatusInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceInstanceSyncStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Revision:
    boto3_raw_data: "type_defs.RevisionTypeDef" = dataclasses.field()

    branch = field("branch")
    directory = field("directory")
    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    sha = field("sha")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RevisionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceSyncBlockerSummaryInput:
    boto3_raw_data: "type_defs.GetServiceSyncBlockerSummaryInputTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")
    serviceInstanceName = field("serviceInstanceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceSyncBlockerSummaryInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceSyncBlockerSummaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceSyncConfigInput:
    boto3_raw_data: "type_defs.GetServiceSyncConfigInputTypeDef" = dataclasses.field()

    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceSyncConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceSyncConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceTemplateInput:
    boto3_raw_data: "type_defs.GetServiceTemplateInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceTemplateVersionInput:
    boto3_raw_data: "type_defs.GetServiceTemplateVersionInputTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServiceTemplateVersionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceTemplateVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateSyncConfigInput:
    boto3_raw_data: "type_defs.GetTemplateSyncConfigInputTypeDef" = dataclasses.field()

    templateName = field("templateName")
    templateType = field("templateType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateSyncConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateSyncConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateSyncStatusInput:
    boto3_raw_data: "type_defs.GetTemplateSyncStatusInputTypeDef" = dataclasses.field()

    templateName = field("templateName")
    templateType = field("templateType")
    templateVersion = field("templateVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateSyncStatusInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateSyncStatusInputTypeDef"]
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
class ListComponentOutputsInput:
    boto3_raw_data: "type_defs.ListComponentOutputsInputTypeDef" = dataclasses.field()

    componentName = field("componentName")
    deploymentId = field("deploymentId")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentOutputsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentOutputsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Output:
    boto3_raw_data: "type_defs.OutputTypeDef" = dataclasses.field()

    key = field("key")
    valueString = field("valueString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentProvisionedResourcesInput:
    boto3_raw_data: "type_defs.ListComponentProvisionedResourcesInputTypeDef" = (
        dataclasses.field()
    )

    componentName = field("componentName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComponentProvisionedResourcesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentProvisionedResourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedResource:
    boto3_raw_data: "type_defs.ProvisionedResourceTypeDef" = dataclasses.field()

    identifier = field("identifier")
    name = field("name")
    provisioningEngine = field("provisioningEngine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsInput:
    boto3_raw_data: "type_defs.ListComponentsInputTypeDef" = dataclasses.field()

    environmentName = field("environmentName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsInput:
    boto3_raw_data: "type_defs.ListDeploymentsInputTypeDef" = dataclasses.field()

    componentName = field("componentName")
    environmentName = field("environmentName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentAccountConnectionsInput:
    boto3_raw_data: "type_defs.ListEnvironmentAccountConnectionsInputTypeDef" = (
        dataclasses.field()
    )

    requestedBy = field("requestedBy")
    environmentName = field("environmentName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    statuses = field("statuses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentAccountConnectionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentAccountConnectionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentOutputsInput:
    boto3_raw_data: "type_defs.ListEnvironmentOutputsInputTypeDef" = dataclasses.field()

    environmentName = field("environmentName")
    deploymentId = field("deploymentId")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentOutputsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentOutputsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentProvisionedResourcesInput:
    boto3_raw_data: "type_defs.ListEnvironmentProvisionedResourcesInputTypeDef" = (
        dataclasses.field()
    )

    environmentName = field("environmentName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentProvisionedResourcesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentProvisionedResourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentTemplateVersionsInput:
    boto3_raw_data: "type_defs.ListEnvironmentTemplateVersionsInputTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    majorVersion = field("majorVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentTemplateVersionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentTemplateVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentTemplatesInput:
    boto3_raw_data: "type_defs.ListEnvironmentTemplatesInputTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentTemplatesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesInput:
    boto3_raw_data: "type_defs.ListRepositoriesInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRepositoriesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositorySummary:
    boto3_raw_data: "type_defs.RepositorySummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    connectionArn = field("connectionArn")
    name = field("name")
    provider = field("provider")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RepositorySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositorySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositorySyncDefinitionsInput:
    boto3_raw_data: "type_defs.ListRepositorySyncDefinitionsInputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    syncType = field("syncType")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositorySyncDefinitionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositorySyncDefinitionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositorySyncDefinition:
    boto3_raw_data: "type_defs.RepositorySyncDefinitionTypeDef" = dataclasses.field()

    branch = field("branch")
    directory = field("directory")
    parent = field("parent")
    target = field("target")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositorySyncDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositorySyncDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstanceOutputsInput:
    boto3_raw_data: "type_defs.ListServiceInstanceOutputsInputTypeDef" = (
        dataclasses.field()
    )

    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")
    deploymentId = field("deploymentId")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceInstanceOutputsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceInstanceOutputsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstanceProvisionedResourcesInput:
    boto3_raw_data: "type_defs.ListServiceInstanceProvisionedResourcesInputTypeDef" = (
        dataclasses.field()
    )

    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceInstanceProvisionedResourcesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceInstanceProvisionedResourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstancesFilter:
    boto3_raw_data: "type_defs.ListServiceInstancesFilterTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceInstancesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceInstancesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceInstanceSummary:
    boto3_raw_data: "type_defs.ServiceInstanceSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    deploymentStatus = field("deploymentStatus")
    environmentName = field("environmentName")
    lastDeploymentAttemptedAt = field("lastDeploymentAttemptedAt")
    lastDeploymentSucceededAt = field("lastDeploymentSucceededAt")
    name = field("name")
    serviceName = field("serviceName")
    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")
    templateName = field("templateName")
    deploymentStatusMessage = field("deploymentStatusMessage")
    lastAttemptedDeploymentId = field("lastAttemptedDeploymentId")
    lastSucceededDeploymentId = field("lastSucceededDeploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceInstanceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceInstanceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicePipelineOutputsInput:
    boto3_raw_data: "type_defs.ListServicePipelineOutputsInputTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")
    deploymentId = field("deploymentId")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServicePipelineOutputsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicePipelineOutputsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicePipelineProvisionedResourcesInput:
    boto3_raw_data: "type_defs.ListServicePipelineProvisionedResourcesInputTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServicePipelineProvisionedResourcesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicePipelineProvisionedResourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceTemplateVersionsInput:
    boto3_raw_data: "type_defs.ListServiceTemplateVersionsInputTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    majorVersion = field("majorVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceTemplateVersionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceTemplateVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceTemplateVersionSummary:
    boto3_raw_data: "type_defs.ServiceTemplateVersionSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    status = field("status")
    templateName = field("templateName")
    description = field("description")
    recommendedMinorVersion = field("recommendedMinorVersion")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceTemplateVersionSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceTemplateVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceTemplatesInput:
    boto3_raw_data: "type_defs.ListServiceTemplatesInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceTemplatesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceTemplateSummary:
    boto3_raw_data: "type_defs.ServiceTemplateSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    name = field("name")
    description = field("description")
    displayName = field("displayName")
    pipelineProvisioning = field("pipelineProvisioning")
    recommendedVersion = field("recommendedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesInput:
    boto3_raw_data: "type_defs.ListServicesInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListServicesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSummary:
    boto3_raw_data: "type_defs.ServiceSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    name = field("name")
    status = field("status")
    templateName = field("templateName")
    description = field("description")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectEnvironmentAccountConnectionInput:
    boto3_raw_data: "type_defs.RejectEnvironmentAccountConnectionInputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectEnvironmentAccountConnectionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectEnvironmentAccountConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositorySyncEvent:
    boto3_raw_data: "type_defs.RepositorySyncEventTypeDef" = dataclasses.field()

    event = field("event")
    time = field("time")
    type = field("type")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositorySyncEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositorySyncEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSyncEvent:
    boto3_raw_data: "type_defs.ResourceSyncEventTypeDef" = dataclasses.field()

    event = field("event")
    time = field("time")
    type = field("type")
    externalId = field("externalId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceSyncEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSyncEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ObjectSource:
    boto3_raw_data: "type_defs.S3ObjectSourceTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncBlockerContext:
    boto3_raw_data: "type_defs.SyncBlockerContextTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SyncBlockerContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SyncBlockerContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComponentInput:
    boto3_raw_data: "type_defs.UpdateComponentInputTypeDef" = dataclasses.field()

    deploymentType = field("deploymentType")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")
    serviceSpec = field("serviceSpec")
    templateFile = field("templateFile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateComponentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComponentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentAccountConnectionInput:
    boto3_raw_data: "type_defs.UpdateEnvironmentAccountConnectionInputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    codebuildRoleArn = field("codebuildRoleArn")
    componentRoleArn = field("componentRoleArn")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEnvironmentAccountConnectionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentAccountConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentTemplateInput:
    boto3_raw_data: "type_defs.UpdateEnvironmentTemplateInputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")
    displayName = field("displayName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentTemplateVersionInput:
    boto3_raw_data: "type_defs.UpdateEnvironmentTemplateVersionInputTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    templateName = field("templateName")
    description = field("description")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEnvironmentTemplateVersionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentTemplateVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceInput:
    boto3_raw_data: "type_defs.UpdateServiceInputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    spec = field("spec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceInstanceInput:
    boto3_raw_data: "type_defs.UpdateServiceInstanceInputTypeDef" = dataclasses.field()

    deploymentType = field("deploymentType")
    name = field("name")
    serviceName = field("serviceName")
    clientToken = field("clientToken")
    spec = field("spec")
    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServicePipelineInput:
    boto3_raw_data: "type_defs.UpdateServicePipelineInputTypeDef" = dataclasses.field()

    deploymentType = field("deploymentType")
    serviceName = field("serviceName")
    spec = field("spec")
    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServicePipelineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServicePipelineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceSyncBlockerInput:
    boto3_raw_data: "type_defs.UpdateServiceSyncBlockerInputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    resolvedReason = field("resolvedReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateServiceSyncBlockerInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceSyncBlockerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceSyncConfigInput:
    boto3_raw_data: "type_defs.UpdateServiceSyncConfigInputTypeDef" = (
        dataclasses.field()
    )

    branch = field("branch")
    filePath = field("filePath")
    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceSyncConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceSyncConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceTemplateInput:
    boto3_raw_data: "type_defs.UpdateServiceTemplateInputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    displayName = field("displayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTemplateSyncConfigInput:
    boto3_raw_data: "type_defs.UpdateTemplateSyncConfigInputTypeDef" = (
        dataclasses.field()
    )

    branch = field("branch")
    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    templateName = field("templateName")
    templateType = field("templateType")
    subdirectory = field("subdirectory")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateTemplateSyncConfigInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateSyncConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptEnvironmentAccountConnectionOutput:
    boto3_raw_data: "type_defs.AcceptEnvironmentAccountConnectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentAccountConnection(self):  # pragma: no cover
        return EnvironmentAccountConnection.make_one(
            self.boto3_raw_data["environmentAccountConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptEnvironmentAccountConnectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptEnvironmentAccountConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentAccountConnectionOutput:
    boto3_raw_data: "type_defs.CreateEnvironmentAccountConnectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentAccountConnection(self):  # pragma: no cover
        return EnvironmentAccountConnection.make_one(
            self.boto3_raw_data["environmentAccountConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEnvironmentAccountConnectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentAccountConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentAccountConnectionOutput:
    boto3_raw_data: "type_defs.DeleteEnvironmentAccountConnectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentAccountConnection(self):  # pragma: no cover
        return EnvironmentAccountConnection.make_one(
            self.boto3_raw_data["environmentAccountConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEnvironmentAccountConnectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentAccountConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentAccountConnectionOutput:
    boto3_raw_data: "type_defs.GetEnvironmentAccountConnectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentAccountConnection(self):  # pragma: no cover
        return EnvironmentAccountConnection.make_one(
            self.boto3_raw_data["environmentAccountConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnvironmentAccountConnectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentAccountConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectEnvironmentAccountConnectionOutput:
    boto3_raw_data: "type_defs.RejectEnvironmentAccountConnectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentAccountConnection(self):  # pragma: no cover
        return EnvironmentAccountConnection.make_one(
            self.boto3_raw_data["environmentAccountConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectEnvironmentAccountConnectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectEnvironmentAccountConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentAccountConnectionOutput:
    boto3_raw_data: "type_defs.UpdateEnvironmentAccountConnectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentAccountConnection(self):  # pragma: no cover
        return EnvironmentAccountConnection.make_one(
            self.boto3_raw_data["environmentAccountConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEnvironmentAccountConnectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentAccountConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountSettings:
    boto3_raw_data: "type_defs.AccountSettingsTypeDef" = dataclasses.field()

    pipelineCodebuildRoleArn = field("pipelineCodebuildRoleArn")

    @cached_property
    def pipelineProvisioningRepository(self):  # pragma: no cover
        return RepositoryBranch.make_one(
            self.boto3_raw_data["pipelineProvisioningRepository"]
        )

    pipelineServiceRoleArn = field("pipelineServiceRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Environment:
    boto3_raw_data: "type_defs.EnvironmentTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    deploymentStatus = field("deploymentStatus")
    lastDeploymentAttemptedAt = field("lastDeploymentAttemptedAt")
    lastDeploymentSucceededAt = field("lastDeploymentSucceededAt")
    name = field("name")
    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")
    templateName = field("templateName")
    codebuildRoleArn = field("codebuildRoleArn")
    componentRoleArn = field("componentRoleArn")
    deploymentStatusMessage = field("deploymentStatusMessage")
    description = field("description")
    environmentAccountConnectionId = field("environmentAccountConnectionId")
    environmentAccountId = field("environmentAccountId")
    lastAttemptedDeploymentId = field("lastAttemptedDeploymentId")
    lastSucceededDeploymentId = field("lastSucceededDeploymentId")
    protonServiceRoleArn = field("protonServiceRoleArn")
    provisioning = field("provisioning")

    @cached_property
    def provisioningRepository(self):  # pragma: no cover
        return RepositoryBranch.make_one(self.boto3_raw_data["provisioningRepository"])

    spec = field("spec")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelComponentDeploymentOutput:
    boto3_raw_data: "type_defs.CancelComponentDeploymentOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def component(self):  # pragma: no cover
        return Component.make_one(self.boto3_raw_data["component"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelComponentDeploymentOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelComponentDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentOutput:
    boto3_raw_data: "type_defs.CreateComponentOutputTypeDef" = dataclasses.field()

    @cached_property
    def component(self):  # pragma: no cover
        return Component.make_one(self.boto3_raw_data["component"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComponentOutput:
    boto3_raw_data: "type_defs.DeleteComponentOutputTypeDef" = dataclasses.field()

    @cached_property
    def component(self):  # pragma: no cover
        return Component.make_one(self.boto3_raw_data["component"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteComponentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComponentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentOutput:
    boto3_raw_data: "type_defs.GetComponentOutputTypeDef" = dataclasses.field()

    @cached_property
    def component(self):  # pragma: no cover
        return Component.make_one(self.boto3_raw_data["component"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComponentOutput:
    boto3_raw_data: "type_defs.UpdateComponentOutputTypeDef" = dataclasses.field()

    @cached_property
    def component(self):  # pragma: no cover
        return Component.make_one(self.boto3_raw_data["component"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateComponentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComponentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelServiceInstanceDeploymentOutput:
    boto3_raw_data: "type_defs.CancelServiceInstanceDeploymentOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceInstance(self):  # pragma: no cover
        return ServiceInstance.make_one(self.boto3_raw_data["serviceInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelServiceInstanceDeploymentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelServiceInstanceDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceInstanceOutput:
    boto3_raw_data: "type_defs.CreateServiceInstanceOutputTypeDef" = dataclasses.field()

    @cached_property
    def serviceInstance(self):  # pragma: no cover
        return ServiceInstance.make_one(self.boto3_raw_data["serviceInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInstanceOutput:
    boto3_raw_data: "type_defs.GetServiceInstanceOutputTypeDef" = dataclasses.field()

    @cached_property
    def serviceInstance(self):  # pragma: no cover
        return ServiceInstance.make_one(self.boto3_raw_data["serviceInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceInstanceOutput:
    boto3_raw_data: "type_defs.UpdateServiceInstanceOutputTypeDef" = dataclasses.field()

    @cached_property
    def serviceInstance(self):  # pragma: no cover
        return ServiceInstance.make_one(self.boto3_raw_data["serviceInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelServicePipelineDeploymentOutput:
    boto3_raw_data: "type_defs.CancelServicePipelineDeploymentOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pipeline(self):  # pragma: no cover
        return ServicePipeline.make_one(self.boto3_raw_data["pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelServicePipelineDeploymentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelServicePipelineDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Service:
    boto3_raw_data: "type_defs.ServiceTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    name = field("name")
    spec = field("spec")
    status = field("status")
    templateName = field("templateName")
    branchName = field("branchName")
    description = field("description")

    @cached_property
    def pipeline(self):  # pragma: no cover
        return ServicePipeline.make_one(self.boto3_raw_data["pipeline"])

    repositoryConnectionArn = field("repositoryConnectionArn")
    repositoryId = field("repositoryId")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServicePipelineOutput:
    boto3_raw_data: "type_defs.UpdateServicePipelineOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipeline(self):  # pragma: no cover
        return ServicePipeline.make_one(self.boto3_raw_data["pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServicePipelineOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServicePipelineOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceTemplateVersionInput:
    boto3_raw_data: "type_defs.UpdateServiceTemplateVersionInputTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    templateName = field("templateName")

    @cached_property
    def compatibleEnvironmentTemplates(self):  # pragma: no cover
        return CompatibleEnvironmentTemplateInput.make_many(
            self.boto3_raw_data["compatibleEnvironmentTemplates"]
        )

    description = field("description")
    status = field("status")
    supportedComponentSources = field("supportedComponentSources")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServiceTemplateVersionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceTemplateVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceTemplateVersion:
    boto3_raw_data: "type_defs.ServiceTemplateVersionTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def compatibleEnvironmentTemplates(self):  # pragma: no cover
        return CompatibleEnvironmentTemplate.make_many(
            self.boto3_raw_data["compatibleEnvironmentTemplates"]
        )

    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    status = field("status")
    templateName = field("templateName")
    description = field("description")
    recommendedMinorVersion = field("recommendedMinorVersion")
    schema = field("schema")
    statusMessage = field("statusMessage")
    supportedComponentSources = field("supportedComponentSources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceTemplateVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceTemplateVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsOutput:
    boto3_raw_data: "type_defs.ListComponentsOutputTypeDef" = dataclasses.field()

    @cached_property
    def components(self):  # pragma: no cover
        return ComponentSummary.make_many(self.boto3_raw_data["components"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountsSummary:
    boto3_raw_data: "type_defs.CountsSummaryTypeDef" = dataclasses.field()

    @cached_property
    def components(self):  # pragma: no cover
        return ResourceCountsSummary.make_one(self.boto3_raw_data["components"])

    @cached_property
    def environmentTemplates(self):  # pragma: no cover
        return ResourceCountsSummary.make_one(
            self.boto3_raw_data["environmentTemplates"]
        )

    @cached_property
    def environments(self):  # pragma: no cover
        return ResourceCountsSummary.make_one(self.boto3_raw_data["environments"])

    @cached_property
    def pipelines(self):  # pragma: no cover
        return ResourceCountsSummary.make_one(self.boto3_raw_data["pipelines"])

    @cached_property
    def serviceInstances(self):  # pragma: no cover
        return ResourceCountsSummary.make_one(self.boto3_raw_data["serviceInstances"])

    @cached_property
    def serviceTemplates(self):  # pragma: no cover
        return ResourceCountsSummary.make_one(self.boto3_raw_data["serviceTemplates"])

    @cached_property
    def services(self):  # pragma: no cover
        return ResourceCountsSummary.make_one(self.boto3_raw_data["services"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CountsSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CountsSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentInput:
    boto3_raw_data: "type_defs.CreateComponentInputTypeDef" = dataclasses.field()

    manifest = field("manifest")
    name = field("name")
    templateFile = field("templateFile")
    clientToken = field("clientToken")
    description = field("description")
    environmentName = field("environmentName")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")
    serviceSpec = field("serviceSpec")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentAccountConnectionInput:
    boto3_raw_data: "type_defs.CreateEnvironmentAccountConnectionInputTypeDef" = (
        dataclasses.field()
    )

    environmentName = field("environmentName")
    managementAccountId = field("managementAccountId")
    clientToken = field("clientToken")
    codebuildRoleArn = field("codebuildRoleArn")
    componentRoleArn = field("componentRoleArn")
    roleArn = field("roleArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEnvironmentAccountConnectionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentAccountConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentTemplateInput:
    boto3_raw_data: "type_defs.CreateEnvironmentTemplateInputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")
    displayName = field("displayName")
    encryptionKey = field("encryptionKey")
    provisioning = field("provisioning")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEnvironmentTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryInput:
    boto3_raw_data: "type_defs.CreateRepositoryInputTypeDef" = dataclasses.field()

    connectionArn = field("connectionArn")
    name = field("name")
    provider = field("provider")
    encryptionKey = field("encryptionKey")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceInput:
    boto3_raw_data: "type_defs.CreateServiceInputTypeDef" = dataclasses.field()

    name = field("name")
    spec = field("spec")
    templateMajorVersion = field("templateMajorVersion")
    templateName = field("templateName")
    branchName = field("branchName")
    description = field("description")
    repositoryConnectionArn = field("repositoryConnectionArn")
    repositoryId = field("repositoryId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    templateMinorVersion = field("templateMinorVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceInstanceInput:
    boto3_raw_data: "type_defs.CreateServiceInstanceInputTypeDef" = dataclasses.field()

    name = field("name")
    serviceName = field("serviceName")
    spec = field("spec")
    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceTemplateInput:
    boto3_raw_data: "type_defs.CreateServiceTemplateInputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    displayName = field("displayName")
    encryptionKey = field("encryptionKey")
    pipelineProvisioning = field("pipelineProvisioning")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentInput:
    boto3_raw_data: "type_defs.CreateEnvironmentInputTypeDef" = dataclasses.field()

    name = field("name")
    spec = field("spec")
    templateMajorVersion = field("templateMajorVersion")
    templateName = field("templateName")
    codebuildRoleArn = field("codebuildRoleArn")
    componentRoleArn = field("componentRoleArn")
    description = field("description")
    environmentAccountConnectionId = field("environmentAccountConnectionId")
    protonServiceRoleArn = field("protonServiceRoleArn")

    @cached_property
    def provisioningRepository(self):  # pragma: no cover
        return RepositoryBranchInput.make_one(
            self.boto3_raw_data["provisioningRepository"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    templateMinorVersion = field("templateMinorVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountSettingsInput:
    boto3_raw_data: "type_defs.UpdateAccountSettingsInputTypeDef" = dataclasses.field()

    deletePipelineProvisioningRepository = field("deletePipelineProvisioningRepository")
    pipelineCodebuildRoleArn = field("pipelineCodebuildRoleArn")

    @cached_property
    def pipelineProvisioningRepository(self):  # pragma: no cover
        return RepositoryBranchInput.make_one(
            self.boto3_raw_data["pipelineProvisioningRepository"]
        )

    pipelineServiceRoleArn = field("pipelineServiceRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountSettingsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentInput:
    boto3_raw_data: "type_defs.UpdateEnvironmentInputTypeDef" = dataclasses.field()

    deploymentType = field("deploymentType")
    name = field("name")
    codebuildRoleArn = field("codebuildRoleArn")
    componentRoleArn = field("componentRoleArn")
    description = field("description")
    environmentAccountConnectionId = field("environmentAccountConnectionId")
    protonServiceRoleArn = field("protonServiceRoleArn")

    @cached_property
    def provisioningRepository(self):  # pragma: no cover
        return RepositoryBranchInput.make_one(
            self.boto3_raw_data["provisioningRepository"]
        )

    spec = field("spec")
    templateMajorVersion = field("templateMajorVersion")
    templateMinorVersion = field("templateMinorVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentTemplateOutput:
    boto3_raw_data: "type_defs.CreateEnvironmentTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentTemplate(self):  # pragma: no cover
        return EnvironmentTemplate.make_one(self.boto3_raw_data["environmentTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEnvironmentTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentTemplateOutput:
    boto3_raw_data: "type_defs.DeleteEnvironmentTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentTemplate(self):  # pragma: no cover
        return EnvironmentTemplate.make_one(self.boto3_raw_data["environmentTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentTemplateOutput:
    boto3_raw_data: "type_defs.GetEnvironmentTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentTemplate(self):  # pragma: no cover
        return EnvironmentTemplate.make_one(self.boto3_raw_data["environmentTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentTemplateOutput:
    boto3_raw_data: "type_defs.UpdateEnvironmentTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentTemplate(self):  # pragma: no cover
        return EnvironmentTemplate.make_one(self.boto3_raw_data["environmentTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentTemplateVersionOutput:
    boto3_raw_data: "type_defs.CreateEnvironmentTemplateVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentTemplateVersion(self):  # pragma: no cover
        return EnvironmentTemplateVersion.make_one(
            self.boto3_raw_data["environmentTemplateVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEnvironmentTemplateVersionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentTemplateVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentTemplateVersionOutput:
    boto3_raw_data: "type_defs.DeleteEnvironmentTemplateVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentTemplateVersion(self):  # pragma: no cover
        return EnvironmentTemplateVersion.make_one(
            self.boto3_raw_data["environmentTemplateVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEnvironmentTemplateVersionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentTemplateVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentTemplateVersionOutput:
    boto3_raw_data: "type_defs.GetEnvironmentTemplateVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentTemplateVersion(self):  # pragma: no cover
        return EnvironmentTemplateVersion.make_one(
            self.boto3_raw_data["environmentTemplateVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnvironmentTemplateVersionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentTemplateVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentTemplateVersionOutput:
    boto3_raw_data: "type_defs.UpdateEnvironmentTemplateVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentTemplateVersion(self):  # pragma: no cover
        return EnvironmentTemplateVersion.make_one(
            self.boto3_raw_data["environmentTemplateVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEnvironmentTemplateVersionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentTemplateVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryOutput:
    boto3_raw_data: "type_defs.CreateRepositoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def repository(self):  # pragma: no cover
        return Repository.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryOutput:
    boto3_raw_data: "type_defs.DeleteRepositoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def repository(self):  # pragma: no cover
        return Repository.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRepositoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryOutput:
    boto3_raw_data: "type_defs.GetRepositoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def repository(self):  # pragma: no cover
        return Repository.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceSyncConfigOutput:
    boto3_raw_data: "type_defs.CreateServiceSyncConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceSyncConfig(self):  # pragma: no cover
        return ServiceSyncConfig.make_one(self.boto3_raw_data["serviceSyncConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateServiceSyncConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceSyncConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceSyncConfigOutput:
    boto3_raw_data: "type_defs.DeleteServiceSyncConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceSyncConfig(self):  # pragma: no cover
        return ServiceSyncConfig.make_one(self.boto3_raw_data["serviceSyncConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteServiceSyncConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceSyncConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceSyncConfigOutput:
    boto3_raw_data: "type_defs.GetServiceSyncConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def serviceSyncConfig(self):  # pragma: no cover
        return ServiceSyncConfig.make_one(self.boto3_raw_data["serviceSyncConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceSyncConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceSyncConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceSyncConfigOutput:
    boto3_raw_data: "type_defs.UpdateServiceSyncConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceSyncConfig(self):  # pragma: no cover
        return ServiceSyncConfig.make_one(self.boto3_raw_data["serviceSyncConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateServiceSyncConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceSyncConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceTemplateOutput:
    boto3_raw_data: "type_defs.CreateServiceTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def serviceTemplate(self):  # pragma: no cover
        return ServiceTemplate.make_one(self.boto3_raw_data["serviceTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceTemplateOutput:
    boto3_raw_data: "type_defs.DeleteServiceTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def serviceTemplate(self):  # pragma: no cover
        return ServiceTemplate.make_one(self.boto3_raw_data["serviceTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceTemplateOutput:
    boto3_raw_data: "type_defs.GetServiceTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def serviceTemplate(self):  # pragma: no cover
        return ServiceTemplate.make_one(self.boto3_raw_data["serviceTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceTemplateOutput:
    boto3_raw_data: "type_defs.UpdateServiceTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def serviceTemplate(self):  # pragma: no cover
        return ServiceTemplate.make_one(self.boto3_raw_data["serviceTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateSyncConfigOutput:
    boto3_raw_data: "type_defs.CreateTemplateSyncConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templateSyncConfig(self):  # pragma: no cover
        return TemplateSyncConfig.make_one(self.boto3_raw_data["templateSyncConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateTemplateSyncConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateSyncConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTemplateSyncConfigOutput:
    boto3_raw_data: "type_defs.DeleteTemplateSyncConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templateSyncConfig(self):  # pragma: no cover
        return TemplateSyncConfig.make_one(self.boto3_raw_data["templateSyncConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTemplateSyncConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTemplateSyncConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateSyncConfigOutput:
    boto3_raw_data: "type_defs.GetTemplateSyncConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def templateSyncConfig(self):  # pragma: no cover
        return TemplateSyncConfig.make_one(self.boto3_raw_data["templateSyncConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateSyncConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateSyncConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTemplateSyncConfigOutput:
    boto3_raw_data: "type_defs.UpdateTemplateSyncConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templateSyncConfig(self):  # pragma: no cover
        return TemplateSyncConfig.make_one(self.boto3_raw_data["templateSyncConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateTemplateSyncConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateSyncConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentState:
    boto3_raw_data: "type_defs.DeploymentStateTypeDef" = dataclasses.field()

    @cached_property
    def component(self):  # pragma: no cover
        return ComponentState.make_one(self.boto3_raw_data["component"])

    @cached_property
    def environment(self):  # pragma: no cover
        return EnvironmentState.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def serviceInstance(self):  # pragma: no cover
        return ServiceInstanceState.make_one(self.boto3_raw_data["serviceInstance"])

    @cached_property
    def servicePipeline(self):  # pragma: no cover
        return ServicePipelineState.make_one(self.boto3_raw_data["servicePipeline"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsOutput:
    boto3_raw_data: "type_defs.ListDeploymentsOutputTypeDef" = dataclasses.field()

    @cached_property
    def deployments(self):  # pragma: no cover
        return DeploymentSummary.make_many(self.boto3_raw_data["deployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentAccountConnectionsOutput:
    boto3_raw_data: "type_defs.ListEnvironmentAccountConnectionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentAccountConnections(self):  # pragma: no cover
        return EnvironmentAccountConnectionSummary.make_many(
            self.boto3_raw_data["environmentAccountConnections"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentAccountConnectionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentAccountConnectionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsOutput:
    boto3_raw_data: "type_defs.ListEnvironmentsOutputTypeDef" = dataclasses.field()

    @cached_property
    def environments(self):  # pragma: no cover
        return EnvironmentSummary.make_many(self.boto3_raw_data["environments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsInput:
    boto3_raw_data: "type_defs.ListEnvironmentsInputTypeDef" = dataclasses.field()

    @cached_property
    def environmentTemplates(self):  # pragma: no cover
        return EnvironmentTemplateFilter.make_many(
            self.boto3_raw_data["environmentTemplates"]
        )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentTemplatesOutput:
    boto3_raw_data: "type_defs.ListEnvironmentTemplatesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templates(self):  # pragma: no cover
        return EnvironmentTemplateSummary.make_many(self.boto3_raw_data["templates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentTemplatesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentTemplateVersionsOutput:
    boto3_raw_data: "type_defs.ListEnvironmentTemplateVersionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templateVersions(self):  # pragma: no cover
        return EnvironmentTemplateVersionSummary.make_many(
            self.boto3_raw_data["templateVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentTemplateVersionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentTemplateVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentInputWaitExtra:
    boto3_raw_data: "type_defs.GetComponentInputWaitExtraTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentInputWait:
    boto3_raw_data: "type_defs.GetComponentInputWaitTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentInputWait:
    boto3_raw_data: "type_defs.GetEnvironmentInputWaitTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentTemplateVersionInputWait:
    boto3_raw_data: "type_defs.GetEnvironmentTemplateVersionInputWaitTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    templateName = field("templateName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnvironmentTemplateVersionInputWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentTemplateVersionInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInputWaitExtraExtraExtra:
    boto3_raw_data: "type_defs.GetServiceInputWaitExtraExtraExtraTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceInputWaitExtraExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceInputWaitExtraExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInputWaitExtraExtra:
    boto3_raw_data: "type_defs.GetServiceInputWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServiceInputWaitExtraExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceInputWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInputWaitExtra:
    boto3_raw_data: "type_defs.GetServiceInputWaitExtraTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInputWait:
    boto3_raw_data: "type_defs.GetServiceInputWaitTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInstanceInputWait:
    boto3_raw_data: "type_defs.GetServiceInstanceInputWaitTypeDef" = dataclasses.field()

    name = field("name")
    serviceName = field("serviceName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceInstanceInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceInstanceInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceTemplateVersionInputWait:
    boto3_raw_data: "type_defs.GetServiceTemplateVersionInputWaitTypeDef" = (
        dataclasses.field()
    )

    majorVersion = field("majorVersion")
    minorVersion = field("minorVersion")
    templateName = field("templateName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceTemplateVersionInputWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceTemplateVersionInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentOutputsInputPaginate:
    boto3_raw_data: "type_defs.ListComponentOutputsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    componentName = field("componentName")
    deploymentId = field("deploymentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComponentOutputsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentOutputsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentProvisionedResourcesInputPaginate:
    boto3_raw_data: (
        "type_defs.ListComponentProvisionedResourcesInputPaginateTypeDef"
    ) = dataclasses.field()

    componentName = field("componentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComponentProvisionedResourcesInputPaginateTypeDef"
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
                "type_defs.ListComponentProvisionedResourcesInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsInputPaginate:
    boto3_raw_data: "type_defs.ListComponentsInputPaginateTypeDef" = dataclasses.field()

    environmentName = field("environmentName")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsInputPaginate:
    boto3_raw_data: "type_defs.ListDeploymentsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    componentName = field("componentName")
    environmentName = field("environmentName")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentAccountConnectionsInputPaginate:
    boto3_raw_data: (
        "type_defs.ListEnvironmentAccountConnectionsInputPaginateTypeDef"
    ) = dataclasses.field()

    requestedBy = field("requestedBy")
    environmentName = field("environmentName")
    statuses = field("statuses")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentAccountConnectionsInputPaginateTypeDef"
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
                "type_defs.ListEnvironmentAccountConnectionsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentOutputsInputPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentOutputsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    environmentName = field("environmentName")
    deploymentId = field("deploymentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentOutputsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentOutputsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentProvisionedResourcesInputPaginate:
    boto3_raw_data: (
        "type_defs.ListEnvironmentProvisionedResourcesInputPaginateTypeDef"
    ) = dataclasses.field()

    environmentName = field("environmentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentProvisionedResourcesInputPaginateTypeDef"
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
                "type_defs.ListEnvironmentProvisionedResourcesInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentTemplateVersionsInputPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentTemplateVersionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    majorVersion = field("majorVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentTemplateVersionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentTemplateVersionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentTemplatesInputPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentTemplatesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentTemplatesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentTemplatesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsInputPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentTemplates(self):  # pragma: no cover
        return EnvironmentTemplateFilter.make_many(
            self.boto3_raw_data["environmentTemplates"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesInputPaginate:
    boto3_raw_data: "type_defs.ListRepositoriesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRepositoriesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositorySyncDefinitionsInputPaginate:
    boto3_raw_data: "type_defs.ListRepositorySyncDefinitionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    repositoryProvider = field("repositoryProvider")
    syncType = field("syncType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositorySyncDefinitionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositorySyncDefinitionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstanceOutputsInputPaginate:
    boto3_raw_data: "type_defs.ListServiceInstanceOutputsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")
    deploymentId = field("deploymentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceInstanceOutputsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceInstanceOutputsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstanceProvisionedResourcesInputPaginate:
    boto3_raw_data: (
        "type_defs.ListServiceInstanceProvisionedResourcesInputPaginateTypeDef"
    ) = dataclasses.field()

    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceInstanceProvisionedResourcesInputPaginateTypeDef"
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
                "type_defs.ListServiceInstanceProvisionedResourcesInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicePipelineOutputsInputPaginate:
    boto3_raw_data: "type_defs.ListServicePipelineOutputsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    serviceName = field("serviceName")
    deploymentId = field("deploymentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServicePipelineOutputsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicePipelineOutputsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicePipelineProvisionedResourcesInputPaginate:
    boto3_raw_data: (
        "type_defs.ListServicePipelineProvisionedResourcesInputPaginateTypeDef"
    ) = dataclasses.field()

    serviceName = field("serviceName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServicePipelineProvisionedResourcesInputPaginateTypeDef"
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
                "type_defs.ListServicePipelineProvisionedResourcesInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceTemplateVersionsInputPaginate:
    boto3_raw_data: "type_defs.ListServiceTemplateVersionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    majorVersion = field("majorVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceTemplateVersionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceTemplateVersionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceTemplatesInputPaginate:
    boto3_raw_data: "type_defs.ListServiceTemplatesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceTemplatesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceTemplatesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesInputPaginate:
    boto3_raw_data: "type_defs.ListServicesInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInputPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceInputPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentOutputsOutput:
    boto3_raw_data: "type_defs.ListComponentOutputsOutputTypeDef" = dataclasses.field()

    @cached_property
    def outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["outputs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentOutputsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentOutputsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentOutputsOutput:
    boto3_raw_data: "type_defs.ListEnvironmentOutputsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["outputs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentOutputsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentOutputsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstanceOutputsOutput:
    boto3_raw_data: "type_defs.ListServiceInstanceOutputsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["outputs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceInstanceOutputsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceInstanceOutputsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicePipelineOutputsOutput:
    boto3_raw_data: "type_defs.ListServicePipelineOutputsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["outputs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServicePipelineOutputsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicePipelineOutputsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyResourceDeploymentStatusChangeInput:
    boto3_raw_data: "type_defs.NotifyResourceDeploymentStatusChangeInputTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    deploymentId = field("deploymentId")

    @cached_property
    def outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["outputs"])

    status = field("status")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotifyResourceDeploymentStatusChangeInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyResourceDeploymentStatusChangeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentProvisionedResourcesOutput:
    boto3_raw_data: "type_defs.ListComponentProvisionedResourcesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def provisionedResources(self):  # pragma: no cover
        return ProvisionedResource.make_many(
            self.boto3_raw_data["provisionedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComponentProvisionedResourcesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentProvisionedResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentProvisionedResourcesOutput:
    boto3_raw_data: "type_defs.ListEnvironmentProvisionedResourcesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def provisionedResources(self):  # pragma: no cover
        return ProvisionedResource.make_many(
            self.boto3_raw_data["provisionedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentProvisionedResourcesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentProvisionedResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstanceProvisionedResourcesOutput:
    boto3_raw_data: "type_defs.ListServiceInstanceProvisionedResourcesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def provisionedResources(self):  # pragma: no cover
        return ProvisionedResource.make_many(
            self.boto3_raw_data["provisionedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceInstanceProvisionedResourcesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceInstanceProvisionedResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicePipelineProvisionedResourcesOutput:
    boto3_raw_data: "type_defs.ListServicePipelineProvisionedResourcesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def provisionedResources(self):  # pragma: no cover
        return ProvisionedResource.make_many(
            self.boto3_raw_data["provisionedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServicePipelineProvisionedResourcesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicePipelineProvisionedResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesOutput:
    boto3_raw_data: "type_defs.ListRepositoriesOutputTypeDef" = dataclasses.field()

    @cached_property
    def repositories(self):  # pragma: no cover
        return RepositorySummary.make_many(self.boto3_raw_data["repositories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRepositoriesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositorySyncDefinitionsOutput:
    boto3_raw_data: "type_defs.ListRepositorySyncDefinitionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def syncDefinitions(self):  # pragma: no cover
        return RepositorySyncDefinition.make_many(
            self.boto3_raw_data["syncDefinitions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositorySyncDefinitionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositorySyncDefinitionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstancesInputPaginate:
    boto3_raw_data: "type_defs.ListServiceInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return ListServiceInstancesFilter.make_many(self.boto3_raw_data["filters"])

    serviceName = field("serviceName")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceInstancesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstancesInput:
    boto3_raw_data: "type_defs.ListServiceInstancesInputTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return ListServiceInstancesFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    serviceName = field("serviceName")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceInstancesOutput:
    boto3_raw_data: "type_defs.ListServiceInstancesOutputTypeDef" = dataclasses.field()

    @cached_property
    def serviceInstances(self):  # pragma: no cover
        return ServiceInstanceSummary.make_many(self.boto3_raw_data["serviceInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceTemplateVersionsOutput:
    boto3_raw_data: "type_defs.ListServiceTemplateVersionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templateVersions(self):  # pragma: no cover
        return ServiceTemplateVersionSummary.make_many(
            self.boto3_raw_data["templateVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceTemplateVersionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceTemplateVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceTemplatesOutput:
    boto3_raw_data: "type_defs.ListServiceTemplatesOutputTypeDef" = dataclasses.field()

    @cached_property
    def templates(self):  # pragma: no cover
        return ServiceTemplateSummary.make_many(self.boto3_raw_data["templates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceTemplatesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesOutput:
    boto3_raw_data: "type_defs.ListServicesOutputTypeDef" = dataclasses.field()

    @cached_property
    def services(self):  # pragma: no cover
        return ServiceSummary.make_many(self.boto3_raw_data["services"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositorySyncAttempt:
    boto3_raw_data: "type_defs.RepositorySyncAttemptTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return RepositorySyncEvent.make_many(self.boto3_raw_data["events"])

    startedAt = field("startedAt")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositorySyncAttemptTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositorySyncAttemptTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSyncAttempt:
    boto3_raw_data: "type_defs.ResourceSyncAttemptTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return ResourceSyncEvent.make_many(self.boto3_raw_data["events"])

    @cached_property
    def initialRevision(self):  # pragma: no cover
        return Revision.make_one(self.boto3_raw_data["initialRevision"])

    startedAt = field("startedAt")
    status = field("status")
    target = field("target")

    @cached_property
    def targetRevision(self):  # pragma: no cover
        return Revision.make_one(self.boto3_raw_data["targetRevision"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceSyncAttemptTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSyncAttemptTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateVersionSourceInput:
    boto3_raw_data: "type_defs.TemplateVersionSourceInputTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return S3ObjectSource.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateVersionSourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateVersionSourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncBlocker:
    boto3_raw_data: "type_defs.SyncBlockerTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdReason = field("createdReason")
    id = field("id")
    status = field("status")
    type = field("type")

    @cached_property
    def contexts(self):  # pragma: no cover
        return SyncBlockerContext.make_many(self.boto3_raw_data["contexts"])

    resolvedAt = field("resolvedAt")
    resolvedReason = field("resolvedReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SyncBlockerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SyncBlockerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountSettingsOutput:
    boto3_raw_data: "type_defs.GetAccountSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def accountSettings(self):  # pragma: no cover
        return AccountSettings.make_one(self.boto3_raw_data["accountSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountSettingsOutput:
    boto3_raw_data: "type_defs.UpdateAccountSettingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def accountSettings(self):  # pragma: no cover
        return AccountSettings.make_one(self.boto3_raw_data["accountSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelEnvironmentDeploymentOutput:
    boto3_raw_data: "type_defs.CancelEnvironmentDeploymentOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelEnvironmentDeploymentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelEnvironmentDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentOutput:
    boto3_raw_data: "type_defs.CreateEnvironmentOutputTypeDef" = dataclasses.field()

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentOutput:
    boto3_raw_data: "type_defs.DeleteEnvironmentOutputTypeDef" = dataclasses.field()

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentOutput:
    boto3_raw_data: "type_defs.GetEnvironmentOutputTypeDef" = dataclasses.field()

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentOutput:
    boto3_raw_data: "type_defs.UpdateEnvironmentOutputTypeDef" = dataclasses.field()

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceOutput:
    boto3_raw_data: "type_defs.CreateServiceOutputTypeDef" = dataclasses.field()

    @cached_property
    def service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["service"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceOutput:
    boto3_raw_data: "type_defs.DeleteServiceOutputTypeDef" = dataclasses.field()

    @cached_property
    def service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["service"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceOutput:
    boto3_raw_data: "type_defs.GetServiceOutputTypeDef" = dataclasses.field()

    @cached_property
    def service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["service"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetServiceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceOutput:
    boto3_raw_data: "type_defs.UpdateServiceOutputTypeDef" = dataclasses.field()

    @cached_property
    def service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["service"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceTemplateVersionOutput:
    boto3_raw_data: "type_defs.CreateServiceTemplateVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceTemplateVersion(self):  # pragma: no cover
        return ServiceTemplateVersion.make_one(
            self.boto3_raw_data["serviceTemplateVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceTemplateVersionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceTemplateVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceTemplateVersionOutput:
    boto3_raw_data: "type_defs.DeleteServiceTemplateVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceTemplateVersion(self):  # pragma: no cover
        return ServiceTemplateVersion.make_one(
            self.boto3_raw_data["serviceTemplateVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceTemplateVersionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceTemplateVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceTemplateVersionOutput:
    boto3_raw_data: "type_defs.GetServiceTemplateVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceTemplateVersion(self):  # pragma: no cover
        return ServiceTemplateVersion.make_one(
            self.boto3_raw_data["serviceTemplateVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServiceTemplateVersionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceTemplateVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceTemplateVersionOutput:
    boto3_raw_data: "type_defs.UpdateServiceTemplateVersionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceTemplateVersion(self):  # pragma: no cover
        return ServiceTemplateVersion.make_one(
            self.boto3_raw_data["serviceTemplateVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServiceTemplateVersionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceTemplateVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcesSummaryOutput:
    boto3_raw_data: "type_defs.GetResourcesSummaryOutputTypeDef" = dataclasses.field()

    @cached_property
    def counts(self):  # pragma: no cover
        return CountsSummary.make_one(self.boto3_raw_data["counts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcesSummaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcesSummaryOutputTypeDef"]
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

    arn = field("arn")
    createdAt = field("createdAt")
    deploymentStatus = field("deploymentStatus")
    environmentName = field("environmentName")
    id = field("id")
    lastModifiedAt = field("lastModifiedAt")
    targetArn = field("targetArn")
    targetResourceCreatedAt = field("targetResourceCreatedAt")
    targetResourceType = field("targetResourceType")
    completedAt = field("completedAt")
    componentName = field("componentName")
    deploymentStatusMessage = field("deploymentStatusMessage")

    @cached_property
    def initialState(self):  # pragma: no cover
        return DeploymentState.make_one(self.boto3_raw_data["initialState"])

    lastAttemptedDeploymentId = field("lastAttemptedDeploymentId")
    lastSucceededDeploymentId = field("lastSucceededDeploymentId")
    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @cached_property
    def targetState(self):  # pragma: no cover
        return DeploymentState.make_one(self.boto3_raw_data["targetState"])

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
class GetRepositorySyncStatusOutput:
    boto3_raw_data: "type_defs.GetRepositorySyncStatusOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def latestSync(self):  # pragma: no cover
        return RepositorySyncAttempt.make_one(self.boto3_raw_data["latestSync"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRepositorySyncStatusOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositorySyncStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInstanceSyncStatusOutput:
    boto3_raw_data: "type_defs.GetServiceInstanceSyncStatusOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def desiredState(self):  # pragma: no cover
        return Revision.make_one(self.boto3_raw_data["desiredState"])

    @cached_property
    def latestSuccessfulSync(self):  # pragma: no cover
        return ResourceSyncAttempt.make_one(self.boto3_raw_data["latestSuccessfulSync"])

    @cached_property
    def latestSync(self):  # pragma: no cover
        return ResourceSyncAttempt.make_one(self.boto3_raw_data["latestSync"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceInstanceSyncStatusOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceInstanceSyncStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateSyncStatusOutput:
    boto3_raw_data: "type_defs.GetTemplateSyncStatusOutputTypeDef" = dataclasses.field()

    @cached_property
    def desiredState(self):  # pragma: no cover
        return Revision.make_one(self.boto3_raw_data["desiredState"])

    @cached_property
    def latestSuccessfulSync(self):  # pragma: no cover
        return ResourceSyncAttempt.make_one(self.boto3_raw_data["latestSuccessfulSync"])

    @cached_property
    def latestSync(self):  # pragma: no cover
        return ResourceSyncAttempt.make_one(self.boto3_raw_data["latestSync"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateSyncStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateSyncStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentTemplateVersionInput:
    boto3_raw_data: "type_defs.CreateEnvironmentTemplateVersionInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def source(self):  # pragma: no cover
        return TemplateVersionSourceInput.make_one(self.boto3_raw_data["source"])

    templateName = field("templateName")
    clientToken = field("clientToken")
    description = field("description")
    majorVersion = field("majorVersion")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEnvironmentTemplateVersionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentTemplateVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceTemplateVersionInput:
    boto3_raw_data: "type_defs.CreateServiceTemplateVersionInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def compatibleEnvironmentTemplates(self):  # pragma: no cover
        return CompatibleEnvironmentTemplateInput.make_many(
            self.boto3_raw_data["compatibleEnvironmentTemplates"]
        )

    @cached_property
    def source(self):  # pragma: no cover
        return TemplateVersionSourceInput.make_one(self.boto3_raw_data["source"])

    templateName = field("templateName")
    clientToken = field("clientToken")
    description = field("description")
    majorVersion = field("majorVersion")
    supportedComponentSources = field("supportedComponentSources")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceTemplateVersionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceTemplateVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSyncBlockerSummary:
    boto3_raw_data: "type_defs.ServiceSyncBlockerSummaryTypeDef" = dataclasses.field()

    serviceName = field("serviceName")

    @cached_property
    def latestBlockers(self):  # pragma: no cover
        return SyncBlocker.make_many(self.boto3_raw_data["latestBlockers"])

    serviceInstanceName = field("serviceInstanceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceSyncBlockerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceSyncBlockerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceSyncBlockerOutput:
    boto3_raw_data: "type_defs.UpdateServiceSyncBlockerOutputTypeDef" = (
        dataclasses.field()
    )

    serviceInstanceName = field("serviceInstanceName")
    serviceName = field("serviceName")

    @cached_property
    def serviceSyncBlocker(self):  # pragma: no cover
        return SyncBlocker.make_one(self.boto3_raw_data["serviceSyncBlocker"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateServiceSyncBlockerOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceSyncBlockerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeploymentOutput:
    boto3_raw_data: "type_defs.DeleteDeploymentOutputTypeDef" = dataclasses.field()

    @cached_property
    def deployment(self):  # pragma: no cover
        return Deployment.make_one(self.boto3_raw_data["deployment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeploymentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentOutput:
    boto3_raw_data: "type_defs.GetDeploymentOutputTypeDef" = dataclasses.field()

    @cached_property
    def deployment(self):  # pragma: no cover
        return Deployment.make_one(self.boto3_raw_data["deployment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceSyncBlockerSummaryOutput:
    boto3_raw_data: "type_defs.GetServiceSyncBlockerSummaryOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceSyncBlockerSummary(self):  # pragma: no cover
        return ServiceSyncBlockerSummary.make_one(
            self.boto3_raw_data["serviceSyncBlockerSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceSyncBlockerSummaryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceSyncBlockerSummaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
