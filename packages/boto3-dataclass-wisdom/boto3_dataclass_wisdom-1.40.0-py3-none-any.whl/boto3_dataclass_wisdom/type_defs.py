# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_wisdom import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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

    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")

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
class ContentData:
    boto3_raw_data: "type_defs.ContentDataTypeDef" = dataclasses.field()

    contentArn = field("contentArn")
    contentId = field("contentId")
    contentType = field("contentType")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    metadata = field("metadata")
    name = field("name")
    revisionId = field("revisionId")
    status = field("status")
    title = field("title")
    url = field("url")
    urlExpiry = field("urlExpiry")
    linkOutUri = field("linkOutUri")
    tags = field("tags")

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
class ContentReference:
    boto3_raw_data: "type_defs.ContentReferenceTypeDef" = dataclasses.field()

    contentArn = field("contentArn")
    contentId = field("contentId")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")

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
    contentType = field("contentType")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    metadata = field("metadata")
    name = field("name")
    revisionId = field("revisionId")
    status = field("status")
    title = field("title")
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
class CreateContentRequest:
    boto3_raw_data: "type_defs.CreateContentRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    uploadId = field("uploadId")
    clientToken = field("clientToken")
    metadata = field("metadata")
    overrideLinkOutUri = field("overrideLinkOutUri")
    tags = field("tags")
    title = field("title")

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
class CreateSessionRequest:
    boto3_raw_data: "type_defs.CreateSessionRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")
    tags = field("tags")

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
class DeleteContentRequest:
    boto3_raw_data: "type_defs.DeleteContentRequestTypeDef" = dataclasses.field()

    contentId = field("contentId")
    knowledgeBaseId = field("knowledgeBaseId")

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

    importJobId = field("importJobId")
    knowledgeBaseId = field("knowledgeBaseId")

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
class GetQuickResponseRequest:
    boto3_raw_data: "type_defs.GetQuickResponseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    quickResponseId = field("quickResponseId")

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
class ListAssistantAssociationsRequest:
    boto3_raw_data: "type_defs.ListAssistantAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

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

    maxResults = field("maxResults")
    nextToken = field("nextToken")

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
class ListContentsRequest:
    boto3_raw_data: "type_defs.ListContentsRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

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
    maxResults = field("maxResults")
    nextToken = field("nextToken")

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

    maxResults = field("maxResults")
    nextToken = field("nextToken")

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
class ListQuickResponsesRequest:
    boto3_raw_data: "type_defs.ListQuickResponsesRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

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

    contentType = field("contentType")
    createdTime = field("createdTime")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    lastModifiedTime = field("lastModifiedTime")
    name = field("name")
    quickResponseArn = field("quickResponseArn")
    quickResponseId = field("quickResponseId")
    status = field("status")
    channels = field("channels")
    description = field("description")
    isActive = field("isActive")
    lastModifiedBy = field("lastModifiedBy")
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
class NotifyRecommendationsReceivedError:
    boto3_raw_data: "type_defs.NotifyRecommendationsReceivedErrorTypeDef" = (
        dataclasses.field()
    )

    message = field("message")
    recommendationId = field("recommendationId")

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
    recommendationIds = field("recommendationIds")
    sessionId = field("sessionId")

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
class QueryAssistantRequest:
    boto3_raw_data: "type_defs.QueryAssistantRequestTypeDef" = dataclasses.field()

    assistantId = field("assistantId")
    queryText = field("queryText")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

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
    includeNoExistence = field("includeNoExistence")
    values = field("values")

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
    operator = field("operator")
    values = field("values")
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
class SessionSummary:
    boto3_raw_data: "type_defs.SessionSummaryTypeDef" = dataclasses.field()

    assistantArn = field("assistantArn")
    assistantId = field("assistantId")
    sessionArn = field("sessionArn")
    sessionId = field("sessionId")

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

    contentType = field("contentType")
    knowledgeBaseId = field("knowledgeBaseId")
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

    contentId = field("contentId")
    knowledgeBaseId = field("knowledgeBaseId")
    metadata = field("metadata")
    overrideLinkOutUri = field("overrideLinkOutUri")
    removeOverrideLinkOutUri = field("removeOverrideLinkOutUri")
    revisionId = field("revisionId")
    title = field("title")
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
class SourceConfigurationOutput:
    boto3_raw_data: "type_defs.SourceConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def appIntegrations(self):  # pragma: no cover
        return AppIntegrationsConfigurationOutput.make_one(
            self.boto3_raw_data["appIntegrations"]
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
class CreateAssistantAssociationRequest:
    boto3_raw_data: "type_defs.CreateAssistantAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")

    @cached_property
    def association(self):  # pragma: no cover
        return AssistantAssociationInputData.make_one(
            self.boto3_raw_data["association"]
        )

    associationType = field("associationType")
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

    assistantArn = field("assistantArn")
    assistantId = field("assistantId")
    name = field("name")
    status = field("status")
    type = field("type")
    description = field("description")

    @cached_property
    def integrationConfiguration(self):  # pragma: no cover
        return AssistantIntegrationConfiguration.make_one(
            self.boto3_raw_data["integrationConfiguration"]
        )

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    tags = field("tags")

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

    assistantArn = field("assistantArn")
    assistantId = field("assistantId")
    name = field("name")
    status = field("status")
    type = field("type")
    description = field("description")

    @cached_property
    def integrationConfiguration(self):  # pragma: no cover
        return AssistantIntegrationConfiguration.make_one(
            self.boto3_raw_data["integrationConfiguration"]
        )

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    tags = field("tags")

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

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    tags = field("tags")

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
class StartContentUploadResponse:
    boto3_raw_data: "type_defs.StartContentUploadResponseTypeDef" = dataclasses.field()

    headersToInclude = field("headersToInclude")
    uploadId = field("uploadId")
    url = field("url")
    urlExpiry = field("urlExpiry")

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
class DocumentText:
    boto3_raw_data: "type_defs.DocumentTextTypeDef" = dataclasses.field()

    @cached_property
    def highlights(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["highlights"])

    text = field("text")

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
class QueryAssistantRequestPaginate:
    boto3_raw_data: "type_defs.QueryAssistantRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    assistantId = field("assistantId")
    queryText = field("queryText")

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
class NotifyRecommendationsReceivedResponse:
    boto3_raw_data: "type_defs.NotifyRecommendationsReceivedResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return NotifyRecommendationsReceivedError.make_many(
            self.boto3_raw_data["errors"]
        )

    recommendationIds = field("recommendationIds")

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
    def markdown(self):  # pragma: no cover
        return QuickResponseContentProvider.make_one(self.boto3_raw_data["markdown"])

    @cached_property
    def plainText(self):  # pragma: no cover
        return QuickResponseContentProvider.make_one(self.boto3_raw_data["plainText"])

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
    def filters(self):  # pragma: no cover
        return QuickResponseFilterField.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def orderOnField(self):  # pragma: no cover
        return QuickResponseOrderField.make_one(self.boto3_raw_data["orderOnField"])

    @cached_property
    def queries(self):  # pragma: no cover
        return QuickResponseQueryField.make_many(self.boto3_raw_data["queries"])

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
class SessionData:
    boto3_raw_data: "type_defs.SessionDataTypeDef" = dataclasses.field()

    name = field("name")
    sessionArn = field("sessionArn")
    sessionId = field("sessionId")
    description = field("description")

    @cached_property
    def integrationConfiguration(self):  # pragma: no cover
        return SessionIntegrationConfiguration.make_one(
            self.boto3_raw_data["integrationConfiguration"]
        )

    tags = field("tags")

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
class KnowledgeBaseData:
    boto3_raw_data: "type_defs.KnowledgeBaseDataTypeDef" = dataclasses.field()

    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    knowledgeBaseType = field("knowledgeBaseType")
    name = field("name")
    status = field("status")
    description = field("description")
    lastContentModificationTime = field("lastContentModificationTime")

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

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return SourceConfigurationOutput.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    tags = field("tags")

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

    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    knowledgeBaseType = field("knowledgeBaseType")
    name = field("name")
    status = field("status")
    description = field("description")

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

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return SourceConfigurationOutput.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

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
class AssistantAssociationData:
    boto3_raw_data: "type_defs.AssistantAssociationDataTypeDef" = dataclasses.field()

    assistantArn = field("assistantArn")
    assistantAssociationArn = field("assistantAssociationArn")
    assistantAssociationId = field("assistantAssociationId")
    assistantId = field("assistantId")

    @cached_property
    def associationData(self):  # pragma: no cover
        return AssistantAssociationOutputData.make_one(
            self.boto3_raw_data["associationData"]
        )

    associationType = field("associationType")
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

    assistantArn = field("assistantArn")
    assistantAssociationArn = field("assistantAssociationArn")
    assistantAssociationId = field("assistantAssociationId")
    assistantId = field("assistantId")

    @cached_property
    def associationData(self):  # pragma: no cover
        return AssistantAssociationOutputData.make_one(
            self.boto3_raw_data["associationData"]
        )

    associationType = field("associationType")
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
class ExternalSourceConfiguration:
    boto3_raw_data: "type_defs.ExternalSourceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return Configuration.make_one(self.boto3_raw_data["configuration"])

    source = field("source")

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
class Document:
    boto3_raw_data: "type_defs.DocumentTypeDef" = dataclasses.field()

    @cached_property
    def contentReference(self):  # pragma: no cover
        return ContentReference.make_one(self.boto3_raw_data["contentReference"])

    @cached_property
    def excerpt(self):  # pragma: no cover
        return DocumentText.make_one(self.boto3_raw_data["excerpt"])

    @cached_property
    def title(self):  # pragma: no cover
        return DocumentText.make_one(self.boto3_raw_data["title"])

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

    maxResults = field("maxResults")
    nextToken = field("nextToken")

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

    maxResults = field("maxResults")
    nextToken = field("nextToken")

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

    @cached_property
    def content(self):  # pragma: no cover
        return QuickResponseDataProvider.make_one(self.boto3_raw_data["content"])

    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    channels = field("channels")
    clientToken = field("clientToken")
    contentType = field("contentType")
    description = field("description")
    groupingConfiguration = field("groupingConfiguration")
    isActive = field("isActive")
    language = field("language")
    shortcutKey = field("shortcutKey")
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
class UpdateQuickResponseRequest:
    boto3_raw_data: "type_defs.UpdateQuickResponseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    quickResponseId = field("quickResponseId")
    channels = field("channels")

    @cached_property
    def content(self):  # pragma: no cover
        return QuickResponseDataProvider.make_one(self.boto3_raw_data["content"])

    contentType = field("contentType")
    description = field("description")
    groupingConfiguration = field("groupingConfiguration")
    isActive = field("isActive")
    language = field("language")
    name = field("name")
    removeDescription = field("removeDescription")
    removeGroupingConfiguration = field("removeGroupingConfiguration")
    removeShortcutKey = field("removeShortcutKey")
    shortcutKey = field("shortcutKey")

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
class RecommendationTrigger:
    boto3_raw_data: "type_defs.RecommendationTriggerTypeDef" = dataclasses.field()

    @cached_property
    def data(self):  # pragma: no cover
        return RecommendationTriggerData.make_one(self.boto3_raw_data["data"])

    id = field("id")
    recommendationIds = field("recommendationIds")
    source = field("source")
    type = field("type")

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

    contentType = field("contentType")
    createdTime = field("createdTime")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    lastModifiedTime = field("lastModifiedTime")
    name = field("name")
    quickResponseArn = field("quickResponseArn")
    quickResponseId = field("quickResponseId")
    status = field("status")
    channels = field("channels")

    @cached_property
    def contents(self):  # pragma: no cover
        return QuickResponseContents.make_one(self.boto3_raw_data["contents"])

    description = field("description")

    @cached_property
    def groupingConfiguration(self):  # pragma: no cover
        return GroupingConfigurationOutput.make_one(
            self.boto3_raw_data["groupingConfiguration"]
        )

    isActive = field("isActive")
    language = field("language")
    lastModifiedBy = field("lastModifiedBy")
    shortcutKey = field("shortcutKey")
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

    contentType = field("contentType")

    @cached_property
    def contents(self):  # pragma: no cover
        return QuickResponseContents.make_one(self.boto3_raw_data["contents"])

    createdTime = field("createdTime")
    isActive = field("isActive")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    lastModifiedTime = field("lastModifiedTime")
    name = field("name")
    quickResponseArn = field("quickResponseArn")
    quickResponseId = field("quickResponseId")
    status = field("status")
    attributesInterpolated = field("attributesInterpolated")
    attributesNotInterpolated = field("attributesNotInterpolated")
    channels = field("channels")
    description = field("description")

    @cached_property
    def groupingConfiguration(self):  # pragma: no cover
        return GroupingConfigurationOutput.make_one(
            self.boto3_raw_data["groupingConfiguration"]
        )

    language = field("language")
    lastModifiedBy = field("lastModifiedBy")
    shortcutKey = field("shortcutKey")
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

    attributes = field("attributes")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

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

    knowledgeBaseType = field("knowledgeBaseType")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")

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

    sourceConfiguration = field("sourceConfiguration")
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

    createdTime = field("createdTime")
    importJobId = field("importJobId")
    importJobType = field("importJobType")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    lastModifiedTime = field("lastModifiedTime")
    status = field("status")
    uploadId = field("uploadId")
    url = field("url")
    urlExpiry = field("urlExpiry")

    @cached_property
    def externalSourceConfiguration(self):  # pragma: no cover
        return ExternalSourceConfiguration.make_one(
            self.boto3_raw_data["externalSourceConfiguration"]
        )

    failedRecordReport = field("failedRecordReport")
    metadata = field("metadata")

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

    createdTime = field("createdTime")
    importJobId = field("importJobId")
    importJobType = field("importJobType")
    knowledgeBaseArn = field("knowledgeBaseArn")
    knowledgeBaseId = field("knowledgeBaseId")
    lastModifiedTime = field("lastModifiedTime")
    status = field("status")
    uploadId = field("uploadId")

    @cached_property
    def externalSourceConfiguration(self):  # pragma: no cover
        return ExternalSourceConfiguration.make_one(
            self.boto3_raw_data["externalSourceConfiguration"]
        )

    metadata = field("metadata")

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

    importJobType = field("importJobType")
    knowledgeBaseId = field("knowledgeBaseId")
    uploadId = field("uploadId")
    clientToken = field("clientToken")

    @cached_property
    def externalSourceConfiguration(self):  # pragma: no cover
        return ExternalSourceConfiguration.make_one(
            self.boto3_raw_data["externalSourceConfiguration"]
        )

    metadata = field("metadata")

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
class RecommendationData:
    boto3_raw_data: "type_defs.RecommendationDataTypeDef" = dataclasses.field()

    @cached_property
    def document(self):  # pragma: no cover
        return Document.make_one(self.boto3_raw_data["document"])

    recommendationId = field("recommendationId")
    relevanceLevel = field("relevanceLevel")
    relevanceScore = field("relevanceScore")
    type = field("type")

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

    @cached_property
    def document(self):  # pragma: no cover
        return Document.make_one(self.boto3_raw_data["document"])

    resultId = field("resultId")
    relevanceScore = field("relevanceScore")

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
