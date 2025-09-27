# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_greengrassv2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssociateClientDeviceWithCoreDeviceEntry:
    boto3_raw_data: "type_defs.AssociateClientDeviceWithCoreDeviceEntryTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateClientDeviceWithCoreDeviceEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateClientDeviceWithCoreDeviceEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateClientDeviceWithCoreDeviceErrorEntry:
    boto3_raw_data: "type_defs.AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef"]
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

    roleArn = field("roleArn")

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
class AssociatedClientDevice:
    boto3_raw_data: "type_defs.AssociatedClientDeviceTypeDef" = dataclasses.field()

    thingName = field("thingName")
    associationTimestamp = field("associationTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedClientDeviceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedClientDeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateClientDeviceFromCoreDeviceEntry:
    boto3_raw_data: "type_defs.DisassociateClientDeviceFromCoreDeviceEntryTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateClientDeviceFromCoreDeviceEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateClientDeviceFromCoreDeviceEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateClientDeviceFromCoreDeviceErrorEntry:
    boto3_raw_data: (
        "type_defs.DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef"
    ) = dataclasses.field()

    thingName = field("thingName")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef"
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
                "type_defs.DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelDeploymentRequest:
    boto3_raw_data: "type_defs.CancelDeploymentRequestTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudComponentStatus:
    boto3_raw_data: "type_defs.CloudComponentStatusTypeDef" = dataclasses.field()

    componentState = field("componentState")
    message = field("message")
    errors = field("errors")
    vendorGuidance = field("vendorGuidance")
    vendorGuidanceMessage = field("vendorGuidanceMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudComponentStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudComponentStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentCandidate:
    boto3_raw_data: "type_defs.ComponentCandidateTypeDef" = dataclasses.field()

    componentName = field("componentName")
    componentVersion = field("componentVersion")
    versionRequirements = field("versionRequirements")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentCandidateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentCandidateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentConfigurationUpdateOutput:
    boto3_raw_data: "type_defs.ComponentConfigurationUpdateOutputTypeDef" = (
        dataclasses.field()
    )

    merge = field("merge")
    reset = field("reset")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentConfigurationUpdateOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentConfigurationUpdateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentConfigurationUpdate:
    boto3_raw_data: "type_defs.ComponentConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    merge = field("merge")
    reset = field("reset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentConfigurationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentDependencyRequirement:
    boto3_raw_data: "type_defs.ComponentDependencyRequirementTypeDef" = (
        dataclasses.field()
    )

    versionRequirement = field("versionRequirement")
    dependencyType = field("dependencyType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComponentDependencyRequirementTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentDependencyRequirementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentPlatformOutput:
    boto3_raw_data: "type_defs.ComponentPlatformOutputTypeDef" = dataclasses.field()

    name = field("name")
    attributes = field("attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentPlatformOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentPlatformOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentPlatform:
    boto3_raw_data: "type_defs.ComponentPlatformTypeDef" = dataclasses.field()

    name = field("name")
    attributes = field("attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentPlatformTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentPlatformTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SystemResourceLimits:
    boto3_raw_data: "type_defs.SystemResourceLimitsTypeDef" = dataclasses.field()

    memory = field("memory")
    cpus = field("cpus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SystemResourceLimitsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SystemResourceLimitsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentVersionListItem:
    boto3_raw_data: "type_defs.ComponentVersionListItemTypeDef" = dataclasses.field()

    componentName = field("componentName")
    componentVersion = field("componentVersion")
    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentVersionListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentVersionListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectivityInfo:
    boto3_raw_data: "type_defs.ConnectivityInfoTypeDef" = dataclasses.field()

    id = field("id")
    hostAddress = field("hostAddress")
    portNumber = field("portNumber")
    metadata = field("metadata")

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
class CoreDevice:
    boto3_raw_data: "type_defs.CoreDeviceTypeDef" = dataclasses.field()

    coreDeviceThingName = field("coreDeviceThingName")
    status = field("status")
    lastStatusUpdateTimestamp = field("lastStatusUpdateTimestamp")
    platform = field("platform")
    architecture = field("architecture")
    runtime = field("runtime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoreDeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoreDeviceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComponentRequest:
    boto3_raw_data: "type_defs.DeleteComponentRequestTypeDef" = dataclasses.field()

    arn = field("arn")

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
class DeleteCoreDeviceRequest:
    boto3_raw_data: "type_defs.DeleteCoreDeviceRequestTypeDef" = dataclasses.field()

    coreDeviceThingName = field("coreDeviceThingName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCoreDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCoreDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeploymentRequest:
    boto3_raw_data: "type_defs.DeleteDeploymentRequestTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentComponentUpdatePolicy:
    boto3_raw_data: "type_defs.DeploymentComponentUpdatePolicyTypeDef" = (
        dataclasses.field()
    )

    timeoutInSeconds = field("timeoutInSeconds")
    action = field("action")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeploymentComponentUpdatePolicyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentComponentUpdatePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentConfigurationValidationPolicy:
    boto3_raw_data: "type_defs.DeploymentConfigurationValidationPolicyTypeDef" = (
        dataclasses.field()
    )

    timeoutInSeconds = field("timeoutInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeploymentConfigurationValidationPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentConfigurationValidationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IoTJobTimeoutConfig:
    boto3_raw_data: "type_defs.IoTJobTimeoutConfigTypeDef" = dataclasses.field()

    inProgressTimeoutInMinutes = field("inProgressTimeoutInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IoTJobTimeoutConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IoTJobTimeoutConfigTypeDef"]
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

    targetArn = field("targetArn")
    revisionId = field("revisionId")
    deploymentId = field("deploymentId")
    deploymentName = field("deploymentName")
    creationTimestamp = field("creationTimestamp")
    deploymentStatus = field("deploymentStatus")
    isLatestForTarget = field("isLatestForTarget")
    parentTargetArn = field("parentTargetArn")

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
class DescribeComponentRequest:
    boto3_raw_data: "type_defs.DescribeComponentRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EffectiveDeploymentStatusDetails:
    boto3_raw_data: "type_defs.EffectiveDeploymentStatusDetailsTypeDef" = (
        dataclasses.field()
    )

    errorStack = field("errorStack")
    errorTypes = field("errorTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EffectiveDeploymentStatusDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EffectiveDeploymentStatusDetailsTypeDef"]
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

    arn = field("arn")
    recipeOutputFormat = field("recipeOutputFormat")

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
class GetComponentVersionArtifactRequest:
    boto3_raw_data: "type_defs.GetComponentVersionArtifactRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    artifactName = field("artifactName")
    s3EndpointType = field("s3EndpointType")
    iotEndpointType = field("iotEndpointType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComponentVersionArtifactRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentVersionArtifactRequestTypeDef"]
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

    thingName = field("thingName")

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
class GetCoreDeviceRequest:
    boto3_raw_data: "type_defs.GetCoreDeviceRequestTypeDef" = dataclasses.field()

    coreDeviceThingName = field("coreDeviceThingName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCoreDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentRequest:
    boto3_raw_data: "type_defs.GetDeploymentRequestTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstalledComponent:
    boto3_raw_data: "type_defs.InstalledComponentTypeDef" = dataclasses.field()

    componentName = field("componentName")
    componentVersion = field("componentVersion")
    lifecycleState = field("lifecycleState")
    lifecycleStateDetails = field("lifecycleStateDetails")
    isRoot = field("isRoot")
    lastStatusChangeTimestamp = field("lastStatusChangeTimestamp")
    lastReportedTimestamp = field("lastReportedTimestamp")
    lastInstallationSource = field("lastInstallationSource")
    lifecycleStatusCodes = field("lifecycleStatusCodes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstalledComponentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstalledComponentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IoTJobAbortCriteria:
    boto3_raw_data: "type_defs.IoTJobAbortCriteriaTypeDef" = dataclasses.field()

    failureType = field("failureType")
    action = field("action")
    thresholdPercentage = field("thresholdPercentage")
    minNumberOfExecutedThings = field("minNumberOfExecutedThings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IoTJobAbortCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IoTJobAbortCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IoTJobRateIncreaseCriteria:
    boto3_raw_data: "type_defs.IoTJobRateIncreaseCriteriaTypeDef" = dataclasses.field()

    numberOfNotifiedThings = field("numberOfNotifiedThings")
    numberOfSucceededThings = field("numberOfSucceededThings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IoTJobRateIncreaseCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IoTJobRateIncreaseCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaDeviceMount:
    boto3_raw_data: "type_defs.LambdaDeviceMountTypeDef" = dataclasses.field()

    path = field("path")
    permission = field("permission")
    addGroupOwner = field("addGroupOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaDeviceMountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaDeviceMountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaVolumeMount:
    boto3_raw_data: "type_defs.LambdaVolumeMountTypeDef" = dataclasses.field()

    sourcePath = field("sourcePath")
    destinationPath = field("destinationPath")
    permission = field("permission")
    addGroupOwner = field("addGroupOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaVolumeMountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaVolumeMountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaEventSource:
    boto3_raw_data: "type_defs.LambdaEventSourceTypeDef" = dataclasses.field()

    topic = field("topic")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaEventSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaEventSourceTypeDef"]
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
class ListClientDevicesAssociatedWithCoreDeviceRequest:
    boto3_raw_data: (
        "type_defs.ListClientDevicesAssociatedWithCoreDeviceRequestTypeDef"
    ) = dataclasses.field()

    coreDeviceThingName = field("coreDeviceThingName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClientDevicesAssociatedWithCoreDeviceRequestTypeDef"
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
                "type_defs.ListClientDevicesAssociatedWithCoreDeviceRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentVersionsRequest:
    boto3_raw_data: "type_defs.ListComponentVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentVersionsRequestTypeDef"]
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

    scope = field("scope")
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
class ListCoreDevicesRequest:
    boto3_raw_data: "type_defs.ListCoreDevicesRequestTypeDef" = dataclasses.field()

    thingGroupArn = field("thingGroupArn")
    status = field("status")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    runtime = field("runtime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoreDevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreDevicesRequestTypeDef"]
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

    targetArn = field("targetArn")
    historyFilter = field("historyFilter")
    parentTargetArn = field("parentTargetArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

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
class ListEffectiveDeploymentsRequest:
    boto3_raw_data: "type_defs.ListEffectiveDeploymentsRequestTypeDef" = (
        dataclasses.field()
    )

    coreDeviceThingName = field("coreDeviceThingName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEffectiveDeploymentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEffectiveDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstalledComponentsRequest:
    boto3_raw_data: "type_defs.ListInstalledComponentsRequestTypeDef" = (
        dataclasses.field()
    )

    coreDeviceThingName = field("coreDeviceThingName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    topologyFilter = field("topologyFilter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstalledComponentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstalledComponentsRequestTypeDef"]
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
class ResolvedComponentVersion:
    boto3_raw_data: "type_defs.ResolvedComponentVersionTypeDef" = dataclasses.field()

    arn = field("arn")
    componentName = field("componentName")
    componentVersion = field("componentVersion")
    recipe = field("recipe")
    vendorGuidance = field("vendorGuidance")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolvedComponentVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolvedComponentVersionTypeDef"]
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
class BatchAssociateClientDeviceWithCoreDeviceRequest:
    boto3_raw_data: (
        "type_defs.BatchAssociateClientDeviceWithCoreDeviceRequestTypeDef"
    ) = dataclasses.field()

    coreDeviceThingName = field("coreDeviceThingName")

    @cached_property
    def entries(self):  # pragma: no cover
        return AssociateClientDeviceWithCoreDeviceEntry.make_many(
            self.boto3_raw_data["entries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateClientDeviceWithCoreDeviceRequestTypeDef"
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
                "type_defs.BatchAssociateClientDeviceWithCoreDeviceRequestTypeDef"
            ]
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

    associatedAt = field("associatedAt")

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
class BatchAssociateClientDeviceWithCoreDeviceResponse:
    boto3_raw_data: (
        "type_defs.BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return AssociateClientDeviceWithCoreDeviceErrorEntry.make_many(
            self.boto3_raw_data["errorEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef"
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
                "type_defs.BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelDeploymentResponse:
    boto3_raw_data: "type_defs.CancelDeploymentResponseTypeDef" = dataclasses.field()

    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelDeploymentResponseTypeDef"]
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

    deploymentId = field("deploymentId")
    iotJobId = field("iotJobId")
    iotJobArn = field("iotJobArn")

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
class DisassociateServiceRoleFromAccountResponse:
    boto3_raw_data: "type_defs.DisassociateServiceRoleFromAccountResponseTypeDef" = (
        dataclasses.field()
    )

    disassociatedAt = field("disassociatedAt")

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
class GetComponentResponse:
    boto3_raw_data: "type_defs.GetComponentResponseTypeDef" = dataclasses.field()

    recipeOutputFormat = field("recipeOutputFormat")
    recipe = field("recipe")
    tags = field("tags")

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
class GetComponentVersionArtifactResponse:
    boto3_raw_data: "type_defs.GetComponentVersionArtifactResponseTypeDef" = (
        dataclasses.field()
    )

    preSignedUrl = field("preSignedUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComponentVersionArtifactResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentVersionArtifactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoreDeviceResponse:
    boto3_raw_data: "type_defs.GetCoreDeviceResponseTypeDef" = dataclasses.field()

    coreDeviceThingName = field("coreDeviceThingName")
    coreVersion = field("coreVersion")
    platform = field("platform")
    architecture = field("architecture")
    runtime = field("runtime")
    status = field("status")
    lastStatusUpdateTimestamp = field("lastStatusUpdateTimestamp")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCoreDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoreDeviceResponseTypeDef"]
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

    associatedAt = field("associatedAt")
    roleArn = field("roleArn")

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
class UpdateConnectivityInfoResponse:
    boto3_raw_data: "type_defs.UpdateConnectivityInfoResponseTypeDef" = (
        dataclasses.field()
    )

    version = field("version")
    message = field("message")

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
class ListClientDevicesAssociatedWithCoreDeviceResponse:
    boto3_raw_data: (
        "type_defs.ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def associatedClientDevices(self):  # pragma: no cover
        return AssociatedClientDevice.make_many(
            self.boto3_raw_data["associatedClientDevices"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef"
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
                "type_defs.ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateClientDeviceFromCoreDeviceRequest:
    boto3_raw_data: (
        "type_defs.BatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef"
    ) = dataclasses.field()

    coreDeviceThingName = field("coreDeviceThingName")

    @cached_property
    def entries(self):  # pragma: no cover
        return DisassociateClientDeviceFromCoreDeviceEntry.make_many(
            self.boto3_raw_data["entries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef"
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
                "type_defs.BatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateClientDeviceFromCoreDeviceResponse:
    boto3_raw_data: (
        "type_defs.BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def errorEntries(self):  # pragma: no cover
        return DisassociateClientDeviceFromCoreDeviceErrorEntry.make_many(
            self.boto3_raw_data["errorEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef"
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
                "type_defs.BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentVersionResponse:
    boto3_raw_data: "type_defs.CreateComponentVersionResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    componentName = field("componentName")
    componentVersion = field("componentVersion")
    creationTimestamp = field("creationTimestamp")

    @cached_property
    def status(self):  # pragma: no cover
        return CloudComponentStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateComponentVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentLatestVersion:
    boto3_raw_data: "type_defs.ComponentLatestVersionTypeDef" = dataclasses.field()

    arn = field("arn")
    componentVersion = field("componentVersion")
    creationTimestamp = field("creationTimestamp")
    description = field("description")
    publisher = field("publisher")

    @cached_property
    def platforms(self):  # pragma: no cover
        return ComponentPlatformOutput.make_many(self.boto3_raw_data["platforms"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentLatestVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentLatestVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComponentResponse:
    boto3_raw_data: "type_defs.DescribeComponentResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    componentName = field("componentName")
    componentVersion = field("componentVersion")
    creationTimestamp = field("creationTimestamp")
    publisher = field("publisher")
    description = field("description")

    @cached_property
    def status(self):  # pragma: no cover
        return CloudComponentStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def platforms(self):  # pragma: no cover
        return ComponentPlatformOutput.make_many(self.boto3_raw_data["platforms"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeComponentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentRunWith:
    boto3_raw_data: "type_defs.ComponentRunWithTypeDef" = dataclasses.field()

    posixUser = field("posixUser")

    @cached_property
    def systemResourceLimits(self):  # pragma: no cover
        return SystemResourceLimits.make_one(
            self.boto3_raw_data["systemResourceLimits"]
        )

    windowsUser = field("windowsUser")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentRunWithTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentRunWithTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentVersionsResponse:
    boto3_raw_data: "type_defs.ListComponentVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def componentVersions(self):  # pragma: no cover
        return ComponentVersionListItem.make_many(
            self.boto3_raw_data["componentVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListComponentVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentVersionsResponseTypeDef"]
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
    def connectivityInfo(self):  # pragma: no cover
        return ConnectivityInfo.make_many(self.boto3_raw_data["connectivityInfo"])

    message = field("message")

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

    thingName = field("thingName")

    @cached_property
    def connectivityInfo(self):  # pragma: no cover
        return ConnectivityInfo.make_many(self.boto3_raw_data["connectivityInfo"])

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
class ListCoreDevicesResponse:
    boto3_raw_data: "type_defs.ListCoreDevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def coreDevices(self):  # pragma: no cover
        return CoreDevice.make_many(self.boto3_raw_data["coreDevices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoreDevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreDevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentPolicies:
    boto3_raw_data: "type_defs.DeploymentPoliciesTypeDef" = dataclasses.field()

    failureHandlingPolicy = field("failureHandlingPolicy")

    @cached_property
    def componentUpdatePolicy(self):  # pragma: no cover
        return DeploymentComponentUpdatePolicy.make_one(
            self.boto3_raw_data["componentUpdatePolicy"]
        )

    @cached_property
    def configurationValidationPolicy(self):  # pragma: no cover
        return DeploymentConfigurationValidationPolicy.make_one(
            self.boto3_raw_data["configurationValidationPolicy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentPoliciesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentPoliciesTypeDef"]
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
    def deployments(self):  # pragma: no cover
        return Deployment.make_many(self.boto3_raw_data["deployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

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
class EffectiveDeployment:
    boto3_raw_data: "type_defs.EffectiveDeploymentTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    deploymentName = field("deploymentName")
    targetArn = field("targetArn")
    coreDeviceExecutionStatus = field("coreDeviceExecutionStatus")
    creationTimestamp = field("creationTimestamp")
    modifiedTimestamp = field("modifiedTimestamp")
    iotJobId = field("iotJobId")
    iotJobArn = field("iotJobArn")
    description = field("description")
    reason = field("reason")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return EffectiveDeploymentStatusDetails.make_one(
            self.boto3_raw_data["statusDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EffectiveDeploymentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EffectiveDeploymentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstalledComponentsResponse:
    boto3_raw_data: "type_defs.ListInstalledComponentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def installedComponents(self):  # pragma: no cover
        return InstalledComponent.make_many(self.boto3_raw_data["installedComponents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstalledComponentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstalledComponentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IoTJobAbortConfigOutput:
    boto3_raw_data: "type_defs.IoTJobAbortConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def criteriaList(self):  # pragma: no cover
        return IoTJobAbortCriteria.make_many(self.boto3_raw_data["criteriaList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IoTJobAbortConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IoTJobAbortConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IoTJobAbortConfig:
    boto3_raw_data: "type_defs.IoTJobAbortConfigTypeDef" = dataclasses.field()

    @cached_property
    def criteriaList(self):  # pragma: no cover
        return IoTJobAbortCriteria.make_many(self.boto3_raw_data["criteriaList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IoTJobAbortConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IoTJobAbortConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IoTJobExponentialRolloutRate:
    boto3_raw_data: "type_defs.IoTJobExponentialRolloutRateTypeDef" = (
        dataclasses.field()
    )

    baseRatePerMinute = field("baseRatePerMinute")
    incrementFactor = field("incrementFactor")

    @cached_property
    def rateIncreaseCriteria(self):  # pragma: no cover
        return IoTJobRateIncreaseCriteria.make_one(
            self.boto3_raw_data["rateIncreaseCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IoTJobExponentialRolloutRateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IoTJobExponentialRolloutRateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaContainerParams:
    boto3_raw_data: "type_defs.LambdaContainerParamsTypeDef" = dataclasses.field()

    memorySizeInKB = field("memorySizeInKB")
    mountROSysfs = field("mountROSysfs")

    @cached_property
    def volumes(self):  # pragma: no cover
        return LambdaVolumeMount.make_many(self.boto3_raw_data["volumes"])

    @cached_property
    def devices(self):  # pragma: no cover
        return LambdaDeviceMount.make_many(self.boto3_raw_data["devices"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaContainerParamsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaContainerParamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClientDevicesAssociatedWithCoreDeviceRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListClientDevicesAssociatedWithCoreDeviceRequestPaginateTypeDef"
    ) = dataclasses.field()

    coreDeviceThingName = field("coreDeviceThingName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClientDevicesAssociatedWithCoreDeviceRequestPaginateTypeDef"
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
                "type_defs.ListClientDevicesAssociatedWithCoreDeviceRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListComponentVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComponentVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentVersionsRequestPaginateTypeDef"]
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

    scope = field("scope")

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
class ListCoreDevicesRequestPaginate:
    boto3_raw_data: "type_defs.ListCoreDevicesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    thingGroupArn = field("thingGroupArn")
    status = field("status")
    runtime = field("runtime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCoreDevicesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoreDevicesRequestPaginateTypeDef"]
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

    targetArn = field("targetArn")
    historyFilter = field("historyFilter")
    parentTargetArn = field("parentTargetArn")

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
class ListEffectiveDeploymentsRequestPaginate:
    boto3_raw_data: "type_defs.ListEffectiveDeploymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    coreDeviceThingName = field("coreDeviceThingName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEffectiveDeploymentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEffectiveDeploymentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstalledComponentsRequestPaginate:
    boto3_raw_data: "type_defs.ListInstalledComponentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    coreDeviceThingName = field("coreDeviceThingName")
    topologyFilter = field("topologyFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstalledComponentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstalledComponentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolveComponentCandidatesResponse:
    boto3_raw_data: "type_defs.ResolveComponentCandidatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resolvedComponentVersions(self):  # pragma: no cover
        return ResolvedComponentVersion.make_many(
            self.boto3_raw_data["resolvedComponentVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResolveComponentCandidatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolveComponentCandidatesResponseTypeDef"]
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
    componentName = field("componentName")

    @cached_property
    def latestVersion(self):  # pragma: no cover
        return ComponentLatestVersion.make_one(self.boto3_raw_data["latestVersion"])

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
class ResolveComponentCandidatesRequest:
    boto3_raw_data: "type_defs.ResolveComponentCandidatesRequestTypeDef" = (
        dataclasses.field()
    )

    platform = field("platform")

    @cached_property
    def componentCandidates(self):  # pragma: no cover
        return ComponentCandidate.make_many(self.boto3_raw_data["componentCandidates"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResolveComponentCandidatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolveComponentCandidatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentDeploymentSpecificationOutput:
    boto3_raw_data: "type_defs.ComponentDeploymentSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    componentVersion = field("componentVersion")

    @cached_property
    def configurationUpdate(self):  # pragma: no cover
        return ComponentConfigurationUpdateOutput.make_one(
            self.boto3_raw_data["configurationUpdate"]
        )

    @cached_property
    def runWith(self):  # pragma: no cover
        return ComponentRunWith.make_one(self.boto3_raw_data["runWith"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentDeploymentSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentDeploymentSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentDeploymentSpecification:
    boto3_raw_data: "type_defs.ComponentDeploymentSpecificationTypeDef" = (
        dataclasses.field()
    )

    componentVersion = field("componentVersion")
    configurationUpdate = field("configurationUpdate")

    @cached_property
    def runWith(self):  # pragma: no cover
        return ComponentRunWith.make_one(self.boto3_raw_data["runWith"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComponentDeploymentSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentDeploymentSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEffectiveDeploymentsResponse:
    boto3_raw_data: "type_defs.ListEffectiveDeploymentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def effectiveDeployments(self):  # pragma: no cover
        return EffectiveDeployment.make_many(
            self.boto3_raw_data["effectiveDeployments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEffectiveDeploymentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEffectiveDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IoTJobExecutionsRolloutConfig:
    boto3_raw_data: "type_defs.IoTJobExecutionsRolloutConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def exponentialRate(self):  # pragma: no cover
        return IoTJobExponentialRolloutRate.make_one(
            self.boto3_raw_data["exponentialRate"]
        )

    maximumPerMinute = field("maximumPerMinute")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IoTJobExecutionsRolloutConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IoTJobExecutionsRolloutConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaLinuxProcessParams:
    boto3_raw_data: "type_defs.LambdaLinuxProcessParamsTypeDef" = dataclasses.field()

    isolationMode = field("isolationMode")

    @cached_property
    def containerParams(self):  # pragma: no cover
        return LambdaContainerParams.make_one(self.boto3_raw_data["containerParams"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaLinuxProcessParamsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaLinuxProcessParamsTypeDef"]
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

    @cached_property
    def components(self):  # pragma: no cover
        return Component.make_many(self.boto3_raw_data["components"])

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
class DeploymentIoTJobConfigurationOutput:
    boto3_raw_data: "type_defs.DeploymentIoTJobConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def jobExecutionsRolloutConfig(self):  # pragma: no cover
        return IoTJobExecutionsRolloutConfig.make_one(
            self.boto3_raw_data["jobExecutionsRolloutConfig"]
        )

    @cached_property
    def abortConfig(self):  # pragma: no cover
        return IoTJobAbortConfigOutput.make_one(self.boto3_raw_data["abortConfig"])

    @cached_property
    def timeoutConfig(self):  # pragma: no cover
        return IoTJobTimeoutConfig.make_one(self.boto3_raw_data["timeoutConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeploymentIoTJobConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentIoTJobConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentIoTJobConfiguration:
    boto3_raw_data: "type_defs.DeploymentIoTJobConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def jobExecutionsRolloutConfig(self):  # pragma: no cover
        return IoTJobExecutionsRolloutConfig.make_one(
            self.boto3_raw_data["jobExecutionsRolloutConfig"]
        )

    @cached_property
    def abortConfig(self):  # pragma: no cover
        return IoTJobAbortConfig.make_one(self.boto3_raw_data["abortConfig"])

    @cached_property
    def timeoutConfig(self):  # pragma: no cover
        return IoTJobTimeoutConfig.make_one(self.boto3_raw_data["timeoutConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeploymentIoTJobConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentIoTJobConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaExecutionParameters:
    boto3_raw_data: "type_defs.LambdaExecutionParametersTypeDef" = dataclasses.field()

    @cached_property
    def eventSources(self):  # pragma: no cover
        return LambdaEventSource.make_many(self.boto3_raw_data["eventSources"])

    maxQueueSize = field("maxQueueSize")
    maxInstancesCount = field("maxInstancesCount")
    maxIdleTimeInSeconds = field("maxIdleTimeInSeconds")
    timeoutInSeconds = field("timeoutInSeconds")
    statusTimeoutInSeconds = field("statusTimeoutInSeconds")
    pinned = field("pinned")
    inputPayloadEncodingType = field("inputPayloadEncodingType")
    execArgs = field("execArgs")
    environmentVariables = field("environmentVariables")

    @cached_property
    def linuxProcessParams(self):  # pragma: no cover
        return LambdaLinuxProcessParams.make_one(
            self.boto3_raw_data["linuxProcessParams"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaExecutionParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaExecutionParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentResponse:
    boto3_raw_data: "type_defs.GetDeploymentResponseTypeDef" = dataclasses.field()

    targetArn = field("targetArn")
    revisionId = field("revisionId")
    deploymentId = field("deploymentId")
    deploymentName = field("deploymentName")
    deploymentStatus = field("deploymentStatus")
    iotJobId = field("iotJobId")
    iotJobArn = field("iotJobArn")
    components = field("components")

    @cached_property
    def deploymentPolicies(self):  # pragma: no cover
        return DeploymentPolicies.make_one(self.boto3_raw_data["deploymentPolicies"])

    @cached_property
    def iotJobConfiguration(self):  # pragma: no cover
        return DeploymentIoTJobConfigurationOutput.make_one(
            self.boto3_raw_data["iotJobConfiguration"]
        )

    creationTimestamp = field("creationTimestamp")
    isLatestForTarget = field("isLatestForTarget")
    parentTargetArn = field("parentTargetArn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionRecipeSource:
    boto3_raw_data: "type_defs.LambdaFunctionRecipeSourceTypeDef" = dataclasses.field()

    lambdaArn = field("lambdaArn")
    componentName = field("componentName")
    componentVersion = field("componentVersion")
    componentPlatforms = field("componentPlatforms")
    componentDependencies = field("componentDependencies")

    @cached_property
    def componentLambdaParameters(self):  # pragma: no cover
        return LambdaExecutionParameters.make_one(
            self.boto3_raw_data["componentLambdaParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionRecipeSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionRecipeSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentRequest:
    boto3_raw_data: "type_defs.CreateDeploymentRequestTypeDef" = dataclasses.field()

    targetArn = field("targetArn")
    deploymentName = field("deploymentName")
    components = field("components")
    iotJobConfiguration = field("iotJobConfiguration")

    @cached_property
    def deploymentPolicies(self):  # pragma: no cover
        return DeploymentPolicies.make_one(self.boto3_raw_data["deploymentPolicies"])

    parentTargetArn = field("parentTargetArn")
    tags = field("tags")
    clientToken = field("clientToken")

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
class CreateComponentVersionRequest:
    boto3_raw_data: "type_defs.CreateComponentVersionRequestTypeDef" = (
        dataclasses.field()
    )

    inlineRecipe = field("inlineRecipe")

    @cached_property
    def lambdaFunction(self):  # pragma: no cover
        return LambdaFunctionRecipeSource.make_one(
            self.boto3_raw_data["lambdaFunction"]
        )

    tags = field("tags")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateComponentVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
