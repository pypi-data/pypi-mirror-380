# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_inspector import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedItemDetails:
    boto3_raw_data: "type_defs.FailedItemDetailsTypeDef" = dataclasses.field()

    failureCode = field("failureCode")
    retryable = field("retryable")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailedItemDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedItemDetailsTypeDef"]
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
class AgentFilter:
    boto3_raw_data: "type_defs.AgentFilterTypeDef" = dataclasses.field()

    agentHealths = field("agentHealths")
    agentHealthCodes = field("agentHealthCodes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentPreview:
    boto3_raw_data: "type_defs.AgentPreviewTypeDef" = dataclasses.field()

    agentId = field("agentId")
    hostname = field("hostname")
    autoScalingGroup = field("autoScalingGroup")
    agentHealth = field("agentHealth")
    agentVersion = field("agentVersion")
    operatingSystem = field("operatingSystem")
    kernelVersion = field("kernelVersion")
    ipv4Address = field("ipv4Address")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentPreviewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentPreviewTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelemetryMetadata:
    boto3_raw_data: "type_defs.TelemetryMetadataTypeDef" = dataclasses.field()

    messageType = field("messageType")
    count = field("count")
    dataSize = field("dataSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TelemetryMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelemetryMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DurationRange:
    boto3_raw_data: "type_defs.DurationRangeTypeDef" = dataclasses.field()

    minSeconds = field("minSeconds")
    maxSeconds = field("maxSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DurationRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DurationRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentRunNotification:
    boto3_raw_data: "type_defs.AssessmentRunNotificationTypeDef" = dataclasses.field()

    date = field("date")
    event = field("event")
    error = field("error")
    message = field("message")
    snsTopicArn = field("snsTopicArn")
    snsPublishStatusCode = field("snsPublishStatusCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentRunNotificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentRunNotificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentRunStateChange:
    boto3_raw_data: "type_defs.AssessmentRunStateChangeTypeDef" = dataclasses.field()

    stateChangedAt = field("stateChangedAt")
    state = field("state")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentRunStateChangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentRunStateChangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentTargetFilter:
    boto3_raw_data: "type_defs.AssessmentTargetFilterTypeDef" = dataclasses.field()

    assessmentTargetNamePattern = field("assessmentTargetNamePattern")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentTargetFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentTargetFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentTarget:
    boto3_raw_data: "type_defs.AssessmentTargetTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    resourceGroupArn = field("resourceGroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentTargetTypeDef"]
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
class CreateAssessmentTargetRequest:
    boto3_raw_data: "type_defs.CreateAssessmentTargetRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentTargetName = field("assessmentTargetName")
    resourceGroupArn = field("resourceGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssessmentTargetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExclusionsPreviewRequest:
    boto3_raw_data: "type_defs.CreateExclusionsPreviewRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentTemplateArn = field("assessmentTemplateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateExclusionsPreviewRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExclusionsPreviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceGroupTag:
    boto3_raw_data: "type_defs.ResourceGroupTagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceGroupTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceGroupTagTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssessmentRunRequest:
    boto3_raw_data: "type_defs.DeleteAssessmentRunRequestTypeDef" = dataclasses.field()

    assessmentRunArn = field("assessmentRunArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssessmentRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssessmentRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssessmentTargetRequest:
    boto3_raw_data: "type_defs.DeleteAssessmentTargetRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentTargetArn = field("assessmentTargetArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAssessmentTargetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssessmentTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssessmentTemplateRequest:
    boto3_raw_data: "type_defs.DeleteAssessmentTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentTemplateArn = field("assessmentTemplateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAssessmentTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssessmentTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssessmentRunsRequest:
    boto3_raw_data: "type_defs.DescribeAssessmentRunsRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentRunArns = field("assessmentRunArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAssessmentRunsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssessmentRunsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssessmentTargetsRequest:
    boto3_raw_data: "type_defs.DescribeAssessmentTargetsRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentTargetArns = field("assessmentTargetArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAssessmentTargetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssessmentTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssessmentTemplatesRequest:
    boto3_raw_data: "type_defs.DescribeAssessmentTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentTemplateArns = field("assessmentTemplateArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssessmentTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssessmentTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExclusionsRequest:
    boto3_raw_data: "type_defs.DescribeExclusionsRequestTypeDef" = dataclasses.field()

    exclusionArns = field("exclusionArns")
    locale = field("locale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExclusionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExclusionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFindingsRequest:
    boto3_raw_data: "type_defs.DescribeFindingsRequestTypeDef" = dataclasses.field()

    findingArns = field("findingArns")
    locale = field("locale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceGroupsRequest:
    boto3_raw_data: "type_defs.DescribeResourceGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceGroupArns = field("resourceGroupArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourceGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRulesPackagesRequest:
    boto3_raw_data: "type_defs.DescribeRulesPackagesRequestTypeDef" = (
        dataclasses.field()
    )

    rulesPackageArns = field("rulesPackageArns")
    locale = field("locale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRulesPackagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRulesPackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RulesPackage:
    boto3_raw_data: "type_defs.RulesPackageTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    version = field("version")
    provider = field("provider")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RulesPackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RulesPackageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSubscription:
    boto3_raw_data: "type_defs.EventSubscriptionTypeDef" = dataclasses.field()

    event = field("event")
    subscribedAt = field("subscribedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSubscriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scope:
    boto3_raw_data: "type_defs.ScopeTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InspectorServiceAttributes:
    boto3_raw_data: "type_defs.InspectorServiceAttributesTypeDef" = dataclasses.field()

    schemaVersion = field("schemaVersion")
    assessmentRunArn = field("assessmentRunArn")
    rulesPackageArn = field("rulesPackageArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InspectorServiceAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InspectorServiceAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssessmentReportRequest:
    boto3_raw_data: "type_defs.GetAssessmentReportRequestTypeDef" = dataclasses.field()

    assessmentRunArn = field("assessmentRunArn")
    reportFileFormat = field("reportFileFormat")
    reportType = field("reportType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssessmentReportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExclusionsPreviewRequest:
    boto3_raw_data: "type_defs.GetExclusionsPreviewRequestTypeDef" = dataclasses.field()

    assessmentTemplateArn = field("assessmentTemplateArn")
    previewToken = field("previewToken")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    locale = field("locale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExclusionsPreviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExclusionsPreviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTelemetryMetadataRequest:
    boto3_raw_data: "type_defs.GetTelemetryMetadataRequestTypeDef" = dataclasses.field()

    assessmentRunArn = field("assessmentRunArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTelemetryMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTelemetryMetadataRequestTypeDef"]
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
class ListEventSubscriptionsRequest:
    boto3_raw_data: "type_defs.ListEventSubscriptionsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventSubscriptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventSubscriptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExclusionsRequest:
    boto3_raw_data: "type_defs.ListExclusionsRequestTypeDef" = dataclasses.field()

    assessmentRunArn = field("assessmentRunArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExclusionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExclusionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesPackagesRequest:
    boto3_raw_data: "type_defs.ListRulesPackagesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesPackagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesPackagesRequestTypeDef"]
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
class PrivateIp:
    boto3_raw_data: "type_defs.PrivateIpTypeDef" = dataclasses.field()

    privateDnsName = field("privateDnsName")
    privateIpAddress = field("privateIpAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrivateIpTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrivateIpTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityGroup:
    boto3_raw_data: "type_defs.SecurityGroupTypeDef" = dataclasses.field()

    groupName = field("groupName")
    groupId = field("groupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SecurityGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SecurityGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreviewAgentsRequest:
    boto3_raw_data: "type_defs.PreviewAgentsRequestTypeDef" = dataclasses.field()

    previewAgentsArn = field("previewAgentsArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PreviewAgentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreviewAgentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterCrossAccountAccessRoleRequest:
    boto3_raw_data: "type_defs.RegisterCrossAccountAccessRoleRequestTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterCrossAccountAccessRoleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterCrossAccountAccessRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAttributesFromFindingsRequest:
    boto3_raw_data: "type_defs.RemoveAttributesFromFindingsRequestTypeDef" = (
        dataclasses.field()
    )

    findingArns = field("findingArns")
    attributeKeys = field("attributeKeys")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveAttributesFromFindingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAttributesFromFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAssessmentRunRequest:
    boto3_raw_data: "type_defs.StartAssessmentRunRequestTypeDef" = dataclasses.field()

    assessmentTemplateArn = field("assessmentTemplateArn")
    assessmentRunName = field("assessmentRunName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAssessmentRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAssessmentRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopAssessmentRunRequest:
    boto3_raw_data: "type_defs.StopAssessmentRunRequestTypeDef" = dataclasses.field()

    assessmentRunArn = field("assessmentRunArn")
    stopAction = field("stopAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopAssessmentRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopAssessmentRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribeToEventRequest:
    boto3_raw_data: "type_defs.SubscribeToEventRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    event = field("event")
    topicArn = field("topicArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribeToEventRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribeToEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnsubscribeFromEventRequest:
    boto3_raw_data: "type_defs.UnsubscribeFromEventRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    event = field("event")
    topicArn = field("topicArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnsubscribeFromEventRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnsubscribeFromEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentTargetRequest:
    boto3_raw_data: "type_defs.UpdateAssessmentTargetRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentTargetArn = field("assessmentTargetArn")
    assessmentTargetName = field("assessmentTargetName")
    resourceGroupArn = field("resourceGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssessmentTargetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddAttributesToFindingsRequest:
    boto3_raw_data: "type_defs.AddAttributesToFindingsRequestTypeDef" = (
        dataclasses.field()
    )

    findingArns = field("findingArns")

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddAttributesToFindingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddAttributesToFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentTemplate:
    boto3_raw_data: "type_defs.AssessmentTemplateTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    assessmentTargetArn = field("assessmentTargetArn")
    durationInSeconds = field("durationInSeconds")
    rulesPackageArns = field("rulesPackageArns")

    @cached_property
    def userAttributesForFindings(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["userAttributesForFindings"])

    assessmentRunCount = field("assessmentRunCount")
    createdAt = field("createdAt")
    lastAssessmentRunArn = field("lastAssessmentRunArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentTemplateRequest:
    boto3_raw_data: "type_defs.CreateAssessmentTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentTargetArn = field("assessmentTargetArn")
    assessmentTemplateName = field("assessmentTemplateName")
    durationInSeconds = field("durationInSeconds")
    rulesPackageArns = field("rulesPackageArns")

    @cached_property
    def userAttributesForFindings(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["userAttributesForFindings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssessmentTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddAttributesToFindingsResponse:
    boto3_raw_data: "type_defs.AddAttributesToFindingsResponseTypeDef" = (
        dataclasses.field()
    )

    failedItems = field("failedItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddAttributesToFindingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddAttributesToFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentTargetResponse:
    boto3_raw_data: "type_defs.CreateAssessmentTargetResponseTypeDef" = (
        dataclasses.field()
    )

    assessmentTargetArn = field("assessmentTargetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssessmentTargetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentTemplateResponse:
    boto3_raw_data: "type_defs.CreateAssessmentTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    assessmentTemplateArn = field("assessmentTemplateArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssessmentTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExclusionsPreviewResponse:
    boto3_raw_data: "type_defs.CreateExclusionsPreviewResponseTypeDef" = (
        dataclasses.field()
    )

    previewToken = field("previewToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateExclusionsPreviewResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExclusionsPreviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceGroupResponse:
    boto3_raw_data: "type_defs.CreateResourceGroupResponseTypeDef" = dataclasses.field()

    resourceGroupArn = field("resourceGroupArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourceGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCrossAccountAccessRoleResponse:
    boto3_raw_data: "type_defs.DescribeCrossAccountAccessRoleResponseTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")
    valid = field("valid")
    registeredAt = field("registeredAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCrossAccountAccessRoleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCrossAccountAccessRoleResponseTypeDef"]
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
class GetAssessmentReportResponse:
    boto3_raw_data: "type_defs.GetAssessmentReportResponseTypeDef" = dataclasses.field()

    status = field("status")
    url = field("url")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssessmentReportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentRunsResponse:
    boto3_raw_data: "type_defs.ListAssessmentRunsResponseTypeDef" = dataclasses.field()

    assessmentRunArns = field("assessmentRunArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssessmentRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentTargetsResponse:
    boto3_raw_data: "type_defs.ListAssessmentTargetsResponseTypeDef" = (
        dataclasses.field()
    )

    assessmentTargetArns = field("assessmentTargetArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssessmentTargetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentTemplatesResponse:
    boto3_raw_data: "type_defs.ListAssessmentTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    assessmentTemplateArns = field("assessmentTemplateArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssessmentTemplatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExclusionsResponse:
    boto3_raw_data: "type_defs.ListExclusionsResponseTypeDef" = dataclasses.field()

    exclusionArns = field("exclusionArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExclusionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExclusionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsResponse:
    boto3_raw_data: "type_defs.ListFindingsResponseTypeDef" = dataclasses.field()

    findingArns = field("findingArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesPackagesResponse:
    boto3_raw_data: "type_defs.ListRulesPackagesResponseTypeDef" = dataclasses.field()

    rulesPackageArns = field("rulesPackageArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesPackagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesPackagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAttributesFromFindingsResponse:
    boto3_raw_data: "type_defs.RemoveAttributesFromFindingsResponseTypeDef" = (
        dataclasses.field()
    )

    failedItems = field("failedItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveAttributesFromFindingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAttributesFromFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAssessmentRunResponse:
    boto3_raw_data: "type_defs.StartAssessmentRunResponseTypeDef" = dataclasses.field()

    assessmentRunArn = field("assessmentRunArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAssessmentRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAssessmentRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentRunAgentsRequest:
    boto3_raw_data: "type_defs.ListAssessmentRunAgentsRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentRunArn = field("assessmentRunArn")

    @cached_property
    def filter(self):  # pragma: no cover
        return AgentFilter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssessmentRunAgentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentRunAgentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreviewAgentsResponse:
    boto3_raw_data: "type_defs.PreviewAgentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentPreviews(self):  # pragma: no cover
        return AgentPreview.make_many(self.boto3_raw_data["agentPreviews"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PreviewAgentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreviewAgentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentRunAgent:
    boto3_raw_data: "type_defs.AssessmentRunAgentTypeDef" = dataclasses.field()

    agentId = field("agentId")
    assessmentRunArn = field("assessmentRunArn")
    agentHealth = field("agentHealth")
    agentHealthCode = field("agentHealthCode")

    @cached_property
    def telemetryMetadata(self):  # pragma: no cover
        return TelemetryMetadata.make_many(self.boto3_raw_data["telemetryMetadata"])

    agentHealthDetails = field("agentHealthDetails")
    autoScalingGroup = field("autoScalingGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentRunAgentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentRunAgentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTelemetryMetadataResponse:
    boto3_raw_data: "type_defs.GetTelemetryMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def telemetryMetadata(self):  # pragma: no cover
        return TelemetryMetadata.make_many(self.boto3_raw_data["telemetryMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTelemetryMetadataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTelemetryMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentTemplateFilter:
    boto3_raw_data: "type_defs.AssessmentTemplateFilterTypeDef" = dataclasses.field()

    namePattern = field("namePattern")

    @cached_property
    def durationRange(self):  # pragma: no cover
        return DurationRange.make_one(self.boto3_raw_data["durationRange"])

    rulesPackageArns = field("rulesPackageArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentTemplateFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentTemplateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentRun:
    boto3_raw_data: "type_defs.AssessmentRunTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    assessmentTemplateArn = field("assessmentTemplateArn")
    state = field("state")
    durationInSeconds = field("durationInSeconds")
    rulesPackageArns = field("rulesPackageArns")

    @cached_property
    def userAttributesForFindings(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["userAttributesForFindings"])

    createdAt = field("createdAt")
    stateChangedAt = field("stateChangedAt")
    dataCollected = field("dataCollected")

    @cached_property
    def stateChanges(self):  # pragma: no cover
        return AssessmentRunStateChange.make_many(self.boto3_raw_data["stateChanges"])

    @cached_property
    def notifications(self):  # pragma: no cover
        return AssessmentRunNotification.make_many(self.boto3_raw_data["notifications"])

    findingCounts = field("findingCounts")
    startedAt = field("startedAt")
    completedAt = field("completedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentRunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssessmentRunTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentTargetsRequest:
    boto3_raw_data: "type_defs.ListAssessmentTargetsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return AssessmentTargetFilter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssessmentTargetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssessmentTargetsResponse:
    boto3_raw_data: "type_defs.DescribeAssessmentTargetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessmentTargets(self):  # pragma: no cover
        return AssessmentTarget.make_many(self.boto3_raw_data["assessmentTargets"])

    failedItems = field("failedItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssessmentTargetsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssessmentTargetsResponseTypeDef"]
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

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class SetTagsForResourceRequest:
    boto3_raw_data: "type_defs.SetTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceGroupRequest:
    boto3_raw_data: "type_defs.CreateResourceGroupRequestTypeDef" = dataclasses.field()

    @cached_property
    def resourceGroupTags(self):  # pragma: no cover
        return ResourceGroupTag.make_many(self.boto3_raw_data["resourceGroupTags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourceGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceGroup:
    boto3_raw_data: "type_defs.ResourceGroupTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def tags(self):  # pragma: no cover
        return ResourceGroupTag.make_many(self.boto3_raw_data["tags"])

    createdAt = field("createdAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRulesPackagesResponse:
    boto3_raw_data: "type_defs.DescribeRulesPackagesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def rulesPackages(self):  # pragma: no cover
        return RulesPackage.make_many(self.boto3_raw_data["rulesPackages"])

    failedItems = field("failedItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRulesPackagesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRulesPackagesResponseTypeDef"]
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

    resourceArn = field("resourceArn")
    topicArn = field("topicArn")

    @cached_property
    def eventSubscriptions(self):  # pragma: no cover
        return EventSubscription.make_many(self.boto3_raw_data["eventSubscriptions"])

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
class ExclusionPreview:
    boto3_raw_data: "type_defs.ExclusionPreviewTypeDef" = dataclasses.field()

    title = field("title")
    description = field("description")
    recommendation = field("recommendation")

    @cached_property
    def scopes(self):  # pragma: no cover
        return Scope.make_many(self.boto3_raw_data["scopes"])

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExclusionPreviewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExclusionPreviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Exclusion:
    boto3_raw_data: "type_defs.ExclusionTypeDef" = dataclasses.field()

    arn = field("arn")
    title = field("title")
    description = field("description")
    recommendation = field("recommendation")

    @cached_property
    def scopes(self):  # pragma: no cover
        return Scope.make_many(self.boto3_raw_data["scopes"])

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExclusionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExclusionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentRunAgentsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssessmentRunAgentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assessmentRunArn = field("assessmentRunArn")

    @cached_property
    def filter(self):  # pragma: no cover
        return AgentFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssessmentRunAgentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentRunAgentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentTargetsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssessmentTargetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return AssessmentTargetFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssessmentTargetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentTargetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventSubscriptionsRequestPaginate:
    boto3_raw_data: "type_defs.ListEventSubscriptionsRequestPaginateTypeDef" = (
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
            "type_defs.ListEventSubscriptionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventSubscriptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExclusionsRequestPaginate:
    boto3_raw_data: "type_defs.ListExclusionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assessmentRunArn = field("assessmentRunArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExclusionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExclusionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesPackagesRequestPaginate:
    boto3_raw_data: "type_defs.ListRulesPackagesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRulesPackagesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesPackagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreviewAgentsRequestPaginate:
    boto3_raw_data: "type_defs.PreviewAgentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    previewAgentsArn = field("previewAgentsArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PreviewAgentsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreviewAgentsRequestPaginateTypeDef"]
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

    networkInterfaceId = field("networkInterfaceId")
    subnetId = field("subnetId")
    vpcId = field("vpcId")
    privateDnsName = field("privateDnsName")
    privateIpAddress = field("privateIpAddress")

    @cached_property
    def privateIpAddresses(self):  # pragma: no cover
        return PrivateIp.make_many(self.boto3_raw_data["privateIpAddresses"])

    publicDnsName = field("publicDnsName")
    publicIp = field("publicIp")
    ipv6Addresses = field("ipv6Addresses")

    @cached_property
    def securityGroups(self):  # pragma: no cover
        return SecurityGroup.make_many(self.boto3_raw_data["securityGroups"])

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
class TimestampRange:
    boto3_raw_data: "type_defs.TimestampRangeTypeDef" = dataclasses.field()

    beginDate = field("beginDate")
    endDate = field("endDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimestampRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimestampRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssessmentTemplatesResponse:
    boto3_raw_data: "type_defs.DescribeAssessmentTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessmentTemplates(self):  # pragma: no cover
        return AssessmentTemplate.make_many(self.boto3_raw_data["assessmentTemplates"])

    failedItems = field("failedItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssessmentTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssessmentTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentRunAgentsResponse:
    boto3_raw_data: "type_defs.ListAssessmentRunAgentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessmentRunAgents(self):  # pragma: no cover
        return AssessmentRunAgent.make_many(self.boto3_raw_data["assessmentRunAgents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssessmentRunAgentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentRunAgentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListAssessmentTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assessmentTargetArns = field("assessmentTargetArns")

    @cached_property
    def filter(self):  # pragma: no cover
        return AssessmentTemplateFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssessmentTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentTemplatesRequest:
    boto3_raw_data: "type_defs.ListAssessmentTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentTargetArns = field("assessmentTargetArns")

    @cached_property
    def filter(self):  # pragma: no cover
        return AssessmentTemplateFilter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssessmentTemplatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssessmentRunsResponse:
    boto3_raw_data: "type_defs.DescribeAssessmentRunsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessmentRuns(self):  # pragma: no cover
        return AssessmentRun.make_many(self.boto3_raw_data["assessmentRuns"])

    failedItems = field("failedItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAssessmentRunsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssessmentRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceGroupsResponse:
    boto3_raw_data: "type_defs.DescribeResourceGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resourceGroups(self):  # pragma: no cover
        return ResourceGroup.make_many(self.boto3_raw_data["resourceGroups"])

    failedItems = field("failedItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourceGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventSubscriptionsResponse:
    boto3_raw_data: "type_defs.ListEventSubscriptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def subscriptions(self):  # pragma: no cover
        return Subscription.make_many(self.boto3_raw_data["subscriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventSubscriptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventSubscriptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExclusionsPreviewResponse:
    boto3_raw_data: "type_defs.GetExclusionsPreviewResponseTypeDef" = (
        dataclasses.field()
    )

    previewStatus = field("previewStatus")

    @cached_property
    def exclusionPreviews(self):  # pragma: no cover
        return ExclusionPreview.make_many(self.boto3_raw_data["exclusionPreviews"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExclusionsPreviewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExclusionsPreviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExclusionsResponse:
    boto3_raw_data: "type_defs.DescribeExclusionsResponseTypeDef" = dataclasses.field()

    exclusions = field("exclusions")
    failedItems = field("failedItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExclusionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExclusionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetAttributes:
    boto3_raw_data: "type_defs.AssetAttributesTypeDef" = dataclasses.field()

    schemaVersion = field("schemaVersion")
    agentId = field("agentId")
    autoScalingGroup = field("autoScalingGroup")
    amiId = field("amiId")
    hostname = field("hostname")
    ipv4Addresses = field("ipv4Addresses")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentRunFilter:
    boto3_raw_data: "type_defs.AssessmentRunFilterTypeDef" = dataclasses.field()

    namePattern = field("namePattern")
    states = field("states")

    @cached_property
    def durationRange(self):  # pragma: no cover
        return DurationRange.make_one(self.boto3_raw_data["durationRange"])

    rulesPackageArns = field("rulesPackageArns")

    @cached_property
    def startTimeRange(self):  # pragma: no cover
        return TimestampRange.make_one(self.boto3_raw_data["startTimeRange"])

    @cached_property
    def completionTimeRange(self):  # pragma: no cover
        return TimestampRange.make_one(self.boto3_raw_data["completionTimeRange"])

    @cached_property
    def stateChangeTimeRange(self):  # pragma: no cover
        return TimestampRange.make_one(self.boto3_raw_data["stateChangeTimeRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentRunFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentRunFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingFilter:
    boto3_raw_data: "type_defs.FindingFilterTypeDef" = dataclasses.field()

    agentIds = field("agentIds")
    autoScalingGroups = field("autoScalingGroups")
    ruleNames = field("ruleNames")
    severities = field("severities")
    rulesPackageArns = field("rulesPackageArns")

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @cached_property
    def userAttributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["userAttributes"])

    @cached_property
    def creationTimeRange(self):  # pragma: no cover
        return TimestampRange.make_one(self.boto3_raw_data["creationTimeRange"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Finding:
    boto3_raw_data: "type_defs.FindingTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @cached_property
    def userAttributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["userAttributes"])

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    schemaVersion = field("schemaVersion")
    service = field("service")

    @cached_property
    def serviceAttributes(self):  # pragma: no cover
        return InspectorServiceAttributes.make_one(
            self.boto3_raw_data["serviceAttributes"]
        )

    assetType = field("assetType")

    @cached_property
    def assetAttributes(self):  # pragma: no cover
        return AssetAttributes.make_one(self.boto3_raw_data["assetAttributes"])

    id = field("id")
    title = field("title")
    description = field("description")
    recommendation = field("recommendation")
    severity = field("severity")
    numericSeverity = field("numericSeverity")
    confidence = field("confidence")
    indicatorOfCompromise = field("indicatorOfCompromise")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentRunsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssessmentRunsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assessmentTemplateArns = field("assessmentTemplateArns")

    @cached_property
    def filter(self):  # pragma: no cover
        return AssessmentRunFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssessmentRunsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentRunsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentRunsRequest:
    boto3_raw_data: "type_defs.ListAssessmentRunsRequestTypeDef" = dataclasses.field()

    assessmentTemplateArns = field("assessmentTemplateArns")

    @cached_property
    def filter(self):  # pragma: no cover
        return AssessmentRunFilter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssessmentRunsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentRunsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsRequestPaginate:
    boto3_raw_data: "type_defs.ListFindingsRequestPaginateTypeDef" = dataclasses.field()

    assessmentRunArns = field("assessmentRunArns")

    @cached_property
    def filter(self):  # pragma: no cover
        return FindingFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsRequest:
    boto3_raw_data: "type_defs.ListFindingsRequestTypeDef" = dataclasses.field()

    assessmentRunArns = field("assessmentRunArns")

    @cached_property
    def filter(self):  # pragma: no cover
        return FindingFilter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFindingsResponse:
    boto3_raw_data: "type_defs.DescribeFindingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def findings(self):  # pragma: no cover
        return Finding.make_many(self.boto3_raw_data["findings"])

    failedItems = field("failedItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFindingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
