# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_migrationhubstrategy import type_defs as bs_td


class MIGRATIONHUBSTRATEGYCaster:

    def get_application_component_details(
        self,
        res: "bs_td.GetApplicationComponentDetailsResponseTypeDef",
    ) -> "dc_td.GetApplicationComponentDetailsResponse":
        return dc_td.GetApplicationComponentDetailsResponse.make_one(res)

    def get_application_component_strategies(
        self,
        res: "bs_td.GetApplicationComponentStrategiesResponseTypeDef",
    ) -> "dc_td.GetApplicationComponentStrategiesResponse":
        return dc_td.GetApplicationComponentStrategiesResponse.make_one(res)

    def get_assessment(
        self,
        res: "bs_td.GetAssessmentResponseTypeDef",
    ) -> "dc_td.GetAssessmentResponse":
        return dc_td.GetAssessmentResponse.make_one(res)

    def get_import_file_task(
        self,
        res: "bs_td.GetImportFileTaskResponseTypeDef",
    ) -> "dc_td.GetImportFileTaskResponse":
        return dc_td.GetImportFileTaskResponse.make_one(res)

    def get_latest_assessment_id(
        self,
        res: "bs_td.GetLatestAssessmentIdResponseTypeDef",
    ) -> "dc_td.GetLatestAssessmentIdResponse":
        return dc_td.GetLatestAssessmentIdResponse.make_one(res)

    def get_portfolio_preferences(
        self,
        res: "bs_td.GetPortfolioPreferencesResponseTypeDef",
    ) -> "dc_td.GetPortfolioPreferencesResponse":
        return dc_td.GetPortfolioPreferencesResponse.make_one(res)

    def get_portfolio_summary(
        self,
        res: "bs_td.GetPortfolioSummaryResponseTypeDef",
    ) -> "dc_td.GetPortfolioSummaryResponse":
        return dc_td.GetPortfolioSummaryResponse.make_one(res)

    def get_recommendation_report_details(
        self,
        res: "bs_td.GetRecommendationReportDetailsResponseTypeDef",
    ) -> "dc_td.GetRecommendationReportDetailsResponse":
        return dc_td.GetRecommendationReportDetailsResponse.make_one(res)

    def get_server_details(
        self,
        res: "bs_td.GetServerDetailsResponseTypeDef",
    ) -> "dc_td.GetServerDetailsResponse":
        return dc_td.GetServerDetailsResponse.make_one(res)

    def get_server_strategies(
        self,
        res: "bs_td.GetServerStrategiesResponseTypeDef",
    ) -> "dc_td.GetServerStrategiesResponse":
        return dc_td.GetServerStrategiesResponse.make_one(res)

    def list_analyzable_servers(
        self,
        res: "bs_td.ListAnalyzableServersResponseTypeDef",
    ) -> "dc_td.ListAnalyzableServersResponse":
        return dc_td.ListAnalyzableServersResponse.make_one(res)

    def list_application_components(
        self,
        res: "bs_td.ListApplicationComponentsResponseTypeDef",
    ) -> "dc_td.ListApplicationComponentsResponse":
        return dc_td.ListApplicationComponentsResponse.make_one(res)

    def list_collectors(
        self,
        res: "bs_td.ListCollectorsResponseTypeDef",
    ) -> "dc_td.ListCollectorsResponse":
        return dc_td.ListCollectorsResponse.make_one(res)

    def list_import_file_task(
        self,
        res: "bs_td.ListImportFileTaskResponseTypeDef",
    ) -> "dc_td.ListImportFileTaskResponse":
        return dc_td.ListImportFileTaskResponse.make_one(res)

    def list_servers(
        self,
        res: "bs_td.ListServersResponseTypeDef",
    ) -> "dc_td.ListServersResponse":
        return dc_td.ListServersResponse.make_one(res)

    def start_assessment(
        self,
        res: "bs_td.StartAssessmentResponseTypeDef",
    ) -> "dc_td.StartAssessmentResponse":
        return dc_td.StartAssessmentResponse.make_one(res)

    def start_import_file_task(
        self,
        res: "bs_td.StartImportFileTaskResponseTypeDef",
    ) -> "dc_td.StartImportFileTaskResponse":
        return dc_td.StartImportFileTaskResponse.make_one(res)

    def start_recommendation_report_generation(
        self,
        res: "bs_td.StartRecommendationReportGenerationResponseTypeDef",
    ) -> "dc_td.StartRecommendationReportGenerationResponse":
        return dc_td.StartRecommendationReportGenerationResponse.make_one(res)


migrationhubstrategy_caster = MIGRATIONHUBSTRATEGYCaster()
