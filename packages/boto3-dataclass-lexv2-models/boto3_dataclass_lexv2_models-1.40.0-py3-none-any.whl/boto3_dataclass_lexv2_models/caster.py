# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lexv2_models import type_defs as bs_td


class LEXV2_MODELSCaster:

    def batch_create_custom_vocabulary_item(
        self,
        res: "bs_td.BatchCreateCustomVocabularyItemResponseTypeDef",
    ) -> "dc_td.BatchCreateCustomVocabularyItemResponse":
        return dc_td.BatchCreateCustomVocabularyItemResponse.make_one(res)

    def batch_delete_custom_vocabulary_item(
        self,
        res: "bs_td.BatchDeleteCustomVocabularyItemResponseTypeDef",
    ) -> "dc_td.BatchDeleteCustomVocabularyItemResponse":
        return dc_td.BatchDeleteCustomVocabularyItemResponse.make_one(res)

    def batch_update_custom_vocabulary_item(
        self,
        res: "bs_td.BatchUpdateCustomVocabularyItemResponseTypeDef",
    ) -> "dc_td.BatchUpdateCustomVocabularyItemResponse":
        return dc_td.BatchUpdateCustomVocabularyItemResponse.make_one(res)

    def build_bot_locale(
        self,
        res: "bs_td.BuildBotLocaleResponseTypeDef",
    ) -> "dc_td.BuildBotLocaleResponse":
        return dc_td.BuildBotLocaleResponse.make_one(res)

    def create_bot(
        self,
        res: "bs_td.CreateBotResponseTypeDef",
    ) -> "dc_td.CreateBotResponse":
        return dc_td.CreateBotResponse.make_one(res)

    def create_bot_alias(
        self,
        res: "bs_td.CreateBotAliasResponseTypeDef",
    ) -> "dc_td.CreateBotAliasResponse":
        return dc_td.CreateBotAliasResponse.make_one(res)

    def create_bot_locale(
        self,
        res: "bs_td.CreateBotLocaleResponseTypeDef",
    ) -> "dc_td.CreateBotLocaleResponse":
        return dc_td.CreateBotLocaleResponse.make_one(res)

    def create_bot_replica(
        self,
        res: "bs_td.CreateBotReplicaResponseTypeDef",
    ) -> "dc_td.CreateBotReplicaResponse":
        return dc_td.CreateBotReplicaResponse.make_one(res)

    def create_bot_version(
        self,
        res: "bs_td.CreateBotVersionResponseTypeDef",
    ) -> "dc_td.CreateBotVersionResponse":
        return dc_td.CreateBotVersionResponse.make_one(res)

    def create_export(
        self,
        res: "bs_td.CreateExportResponseTypeDef",
    ) -> "dc_td.CreateExportResponse":
        return dc_td.CreateExportResponse.make_one(res)

    def create_intent(
        self,
        res: "bs_td.CreateIntentResponseTypeDef",
    ) -> "dc_td.CreateIntentResponse":
        return dc_td.CreateIntentResponse.make_one(res)

    def create_resource_policy(
        self,
        res: "bs_td.CreateResourcePolicyResponseTypeDef",
    ) -> "dc_td.CreateResourcePolicyResponse":
        return dc_td.CreateResourcePolicyResponse.make_one(res)

    def create_resource_policy_statement(
        self,
        res: "bs_td.CreateResourcePolicyStatementResponseTypeDef",
    ) -> "dc_td.CreateResourcePolicyStatementResponse":
        return dc_td.CreateResourcePolicyStatementResponse.make_one(res)

    def create_slot(
        self,
        res: "bs_td.CreateSlotResponseTypeDef",
    ) -> "dc_td.CreateSlotResponse":
        return dc_td.CreateSlotResponse.make_one(res)

    def create_slot_type(
        self,
        res: "bs_td.CreateSlotTypeResponseTypeDef",
    ) -> "dc_td.CreateSlotTypeResponse":
        return dc_td.CreateSlotTypeResponse.make_one(res)

    def create_test_set_discrepancy_report(
        self,
        res: "bs_td.CreateTestSetDiscrepancyReportResponseTypeDef",
    ) -> "dc_td.CreateTestSetDiscrepancyReportResponse":
        return dc_td.CreateTestSetDiscrepancyReportResponse.make_one(res)

    def create_upload_url(
        self,
        res: "bs_td.CreateUploadUrlResponseTypeDef",
    ) -> "dc_td.CreateUploadUrlResponse":
        return dc_td.CreateUploadUrlResponse.make_one(res)

    def delete_bot(
        self,
        res: "bs_td.DeleteBotResponseTypeDef",
    ) -> "dc_td.DeleteBotResponse":
        return dc_td.DeleteBotResponse.make_one(res)

    def delete_bot_alias(
        self,
        res: "bs_td.DeleteBotAliasResponseTypeDef",
    ) -> "dc_td.DeleteBotAliasResponse":
        return dc_td.DeleteBotAliasResponse.make_one(res)

    def delete_bot_locale(
        self,
        res: "bs_td.DeleteBotLocaleResponseTypeDef",
    ) -> "dc_td.DeleteBotLocaleResponse":
        return dc_td.DeleteBotLocaleResponse.make_one(res)

    def delete_bot_replica(
        self,
        res: "bs_td.DeleteBotReplicaResponseTypeDef",
    ) -> "dc_td.DeleteBotReplicaResponse":
        return dc_td.DeleteBotReplicaResponse.make_one(res)

    def delete_bot_version(
        self,
        res: "bs_td.DeleteBotVersionResponseTypeDef",
    ) -> "dc_td.DeleteBotVersionResponse":
        return dc_td.DeleteBotVersionResponse.make_one(res)

    def delete_custom_vocabulary(
        self,
        res: "bs_td.DeleteCustomVocabularyResponseTypeDef",
    ) -> "dc_td.DeleteCustomVocabularyResponse":
        return dc_td.DeleteCustomVocabularyResponse.make_one(res)

    def delete_export(
        self,
        res: "bs_td.DeleteExportResponseTypeDef",
    ) -> "dc_td.DeleteExportResponse":
        return dc_td.DeleteExportResponse.make_one(res)

    def delete_import(
        self,
        res: "bs_td.DeleteImportResponseTypeDef",
    ) -> "dc_td.DeleteImportResponse":
        return dc_td.DeleteImportResponse.make_one(res)

    def delete_intent(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.DeleteResourcePolicyResponseTypeDef",
    ) -> "dc_td.DeleteResourcePolicyResponse":
        return dc_td.DeleteResourcePolicyResponse.make_one(res)

    def delete_resource_policy_statement(
        self,
        res: "bs_td.DeleteResourcePolicyStatementResponseTypeDef",
    ) -> "dc_td.DeleteResourcePolicyStatementResponse":
        return dc_td.DeleteResourcePolicyStatementResponse.make_one(res)

    def delete_slot(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_slot_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_test_set(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_bot(
        self,
        res: "bs_td.DescribeBotResponseTypeDef",
    ) -> "dc_td.DescribeBotResponse":
        return dc_td.DescribeBotResponse.make_one(res)

    def describe_bot_alias(
        self,
        res: "bs_td.DescribeBotAliasResponseTypeDef",
    ) -> "dc_td.DescribeBotAliasResponse":
        return dc_td.DescribeBotAliasResponse.make_one(res)

    def describe_bot_locale(
        self,
        res: "bs_td.DescribeBotLocaleResponseTypeDef",
    ) -> "dc_td.DescribeBotLocaleResponse":
        return dc_td.DescribeBotLocaleResponse.make_one(res)

    def describe_bot_recommendation(
        self,
        res: "bs_td.DescribeBotRecommendationResponseTypeDef",
    ) -> "dc_td.DescribeBotRecommendationResponse":
        return dc_td.DescribeBotRecommendationResponse.make_one(res)

    def describe_bot_replica(
        self,
        res: "bs_td.DescribeBotReplicaResponseTypeDef",
    ) -> "dc_td.DescribeBotReplicaResponse":
        return dc_td.DescribeBotReplicaResponse.make_one(res)

    def describe_bot_resource_generation(
        self,
        res: "bs_td.DescribeBotResourceGenerationResponseTypeDef",
    ) -> "dc_td.DescribeBotResourceGenerationResponse":
        return dc_td.DescribeBotResourceGenerationResponse.make_one(res)

    def describe_bot_version(
        self,
        res: "bs_td.DescribeBotVersionResponseTypeDef",
    ) -> "dc_td.DescribeBotVersionResponse":
        return dc_td.DescribeBotVersionResponse.make_one(res)

    def describe_custom_vocabulary_metadata(
        self,
        res: "bs_td.DescribeCustomVocabularyMetadataResponseTypeDef",
    ) -> "dc_td.DescribeCustomVocabularyMetadataResponse":
        return dc_td.DescribeCustomVocabularyMetadataResponse.make_one(res)

    def describe_export(
        self,
        res: "bs_td.DescribeExportResponseTypeDef",
    ) -> "dc_td.DescribeExportResponse":
        return dc_td.DescribeExportResponse.make_one(res)

    def describe_import(
        self,
        res: "bs_td.DescribeImportResponseTypeDef",
    ) -> "dc_td.DescribeImportResponse":
        return dc_td.DescribeImportResponse.make_one(res)

    def describe_intent(
        self,
        res: "bs_td.DescribeIntentResponseTypeDef",
    ) -> "dc_td.DescribeIntentResponse":
        return dc_td.DescribeIntentResponse.make_one(res)

    def describe_resource_policy(
        self,
        res: "bs_td.DescribeResourcePolicyResponseTypeDef",
    ) -> "dc_td.DescribeResourcePolicyResponse":
        return dc_td.DescribeResourcePolicyResponse.make_one(res)

    def describe_slot(
        self,
        res: "bs_td.DescribeSlotResponseTypeDef",
    ) -> "dc_td.DescribeSlotResponse":
        return dc_td.DescribeSlotResponse.make_one(res)

    def describe_slot_type(
        self,
        res: "bs_td.DescribeSlotTypeResponseTypeDef",
    ) -> "dc_td.DescribeSlotTypeResponse":
        return dc_td.DescribeSlotTypeResponse.make_one(res)

    def describe_test_execution(
        self,
        res: "bs_td.DescribeTestExecutionResponseTypeDef",
    ) -> "dc_td.DescribeTestExecutionResponse":
        return dc_td.DescribeTestExecutionResponse.make_one(res)

    def describe_test_set(
        self,
        res: "bs_td.DescribeTestSetResponseTypeDef",
    ) -> "dc_td.DescribeTestSetResponse":
        return dc_td.DescribeTestSetResponse.make_one(res)

    def describe_test_set_discrepancy_report(
        self,
        res: "bs_td.DescribeTestSetDiscrepancyReportResponseTypeDef",
    ) -> "dc_td.DescribeTestSetDiscrepancyReportResponse":
        return dc_td.DescribeTestSetDiscrepancyReportResponse.make_one(res)

    def describe_test_set_generation(
        self,
        res: "bs_td.DescribeTestSetGenerationResponseTypeDef",
    ) -> "dc_td.DescribeTestSetGenerationResponse":
        return dc_td.DescribeTestSetGenerationResponse.make_one(res)

    def generate_bot_element(
        self,
        res: "bs_td.GenerateBotElementResponseTypeDef",
    ) -> "dc_td.GenerateBotElementResponse":
        return dc_td.GenerateBotElementResponse.make_one(res)

    def get_test_execution_artifacts_url(
        self,
        res: "bs_td.GetTestExecutionArtifactsUrlResponseTypeDef",
    ) -> "dc_td.GetTestExecutionArtifactsUrlResponse":
        return dc_td.GetTestExecutionArtifactsUrlResponse.make_one(res)

    def list_aggregated_utterances(
        self,
        res: "bs_td.ListAggregatedUtterancesResponseTypeDef",
    ) -> "dc_td.ListAggregatedUtterancesResponse":
        return dc_td.ListAggregatedUtterancesResponse.make_one(res)

    def list_bot_alias_replicas(
        self,
        res: "bs_td.ListBotAliasReplicasResponseTypeDef",
    ) -> "dc_td.ListBotAliasReplicasResponse":
        return dc_td.ListBotAliasReplicasResponse.make_one(res)

    def list_bot_aliases(
        self,
        res: "bs_td.ListBotAliasesResponseTypeDef",
    ) -> "dc_td.ListBotAliasesResponse":
        return dc_td.ListBotAliasesResponse.make_one(res)

    def list_bot_locales(
        self,
        res: "bs_td.ListBotLocalesResponseTypeDef",
    ) -> "dc_td.ListBotLocalesResponse":
        return dc_td.ListBotLocalesResponse.make_one(res)

    def list_bot_recommendations(
        self,
        res: "bs_td.ListBotRecommendationsResponseTypeDef",
    ) -> "dc_td.ListBotRecommendationsResponse":
        return dc_td.ListBotRecommendationsResponse.make_one(res)

    def list_bot_replicas(
        self,
        res: "bs_td.ListBotReplicasResponseTypeDef",
    ) -> "dc_td.ListBotReplicasResponse":
        return dc_td.ListBotReplicasResponse.make_one(res)

    def list_bot_resource_generations(
        self,
        res: "bs_td.ListBotResourceGenerationsResponseTypeDef",
    ) -> "dc_td.ListBotResourceGenerationsResponse":
        return dc_td.ListBotResourceGenerationsResponse.make_one(res)

    def list_bot_version_replicas(
        self,
        res: "bs_td.ListBotVersionReplicasResponseTypeDef",
    ) -> "dc_td.ListBotVersionReplicasResponse":
        return dc_td.ListBotVersionReplicasResponse.make_one(res)

    def list_bot_versions(
        self,
        res: "bs_td.ListBotVersionsResponseTypeDef",
    ) -> "dc_td.ListBotVersionsResponse":
        return dc_td.ListBotVersionsResponse.make_one(res)

    def list_bots(
        self,
        res: "bs_td.ListBotsResponseTypeDef",
    ) -> "dc_td.ListBotsResponse":
        return dc_td.ListBotsResponse.make_one(res)

    def list_built_in_intents(
        self,
        res: "bs_td.ListBuiltInIntentsResponseTypeDef",
    ) -> "dc_td.ListBuiltInIntentsResponse":
        return dc_td.ListBuiltInIntentsResponse.make_one(res)

    def list_built_in_slot_types(
        self,
        res: "bs_td.ListBuiltInSlotTypesResponseTypeDef",
    ) -> "dc_td.ListBuiltInSlotTypesResponse":
        return dc_td.ListBuiltInSlotTypesResponse.make_one(res)

    def list_custom_vocabulary_items(
        self,
        res: "bs_td.ListCustomVocabularyItemsResponseTypeDef",
    ) -> "dc_td.ListCustomVocabularyItemsResponse":
        return dc_td.ListCustomVocabularyItemsResponse.make_one(res)

    def list_exports(
        self,
        res: "bs_td.ListExportsResponseTypeDef",
    ) -> "dc_td.ListExportsResponse":
        return dc_td.ListExportsResponse.make_one(res)

    def list_imports(
        self,
        res: "bs_td.ListImportsResponseTypeDef",
    ) -> "dc_td.ListImportsResponse":
        return dc_td.ListImportsResponse.make_one(res)

    def list_intent_metrics(
        self,
        res: "bs_td.ListIntentMetricsResponseTypeDef",
    ) -> "dc_td.ListIntentMetricsResponse":
        return dc_td.ListIntentMetricsResponse.make_one(res)

    def list_intent_paths(
        self,
        res: "bs_td.ListIntentPathsResponseTypeDef",
    ) -> "dc_td.ListIntentPathsResponse":
        return dc_td.ListIntentPathsResponse.make_one(res)

    def list_intent_stage_metrics(
        self,
        res: "bs_td.ListIntentStageMetricsResponseTypeDef",
    ) -> "dc_td.ListIntentStageMetricsResponse":
        return dc_td.ListIntentStageMetricsResponse.make_one(res)

    def list_intents(
        self,
        res: "bs_td.ListIntentsResponseTypeDef",
    ) -> "dc_td.ListIntentsResponse":
        return dc_td.ListIntentsResponse.make_one(res)

    def list_recommended_intents(
        self,
        res: "bs_td.ListRecommendedIntentsResponseTypeDef",
    ) -> "dc_td.ListRecommendedIntentsResponse":
        return dc_td.ListRecommendedIntentsResponse.make_one(res)

    def list_session_analytics_data(
        self,
        res: "bs_td.ListSessionAnalyticsDataResponseTypeDef",
    ) -> "dc_td.ListSessionAnalyticsDataResponse":
        return dc_td.ListSessionAnalyticsDataResponse.make_one(res)

    def list_session_metrics(
        self,
        res: "bs_td.ListSessionMetricsResponseTypeDef",
    ) -> "dc_td.ListSessionMetricsResponse":
        return dc_td.ListSessionMetricsResponse.make_one(res)

    def list_slot_types(
        self,
        res: "bs_td.ListSlotTypesResponseTypeDef",
    ) -> "dc_td.ListSlotTypesResponse":
        return dc_td.ListSlotTypesResponse.make_one(res)

    def list_slots(
        self,
        res: "bs_td.ListSlotsResponseTypeDef",
    ) -> "dc_td.ListSlotsResponse":
        return dc_td.ListSlotsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_test_execution_result_items(
        self,
        res: "bs_td.ListTestExecutionResultItemsResponseTypeDef",
    ) -> "dc_td.ListTestExecutionResultItemsResponse":
        return dc_td.ListTestExecutionResultItemsResponse.make_one(res)

    def list_test_executions(
        self,
        res: "bs_td.ListTestExecutionsResponseTypeDef",
    ) -> "dc_td.ListTestExecutionsResponse":
        return dc_td.ListTestExecutionsResponse.make_one(res)

    def list_test_set_records(
        self,
        res: "bs_td.ListTestSetRecordsResponseTypeDef",
    ) -> "dc_td.ListTestSetRecordsResponse":
        return dc_td.ListTestSetRecordsResponse.make_one(res)

    def list_test_sets(
        self,
        res: "bs_td.ListTestSetsResponseTypeDef",
    ) -> "dc_td.ListTestSetsResponse":
        return dc_td.ListTestSetsResponse.make_one(res)

    def list_utterance_analytics_data(
        self,
        res: "bs_td.ListUtteranceAnalyticsDataResponseTypeDef",
    ) -> "dc_td.ListUtteranceAnalyticsDataResponse":
        return dc_td.ListUtteranceAnalyticsDataResponse.make_one(res)

    def list_utterance_metrics(
        self,
        res: "bs_td.ListUtteranceMetricsResponseTypeDef",
    ) -> "dc_td.ListUtteranceMetricsResponse":
        return dc_td.ListUtteranceMetricsResponse.make_one(res)

    def search_associated_transcripts(
        self,
        res: "bs_td.SearchAssociatedTranscriptsResponseTypeDef",
    ) -> "dc_td.SearchAssociatedTranscriptsResponse":
        return dc_td.SearchAssociatedTranscriptsResponse.make_one(res)

    def start_bot_recommendation(
        self,
        res: "bs_td.StartBotRecommendationResponseTypeDef",
    ) -> "dc_td.StartBotRecommendationResponse":
        return dc_td.StartBotRecommendationResponse.make_one(res)

    def start_bot_resource_generation(
        self,
        res: "bs_td.StartBotResourceGenerationResponseTypeDef",
    ) -> "dc_td.StartBotResourceGenerationResponse":
        return dc_td.StartBotResourceGenerationResponse.make_one(res)

    def start_import(
        self,
        res: "bs_td.StartImportResponseTypeDef",
    ) -> "dc_td.StartImportResponse":
        return dc_td.StartImportResponse.make_one(res)

    def start_test_execution(
        self,
        res: "bs_td.StartTestExecutionResponseTypeDef",
    ) -> "dc_td.StartTestExecutionResponse":
        return dc_td.StartTestExecutionResponse.make_one(res)

    def start_test_set_generation(
        self,
        res: "bs_td.StartTestSetGenerationResponseTypeDef",
    ) -> "dc_td.StartTestSetGenerationResponse":
        return dc_td.StartTestSetGenerationResponse.make_one(res)

    def stop_bot_recommendation(
        self,
        res: "bs_td.StopBotRecommendationResponseTypeDef",
    ) -> "dc_td.StopBotRecommendationResponse":
        return dc_td.StopBotRecommendationResponse.make_one(res)

    def update_bot(
        self,
        res: "bs_td.UpdateBotResponseTypeDef",
    ) -> "dc_td.UpdateBotResponse":
        return dc_td.UpdateBotResponse.make_one(res)

    def update_bot_alias(
        self,
        res: "bs_td.UpdateBotAliasResponseTypeDef",
    ) -> "dc_td.UpdateBotAliasResponse":
        return dc_td.UpdateBotAliasResponse.make_one(res)

    def update_bot_locale(
        self,
        res: "bs_td.UpdateBotLocaleResponseTypeDef",
    ) -> "dc_td.UpdateBotLocaleResponse":
        return dc_td.UpdateBotLocaleResponse.make_one(res)

    def update_bot_recommendation(
        self,
        res: "bs_td.UpdateBotRecommendationResponseTypeDef",
    ) -> "dc_td.UpdateBotRecommendationResponse":
        return dc_td.UpdateBotRecommendationResponse.make_one(res)

    def update_export(
        self,
        res: "bs_td.UpdateExportResponseTypeDef",
    ) -> "dc_td.UpdateExportResponse":
        return dc_td.UpdateExportResponse.make_one(res)

    def update_intent(
        self,
        res: "bs_td.UpdateIntentResponseTypeDef",
    ) -> "dc_td.UpdateIntentResponse":
        return dc_td.UpdateIntentResponse.make_one(res)

    def update_resource_policy(
        self,
        res: "bs_td.UpdateResourcePolicyResponseTypeDef",
    ) -> "dc_td.UpdateResourcePolicyResponse":
        return dc_td.UpdateResourcePolicyResponse.make_one(res)

    def update_slot(
        self,
        res: "bs_td.UpdateSlotResponseTypeDef",
    ) -> "dc_td.UpdateSlotResponse":
        return dc_td.UpdateSlotResponse.make_one(res)

    def update_slot_type(
        self,
        res: "bs_td.UpdateSlotTypeResponseTypeDef",
    ) -> "dc_td.UpdateSlotTypeResponse":
        return dc_td.UpdateSlotTypeResponse.make_one(res)

    def update_test_set(
        self,
        res: "bs_td.UpdateTestSetResponseTypeDef",
    ) -> "dc_td.UpdateTestSetResponse":
        return dc_td.UpdateTestSetResponse.make_one(res)


lexv2_models_caster = LEXV2_MODELSCaster()
