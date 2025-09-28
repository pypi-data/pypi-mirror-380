# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_translate import type_defs as bs_td


class TRANSLATECaster:

    def create_parallel_data(
        self,
        res: "bs_td.CreateParallelDataResponseTypeDef",
    ) -> "dc_td.CreateParallelDataResponse":
        return dc_td.CreateParallelDataResponse.make_one(res)

    def delete_parallel_data(
        self,
        res: "bs_td.DeleteParallelDataResponseTypeDef",
    ) -> "dc_td.DeleteParallelDataResponse":
        return dc_td.DeleteParallelDataResponse.make_one(res)

    def delete_terminology(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_text_translation_job(
        self,
        res: "bs_td.DescribeTextTranslationJobResponseTypeDef",
    ) -> "dc_td.DescribeTextTranslationJobResponse":
        return dc_td.DescribeTextTranslationJobResponse.make_one(res)

    def get_parallel_data(
        self,
        res: "bs_td.GetParallelDataResponseTypeDef",
    ) -> "dc_td.GetParallelDataResponse":
        return dc_td.GetParallelDataResponse.make_one(res)

    def get_terminology(
        self,
        res: "bs_td.GetTerminologyResponseTypeDef",
    ) -> "dc_td.GetTerminologyResponse":
        return dc_td.GetTerminologyResponse.make_one(res)

    def import_terminology(
        self,
        res: "bs_td.ImportTerminologyResponseTypeDef",
    ) -> "dc_td.ImportTerminologyResponse":
        return dc_td.ImportTerminologyResponse.make_one(res)

    def list_languages(
        self,
        res: "bs_td.ListLanguagesResponseTypeDef",
    ) -> "dc_td.ListLanguagesResponse":
        return dc_td.ListLanguagesResponse.make_one(res)

    def list_parallel_data(
        self,
        res: "bs_td.ListParallelDataResponseTypeDef",
    ) -> "dc_td.ListParallelDataResponse":
        return dc_td.ListParallelDataResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_terminologies(
        self,
        res: "bs_td.ListTerminologiesResponseTypeDef",
    ) -> "dc_td.ListTerminologiesResponse":
        return dc_td.ListTerminologiesResponse.make_one(res)

    def list_text_translation_jobs(
        self,
        res: "bs_td.ListTextTranslationJobsResponseTypeDef",
    ) -> "dc_td.ListTextTranslationJobsResponse":
        return dc_td.ListTextTranslationJobsResponse.make_one(res)

    def start_text_translation_job(
        self,
        res: "bs_td.StartTextTranslationJobResponseTypeDef",
    ) -> "dc_td.StartTextTranslationJobResponse":
        return dc_td.StartTextTranslationJobResponse.make_one(res)

    def stop_text_translation_job(
        self,
        res: "bs_td.StopTextTranslationJobResponseTypeDef",
    ) -> "dc_td.StopTextTranslationJobResponse":
        return dc_td.StopTextTranslationJobResponse.make_one(res)

    def translate_document(
        self,
        res: "bs_td.TranslateDocumentResponseTypeDef",
    ) -> "dc_td.TranslateDocumentResponse":
        return dc_td.TranslateDocumentResponse.make_one(res)

    def translate_text(
        self,
        res: "bs_td.TranslateTextResponseTypeDef",
    ) -> "dc_td.TranslateTextResponse":
        return dc_td.TranslateTextResponse.make_one(res)

    def update_parallel_data(
        self,
        res: "bs_td.UpdateParallelDataResponseTypeDef",
    ) -> "dc_td.UpdateParallelDataResponse":
        return dc_td.UpdateParallelDataResponse.make_one(res)


translate_caster = TRANSLATECaster()
