# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_support import type_defs as bs_td


class SUPPORTCaster:

    def add_attachments_to_set(
        self,
        res: "bs_td.AddAttachmentsToSetResponseTypeDef",
    ) -> "dc_td.AddAttachmentsToSetResponse":
        return dc_td.AddAttachmentsToSetResponse.make_one(res)

    def add_communication_to_case(
        self,
        res: "bs_td.AddCommunicationToCaseResponseTypeDef",
    ) -> "dc_td.AddCommunicationToCaseResponse":
        return dc_td.AddCommunicationToCaseResponse.make_one(res)

    def create_case(
        self,
        res: "bs_td.CreateCaseResponseTypeDef",
    ) -> "dc_td.CreateCaseResponse":
        return dc_td.CreateCaseResponse.make_one(res)

    def describe_attachment(
        self,
        res: "bs_td.DescribeAttachmentResponseTypeDef",
    ) -> "dc_td.DescribeAttachmentResponse":
        return dc_td.DescribeAttachmentResponse.make_one(res)

    def describe_cases(
        self,
        res: "bs_td.DescribeCasesResponseTypeDef",
    ) -> "dc_td.DescribeCasesResponse":
        return dc_td.DescribeCasesResponse.make_one(res)

    def describe_communications(
        self,
        res: "bs_td.DescribeCommunicationsResponseTypeDef",
    ) -> "dc_td.DescribeCommunicationsResponse":
        return dc_td.DescribeCommunicationsResponse.make_one(res)

    def describe_create_case_options(
        self,
        res: "bs_td.DescribeCreateCaseOptionsResponseTypeDef",
    ) -> "dc_td.DescribeCreateCaseOptionsResponse":
        return dc_td.DescribeCreateCaseOptionsResponse.make_one(res)

    def describe_services(
        self,
        res: "bs_td.DescribeServicesResponseTypeDef",
    ) -> "dc_td.DescribeServicesResponse":
        return dc_td.DescribeServicesResponse.make_one(res)

    def describe_severity_levels(
        self,
        res: "bs_td.DescribeSeverityLevelsResponseTypeDef",
    ) -> "dc_td.DescribeSeverityLevelsResponse":
        return dc_td.DescribeSeverityLevelsResponse.make_one(res)

    def describe_supported_languages(
        self,
        res: "bs_td.DescribeSupportedLanguagesResponseTypeDef",
    ) -> "dc_td.DescribeSupportedLanguagesResponse":
        return dc_td.DescribeSupportedLanguagesResponse.make_one(res)

    def describe_trusted_advisor_check_refresh_statuses(
        self,
        res: "bs_td.DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    ) -> "dc_td.DescribeTrustedAdvisorCheckRefreshStatusesResponse":
        return dc_td.DescribeTrustedAdvisorCheckRefreshStatusesResponse.make_one(res)

    def describe_trusted_advisor_check_result(
        self,
        res: "bs_td.DescribeTrustedAdvisorCheckResultResponseTypeDef",
    ) -> "dc_td.DescribeTrustedAdvisorCheckResultResponse":
        return dc_td.DescribeTrustedAdvisorCheckResultResponse.make_one(res)

    def describe_trusted_advisor_check_summaries(
        self,
        res: "bs_td.DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    ) -> "dc_td.DescribeTrustedAdvisorCheckSummariesResponse":
        return dc_td.DescribeTrustedAdvisorCheckSummariesResponse.make_one(res)

    def describe_trusted_advisor_checks(
        self,
        res: "bs_td.DescribeTrustedAdvisorChecksResponseTypeDef",
    ) -> "dc_td.DescribeTrustedAdvisorChecksResponse":
        return dc_td.DescribeTrustedAdvisorChecksResponse.make_one(res)

    def refresh_trusted_advisor_check(
        self,
        res: "bs_td.RefreshTrustedAdvisorCheckResponseTypeDef",
    ) -> "dc_td.RefreshTrustedAdvisorCheckResponse":
        return dc_td.RefreshTrustedAdvisorCheckResponse.make_one(res)

    def resolve_case(
        self,
        res: "bs_td.ResolveCaseResponseTypeDef",
    ) -> "dc_td.ResolveCaseResponse":
        return dc_td.ResolveCaseResponse.make_one(res)


support_caster = SUPPORTCaster()
