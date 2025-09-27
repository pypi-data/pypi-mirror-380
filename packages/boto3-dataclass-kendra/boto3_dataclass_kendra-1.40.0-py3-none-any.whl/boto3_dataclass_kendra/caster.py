# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kendra import type_defs as bs_td


class KENDRACaster:

    def associate_entities_to_experience(
        self,
        res: "bs_td.AssociateEntitiesToExperienceResponseTypeDef",
    ) -> "dc_td.AssociateEntitiesToExperienceResponse":
        return dc_td.AssociateEntitiesToExperienceResponse.make_one(res)

    def associate_personas_to_entities(
        self,
        res: "bs_td.AssociatePersonasToEntitiesResponseTypeDef",
    ) -> "dc_td.AssociatePersonasToEntitiesResponse":
        return dc_td.AssociatePersonasToEntitiesResponse.make_one(res)

    def batch_delete_document(
        self,
        res: "bs_td.BatchDeleteDocumentResponseTypeDef",
    ) -> "dc_td.BatchDeleteDocumentResponse":
        return dc_td.BatchDeleteDocumentResponse.make_one(res)

    def batch_delete_featured_results_set(
        self,
        res: "bs_td.BatchDeleteFeaturedResultsSetResponseTypeDef",
    ) -> "dc_td.BatchDeleteFeaturedResultsSetResponse":
        return dc_td.BatchDeleteFeaturedResultsSetResponse.make_one(res)

    def batch_get_document_status(
        self,
        res: "bs_td.BatchGetDocumentStatusResponseTypeDef",
    ) -> "dc_td.BatchGetDocumentStatusResponse":
        return dc_td.BatchGetDocumentStatusResponse.make_one(res)

    def batch_put_document(
        self,
        res: "bs_td.BatchPutDocumentResponseTypeDef",
    ) -> "dc_td.BatchPutDocumentResponse":
        return dc_td.BatchPutDocumentResponse.make_one(res)

    def clear_query_suggestions(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_access_control_configuration(
        self,
        res: "bs_td.CreateAccessControlConfigurationResponseTypeDef",
    ) -> "dc_td.CreateAccessControlConfigurationResponse":
        return dc_td.CreateAccessControlConfigurationResponse.make_one(res)

    def create_data_source(
        self,
        res: "bs_td.CreateDataSourceResponseTypeDef",
    ) -> "dc_td.CreateDataSourceResponse":
        return dc_td.CreateDataSourceResponse.make_one(res)

    def create_experience(
        self,
        res: "bs_td.CreateExperienceResponseTypeDef",
    ) -> "dc_td.CreateExperienceResponse":
        return dc_td.CreateExperienceResponse.make_one(res)

    def create_faq(
        self,
        res: "bs_td.CreateFaqResponseTypeDef",
    ) -> "dc_td.CreateFaqResponse":
        return dc_td.CreateFaqResponse.make_one(res)

    def create_featured_results_set(
        self,
        res: "bs_td.CreateFeaturedResultsSetResponseTypeDef",
    ) -> "dc_td.CreateFeaturedResultsSetResponse":
        return dc_td.CreateFeaturedResultsSetResponse.make_one(res)

    def create_index(
        self,
        res: "bs_td.CreateIndexResponseTypeDef",
    ) -> "dc_td.CreateIndexResponse":
        return dc_td.CreateIndexResponse.make_one(res)

    def create_query_suggestions_block_list(
        self,
        res: "bs_td.CreateQuerySuggestionsBlockListResponseTypeDef",
    ) -> "dc_td.CreateQuerySuggestionsBlockListResponse":
        return dc_td.CreateQuerySuggestionsBlockListResponse.make_one(res)

    def create_thesaurus(
        self,
        res: "bs_td.CreateThesaurusResponseTypeDef",
    ) -> "dc_td.CreateThesaurusResponse":
        return dc_td.CreateThesaurusResponse.make_one(res)

    def delete_data_source(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_faq(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_index(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_principal_mapping(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_query_suggestions_block_list(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_thesaurus(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_access_control_configuration(
        self,
        res: "bs_td.DescribeAccessControlConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeAccessControlConfigurationResponse":
        return dc_td.DescribeAccessControlConfigurationResponse.make_one(res)

    def describe_data_source(
        self,
        res: "bs_td.DescribeDataSourceResponseTypeDef",
    ) -> "dc_td.DescribeDataSourceResponse":
        return dc_td.DescribeDataSourceResponse.make_one(res)

    def describe_experience(
        self,
        res: "bs_td.DescribeExperienceResponseTypeDef",
    ) -> "dc_td.DescribeExperienceResponse":
        return dc_td.DescribeExperienceResponse.make_one(res)

    def describe_faq(
        self,
        res: "bs_td.DescribeFaqResponseTypeDef",
    ) -> "dc_td.DescribeFaqResponse":
        return dc_td.DescribeFaqResponse.make_one(res)

    def describe_featured_results_set(
        self,
        res: "bs_td.DescribeFeaturedResultsSetResponseTypeDef",
    ) -> "dc_td.DescribeFeaturedResultsSetResponse":
        return dc_td.DescribeFeaturedResultsSetResponse.make_one(res)

    def describe_index(
        self,
        res: "bs_td.DescribeIndexResponseTypeDef",
    ) -> "dc_td.DescribeIndexResponse":
        return dc_td.DescribeIndexResponse.make_one(res)

    def describe_principal_mapping(
        self,
        res: "bs_td.DescribePrincipalMappingResponseTypeDef",
    ) -> "dc_td.DescribePrincipalMappingResponse":
        return dc_td.DescribePrincipalMappingResponse.make_one(res)

    def describe_query_suggestions_block_list(
        self,
        res: "bs_td.DescribeQuerySuggestionsBlockListResponseTypeDef",
    ) -> "dc_td.DescribeQuerySuggestionsBlockListResponse":
        return dc_td.DescribeQuerySuggestionsBlockListResponse.make_one(res)

    def describe_query_suggestions_config(
        self,
        res: "bs_td.DescribeQuerySuggestionsConfigResponseTypeDef",
    ) -> "dc_td.DescribeQuerySuggestionsConfigResponse":
        return dc_td.DescribeQuerySuggestionsConfigResponse.make_one(res)

    def describe_thesaurus(
        self,
        res: "bs_td.DescribeThesaurusResponseTypeDef",
    ) -> "dc_td.DescribeThesaurusResponse":
        return dc_td.DescribeThesaurusResponse.make_one(res)

    def disassociate_entities_from_experience(
        self,
        res: "bs_td.DisassociateEntitiesFromExperienceResponseTypeDef",
    ) -> "dc_td.DisassociateEntitiesFromExperienceResponse":
        return dc_td.DisassociateEntitiesFromExperienceResponse.make_one(res)

    def disassociate_personas_from_entities(
        self,
        res: "bs_td.DisassociatePersonasFromEntitiesResponseTypeDef",
    ) -> "dc_td.DisassociatePersonasFromEntitiesResponse":
        return dc_td.DisassociatePersonasFromEntitiesResponse.make_one(res)

    def get_query_suggestions(
        self,
        res: "bs_td.GetQuerySuggestionsResponseTypeDef",
    ) -> "dc_td.GetQuerySuggestionsResponse":
        return dc_td.GetQuerySuggestionsResponse.make_one(res)

    def get_snapshots(
        self,
        res: "bs_td.GetSnapshotsResponseTypeDef",
    ) -> "dc_td.GetSnapshotsResponse":
        return dc_td.GetSnapshotsResponse.make_one(res)

    def list_access_control_configurations(
        self,
        res: "bs_td.ListAccessControlConfigurationsResponseTypeDef",
    ) -> "dc_td.ListAccessControlConfigurationsResponse":
        return dc_td.ListAccessControlConfigurationsResponse.make_one(res)

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

    def list_entity_personas(
        self,
        res: "bs_td.ListEntityPersonasResponseTypeDef",
    ) -> "dc_td.ListEntityPersonasResponse":
        return dc_td.ListEntityPersonasResponse.make_one(res)

    def list_experience_entities(
        self,
        res: "bs_td.ListExperienceEntitiesResponseTypeDef",
    ) -> "dc_td.ListExperienceEntitiesResponse":
        return dc_td.ListExperienceEntitiesResponse.make_one(res)

    def list_experiences(
        self,
        res: "bs_td.ListExperiencesResponseTypeDef",
    ) -> "dc_td.ListExperiencesResponse":
        return dc_td.ListExperiencesResponse.make_one(res)

    def list_faqs(
        self,
        res: "bs_td.ListFaqsResponseTypeDef",
    ) -> "dc_td.ListFaqsResponse":
        return dc_td.ListFaqsResponse.make_one(res)

    def list_featured_results_sets(
        self,
        res: "bs_td.ListFeaturedResultsSetsResponseTypeDef",
    ) -> "dc_td.ListFeaturedResultsSetsResponse":
        return dc_td.ListFeaturedResultsSetsResponse.make_one(res)

    def list_groups_older_than_ordering_id(
        self,
        res: "bs_td.ListGroupsOlderThanOrderingIdResponseTypeDef",
    ) -> "dc_td.ListGroupsOlderThanOrderingIdResponse":
        return dc_td.ListGroupsOlderThanOrderingIdResponse.make_one(res)

    def list_indices(
        self,
        res: "bs_td.ListIndicesResponseTypeDef",
    ) -> "dc_td.ListIndicesResponse":
        return dc_td.ListIndicesResponse.make_one(res)

    def list_query_suggestions_block_lists(
        self,
        res: "bs_td.ListQuerySuggestionsBlockListsResponseTypeDef",
    ) -> "dc_td.ListQuerySuggestionsBlockListsResponse":
        return dc_td.ListQuerySuggestionsBlockListsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_thesauri(
        self,
        res: "bs_td.ListThesauriResponseTypeDef",
    ) -> "dc_td.ListThesauriResponse":
        return dc_td.ListThesauriResponse.make_one(res)

    def put_principal_mapping(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def query(
        self,
        res: "bs_td.QueryResultTypeDef",
    ) -> "dc_td.QueryResult":
        return dc_td.QueryResult.make_one(res)

    def retrieve(
        self,
        res: "bs_td.RetrieveResultTypeDef",
    ) -> "dc_td.RetrieveResult":
        return dc_td.RetrieveResult.make_one(res)

    def start_data_source_sync_job(
        self,
        res: "bs_td.StartDataSourceSyncJobResponseTypeDef",
    ) -> "dc_td.StartDataSourceSyncJobResponse":
        return dc_td.StartDataSourceSyncJobResponse.make_one(res)

    def stop_data_source_sync_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def submit_feedback(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_data_source(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_experience(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_featured_results_set(
        self,
        res: "bs_td.UpdateFeaturedResultsSetResponseTypeDef",
    ) -> "dc_td.UpdateFeaturedResultsSetResponse":
        return dc_td.UpdateFeaturedResultsSetResponse.make_one(res)

    def update_index(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_query_suggestions_block_list(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_query_suggestions_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_thesaurus(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


kendra_caster = KENDRACaster()
