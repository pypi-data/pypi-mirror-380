# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_imagebuilder import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class SeverityCounts:
    boto3_raw_data: "type_defs.SeverityCountsTypeDef" = dataclasses.field()

    all = field("all")
    critical = field("critical")
    high = field("high")
    medium = field("medium")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SeverityCountsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SeverityCountsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SystemsManagerAgent:
    boto3_raw_data: "type_defs.SystemsManagerAgentTypeDef" = dataclasses.field()

    uninstallAfterBuild = field("uninstallAfterBuild")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SystemsManagerAgentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SystemsManagerAgentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchPermissionConfigurationOutput:
    boto3_raw_data: "type_defs.LaunchPermissionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    userIds = field("userIds")
    userGroups = field("userGroups")
    organizationArns = field("organizationArns")
    organizationalUnitArns = field("organizationalUnitArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LaunchPermissionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchPermissionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageState:
    boto3_raw_data: "type_defs.ImageStateTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelImageCreationRequest:
    boto3_raw_data: "type_defs.CancelImageCreationRequestTypeDef" = dataclasses.field()

    imageBuildVersionArn = field("imageBuildVersionArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelImageCreationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelImageCreationRequestTypeDef"]
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
class CancelLifecycleExecutionRequest:
    boto3_raw_data: "type_defs.CancelLifecycleExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    lifecycleExecutionId = field("lifecycleExecutionId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelLifecycleExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelLifecycleExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentParameterOutput:
    boto3_raw_data: "type_defs.ComponentParameterOutputTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentParameterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentParameterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentParameterDetail:
    boto3_raw_data: "type_defs.ComponentParameterDetailTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    defaultValue = field("defaultValue")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentParameterDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentParameterDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentParameter:
    boto3_raw_data: "type_defs.ComponentParameterTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentParameterTypeDef"]
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

    status = field("status")
    reason = field("reason")

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
class ProductCodeListItem:
    boto3_raw_data: "type_defs.ProductCodeListItemTypeDef" = dataclasses.field()

    productCodeId = field("productCodeId")
    productCodeType = field("productCodeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProductCodeListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductCodeListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetContainerRepository:
    boto3_raw_data: "type_defs.TargetContainerRepositoryTypeDef" = dataclasses.field()

    service = field("service")
    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetContainerRepositoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetContainerRepositoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerRecipeSummary:
    boto3_raw_data: "type_defs.ContainerRecipeSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    containerType = field("containerType")
    name = field("name")
    platform = field("platform")
    owner = field("owner")
    parentImage = field("parentImage")
    dateCreated = field("dateCreated")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerRecipeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerRecipeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Container:
    boto3_raw_data: "type_defs.ContainerTypeDef" = dataclasses.field()

    region = field("region")
    imageUris = field("imageUris")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentRequest:
    boto3_raw_data: "type_defs.CreateComponentRequestTypeDef" = dataclasses.field()

    name = field("name")
    semanticVersion = field("semanticVersion")
    platform = field("platform")
    clientToken = field("clientToken")
    description = field("description")
    changeDescription = field("changeDescription")
    supportedOsVersions = field("supportedOsVersions")
    data = field("data")
    uri = field("uri")
    kmsKeyId = field("kmsKeyId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageTestsConfiguration:
    boto3_raw_data: "type_defs.ImageTestsConfigurationTypeDef" = dataclasses.field()

    imageTestsEnabled = field("imageTestsEnabled")
    timeoutMinutes = field("timeoutMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageTestsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageTestsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schedule:
    boto3_raw_data: "type_defs.ScheduleTypeDef" = dataclasses.field()

    scheduleExpression = field("scheduleExpression")
    timezone = field("timezone")
    pipelineExecutionStartCondition = field("pipelineExecutionStartCondition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceMetadataOptions:
    boto3_raw_data: "type_defs.InstanceMetadataOptionsTypeDef" = dataclasses.field()

    httpTokens = field("httpTokens")
    httpPutResponseHopLimit = field("httpPutResponseHopLimit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceMetadataOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceMetadataOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Placement:
    boto3_raw_data: "type_defs.PlacementTypeDef" = dataclasses.field()

    availabilityZone = field("availabilityZone")
    tenancy = field("tenancy")
    hostId = field("hostId")
    hostResourceGroupArn = field("hostResourceGroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlacementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlacementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowRequest:
    boto3_raw_data: "type_defs.CreateWorkflowRequestTypeDef" = dataclasses.field()

    name = field("name")
    semanticVersion = field("semanticVersion")
    clientToken = field("clientToken")
    type = field("type")
    description = field("description")
    changeDescription = field("changeDescription")
    data = field("data")
    uri = field("uri")
    kmsKeyId = field("kmsKeyId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CvssScoreAdjustment:
    boto3_raw_data: "type_defs.CvssScoreAdjustmentTypeDef" = dataclasses.field()

    metric = field("metric")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CvssScoreAdjustmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CvssScoreAdjustmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CvssScore:
    boto3_raw_data: "type_defs.CvssScoreTypeDef" = dataclasses.field()

    baseScore = field("baseScore")
    scoringVector = field("scoringVector")
    version = field("version")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CvssScoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CvssScoreTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComponentRequest:
    boto3_raw_data: "type_defs.DeleteComponentRequestTypeDef" = dataclasses.field()

    componentBuildVersionArn = field("componentBuildVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContainerRecipeRequest:
    boto3_raw_data: "type_defs.DeleteContainerRecipeRequestTypeDef" = (
        dataclasses.field()
    )

    containerRecipeArn = field("containerRecipeArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContainerRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContainerRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDistributionConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteDistributionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    distributionConfigurationArn = field("distributionConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDistributionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDistributionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImagePipelineRequest:
    boto3_raw_data: "type_defs.DeleteImagePipelineRequestTypeDef" = dataclasses.field()

    imagePipelineArn = field("imagePipelineArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImagePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImagePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageRecipeRequest:
    boto3_raw_data: "type_defs.DeleteImageRecipeRequestTypeDef" = dataclasses.field()

    imageRecipeArn = field("imageRecipeArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImageRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageRequest:
    boto3_raw_data: "type_defs.DeleteImageRequestTypeDef" = dataclasses.field()

    imageBuildVersionArn = field("imageBuildVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInfrastructureConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteInfrastructureConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    infrastructureConfigurationArn = field("infrastructureConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteInfrastructureConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInfrastructureConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.DeleteLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    lifecyclePolicyArn = field("lifecyclePolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkflowRequest:
    boto3_raw_data: "type_defs.DeleteWorkflowRequestTypeDef" = dataclasses.field()

    workflowBuildVersionArn = field("workflowBuildVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionConfigurationSummary:
    boto3_raw_data: "type_defs.DistributionConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    description = field("description")
    dateCreated = field("dateCreated")
    dateUpdated = field("dateUpdated")
    tags = field("tags")
    regions = field("regions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DistributionConfigurationSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateConfiguration:
    boto3_raw_data: "type_defs.LaunchTemplateConfigurationTypeDef" = dataclasses.field()

    launchTemplateId = field("launchTemplateId")
    accountId = field("accountId")
    setDefaultVersion = field("setDefaultVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ExportConfiguration:
    boto3_raw_data: "type_defs.S3ExportConfigurationTypeDef" = dataclasses.field()

    roleName = field("roleName")
    diskImageFormat = field("diskImageFormat")
    s3Bucket = field("s3Bucket")
    s3Prefix = field("s3Prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ExportConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ExportConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SsmParameterConfiguration:
    boto3_raw_data: "type_defs.SsmParameterConfigurationTypeDef" = dataclasses.field()

    parameterName = field("parameterName")
    amiAccountId = field("amiAccountId")
    dataType = field("dataType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SsmParameterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SsmParameterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsInstanceBlockDeviceSpecification:
    boto3_raw_data: "type_defs.EbsInstanceBlockDeviceSpecificationTypeDef" = (
        dataclasses.field()
    )

    encrypted = field("encrypted")
    deleteOnTermination = field("deleteOnTermination")
    iops = field("iops")
    kmsKeyId = field("kmsKeyId")
    snapshotId = field("snapshotId")
    volumeSize = field("volumeSize")
    volumeType = field("volumeType")
    throughput = field("throughput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EbsInstanceBlockDeviceSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbsInstanceBlockDeviceSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcrConfigurationOutput:
    boto3_raw_data: "type_defs.EcrConfigurationOutputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    containerTags = field("containerTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcrConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcrConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcrConfiguration:
    boto3_raw_data: "type_defs.EcrConfigurationTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    containerTags = field("containerTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcrConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcrConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FastLaunchLaunchTemplateSpecification:
    boto3_raw_data: "type_defs.FastLaunchLaunchTemplateSpecificationTypeDef" = (
        dataclasses.field()
    )

    launchTemplateId = field("launchTemplateId")
    launchTemplateName = field("launchTemplateName")
    launchTemplateVersion = field("launchTemplateVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FastLaunchLaunchTemplateSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FastLaunchLaunchTemplateSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FastLaunchSnapshotConfiguration:
    boto3_raw_data: "type_defs.FastLaunchSnapshotConfigurationTypeDef" = (
        dataclasses.field()
    )

    targetResourceCount = field("targetResourceCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FastLaunchSnapshotConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FastLaunchSnapshotConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentPolicyRequest:
    boto3_raw_data: "type_defs.GetComponentPolicyRequestTypeDef" = dataclasses.field()

    componentArn = field("componentArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentRequest:
    boto3_raw_data: "type_defs.GetComponentRequestTypeDef" = dataclasses.field()

    componentBuildVersionArn = field("componentBuildVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerRecipePolicyRequest:
    boto3_raw_data: "type_defs.GetContainerRecipePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    containerRecipeArn = field("containerRecipeArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetContainerRecipePolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerRecipePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerRecipeRequest:
    boto3_raw_data: "type_defs.GetContainerRecipeRequestTypeDef" = dataclasses.field()

    containerRecipeArn = field("containerRecipeArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContainerRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionConfigurationRequest:
    boto3_raw_data: "type_defs.GetDistributionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    distributionConfigurationArn = field("distributionConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDistributionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImagePipelineRequest:
    boto3_raw_data: "type_defs.GetImagePipelineRequestTypeDef" = dataclasses.field()

    imagePipelineArn = field("imagePipelineArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImagePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImagePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImagePolicyRequest:
    boto3_raw_data: "type_defs.GetImagePolicyRequestTypeDef" = dataclasses.field()

    imageArn = field("imageArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImagePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImagePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageRecipePolicyRequest:
    boto3_raw_data: "type_defs.GetImageRecipePolicyRequestTypeDef" = dataclasses.field()

    imageRecipeArn = field("imageRecipeArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageRecipePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageRecipePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageRecipeRequest:
    boto3_raw_data: "type_defs.GetImageRecipeRequestTypeDef" = dataclasses.field()

    imageRecipeArn = field("imageRecipeArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageRequest:
    boto3_raw_data: "type_defs.GetImageRequestTypeDef" = dataclasses.field()

    imageBuildVersionArn = field("imageBuildVersionArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetImageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetImageRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInfrastructureConfigurationRequest:
    boto3_raw_data: "type_defs.GetInfrastructureConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    infrastructureConfigurationArn = field("infrastructureConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInfrastructureConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInfrastructureConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecycleExecutionRequest:
    boto3_raw_data: "type_defs.GetLifecycleExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    lifecycleExecutionId = field("lifecycleExecutionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLifecycleExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecycleExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.GetLifecyclePolicyRequestTypeDef" = dataclasses.field()

    lifecyclePolicyArn = field("lifecyclePolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMarketplaceResourceRequest:
    boto3_raw_data: "type_defs.GetMarketplaceResourceRequestTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    resourceArn = field("resourceArn")
    resourceLocation = field("resourceLocation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMarketplaceResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMarketplaceResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowExecutionRequest:
    boto3_raw_data: "type_defs.GetWorkflowExecutionRequestTypeDef" = dataclasses.field()

    workflowExecutionId = field("workflowExecutionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowRequest:
    boto3_raw_data: "type_defs.GetWorkflowRequestTypeDef" = dataclasses.field()

    workflowBuildVersionArn = field("workflowBuildVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowStepExecutionRequest:
    boto3_raw_data: "type_defs.GetWorkflowStepExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    stepExecutionId = field("stepExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetWorkflowStepExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowStepExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImagePackage:
    boto3_raw_data: "type_defs.ImagePackageTypeDef" = dataclasses.field()

    packageName = field("packageName")
    packageVersion = field("packageVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImagePackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImagePackageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageRecipeSummary:
    boto3_raw_data: "type_defs.ImageRecipeSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    platform = field("platform")
    owner = field("owner")
    parentImage = field("parentImage")
    dateCreated = field("dateCreated")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageRecipeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageRecipeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageScanFindingsFilter:
    boto3_raw_data: "type_defs.ImageScanFindingsFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageScanFindingsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageScanFindingsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageScanState:
    boto3_raw_data: "type_defs.ImageScanStateTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageScanStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageScanStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageVersion:
    boto3_raw_data: "type_defs.ImageVersionTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    type = field("type")
    version = field("version")
    platform = field("platform")
    osVersion = field("osVersion")
    owner = field("owner")
    dateCreated = field("dateCreated")
    buildType = field("buildType")
    imageSource = field("imageSource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportComponentRequest:
    boto3_raw_data: "type_defs.ImportComponentRequestTypeDef" = dataclasses.field()

    name = field("name")
    semanticVersion = field("semanticVersion")
    type = field("type")
    format = field("format")
    platform = field("platform")
    clientToken = field("clientToken")
    description = field("description")
    changeDescription = field("changeDescription")
    data = field("data")
    uri = field("uri")
    kmsKeyId = field("kmsKeyId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDiskImageRequest:
    boto3_raw_data: "type_defs.ImportDiskImageRequestTypeDef" = dataclasses.field()

    name = field("name")
    semanticVersion = field("semanticVersion")
    platform = field("platform")
    osVersion = field("osVersion")
    infrastructureConfigurationArn = field("infrastructureConfigurationArn")
    uri = field("uri")
    clientToken = field("clientToken")
    description = field("description")
    executionRole = field("executionRole")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportDiskImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDiskImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportVmImageRequest:
    boto3_raw_data: "type_defs.ImportVmImageRequestTypeDef" = dataclasses.field()

    name = field("name")
    semanticVersion = field("semanticVersion")
    platform = field("platform")
    vmImportTaskId = field("vmImportTaskId")
    clientToken = field("clientToken")
    description = field("description")
    osVersion = field("osVersion")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportVmImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportVmImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchPermissionConfiguration:
    boto3_raw_data: "type_defs.LaunchPermissionConfigurationTypeDef" = (
        dataclasses.field()
    )

    userIds = field("userIds")
    userGroups = field("userGroups")
    organizationArns = field("organizationArns")
    organizationalUnitArns = field("organizationalUnitArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LaunchPermissionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchPermissionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExecutionResourceAction:
    boto3_raw_data: "type_defs.LifecycleExecutionResourceActionTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    reason = field("reason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LifecycleExecutionResourceActionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExecutionResourceActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExecutionResourceState:
    boto3_raw_data: "type_defs.LifecycleExecutionResourceStateTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LifecycleExecutionResourceStateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExecutionResourceStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExecutionResourcesImpactedSummary:
    boto3_raw_data: "type_defs.LifecycleExecutionResourcesImpactedSummaryTypeDef" = (
        dataclasses.field()
    )

    hasImpactedResources = field("hasImpactedResources")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecycleExecutionResourcesImpactedSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExecutionResourcesImpactedSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExecutionState:
    boto3_raw_data: "type_defs.LifecycleExecutionStateTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleExecutionStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExecutionStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetailActionIncludeResources:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailActionIncludeResourcesTypeDef" = (
        dataclasses.field()
    )

    amis = field("amis")
    snapshots = field("snapshots")
    containers = field("containers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecyclePolicyDetailActionIncludeResourcesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailActionIncludeResourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetailExclusionRulesAmisLastLaunched:
    boto3_raw_data: (
        "type_defs.LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef"
    ) = dataclasses.field()

    value = field("value")
    unit = field("unit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef"
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
                "type_defs.LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetailFilter:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailFilterTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")
    unit = field("unit")
    retainAtLeast = field("retainAtLeast")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyDetailFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyResourceSelectionRecipe:
    boto3_raw_data: "type_defs.LifecyclePolicyResourceSelectionRecipeTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    semanticVersion = field("semanticVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecyclePolicyResourceSelectionRecipeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyResourceSelectionRecipeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicySummary:
    boto3_raw_data: "type_defs.LifecyclePolicySummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    description = field("description")
    status = field("status")
    executionRole = field("executionRole")
    resourceType = field("resourceType")
    dateCreated = field("dateCreated")
    dateUpdated = field("dateUpdated")
    dateLastRun = field("dateLastRun")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicySummaryTypeDef"]
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
class ListComponentBuildVersionsRequest:
    boto3_raw_data: "type_defs.ListComponentBuildVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    componentVersionArn = field("componentVersionArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComponentBuildVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentBuildVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagePackagesRequest:
    boto3_raw_data: "type_defs.ListImagePackagesRequestTypeDef" = dataclasses.field()

    imageBuildVersionArn = field("imageBuildVersionArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImagePackagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagePackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecycleExecutionResourcesRequest:
    boto3_raw_data: "type_defs.ListLifecycleExecutionResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    lifecycleExecutionId = field("lifecycleExecutionId")
    parentResourceId = field("parentResourceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLifecycleExecutionResourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecycleExecutionResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecycleExecutionsRequest:
    boto3_raw_data: "type_defs.ListLifecycleExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLifecycleExecutionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecycleExecutionsRequestTypeDef"]
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
class ListWaitingWorkflowStepsRequest:
    boto3_raw_data: "type_defs.ListWaitingWorkflowStepsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWaitingWorkflowStepsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWaitingWorkflowStepsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepExecution:
    boto3_raw_data: "type_defs.WorkflowStepExecutionTypeDef" = dataclasses.field()

    stepExecutionId = field("stepExecutionId")
    imageBuildVersionArn = field("imageBuildVersionArn")
    workflowExecutionId = field("workflowExecutionId")
    workflowBuildVersionArn = field("workflowBuildVersionArn")
    name = field("name")
    action = field("action")
    startTime = field("startTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowBuildVersionsRequest:
    boto3_raw_data: "type_defs.ListWorkflowBuildVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    workflowVersionArn = field("workflowVersionArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkflowBuildVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowBuildVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowExecutionsRequest:
    boto3_raw_data: "type_defs.ListWorkflowExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    imageBuildVersionArn = field("imageBuildVersionArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkflowExecutionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionMetadata:
    boto3_raw_data: "type_defs.WorkflowExecutionMetadataTypeDef" = dataclasses.field()

    workflowBuildVersionArn = field("workflowBuildVersionArn")
    workflowExecutionId = field("workflowExecutionId")
    type = field("type")
    status = field("status")
    message = field("message")
    totalStepCount = field("totalStepCount")
    totalStepsSucceeded = field("totalStepsSucceeded")
    totalStepsFailed = field("totalStepsFailed")
    totalStepsSkipped = field("totalStepsSkipped")
    startTime = field("startTime")
    endTime = field("endTime")
    parallelGroup = field("parallelGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowExecutionMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowStepExecutionsRequest:
    boto3_raw_data: "type_defs.ListWorkflowStepExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    workflowExecutionId = field("workflowExecutionId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkflowStepExecutionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowStepExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepMetadata:
    boto3_raw_data: "type_defs.WorkflowStepMetadataTypeDef" = dataclasses.field()

    stepExecutionId = field("stepExecutionId")
    name = field("name")
    description = field("description")
    action = field("action")
    status = field("status")
    rollbackStatus = field("rollbackStatus")
    message = field("message")
    inputs = field("inputs")
    outputs = field("outputs")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowVersion:
    boto3_raw_data: "type_defs.WorkflowVersionTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    version = field("version")
    description = field("description")
    type = field("type")
    owner = field("owner")
    dateCreated = field("dateCreated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkflowVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Logs:
    boto3_raw_data: "type_defs.S3LogsTypeDef" = dataclasses.field()

    s3BucketName = field("s3BucketName")
    s3KeyPrefix = field("s3KeyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LogsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LogsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VulnerablePackage:
    boto3_raw_data: "type_defs.VulnerablePackageTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")
    sourceLayerHash = field("sourceLayerHash")
    epoch = field("epoch")
    release = field("release")
    arch = field("arch")
    packageManager = field("packageManager")
    filePath = field("filePath")
    fixedInVersion = field("fixedInVersion")
    remediation = field("remediation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VulnerablePackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VulnerablePackageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutComponentPolicyRequest:
    boto3_raw_data: "type_defs.PutComponentPolicyRequestTypeDef" = dataclasses.field()

    componentArn = field("componentArn")
    policy = field("policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutComponentPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutComponentPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutContainerRecipePolicyRequest:
    boto3_raw_data: "type_defs.PutContainerRecipePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    containerRecipeArn = field("containerRecipeArn")
    policy = field("policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutContainerRecipePolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutContainerRecipePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImagePolicyRequest:
    boto3_raw_data: "type_defs.PutImagePolicyRequestTypeDef" = dataclasses.field()

    imageArn = field("imageArn")
    policy = field("policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutImagePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutImagePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImageRecipePolicyRequest:
    boto3_raw_data: "type_defs.PutImageRecipePolicyRequestTypeDef" = dataclasses.field()

    imageRecipeArn = field("imageRecipeArn")
    policy = field("policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutImageRecipePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutImageRecipePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationRecommendation:
    boto3_raw_data: "type_defs.RemediationRecommendationTypeDef" = dataclasses.field()

    text = field("text")
    url = field("url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemediationRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceState:
    boto3_raw_data: "type_defs.ResourceStateTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceStateUpdateIncludeResources:
    boto3_raw_data: "type_defs.ResourceStateUpdateIncludeResourcesTypeDef" = (
        dataclasses.field()
    )

    amis = field("amis")
    snapshots = field("snapshots")
    containers = field("containers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourceStateUpdateIncludeResourcesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceStateUpdateIncludeResourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendWorkflowStepActionRequest:
    boto3_raw_data: "type_defs.SendWorkflowStepActionRequestTypeDef" = (
        dataclasses.field()
    )

    stepExecutionId = field("stepExecutionId")
    imageBuildVersionArn = field("imageBuildVersionArn")
    action = field("action")
    clientToken = field("clientToken")
    reason = field("reason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendWorkflowStepActionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendWorkflowStepActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImagePipelineExecutionRequest:
    boto3_raw_data: "type_defs.StartImagePipelineExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    imagePipelineArn = field("imagePipelineArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartImagePipelineExecutionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImagePipelineExecutionRequestTypeDef"]
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
class WorkflowParameterOutput:
    boto3_raw_data: "type_defs.WorkflowParameterOutputTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowParameterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowParameterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowParameterDetail:
    boto3_raw_data: "type_defs.WorkflowParameterDetailTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    defaultValue = field("defaultValue")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowParameterDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowParameterDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowParameter:
    boto3_raw_data: "type_defs.WorkflowParameterTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowState:
    boto3_raw_data: "type_defs.WorkflowStateTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkflowStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAggregation:
    boto3_raw_data: "type_defs.AccountAggregationTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageAggregation:
    boto3_raw_data: "type_defs.ImageAggregationTypeDef" = dataclasses.field()

    imageBuildVersionArn = field("imageBuildVersionArn")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageAggregationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImagePipelineAggregation:
    boto3_raw_data: "type_defs.ImagePipelineAggregationTypeDef" = dataclasses.field()

    imagePipelineArn = field("imagePipelineArn")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImagePipelineAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImagePipelineAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VulnerabilityIdAggregation:
    boto3_raw_data: "type_defs.VulnerabilityIdAggregationTypeDef" = dataclasses.field()

    vulnerabilityId = field("vulnerabilityId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VulnerabilityIdAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VulnerabilityIdAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalInstanceConfiguration:
    boto3_raw_data: "type_defs.AdditionalInstanceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def systemsManagerAgent(self):  # pragma: no cover
        return SystemsManagerAgent.make_one(self.boto3_raw_data["systemsManagerAgent"])

    userDataOverride = field("userDataOverride")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdditionalInstanceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalInstanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiDistributionConfigurationOutput:
    boto3_raw_data: "type_defs.AmiDistributionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")
    targetAccountIds = field("targetAccountIds")
    amiTags = field("amiTags")
    kmsKeyId = field("kmsKeyId")

    @cached_property
    def launchPermission(self):  # pragma: no cover
        return LaunchPermissionConfigurationOutput.make_one(
            self.boto3_raw_data["launchPermission"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmiDistributionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiDistributionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ami:
    boto3_raw_data: "type_defs.AmiTypeDef" = dataclasses.field()

    region = field("region")
    image = field("image")
    name = field("name")
    description = field("description")

    @cached_property
    def state(self):  # pragma: no cover
        return ImageState.make_one(self.boto3_raw_data["state"])

    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AmiTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AmiTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelImageCreationResponse:
    boto3_raw_data: "type_defs.CancelImageCreationResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    clientToken = field("clientToken")
    imageBuildVersionArn = field("imageBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelImageCreationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelImageCreationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelLifecycleExecutionResponse:
    boto3_raw_data: "type_defs.CancelLifecycleExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    lifecycleExecutionId = field("lifecycleExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelLifecycleExecutionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelLifecycleExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentResponse:
    boto3_raw_data: "type_defs.CreateComponentResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    clientToken = field("clientToken")
    componentBuildVersionArn = field("componentBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerRecipeResponse:
    boto3_raw_data: "type_defs.CreateContainerRecipeResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    clientToken = field("clientToken")
    containerRecipeArn = field("containerRecipeArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateContainerRecipeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionConfigurationResponse:
    boto3_raw_data: "type_defs.CreateDistributionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    clientToken = field("clientToken")
    distributionConfigurationArn = field("distributionConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDistributionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImagePipelineResponse:
    boto3_raw_data: "type_defs.CreateImagePipelineResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    clientToken = field("clientToken")
    imagePipelineArn = field("imagePipelineArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImagePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImagePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImageRecipeResponse:
    boto3_raw_data: "type_defs.CreateImageRecipeResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    clientToken = field("clientToken")
    imageRecipeArn = field("imageRecipeArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImageRecipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImageRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImageResponse:
    boto3_raw_data: "type_defs.CreateImageResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    clientToken = field("clientToken")
    imageBuildVersionArn = field("imageBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInfrastructureConfigurationResponse:
    boto3_raw_data: "type_defs.CreateInfrastructureConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    clientToken = field("clientToken")
    infrastructureConfigurationArn = field("infrastructureConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateInfrastructureConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInfrastructureConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.CreateLifecyclePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    clientToken = field("clientToken")
    lifecyclePolicyArn = field("lifecyclePolicyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLifecyclePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowResponse:
    boto3_raw_data: "type_defs.CreateWorkflowResponseTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    workflowBuildVersionArn = field("workflowBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkflowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComponentResponse:
    boto3_raw_data: "type_defs.DeleteComponentResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    componentBuildVersionArn = field("componentBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteComponentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContainerRecipeResponse:
    boto3_raw_data: "type_defs.DeleteContainerRecipeResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    containerRecipeArn = field("containerRecipeArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteContainerRecipeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContainerRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDistributionConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteDistributionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    distributionConfigurationArn = field("distributionConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDistributionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDistributionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImagePipelineResponse:
    boto3_raw_data: "type_defs.DeleteImagePipelineResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    imagePipelineArn = field("imagePipelineArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImagePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImagePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageRecipeResponse:
    boto3_raw_data: "type_defs.DeleteImageRecipeResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    imageRecipeArn = field("imageRecipeArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImageRecipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageResponse:
    boto3_raw_data: "type_defs.DeleteImageResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    imageBuildVersionArn = field("imageBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInfrastructureConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteInfrastructureConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    infrastructureConfigurationArn = field("infrastructureConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteInfrastructureConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInfrastructureConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.DeleteLifecyclePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    lifecyclePolicyArn = field("lifecyclePolicyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteLifecyclePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkflowResponse:
    boto3_raw_data: "type_defs.DeleteWorkflowResponseTypeDef" = dataclasses.field()

    workflowBuildVersionArn = field("workflowBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkflowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentPolicyResponse:
    boto3_raw_data: "type_defs.GetComponentPolicyResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerRecipePolicyResponse:
    boto3_raw_data: "type_defs.GetContainerRecipePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetContainerRecipePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerRecipePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImagePolicyResponse:
    boto3_raw_data: "type_defs.GetImagePolicyResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImagePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImagePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageRecipePolicyResponse:
    boto3_raw_data: "type_defs.GetImageRecipePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageRecipePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageRecipePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMarketplaceResourceResponse:
    boto3_raw_data: "type_defs.GetMarketplaceResourceResponseTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    url = field("url")
    data = field("data")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMarketplaceResourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMarketplaceResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowExecutionResponse:
    boto3_raw_data: "type_defs.GetWorkflowExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    workflowBuildVersionArn = field("workflowBuildVersionArn")
    workflowExecutionId = field("workflowExecutionId")
    imageBuildVersionArn = field("imageBuildVersionArn")
    type = field("type")
    status = field("status")
    message = field("message")
    totalStepCount = field("totalStepCount")
    totalStepsSucceeded = field("totalStepsSucceeded")
    totalStepsFailed = field("totalStepsFailed")
    totalStepsSkipped = field("totalStepsSkipped")
    startTime = field("startTime")
    endTime = field("endTime")
    parallelGroup = field("parallelGroup")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowStepExecutionResponse:
    boto3_raw_data: "type_defs.GetWorkflowStepExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    stepExecutionId = field("stepExecutionId")
    workflowBuildVersionArn = field("workflowBuildVersionArn")
    workflowExecutionId = field("workflowExecutionId")
    imageBuildVersionArn = field("imageBuildVersionArn")
    name = field("name")
    description = field("description")
    action = field("action")
    status = field("status")
    rollbackStatus = field("rollbackStatus")
    message = field("message")
    inputs = field("inputs")
    outputs = field("outputs")
    startTime = field("startTime")
    endTime = field("endTime")
    onFailure = field("onFailure")
    timeoutSeconds = field("timeoutSeconds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetWorkflowStepExecutionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowStepExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportComponentResponse:
    boto3_raw_data: "type_defs.ImportComponentResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    clientToken = field("clientToken")
    componentBuildVersionArn = field("componentBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportComponentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDiskImageResponse:
    boto3_raw_data: "type_defs.ImportDiskImageResponseTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    imageBuildVersionArn = field("imageBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportDiskImageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDiskImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportVmImageResponse:
    boto3_raw_data: "type_defs.ImportVmImageResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    imageArn = field("imageArn")
    clientToken = field("clientToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportVmImageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportVmImageResponseTypeDef"]
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
class PutComponentPolicyResponse:
    boto3_raw_data: "type_defs.PutComponentPolicyResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    componentArn = field("componentArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutComponentPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutComponentPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutContainerRecipePolicyResponse:
    boto3_raw_data: "type_defs.PutContainerRecipePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    containerRecipeArn = field("containerRecipeArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutContainerRecipePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutContainerRecipePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImagePolicyResponse:
    boto3_raw_data: "type_defs.PutImagePolicyResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    imageArn = field("imageArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutImagePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutImagePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImageRecipePolicyResponse:
    boto3_raw_data: "type_defs.PutImageRecipePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    imageRecipeArn = field("imageRecipeArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutImageRecipePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutImageRecipePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendWorkflowStepActionResponse:
    boto3_raw_data: "type_defs.SendWorkflowStepActionResponseTypeDef" = (
        dataclasses.field()
    )

    stepExecutionId = field("stepExecutionId")
    imageBuildVersionArn = field("imageBuildVersionArn")
    clientToken = field("clientToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendWorkflowStepActionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendWorkflowStepActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImagePipelineExecutionResponse:
    boto3_raw_data: "type_defs.StartImagePipelineExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    clientToken = field("clientToken")
    imageBuildVersionArn = field("imageBuildVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartImagePipelineExecutionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImagePipelineExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceStateUpdateResponse:
    boto3_raw_data: "type_defs.StartResourceStateUpdateResponseTypeDef" = (
        dataclasses.field()
    )

    lifecycleExecutionId = field("lifecycleExecutionId")
    resourceArn = field("resourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartResourceStateUpdateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartResourceStateUpdateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateDistributionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    clientToken = field("clientToken")
    distributionConfigurationArn = field("distributionConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDistributionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateImagePipelineResponse:
    boto3_raw_data: "type_defs.UpdateImagePipelineResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")
    clientToken = field("clientToken")
    imagePipelineArn = field("imagePipelineArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateImagePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateImagePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInfrastructureConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateInfrastructureConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    clientToken = field("clientToken")
    infrastructureConfigurationArn = field("infrastructureConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateInfrastructureConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInfrastructureConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.UpdateLifecyclePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    lifecyclePolicyArn = field("lifecyclePolicyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLifecyclePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentConfigurationOutput:
    boto3_raw_data: "type_defs.ComponentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    componentArn = field("componentArn")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ComponentParameterOutput.make_many(self.boto3_raw_data["parameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentConfigurationOutputTypeDef"]
        ],
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
    name = field("name")
    version = field("version")
    platform = field("platform")
    supportedOsVersions = field("supportedOsVersions")

    @cached_property
    def state(self):  # pragma: no cover
        return ComponentState.make_one(self.boto3_raw_data["state"])

    type = field("type")
    owner = field("owner")
    description = field("description")
    changeDescription = field("changeDescription")
    dateCreated = field("dateCreated")
    tags = field("tags")
    publisher = field("publisher")
    obfuscate = field("obfuscate")

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
class Component:
    boto3_raw_data: "type_defs.ComponentTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    version = field("version")
    description = field("description")
    changeDescription = field("changeDescription")
    type = field("type")
    platform = field("platform")
    supportedOsVersions = field("supportedOsVersions")

    @cached_property
    def state(self):  # pragma: no cover
        return ComponentState.make_one(self.boto3_raw_data["state"])

    @cached_property
    def parameters(self):  # pragma: no cover
        return ComponentParameterDetail.make_many(self.boto3_raw_data["parameters"])

    owner = field("owner")
    data = field("data")
    kmsKeyId = field("kmsKeyId")
    encrypted = field("encrypted")
    dateCreated = field("dateCreated")
    tags = field("tags")
    publisher = field("publisher")
    obfuscate = field("obfuscate")

    @cached_property
    def productCodes(self):  # pragma: no cover
        return ProductCodeListItem.make_many(self.boto3_raw_data["productCodes"])

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
class ComponentVersion:
    boto3_raw_data: "type_defs.ComponentVersionTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    version = field("version")
    description = field("description")
    platform = field("platform")
    supportedOsVersions = field("supportedOsVersions")
    type = field("type")
    owner = field("owner")
    dateCreated = field("dateCreated")
    status = field("status")

    @cached_property
    def productCodes(self):  # pragma: no cover
        return ProductCodeListItem.make_many(self.boto3_raw_data["productCodes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerDistributionConfigurationOutput:
    boto3_raw_data: "type_defs.ContainerDistributionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targetRepository(self):  # pragma: no cover
        return TargetContainerRepository.make_one(
            self.boto3_raw_data["targetRepository"]
        )

    description = field("description")
    containerTags = field("containerTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContainerDistributionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerDistributionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerDistributionConfiguration:
    boto3_raw_data: "type_defs.ContainerDistributionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targetRepository(self):  # pragma: no cover
        return TargetContainerRepository.make_one(
            self.boto3_raw_data["targetRepository"]
        )

    description = field("description")
    containerTags = field("containerTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContainerDistributionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerDistributionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerRecipesResponse:
    boto3_raw_data: "type_defs.ListContainerRecipesResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def containerRecipeSummaryList(self):  # pragma: no cover
        return ContainerRecipeSummary.make_many(
            self.boto3_raw_data["containerRecipeSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContainerRecipesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerRecipesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InfrastructureConfigurationSummary:
    boto3_raw_data: "type_defs.InfrastructureConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    description = field("description")
    dateCreated = field("dateCreated")
    dateUpdated = field("dateUpdated")
    resourceTags = field("resourceTags")
    tags = field("tags")
    instanceTypes = field("instanceTypes")
    instanceProfileName = field("instanceProfileName")

    @cached_property
    def placement(self):  # pragma: no cover
        return Placement.make_one(self.boto3_raw_data["placement"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InfrastructureConfigurationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InfrastructureConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CvssScoreDetails:
    boto3_raw_data: "type_defs.CvssScoreDetailsTypeDef" = dataclasses.field()

    scoreSource = field("scoreSource")
    cvssSource = field("cvssSource")
    version = field("version")
    score = field("score")
    scoringVector = field("scoringVector")

    @cached_property
    def adjustments(self):  # pragma: no cover
        return CvssScoreAdjustment.make_many(self.boto3_raw_data["adjustments"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CvssScoreDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CvssScoreDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionConfigurationsResponse:
    boto3_raw_data: "type_defs.ListDistributionConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def distributionConfigurationSummaryList(self):  # pragma: no cover
        return DistributionConfigurationSummary.make_many(
            self.boto3_raw_data["distributionConfigurationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceBlockDeviceMapping:
    boto3_raw_data: "type_defs.InstanceBlockDeviceMappingTypeDef" = dataclasses.field()

    deviceName = field("deviceName")

    @cached_property
    def ebs(self):  # pragma: no cover
        return EbsInstanceBlockDeviceSpecification.make_one(self.boto3_raw_data["ebs"])

    virtualName = field("virtualName")
    noDevice = field("noDevice")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceBlockDeviceMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceBlockDeviceMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageScanningConfigurationOutput:
    boto3_raw_data: "type_defs.ImageScanningConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    imageScanningEnabled = field("imageScanningEnabled")

    @cached_property
    def ecrConfiguration(self):  # pragma: no cover
        return EcrConfigurationOutput.make_one(self.boto3_raw_data["ecrConfiguration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImageScanningConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageScanningConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageScanningConfiguration:
    boto3_raw_data: "type_defs.ImageScanningConfigurationTypeDef" = dataclasses.field()

    imageScanningEnabled = field("imageScanningEnabled")

    @cached_property
    def ecrConfiguration(self):  # pragma: no cover
        return EcrConfiguration.make_one(self.boto3_raw_data["ecrConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageScanningConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageScanningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FastLaunchConfiguration:
    boto3_raw_data: "type_defs.FastLaunchConfigurationTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @cached_property
    def snapshotConfiguration(self):  # pragma: no cover
        return FastLaunchSnapshotConfiguration.make_one(
            self.boto3_raw_data["snapshotConfiguration"]
        )

    maxParallelLaunches = field("maxParallelLaunches")

    @cached_property
    def launchTemplate(self):  # pragma: no cover
        return FastLaunchLaunchTemplateSpecification.make_one(
            self.boto3_raw_data["launchTemplate"]
        )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FastLaunchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FastLaunchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsRequest:
    boto3_raw_data: "type_defs.ListComponentsRequestTypeDef" = dataclasses.field()

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    byName = field("byName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerRecipesRequest:
    boto3_raw_data: "type_defs.ListContainerRecipesRequestTypeDef" = dataclasses.field()

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContainerRecipesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerRecipesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionConfigurationsRequest:
    boto3_raw_data: "type_defs.ListDistributionConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageBuildVersionsRequest:
    boto3_raw_data: "type_defs.ListImageBuildVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    imageVersionArn = field("imageVersionArn")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImageBuildVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageBuildVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagePipelineImagesRequest:
    boto3_raw_data: "type_defs.ListImagePipelineImagesRequestTypeDef" = (
        dataclasses.field()
    )

    imagePipelineArn = field("imagePipelineArn")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImagePipelineImagesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagePipelineImagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagePipelinesRequest:
    boto3_raw_data: "type_defs.ListImagePipelinesRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImagePipelinesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagePipelinesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageRecipesRequest:
    boto3_raw_data: "type_defs.ListImageRecipesRequestTypeDef" = dataclasses.field()

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImageRecipesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageRecipesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageScanFindingAggregationsRequest:
    boto3_raw_data: "type_defs.ListImageScanFindingAggregationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImageScanFindingAggregationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageScanFindingAggregationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagesRequest:
    boto3_raw_data: "type_defs.ListImagesRequestTypeDef" = dataclasses.field()

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    byName = field("byName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    includeDeprecated = field("includeDeprecated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListImagesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInfrastructureConfigurationsRequest:
    boto3_raw_data: "type_defs.ListInfrastructureConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInfrastructureConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInfrastructureConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecyclePoliciesRequest:
    boto3_raw_data: "type_defs.ListLifecyclePoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLifecyclePoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecyclePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsRequest:
    boto3_raw_data: "type_defs.ListWorkflowsRequestTypeDef" = dataclasses.field()

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    byName = field("byName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagePackagesResponse:
    boto3_raw_data: "type_defs.ListImagePackagesResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def imagePackageList(self):  # pragma: no cover
        return ImagePackage.make_many(self.boto3_raw_data["imagePackageList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImagePackagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagePackagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageRecipesResponse:
    boto3_raw_data: "type_defs.ListImageRecipesResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def imageRecipeSummaryList(self):  # pragma: no cover
        return ImageRecipeSummary.make_many(
            self.boto3_raw_data["imageRecipeSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImageRecipesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageRecipesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageScanFindingsRequest:
    boto3_raw_data: "type_defs.ListImageScanFindingsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return ImageScanFindingsFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImageScanFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageScanFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagesResponse:
    boto3_raw_data: "type_defs.ListImagesResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def imageVersionList(self):  # pragma: no cover
        return ImageVersion.make_many(self.boto3_raw_data["imageVersionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExecutionSnapshotResource:
    boto3_raw_data: "type_defs.LifecycleExecutionSnapshotResourceTypeDef" = (
        dataclasses.field()
    )

    snapshotId = field("snapshotId")

    @cached_property
    def state(self):  # pragma: no cover
        return LifecycleExecutionResourceState.make_one(self.boto3_raw_data["state"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecycleExecutionSnapshotResourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExecutionSnapshotResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExecution:
    boto3_raw_data: "type_defs.LifecycleExecutionTypeDef" = dataclasses.field()

    lifecycleExecutionId = field("lifecycleExecutionId")
    lifecyclePolicyArn = field("lifecyclePolicyArn")

    @cached_property
    def resourcesImpactedSummary(self):  # pragma: no cover
        return LifecycleExecutionResourcesImpactedSummary.make_one(
            self.boto3_raw_data["resourcesImpactedSummary"]
        )

    @cached_property
    def state(self):  # pragma: no cover
        return LifecycleExecutionState.make_one(self.boto3_raw_data["state"])

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetailAction:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailActionTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def includeResources(self):  # pragma: no cover
        return LifecyclePolicyDetailActionIncludeResources.make_one(
            self.boto3_raw_data["includeResources"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyDetailActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetailExclusionRulesAmisOutput:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef" = (
        dataclasses.field()
    )

    isPublic = field("isPublic")
    regions = field("regions")
    sharedAccounts = field("sharedAccounts")

    @cached_property
    def lastLaunched(self):  # pragma: no cover
        return LifecyclePolicyDetailExclusionRulesAmisLastLaunched.make_one(
            self.boto3_raw_data["lastLaunched"]
        )

    tagMap = field("tagMap")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetailExclusionRulesAmis:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailExclusionRulesAmisTypeDef" = (
        dataclasses.field()
    )

    isPublic = field("isPublic")
    regions = field("regions")
    sharedAccounts = field("sharedAccounts")

    @cached_property
    def lastLaunched(self):  # pragma: no cover
        return LifecyclePolicyDetailExclusionRulesAmisLastLaunched.make_one(
            self.boto3_raw_data["lastLaunched"]
        )

    tagMap = field("tagMap")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecyclePolicyDetailExclusionRulesAmisTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailExclusionRulesAmisTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyResourceSelectionOutput:
    boto3_raw_data: "type_defs.LifecyclePolicyResourceSelectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def recipes(self):  # pragma: no cover
        return LifecyclePolicyResourceSelectionRecipe.make_many(
            self.boto3_raw_data["recipes"]
        )

    tagMap = field("tagMap")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecyclePolicyResourceSelectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyResourceSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyResourceSelection:
    boto3_raw_data: "type_defs.LifecyclePolicyResourceSelectionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def recipes(self):  # pragma: no cover
        return LifecyclePolicyResourceSelectionRecipe.make_many(
            self.boto3_raw_data["recipes"]
        )

    tagMap = field("tagMap")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LifecyclePolicyResourceSelectionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyResourceSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecyclePoliciesResponse:
    boto3_raw_data: "type_defs.ListLifecyclePoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lifecyclePolicySummaryList(self):  # pragma: no cover
        return LifecyclePolicySummary.make_many(
            self.boto3_raw_data["lifecyclePolicySummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLifecyclePoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecyclePoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentBuildVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListComponentBuildVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    componentVersionArn = field("componentVersionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComponentBuildVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentBuildVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsRequestPaginate:
    boto3_raw_data: "type_defs.ListComponentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    byName = field("byName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListComponentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerRecipesRequestPaginate:
    boto3_raw_data: "type_defs.ListContainerRecipesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContainerRecipesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerRecipesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListDistributionConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageBuildVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListImageBuildVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    imageVersionArn = field("imageVersionArn")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImageBuildVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageBuildVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagePackagesRequestPaginate:
    boto3_raw_data: "type_defs.ListImagePackagesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    imageBuildVersionArn = field("imageBuildVersionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImagePackagesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagePackagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagePipelineImagesRequestPaginate:
    boto3_raw_data: "type_defs.ListImagePipelineImagesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    imagePipelineArn = field("imagePipelineArn")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImagePipelineImagesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagePipelineImagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagePipelinesRequestPaginate:
    boto3_raw_data: "type_defs.ListImagePipelinesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImagePipelinesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagePipelinesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageRecipesRequestPaginate:
    boto3_raw_data: "type_defs.ListImageRecipesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImageRecipesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageRecipesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageScanFindingAggregationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListImageScanFindingAggregationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImageScanFindingAggregationsRequestPaginateTypeDef"
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
                "type_defs.ListImageScanFindingAggregationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageScanFindingsRequestPaginate:
    boto3_raw_data: "type_defs.ListImageScanFindingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return ImageScanFindingsFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImageScanFindingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageScanFindingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagesRequestPaginate:
    boto3_raw_data: "type_defs.ListImagesRequestPaginateTypeDef" = dataclasses.field()

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    byName = field("byName")
    includeDeprecated = field("includeDeprecated")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImagesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInfrastructureConfigurationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListInfrastructureConfigurationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInfrastructureConfigurationsRequestPaginateTypeDef"
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
                "type_defs.ListInfrastructureConfigurationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecycleExecutionResourcesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListLifecycleExecutionResourcesRequestPaginateTypeDef"
    ) = dataclasses.field()

    lifecycleExecutionId = field("lifecycleExecutionId")
    parentResourceId = field("parentResourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLifecycleExecutionResourcesRequestPaginateTypeDef"
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
                "type_defs.ListLifecycleExecutionResourcesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecycleExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListLifecycleExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLifecycleExecutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecycleExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecyclePoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListLifecyclePoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLifecyclePoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecyclePoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWaitingWorkflowStepsRequestPaginate:
    boto3_raw_data: "type_defs.ListWaitingWorkflowStepsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWaitingWorkflowStepsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWaitingWorkflowStepsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowBuildVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkflowBuildVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    workflowVersionArn = field("workflowVersionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkflowBuildVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowBuildVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkflowExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    imageBuildVersionArn = field("imageBuildVersionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkflowExecutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowStepExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkflowStepExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    workflowExecutionId = field("workflowExecutionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkflowStepExecutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowStepExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkflowsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    owner = field("owner")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    byName = field("byName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWaitingWorkflowStepsResponse:
    boto3_raw_data: "type_defs.ListWaitingWorkflowStepsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def steps(self):  # pragma: no cover
        return WorkflowStepExecution.make_many(self.boto3_raw_data["steps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWaitingWorkflowStepsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWaitingWorkflowStepsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowExecutionsResponse:
    boto3_raw_data: "type_defs.ListWorkflowExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def workflowExecutions(self):  # pragma: no cover
        return WorkflowExecutionMetadata.make_many(
            self.boto3_raw_data["workflowExecutions"]
        )

    imageBuildVersionArn = field("imageBuildVersionArn")
    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkflowExecutionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowStepExecutionsResponse:
    boto3_raw_data: "type_defs.ListWorkflowStepExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def steps(self):  # pragma: no cover
        return WorkflowStepMetadata.make_many(self.boto3_raw_data["steps"])

    workflowBuildVersionArn = field("workflowBuildVersionArn")
    workflowExecutionId = field("workflowExecutionId")
    imageBuildVersionArn = field("imageBuildVersionArn")
    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkflowStepExecutionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowStepExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsResponse:
    boto3_raw_data: "type_defs.ListWorkflowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def workflowVersionList(self):  # pragma: no cover
        return WorkflowVersion.make_many(self.boto3_raw_data["workflowVersionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Logging:
    boto3_raw_data: "type_defs.LoggingTypeDef" = dataclasses.field()

    @cached_property
    def s3Logs(self):  # pragma: no cover
        return S3Logs.make_one(self.boto3_raw_data["s3Logs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVulnerabilityDetails:
    boto3_raw_data: "type_defs.PackageVulnerabilityDetailsTypeDef" = dataclasses.field()

    vulnerabilityId = field("vulnerabilityId")

    @cached_property
    def vulnerablePackages(self):  # pragma: no cover
        return VulnerablePackage.make_many(self.boto3_raw_data["vulnerablePackages"])

    source = field("source")

    @cached_property
    def cvss(self):  # pragma: no cover
        return CvssScore.make_many(self.boto3_raw_data["cvss"])

    relatedVulnerabilities = field("relatedVulnerabilities")
    sourceUrl = field("sourceUrl")
    vendorSeverity = field("vendorSeverity")
    vendorCreatedAt = field("vendorCreatedAt")
    vendorUpdatedAt = field("vendorUpdatedAt")
    referenceUrls = field("referenceUrls")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVulnerabilityDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVulnerabilityDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Remediation:
    boto3_raw_data: "type_defs.RemediationTypeDef" = dataclasses.field()

    @cached_property
    def recommendation(self):  # pragma: no cover
        return RemediationRecommendation.make_one(self.boto3_raw_data["recommendation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemediationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemediationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowConfigurationOutput:
    boto3_raw_data: "type_defs.WorkflowConfigurationOutputTypeDef" = dataclasses.field()

    workflowArn = field("workflowArn")

    @cached_property
    def parameters(self):  # pragma: no cover
        return WorkflowParameterOutput.make_many(self.boto3_raw_data["parameters"])

    parallelGroup = field("parallelGroup")
    onFailure = field("onFailure")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowSummary:
    boto3_raw_data: "type_defs.WorkflowSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    version = field("version")
    description = field("description")
    changeDescription = field("changeDescription")
    type = field("type")
    owner = field("owner")

    @cached_property
    def state(self):  # pragma: no cover
        return WorkflowState.make_one(self.boto3_raw_data["state"])

    dateCreated = field("dateCreated")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkflowSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Workflow:
    boto3_raw_data: "type_defs.WorkflowTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    version = field("version")
    description = field("description")
    changeDescription = field("changeDescription")
    type = field("type")

    @cached_property
    def state(self):  # pragma: no cover
        return WorkflowState.make_one(self.boto3_raw_data["state"])

    owner = field("owner")
    data = field("data")
    kmsKeyId = field("kmsKeyId")
    dateCreated = field("dateCreated")
    tags = field("tags")

    @cached_property
    def parameters(self):  # pragma: no cover
        return WorkflowParameterDetail.make_many(self.boto3_raw_data["parameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkflowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageScanFindingAggregation:
    boto3_raw_data: "type_defs.ImageScanFindingAggregationTypeDef" = dataclasses.field()

    @cached_property
    def accountAggregation(self):  # pragma: no cover
        return AccountAggregation.make_one(self.boto3_raw_data["accountAggregation"])

    @cached_property
    def imageAggregation(self):  # pragma: no cover
        return ImageAggregation.make_one(self.boto3_raw_data["imageAggregation"])

    @cached_property
    def imagePipelineAggregation(self):  # pragma: no cover
        return ImagePipelineAggregation.make_one(
            self.boto3_raw_data["imagePipelineAggregation"]
        )

    @cached_property
    def vulnerabilityIdAggregation(self):  # pragma: no cover
        return VulnerabilityIdAggregation.make_one(
            self.boto3_raw_data["vulnerabilityIdAggregation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageScanFindingAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageScanFindingAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputResources:
    boto3_raw_data: "type_defs.OutputResourcesTypeDef" = dataclasses.field()

    @cached_property
    def amis(self):  # pragma: no cover
        return Ami.make_many(self.boto3_raw_data["amis"])

    @cached_property
    def containers(self):  # pragma: no cover
        return Container.make_many(self.boto3_raw_data["containers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputResourcesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputResourcesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentConfiguration:
    boto3_raw_data: "type_defs.ComponentConfigurationTypeDef" = dataclasses.field()

    componentArn = field("componentArn")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentBuildVersionsResponse:
    boto3_raw_data: "type_defs.ListComponentBuildVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def componentSummaryList(self):  # pragma: no cover
        return ComponentSummary.make_many(self.boto3_raw_data["componentSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComponentBuildVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentBuildVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentResponse:
    boto3_raw_data: "type_defs.GetComponentResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def component(self):  # pragma: no cover
        return Component.make_one(self.boto3_raw_data["component"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsResponse:
    boto3_raw_data: "type_defs.ListComponentsResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def componentVersionList(self):  # pragma: no cover
        return ComponentVersion.make_many(self.boto3_raw_data["componentVersionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInfrastructureConfigurationsResponse:
    boto3_raw_data: "type_defs.ListInfrastructureConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def infrastructureConfigurationSummaryList(self):  # pragma: no cover
        return InfrastructureConfigurationSummary.make_many(
            self.boto3_raw_data["infrastructureConfigurationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInfrastructureConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInfrastructureConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InspectorScoreDetails:
    boto3_raw_data: "type_defs.InspectorScoreDetailsTypeDef" = dataclasses.field()

    @cached_property
    def adjustedCvss(self):  # pragma: no cover
        return CvssScoreDetails.make_one(self.boto3_raw_data["adjustedCvss"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InspectorScoreDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InspectorScoreDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageRecipe:
    boto3_raw_data: "type_defs.ImageRecipeTypeDef" = dataclasses.field()

    arn = field("arn")
    type = field("type")
    name = field("name")
    description = field("description")
    platform = field("platform")
    owner = field("owner")
    version = field("version")

    @cached_property
    def components(self):  # pragma: no cover
        return ComponentConfigurationOutput.make_many(self.boto3_raw_data["components"])

    parentImage = field("parentImage")

    @cached_property
    def blockDeviceMappings(self):  # pragma: no cover
        return InstanceBlockDeviceMapping.make_many(
            self.boto3_raw_data["blockDeviceMappings"]
        )

    dateCreated = field("dateCreated")
    tags = field("tags")
    workingDirectory = field("workingDirectory")

    @cached_property
    def additionalInstanceConfiguration(self):  # pragma: no cover
        return AdditionalInstanceConfiguration.make_one(
            self.boto3_raw_data["additionalInstanceConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageRecipeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageRecipeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceConfigurationOutput:
    boto3_raw_data: "type_defs.InstanceConfigurationOutputTypeDef" = dataclasses.field()

    image = field("image")

    @cached_property
    def blockDeviceMappings(self):  # pragma: no cover
        return InstanceBlockDeviceMapping.make_many(
            self.boto3_raw_data["blockDeviceMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceConfiguration:
    boto3_raw_data: "type_defs.InstanceConfigurationTypeDef" = dataclasses.field()

    image = field("image")

    @cached_property
    def blockDeviceMappings(self):  # pragma: no cover
        return InstanceBlockDeviceMapping.make_many(
            self.boto3_raw_data["blockDeviceMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionOutput:
    boto3_raw_data: "type_defs.DistributionOutputTypeDef" = dataclasses.field()

    region = field("region")

    @cached_property
    def amiDistributionConfiguration(self):  # pragma: no cover
        return AmiDistributionConfigurationOutput.make_one(
            self.boto3_raw_data["amiDistributionConfiguration"]
        )

    @cached_property
    def containerDistributionConfiguration(self):  # pragma: no cover
        return ContainerDistributionConfigurationOutput.make_one(
            self.boto3_raw_data["containerDistributionConfiguration"]
        )

    licenseConfigurationArns = field("licenseConfigurationArns")

    @cached_property
    def launchTemplateConfigurations(self):  # pragma: no cover
        return LaunchTemplateConfiguration.make_many(
            self.boto3_raw_data["launchTemplateConfigurations"]
        )

    @cached_property
    def s3ExportConfiguration(self):  # pragma: no cover
        return S3ExportConfiguration.make_one(
            self.boto3_raw_data["s3ExportConfiguration"]
        )

    @cached_property
    def fastLaunchConfigurations(self):  # pragma: no cover
        return FastLaunchConfiguration.make_many(
            self.boto3_raw_data["fastLaunchConfigurations"]
        )

    @cached_property
    def ssmParameterConfigurations(self):  # pragma: no cover
        return SsmParameterConfiguration.make_many(
            self.boto3_raw_data["ssmParameterConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiDistributionConfiguration:
    boto3_raw_data: "type_defs.AmiDistributionConfigurationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")
    targetAccountIds = field("targetAccountIds")
    amiTags = field("amiTags")
    kmsKeyId = field("kmsKeyId")
    launchPermission = field("launchPermission")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AmiDistributionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiDistributionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExecutionResource:
    boto3_raw_data: "type_defs.LifecycleExecutionResourceTypeDef" = dataclasses.field()

    accountId = field("accountId")
    resourceId = field("resourceId")

    @cached_property
    def state(self):  # pragma: no cover
        return LifecycleExecutionResourceState.make_one(self.boto3_raw_data["state"])

    @cached_property
    def action(self):  # pragma: no cover
        return LifecycleExecutionResourceAction.make_one(self.boto3_raw_data["action"])

    region = field("region")

    @cached_property
    def snapshots(self):  # pragma: no cover
        return LifecycleExecutionSnapshotResource.make_many(
            self.boto3_raw_data["snapshots"]
        )

    imageUris = field("imageUris")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleExecutionResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExecutionResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecycleExecutionResponse:
    boto3_raw_data: "type_defs.GetLifecycleExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lifecycleExecution(self):  # pragma: no cover
        return LifecycleExecution.make_one(self.boto3_raw_data["lifecycleExecution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLifecycleExecutionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecycleExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecycleExecutionsResponse:
    boto3_raw_data: "type_defs.ListLifecycleExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lifecycleExecutions(self):  # pragma: no cover
        return LifecycleExecution.make_many(self.boto3_raw_data["lifecycleExecutions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLifecycleExecutionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecycleExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetailExclusionRulesOutput:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailExclusionRulesOutputTypeDef" = (
        dataclasses.field()
    )

    tagMap = field("tagMap")

    @cached_property
    def amis(self):  # pragma: no cover
        return LifecyclePolicyDetailExclusionRulesAmisOutput.make_one(
            self.boto3_raw_data["amis"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecyclePolicyDetailExclusionRulesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailExclusionRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInfrastructureConfigurationRequest:
    boto3_raw_data: "type_defs.CreateInfrastructureConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    instanceProfileName = field("instanceProfileName")
    clientToken = field("clientToken")
    description = field("description")
    instanceTypes = field("instanceTypes")
    securityGroupIds = field("securityGroupIds")
    subnetId = field("subnetId")

    @cached_property
    def logging(self):  # pragma: no cover
        return Logging.make_one(self.boto3_raw_data["logging"])

    keyPair = field("keyPair")
    terminateInstanceOnFailure = field("terminateInstanceOnFailure")
    snsTopicArn = field("snsTopicArn")
    resourceTags = field("resourceTags")

    @cached_property
    def instanceMetadataOptions(self):  # pragma: no cover
        return InstanceMetadataOptions.make_one(
            self.boto3_raw_data["instanceMetadataOptions"]
        )

    tags = field("tags")

    @cached_property
    def placement(self):  # pragma: no cover
        return Placement.make_one(self.boto3_raw_data["placement"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateInfrastructureConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInfrastructureConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InfrastructureConfiguration:
    boto3_raw_data: "type_defs.InfrastructureConfigurationTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    description = field("description")
    instanceTypes = field("instanceTypes")
    instanceProfileName = field("instanceProfileName")
    securityGroupIds = field("securityGroupIds")
    subnetId = field("subnetId")

    @cached_property
    def logging(self):  # pragma: no cover
        return Logging.make_one(self.boto3_raw_data["logging"])

    keyPair = field("keyPair")
    terminateInstanceOnFailure = field("terminateInstanceOnFailure")
    snsTopicArn = field("snsTopicArn")
    dateCreated = field("dateCreated")
    dateUpdated = field("dateUpdated")
    resourceTags = field("resourceTags")

    @cached_property
    def instanceMetadataOptions(self):  # pragma: no cover
        return InstanceMetadataOptions.make_one(
            self.boto3_raw_data["instanceMetadataOptions"]
        )

    tags = field("tags")

    @cached_property
    def placement(self):  # pragma: no cover
        return Placement.make_one(self.boto3_raw_data["placement"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InfrastructureConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InfrastructureConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInfrastructureConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateInfrastructureConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    infrastructureConfigurationArn = field("infrastructureConfigurationArn")
    instanceProfileName = field("instanceProfileName")
    clientToken = field("clientToken")
    description = field("description")
    instanceTypes = field("instanceTypes")
    securityGroupIds = field("securityGroupIds")
    subnetId = field("subnetId")

    @cached_property
    def logging(self):  # pragma: no cover
        return Logging.make_one(self.boto3_raw_data["logging"])

    keyPair = field("keyPair")
    terminateInstanceOnFailure = field("terminateInstanceOnFailure")
    snsTopicArn = field("snsTopicArn")
    resourceTags = field("resourceTags")

    @cached_property
    def instanceMetadataOptions(self):  # pragma: no cover
        return InstanceMetadataOptions.make_one(
            self.boto3_raw_data["instanceMetadataOptions"]
        )

    @cached_property
    def placement(self):  # pragma: no cover
        return Placement.make_one(self.boto3_raw_data["placement"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateInfrastructureConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInfrastructureConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImagePipeline:
    boto3_raw_data: "type_defs.ImagePipelineTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    description = field("description")
    platform = field("platform")
    enhancedImageMetadataEnabled = field("enhancedImageMetadataEnabled")
    imageRecipeArn = field("imageRecipeArn")
    containerRecipeArn = field("containerRecipeArn")
    infrastructureConfigurationArn = field("infrastructureConfigurationArn")
    distributionConfigurationArn = field("distributionConfigurationArn")

    @cached_property
    def imageTestsConfiguration(self):  # pragma: no cover
        return ImageTestsConfiguration.make_one(
            self.boto3_raw_data["imageTestsConfiguration"]
        )

    @cached_property
    def schedule(self):  # pragma: no cover
        return Schedule.make_one(self.boto3_raw_data["schedule"])

    status = field("status")
    dateCreated = field("dateCreated")
    dateUpdated = field("dateUpdated")
    dateLastRun = field("dateLastRun")
    dateNextRun = field("dateNextRun")
    tags = field("tags")

    @cached_property
    def imageScanningConfiguration(self):  # pragma: no cover
        return ImageScanningConfigurationOutput.make_one(
            self.boto3_raw_data["imageScanningConfiguration"]
        )

    executionRole = field("executionRole")

    @cached_property
    def workflows(self):  # pragma: no cover
        return WorkflowConfigurationOutput.make_many(self.boto3_raw_data["workflows"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImagePipelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImagePipelineTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowConfiguration:
    boto3_raw_data: "type_defs.WorkflowConfigurationTypeDef" = dataclasses.field()

    workflowArn = field("workflowArn")
    parameters = field("parameters")
    parallelGroup = field("parallelGroup")
    onFailure = field("onFailure")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowBuildVersionsResponse:
    boto3_raw_data: "type_defs.ListWorkflowBuildVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workflowSummaryList(self):  # pragma: no cover
        return WorkflowSummary.make_many(self.boto3_raw_data["workflowSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkflowBuildVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowBuildVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowResponse:
    boto3_raw_data: "type_defs.GetWorkflowResponseTypeDef" = dataclasses.field()

    @cached_property
    def workflow(self):  # pragma: no cover
        return Workflow.make_one(self.boto3_raw_data["workflow"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageScanFindingAggregationsResponse:
    boto3_raw_data: "type_defs.ListImageScanFindingAggregationsResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    aggregationType = field("aggregationType")

    @cached_property
    def responses(self):  # pragma: no cover
        return ImageScanFindingAggregation.make_many(self.boto3_raw_data["responses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImageScanFindingAggregationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageScanFindingAggregationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageSummary:
    boto3_raw_data: "type_defs.ImageSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    type = field("type")
    version = field("version")
    platform = field("platform")
    osVersion = field("osVersion")

    @cached_property
    def state(self):  # pragma: no cover
        return ImageState.make_one(self.boto3_raw_data["state"])

    owner = field("owner")
    dateCreated = field("dateCreated")

    @cached_property
    def outputResources(self):  # pragma: no cover
        return OutputResources.make_one(self.boto3_raw_data["outputResources"])

    tags = field("tags")
    buildType = field("buildType")
    imageSource = field("imageSource")
    deprecationTime = field("deprecationTime")
    lifecycleExecutionId = field("lifecycleExecutionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageScanFinding:
    boto3_raw_data: "type_defs.ImageScanFindingTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    imageBuildVersionArn = field("imageBuildVersionArn")
    imagePipelineArn = field("imagePipelineArn")
    type = field("type")
    description = field("description")
    title = field("title")

    @cached_property
    def remediation(self):  # pragma: no cover
        return Remediation.make_one(self.boto3_raw_data["remediation"])

    severity = field("severity")
    firstObservedAt = field("firstObservedAt")
    updatedAt = field("updatedAt")
    inspectorScore = field("inspectorScore")

    @cached_property
    def inspectorScoreDetails(self):  # pragma: no cover
        return InspectorScoreDetails.make_one(
            self.boto3_raw_data["inspectorScoreDetails"]
        )

    @cached_property
    def packageVulnerabilityDetails(self):  # pragma: no cover
        return PackageVulnerabilityDetails.make_one(
            self.boto3_raw_data["packageVulnerabilityDetails"]
        )

    fixAvailable = field("fixAvailable")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageScanFindingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageScanFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageRecipeResponse:
    boto3_raw_data: "type_defs.GetImageRecipeResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def imageRecipe(self):  # pragma: no cover
        return ImageRecipe.make_one(self.boto3_raw_data["imageRecipe"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImageRecipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerRecipe:
    boto3_raw_data: "type_defs.ContainerRecipeTypeDef" = dataclasses.field()

    arn = field("arn")
    containerType = field("containerType")
    name = field("name")
    description = field("description")
    platform = field("platform")
    owner = field("owner")
    version = field("version")

    @cached_property
    def components(self):  # pragma: no cover
        return ComponentConfigurationOutput.make_many(self.boto3_raw_data["components"])

    @cached_property
    def instanceConfiguration(self):  # pragma: no cover
        return InstanceConfigurationOutput.make_one(
            self.boto3_raw_data["instanceConfiguration"]
        )

    dockerfileTemplateData = field("dockerfileTemplateData")
    kmsKeyId = field("kmsKeyId")
    encrypted = field("encrypted")
    parentImage = field("parentImage")
    dateCreated = field("dateCreated")
    tags = field("tags")
    workingDirectory = field("workingDirectory")

    @cached_property
    def targetRepository(self):  # pragma: no cover
        return TargetContainerRepository.make_one(
            self.boto3_raw_data["targetRepository"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerRecipeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerRecipeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionConfiguration:
    boto3_raw_data: "type_defs.DistributionConfigurationTypeDef" = dataclasses.field()

    timeoutMinutes = field("timeoutMinutes")
    arn = field("arn")
    name = field("name")
    description = field("description")

    @cached_property
    def distributions(self):  # pragma: no cover
        return DistributionOutput.make_many(self.boto3_raw_data["distributions"])

    dateCreated = field("dateCreated")
    dateUpdated = field("dateUpdated")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecycleExecutionResourcesResponse:
    boto3_raw_data: "type_defs.ListLifecycleExecutionResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    lifecycleExecutionId = field("lifecycleExecutionId")

    @cached_property
    def lifecycleExecutionState(self):  # pragma: no cover
        return LifecycleExecutionState.make_one(
            self.boto3_raw_data["lifecycleExecutionState"]
        )

    @cached_property
    def resources(self):  # pragma: no cover
        return LifecycleExecutionResource.make_many(self.boto3_raw_data["resources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLifecycleExecutionResourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecycleExecutionResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetailOutput:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailOutputTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return LifecyclePolicyDetailAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def filter(self):  # pragma: no cover
        return LifecyclePolicyDetailFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def exclusionRules(self):  # pragma: no cover
        return LifecyclePolicyDetailExclusionRulesOutput.make_one(
            self.boto3_raw_data["exclusionRules"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyDetailOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetailExclusionRules:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailExclusionRulesTypeDef" = (
        dataclasses.field()
    )

    tagMap = field("tagMap")
    amis = field("amis")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecyclePolicyDetailExclusionRulesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailExclusionRulesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceStateUpdateExclusionRules:
    boto3_raw_data: "type_defs.ResourceStateUpdateExclusionRulesTypeDef" = (
        dataclasses.field()
    )

    amis = field("amis")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourceStateUpdateExclusionRulesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceStateUpdateExclusionRulesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInfrastructureConfigurationResponse:
    boto3_raw_data: "type_defs.GetInfrastructureConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def infrastructureConfiguration(self):  # pragma: no cover
        return InfrastructureConfiguration.make_one(
            self.boto3_raw_data["infrastructureConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInfrastructureConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInfrastructureConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImagePipelineResponse:
    boto3_raw_data: "type_defs.GetImagePipelineResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def imagePipeline(self):  # pragma: no cover
        return ImagePipeline.make_one(self.boto3_raw_data["imagePipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImagePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImagePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagePipelinesResponse:
    boto3_raw_data: "type_defs.ListImagePipelinesResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def imagePipelineList(self):  # pragma: no cover
        return ImagePipeline.make_many(self.boto3_raw_data["imagePipelineList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImagePipelinesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagePipelinesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageBuildVersionsResponse:
    boto3_raw_data: "type_defs.ListImageBuildVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def imageSummaryList(self):  # pragma: no cover
        return ImageSummary.make_many(self.boto3_raw_data["imageSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImageBuildVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageBuildVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagePipelineImagesResponse:
    boto3_raw_data: "type_defs.ListImagePipelineImagesResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def imageSummaryList(self):  # pragma: no cover
        return ImageSummary.make_many(self.boto3_raw_data["imageSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImagePipelineImagesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagePipelineImagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImageRecipeRequest:
    boto3_raw_data: "type_defs.CreateImageRecipeRequestTypeDef" = dataclasses.field()

    name = field("name")
    semanticVersion = field("semanticVersion")
    components = field("components")
    parentImage = field("parentImage")
    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def blockDeviceMappings(self):  # pragma: no cover
        return InstanceBlockDeviceMapping.make_many(
            self.boto3_raw_data["blockDeviceMappings"]
        )

    tags = field("tags")
    workingDirectory = field("workingDirectory")

    @cached_property
    def additionalInstanceConfiguration(self):  # pragma: no cover
        return AdditionalInstanceConfiguration.make_one(
            self.boto3_raw_data["additionalInstanceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImageRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImageRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImageScanFindingsResponse:
    boto3_raw_data: "type_defs.ListImageScanFindingsResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def findings(self):  # pragma: no cover
        return ImageScanFinding.make_many(self.boto3_raw_data["findings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImageScanFindingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImageScanFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContainerRecipeResponse:
    boto3_raw_data: "type_defs.GetContainerRecipeResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def containerRecipe(self):  # pragma: no cover
        return ContainerRecipe.make_one(self.boto3_raw_data["containerRecipe"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContainerRecipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContainerRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContainerRecipeRequest:
    boto3_raw_data: "type_defs.CreateContainerRecipeRequestTypeDef" = (
        dataclasses.field()
    )

    containerType = field("containerType")
    name = field("name")
    semanticVersion = field("semanticVersion")
    components = field("components")
    parentImage = field("parentImage")

    @cached_property
    def targetRepository(self):  # pragma: no cover
        return TargetContainerRepository.make_one(
            self.boto3_raw_data["targetRepository"]
        )

    clientToken = field("clientToken")
    description = field("description")
    instanceConfiguration = field("instanceConfiguration")
    dockerfileTemplateData = field("dockerfileTemplateData")
    dockerfileTemplateUri = field("dockerfileTemplateUri")
    platformOverride = field("platformOverride")
    imageOsVersionOverride = field("imageOsVersionOverride")
    tags = field("tags")
    workingDirectory = field("workingDirectory")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContainerRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContainerRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionConfigurationResponse:
    boto3_raw_data: "type_defs.GetDistributionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")

    @cached_property
    def distributionConfiguration(self):  # pragma: no cover
        return DistributionConfiguration.make_one(
            self.boto3_raw_data["distributionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDistributionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Image:
    boto3_raw_data: "type_defs.ImageTypeDef" = dataclasses.field()

    arn = field("arn")
    type = field("type")
    name = field("name")
    version = field("version")
    platform = field("platform")
    enhancedImageMetadataEnabled = field("enhancedImageMetadataEnabled")
    osVersion = field("osVersion")

    @cached_property
    def state(self):  # pragma: no cover
        return ImageState.make_one(self.boto3_raw_data["state"])

    @cached_property
    def imageRecipe(self):  # pragma: no cover
        return ImageRecipe.make_one(self.boto3_raw_data["imageRecipe"])

    @cached_property
    def containerRecipe(self):  # pragma: no cover
        return ContainerRecipe.make_one(self.boto3_raw_data["containerRecipe"])

    sourcePipelineName = field("sourcePipelineName")
    sourcePipelineArn = field("sourcePipelineArn")

    @cached_property
    def infrastructureConfiguration(self):  # pragma: no cover
        return InfrastructureConfiguration.make_one(
            self.boto3_raw_data["infrastructureConfiguration"]
        )

    @cached_property
    def distributionConfiguration(self):  # pragma: no cover
        return DistributionConfiguration.make_one(
            self.boto3_raw_data["distributionConfiguration"]
        )

    @cached_property
    def imageTestsConfiguration(self):  # pragma: no cover
        return ImageTestsConfiguration.make_one(
            self.boto3_raw_data["imageTestsConfiguration"]
        )

    dateCreated = field("dateCreated")

    @cached_property
    def outputResources(self):  # pragma: no cover
        return OutputResources.make_one(self.boto3_raw_data["outputResources"])

    tags = field("tags")
    buildType = field("buildType")
    imageSource = field("imageSource")

    @cached_property
    def scanState(self):  # pragma: no cover
        return ImageScanState.make_one(self.boto3_raw_data["scanState"])

    @cached_property
    def imageScanningConfiguration(self):  # pragma: no cover
        return ImageScanningConfigurationOutput.make_one(
            self.boto3_raw_data["imageScanningConfiguration"]
        )

    deprecationTime = field("deprecationTime")
    lifecycleExecutionId = field("lifecycleExecutionId")
    executionRole = field("executionRole")

    @cached_property
    def workflows(self):  # pragma: no cover
        return WorkflowConfigurationOutput.make_many(self.boto3_raw_data["workflows"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Distribution:
    boto3_raw_data: "type_defs.DistributionTypeDef" = dataclasses.field()

    region = field("region")
    amiDistributionConfiguration = field("amiDistributionConfiguration")
    containerDistributionConfiguration = field("containerDistributionConfiguration")
    licenseConfigurationArns = field("licenseConfigurationArns")

    @cached_property
    def launchTemplateConfigurations(self):  # pragma: no cover
        return LaunchTemplateConfiguration.make_many(
            self.boto3_raw_data["launchTemplateConfigurations"]
        )

    @cached_property
    def s3ExportConfiguration(self):  # pragma: no cover
        return S3ExportConfiguration.make_one(
            self.boto3_raw_data["s3ExportConfiguration"]
        )

    @cached_property
    def fastLaunchConfigurations(self):  # pragma: no cover
        return FastLaunchConfiguration.make_many(
            self.boto3_raw_data["fastLaunchConfigurations"]
        )

    @cached_property
    def ssmParameterConfigurations(self):  # pragma: no cover
        return SsmParameterConfiguration.make_many(
            self.boto3_raw_data["ssmParameterConfigurations"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DistributionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DistributionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicy:
    boto3_raw_data: "type_defs.LifecyclePolicyTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    description = field("description")
    status = field("status")
    executionRole = field("executionRole")
    resourceType = field("resourceType")

    @cached_property
    def policyDetails(self):  # pragma: no cover
        return LifecyclePolicyDetailOutput.make_many(
            self.boto3_raw_data["policyDetails"]
        )

    @cached_property
    def resourceSelection(self):  # pragma: no cover
        return LifecyclePolicyResourceSelectionOutput.make_one(
            self.boto3_raw_data["resourceSelection"]
        )

    dateCreated = field("dateCreated")
    dateUpdated = field("dateUpdated")
    dateLastRun = field("dateLastRun")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifecyclePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceStateUpdateRequest:
    boto3_raw_data: "type_defs.StartResourceStateUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @cached_property
    def state(self):  # pragma: no cover
        return ResourceState.make_one(self.boto3_raw_data["state"])

    clientToken = field("clientToken")
    executionRole = field("executionRole")

    @cached_property
    def includeResources(self):  # pragma: no cover
        return ResourceStateUpdateIncludeResources.make_one(
            self.boto3_raw_data["includeResources"]
        )

    @cached_property
    def exclusionRules(self):  # pragma: no cover
        return ResourceStateUpdateExclusionRules.make_one(
            self.boto3_raw_data["exclusionRules"]
        )

    updateAt = field("updateAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartResourceStateUpdateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartResourceStateUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImagePipelineRequest:
    boto3_raw_data: "type_defs.CreateImagePipelineRequestTypeDef" = dataclasses.field()

    name = field("name")
    infrastructureConfigurationArn = field("infrastructureConfigurationArn")
    clientToken = field("clientToken")
    description = field("description")
    imageRecipeArn = field("imageRecipeArn")
    containerRecipeArn = field("containerRecipeArn")
    distributionConfigurationArn = field("distributionConfigurationArn")

    @cached_property
    def imageTestsConfiguration(self):  # pragma: no cover
        return ImageTestsConfiguration.make_one(
            self.boto3_raw_data["imageTestsConfiguration"]
        )

    enhancedImageMetadataEnabled = field("enhancedImageMetadataEnabled")

    @cached_property
    def schedule(self):  # pragma: no cover
        return Schedule.make_one(self.boto3_raw_data["schedule"])

    status = field("status")
    tags = field("tags")
    imageScanningConfiguration = field("imageScanningConfiguration")
    workflows = field("workflows")
    executionRole = field("executionRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImagePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImagePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImageRequest:
    boto3_raw_data: "type_defs.CreateImageRequestTypeDef" = dataclasses.field()

    infrastructureConfigurationArn = field("infrastructureConfigurationArn")
    clientToken = field("clientToken")
    imageRecipeArn = field("imageRecipeArn")
    containerRecipeArn = field("containerRecipeArn")
    distributionConfigurationArn = field("distributionConfigurationArn")

    @cached_property
    def imageTestsConfiguration(self):  # pragma: no cover
        return ImageTestsConfiguration.make_one(
            self.boto3_raw_data["imageTestsConfiguration"]
        )

    enhancedImageMetadataEnabled = field("enhancedImageMetadataEnabled")
    tags = field("tags")
    imageScanningConfiguration = field("imageScanningConfiguration")
    workflows = field("workflows")
    executionRole = field("executionRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateImagePipelineRequest:
    boto3_raw_data: "type_defs.UpdateImagePipelineRequestTypeDef" = dataclasses.field()

    imagePipelineArn = field("imagePipelineArn")
    infrastructureConfigurationArn = field("infrastructureConfigurationArn")
    clientToken = field("clientToken")
    description = field("description")
    imageRecipeArn = field("imageRecipeArn")
    containerRecipeArn = field("containerRecipeArn")
    distributionConfigurationArn = field("distributionConfigurationArn")

    @cached_property
    def imageTestsConfiguration(self):  # pragma: no cover
        return ImageTestsConfiguration.make_one(
            self.boto3_raw_data["imageTestsConfiguration"]
        )

    enhancedImageMetadataEnabled = field("enhancedImageMetadataEnabled")

    @cached_property
    def schedule(self):  # pragma: no cover
        return Schedule.make_one(self.boto3_raw_data["schedule"])

    status = field("status")
    imageScanningConfiguration = field("imageScanningConfiguration")
    workflows = field("workflows")
    executionRole = field("executionRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateImagePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateImagePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImageResponse:
    boto3_raw_data: "type_defs.GetImageResponseTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["image"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetImageResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.GetLifecyclePolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def lifecyclePolicy(self):  # pragma: no cover
        return LifecyclePolicy.make_one(self.boto3_raw_data["lifecyclePolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLifecyclePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetail:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return LifecyclePolicyDetailAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def filter(self):  # pragma: no cover
        return LifecyclePolicyDetailFilter.make_one(self.boto3_raw_data["filter"])

    exclusionRules = field("exclusionRules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionConfigurationRequest:
    boto3_raw_data: "type_defs.CreateDistributionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    distributions = field("distributions")
    clientToken = field("clientToken")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDistributionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateDistributionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    distributionConfigurationArn = field("distributionConfigurationArn")
    distributions = field("distributions")
    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDistributionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.CreateLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    executionRole = field("executionRole")
    resourceType = field("resourceType")
    policyDetails = field("policyDetails")
    resourceSelection = field("resourceSelection")
    clientToken = field("clientToken")
    description = field("description")
    status = field("status")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.UpdateLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    lifecyclePolicyArn = field("lifecyclePolicyArn")
    executionRole = field("executionRole")
    resourceType = field("resourceType")
    policyDetails = field("policyDetails")
    resourceSelection = field("resourceSelection")
    clientToken = field("clientToken")
    description = field("description")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
