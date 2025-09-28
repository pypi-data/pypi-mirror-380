# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_qbusiness import type_defs as bs_td


class QBUSINESSCaster:

    def associate_permission(
        self,
        res: "bs_td.AssociatePermissionResponseTypeDef",
    ) -> "dc_td.AssociatePermissionResponse":
        return dc_td.AssociatePermissionResponse.make_one(res)

    def batch_delete_document(
        self,
        res: "bs_td.BatchDeleteDocumentResponseTypeDef",
    ) -> "dc_td.BatchDeleteDocumentResponse":
        return dc_td.BatchDeleteDocumentResponse.make_one(res)

    def batch_put_document(
        self,
        res: "bs_td.BatchPutDocumentResponseTypeDef",
    ) -> "dc_td.BatchPutDocumentResponse":
        return dc_td.BatchPutDocumentResponse.make_one(res)

    def cancel_subscription(
        self,
        res: "bs_td.CancelSubscriptionResponseTypeDef",
    ) -> "dc_td.CancelSubscriptionResponse":
        return dc_td.CancelSubscriptionResponse.make_one(res)

    def chat(
        self,
        res: "bs_td.ChatOutputTypeDef",
    ) -> "dc_td.ChatOutput":
        return dc_td.ChatOutput.make_one(res)

    def chat_sync(
        self,
        res: "bs_td.ChatSyncOutputTypeDef",
    ) -> "dc_td.ChatSyncOutput":
        return dc_td.ChatSyncOutput.make_one(res)

    def check_document_access(
        self,
        res: "bs_td.CheckDocumentAccessResponseTypeDef",
    ) -> "dc_td.CheckDocumentAccessResponse":
        return dc_td.CheckDocumentAccessResponse.make_one(res)

    def create_anonymous_web_experience_url(
        self,
        res: "bs_td.CreateAnonymousWebExperienceUrlResponseTypeDef",
    ) -> "dc_td.CreateAnonymousWebExperienceUrlResponse":
        return dc_td.CreateAnonymousWebExperienceUrlResponse.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_chat_response_configuration(
        self,
        res: "bs_td.CreateChatResponseConfigurationResponseTypeDef",
    ) -> "dc_td.CreateChatResponseConfigurationResponse":
        return dc_td.CreateChatResponseConfigurationResponse.make_one(res)

    def create_data_accessor(
        self,
        res: "bs_td.CreateDataAccessorResponseTypeDef",
    ) -> "dc_td.CreateDataAccessorResponse":
        return dc_td.CreateDataAccessorResponse.make_one(res)

    def create_data_source(
        self,
        res: "bs_td.CreateDataSourceResponseTypeDef",
    ) -> "dc_td.CreateDataSourceResponse":
        return dc_td.CreateDataSourceResponse.make_one(res)

    def create_index(
        self,
        res: "bs_td.CreateIndexResponseTypeDef",
    ) -> "dc_td.CreateIndexResponse":
        return dc_td.CreateIndexResponse.make_one(res)

    def create_plugin(
        self,
        res: "bs_td.CreatePluginResponseTypeDef",
    ) -> "dc_td.CreatePluginResponse":
        return dc_td.CreatePluginResponse.make_one(res)

    def create_retriever(
        self,
        res: "bs_td.CreateRetrieverResponseTypeDef",
    ) -> "dc_td.CreateRetrieverResponse":
        return dc_td.CreateRetrieverResponse.make_one(res)

    def create_subscription(
        self,
        res: "bs_td.CreateSubscriptionResponseTypeDef",
    ) -> "dc_td.CreateSubscriptionResponse":
        return dc_td.CreateSubscriptionResponse.make_one(res)

    def create_web_experience(
        self,
        res: "bs_td.CreateWebExperienceResponseTypeDef",
    ) -> "dc_td.CreateWebExperienceResponse":
        return dc_td.CreateWebExperienceResponse.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationResponseTypeDef",
    ) -> "dc_td.GetApplicationResponse":
        return dc_td.GetApplicationResponse.make_one(res)

    def get_chat_controls_configuration(
        self,
        res: "bs_td.GetChatControlsConfigurationResponseTypeDef",
    ) -> "dc_td.GetChatControlsConfigurationResponse":
        return dc_td.GetChatControlsConfigurationResponse.make_one(res)

    def get_chat_response_configuration(
        self,
        res: "bs_td.GetChatResponseConfigurationResponseTypeDef",
    ) -> "dc_td.GetChatResponseConfigurationResponse":
        return dc_td.GetChatResponseConfigurationResponse.make_one(res)

    def get_data_accessor(
        self,
        res: "bs_td.GetDataAccessorResponseTypeDef",
    ) -> "dc_td.GetDataAccessorResponse":
        return dc_td.GetDataAccessorResponse.make_one(res)

    def get_data_source(
        self,
        res: "bs_td.GetDataSourceResponseTypeDef",
    ) -> "dc_td.GetDataSourceResponse":
        return dc_td.GetDataSourceResponse.make_one(res)

    def get_document_content(
        self,
        res: "bs_td.GetDocumentContentResponseTypeDef",
    ) -> "dc_td.GetDocumentContentResponse":
        return dc_td.GetDocumentContentResponse.make_one(res)

    def get_group(
        self,
        res: "bs_td.GetGroupResponseTypeDef",
    ) -> "dc_td.GetGroupResponse":
        return dc_td.GetGroupResponse.make_one(res)

    def get_index(
        self,
        res: "bs_td.GetIndexResponseTypeDef",
    ) -> "dc_td.GetIndexResponse":
        return dc_td.GetIndexResponse.make_one(res)

    def get_media(
        self,
        res: "bs_td.GetMediaResponseTypeDef",
    ) -> "dc_td.GetMediaResponse":
        return dc_td.GetMediaResponse.make_one(res)

    def get_plugin(
        self,
        res: "bs_td.GetPluginResponseTypeDef",
    ) -> "dc_td.GetPluginResponse":
        return dc_td.GetPluginResponse.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyResponseTypeDef",
    ) -> "dc_td.GetPolicyResponse":
        return dc_td.GetPolicyResponse.make_one(res)

    def get_retriever(
        self,
        res: "bs_td.GetRetrieverResponseTypeDef",
    ) -> "dc_td.GetRetrieverResponse":
        return dc_td.GetRetrieverResponse.make_one(res)

    def get_user(
        self,
        res: "bs_td.GetUserResponseTypeDef",
    ) -> "dc_td.GetUserResponse":
        return dc_td.GetUserResponse.make_one(res)

    def get_web_experience(
        self,
        res: "bs_td.GetWebExperienceResponseTypeDef",
    ) -> "dc_td.GetWebExperienceResponse":
        return dc_td.GetWebExperienceResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_attachments(
        self,
        res: "bs_td.ListAttachmentsResponseTypeDef",
    ) -> "dc_td.ListAttachmentsResponse":
        return dc_td.ListAttachmentsResponse.make_one(res)

    def list_chat_response_configurations(
        self,
        res: "bs_td.ListChatResponseConfigurationsResponseTypeDef",
    ) -> "dc_td.ListChatResponseConfigurationsResponse":
        return dc_td.ListChatResponseConfigurationsResponse.make_one(res)

    def list_conversations(
        self,
        res: "bs_td.ListConversationsResponseTypeDef",
    ) -> "dc_td.ListConversationsResponse":
        return dc_td.ListConversationsResponse.make_one(res)

    def list_data_accessors(
        self,
        res: "bs_td.ListDataAccessorsResponseTypeDef",
    ) -> "dc_td.ListDataAccessorsResponse":
        return dc_td.ListDataAccessorsResponse.make_one(res)

    def list_data_source_sync_jobs(
        self,
        res: "bs_td.ListDataSourceSyncJobsResponseTypeDef",
    ) -> "dc_td.ListDataSourceSyncJobsResponse":
        return dc_td.ListDataSourceSyncJobsResponse.make_one(res)

    def list_data_sources(
        self,
        res: "bs_td.ListDataSourcesResponseTypeDef",
    ) -> "dc_td.ListDataSourcesResponse":
        return dc_td.ListDataSourcesResponse.make_one(res)

    def list_documents(
        self,
        res: "bs_td.ListDocumentsResponseTypeDef",
    ) -> "dc_td.ListDocumentsResponse":
        return dc_td.ListDocumentsResponse.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsResponseTypeDef",
    ) -> "dc_td.ListGroupsResponse":
        return dc_td.ListGroupsResponse.make_one(res)

    def list_indices(
        self,
        res: "bs_td.ListIndicesResponseTypeDef",
    ) -> "dc_td.ListIndicesResponse":
        return dc_td.ListIndicesResponse.make_one(res)

    def list_messages(
        self,
        res: "bs_td.ListMessagesResponseTypeDef",
    ) -> "dc_td.ListMessagesResponse":
        return dc_td.ListMessagesResponse.make_one(res)

    def list_plugin_actions(
        self,
        res: "bs_td.ListPluginActionsResponseTypeDef",
    ) -> "dc_td.ListPluginActionsResponse":
        return dc_td.ListPluginActionsResponse.make_one(res)

    def list_plugin_type_actions(
        self,
        res: "bs_td.ListPluginTypeActionsResponseTypeDef",
    ) -> "dc_td.ListPluginTypeActionsResponse":
        return dc_td.ListPluginTypeActionsResponse.make_one(res)

    def list_plugin_type_metadata(
        self,
        res: "bs_td.ListPluginTypeMetadataResponseTypeDef",
    ) -> "dc_td.ListPluginTypeMetadataResponse":
        return dc_td.ListPluginTypeMetadataResponse.make_one(res)

    def list_plugins(
        self,
        res: "bs_td.ListPluginsResponseTypeDef",
    ) -> "dc_td.ListPluginsResponse":
        return dc_td.ListPluginsResponse.make_one(res)

    def list_retrievers(
        self,
        res: "bs_td.ListRetrieversResponseTypeDef",
    ) -> "dc_td.ListRetrieversResponse":
        return dc_td.ListRetrieversResponse.make_one(res)

    def list_subscriptions(
        self,
        res: "bs_td.ListSubscriptionsResponseTypeDef",
    ) -> "dc_td.ListSubscriptionsResponse":
        return dc_td.ListSubscriptionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_web_experiences(
        self,
        res: "bs_td.ListWebExperiencesResponseTypeDef",
    ) -> "dc_td.ListWebExperiencesResponse":
        return dc_td.ListWebExperiencesResponse.make_one(res)

    def put_feedback(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def search_relevant_content(
        self,
        res: "bs_td.SearchRelevantContentResponseTypeDef",
    ) -> "dc_td.SearchRelevantContentResponse":
        return dc_td.SearchRelevantContentResponse.make_one(res)

    def start_data_source_sync_job(
        self,
        res: "bs_td.StartDataSourceSyncJobResponseTypeDef",
    ) -> "dc_td.StartDataSourceSyncJobResponse":
        return dc_td.StartDataSourceSyncJobResponse.make_one(res)

    def update_subscription(
        self,
        res: "bs_td.UpdateSubscriptionResponseTypeDef",
    ) -> "dc_td.UpdateSubscriptionResponse":
        return dc_td.UpdateSubscriptionResponse.make_one(res)

    def update_user(
        self,
        res: "bs_td.UpdateUserResponseTypeDef",
    ) -> "dc_td.UpdateUserResponse":
        return dc_td.UpdateUserResponse.make_one(res)


qbusiness_caster = QBUSINESSCaster()
