# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_textract import type_defs as bs_td


class TEXTRACTCaster:

    def analyze_document(
        self,
        res: "bs_td.AnalyzeDocumentResponseTypeDef",
    ) -> "dc_td.AnalyzeDocumentResponse":
        return dc_td.AnalyzeDocumentResponse.make_one(res)

    def analyze_expense(
        self,
        res: "bs_td.AnalyzeExpenseResponseTypeDef",
    ) -> "dc_td.AnalyzeExpenseResponse":
        return dc_td.AnalyzeExpenseResponse.make_one(res)

    def analyze_id(
        self,
        res: "bs_td.AnalyzeIDResponseTypeDef",
    ) -> "dc_td.AnalyzeIDResponse":
        return dc_td.AnalyzeIDResponse.make_one(res)

    def create_adapter(
        self,
        res: "bs_td.CreateAdapterResponseTypeDef",
    ) -> "dc_td.CreateAdapterResponse":
        return dc_td.CreateAdapterResponse.make_one(res)

    def create_adapter_version(
        self,
        res: "bs_td.CreateAdapterVersionResponseTypeDef",
    ) -> "dc_td.CreateAdapterVersionResponse":
        return dc_td.CreateAdapterVersionResponse.make_one(res)

    def detect_document_text(
        self,
        res: "bs_td.DetectDocumentTextResponseTypeDef",
    ) -> "dc_td.DetectDocumentTextResponse":
        return dc_td.DetectDocumentTextResponse.make_one(res)

    def get_adapter(
        self,
        res: "bs_td.GetAdapterResponseTypeDef",
    ) -> "dc_td.GetAdapterResponse":
        return dc_td.GetAdapterResponse.make_one(res)

    def get_adapter_version(
        self,
        res: "bs_td.GetAdapterVersionResponseTypeDef",
    ) -> "dc_td.GetAdapterVersionResponse":
        return dc_td.GetAdapterVersionResponse.make_one(res)

    def get_document_analysis(
        self,
        res: "bs_td.GetDocumentAnalysisResponseTypeDef",
    ) -> "dc_td.GetDocumentAnalysisResponse":
        return dc_td.GetDocumentAnalysisResponse.make_one(res)

    def get_document_text_detection(
        self,
        res: "bs_td.GetDocumentTextDetectionResponseTypeDef",
    ) -> "dc_td.GetDocumentTextDetectionResponse":
        return dc_td.GetDocumentTextDetectionResponse.make_one(res)

    def get_expense_analysis(
        self,
        res: "bs_td.GetExpenseAnalysisResponseTypeDef",
    ) -> "dc_td.GetExpenseAnalysisResponse":
        return dc_td.GetExpenseAnalysisResponse.make_one(res)

    def get_lending_analysis(
        self,
        res: "bs_td.GetLendingAnalysisResponseTypeDef",
    ) -> "dc_td.GetLendingAnalysisResponse":
        return dc_td.GetLendingAnalysisResponse.make_one(res)

    def get_lending_analysis_summary(
        self,
        res: "bs_td.GetLendingAnalysisSummaryResponseTypeDef",
    ) -> "dc_td.GetLendingAnalysisSummaryResponse":
        return dc_td.GetLendingAnalysisSummaryResponse.make_one(res)

    def list_adapter_versions(
        self,
        res: "bs_td.ListAdapterVersionsResponseTypeDef",
    ) -> "dc_td.ListAdapterVersionsResponse":
        return dc_td.ListAdapterVersionsResponse.make_one(res)

    def list_adapters(
        self,
        res: "bs_td.ListAdaptersResponseTypeDef",
    ) -> "dc_td.ListAdaptersResponse":
        return dc_td.ListAdaptersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_document_analysis(
        self,
        res: "bs_td.StartDocumentAnalysisResponseTypeDef",
    ) -> "dc_td.StartDocumentAnalysisResponse":
        return dc_td.StartDocumentAnalysisResponse.make_one(res)

    def start_document_text_detection(
        self,
        res: "bs_td.StartDocumentTextDetectionResponseTypeDef",
    ) -> "dc_td.StartDocumentTextDetectionResponse":
        return dc_td.StartDocumentTextDetectionResponse.make_one(res)

    def start_expense_analysis(
        self,
        res: "bs_td.StartExpenseAnalysisResponseTypeDef",
    ) -> "dc_td.StartExpenseAnalysisResponse":
        return dc_td.StartExpenseAnalysisResponse.make_one(res)

    def start_lending_analysis(
        self,
        res: "bs_td.StartLendingAnalysisResponseTypeDef",
    ) -> "dc_td.StartLendingAnalysisResponse":
        return dc_td.StartLendingAnalysisResponse.make_one(res)

    def update_adapter(
        self,
        res: "bs_td.UpdateAdapterResponseTypeDef",
    ) -> "dc_td.UpdateAdapterResponse":
        return dc_td.UpdateAdapterResponse.make_one(res)


textract_caster = TEXTRACTCaster()
