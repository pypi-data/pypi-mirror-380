# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_support import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class AddCommunicationToCaseRequest:
    boto3_raw_data: "type_defs.AddCommunicationToCaseRequestTypeDef" = (
        dataclasses.field()
    )

    communicationBody = field("communicationBody")
    caseId = field("caseId")
    ccEmailAddresses = field("ccEmailAddresses")
    attachmentSetId = field("attachmentSetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddCommunicationToCaseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddCommunicationToCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentDetails:
    boto3_raw_data: "type_defs.AttachmentDetailsTypeDef" = dataclasses.field()

    attachmentId = field("attachmentId")
    fileName = field("fileName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentOutput:
    boto3_raw_data: "type_defs.AttachmentOutputTypeDef" = dataclasses.field()

    fileName = field("fileName")
    data = field("data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Category:
    boto3_raw_data: "type_defs.CategoryTypeDef" = dataclasses.field()

    code = field("code")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CategoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CategoryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateInterval:
    boto3_raw_data: "type_defs.DateIntervalTypeDef" = dataclasses.field()

    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateIntervalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateIntervalTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedHour:
    boto3_raw_data: "type_defs.SupportedHourTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SupportedHourTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SupportedHourTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCaseRequest:
    boto3_raw_data: "type_defs.CreateCaseRequestTypeDef" = dataclasses.field()

    subject = field("subject")
    communicationBody = field("communicationBody")
    serviceCode = field("serviceCode")
    severityCode = field("severityCode")
    categoryCode = field("categoryCode")
    ccEmailAddresses = field("ccEmailAddresses")
    language = field("language")
    issueType = field("issueType")
    attachmentSetId = field("attachmentSetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateCaseRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAttachmentRequest:
    boto3_raw_data: "type_defs.DescribeAttachmentRequestTypeDef" = dataclasses.field()

    attachmentId = field("attachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAttachmentRequestTypeDef"]
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
class DescribeCasesRequest:
    boto3_raw_data: "type_defs.DescribeCasesRequestTypeDef" = dataclasses.field()

    caseIdList = field("caseIdList")
    displayId = field("displayId")
    afterTime = field("afterTime")
    beforeTime = field("beforeTime")
    includeResolvedCases = field("includeResolvedCases")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    language = field("language")
    includeCommunications = field("includeCommunications")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCommunicationsRequest:
    boto3_raw_data: "type_defs.DescribeCommunicationsRequestTypeDef" = (
        dataclasses.field()
    )

    caseId = field("caseId")
    beforeTime = field("beforeTime")
    afterTime = field("afterTime")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCommunicationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCommunicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCreateCaseOptionsRequest:
    boto3_raw_data: "type_defs.DescribeCreateCaseOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    issueType = field("issueType")
    serviceCode = field("serviceCode")
    language = field("language")
    categoryCode = field("categoryCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCreateCaseOptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCreateCaseOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServicesRequest:
    boto3_raw_data: "type_defs.DescribeServicesRequestTypeDef" = dataclasses.field()

    serviceCodeList = field("serviceCodeList")
    language = field("language")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSeverityLevelsRequest:
    boto3_raw_data: "type_defs.DescribeSeverityLevelsRequestTypeDef" = (
        dataclasses.field()
    )

    language = field("language")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSeverityLevelsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSeverityLevelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SeverityLevel:
    boto3_raw_data: "type_defs.SeverityLevelTypeDef" = dataclasses.field()

    code = field("code")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SeverityLevelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SeverityLevelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSupportedLanguagesRequest:
    boto3_raw_data: "type_defs.DescribeSupportedLanguagesRequestTypeDef" = (
        dataclasses.field()
    )

    issueType = field("issueType")
    serviceCode = field("serviceCode")
    categoryCode = field("categoryCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSupportedLanguagesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSupportedLanguagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedLanguage:
    boto3_raw_data: "type_defs.SupportedLanguageTypeDef" = dataclasses.field()

    code = field("code")
    language = field("language")
    display = field("display")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SupportedLanguageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportedLanguageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedAdvisorCheckRefreshStatusesRequest:
    boto3_raw_data: (
        "type_defs.DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef"
    ) = dataclasses.field()

    checkIds = field("checkIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedAdvisorCheckRefreshStatus:
    boto3_raw_data: "type_defs.TrustedAdvisorCheckRefreshStatusTypeDef" = (
        dataclasses.field()
    )

    checkId = field("checkId")
    status = field("status")
    millisUntilNextRefreshable = field("millisUntilNextRefreshable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TrustedAdvisorCheckRefreshStatusTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedAdvisorCheckRefreshStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedAdvisorCheckResultRequest:
    boto3_raw_data: "type_defs.DescribeTrustedAdvisorCheckResultRequestTypeDef" = (
        dataclasses.field()
    )

    checkId = field("checkId")
    language = field("language")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedAdvisorCheckResultRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustedAdvisorCheckResultRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedAdvisorCheckSummariesRequest:
    boto3_raw_data: "type_defs.DescribeTrustedAdvisorCheckSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    checkIds = field("checkIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedAdvisorCheckSummariesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustedAdvisorCheckSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedAdvisorChecksRequest:
    boto3_raw_data: "type_defs.DescribeTrustedAdvisorChecksRequestTypeDef" = (
        dataclasses.field()
    )

    language = field("language")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedAdvisorChecksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustedAdvisorChecksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedAdvisorCheckDescription:
    boto3_raw_data: "type_defs.TrustedAdvisorCheckDescriptionTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    description = field("description")
    category = field("category")
    metadata = field("metadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TrustedAdvisorCheckDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedAdvisorCheckDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshTrustedAdvisorCheckRequest:
    boto3_raw_data: "type_defs.RefreshTrustedAdvisorCheckRequestTypeDef" = (
        dataclasses.field()
    )

    checkId = field("checkId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RefreshTrustedAdvisorCheckRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshTrustedAdvisorCheckRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolveCaseRequest:
    boto3_raw_data: "type_defs.ResolveCaseRequestTypeDef" = dataclasses.field()

    caseId = field("caseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolveCaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolveCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedAdvisorCostOptimizingSummary:
    boto3_raw_data: "type_defs.TrustedAdvisorCostOptimizingSummaryTypeDef" = (
        dataclasses.field()
    )

    estimatedMonthlySavings = field("estimatedMonthlySavings")
    estimatedPercentMonthlySavings = field("estimatedPercentMonthlySavings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrustedAdvisorCostOptimizingSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedAdvisorCostOptimizingSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedAdvisorResourceDetail:
    boto3_raw_data: "type_defs.TrustedAdvisorResourceDetailTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    resourceId = field("resourceId")
    metadata = field("metadata")
    region = field("region")
    isSuppressed = field("isSuppressed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustedAdvisorResourceDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedAdvisorResourceDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedAdvisorResourcesSummary:
    boto3_raw_data: "type_defs.TrustedAdvisorResourcesSummaryTypeDef" = (
        dataclasses.field()
    )

    resourcesProcessed = field("resourcesProcessed")
    resourcesFlagged = field("resourcesFlagged")
    resourcesIgnored = field("resourcesIgnored")
    resourcesSuppressed = field("resourcesSuppressed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TrustedAdvisorResourcesSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedAdvisorResourcesSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddAttachmentsToSetResponse:
    boto3_raw_data: "type_defs.AddAttachmentsToSetResponseTypeDef" = dataclasses.field()

    attachmentSetId = field("attachmentSetId")
    expiryTime = field("expiryTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddAttachmentsToSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddAttachmentsToSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddCommunicationToCaseResponse:
    boto3_raw_data: "type_defs.AddCommunicationToCaseResponseTypeDef" = (
        dataclasses.field()
    )

    result = field("result")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddCommunicationToCaseResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddCommunicationToCaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCaseResponse:
    boto3_raw_data: "type_defs.CreateCaseResponseTypeDef" = dataclasses.field()

    caseId = field("caseId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolveCaseResponse:
    boto3_raw_data: "type_defs.ResolveCaseResponseTypeDef" = dataclasses.field()

    initialCaseStatus = field("initialCaseStatus")
    finalCaseStatus = field("finalCaseStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolveCaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolveCaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Communication:
    boto3_raw_data: "type_defs.CommunicationTypeDef" = dataclasses.field()

    caseId = field("caseId")
    body = field("body")
    submittedBy = field("submittedBy")
    timeCreated = field("timeCreated")

    @cached_property
    def attachmentSet(self):  # pragma: no cover
        return AttachmentDetails.make_many(self.boto3_raw_data["attachmentSet"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommunicationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommunicationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAttachmentResponse:
    boto3_raw_data: "type_defs.DescribeAttachmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def attachment(self):  # pragma: no cover
        return AttachmentOutput.make_one(self.boto3_raw_data["attachment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAttachmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attachment:
    boto3_raw_data: "type_defs.AttachmentTypeDef" = dataclasses.field()

    fileName = field("fileName")
    data = field("data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Service:
    boto3_raw_data: "type_defs.ServiceTypeDef" = dataclasses.field()

    code = field("code")
    name = field("name")

    @cached_property
    def categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["categories"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommunicationTypeOptions:
    boto3_raw_data: "type_defs.CommunicationTypeOptionsTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def supportedHours(self):  # pragma: no cover
        return SupportedHour.make_many(self.boto3_raw_data["supportedHours"])

    @cached_property
    def datesWithoutSupport(self):  # pragma: no cover
        return DateInterval.make_many(self.boto3_raw_data["datesWithoutSupport"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommunicationTypeOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommunicationTypeOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCasesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeCasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    caseIdList = field("caseIdList")
    displayId = field("displayId")
    afterTime = field("afterTime")
    beforeTime = field("beforeTime")
    includeResolvedCases = field("includeResolvedCases")
    language = field("language")
    includeCommunications = field("includeCommunications")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCasesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCommunicationsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeCommunicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    caseId = field("caseId")
    beforeTime = field("beforeTime")
    afterTime = field("afterTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCommunicationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCommunicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSeverityLevelsResponse:
    boto3_raw_data: "type_defs.DescribeSeverityLevelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def severityLevels(self):  # pragma: no cover
        return SeverityLevel.make_many(self.boto3_raw_data["severityLevels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSeverityLevelsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSeverityLevelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSupportedLanguagesResponse:
    boto3_raw_data: "type_defs.DescribeSupportedLanguagesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def supportedLanguages(self):  # pragma: no cover
        return SupportedLanguage.make_many(self.boto3_raw_data["supportedLanguages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSupportedLanguagesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSupportedLanguagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedAdvisorCheckRefreshStatusesResponse:
    boto3_raw_data: (
        "type_defs.DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def statuses(self):  # pragma: no cover
        return TrustedAdvisorCheckRefreshStatus.make_many(
            self.boto3_raw_data["statuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshTrustedAdvisorCheckResponse:
    boto3_raw_data: "type_defs.RefreshTrustedAdvisorCheckResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def status(self):  # pragma: no cover
        return TrustedAdvisorCheckRefreshStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RefreshTrustedAdvisorCheckResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshTrustedAdvisorCheckResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedAdvisorChecksResponse:
    boto3_raw_data: "type_defs.DescribeTrustedAdvisorChecksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def checks(self):  # pragma: no cover
        return TrustedAdvisorCheckDescription.make_many(self.boto3_raw_data["checks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedAdvisorChecksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustedAdvisorChecksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedAdvisorCategorySpecificSummary:
    boto3_raw_data: "type_defs.TrustedAdvisorCategorySpecificSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def costOptimizing(self):  # pragma: no cover
        return TrustedAdvisorCostOptimizingSummary.make_one(
            self.boto3_raw_data["costOptimizing"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrustedAdvisorCategorySpecificSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedAdvisorCategorySpecificSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCommunicationsResponse:
    boto3_raw_data: "type_defs.DescribeCommunicationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def communications(self):  # pragma: no cover
        return Communication.make_many(self.boto3_raw_data["communications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCommunicationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCommunicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecentCaseCommunications:
    boto3_raw_data: "type_defs.RecentCaseCommunicationsTypeDef" = dataclasses.field()

    @cached_property
    def communications(self):  # pragma: no cover
        return Communication.make_many(self.boto3_raw_data["communications"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecentCaseCommunicationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecentCaseCommunicationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServicesResponse:
    boto3_raw_data: "type_defs.DescribeServicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def services(self):  # pragma: no cover
        return Service.make_many(self.boto3_raw_data["services"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCreateCaseOptionsResponse:
    boto3_raw_data: "type_defs.DescribeCreateCaseOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    languageAvailability = field("languageAvailability")

    @cached_property
    def communicationTypes(self):  # pragma: no cover
        return CommunicationTypeOptions.make_many(
            self.boto3_raw_data["communicationTypes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCreateCaseOptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCreateCaseOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedAdvisorCheckResult:
    boto3_raw_data: "type_defs.TrustedAdvisorCheckResultTypeDef" = dataclasses.field()

    checkId = field("checkId")
    timestamp = field("timestamp")
    status = field("status")

    @cached_property
    def resourcesSummary(self):  # pragma: no cover
        return TrustedAdvisorResourcesSummary.make_one(
            self.boto3_raw_data["resourcesSummary"]
        )

    @cached_property
    def categorySpecificSummary(self):  # pragma: no cover
        return TrustedAdvisorCategorySpecificSummary.make_one(
            self.boto3_raw_data["categorySpecificSummary"]
        )

    @cached_property
    def flaggedResources(self):  # pragma: no cover
        return TrustedAdvisorResourceDetail.make_many(
            self.boto3_raw_data["flaggedResources"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustedAdvisorCheckResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedAdvisorCheckResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedAdvisorCheckSummary:
    boto3_raw_data: "type_defs.TrustedAdvisorCheckSummaryTypeDef" = dataclasses.field()

    checkId = field("checkId")
    timestamp = field("timestamp")
    status = field("status")

    @cached_property
    def resourcesSummary(self):  # pragma: no cover
        return TrustedAdvisorResourcesSummary.make_one(
            self.boto3_raw_data["resourcesSummary"]
        )

    @cached_property
    def categorySpecificSummary(self):  # pragma: no cover
        return TrustedAdvisorCategorySpecificSummary.make_one(
            self.boto3_raw_data["categorySpecificSummary"]
        )

    hasFlaggedResources = field("hasFlaggedResources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustedAdvisorCheckSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedAdvisorCheckSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseDetails:
    boto3_raw_data: "type_defs.CaseDetailsTypeDef" = dataclasses.field()

    caseId = field("caseId")
    displayId = field("displayId")
    subject = field("subject")
    status = field("status")
    serviceCode = field("serviceCode")
    categoryCode = field("categoryCode")
    severityCode = field("severityCode")
    submittedBy = field("submittedBy")
    timeCreated = field("timeCreated")

    @cached_property
    def recentCommunications(self):  # pragma: no cover
        return RecentCaseCommunications.make_one(
            self.boto3_raw_data["recentCommunications"]
        )

    ccEmailAddresses = field("ccEmailAddresses")
    language = field("language")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaseDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaseDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddAttachmentsToSetRequest:
    boto3_raw_data: "type_defs.AddAttachmentsToSetRequestTypeDef" = dataclasses.field()

    attachments = field("attachments")
    attachmentSetId = field("attachmentSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddAttachmentsToSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddAttachmentsToSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedAdvisorCheckResultResponse:
    boto3_raw_data: "type_defs.DescribeTrustedAdvisorCheckResultResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def result(self):  # pragma: no cover
        return TrustedAdvisorCheckResult.make_one(self.boto3_raw_data["result"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedAdvisorCheckResultResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustedAdvisorCheckResultResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedAdvisorCheckSummariesResponse:
    boto3_raw_data: "type_defs.DescribeTrustedAdvisorCheckSummariesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def summaries(self):  # pragma: no cover
        return TrustedAdvisorCheckSummary.make_many(self.boto3_raw_data["summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedAdvisorCheckSummariesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustedAdvisorCheckSummariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCasesResponse:
    boto3_raw_data: "type_defs.DescribeCasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def cases(self):  # pragma: no cover
        return CaseDetails.make_many(self.boto3_raw_data["cases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
