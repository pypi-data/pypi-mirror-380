# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_qconnect import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AIAgentConfigurationData:
    boto3_raw_data: "type_defs.AIAgentConfigurationDataTypeDef" = dataclasses.field()

    aiAgentId = field("aiAgentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AIAgentConfigurationDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIAgentConfigurationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentFilterConfig:
    boto3_raw_data: "type_defs.GuardrailContentFilterConfigTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    inputStrength = field("inputStrength")
    outputStrength = field("outputStrength")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailContentFilterConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentFilterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContextualGroundingFilterConfig:
    boto3_raw_data: "type_defs.GuardrailContextualGroundingFilterConfigTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    threshold = field("threshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailContextualGroundingFilterConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContextualGroundingFilterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailPiiEntityConfig:
    boto3_raw_data: "type_defs.GuardrailPiiEntityConfigTypeDef" = dataclasses.field()

    type = field("type")
    action = field("action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailPiiEntityConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailPiiEntityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailRegexConfig:
    boto3_raw_data: "type_defs.GuardrailRegexConfigTypeDef" = dataclasses.field()

    name = field("name")
    pattern = field("pattern")
    action = field("action")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailRegexConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailRegexConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailSummary:
    boto3_raw_data: "type_defs.AIGuardrailSummaryTypeDef" = dataclasses.field()

    name = field("name")
    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    aiGuardrailId = field("aiGuardrailId")
    aiGuardrailArn = field("aiGuardrailArn")
    visibilityStatus = field("visibilityStatus")
    modifiedTime = field("modifiedTime")
    description = field("description")
    status = field("status")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AIGuardrailSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopicConfigOutput:
    boto3_raw_data: "type_defs.GuardrailTopicConfigOutputTypeDef" = dataclasses.field()

    name = field("name")
    definition = field("definition")
    type = field("type")
    examples = field("examples")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailTopicConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTopicConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopicConfig:
    boto3_raw_data: "type_defs.GuardrailTopicConfigTypeDef" = dataclasses.field()

    name = field("name")
    definition = field("definition")
    type = field("type")
    examples = field("examples")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailTopicConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTopicConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailManagedWordsConfig:
    boto3_raw_data: "type_defs.GuardrailManagedWordsConfigTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailManagedWordsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailManagedWordsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailWordConfig:
    boto3_raw_data: "type_defs.GuardrailWordConfigTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailWordConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailWordConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIPromptSummary:
    boto3_raw_data: "type_defs.AIPromptSummaryTypeDef" = dataclasses.field()

    name = field("name")
    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    aiPromptId = field("aiPromptId")
    type = field("type")
    aiPromptArn = field("aiPromptArn")
    templateType = field("templateType")
    modelId = field("modelId")
    apiFormat = field("apiFormat")
    visibilityStatus = field("visibilityStatus")
    modifiedTime = field("modifiedTime")
    origin = field("origin")
    description = field("description")
    status = field("status")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AIPromptSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AIPromptSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextFullAIPromptEditTemplateConfiguration:
    boto3_raw_data: "type_defs.TextFullAIPromptEditTemplateConfigurationTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TextFullAIPromptEditTemplateConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextFullAIPromptEditTemplateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateMessageTemplateRequest:
    boto3_raw_data: "type_defs.ActivateMessageTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")
    versionNumber = field("versionNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActivateMessageTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateMessageTemplateRequestTypeDef"]
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
class AgentAttributes:
    boto3_raw_data: "type_defs.AgentAttributesTypeDef" = dataclasses.field()

    firstName = field("firstName")
    lastName = field("lastName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonConnectGuideAssociationData:
    boto3_raw_data: "type_defs.AmazonConnectGuideAssociationDataTypeDef" = (
        dataclasses.field()
    )

    flowId = field("flowId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonConnectGuideAssociationDataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonConnectGuideAssociationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppIntegrationsConfigurationOutput:
    boto3_raw_data: "type_defs.AppIntegrationsConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    appIntegrationArn = field("appIntegrationArn")
    objectFields = field("objectFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AppIntegrationsConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppIntegrationsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppIntegrationsConfiguration:
    boto3_raw_data: "type_defs.AppIntegrationsConfigurationTypeDef" = (
        dataclasses.field()
    )

    appIntegrationArn = field("appIntegrationArn")
    objectFields = field("objectFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppIntegrationsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppIntegrationsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssistantAssociationInputData:
    boto3_raw_data: "type_defs.AssistantAssociationInputDataTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssistantAssociationInputDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssistantAssociationInputDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseAssociationData:
    boto3_raw_data: "type_defs.KnowledgeBaseAssociationDataTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    knowledgeBaseArn = field("knowledgeBaseArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseAssociationDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseAssociationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssistantCapabilityConfiguration:
    boto3_raw_data: "type_defs.AssistantCapabilityConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssistantCapabilityConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssistantCapabilityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssistantIntegrationConfiguration:
    boto3_raw_data: "type_defs.AssistantIntegrationConfigurationTypeDef" = (
        dataclasses.field()
    )

    topicIntegrationArn = field("topicIntegrationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssistantIntegrationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssistantIntegrationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionConfiguration:
    boto3_raw_data: "type_defs.ServerSideEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerSideEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParsingPrompt:
    boto3_raw_data: "type_defs.ParsingPromptTypeDef" = dataclasses.field()

    parsingPromptText = field("parsingPromptText")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParsingPromptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParsingPromptTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FixedSizeChunkingConfiguration:
    boto3_raw_data: "type_defs.FixedSizeChunkingConfigurationTypeDef" = (
        dataclasses.field()
    )

    maxTokens = field("maxTokens")
    overlapPercentage = field("overlapPercentage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FixedSizeChunkingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FixedSizeChunkingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemanticChunkingConfiguration:
    boto3_raw_data: "type_defs.SemanticChunkingConfigurationTypeDef" = (
        dataclasses.field()
    )

    maxTokens = field("maxTokens")
    bufferSize = field("bufferSize")
    breakpointPercentileThreshold = field("breakpointPercentileThreshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SemanticChunkingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SemanticChunkingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationSpan:
    boto3_raw_data: "type_defs.CitationSpanTypeDef" = dataclasses.field()

    beginOffsetInclusive = field("beginOffsetInclusive")
    endOffsetExclusive = field("endOffsetExclusive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CitationSpanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CitationSpanTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectConfiguration:
    boto3_raw_data: "type_defs.ConnectConfigurationTypeDef" = dataclasses.field()

    instanceId = field("instanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RankingData:
    boto3_raw_data: "type_defs.RankingDataTypeDef" = dataclasses.field()

    relevanceScore = field("relevanceScore")
    relevanceLevel = field("relevanceLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RankingDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RankingDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentData:
    boto3_raw_data: "type_defs.ContentDataTypeDef" = dataclasses.field()

    contentArn = field("contentArn")
    contentId = field("contentId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    revisionId = field("revisionId")
    title = field("title")
    contentType = field("contentType")
    status = field("status")
    metadata = field("metadata")
    url = field("url")
    urlExpiry = field("urlExpiry")
    tags = field("tags")
    linkOutUri = field("linkOutUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerativeContentFeedbackData:
    boto3_raw_data: "type_defs.GenerativeContentFeedbackDataTypeDef" = (
        dataclasses.field()
    )

    relevance = field("relevance")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerativeContentFeedbackDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerativeContentFeedbackDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentReference:
    boto3_raw_data: "type_defs.ContentReferenceTypeDef" = dataclasses.field()

    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    contentArn = field("contentArn")
    contentId = field("contentId")
    sourceURL = field("sourceURL")
    referenceType = field("referenceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentSummary:
    boto3_raw_data: "type_defs.ContentSummaryTypeDef" = dataclasses.field()

    contentArn = field("contentArn")
    contentId = field("contentId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    revisionId = field("revisionId")
    title = field("title")
    contentType = field("contentType")
    status = field("status")
    metadata = field("metadata")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfServiceConversationHistory:
    boto3_raw_data: "type_defs.SelfServiceConversationHistoryTypeDef" = (
        dataclasses.field()
    )

    turnNumber = field("turnNumber")
    inputTranscript = field("inputTranscript")
    botResponse = field("botResponse")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SelfServiceConversationHistoryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfServiceConversationHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationState:
    boto3_raw_data: "type_defs.ConversationStateTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConversationStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContentRequest:
    boto3_raw_data: "type_defs.CreateContentRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    uploadId = field("uploadId")
    title = field("title")
    overrideLinkOutUri = field("overrideLinkOutUri")
    metadata = field("metadata")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenderingConfiguration:
    boto3_raw_data: "type_defs.RenderingConfigurationTypeDef" = dataclasses.field()

    templateUri = field("templateUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RenderingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenderingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMessageTemplateAttachmentRequest:
    boto3_raw_data: "type_defs.CreateMessageTemplateAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")
    contentDisposition = field("contentDisposition")
    name = field("name")
    body = field("body")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMessageTemplateAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMessageTemplateAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateAttachment:
    boto3_raw_data: "type_defs.MessageTemplateAttachmentTypeDef" = dataclasses.field()

    contentDisposition = field("contentDisposition")
    name = field("name")
    uploadedTime = field("uploadedTime")
    url = field("url")
    urlExpiry = field("urlExpiry")
    attachmentId = field("attachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageTemplateAttachmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMessageTemplateVersionRequest:
    boto3_raw_data: "type_defs.CreateMessageTemplateVersionRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")
    messageTemplateContentSha256 = field("messageTemplateContentSha256")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMessageTemplateVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMessageTemplateVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseDataProvider:
    boto3_raw_data: "type_defs.QuickResponseDataProviderTypeDef" = dataclasses.field()

    content = field("content")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickResponseDataProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseDataProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerProfileAttributesOutput:
    boto3_raw_data: "type_defs.CustomerProfileAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    profileId = field("profileId")
    profileARN = field("profileARN")
    firstName = field("firstName")
    middleName = field("middleName")
    lastName = field("lastName")
    accountNumber = field("accountNumber")
    emailAddress = field("emailAddress")
    phoneNumber = field("phoneNumber")
    additionalInformation = field("additionalInformation")
    partyType = field("partyType")
    businessName = field("businessName")
    birthDate = field("birthDate")
    gender = field("gender")
    mobilePhoneNumber = field("mobilePhoneNumber")
    homePhoneNumber = field("homePhoneNumber")
    businessPhoneNumber = field("businessPhoneNumber")
    businessEmailAddress = field("businessEmailAddress")
    address1 = field("address1")
    address2 = field("address2")
    address3 = field("address3")
    address4 = field("address4")
    city = field("city")
    county = field("county")
    country = field("country")
    postalCode = field("postalCode")
    province = field("province")
    state = field("state")
    shippingAddress1 = field("shippingAddress1")
    shippingAddress2 = field("shippingAddress2")
    shippingAddress3 = field("shippingAddress3")
    shippingAddress4 = field("shippingAddress4")
    shippingCity = field("shippingCity")
    shippingCounty = field("shippingCounty")
    shippingCountry = field("shippingCountry")
    shippingPostalCode = field("shippingPostalCode")
    shippingProvince = field("shippingProvince")
    shippingState = field("shippingState")
    mailingAddress1 = field("mailingAddress1")
    mailingAddress2 = field("mailingAddress2")
    mailingAddress3 = field("mailingAddress3")
    mailingAddress4 = field("mailingAddress4")
    mailingCity = field("mailingCity")
    mailingCounty = field("mailingCounty")
    mailingCountry = field("mailingCountry")
    mailingPostalCode = field("mailingPostalCode")
    mailingProvince = field("mailingProvince")
    mailingState = field("mailingState")
    billingAddress1 = field("billingAddress1")
    billingAddress2 = field("billingAddress2")
    billingAddress3 = field("billingAddress3")
    billingAddress4 = field("billingAddress4")
    billingCity = field("billingCity")
    billingCounty = field("billingCounty")
    billingCountry = field("billingCountry")
    billingPostalCode = field("billingPostalCode")
    billingProvince = field("billingProvince")
    billingState = field("billingState")
    custom = field("custom")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomerProfileAttributesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerProfileAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerProfileAttributes:
    boto3_raw_data: "type_defs.CustomerProfileAttributesTypeDef" = dataclasses.field()

    profileId = field("profileId")
    profileARN = field("profileARN")
    firstName = field("firstName")
    middleName = field("middleName")
    lastName = field("lastName")
    accountNumber = field("accountNumber")
    emailAddress = field("emailAddress")
    phoneNumber = field("phoneNumber")
    additionalInformation = field("additionalInformation")
    partyType = field("partyType")
    businessName = field("businessName")
    birthDate = field("birthDate")
    gender = field("gender")
    mobilePhoneNumber = field("mobilePhoneNumber")
    homePhoneNumber = field("homePhoneNumber")
    businessPhoneNumber = field("businessPhoneNumber")
    businessEmailAddress = field("businessEmailAddress")
    address1 = field("address1")
    address2 = field("address2")
    address3 = field("address3")
    address4 = field("address4")
    city = field("city")
    county = field("county")
    country = field("country")
    postalCode = field("postalCode")
    province = field("province")
    state = field("state")
    shippingAddress1 = field("shippingAddress1")
    shippingAddress2 = field("shippingAddress2")
    shippingAddress3 = field("shippingAddress3")
    shippingAddress4 = field("shippingAddress4")
    shippingCity = field("shippingCity")
    shippingCounty = field("shippingCounty")
    shippingCountry = field("shippingCountry")
    shippingPostalCode = field("shippingPostalCode")
    shippingProvince = field("shippingProvince")
    shippingState = field("shippingState")
    mailingAddress1 = field("mailingAddress1")
    mailingAddress2 = field("mailingAddress2")
    mailingAddress3 = field("mailingAddress3")
    mailingAddress4 = field("mailingAddress4")
    mailingCity = field("mailingCity")
    mailingCounty = field("mailingCounty")
    mailingCountry = field("mailingCountry")
    mailingPostalCode = field("mailingPostalCode")
    mailingProvince = field("mailingProvince")
    mailingState = field("mailingState")
    billingAddress1 = field("billingAddress1")
    billingAddress2 = field("billingAddress2")
    billingAddress3 = field("billingAddress3")
    billingAddress4 = field("billingAddress4")
    billingCity = field("billingCity")
    billingCounty = field("billingCounty")
    billingCountry = field("billingCountry")
    billingPostalCode = field("billingPostalCode")
    billingProvince = field("billingProvince")
    billingState = field("billingState")
    custom = field("custom")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomerProfileAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerProfileAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerativeChunkDataDetailsPaginator:
    boto3_raw_data: "type_defs.GenerativeChunkDataDetailsPaginatorTypeDef" = (
        dataclasses.field()
    )

    completion = field("completion")
    references = field("references")
    nextChunkToken = field("nextChunkToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerativeChunkDataDetailsPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerativeChunkDataDetailsPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentDetectedDataDetails:
    boto3_raw_data: "type_defs.IntentDetectedDataDetailsTypeDef" = dataclasses.field()

    intent = field("intent")
    intentId = field("intentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntentDetectedDataDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentDetectedDataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerativeChunkDataDetails:
    boto3_raw_data: "type_defs.GenerativeChunkDataDetailsTypeDef" = dataclasses.field()

    completion = field("completion")
    references = field("references")
    nextChunkToken = field("nextChunkToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerativeChunkDataDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerativeChunkDataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerativeReference:
    boto3_raw_data: "type_defs.GenerativeReferenceTypeDef" = dataclasses.field()

    modelId = field("modelId")
    generationId = field("generationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerativeReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerativeReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateMessageTemplateRequest:
    boto3_raw_data: "type_defs.DeactivateMessageTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")
    versionNumber = field("versionNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeactivateMessageTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateMessageTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAIAgentRequest:
    boto3_raw_data: "type_defs.DeleteAIAgentRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiAgentId = field("aiAgentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAIAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAIAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAIAgentVersionRequest:
    boto3_raw_data: "type_defs.DeleteAIAgentVersionRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiAgentId = field("aiAgentId")
    versionNumber = field("versionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAIAgentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAIAgentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAIGuardrailRequest:
    boto3_raw_data: "type_defs.DeleteAIGuardrailRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiGuardrailId = field("aiGuardrailId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAIGuardrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAIGuardrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAIGuardrailVersionRequest:
    boto3_raw_data: "type_defs.DeleteAIGuardrailVersionRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiGuardrailId = field("aiGuardrailId")
    versionNumber = field("versionNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAIGuardrailVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAIGuardrailVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAIPromptRequest:
    boto3_raw_data: "type_defs.DeleteAIPromptRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiPromptId = field("aiPromptId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAIPromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAIPromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAIPromptVersionRequest:
    boto3_raw_data: "type_defs.DeleteAIPromptVersionRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiPromptId = field("aiPromptId")
    versionNumber = field("versionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAIPromptVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAIPromptVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssistantAssociationRequest:
    boto3_raw_data: "type_defs.DeleteAssistantAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    assistantAssociationId = field("assistantAssociationId")
    assistantId = field("assistantId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAssistantAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssistantAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssistantRequest:
    boto3_raw_data: "type_defs.DeleteAssistantRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssistantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssistantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContentAssociationRequest:
    boto3_raw_data: "type_defs.DeleteContentAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    contentId = field("contentId")
    contentAssociationId = field("contentAssociationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteContentAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContentAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContentRequest:
    boto3_raw_data: "type_defs.DeleteContentRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    contentId = field("contentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImportJobRequest:
    boto3_raw_data: "type_defs.DeleteImportJobRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    importJobId = field("importJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.DeleteKnowledgeBaseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKnowledgeBaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMessageTemplateAttachmentRequest:
    boto3_raw_data: "type_defs.DeleteMessageTemplateAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")
    attachmentId = field("attachmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMessageTemplateAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMessageTemplateAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMessageTemplateRequest:
    boto3_raw_data: "type_defs.DeleteMessageTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMessageTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMessageTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQuickResponseRequest:
    boto3_raw_data: "type_defs.DeleteQuickResponseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    quickResponseId = field("quickResponseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteQuickResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQuickResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Highlight:
    boto3_raw_data: "type_defs.HighlightTypeDef" = dataclasses.field()

    beginOffsetInclusive = field("beginOffsetInclusive")
    endOffsetExclusive = field("endOffsetExclusive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HighlightTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HighlightTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailHeader:
    boto3_raw_data: "type_defs.EmailHeaderTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailHeaderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateBodyContentProvider:
    boto3_raw_data: "type_defs.MessageTemplateBodyContentProviderTypeDef" = (
        dataclasses.field()
    )

    content = field("content")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MessageTemplateBodyContentProviderTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateBodyContentProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupingConfigurationOutput:
    boto3_raw_data: "type_defs.GroupingConfigurationOutputTypeDef" = dataclasses.field()

    criteria = field("criteria")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GroupingConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupingConfigurationOutputTypeDef"]
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

    field = field("field")
    operator = field("operator")
    value = field("value")

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
class GetAIAgentRequest:
    boto3_raw_data: "type_defs.GetAIAgentRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiAgentId = field("aiAgentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAIAgentRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAIAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAIGuardrailRequest:
    boto3_raw_data: "type_defs.GetAIGuardrailRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiGuardrailId = field("aiGuardrailId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAIGuardrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAIGuardrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAIPromptRequest:
    boto3_raw_data: "type_defs.GetAIPromptRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiPromptId = field("aiPromptId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAIPromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAIPromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssistantAssociationRequest:
    boto3_raw_data: "type_defs.GetAssistantAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    assistantAssociationId = field("assistantAssociationId")
    assistantId = field("assistantId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAssistantAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssistantAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssistantRequest:
    boto3_raw_data: "type_defs.GetAssistantRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssistantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssistantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContentAssociationRequest:
    boto3_raw_data: "type_defs.GetContentAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    contentId = field("contentId")
    contentAssociationId = field("contentAssociationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContentAssociationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContentAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContentRequest:
    boto3_raw_data: "type_defs.GetContentRequestTypeDef" = dataclasses.field()

    contentId = field("contentId")
    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetContentRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContentSummaryRequest:
    boto3_raw_data: "type_defs.GetContentSummaryRequestTypeDef" = dataclasses.field()

    contentId = field("contentId")
    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContentSummaryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContentSummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportJobRequest:
    boto3_raw_data: "type_defs.GetImportJobRequestTypeDef" = dataclasses.field()

    importJobId = field("importJobId")
    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.GetKnowledgeBaseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKnowledgeBaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMessageTemplateRequest:
    boto3_raw_data: "type_defs.GetMessageTemplateRequestTypeDef" = dataclasses.field()

    messageTemplateId = field("messageTemplateId")
    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMessageTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMessageTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNextMessageRequest:
    boto3_raw_data: "type_defs.GetNextMessageRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    sessionId = field("sessionId")
    nextMessageToken = field("nextMessageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNextMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNextMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQuickResponseRequest:
    boto3_raw_data: "type_defs.GetQuickResponseRequestTypeDef" = dataclasses.field()

    quickResponseId = field("quickResponseId")
    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQuickResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQuickResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationsRequest:
    boto3_raw_data: "type_defs.GetRecommendationsRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    sessionId = field("sessionId")
    maxResults = field("maxResults")
    waitTimeSeconds = field("waitTimeSeconds")
    nextChunkToken = field("nextChunkToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionRequest:
    boto3_raw_data: "type_defs.GetSessionRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSessionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupingConfiguration:
    boto3_raw_data: "type_defs.GroupingConfigurationTypeDef" = dataclasses.field()

    criteria = field("criteria")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GroupingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchicalChunkingLevelConfiguration:
    boto3_raw_data: "type_defs.HierarchicalChunkingLevelConfigurationTypeDef" = (
        dataclasses.field()
    )

    maxTokens = field("maxTokens")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HierarchicalChunkingLevelConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchicalChunkingLevelConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentInputData:
    boto3_raw_data: "type_defs.IntentInputDataTypeDef" = dataclasses.field()

    intentId = field("intentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentInputDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntentInputDataTypeDef"]],
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
class ListAIAgentVersionsRequest:
    boto3_raw_data: "type_defs.ListAIAgentVersionsRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiAgentId = field("aiAgentId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    origin = field("origin")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIAgentVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIAgentVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIAgentsRequest:
    boto3_raw_data: "type_defs.ListAIAgentsRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    origin = field("origin")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIAgentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIAgentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIGuardrailVersionsRequest:
    boto3_raw_data: "type_defs.ListAIGuardrailVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiGuardrailId = field("aiGuardrailId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAIGuardrailVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIGuardrailVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIGuardrailsRequest:
    boto3_raw_data: "type_defs.ListAIGuardrailsRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIGuardrailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIGuardrailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIPromptVersionsRequest:
    boto3_raw_data: "type_defs.ListAIPromptVersionsRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiPromptId = field("aiPromptId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    origin = field("origin")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIPromptVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIPromptVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIPromptsRequest:
    boto3_raw_data: "type_defs.ListAIPromptsRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    origin = field("origin")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIPromptsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIPromptsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssistantAssociationsRequest:
    boto3_raw_data: "type_defs.ListAssistantAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssistantAssociationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssistantAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssistantsRequest:
    boto3_raw_data: "type_defs.ListAssistantsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssistantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssistantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContentAssociationsRequest:
    boto3_raw_data: "type_defs.ListContentAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    contentId = field("contentId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContentAssociationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContentAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContentsRequest:
    boto3_raw_data: "type_defs.ListContentsRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportJobsRequest:
    boto3_raw_data: "type_defs.ListImportJobsRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKnowledgeBasesRequest:
    boto3_raw_data: "type_defs.ListKnowledgeBasesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKnowledgeBasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKnowledgeBasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessageTemplateVersionsRequest:
    boto3_raw_data: "type_defs.ListMessageTemplateVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMessageTemplateVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessageTemplateVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateVersionSummary:
    boto3_raw_data: "type_defs.MessageTemplateVersionSummaryTypeDef" = (
        dataclasses.field()
    )

    messageTemplateArn = field("messageTemplateArn")
    messageTemplateId = field("messageTemplateId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    channelSubtype = field("channelSubtype")
    isActive = field("isActive")
    versionNumber = field("versionNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MessageTemplateVersionSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessageTemplatesRequest:
    boto3_raw_data: "type_defs.ListMessageTemplatesRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessageTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessageTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateSummary:
    boto3_raw_data: "type_defs.MessageTemplateSummaryTypeDef" = dataclasses.field()

    messageTemplateArn = field("messageTemplateArn")
    messageTemplateId = field("messageTemplateId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    channelSubtype = field("channelSubtype")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    lastModifiedBy = field("lastModifiedBy")
    activeVersionNumber = field("activeVersionNumber")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessagesRequest:
    boto3_raw_data: "type_defs.ListMessagesRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    sessionId = field("sessionId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQuickResponsesRequest:
    boto3_raw_data: "type_defs.ListQuickResponsesRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQuickResponsesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQuickResponsesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseSummary:
    boto3_raw_data: "type_defs.QuickResponseSummaryTypeDef" = dataclasses.field()

    quickResponseArn = field("quickResponseArn")
    quickResponseId = field("quickResponseId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    contentType = field("contentType")
    status = field("status")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    description = field("description")
    lastModifiedBy = field("lastModifiedBy")
    isActive = field("isActive")
    channels = field("channels")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickResponseSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseSummaryTypeDef"]
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
class MessageConfiguration:
    boto3_raw_data: "type_defs.MessageConfigurationTypeDef" = dataclasses.field()

    generateFillerMessage = field("generateFillerMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextMessage:
    boto3_raw_data: "type_defs.TextMessageTypeDef" = dataclasses.field()

    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextMessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateFilterField:
    boto3_raw_data: "type_defs.MessageTemplateFilterFieldTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    values = field("values")
    includeNoExistence = field("includeNoExistence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageTemplateFilterFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateFilterFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateOrderField:
    boto3_raw_data: "type_defs.MessageTemplateOrderFieldTypeDef" = dataclasses.field()

    name = field("name")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageTemplateOrderFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateOrderFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateQueryField:
    boto3_raw_data: "type_defs.MessageTemplateQueryFieldTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")
    allowFuzziness = field("allowFuzziness")
    priority = field("priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageTemplateQueryFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateQueryFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyRecommendationsReceivedError:
    boto3_raw_data: "type_defs.NotifyRecommendationsReceivedErrorTypeDef" = (
        dataclasses.field()
    )

    recommendationId = field("recommendationId")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotifyRecommendationsReceivedErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyRecommendationsReceivedErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyRecommendationsReceivedRequest:
    boto3_raw_data: "type_defs.NotifyRecommendationsReceivedRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    sessionId = field("sessionId")
    recommendationIds = field("recommendationIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotifyRecommendationsReceivedRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyRecommendationsReceivedRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCondition:
    boto3_raw_data: "type_defs.TagConditionTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryConditionItem:
    boto3_raw_data: "type_defs.QueryConditionItemTypeDef" = dataclasses.field()

    field = field("field")
    comparator = field("comparator")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryConditionItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryConditionItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryTextInputData:
    boto3_raw_data: "type_defs.QueryTextInputDataTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryTextInputDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryTextInputDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryRecommendationTriggerData:
    boto3_raw_data: "type_defs.QueryRecommendationTriggerDataTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QueryRecommendationTriggerDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryRecommendationTriggerDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseContentProvider:
    boto3_raw_data: "type_defs.QuickResponseContentProviderTypeDef" = (
        dataclasses.field()
    )

    content = field("content")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickResponseContentProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseContentProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseFilterField:
    boto3_raw_data: "type_defs.QuickResponseFilterFieldTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    values = field("values")
    includeNoExistence = field("includeNoExistence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickResponseFilterFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseFilterFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseOrderField:
    boto3_raw_data: "type_defs.QuickResponseOrderFieldTypeDef" = dataclasses.field()

    name = field("name")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickResponseOrderFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseOrderFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseQueryField:
    boto3_raw_data: "type_defs.QuickResponseQueryFieldTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")
    allowFuzziness = field("allowFuzziness")
    priority = field("priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickResponseQueryFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseQueryFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAssistantAIAgentRequest:
    boto3_raw_data: "type_defs.RemoveAssistantAIAgentRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiAgentType = field("aiAgentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveAssistantAIAgentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAssistantAIAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveKnowledgeBaseTemplateUriRequest:
    boto3_raw_data: "type_defs.RemoveKnowledgeBaseTemplateUriRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveKnowledgeBaseTemplateUriRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveKnowledgeBaseTemplateUriRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeSessionDataValue:
    boto3_raw_data: "type_defs.RuntimeSessionDataValueTypeDef" = dataclasses.field()

    stringValue = field("stringValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeSessionDataValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeSessionDataValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionSummary:
    boto3_raw_data: "type_defs.SessionSummaryTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    sessionArn = field("sessionArn")
    assistantId = field("assistantId")
    assistantArn = field("assistantArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SeedUrl:
    boto3_raw_data: "type_defs.SeedUrlTypeDef" = dataclasses.field()

    url = field("url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SeedUrlTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SeedUrlTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionIntegrationConfiguration:
    boto3_raw_data: "type_defs.SessionIntegrationConfigurationTypeDef" = (
        dataclasses.field()
    )

    topicIntegrationArn = field("topicIntegrationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SessionIntegrationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionIntegrationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartContentUploadRequest:
    boto3_raw_data: "type_defs.StartContentUploadRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    contentType = field("contentType")
    presignedUrlTimeToLive = field("presignedUrlTimeToLive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartContentUploadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartContentUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SystemEndpointAttributes:
    boto3_raw_data: "type_defs.SystemEndpointAttributesTypeDef" = dataclasses.field()

    address = field("address")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SystemEndpointAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SystemEndpointAttributesTypeDef"]
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
class UpdateContentRequest:
    boto3_raw_data: "type_defs.UpdateContentRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    contentId = field("contentId")
    revisionId = field("revisionId")
    title = field("title")
    overrideLinkOutUri = field("overrideLinkOutUri")
    removeOverrideLinkOutUri = field("removeOverrideLinkOutUri")
    metadata = field("metadata")
    uploadId = field("uploadId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKnowledgeBaseTemplateUriRequest:
    boto3_raw_data: "type_defs.UpdateKnowledgeBaseTemplateUriRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    templateUri = field("templateUri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateKnowledgeBaseTemplateUriRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKnowledgeBaseTemplateUriRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebCrawlerLimits:
    boto3_raw_data: "type_defs.WebCrawlerLimitsTypeDef" = dataclasses.field()

    rateLimit = field("rateLimit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebCrawlerLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebCrawlerLimitsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssistantAIAgentRequest:
    boto3_raw_data: "type_defs.UpdateAssistantAIAgentRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiAgentType = field("aiAgentType")

    @cached_property
    def configuration(self):  # pragma: no cover
        return AIAgentConfigurationData.make_one(self.boto3_raw_data["configuration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssistantAIAgentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssistantAIAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailContentPolicyConfigOutput:
    boto3_raw_data: "type_defs.AIGuardrailContentPolicyConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filtersConfig(self):  # pragma: no cover
        return GuardrailContentFilterConfig.make_many(
            self.boto3_raw_data["filtersConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AIGuardrailContentPolicyConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailContentPolicyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailContentPolicyConfig:
    boto3_raw_data: "type_defs.AIGuardrailContentPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filtersConfig(self):  # pragma: no cover
        return GuardrailContentFilterConfig.make_many(
            self.boto3_raw_data["filtersConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AIGuardrailContentPolicyConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailContentPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailContextualGroundingPolicyConfigOutput:
    boto3_raw_data: (
        "type_defs.AIGuardrailContextualGroundingPolicyConfigOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def filtersConfig(self):  # pragma: no cover
        return GuardrailContextualGroundingFilterConfig.make_many(
            self.boto3_raw_data["filtersConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AIGuardrailContextualGroundingPolicyConfigOutputTypeDef"
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
                "type_defs.AIGuardrailContextualGroundingPolicyConfigOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailContextualGroundingPolicyConfig:
    boto3_raw_data: "type_defs.AIGuardrailContextualGroundingPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filtersConfig(self):  # pragma: no cover
        return GuardrailContextualGroundingFilterConfig.make_many(
            self.boto3_raw_data["filtersConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AIGuardrailContextualGroundingPolicyConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailContextualGroundingPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailSensitiveInformationPolicyConfigOutput:
    boto3_raw_data: (
        "type_defs.AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def piiEntitiesConfig(self):  # pragma: no cover
        return GuardrailPiiEntityConfig.make_many(
            self.boto3_raw_data["piiEntitiesConfig"]
        )

    @cached_property
    def regexesConfig(self):  # pragma: no cover
        return GuardrailRegexConfig.make_many(self.boto3_raw_data["regexesConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef"
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
                "type_defs.AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailSensitiveInformationPolicyConfig:
    boto3_raw_data: "type_defs.AIGuardrailSensitiveInformationPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def piiEntitiesConfig(self):  # pragma: no cover
        return GuardrailPiiEntityConfig.make_many(
            self.boto3_raw_data["piiEntitiesConfig"]
        )

    @cached_property
    def regexesConfig(self):  # pragma: no cover
        return GuardrailRegexConfig.make_many(self.boto3_raw_data["regexesConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AIGuardrailSensitiveInformationPolicyConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailSensitiveInformationPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailVersionSummary:
    boto3_raw_data: "type_defs.AIGuardrailVersionSummaryTypeDef" = dataclasses.field()

    @cached_property
    def aiGuardrailSummary(self):  # pragma: no cover
        return AIGuardrailSummary.make_one(self.boto3_raw_data["aiGuardrailSummary"])

    versionNumber = field("versionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AIGuardrailVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailTopicPolicyConfigOutput:
    boto3_raw_data: "type_defs.AIGuardrailTopicPolicyConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def topicsConfig(self):  # pragma: no cover
        return GuardrailTopicConfigOutput.make_many(self.boto3_raw_data["topicsConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AIGuardrailTopicPolicyConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailTopicPolicyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailTopicPolicyConfig:
    boto3_raw_data: "type_defs.AIGuardrailTopicPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def topicsConfig(self):  # pragma: no cover
        return GuardrailTopicConfig.make_many(self.boto3_raw_data["topicsConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AIGuardrailTopicPolicyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailTopicPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailWordPolicyConfigOutput:
    boto3_raw_data: "type_defs.AIGuardrailWordPolicyConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def wordsConfig(self):  # pragma: no cover
        return GuardrailWordConfig.make_many(self.boto3_raw_data["wordsConfig"])

    @cached_property
    def managedWordListsConfig(self):  # pragma: no cover
        return GuardrailManagedWordsConfig.make_many(
            self.boto3_raw_data["managedWordListsConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AIGuardrailWordPolicyConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailWordPolicyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailWordPolicyConfig:
    boto3_raw_data: "type_defs.AIGuardrailWordPolicyConfigTypeDef" = dataclasses.field()

    @cached_property
    def wordsConfig(self):  # pragma: no cover
        return GuardrailWordConfig.make_many(self.boto3_raw_data["wordsConfig"])

    @cached_property
    def managedWordListsConfig(self):  # pragma: no cover
        return GuardrailManagedWordsConfig.make_many(
            self.boto3_raw_data["managedWordListsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AIGuardrailWordPolicyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIGuardrailWordPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIPromptVersionSummary:
    boto3_raw_data: "type_defs.AIPromptVersionSummaryTypeDef" = dataclasses.field()

    @cached_property
    def aiPromptSummary(self):  # pragma: no cover
        return AIPromptSummary.make_one(self.boto3_raw_data["aiPromptSummary"])

    versionNumber = field("versionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AIPromptVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIPromptVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIPromptTemplateConfiguration:
    boto3_raw_data: "type_defs.AIPromptTemplateConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def textFullAIPromptEditTemplateConfiguration(self):  # pragma: no cover
        return TextFullAIPromptEditTemplateConfiguration.make_one(
            self.boto3_raw_data["textFullAIPromptEditTemplateConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AIPromptTemplateConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIPromptTemplateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateMessageTemplateResponse:
    boto3_raw_data: "type_defs.ActivateMessageTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    messageTemplateArn = field("messageTemplateArn")
    messageTemplateId = field("messageTemplateId")
    versionNumber = field("versionNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActivateMessageTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateMessageTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateMessageTemplateResponse:
    boto3_raw_data: "type_defs.DeactivateMessageTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    messageTemplateArn = field("messageTemplateArn")
    messageTemplateId = field("messageTemplateId")
    versionNumber = field("versionNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeactivateMessageTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateMessageTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIGuardrailsResponse:
    boto3_raw_data: "type_defs.ListAIGuardrailsResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiGuardrailSummaries(self):  # pragma: no cover
        return AIGuardrailSummary.make_many(self.boto3_raw_data["aiGuardrailSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIGuardrailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIGuardrailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIPromptsResponse:
    boto3_raw_data: "type_defs.ListAIPromptsResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiPromptSummaries(self):  # pragma: no cover
        return AIPromptSummary.make_many(self.boto3_raw_data["aiPromptSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIPromptsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIPromptsResponseTypeDef"]
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
class StartContentUploadResponse:
    boto3_raw_data: "type_defs.StartContentUploadResponseTypeDef" = dataclasses.field()

    uploadId = field("uploadId")
    url = field("url")
    urlExpiry = field("urlExpiry")
    headersToInclude = field("headersToInclude")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartContentUploadResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartContentUploadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentAssociationContents:
    boto3_raw_data: "type_defs.ContentAssociationContentsTypeDef" = dataclasses.field()

    @cached_property
    def amazonConnectGuideAssociation(self):  # pragma: no cover
        return AmazonConnectGuideAssociationData.make_one(
            self.boto3_raw_data["amazonConnectGuideAssociation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentAssociationContentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentAssociationContentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssistantAssociationRequest:
    boto3_raw_data: "type_defs.CreateAssistantAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    associationType = field("associationType")

    @cached_property
    def association(self):  # pragma: no cover
        return AssistantAssociationInputData.make_one(
            self.boto3_raw_data["association"]
        )

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAssistantAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssistantAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssistantAssociationOutputData:
    boto3_raw_data: "type_defs.AssistantAssociationOutputDataTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def knowledgeBaseAssociation(self):  # pragma: no cover
        return KnowledgeBaseAssociationData.make_one(
            self.boto3_raw_data["knowledgeBaseAssociation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssistantAssociationOutputDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssistantAssociationOutputDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssistantData:
    boto3_raw_data: "type_defs.AssistantDataTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    name = field("name")
    type = field("type")
    status = field("status")
    description = field("description")
    tags = field("tags")

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    @cached_property
    def integrationConfiguration(self):  # pragma: no cover
        return AssistantIntegrationConfiguration.make_one(
            self.boto3_raw_data["integrationConfiguration"]
        )

    @cached_property
    def capabilityConfiguration(self):  # pragma: no cover
        return AssistantCapabilityConfiguration.make_one(
            self.boto3_raw_data["capabilityConfiguration"]
        )

    aiAgentConfiguration = field("aiAgentConfiguration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssistantDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssistantDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssistantSummary:
    boto3_raw_data: "type_defs.AssistantSummaryTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    name = field("name")
    type = field("type")
    status = field("status")
    description = field("description")
    tags = field("tags")

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    @cached_property
    def integrationConfiguration(self):  # pragma: no cover
        return AssistantIntegrationConfiguration.make_one(
            self.boto3_raw_data["integrationConfiguration"]
        )

    @cached_property
    def capabilityConfiguration(self):  # pragma: no cover
        return AssistantCapabilityConfiguration.make_one(
            self.boto3_raw_data["capabilityConfiguration"]
        )

    aiAgentConfiguration = field("aiAgentConfiguration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssistantSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssistantSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssistantRequest:
    boto3_raw_data: "type_defs.CreateAssistantRequestTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    clientToken = field("clientToken")
    description = field("description")
    tags = field("tags")

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssistantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssistantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockFoundationModelConfigurationForParsing:
    boto3_raw_data: "type_defs.BedrockFoundationModelConfigurationForParsingTypeDef" = (
        dataclasses.field()
    )

    modelArn = field("modelArn")

    @cached_property
    def parsingPrompt(self):  # pragma: no cover
        return ParsingPrompt.make_one(self.boto3_raw_data["parsingPrompt"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BedrockFoundationModelConfigurationForParsingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockFoundationModelConfigurationForParsingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Configuration:
    boto3_raw_data: "type_defs.ConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def connectConfiguration(self):  # pragma: no cover
        return ConnectConfiguration.make_one(
            self.boto3_raw_data["connectConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerativeDataDetailsPaginator:
    boto3_raw_data: "type_defs.GenerativeDataDetailsPaginatorTypeDef" = (
        dataclasses.field()
    )

    completion = field("completion")
    references = field("references")

    @cached_property
    def rankingData(self):  # pragma: no cover
        return RankingData.make_one(self.boto3_raw_data["rankingData"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerativeDataDetailsPaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerativeDataDetailsPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerativeDataDetails:
    boto3_raw_data: "type_defs.GenerativeDataDetailsTypeDef" = dataclasses.field()

    completion = field("completion")
    references = field("references")

    @cached_property
    def rankingData(self):  # pragma: no cover
        return RankingData.make_one(self.boto3_raw_data["rankingData"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerativeDataDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerativeDataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContentResponse:
    boto3_raw_data: "type_defs.CreateContentResponseTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return ContentData.make_one(self.boto3_raw_data["content"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContentResponse:
    boto3_raw_data: "type_defs.GetContentResponseTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return ContentData.make_one(self.boto3_raw_data["content"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContentResponse:
    boto3_raw_data: "type_defs.UpdateContentResponseTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return ContentData.make_one(self.boto3_raw_data["content"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentFeedbackData:
    boto3_raw_data: "type_defs.ContentFeedbackDataTypeDef" = dataclasses.field()

    @cached_property
    def generativeContentFeedbackData(self):  # pragma: no cover
        return GenerativeContentFeedbackData.make_one(
            self.boto3_raw_data["generativeContentFeedbackData"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentFeedbackDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentFeedbackDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContentSummaryResponse:
    boto3_raw_data: "type_defs.GetContentSummaryResponseTypeDef" = dataclasses.field()

    @cached_property
    def contentSummary(self):  # pragma: no cover
        return ContentSummary.make_one(self.boto3_raw_data["contentSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContentSummaryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContentSummaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContentsResponse:
    boto3_raw_data: "type_defs.ListContentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def contentSummaries(self):  # pragma: no cover
        return ContentSummary.make_many(self.boto3_raw_data["contentSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContentResponse:
    boto3_raw_data: "type_defs.SearchContentResponseTypeDef" = dataclasses.field()

    @cached_property
    def contentSummaries(self):  # pragma: no cover
        return ContentSummary.make_many(self.boto3_raw_data["contentSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationContext:
    boto3_raw_data: "type_defs.ConversationContextTypeDef" = dataclasses.field()

    @cached_property
    def selfServiceConversationHistory(self):  # pragma: no cover
        return SelfServiceConversationHistory.make_many(
            self.boto3_raw_data["selfServiceConversationHistory"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversationContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIAgentVersionRequest:
    boto3_raw_data: "type_defs.CreateAIAgentVersionRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiAgentId = field("aiAgentId")
    modifiedTime = field("modifiedTime")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAIAgentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIAgentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIGuardrailVersionRequest:
    boto3_raw_data: "type_defs.CreateAIGuardrailVersionRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiGuardrailId = field("aiGuardrailId")
    modifiedTime = field("modifiedTime")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAIGuardrailVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIGuardrailVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIPromptVersionRequest:
    boto3_raw_data: "type_defs.CreateAIPromptVersionRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiPromptId = field("aiPromptId")
    modifiedTime = field("modifiedTime")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAIPromptVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIPromptVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMessageTemplateAttachmentResponse:
    boto3_raw_data: "type_defs.CreateMessageTemplateAttachmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def attachment(self):  # pragma: no cover
        return MessageTemplateAttachment.make_one(self.boto3_raw_data["attachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMessageTemplateAttachmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMessageTemplateAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReference:
    boto3_raw_data: "type_defs.DataReferenceTypeDef" = dataclasses.field()

    @cached_property
    def contentReference(self):  # pragma: no cover
        return ContentReference.make_one(self.boto3_raw_data["contentReference"])

    @cached_property
    def generativeReference(self):  # pragma: no cover
        return GenerativeReference.make_one(self.boto3_raw_data["generativeReference"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentText:
    boto3_raw_data: "type_defs.DocumentTextTypeDef" = dataclasses.field()

    text = field("text")

    @cached_property
    def highlights(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["highlights"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentTextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentTextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailMessageTemplateContentBody:
    boto3_raw_data: "type_defs.EmailMessageTemplateContentBodyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def plainText(self):  # pragma: no cover
        return MessageTemplateBodyContentProvider.make_one(
            self.boto3_raw_data["plainText"]
        )

    @cached_property
    def html(self):  # pragma: no cover
        return MessageTemplateBodyContentProvider.make_one(self.boto3_raw_data["html"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EmailMessageTemplateContentBodyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailMessageTemplateContentBodyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSMessageTemplateContentBody:
    boto3_raw_data: "type_defs.SMSMessageTemplateContentBodyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def plainText(self):  # pragma: no cover
        return MessageTemplateBodyContentProvider.make_one(
            self.boto3_raw_data["plainText"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SMSMessageTemplateContentBodyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSMessageTemplateContentBodyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateSearchResultData:
    boto3_raw_data: "type_defs.MessageTemplateSearchResultDataTypeDef" = (
        dataclasses.field()
    )

    messageTemplateArn = field("messageTemplateArn")
    messageTemplateId = field("messageTemplateId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    channelSubtype = field("channelSubtype")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    lastModifiedBy = field("lastModifiedBy")
    isActive = field("isActive")
    versionNumber = field("versionNumber")
    description = field("description")

    @cached_property
    def groupingConfiguration(self):  # pragma: no cover
        return GroupingConfigurationOutput.make_one(
            self.boto3_raw_data["groupingConfiguration"]
        )

    language = field("language")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MessageTemplateSearchResultDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateSearchResultDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchExpression:
    boto3_raw_data: "type_defs.SearchExpressionTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchicalChunkingConfigurationOutput:
    boto3_raw_data: "type_defs.HierarchicalChunkingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def levelConfigurations(self):  # pragma: no cover
        return HierarchicalChunkingLevelConfiguration.make_many(
            self.boto3_raw_data["levelConfigurations"]
        )

    overlapTokens = field("overlapTokens")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HierarchicalChunkingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchicalChunkingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchicalChunkingConfiguration:
    boto3_raw_data: "type_defs.HierarchicalChunkingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def levelConfigurations(self):  # pragma: no cover
        return HierarchicalChunkingLevelConfiguration.make_many(
            self.boto3_raw_data["levelConfigurations"]
        )

    overlapTokens = field("overlapTokens")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HierarchicalChunkingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchicalChunkingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIAgentVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAIAgentVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiAgentId = field("aiAgentId")
    origin = field("origin")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAIAgentVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIAgentVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIAgentsRequestPaginate:
    boto3_raw_data: "type_defs.ListAIAgentsRequestPaginateTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    origin = field("origin")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIAgentsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIAgentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIGuardrailVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAIGuardrailVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiGuardrailId = field("aiGuardrailId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAIGuardrailVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIGuardrailVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIGuardrailsRequestPaginate:
    boto3_raw_data: "type_defs.ListAIGuardrailsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAIGuardrailsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIGuardrailsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIPromptVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAIPromptVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    aiPromptId = field("aiPromptId")
    origin = field("origin")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAIPromptVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIPromptVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIPromptsRequestPaginate:
    boto3_raw_data: "type_defs.ListAIPromptsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    origin = field("origin")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIPromptsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIPromptsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssistantAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssistantAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssistantAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssistantAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssistantsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssistantsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssistantsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssistantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContentAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListContentAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    contentId = field("contentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContentAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContentAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContentsRequestPaginate:
    boto3_raw_data: "type_defs.ListContentsRequestPaginateTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContentsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImportJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKnowledgeBasesRequestPaginate:
    boto3_raw_data: "type_defs.ListKnowledgeBasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKnowledgeBasesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKnowledgeBasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessageTemplateVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListMessageTemplateVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMessageTemplateVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessageTemplateVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessageTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListMessageTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMessageTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessageTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessagesRequestPaginate:
    boto3_raw_data: "type_defs.ListMessagesRequestPaginateTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    sessionId = field("sessionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessagesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQuickResponsesRequestPaginate:
    boto3_raw_data: "type_defs.ListQuickResponsesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQuickResponsesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQuickResponsesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessageTemplateVersionsResponse:
    boto3_raw_data: "type_defs.ListMessageTemplateVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def messageTemplateVersionSummaries(self):  # pragma: no cover
        return MessageTemplateVersionSummary.make_many(
            self.boto3_raw_data["messageTemplateVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMessageTemplateVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessageTemplateVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessageTemplatesResponse:
    boto3_raw_data: "type_defs.ListMessageTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def messageTemplateSummaries(self):  # pragma: no cover
        return MessageTemplateSummary.make_many(
            self.boto3_raw_data["messageTemplateSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessageTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessageTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQuickResponsesResponse:
    boto3_raw_data: "type_defs.ListQuickResponsesResponseTypeDef" = dataclasses.field()

    @cached_property
    def quickResponseSummaries(self):  # pragma: no cover
        return QuickResponseSummary.make_many(
            self.boto3_raw_data["quickResponseSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQuickResponsesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQuickResponsesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageResponse:
    boto3_raw_data: "type_defs.SendMessageResponseTypeDef" = dataclasses.field()

    requestMessageId = field("requestMessageId")

    @cached_property
    def configuration(self):  # pragma: no cover
        return MessageConfiguration.make_one(self.boto3_raw_data["configuration"])

    nextMessageToken = field("nextMessageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageData:
    boto3_raw_data: "type_defs.MessageDataTypeDef" = dataclasses.field()

    @cached_property
    def text(self):  # pragma: no cover
        return TextMessage.make_one(self.boto3_raw_data["text"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateSearchExpression:
    boto3_raw_data: "type_defs.MessageTemplateSearchExpressionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def queries(self):  # pragma: no cover
        return MessageTemplateQueryField.make_many(self.boto3_raw_data["queries"])

    @cached_property
    def filters(self):  # pragma: no cover
        return MessageTemplateFilterField.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def orderOnField(self):  # pragma: no cover
        return MessageTemplateOrderField.make_one(self.boto3_raw_data["orderOnField"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MessageTemplateSearchExpressionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateSearchExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyRecommendationsReceivedResponse:
    boto3_raw_data: "type_defs.NotifyRecommendationsReceivedResponseTypeDef" = (
        dataclasses.field()
    )

    recommendationIds = field("recommendationIds")

    @cached_property
    def errors(self):  # pragma: no cover
        return NotifyRecommendationsReceivedError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotifyRecommendationsReceivedResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyRecommendationsReceivedResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrConditionOutput:
    boto3_raw_data: "type_defs.OrConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def andConditions(self):  # pragma: no cover
        return TagCondition.make_many(self.boto3_raw_data["andConditions"])

    @cached_property
    def tagCondition(self):  # pragma: no cover
        return TagCondition.make_one(self.boto3_raw_data["tagCondition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrConditionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrCondition:
    boto3_raw_data: "type_defs.OrConditionTypeDef" = dataclasses.field()

    @cached_property
    def andConditions(self):  # pragma: no cover
        return TagCondition.make_many(self.boto3_raw_data["andConditions"])

    @cached_property
    def tagCondition(self):  # pragma: no cover
        return TagCondition.make_one(self.boto3_raw_data["tagCondition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OrConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryCondition:
    boto3_raw_data: "type_defs.QueryConditionTypeDef" = dataclasses.field()

    @cached_property
    def single(self):  # pragma: no cover
        return QueryConditionItem.make_one(self.boto3_raw_data["single"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryInputData:
    boto3_raw_data: "type_defs.QueryInputDataTypeDef" = dataclasses.field()

    @cached_property
    def queryTextInputData(self):  # pragma: no cover
        return QueryTextInputData.make_one(self.boto3_raw_data["queryTextInputData"])

    @cached_property
    def intentInputData(self):  # pragma: no cover
        return IntentInputData.make_one(self.boto3_raw_data["intentInputData"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryInputDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryInputDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationTriggerData:
    boto3_raw_data: "type_defs.RecommendationTriggerDataTypeDef" = dataclasses.field()

    @cached_property
    def query(self):  # pragma: no cover
        return QueryRecommendationTriggerData.make_one(self.boto3_raw_data["query"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationTriggerDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationTriggerDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseContents:
    boto3_raw_data: "type_defs.QuickResponseContentsTypeDef" = dataclasses.field()

    @cached_property
    def plainText(self):  # pragma: no cover
        return QuickResponseContentProvider.make_one(self.boto3_raw_data["plainText"])

    @cached_property
    def markdown(self):  # pragma: no cover
        return QuickResponseContentProvider.make_one(self.boto3_raw_data["markdown"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickResponseContentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseContentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseSearchExpression:
    boto3_raw_data: "type_defs.QuickResponseSearchExpressionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def queries(self):  # pragma: no cover
        return QuickResponseQueryField.make_many(self.boto3_raw_data["queries"])

    @cached_property
    def filters(self):  # pragma: no cover
        return QuickResponseFilterField.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def orderOnField(self):  # pragma: no cover
        return QuickResponseOrderField.make_one(self.boto3_raw_data["orderOnField"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QuickResponseSearchExpressionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseSearchExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeSessionData:
    boto3_raw_data: "type_defs.RuntimeSessionDataTypeDef" = dataclasses.field()

    key = field("key")

    @cached_property
    def value(self):  # pragma: no cover
        return RuntimeSessionDataValue.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeSessionDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeSessionDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSessionsResponse:
    boto3_raw_data: "type_defs.SearchSessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def sessionSummaries(self):  # pragma: no cover
        return SessionSummary.make_many(self.boto3_raw_data["sessionSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UrlConfigurationOutput:
    boto3_raw_data: "type_defs.UrlConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def seedUrls(self):  # pragma: no cover
        return SeedUrl.make_many(self.boto3_raw_data["seedUrls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UrlConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UrlConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UrlConfiguration:
    boto3_raw_data: "type_defs.UrlConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def seedUrls(self):  # pragma: no cover
        return SeedUrl.make_many(self.boto3_raw_data["seedUrls"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UrlConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UrlConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SystemAttributes:
    boto3_raw_data: "type_defs.SystemAttributesTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def customerEndpoint(self):  # pragma: no cover
        return SystemEndpointAttributes.make_one(
            self.boto3_raw_data["customerEndpoint"]
        )

    @cached_property
    def systemEndpoint(self):  # pragma: no cover
        return SystemEndpointAttributes.make_one(self.boto3_raw_data["systemEndpoint"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SystemAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SystemAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIGuardrailVersionsResponse:
    boto3_raw_data: "type_defs.ListAIGuardrailVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aiGuardrailVersionSummaries(self):  # pragma: no cover
        return AIGuardrailVersionSummary.make_many(
            self.boto3_raw_data["aiGuardrailVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAIGuardrailVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIGuardrailVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIGuardrailData:
    boto3_raw_data: "type_defs.AIGuardrailDataTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    aiGuardrailArn = field("aiGuardrailArn")
    aiGuardrailId = field("aiGuardrailId")
    name = field("name")
    visibilityStatus = field("visibilityStatus")
    blockedInputMessaging = field("blockedInputMessaging")
    blockedOutputsMessaging = field("blockedOutputsMessaging")
    description = field("description")

    @cached_property
    def topicPolicyConfig(self):  # pragma: no cover
        return AIGuardrailTopicPolicyConfigOutput.make_one(
            self.boto3_raw_data["topicPolicyConfig"]
        )

    @cached_property
    def contentPolicyConfig(self):  # pragma: no cover
        return AIGuardrailContentPolicyConfigOutput.make_one(
            self.boto3_raw_data["contentPolicyConfig"]
        )

    @cached_property
    def wordPolicyConfig(self):  # pragma: no cover
        return AIGuardrailWordPolicyConfigOutput.make_one(
            self.boto3_raw_data["wordPolicyConfig"]
        )

    @cached_property
    def sensitiveInformationPolicyConfig(self):  # pragma: no cover
        return AIGuardrailSensitiveInformationPolicyConfigOutput.make_one(
            self.boto3_raw_data["sensitiveInformationPolicyConfig"]
        )

    @cached_property
    def contextualGroundingPolicyConfig(self):  # pragma: no cover
        return AIGuardrailContextualGroundingPolicyConfigOutput.make_one(
            self.boto3_raw_data["contextualGroundingPolicyConfig"]
        )

    tags = field("tags")
    status = field("status")
    modifiedTime = field("modifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AIGuardrailDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AIGuardrailDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIPromptVersionsResponse:
    boto3_raw_data: "type_defs.ListAIPromptVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aiPromptVersionSummaries(self):  # pragma: no cover
        return AIPromptVersionSummary.make_many(
            self.boto3_raw_data["aiPromptVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIPromptVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIPromptVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIPromptData:
    boto3_raw_data: "type_defs.AIPromptDataTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    aiPromptId = field("aiPromptId")
    aiPromptArn = field("aiPromptArn")
    name = field("name")
    type = field("type")
    templateType = field("templateType")
    modelId = field("modelId")
    apiFormat = field("apiFormat")

    @cached_property
    def templateConfiguration(self):  # pragma: no cover
        return AIPromptTemplateConfiguration.make_one(
            self.boto3_raw_data["templateConfiguration"]
        )

    visibilityStatus = field("visibilityStatus")
    modifiedTime = field("modifiedTime")
    description = field("description")
    tags = field("tags")
    origin = field("origin")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AIPromptDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AIPromptDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIPromptRequest:
    boto3_raw_data: "type_defs.CreateAIPromptRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    name = field("name")
    type = field("type")

    @cached_property
    def templateConfiguration(self):  # pragma: no cover
        return AIPromptTemplateConfiguration.make_one(
            self.boto3_raw_data["templateConfiguration"]
        )

    visibilityStatus = field("visibilityStatus")
    templateType = field("templateType")
    modelId = field("modelId")
    apiFormat = field("apiFormat")
    clientToken = field("clientToken")
    tags = field("tags")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAIPromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIPromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAIPromptRequest:
    boto3_raw_data: "type_defs.UpdateAIPromptRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiPromptId = field("aiPromptId")
    visibilityStatus = field("visibilityStatus")
    clientToken = field("clientToken")

    @cached_property
    def templateConfiguration(self):  # pragma: no cover
        return AIPromptTemplateConfiguration.make_one(
            self.boto3_raw_data["templateConfiguration"]
        )

    description = field("description")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAIPromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAIPromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentAssociationData:
    boto3_raw_data: "type_defs.ContentAssociationDataTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    contentId = field("contentId")
    contentArn = field("contentArn")
    contentAssociationId = field("contentAssociationId")
    contentAssociationArn = field("contentAssociationArn")
    associationType = field("associationType")

    @cached_property
    def associationData(self):  # pragma: no cover
        return ContentAssociationContents.make_one(
            self.boto3_raw_data["associationData"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentAssociationDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentAssociationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentAssociationSummary:
    boto3_raw_data: "type_defs.ContentAssociationSummaryTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    contentId = field("contentId")
    contentArn = field("contentArn")
    contentAssociationId = field("contentAssociationId")
    contentAssociationArn = field("contentAssociationArn")
    associationType = field("associationType")

    @cached_property
    def associationData(self):  # pragma: no cover
        return ContentAssociationContents.make_one(
            self.boto3_raw_data["associationData"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentAssociationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContentAssociationRequest:
    boto3_raw_data: "type_defs.CreateContentAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    contentId = field("contentId")
    associationType = field("associationType")

    @cached_property
    def association(self):  # pragma: no cover
        return ContentAssociationContents.make_one(self.boto3_raw_data["association"])

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateContentAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContentAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssistantAssociationData:
    boto3_raw_data: "type_defs.AssistantAssociationDataTypeDef" = dataclasses.field()

    assistantAssociationId = field("assistantAssociationId")
    assistantAssociationArn = field("assistantAssociationArn")
    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    associationType = field("associationType")

    @cached_property
    def associationData(self):  # pragma: no cover
        return AssistantAssociationOutputData.make_one(
            self.boto3_raw_data["associationData"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssistantAssociationDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssistantAssociationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssistantAssociationSummary:
    boto3_raw_data: "type_defs.AssistantAssociationSummaryTypeDef" = dataclasses.field()

    assistantAssociationId = field("assistantAssociationId")
    assistantAssociationArn = field("assistantAssociationArn")
    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    associationType = field("associationType")

    @cached_property
    def associationData(self):  # pragma: no cover
        return AssistantAssociationOutputData.make_one(
            self.boto3_raw_data["associationData"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssistantAssociationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssistantAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssistantResponse:
    boto3_raw_data: "type_defs.CreateAssistantResponseTypeDef" = dataclasses.field()

    @cached_property
    def assistant(self):  # pragma: no cover
        return AssistantData.make_one(self.boto3_raw_data["assistant"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssistantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssistantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssistantResponse:
    boto3_raw_data: "type_defs.GetAssistantResponseTypeDef" = dataclasses.field()

    @cached_property
    def assistant(self):  # pragma: no cover
        return AssistantData.make_one(self.boto3_raw_data["assistant"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssistantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssistantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssistantAIAgentResponse:
    boto3_raw_data: "type_defs.UpdateAssistantAIAgentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assistant(self):  # pragma: no cover
        return AssistantData.make_one(self.boto3_raw_data["assistant"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssistantAIAgentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssistantAIAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssistantsResponse:
    boto3_raw_data: "type_defs.ListAssistantsResponseTypeDef" = dataclasses.field()

    @cached_property
    def assistantSummaries(self):  # pragma: no cover
        return AssistantSummary.make_many(self.boto3_raw_data["assistantSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssistantsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssistantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParsingConfiguration:
    boto3_raw_data: "type_defs.ParsingConfigurationTypeDef" = dataclasses.field()

    parsingStrategy = field("parsingStrategy")

    @cached_property
    def bedrockFoundationModelConfiguration(self):  # pragma: no cover
        return BedrockFoundationModelConfigurationForParsing.make_one(
            self.boto3_raw_data["bedrockFoundationModelConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParsingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParsingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSourceConfiguration:
    boto3_raw_data: "type_defs.ExternalSourceConfigurationTypeDef" = dataclasses.field()

    source = field("source")

    @cached_property
    def configuration(self):  # pragma: no cover
        return Configuration.make_one(self.boto3_raw_data["configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFeedbackRequest:
    boto3_raw_data: "type_defs.PutFeedbackRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    targetId = field("targetId")
    targetType = field("targetType")

    @cached_property
    def contentFeedback(self):  # pragma: no cover
        return ContentFeedbackData.make_one(self.boto3_raw_data["contentFeedback"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutFeedbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFeedbackResponse:
    boto3_raw_data: "type_defs.PutFeedbackResponseTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    targetId = field("targetId")
    targetType = field("targetType")

    @cached_property
    def contentFeedback(self):  # pragma: no cover
        return ContentFeedbackData.make_one(self.boto3_raw_data["contentFeedback"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutFeedbackResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFeedbackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Document:
    boto3_raw_data: "type_defs.DocumentTypeDef" = dataclasses.field()

    @cached_property
    def contentReference(self):  # pragma: no cover
        return ContentReference.make_one(self.boto3_raw_data["contentReference"])

    @cached_property
    def title(self):  # pragma: no cover
        return DocumentText.make_one(self.boto3_raw_data["title"])

    @cached_property
    def excerpt(self):  # pragma: no cover
        return DocumentText.make_one(self.boto3_raw_data["excerpt"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextData:
    boto3_raw_data: "type_defs.TextDataTypeDef" = dataclasses.field()

    @cached_property
    def title(self):  # pragma: no cover
        return DocumentText.make_one(self.boto3_raw_data["title"])

    @cached_property
    def excerpt(self):  # pragma: no cover
        return DocumentText.make_one(self.boto3_raw_data["excerpt"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailMessageTemplateContentOutput:
    boto3_raw_data: "type_defs.EmailMessageTemplateContentOutputTypeDef" = (
        dataclasses.field()
    )

    subject = field("subject")

    @cached_property
    def body(self):  # pragma: no cover
        return EmailMessageTemplateContentBody.make_one(self.boto3_raw_data["body"])

    @cached_property
    def headers(self):  # pragma: no cover
        return EmailHeader.make_many(self.boto3_raw_data["headers"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EmailMessageTemplateContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailMessageTemplateContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailMessageTemplateContent:
    boto3_raw_data: "type_defs.EmailMessageTemplateContentTypeDef" = dataclasses.field()

    subject = field("subject")

    @cached_property
    def body(self):  # pragma: no cover
        return EmailMessageTemplateContentBody.make_one(self.boto3_raw_data["body"])

    @cached_property
    def headers(self):  # pragma: no cover
        return EmailHeader.make_many(self.boto3_raw_data["headers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailMessageTemplateContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailMessageTemplateContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSMessageTemplateContent:
    boto3_raw_data: "type_defs.SMSMessageTemplateContentTypeDef" = dataclasses.field()

    @cached_property
    def body(self):  # pragma: no cover
        return SMSMessageTemplateContentBody.make_one(self.boto3_raw_data["body"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SMSMessageTemplateContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSMessageTemplateContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchMessageTemplatesResponse:
    boto3_raw_data: "type_defs.SearchMessageTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def results(self):  # pragma: no cover
        return MessageTemplateSearchResultData.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchMessageTemplatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchMessageTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContentRequestPaginate:
    boto3_raw_data: "type_defs.SearchContentRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def searchExpression(self):  # pragma: no cover
        return SearchExpression.make_one(self.boto3_raw_data["searchExpression"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchContentRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContentRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContentRequest:
    boto3_raw_data: "type_defs.SearchContentRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def searchExpression(self):  # pragma: no cover
        return SearchExpression.make_one(self.boto3_raw_data["searchExpression"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSessionsRequestPaginate:
    boto3_raw_data: "type_defs.SearchSessionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")

    @cached_property
    def searchExpression(self):  # pragma: no cover
        return SearchExpression.make_one(self.boto3_raw_data["searchExpression"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchSessionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSessionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSessionsRequest:
    boto3_raw_data: "type_defs.SearchSessionsRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")

    @cached_property
    def searchExpression(self):  # pragma: no cover
        return SearchExpression.make_one(self.boto3_raw_data["searchExpression"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQuickResponseRequest:
    boto3_raw_data: "type_defs.CreateQuickResponseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")

    @cached_property
    def content(self):  # pragma: no cover
        return QuickResponseDataProvider.make_one(self.boto3_raw_data["content"])

    contentType = field("contentType")
    groupingConfiguration = field("groupingConfiguration")
    description = field("description")
    shortcutKey = field("shortcutKey")
    isActive = field("isActive")
    channels = field("channels")
    language = field("language")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQuickResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQuickResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMessageTemplateMetadataRequest:
    boto3_raw_data: "type_defs.UpdateMessageTemplateMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")
    name = field("name")
    description = field("description")
    groupingConfiguration = field("groupingConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMessageTemplateMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMessageTemplateMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQuickResponseRequest:
    boto3_raw_data: "type_defs.UpdateQuickResponseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    quickResponseId = field("quickResponseId")
    name = field("name")

    @cached_property
    def content(self):  # pragma: no cover
        return QuickResponseDataProvider.make_one(self.boto3_raw_data["content"])

    contentType = field("contentType")
    groupingConfiguration = field("groupingConfiguration")
    removeGroupingConfiguration = field("removeGroupingConfiguration")
    description = field("description")
    removeDescription = field("removeDescription")
    shortcutKey = field("shortcutKey")
    removeShortcutKey = field("removeShortcutKey")
    isActive = field("isActive")
    channels = field("channels")
    language = field("language")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQuickResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQuickResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChunkingConfigurationOutput:
    boto3_raw_data: "type_defs.ChunkingConfigurationOutputTypeDef" = dataclasses.field()

    chunkingStrategy = field("chunkingStrategy")

    @cached_property
    def fixedSizeChunkingConfiguration(self):  # pragma: no cover
        return FixedSizeChunkingConfiguration.make_one(
            self.boto3_raw_data["fixedSizeChunkingConfiguration"]
        )

    @cached_property
    def hierarchicalChunkingConfiguration(self):  # pragma: no cover
        return HierarchicalChunkingConfigurationOutput.make_one(
            self.boto3_raw_data["hierarchicalChunkingConfiguration"]
        )

    @cached_property
    def semanticChunkingConfiguration(self):  # pragma: no cover
        return SemanticChunkingConfiguration.make_one(
            self.boto3_raw_data["semanticChunkingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChunkingConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChunkingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChunkingConfiguration:
    boto3_raw_data: "type_defs.ChunkingConfigurationTypeDef" = dataclasses.field()

    chunkingStrategy = field("chunkingStrategy")

    @cached_property
    def fixedSizeChunkingConfiguration(self):  # pragma: no cover
        return FixedSizeChunkingConfiguration.make_one(
            self.boto3_raw_data["fixedSizeChunkingConfiguration"]
        )

    @cached_property
    def hierarchicalChunkingConfiguration(self):  # pragma: no cover
        return HierarchicalChunkingConfiguration.make_one(
            self.boto3_raw_data["hierarchicalChunkingConfiguration"]
        )

    @cached_property
    def semanticChunkingConfiguration(self):  # pragma: no cover
        return SemanticChunkingConfiguration.make_one(
            self.boto3_raw_data["semanticChunkingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChunkingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChunkingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageInput:
    boto3_raw_data: "type_defs.MessageInputTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return MessageData.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageOutput:
    boto3_raw_data: "type_defs.MessageOutputTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return MessageData.make_one(self.boto3_raw_data["value"])

    messageId = field("messageId")
    participant = field("participant")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchMessageTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.SearchMessageTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def searchExpression(self):  # pragma: no cover
        return MessageTemplateSearchExpression.make_one(
            self.boto3_raw_data["searchExpression"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchMessageTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchMessageTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchMessageTemplatesRequest:
    boto3_raw_data: "type_defs.SearchMessageTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def searchExpression(self):  # pragma: no cover
        return MessageTemplateSearchExpression.make_one(
            self.boto3_raw_data["searchExpression"]
        )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchMessageTemplatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchMessageTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagFilterOutput:
    boto3_raw_data: "type_defs.TagFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def tagCondition(self):  # pragma: no cover
        return TagCondition.make_one(self.boto3_raw_data["tagCondition"])

    @cached_property
    def andConditions(self):  # pragma: no cover
        return TagCondition.make_many(self.boto3_raw_data["andConditions"])

    @cached_property
    def orConditions(self):  # pragma: no cover
        return OrConditionOutput.make_many(self.boto3_raw_data["orConditions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagFilterOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagFilter:
    boto3_raw_data: "type_defs.TagFilterTypeDef" = dataclasses.field()

    @cached_property
    def tagCondition(self):  # pragma: no cover
        return TagCondition.make_one(self.boto3_raw_data["tagCondition"])

    @cached_property
    def andConditions(self):  # pragma: no cover
        return TagCondition.make_many(self.boto3_raw_data["andConditions"])

    @cached_property
    def orConditions(self):  # pragma: no cover
        return OrCondition.make_many(self.boto3_raw_data["orConditions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryAssistantRequestPaginate:
    boto3_raw_data: "type_defs.QueryAssistantRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    queryText = field("queryText")
    sessionId = field("sessionId")

    @cached_property
    def queryCondition(self):  # pragma: no cover
        return QueryCondition.make_many(self.boto3_raw_data["queryCondition"])

    @cached_property
    def queryInputData(self):  # pragma: no cover
        return QueryInputData.make_one(self.boto3_raw_data["queryInputData"])

    overrideKnowledgeBaseSearchType = field("overrideKnowledgeBaseSearchType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QueryAssistantRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryAssistantRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryAssistantRequest:
    boto3_raw_data: "type_defs.QueryAssistantRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    queryText = field("queryText")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    sessionId = field("sessionId")

    @cached_property
    def queryCondition(self):  # pragma: no cover
        return QueryCondition.make_many(self.boto3_raw_data["queryCondition"])

    @cached_property
    def queryInputData(self):  # pragma: no cover
        return QueryInputData.make_one(self.boto3_raw_data["queryInputData"])

    overrideKnowledgeBaseSearchType = field("overrideKnowledgeBaseSearchType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryAssistantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryAssistantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationTrigger:
    boto3_raw_data: "type_defs.RecommendationTriggerTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    source = field("source")

    @cached_property
    def data(self):  # pragma: no cover
        return RecommendationTriggerData.make_one(self.boto3_raw_data["data"])

    recommendationIds = field("recommendationIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationTriggerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationTriggerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseData:
    boto3_raw_data: "type_defs.QuickResponseDataTypeDef" = dataclasses.field()

    quickResponseArn = field("quickResponseArn")
    quickResponseId = field("quickResponseId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    contentType = field("contentType")
    status = field("status")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")

    @cached_property
    def contents(self):  # pragma: no cover
        return QuickResponseContents.make_one(self.boto3_raw_data["contents"])

    description = field("description")

    @cached_property
    def groupingConfiguration(self):  # pragma: no cover
        return GroupingConfigurationOutput.make_one(
            self.boto3_raw_data["groupingConfiguration"]
        )

    shortcutKey = field("shortcutKey")
    lastModifiedBy = field("lastModifiedBy")
    isActive = field("isActive")
    channels = field("channels")
    language = field("language")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QuickResponseDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickResponseSearchResultData:
    boto3_raw_data: "type_defs.QuickResponseSearchResultDataTypeDef" = (
        dataclasses.field()
    )

    quickResponseArn = field("quickResponseArn")
    quickResponseId = field("quickResponseId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    contentType = field("contentType")
    status = field("status")

    @cached_property
    def contents(self):  # pragma: no cover
        return QuickResponseContents.make_one(self.boto3_raw_data["contents"])

    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    isActive = field("isActive")
    description = field("description")

    @cached_property
    def groupingConfiguration(self):  # pragma: no cover
        return GroupingConfigurationOutput.make_one(
            self.boto3_raw_data["groupingConfiguration"]
        )

    shortcutKey = field("shortcutKey")
    lastModifiedBy = field("lastModifiedBy")
    channels = field("channels")
    language = field("language")
    attributesNotInterpolated = field("attributesNotInterpolated")
    attributesInterpolated = field("attributesInterpolated")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QuickResponseSearchResultDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickResponseSearchResultDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuickResponsesRequestPaginate:
    boto3_raw_data: "type_defs.SearchQuickResponsesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def searchExpression(self):  # pragma: no cover
        return QuickResponseSearchExpression.make_one(
            self.boto3_raw_data["searchExpression"]
        )

    attributes = field("attributes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchQuickResponsesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuickResponsesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuickResponsesRequest:
    boto3_raw_data: "type_defs.SearchQuickResponsesRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def searchExpression(self):  # pragma: no cover
        return QuickResponseSearchExpression.make_one(
            self.boto3_raw_data["searchExpression"]
        )

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    attributes = field("attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQuickResponsesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuickResponsesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSessionDataRequest:
    boto3_raw_data: "type_defs.UpdateSessionDataRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    sessionId = field("sessionId")

    @cached_property
    def data(self):  # pragma: no cover
        return RuntimeSessionData.make_many(self.boto3_raw_data["data"])

    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSessionDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSessionDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSessionDataResponse:
    boto3_raw_data: "type_defs.UpdateSessionDataResponseTypeDef" = dataclasses.field()

    sessionArn = field("sessionArn")
    sessionId = field("sessionId")
    namespace = field("namespace")

    @cached_property
    def data(self):  # pragma: no cover
        return RuntimeSessionData.make_many(self.boto3_raw_data["data"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSessionDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSessionDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebCrawlerConfigurationOutput:
    boto3_raw_data: "type_defs.WebCrawlerConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def urlConfiguration(self):  # pragma: no cover
        return UrlConfigurationOutput.make_one(self.boto3_raw_data["urlConfiguration"])

    @cached_property
    def crawlerLimits(self):  # pragma: no cover
        return WebCrawlerLimits.make_one(self.boto3_raw_data["crawlerLimits"])

    inclusionFilters = field("inclusionFilters")
    exclusionFilters = field("exclusionFilters")
    scope = field("scope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WebCrawlerConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebCrawlerConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebCrawlerConfiguration:
    boto3_raw_data: "type_defs.WebCrawlerConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def urlConfiguration(self):  # pragma: no cover
        return UrlConfiguration.make_one(self.boto3_raw_data["urlConfiguration"])

    @cached_property
    def crawlerLimits(self):  # pragma: no cover
        return WebCrawlerLimits.make_one(self.boto3_raw_data["crawlerLimits"])

    inclusionFilters = field("inclusionFilters")
    exclusionFilters = field("exclusionFilters")
    scope = field("scope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebCrawlerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebCrawlerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateAttributesOutput:
    boto3_raw_data: "type_defs.MessageTemplateAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def systemAttributes(self):  # pragma: no cover
        return SystemAttributes.make_one(self.boto3_raw_data["systemAttributes"])

    @cached_property
    def agentAttributes(self):  # pragma: no cover
        return AgentAttributes.make_one(self.boto3_raw_data["agentAttributes"])

    @cached_property
    def customerProfileAttributes(self):  # pragma: no cover
        return CustomerProfileAttributesOutput.make_one(
            self.boto3_raw_data["customerProfileAttributes"]
        )

    customAttributes = field("customAttributes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MessageTemplateAttributesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateAttributes:
    boto3_raw_data: "type_defs.MessageTemplateAttributesTypeDef" = dataclasses.field()

    @cached_property
    def systemAttributes(self):  # pragma: no cover
        return SystemAttributes.make_one(self.boto3_raw_data["systemAttributes"])

    @cached_property
    def agentAttributes(self):  # pragma: no cover
        return AgentAttributes.make_one(self.boto3_raw_data["agentAttributes"])

    @cached_property
    def customerProfileAttributes(self):  # pragma: no cover
        return CustomerProfileAttributes.make_one(
            self.boto3_raw_data["customerProfileAttributes"]
        )

    customAttributes = field("customAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageTemplateAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIGuardrailResponse:
    boto3_raw_data: "type_defs.CreateAIGuardrailResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiGuardrail(self):  # pragma: no cover
        return AIGuardrailData.make_one(self.boto3_raw_data["aiGuardrail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAIGuardrailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIGuardrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIGuardrailVersionResponse:
    boto3_raw_data: "type_defs.CreateAIGuardrailVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aiGuardrail(self):  # pragma: no cover
        return AIGuardrailData.make_one(self.boto3_raw_data["aiGuardrail"])

    versionNumber = field("versionNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAIGuardrailVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIGuardrailVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAIGuardrailResponse:
    boto3_raw_data: "type_defs.GetAIGuardrailResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiGuardrail(self):  # pragma: no cover
        return AIGuardrailData.make_one(self.boto3_raw_data["aiGuardrail"])

    versionNumber = field("versionNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAIGuardrailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAIGuardrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAIGuardrailResponse:
    boto3_raw_data: "type_defs.UpdateAIGuardrailResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiGuardrail(self):  # pragma: no cover
        return AIGuardrailData.make_one(self.boto3_raw_data["aiGuardrail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAIGuardrailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAIGuardrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIGuardrailRequest:
    boto3_raw_data: "type_defs.CreateAIGuardrailRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    name = field("name")
    blockedInputMessaging = field("blockedInputMessaging")
    blockedOutputsMessaging = field("blockedOutputsMessaging")
    visibilityStatus = field("visibilityStatus")
    clientToken = field("clientToken")
    description = field("description")
    topicPolicyConfig = field("topicPolicyConfig")
    contentPolicyConfig = field("contentPolicyConfig")
    wordPolicyConfig = field("wordPolicyConfig")
    sensitiveInformationPolicyConfig = field("sensitiveInformationPolicyConfig")
    contextualGroundingPolicyConfig = field("contextualGroundingPolicyConfig")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAIGuardrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIGuardrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAIGuardrailRequest:
    boto3_raw_data: "type_defs.UpdateAIGuardrailRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiGuardrailId = field("aiGuardrailId")
    visibilityStatus = field("visibilityStatus")
    blockedInputMessaging = field("blockedInputMessaging")
    blockedOutputsMessaging = field("blockedOutputsMessaging")
    clientToken = field("clientToken")
    description = field("description")
    topicPolicyConfig = field("topicPolicyConfig")
    contentPolicyConfig = field("contentPolicyConfig")
    wordPolicyConfig = field("wordPolicyConfig")
    sensitiveInformationPolicyConfig = field("sensitiveInformationPolicyConfig")
    contextualGroundingPolicyConfig = field("contextualGroundingPolicyConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAIGuardrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAIGuardrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIPromptResponse:
    boto3_raw_data: "type_defs.CreateAIPromptResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiPrompt(self):  # pragma: no cover
        return AIPromptData.make_one(self.boto3_raw_data["aiPrompt"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAIPromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIPromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIPromptVersionResponse:
    boto3_raw_data: "type_defs.CreateAIPromptVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aiPrompt(self):  # pragma: no cover
        return AIPromptData.make_one(self.boto3_raw_data["aiPrompt"])

    versionNumber = field("versionNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAIPromptVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIPromptVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAIPromptResponse:
    boto3_raw_data: "type_defs.GetAIPromptResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiPrompt(self):  # pragma: no cover
        return AIPromptData.make_one(self.boto3_raw_data["aiPrompt"])

    versionNumber = field("versionNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAIPromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAIPromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAIPromptResponse:
    boto3_raw_data: "type_defs.UpdateAIPromptResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiPrompt(self):  # pragma: no cover
        return AIPromptData.make_one(self.boto3_raw_data["aiPrompt"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAIPromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAIPromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContentAssociationResponse:
    boto3_raw_data: "type_defs.CreateContentAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def contentAssociation(self):  # pragma: no cover
        return ContentAssociationData.make_one(
            self.boto3_raw_data["contentAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateContentAssociationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContentAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContentAssociationResponse:
    boto3_raw_data: "type_defs.GetContentAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def contentAssociation(self):  # pragma: no cover
        return ContentAssociationData.make_one(
            self.boto3_raw_data["contentAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetContentAssociationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContentAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContentAssociationsResponse:
    boto3_raw_data: "type_defs.ListContentAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def contentAssociationSummaries(self):  # pragma: no cover
        return ContentAssociationSummary.make_many(
            self.boto3_raw_data["contentAssociationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContentAssociationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContentAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssistantAssociationResponse:
    boto3_raw_data: "type_defs.CreateAssistantAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assistantAssociation(self):  # pragma: no cover
        return AssistantAssociationData.make_one(
            self.boto3_raw_data["assistantAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAssistantAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssistantAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssistantAssociationResponse:
    boto3_raw_data: "type_defs.GetAssistantAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assistantAssociation(self):  # pragma: no cover
        return AssistantAssociationData.make_one(
            self.boto3_raw_data["assistantAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAssistantAssociationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssistantAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssistantAssociationsResponse:
    boto3_raw_data: "type_defs.ListAssistantAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assistantAssociationSummaries(self):  # pragma: no cover
        return AssistantAssociationSummary.make_many(
            self.boto3_raw_data["assistantAssociationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssistantAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssistantAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportJobData:
    boto3_raw_data: "type_defs.ImportJobDataTypeDef" = dataclasses.field()

    importJobId = field("importJobId")
    knowledgeBaseId = field("knowledgeBaseId")
    uploadId = field("uploadId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    importJobType = field("importJobType")
    status = field("status")
    url = field("url")
    urlExpiry = field("urlExpiry")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    failedRecordReport = field("failedRecordReport")
    metadata = field("metadata")

    @cached_property
    def externalSourceConfiguration(self):  # pragma: no cover
        return ExternalSourceConfiguration.make_one(
            self.boto3_raw_data["externalSourceConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportJobDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportJobDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportJobSummary:
    boto3_raw_data: "type_defs.ImportJobSummaryTypeDef" = dataclasses.field()

    importJobId = field("importJobId")
    knowledgeBaseId = field("knowledgeBaseId")
    uploadId = field("uploadId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    importJobType = field("importJobType")
    status = field("status")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    metadata = field("metadata")

    @cached_property
    def externalSourceConfiguration(self):  # pragma: no cover
        return ExternalSourceConfiguration.make_one(
            self.boto3_raw_data["externalSourceConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportJobRequest:
    boto3_raw_data: "type_defs.StartImportJobRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    importJobType = field("importJobType")
    uploadId = field("uploadId")
    clientToken = field("clientToken")
    metadata = field("metadata")

    @cached_property
    def externalSourceConfiguration(self):  # pragma: no cover
        return ExternalSourceConfiguration.make_one(
            self.boto3_raw_data["externalSourceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentDataDetails:
    boto3_raw_data: "type_defs.ContentDataDetailsTypeDef" = dataclasses.field()

    @cached_property
    def textData(self):  # pragma: no cover
        return TextData.make_one(self.boto3_raw_data["textData"])

    @cached_property
    def rankingData(self):  # pragma: no cover
        return RankingData.make_one(self.boto3_raw_data["rankingData"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentDataDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentDataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceContentDataDetails:
    boto3_raw_data: "type_defs.SourceContentDataDetailsTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")

    @cached_property
    def textData(self):  # pragma: no cover
        return TextData.make_one(self.boto3_raw_data["textData"])

    @cached_property
    def rankingData(self):  # pragma: no cover
        return RankingData.make_one(self.boto3_raw_data["rankingData"])

    @cached_property
    def citationSpan(self):  # pragma: no cover
        return CitationSpan.make_one(self.boto3_raw_data["citationSpan"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceContentDataDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceContentDataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateContentProviderOutput:
    boto3_raw_data: "type_defs.MessageTemplateContentProviderOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def email(self):  # pragma: no cover
        return EmailMessageTemplateContentOutput.make_one(self.boto3_raw_data["email"])

    @cached_property
    def sms(self):  # pragma: no cover
        return SMSMessageTemplateContent.make_one(self.boto3_raw_data["sms"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MessageTemplateContentProviderOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateContentProviderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateContentProvider:
    boto3_raw_data: "type_defs.MessageTemplateContentProviderTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def email(self):  # pragma: no cover
        return EmailMessageTemplateContent.make_one(self.boto3_raw_data["email"])

    @cached_property
    def sms(self):  # pragma: no cover
        return SMSMessageTemplateContent.make_one(self.boto3_raw_data["sms"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MessageTemplateContentProviderTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateContentProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorIngestionConfigurationOutput:
    boto3_raw_data: "type_defs.VectorIngestionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def chunkingConfiguration(self):  # pragma: no cover
        return ChunkingConfigurationOutput.make_one(
            self.boto3_raw_data["chunkingConfiguration"]
        )

    @cached_property
    def parsingConfiguration(self):  # pragma: no cover
        return ParsingConfiguration.make_one(
            self.boto3_raw_data["parsingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorIngestionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorIngestionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorIngestionConfiguration:
    boto3_raw_data: "type_defs.VectorIngestionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def chunkingConfiguration(self):  # pragma: no cover
        return ChunkingConfiguration.make_one(
            self.boto3_raw_data["chunkingConfiguration"]
        )

    @cached_property
    def parsingConfiguration(self):  # pragma: no cover
        return ParsingConfiguration.make_one(
            self.boto3_raw_data["parsingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VectorIngestionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorIngestionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageRequest:
    boto3_raw_data: "type_defs.SendMessageRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    sessionId = field("sessionId")
    type = field("type")

    @cached_property
    def message(self):  # pragma: no cover
        return MessageInput.make_one(self.boto3_raw_data["message"])

    @cached_property
    def conversationContext(self):  # pragma: no cover
        return ConversationContext.make_one(self.boto3_raw_data["conversationContext"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return MessageConfiguration.make_one(self.boto3_raw_data["configuration"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNextMessageResponse:
    boto3_raw_data: "type_defs.GetNextMessageResponseTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def response(self):  # pragma: no cover
        return MessageOutput.make_one(self.boto3_raw_data["response"])

    requestMessageId = field("requestMessageId")

    @cached_property
    def conversationState(self):  # pragma: no cover
        return ConversationState.make_one(self.boto3_raw_data["conversationState"])

    nextMessageToken = field("nextMessageToken")

    @cached_property
    def conversationSessionData(self):  # pragma: no cover
        return RuntimeSessionData.make_many(
            self.boto3_raw_data["conversationSessionData"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNextMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNextMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessagesResponse:
    boto3_raw_data: "type_defs.ListMessagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return MessageOutput.make_many(self.boto3_raw_data["messages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseAssociationConfigurationDataOutput:
    boto3_raw_data: (
        "type_defs.KnowledgeBaseAssociationConfigurationDataOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def contentTagFilter(self):  # pragma: no cover
        return TagFilterOutput.make_one(self.boto3_raw_data["contentTagFilter"])

    maxResults = field("maxResults")
    overrideKnowledgeBaseSearchType = field("overrideKnowledgeBaseSearchType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseAssociationConfigurationDataOutputTypeDef"
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
                "type_defs.KnowledgeBaseAssociationConfigurationDataOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionData:
    boto3_raw_data: "type_defs.SessionDataTypeDef" = dataclasses.field()

    sessionArn = field("sessionArn")
    sessionId = field("sessionId")
    name = field("name")
    description = field("description")
    tags = field("tags")

    @cached_property
    def integrationConfiguration(self):  # pragma: no cover
        return SessionIntegrationConfiguration.make_one(
            self.boto3_raw_data["integrationConfiguration"]
        )

    @cached_property
    def tagFilter(self):  # pragma: no cover
        return TagFilterOutput.make_one(self.boto3_raw_data["tagFilter"])

    aiAgentConfiguration = field("aiAgentConfiguration")
    origin = field("origin")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseAssociationConfigurationData:
    boto3_raw_data: "type_defs.KnowledgeBaseAssociationConfigurationDataTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def contentTagFilter(self):  # pragma: no cover
        return TagFilter.make_one(self.boto3_raw_data["contentTagFilter"])

    maxResults = field("maxResults")
    overrideKnowledgeBaseSearchType = field("overrideKnowledgeBaseSearchType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseAssociationConfigurationDataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseAssociationConfigurationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQuickResponseResponse:
    boto3_raw_data: "type_defs.CreateQuickResponseResponseTypeDef" = dataclasses.field()

    @cached_property
    def quickResponse(self):  # pragma: no cover
        return QuickResponseData.make_one(self.boto3_raw_data["quickResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQuickResponseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQuickResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQuickResponseResponse:
    boto3_raw_data: "type_defs.GetQuickResponseResponseTypeDef" = dataclasses.field()

    @cached_property
    def quickResponse(self):  # pragma: no cover
        return QuickResponseData.make_one(self.boto3_raw_data["quickResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQuickResponseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQuickResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQuickResponseResponse:
    boto3_raw_data: "type_defs.UpdateQuickResponseResponseTypeDef" = dataclasses.field()

    @cached_property
    def quickResponse(self):  # pragma: no cover
        return QuickResponseData.make_one(self.boto3_raw_data["quickResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQuickResponseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQuickResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuickResponsesResponse:
    boto3_raw_data: "type_defs.SearchQuickResponsesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def results(self):  # pragma: no cover
        return QuickResponseSearchResultData.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQuickResponsesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuickResponsesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedSourceConfigurationOutput:
    boto3_raw_data: "type_defs.ManagedSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def webCrawlerConfiguration(self):  # pragma: no cover
        return WebCrawlerConfigurationOutput.make_one(
            self.boto3_raw_data["webCrawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ManagedSourceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedSourceConfiguration:
    boto3_raw_data: "type_defs.ManagedSourceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def webCrawlerConfiguration(self):  # pragma: no cover
        return WebCrawlerConfiguration.make_one(
            self.boto3_raw_data["webCrawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportJobResponse:
    boto3_raw_data: "type_defs.GetImportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def importJob(self):  # pragma: no cover
        return ImportJobData.make_one(self.boto3_raw_data["importJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportJobResponse:
    boto3_raw_data: "type_defs.StartImportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def importJob(self):  # pragma: no cover
        return ImportJobData.make_one(self.boto3_raw_data["importJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportJobsResponse:
    boto3_raw_data: "type_defs.ListImportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def importJobSummaries(self):  # pragma: no cover
        return ImportJobSummary.make_many(self.boto3_raw_data["importJobSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataDetailsPaginator:
    boto3_raw_data: "type_defs.DataDetailsPaginatorTypeDef" = dataclasses.field()

    @cached_property
    def contentData(self):  # pragma: no cover
        return ContentDataDetails.make_one(self.boto3_raw_data["contentData"])

    @cached_property
    def generativeData(self):  # pragma: no cover
        return GenerativeDataDetailsPaginator.make_one(
            self.boto3_raw_data["generativeData"]
        )

    @cached_property
    def intentDetectedData(self):  # pragma: no cover
        return IntentDetectedDataDetails.make_one(
            self.boto3_raw_data["intentDetectedData"]
        )

    @cached_property
    def sourceContentData(self):  # pragma: no cover
        return SourceContentDataDetails.make_one(
            self.boto3_raw_data["sourceContentData"]
        )

    @cached_property
    def generativeChunkData(self):  # pragma: no cover
        return GenerativeChunkDataDetailsPaginator.make_one(
            self.boto3_raw_data["generativeChunkData"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataDetailsPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataDetailsPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataDetails:
    boto3_raw_data: "type_defs.DataDetailsTypeDef" = dataclasses.field()

    @cached_property
    def contentData(self):  # pragma: no cover
        return ContentDataDetails.make_one(self.boto3_raw_data["contentData"])

    @cached_property
    def generativeData(self):  # pragma: no cover
        return GenerativeDataDetails.make_one(self.boto3_raw_data["generativeData"])

    @cached_property
    def intentDetectedData(self):  # pragma: no cover
        return IntentDetectedDataDetails.make_one(
            self.boto3_raw_data["intentDetectedData"]
        )

    @cached_property
    def sourceContentData(self):  # pragma: no cover
        return SourceContentDataDetails.make_one(
            self.boto3_raw_data["sourceContentData"]
        )

    @cached_property
    def generativeChunkData(self):  # pragma: no cover
        return GenerativeChunkDataDetails.make_one(
            self.boto3_raw_data["generativeChunkData"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendedMessageTemplateData:
    boto3_raw_data: "type_defs.ExtendedMessageTemplateDataTypeDef" = dataclasses.field()

    messageTemplateArn = field("messageTemplateArn")
    messageTemplateId = field("messageTemplateId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    channelSubtype = field("channelSubtype")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    lastModifiedBy = field("lastModifiedBy")

    @cached_property
    def content(self):  # pragma: no cover
        return MessageTemplateContentProviderOutput.make_one(
            self.boto3_raw_data["content"]
        )

    messageTemplateContentSha256 = field("messageTemplateContentSha256")
    description = field("description")
    language = field("language")

    @cached_property
    def groupingConfiguration(self):  # pragma: no cover
        return GroupingConfigurationOutput.make_one(
            self.boto3_raw_data["groupingConfiguration"]
        )

    @cached_property
    def defaultAttributes(self):  # pragma: no cover
        return MessageTemplateAttributesOutput.make_one(
            self.boto3_raw_data["defaultAttributes"]
        )

    attributeTypes = field("attributeTypes")

    @cached_property
    def attachments(self):  # pragma: no cover
        return MessageTemplateAttachment.make_many(self.boto3_raw_data["attachments"])

    isActive = field("isActive")
    versionNumber = field("versionNumber")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtendedMessageTemplateDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtendedMessageTemplateDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateData:
    boto3_raw_data: "type_defs.MessageTemplateDataTypeDef" = dataclasses.field()

    messageTemplateArn = field("messageTemplateArn")
    messageTemplateId = field("messageTemplateId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    channelSubtype = field("channelSubtype")
    createdTime = field("createdTime")
    lastModifiedTime = field("lastModifiedTime")
    lastModifiedBy = field("lastModifiedBy")

    @cached_property
    def content(self):  # pragma: no cover
        return MessageTemplateContentProviderOutput.make_one(
            self.boto3_raw_data["content"]
        )

    messageTemplateContentSha256 = field("messageTemplateContentSha256")
    description = field("description")
    language = field("language")

    @cached_property
    def groupingConfiguration(self):  # pragma: no cover
        return GroupingConfigurationOutput.make_one(
            self.boto3_raw_data["groupingConfiguration"]
        )

    @cached_property
    def defaultAttributes(self):  # pragma: no cover
        return MessageTemplateAttributesOutput.make_one(
            self.boto3_raw_data["defaultAttributes"]
        )

    attributeTypes = field("attributeTypes")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageTemplateDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenderMessageTemplateResponse:
    boto3_raw_data: "type_defs.RenderMessageTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def content(self):  # pragma: no cover
        return MessageTemplateContentProviderOutput.make_one(
            self.boto3_raw_data["content"]
        )

    attributesNotInterpolated = field("attributesNotInterpolated")

    @cached_property
    def attachments(self):  # pragma: no cover
        return MessageTemplateAttachment.make_many(self.boto3_raw_data["attachments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RenderMessageTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenderMessageTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationConfigurationDataOutput:
    boto3_raw_data: "type_defs.AssociationConfigurationDataOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def knowledgeBaseAssociationConfigurationData(self):  # pragma: no cover
        return KnowledgeBaseAssociationConfigurationDataOutput.make_one(
            self.boto3_raw_data["knowledgeBaseAssociationConfigurationData"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociationConfigurationDataOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationConfigurationDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSessionResponse:
    boto3_raw_data: "type_defs.CreateSessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def session(self):  # pragma: no cover
        return SessionData.make_one(self.boto3_raw_data["session"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionResponse:
    boto3_raw_data: "type_defs.GetSessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def session(self):  # pragma: no cover
        return SessionData.make_one(self.boto3_raw_data["session"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSessionResponse:
    boto3_raw_data: "type_defs.UpdateSessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def session(self):  # pragma: no cover
        return SessionData.make_one(self.boto3_raw_data["session"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationConfigurationData:
    boto3_raw_data: "type_defs.AssociationConfigurationDataTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def knowledgeBaseAssociationConfigurationData(self):  # pragma: no cover
        return KnowledgeBaseAssociationConfigurationData.make_one(
            self.boto3_raw_data["knowledgeBaseAssociationConfigurationData"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationConfigurationDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationConfigurationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSessionRequest:
    boto3_raw_data: "type_defs.CreateSessionRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")
    tags = field("tags")
    tagFilter = field("tagFilter")
    aiAgentConfiguration = field("aiAgentConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSessionRequest:
    boto3_raw_data: "type_defs.UpdateSessionRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    sessionId = field("sessionId")
    description = field("description")
    tagFilter = field("tagFilter")
    aiAgentConfiguration = field("aiAgentConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfigurationOutput:
    boto3_raw_data: "type_defs.SourceConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def appIntegrations(self):  # pragma: no cover
        return AppIntegrationsConfigurationOutput.make_one(
            self.boto3_raw_data["appIntegrations"]
        )

    @cached_property
    def managedSourceConfiguration(self):  # pragma: no cover
        return ManagedSourceConfigurationOutput.make_one(
            self.boto3_raw_data["managedSourceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfiguration:
    boto3_raw_data: "type_defs.SourceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def appIntegrations(self):  # pragma: no cover
        return AppIntegrationsConfiguration.make_one(
            self.boto3_raw_data["appIntegrations"]
        )

    @cached_property
    def managedSourceConfiguration(self):  # pragma: no cover
        return ManagedSourceConfiguration.make_one(
            self.boto3_raw_data["managedSourceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenderMessageTemplateRequest:
    boto3_raw_data: "type_defs.RenderMessageTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")
    attributes = field("attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RenderMessageTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenderMessageTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSummaryPaginator:
    boto3_raw_data: "type_defs.DataSummaryPaginatorTypeDef" = dataclasses.field()

    @cached_property
    def reference(self):  # pragma: no cover
        return DataReference.make_one(self.boto3_raw_data["reference"])

    @cached_property
    def details(self):  # pragma: no cover
        return DataDetailsPaginator.make_one(self.boto3_raw_data["details"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSummaryPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSummaryPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSummary:
    boto3_raw_data: "type_defs.DataSummaryTypeDef" = dataclasses.field()

    @cached_property
    def reference(self):  # pragma: no cover
        return DataReference.make_one(self.boto3_raw_data["reference"])

    @cached_property
    def details(self):  # pragma: no cover
        return DataDetails.make_one(self.boto3_raw_data["details"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMessageTemplateVersionResponse:
    boto3_raw_data: "type_defs.CreateMessageTemplateVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def messageTemplate(self):  # pragma: no cover
        return ExtendedMessageTemplateData.make_one(
            self.boto3_raw_data["messageTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMessageTemplateVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMessageTemplateVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMessageTemplateResponse:
    boto3_raw_data: "type_defs.GetMessageTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def messageTemplate(self):  # pragma: no cover
        return ExtendedMessageTemplateData.make_one(
            self.boto3_raw_data["messageTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMessageTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMessageTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMessageTemplateResponse:
    boto3_raw_data: "type_defs.CreateMessageTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def messageTemplate(self):  # pragma: no cover
        return MessageTemplateData.make_one(self.boto3_raw_data["messageTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMessageTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMessageTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMessageTemplateMetadataResponse:
    boto3_raw_data: "type_defs.UpdateMessageTemplateMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def messageTemplate(self):  # pragma: no cover
        return MessageTemplateData.make_one(self.boto3_raw_data["messageTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMessageTemplateMetadataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMessageTemplateMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMessageTemplateResponse:
    boto3_raw_data: "type_defs.UpdateMessageTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def messageTemplate(self):  # pragma: no cover
        return MessageTemplateData.make_one(self.boto3_raw_data["messageTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMessageTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMessageTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMessageTemplateRequest:
    boto3_raw_data: "type_defs.CreateMessageTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    content = field("content")
    channelSubtype = field("channelSubtype")
    description = field("description")
    language = field("language")
    defaultAttributes = field("defaultAttributes")
    groupingConfiguration = field("groupingConfiguration")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMessageTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMessageTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMessageTemplateRequest:
    boto3_raw_data: "type_defs.UpdateMessageTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    messageTemplateId = field("messageTemplateId")
    content = field("content")
    language = field("language")
    defaultAttributes = field("defaultAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMessageTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMessageTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationConfigurationOutput:
    boto3_raw_data: "type_defs.AssociationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    associationId = field("associationId")
    associationType = field("associationType")

    @cached_property
    def associationConfigurationData(self):  # pragma: no cover
        return AssociationConfigurationDataOutput.make_one(
            self.boto3_raw_data["associationConfigurationData"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociationConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationConfiguration:
    boto3_raw_data: "type_defs.AssociationConfigurationTypeDef" = dataclasses.field()

    associationId = field("associationId")
    associationType = field("associationType")

    @cached_property
    def associationConfigurationData(self):  # pragma: no cover
        return AssociationConfigurationData.make_one(
            self.boto3_raw_data["associationConfigurationData"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseData:
    boto3_raw_data: "type_defs.KnowledgeBaseDataTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    name = field("name")
    knowledgeBaseType = field("knowledgeBaseType")
    status = field("status")
    lastContentModificationTime = field("lastContentModificationTime")

    @cached_property
    def vectorIngestionConfiguration(self):  # pragma: no cover
        return VectorIngestionConfigurationOutput.make_one(
            self.boto3_raw_data["vectorIngestionConfiguration"]
        )

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return SourceConfigurationOutput.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def renderingConfiguration(self):  # pragma: no cover
        return RenderingConfiguration.make_one(
            self.boto3_raw_data["renderingConfiguration"]
        )

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    description = field("description")
    tags = field("tags")
    ingestionStatus = field("ingestionStatus")
    ingestionFailureReasons = field("ingestionFailureReasons")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseSummary:
    boto3_raw_data: "type_defs.KnowledgeBaseSummaryTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    name = field("name")
    knowledgeBaseType = field("knowledgeBaseType")
    status = field("status")

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return SourceConfigurationOutput.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def vectorIngestionConfiguration(self):  # pragma: no cover
        return VectorIngestionConfigurationOutput.make_one(
            self.boto3_raw_data["vectorIngestionConfiguration"]
        )

    @cached_property
    def renderingConfiguration(self):  # pragma: no cover
        return RenderingConfiguration.make_one(
            self.boto3_raw_data["renderingConfiguration"]
        )

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultDataPaginator:
    boto3_raw_data: "type_defs.ResultDataPaginatorTypeDef" = dataclasses.field()

    resultId = field("resultId")

    @cached_property
    def document(self):  # pragma: no cover
        return Document.make_one(self.boto3_raw_data["document"])

    relevanceScore = field("relevanceScore")

    @cached_property
    def data(self):  # pragma: no cover
        return DataSummaryPaginator.make_one(self.boto3_raw_data["data"])

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResultDataPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResultDataPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationData:
    boto3_raw_data: "type_defs.RecommendationDataTypeDef" = dataclasses.field()

    recommendationId = field("recommendationId")

    @cached_property
    def document(self):  # pragma: no cover
        return Document.make_one(self.boto3_raw_data["document"])

    relevanceScore = field("relevanceScore")
    relevanceLevel = field("relevanceLevel")
    type = field("type")

    @cached_property
    def data(self):  # pragma: no cover
        return DataSummary.make_one(self.boto3_raw_data["data"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultData:
    boto3_raw_data: "type_defs.ResultDataTypeDef" = dataclasses.field()

    resultId = field("resultId")

    @cached_property
    def document(self):  # pragma: no cover
        return Document.make_one(self.boto3_raw_data["document"])

    relevanceScore = field("relevanceScore")

    @cached_property
    def data(self):  # pragma: no cover
        return DataSummary.make_one(self.boto3_raw_data["data"])

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnswerRecommendationAIAgentConfigurationOutput:
    boto3_raw_data: (
        "type_defs.AnswerRecommendationAIAgentConfigurationOutputTypeDef"
    ) = dataclasses.field()

    intentLabelingGenerationAIPromptId = field("intentLabelingGenerationAIPromptId")
    queryReformulationAIPromptId = field("queryReformulationAIPromptId")
    answerGenerationAIPromptId = field("answerGenerationAIPromptId")
    answerGenerationAIGuardrailId = field("answerGenerationAIGuardrailId")

    @cached_property
    def associationConfigurations(self):  # pragma: no cover
        return AssociationConfigurationOutput.make_many(
            self.boto3_raw_data["associationConfigurations"]
        )

    locale = field("locale")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnswerRecommendationAIAgentConfigurationOutputTypeDef"
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
                "type_defs.AnswerRecommendationAIAgentConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManualSearchAIAgentConfigurationOutput:
    boto3_raw_data: "type_defs.ManualSearchAIAgentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    answerGenerationAIPromptId = field("answerGenerationAIPromptId")
    answerGenerationAIGuardrailId = field("answerGenerationAIGuardrailId")

    @cached_property
    def associationConfigurations(self):  # pragma: no cover
        return AssociationConfigurationOutput.make_many(
            self.boto3_raw_data["associationConfigurations"]
        )

    locale = field("locale")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManualSearchAIAgentConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManualSearchAIAgentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfServiceAIAgentConfigurationOutput:
    boto3_raw_data: "type_defs.SelfServiceAIAgentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    selfServicePreProcessingAIPromptId = field("selfServicePreProcessingAIPromptId")
    selfServiceAnswerGenerationAIPromptId = field(
        "selfServiceAnswerGenerationAIPromptId"
    )
    selfServiceAIGuardrailId = field("selfServiceAIGuardrailId")

    @cached_property
    def associationConfigurations(self):  # pragma: no cover
        return AssociationConfigurationOutput.make_many(
            self.boto3_raw_data["associationConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelfServiceAIAgentConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfServiceAIAgentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnswerRecommendationAIAgentConfiguration:
    boto3_raw_data: "type_defs.AnswerRecommendationAIAgentConfigurationTypeDef" = (
        dataclasses.field()
    )

    intentLabelingGenerationAIPromptId = field("intentLabelingGenerationAIPromptId")
    queryReformulationAIPromptId = field("queryReformulationAIPromptId")
    answerGenerationAIPromptId = field("answerGenerationAIPromptId")
    answerGenerationAIGuardrailId = field("answerGenerationAIGuardrailId")

    @cached_property
    def associationConfigurations(self):  # pragma: no cover
        return AssociationConfiguration.make_many(
            self.boto3_raw_data["associationConfigurations"]
        )

    locale = field("locale")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnswerRecommendationAIAgentConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnswerRecommendationAIAgentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManualSearchAIAgentConfiguration:
    boto3_raw_data: "type_defs.ManualSearchAIAgentConfigurationTypeDef" = (
        dataclasses.field()
    )

    answerGenerationAIPromptId = field("answerGenerationAIPromptId")
    answerGenerationAIGuardrailId = field("answerGenerationAIGuardrailId")

    @cached_property
    def associationConfigurations(self):  # pragma: no cover
        return AssociationConfiguration.make_many(
            self.boto3_raw_data["associationConfigurations"]
        )

    locale = field("locale")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ManualSearchAIAgentConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManualSearchAIAgentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfServiceAIAgentConfiguration:
    boto3_raw_data: "type_defs.SelfServiceAIAgentConfigurationTypeDef" = (
        dataclasses.field()
    )

    selfServicePreProcessingAIPromptId = field("selfServicePreProcessingAIPromptId")
    selfServiceAnswerGenerationAIPromptId = field(
        "selfServiceAnswerGenerationAIPromptId"
    )
    selfServiceAIGuardrailId = field("selfServiceAIGuardrailId")

    @cached_property
    def associationConfigurations(self):  # pragma: no cover
        return AssociationConfiguration.make_many(
            self.boto3_raw_data["associationConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SelfServiceAIAgentConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfServiceAIAgentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKnowledgeBaseResponse:
    boto3_raw_data: "type_defs.CreateKnowledgeBaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def knowledgeBase(self):  # pragma: no cover
        return KnowledgeBaseData.make_one(self.boto3_raw_data["knowledgeBase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKnowledgeBaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKnowledgeBaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKnowledgeBaseResponse:
    boto3_raw_data: "type_defs.GetKnowledgeBaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def knowledgeBase(self):  # pragma: no cover
        return KnowledgeBaseData.make_one(self.boto3_raw_data["knowledgeBase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKnowledgeBaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKnowledgeBaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKnowledgeBaseTemplateUriResponse:
    boto3_raw_data: "type_defs.UpdateKnowledgeBaseTemplateUriResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def knowledgeBase(self):  # pragma: no cover
        return KnowledgeBaseData.make_one(self.boto3_raw_data["knowledgeBase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateKnowledgeBaseTemplateUriResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKnowledgeBaseTemplateUriResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKnowledgeBasesResponse:
    boto3_raw_data: "type_defs.ListKnowledgeBasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def knowledgeBaseSummaries(self):  # pragma: no cover
        return KnowledgeBaseSummary.make_many(
            self.boto3_raw_data["knowledgeBaseSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKnowledgeBasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKnowledgeBasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.CreateKnowledgeBaseRequestTypeDef" = dataclasses.field()

    name = field("name")
    knowledgeBaseType = field("knowledgeBaseType")
    clientToken = field("clientToken")
    sourceConfiguration = field("sourceConfiguration")

    @cached_property
    def renderingConfiguration(self):  # pragma: no cover
        return RenderingConfiguration.make_one(
            self.boto3_raw_data["renderingConfiguration"]
        )

    vectorIngestionConfiguration = field("vectorIngestionConfiguration")

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKnowledgeBaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryAssistantResponsePaginator:
    boto3_raw_data: "type_defs.QueryAssistantResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def results(self):  # pragma: no cover
        return ResultDataPaginator.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QueryAssistantResponsePaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryAssistantResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationsResponse:
    boto3_raw_data: "type_defs.GetRecommendationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def recommendations(self):  # pragma: no cover
        return RecommendationData.make_many(self.boto3_raw_data["recommendations"])

    @cached_property
    def triggers(self):  # pragma: no cover
        return RecommendationTrigger.make_many(self.boto3_raw_data["triggers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryAssistantResponse:
    boto3_raw_data: "type_defs.QueryAssistantResponseTypeDef" = dataclasses.field()

    @cached_property
    def results(self):  # pragma: no cover
        return ResultData.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryAssistantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryAssistantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIAgentConfigurationOutput:
    boto3_raw_data: "type_defs.AIAgentConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def manualSearchAIAgentConfiguration(self):  # pragma: no cover
        return ManualSearchAIAgentConfigurationOutput.make_one(
            self.boto3_raw_data["manualSearchAIAgentConfiguration"]
        )

    @cached_property
    def answerRecommendationAIAgentConfiguration(self):  # pragma: no cover
        return AnswerRecommendationAIAgentConfigurationOutput.make_one(
            self.boto3_raw_data["answerRecommendationAIAgentConfiguration"]
        )

    @cached_property
    def selfServiceAIAgentConfiguration(self):  # pragma: no cover
        return SelfServiceAIAgentConfigurationOutput.make_one(
            self.boto3_raw_data["selfServiceAIAgentConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AIAgentConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIAgentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIAgentConfiguration:
    boto3_raw_data: "type_defs.AIAgentConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def manualSearchAIAgentConfiguration(self):  # pragma: no cover
        return ManualSearchAIAgentConfiguration.make_one(
            self.boto3_raw_data["manualSearchAIAgentConfiguration"]
        )

    @cached_property
    def answerRecommendationAIAgentConfiguration(self):  # pragma: no cover
        return AnswerRecommendationAIAgentConfiguration.make_one(
            self.boto3_raw_data["answerRecommendationAIAgentConfiguration"]
        )

    @cached_property
    def selfServiceAIAgentConfiguration(self):  # pragma: no cover
        return SelfServiceAIAgentConfiguration.make_one(
            self.boto3_raw_data["selfServiceAIAgentConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AIAgentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIAgentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIAgentData:
    boto3_raw_data: "type_defs.AIAgentDataTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    aiAgentId = field("aiAgentId")
    aiAgentArn = field("aiAgentArn")
    name = field("name")
    type = field("type")

    @cached_property
    def configuration(self):  # pragma: no cover
        return AIAgentConfigurationOutput.make_one(self.boto3_raw_data["configuration"])

    visibilityStatus = field("visibilityStatus")
    modifiedTime = field("modifiedTime")
    description = field("description")
    tags = field("tags")
    origin = field("origin")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AIAgentDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AIAgentDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIAgentSummary:
    boto3_raw_data: "type_defs.AIAgentSummaryTypeDef" = dataclasses.field()

    name = field("name")
    assistantId = field("assistantId")
    assistantArn = field("assistantArn")
    aiAgentId = field("aiAgentId")
    type = field("type")
    aiAgentArn = field("aiAgentArn")
    visibilityStatus = field("visibilityStatus")
    modifiedTime = field("modifiedTime")

    @cached_property
    def configuration(self):  # pragma: no cover
        return AIAgentConfigurationOutput.make_one(self.boto3_raw_data["configuration"])

    origin = field("origin")
    description = field("description")
    status = field("status")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AIAgentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AIAgentSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIAgentResponse:
    boto3_raw_data: "type_defs.CreateAIAgentResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiAgent(self):  # pragma: no cover
        return AIAgentData.make_one(self.boto3_raw_data["aiAgent"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAIAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIAgentVersionResponse:
    boto3_raw_data: "type_defs.CreateAIAgentVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aiAgent(self):  # pragma: no cover
        return AIAgentData.make_one(self.boto3_raw_data["aiAgent"])

    versionNumber = field("versionNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAIAgentVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIAgentVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAIAgentResponse:
    boto3_raw_data: "type_defs.GetAIAgentResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiAgent(self):  # pragma: no cover
        return AIAgentData.make_one(self.boto3_raw_data["aiAgent"])

    versionNumber = field("versionNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAIAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAIAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAIAgentResponse:
    boto3_raw_data: "type_defs.UpdateAIAgentResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiAgent(self):  # pragma: no cover
        return AIAgentData.make_one(self.boto3_raw_data["aiAgent"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAIAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAIAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIAgentVersionSummary:
    boto3_raw_data: "type_defs.AIAgentVersionSummaryTypeDef" = dataclasses.field()

    @cached_property
    def aiAgentSummary(self):  # pragma: no cover
        return AIAgentSummary.make_one(self.boto3_raw_data["aiAgentSummary"])

    versionNumber = field("versionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AIAgentVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIAgentVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIAgentsResponse:
    boto3_raw_data: "type_defs.ListAIAgentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiAgentSummaries(self):  # pragma: no cover
        return AIAgentSummary.make_many(self.boto3_raw_data["aiAgentSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIAgentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIAgentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAIAgentRequest:
    boto3_raw_data: "type_defs.CreateAIAgentRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    name = field("name")
    type = field("type")
    configuration = field("configuration")
    visibilityStatus = field("visibilityStatus")
    clientToken = field("clientToken")
    tags = field("tags")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAIAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAIAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAIAgentRequest:
    boto3_raw_data: "type_defs.UpdateAIAgentRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    aiAgentId = field("aiAgentId")
    visibilityStatus = field("visibilityStatus")
    clientToken = field("clientToken")
    configuration = field("configuration")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAIAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAIAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAIAgentVersionsResponse:
    boto3_raw_data: "type_defs.ListAIAgentVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def aiAgentVersionSummaries(self):  # pragma: no cover
        return AIAgentVersionSummary.make_many(
            self.boto3_raw_data["aiAgentVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAIAgentVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAIAgentVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
