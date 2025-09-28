# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_transcribe import type_defs as bs_td


class TRANSCRIBECaster:

    def create_call_analytics_category(
        self,
        res: "bs_td.CreateCallAnalyticsCategoryResponseTypeDef",
    ) -> "dc_td.CreateCallAnalyticsCategoryResponse":
        return dc_td.CreateCallAnalyticsCategoryResponse.make_one(res)

    def create_language_model(
        self,
        res: "bs_td.CreateLanguageModelResponseTypeDef",
    ) -> "dc_td.CreateLanguageModelResponse":
        return dc_td.CreateLanguageModelResponse.make_one(res)

    def create_medical_vocabulary(
        self,
        res: "bs_td.CreateMedicalVocabularyResponseTypeDef",
    ) -> "dc_td.CreateMedicalVocabularyResponse":
        return dc_td.CreateMedicalVocabularyResponse.make_one(res)

    def create_vocabulary(
        self,
        res: "bs_td.CreateVocabularyResponseTypeDef",
    ) -> "dc_td.CreateVocabularyResponse":
        return dc_td.CreateVocabularyResponse.make_one(res)

    def create_vocabulary_filter(
        self,
        res: "bs_td.CreateVocabularyFilterResponseTypeDef",
    ) -> "dc_td.CreateVocabularyFilterResponse":
        return dc_td.CreateVocabularyFilterResponse.make_one(res)

    def delete_language_model(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_medical_scribe_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_medical_transcription_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_medical_vocabulary(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_transcription_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vocabulary(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vocabulary_filter(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_language_model(
        self,
        res: "bs_td.DescribeLanguageModelResponseTypeDef",
    ) -> "dc_td.DescribeLanguageModelResponse":
        return dc_td.DescribeLanguageModelResponse.make_one(res)

    def get_call_analytics_category(
        self,
        res: "bs_td.GetCallAnalyticsCategoryResponseTypeDef",
    ) -> "dc_td.GetCallAnalyticsCategoryResponse":
        return dc_td.GetCallAnalyticsCategoryResponse.make_one(res)

    def get_call_analytics_job(
        self,
        res: "bs_td.GetCallAnalyticsJobResponseTypeDef",
    ) -> "dc_td.GetCallAnalyticsJobResponse":
        return dc_td.GetCallAnalyticsJobResponse.make_one(res)

    def get_medical_scribe_job(
        self,
        res: "bs_td.GetMedicalScribeJobResponseTypeDef",
    ) -> "dc_td.GetMedicalScribeJobResponse":
        return dc_td.GetMedicalScribeJobResponse.make_one(res)

    def get_medical_transcription_job(
        self,
        res: "bs_td.GetMedicalTranscriptionJobResponseTypeDef",
    ) -> "dc_td.GetMedicalTranscriptionJobResponse":
        return dc_td.GetMedicalTranscriptionJobResponse.make_one(res)

    def get_medical_vocabulary(
        self,
        res: "bs_td.GetMedicalVocabularyResponseTypeDef",
    ) -> "dc_td.GetMedicalVocabularyResponse":
        return dc_td.GetMedicalVocabularyResponse.make_one(res)

    def get_transcription_job(
        self,
        res: "bs_td.GetTranscriptionJobResponseTypeDef",
    ) -> "dc_td.GetTranscriptionJobResponse":
        return dc_td.GetTranscriptionJobResponse.make_one(res)

    def get_vocabulary(
        self,
        res: "bs_td.GetVocabularyResponseTypeDef",
    ) -> "dc_td.GetVocabularyResponse":
        return dc_td.GetVocabularyResponse.make_one(res)

    def get_vocabulary_filter(
        self,
        res: "bs_td.GetVocabularyFilterResponseTypeDef",
    ) -> "dc_td.GetVocabularyFilterResponse":
        return dc_td.GetVocabularyFilterResponse.make_one(res)

    def list_call_analytics_categories(
        self,
        res: "bs_td.ListCallAnalyticsCategoriesResponseTypeDef",
    ) -> "dc_td.ListCallAnalyticsCategoriesResponse":
        return dc_td.ListCallAnalyticsCategoriesResponse.make_one(res)

    def list_call_analytics_jobs(
        self,
        res: "bs_td.ListCallAnalyticsJobsResponseTypeDef",
    ) -> "dc_td.ListCallAnalyticsJobsResponse":
        return dc_td.ListCallAnalyticsJobsResponse.make_one(res)

    def list_language_models(
        self,
        res: "bs_td.ListLanguageModelsResponseTypeDef",
    ) -> "dc_td.ListLanguageModelsResponse":
        return dc_td.ListLanguageModelsResponse.make_one(res)

    def list_medical_scribe_jobs(
        self,
        res: "bs_td.ListMedicalScribeJobsResponseTypeDef",
    ) -> "dc_td.ListMedicalScribeJobsResponse":
        return dc_td.ListMedicalScribeJobsResponse.make_one(res)

    def list_medical_transcription_jobs(
        self,
        res: "bs_td.ListMedicalTranscriptionJobsResponseTypeDef",
    ) -> "dc_td.ListMedicalTranscriptionJobsResponse":
        return dc_td.ListMedicalTranscriptionJobsResponse.make_one(res)

    def list_medical_vocabularies(
        self,
        res: "bs_td.ListMedicalVocabulariesResponseTypeDef",
    ) -> "dc_td.ListMedicalVocabulariesResponse":
        return dc_td.ListMedicalVocabulariesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_transcription_jobs(
        self,
        res: "bs_td.ListTranscriptionJobsResponseTypeDef",
    ) -> "dc_td.ListTranscriptionJobsResponse":
        return dc_td.ListTranscriptionJobsResponse.make_one(res)

    def list_vocabularies(
        self,
        res: "bs_td.ListVocabulariesResponseTypeDef",
    ) -> "dc_td.ListVocabulariesResponse":
        return dc_td.ListVocabulariesResponse.make_one(res)

    def list_vocabulary_filters(
        self,
        res: "bs_td.ListVocabularyFiltersResponseTypeDef",
    ) -> "dc_td.ListVocabularyFiltersResponse":
        return dc_td.ListVocabularyFiltersResponse.make_one(res)

    def start_call_analytics_job(
        self,
        res: "bs_td.StartCallAnalyticsJobResponseTypeDef",
    ) -> "dc_td.StartCallAnalyticsJobResponse":
        return dc_td.StartCallAnalyticsJobResponse.make_one(res)

    def start_medical_scribe_job(
        self,
        res: "bs_td.StartMedicalScribeJobResponseTypeDef",
    ) -> "dc_td.StartMedicalScribeJobResponse":
        return dc_td.StartMedicalScribeJobResponse.make_one(res)

    def start_medical_transcription_job(
        self,
        res: "bs_td.StartMedicalTranscriptionJobResponseTypeDef",
    ) -> "dc_td.StartMedicalTranscriptionJobResponse":
        return dc_td.StartMedicalTranscriptionJobResponse.make_one(res)

    def start_transcription_job(
        self,
        res: "bs_td.StartTranscriptionJobResponseTypeDef",
    ) -> "dc_td.StartTranscriptionJobResponse":
        return dc_td.StartTranscriptionJobResponse.make_one(res)

    def update_call_analytics_category(
        self,
        res: "bs_td.UpdateCallAnalyticsCategoryResponseTypeDef",
    ) -> "dc_td.UpdateCallAnalyticsCategoryResponse":
        return dc_td.UpdateCallAnalyticsCategoryResponse.make_one(res)

    def update_medical_vocabulary(
        self,
        res: "bs_td.UpdateMedicalVocabularyResponseTypeDef",
    ) -> "dc_td.UpdateMedicalVocabularyResponse":
        return dc_td.UpdateMedicalVocabularyResponse.make_one(res)

    def update_vocabulary(
        self,
        res: "bs_td.UpdateVocabularyResponseTypeDef",
    ) -> "dc_td.UpdateVocabularyResponse":
        return dc_td.UpdateVocabularyResponse.make_one(res)

    def update_vocabulary_filter(
        self,
        res: "bs_td.UpdateVocabularyFilterResponseTypeDef",
    ) -> "dc_td.UpdateVocabularyFilterResponse":
        return dc_td.UpdateVocabularyFilterResponse.make_one(res)


transcribe_caster = TRANSCRIBECaster()
