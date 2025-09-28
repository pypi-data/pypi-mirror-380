# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_qconnect import type_defs as bs_td


class QCONNECTCaster:

    def activate_message_template(
        self,
        res: "bs_td.ActivateMessageTemplateResponseTypeDef",
    ) -> "dc_td.ActivateMessageTemplateResponse":
        return dc_td.ActivateMessageTemplateResponse.make_one(res)

    def create_ai_agent(
        self,
        res: "bs_td.CreateAIAgentResponseTypeDef",
    ) -> "dc_td.CreateAIAgentResponse":
        return dc_td.CreateAIAgentResponse.make_one(res)

    def create_ai_agent_version(
        self,
        res: "bs_td.CreateAIAgentVersionResponseTypeDef",
    ) -> "dc_td.CreateAIAgentVersionResponse":
        return dc_td.CreateAIAgentVersionResponse.make_one(res)

    def create_ai_guardrail(
        self,
        res: "bs_td.CreateAIGuardrailResponseTypeDef",
    ) -> "dc_td.CreateAIGuardrailResponse":
        return dc_td.CreateAIGuardrailResponse.make_one(res)

    def create_ai_guardrail_version(
        self,
        res: "bs_td.CreateAIGuardrailVersionResponseTypeDef",
    ) -> "dc_td.CreateAIGuardrailVersionResponse":
        return dc_td.CreateAIGuardrailVersionResponse.make_one(res)

    def create_ai_prompt(
        self,
        res: "bs_td.CreateAIPromptResponseTypeDef",
    ) -> "dc_td.CreateAIPromptResponse":
        return dc_td.CreateAIPromptResponse.make_one(res)

    def create_ai_prompt_version(
        self,
        res: "bs_td.CreateAIPromptVersionResponseTypeDef",
    ) -> "dc_td.CreateAIPromptVersionResponse":
        return dc_td.CreateAIPromptVersionResponse.make_one(res)

    def create_assistant(
        self,
        res: "bs_td.CreateAssistantResponseTypeDef",
    ) -> "dc_td.CreateAssistantResponse":
        return dc_td.CreateAssistantResponse.make_one(res)

    def create_assistant_association(
        self,
        res: "bs_td.CreateAssistantAssociationResponseTypeDef",
    ) -> "dc_td.CreateAssistantAssociationResponse":
        return dc_td.CreateAssistantAssociationResponse.make_one(res)

    def create_content(
        self,
        res: "bs_td.CreateContentResponseTypeDef",
    ) -> "dc_td.CreateContentResponse":
        return dc_td.CreateContentResponse.make_one(res)

    def create_content_association(
        self,
        res: "bs_td.CreateContentAssociationResponseTypeDef",
    ) -> "dc_td.CreateContentAssociationResponse":
        return dc_td.CreateContentAssociationResponse.make_one(res)

    def create_knowledge_base(
        self,
        res: "bs_td.CreateKnowledgeBaseResponseTypeDef",
    ) -> "dc_td.CreateKnowledgeBaseResponse":
        return dc_td.CreateKnowledgeBaseResponse.make_one(res)

    def create_message_template(
        self,
        res: "bs_td.CreateMessageTemplateResponseTypeDef",
    ) -> "dc_td.CreateMessageTemplateResponse":
        return dc_td.CreateMessageTemplateResponse.make_one(res)

    def create_message_template_attachment(
        self,
        res: "bs_td.CreateMessageTemplateAttachmentResponseTypeDef",
    ) -> "dc_td.CreateMessageTemplateAttachmentResponse":
        return dc_td.CreateMessageTemplateAttachmentResponse.make_one(res)

    def create_message_template_version(
        self,
        res: "bs_td.CreateMessageTemplateVersionResponseTypeDef",
    ) -> "dc_td.CreateMessageTemplateVersionResponse":
        return dc_td.CreateMessageTemplateVersionResponse.make_one(res)

    def create_quick_response(
        self,
        res: "bs_td.CreateQuickResponseResponseTypeDef",
    ) -> "dc_td.CreateQuickResponseResponse":
        return dc_td.CreateQuickResponseResponse.make_one(res)

    def create_session(
        self,
        res: "bs_td.CreateSessionResponseTypeDef",
    ) -> "dc_td.CreateSessionResponse":
        return dc_td.CreateSessionResponse.make_one(res)

    def deactivate_message_template(
        self,
        res: "bs_td.DeactivateMessageTemplateResponseTypeDef",
    ) -> "dc_td.DeactivateMessageTemplateResponse":
        return dc_td.DeactivateMessageTemplateResponse.make_one(res)

    def get_ai_agent(
        self,
        res: "bs_td.GetAIAgentResponseTypeDef",
    ) -> "dc_td.GetAIAgentResponse":
        return dc_td.GetAIAgentResponse.make_one(res)

    def get_ai_guardrail(
        self,
        res: "bs_td.GetAIGuardrailResponseTypeDef",
    ) -> "dc_td.GetAIGuardrailResponse":
        return dc_td.GetAIGuardrailResponse.make_one(res)

    def get_ai_prompt(
        self,
        res: "bs_td.GetAIPromptResponseTypeDef",
    ) -> "dc_td.GetAIPromptResponse":
        return dc_td.GetAIPromptResponse.make_one(res)

    def get_assistant(
        self,
        res: "bs_td.GetAssistantResponseTypeDef",
    ) -> "dc_td.GetAssistantResponse":
        return dc_td.GetAssistantResponse.make_one(res)

    def get_assistant_association(
        self,
        res: "bs_td.GetAssistantAssociationResponseTypeDef",
    ) -> "dc_td.GetAssistantAssociationResponse":
        return dc_td.GetAssistantAssociationResponse.make_one(res)

    def get_content(
        self,
        res: "bs_td.GetContentResponseTypeDef",
    ) -> "dc_td.GetContentResponse":
        return dc_td.GetContentResponse.make_one(res)

    def get_content_association(
        self,
        res: "bs_td.GetContentAssociationResponseTypeDef",
    ) -> "dc_td.GetContentAssociationResponse":
        return dc_td.GetContentAssociationResponse.make_one(res)

    def get_content_summary(
        self,
        res: "bs_td.GetContentSummaryResponseTypeDef",
    ) -> "dc_td.GetContentSummaryResponse":
        return dc_td.GetContentSummaryResponse.make_one(res)

    def get_import_job(
        self,
        res: "bs_td.GetImportJobResponseTypeDef",
    ) -> "dc_td.GetImportJobResponse":
        return dc_td.GetImportJobResponse.make_one(res)

    def get_knowledge_base(
        self,
        res: "bs_td.GetKnowledgeBaseResponseTypeDef",
    ) -> "dc_td.GetKnowledgeBaseResponse":
        return dc_td.GetKnowledgeBaseResponse.make_one(res)

    def get_message_template(
        self,
        res: "bs_td.GetMessageTemplateResponseTypeDef",
    ) -> "dc_td.GetMessageTemplateResponse":
        return dc_td.GetMessageTemplateResponse.make_one(res)

    def get_next_message(
        self,
        res: "bs_td.GetNextMessageResponseTypeDef",
    ) -> "dc_td.GetNextMessageResponse":
        return dc_td.GetNextMessageResponse.make_one(res)

    def get_quick_response(
        self,
        res: "bs_td.GetQuickResponseResponseTypeDef",
    ) -> "dc_td.GetQuickResponseResponse":
        return dc_td.GetQuickResponseResponse.make_one(res)

    def get_recommendations(
        self,
        res: "bs_td.GetRecommendationsResponseTypeDef",
    ) -> "dc_td.GetRecommendationsResponse":
        return dc_td.GetRecommendationsResponse.make_one(res)

    def get_session(
        self,
        res: "bs_td.GetSessionResponseTypeDef",
    ) -> "dc_td.GetSessionResponse":
        return dc_td.GetSessionResponse.make_one(res)

    def list_ai_agent_versions(
        self,
        res: "bs_td.ListAIAgentVersionsResponseTypeDef",
    ) -> "dc_td.ListAIAgentVersionsResponse":
        return dc_td.ListAIAgentVersionsResponse.make_one(res)

    def list_ai_agents(
        self,
        res: "bs_td.ListAIAgentsResponseTypeDef",
    ) -> "dc_td.ListAIAgentsResponse":
        return dc_td.ListAIAgentsResponse.make_one(res)

    def list_ai_guardrail_versions(
        self,
        res: "bs_td.ListAIGuardrailVersionsResponseTypeDef",
    ) -> "dc_td.ListAIGuardrailVersionsResponse":
        return dc_td.ListAIGuardrailVersionsResponse.make_one(res)

    def list_ai_guardrails(
        self,
        res: "bs_td.ListAIGuardrailsResponseTypeDef",
    ) -> "dc_td.ListAIGuardrailsResponse":
        return dc_td.ListAIGuardrailsResponse.make_one(res)

    def list_ai_prompt_versions(
        self,
        res: "bs_td.ListAIPromptVersionsResponseTypeDef",
    ) -> "dc_td.ListAIPromptVersionsResponse":
        return dc_td.ListAIPromptVersionsResponse.make_one(res)

    def list_ai_prompts(
        self,
        res: "bs_td.ListAIPromptsResponseTypeDef",
    ) -> "dc_td.ListAIPromptsResponse":
        return dc_td.ListAIPromptsResponse.make_one(res)

    def list_assistant_associations(
        self,
        res: "bs_td.ListAssistantAssociationsResponseTypeDef",
    ) -> "dc_td.ListAssistantAssociationsResponse":
        return dc_td.ListAssistantAssociationsResponse.make_one(res)

    def list_assistants(
        self,
        res: "bs_td.ListAssistantsResponseTypeDef",
    ) -> "dc_td.ListAssistantsResponse":
        return dc_td.ListAssistantsResponse.make_one(res)

    def list_content_associations(
        self,
        res: "bs_td.ListContentAssociationsResponseTypeDef",
    ) -> "dc_td.ListContentAssociationsResponse":
        return dc_td.ListContentAssociationsResponse.make_one(res)

    def list_contents(
        self,
        res: "bs_td.ListContentsResponseTypeDef",
    ) -> "dc_td.ListContentsResponse":
        return dc_td.ListContentsResponse.make_one(res)

    def list_import_jobs(
        self,
        res: "bs_td.ListImportJobsResponseTypeDef",
    ) -> "dc_td.ListImportJobsResponse":
        return dc_td.ListImportJobsResponse.make_one(res)

    def list_knowledge_bases(
        self,
        res: "bs_td.ListKnowledgeBasesResponseTypeDef",
    ) -> "dc_td.ListKnowledgeBasesResponse":
        return dc_td.ListKnowledgeBasesResponse.make_one(res)

    def list_message_template_versions(
        self,
        res: "bs_td.ListMessageTemplateVersionsResponseTypeDef",
    ) -> "dc_td.ListMessageTemplateVersionsResponse":
        return dc_td.ListMessageTemplateVersionsResponse.make_one(res)

    def list_message_templates(
        self,
        res: "bs_td.ListMessageTemplatesResponseTypeDef",
    ) -> "dc_td.ListMessageTemplatesResponse":
        return dc_td.ListMessageTemplatesResponse.make_one(res)

    def list_messages(
        self,
        res: "bs_td.ListMessagesResponseTypeDef",
    ) -> "dc_td.ListMessagesResponse":
        return dc_td.ListMessagesResponse.make_one(res)

    def list_quick_responses(
        self,
        res: "bs_td.ListQuickResponsesResponseTypeDef",
    ) -> "dc_td.ListQuickResponsesResponse":
        return dc_td.ListQuickResponsesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def notify_recommendations_received(
        self,
        res: "bs_td.NotifyRecommendationsReceivedResponseTypeDef",
    ) -> "dc_td.NotifyRecommendationsReceivedResponse":
        return dc_td.NotifyRecommendationsReceivedResponse.make_one(res)

    def put_feedback(
        self,
        res: "bs_td.PutFeedbackResponseTypeDef",
    ) -> "dc_td.PutFeedbackResponse":
        return dc_td.PutFeedbackResponse.make_one(res)

    def query_assistant(
        self,
        res: "bs_td.QueryAssistantResponseTypeDef",
    ) -> "dc_td.QueryAssistantResponse":
        return dc_td.QueryAssistantResponse.make_one(res)

    def render_message_template(
        self,
        res: "bs_td.RenderMessageTemplateResponseTypeDef",
    ) -> "dc_td.RenderMessageTemplateResponse":
        return dc_td.RenderMessageTemplateResponse.make_one(res)

    def search_content(
        self,
        res: "bs_td.SearchContentResponseTypeDef",
    ) -> "dc_td.SearchContentResponse":
        return dc_td.SearchContentResponse.make_one(res)

    def search_message_templates(
        self,
        res: "bs_td.SearchMessageTemplatesResponseTypeDef",
    ) -> "dc_td.SearchMessageTemplatesResponse":
        return dc_td.SearchMessageTemplatesResponse.make_one(res)

    def search_quick_responses(
        self,
        res: "bs_td.SearchQuickResponsesResponseTypeDef",
    ) -> "dc_td.SearchQuickResponsesResponse":
        return dc_td.SearchQuickResponsesResponse.make_one(res)

    def search_sessions(
        self,
        res: "bs_td.SearchSessionsResponseTypeDef",
    ) -> "dc_td.SearchSessionsResponse":
        return dc_td.SearchSessionsResponse.make_one(res)

    def send_message(
        self,
        res: "bs_td.SendMessageResponseTypeDef",
    ) -> "dc_td.SendMessageResponse":
        return dc_td.SendMessageResponse.make_one(res)

    def start_content_upload(
        self,
        res: "bs_td.StartContentUploadResponseTypeDef",
    ) -> "dc_td.StartContentUploadResponse":
        return dc_td.StartContentUploadResponse.make_one(res)

    def start_import_job(
        self,
        res: "bs_td.StartImportJobResponseTypeDef",
    ) -> "dc_td.StartImportJobResponse":
        return dc_td.StartImportJobResponse.make_one(res)

    def update_ai_agent(
        self,
        res: "bs_td.UpdateAIAgentResponseTypeDef",
    ) -> "dc_td.UpdateAIAgentResponse":
        return dc_td.UpdateAIAgentResponse.make_one(res)

    def update_ai_guardrail(
        self,
        res: "bs_td.UpdateAIGuardrailResponseTypeDef",
    ) -> "dc_td.UpdateAIGuardrailResponse":
        return dc_td.UpdateAIGuardrailResponse.make_one(res)

    def update_ai_prompt(
        self,
        res: "bs_td.UpdateAIPromptResponseTypeDef",
    ) -> "dc_td.UpdateAIPromptResponse":
        return dc_td.UpdateAIPromptResponse.make_one(res)

    def update_assistant_ai_agent(
        self,
        res: "bs_td.UpdateAssistantAIAgentResponseTypeDef",
    ) -> "dc_td.UpdateAssistantAIAgentResponse":
        return dc_td.UpdateAssistantAIAgentResponse.make_one(res)

    def update_content(
        self,
        res: "bs_td.UpdateContentResponseTypeDef",
    ) -> "dc_td.UpdateContentResponse":
        return dc_td.UpdateContentResponse.make_one(res)

    def update_knowledge_base_template_uri(
        self,
        res: "bs_td.UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    ) -> "dc_td.UpdateKnowledgeBaseTemplateUriResponse":
        return dc_td.UpdateKnowledgeBaseTemplateUriResponse.make_one(res)

    def update_message_template(
        self,
        res: "bs_td.UpdateMessageTemplateResponseTypeDef",
    ) -> "dc_td.UpdateMessageTemplateResponse":
        return dc_td.UpdateMessageTemplateResponse.make_one(res)

    def update_message_template_metadata(
        self,
        res: "bs_td.UpdateMessageTemplateMetadataResponseTypeDef",
    ) -> "dc_td.UpdateMessageTemplateMetadataResponse":
        return dc_td.UpdateMessageTemplateMetadataResponse.make_one(res)

    def update_quick_response(
        self,
        res: "bs_td.UpdateQuickResponseResponseTypeDef",
    ) -> "dc_td.UpdateQuickResponseResponse":
        return dc_td.UpdateQuickResponseResponse.make_one(res)

    def update_session(
        self,
        res: "bs_td.UpdateSessionResponseTypeDef",
    ) -> "dc_td.UpdateSessionResponse":
        return dc_td.UpdateSessionResponse.make_one(res)

    def update_session_data(
        self,
        res: "bs_td.UpdateSessionDataResponseTypeDef",
    ) -> "dc_td.UpdateSessionDataResponse":
        return dc_td.UpdateSessionDataResponse.make_one(res)


qconnect_caster = QCONNECTCaster()
