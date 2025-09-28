# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_trustedadvisor import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountRecommendationLifecycleSummary:
    boto3_raw_data: "type_defs.AccountRecommendationLifecycleSummaryTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    accountRecommendationArn = field("accountRecommendationArn")
    lastUpdatedAt = field("lastUpdatedAt")
    lifecycleStage = field("lifecycleStage")
    updateReason = field("updateReason")
    updateReasonCode = field("updateReasonCode")
    updatedOnBehalfOf = field("updatedOnBehalfOf")
    updatedOnBehalfOfJobTitle = field("updatedOnBehalfOfJobTitle")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AccountRecommendationLifecycleSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountRecommendationLifecycleSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationResourceExclusion:
    boto3_raw_data: "type_defs.RecommendationResourceExclusionTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    isExcluded = field("isExcluded")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RecommendationResourceExclusionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationResourceExclusionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


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
class UpdateRecommendationResourceExclusionError:
    boto3_raw_data: "type_defs.UpdateRecommendationResourceExclusionErrorTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRecommendationResourceExclusionErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecommendationResourceExclusionErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckSummary:
    boto3_raw_data: "type_defs.CheckSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    awsServices = field("awsServices")
    description = field("description")
    id = field("id")
    metadata = field("metadata")
    name = field("name")
    pillars = field("pillars")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CheckSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CheckSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationRecommendationRequest:
    boto3_raw_data: "type_defs.GetOrganizationRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    organizationRecommendationIdentifier = field("organizationRecommendationIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationRecommendationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOrganizationRecommendationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationRequest:
    boto3_raw_data: "type_defs.GetRecommendationRequestTypeDef" = dataclasses.field()

    recommendationIdentifier = field("recommendationIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationRequestTypeDef"]
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
class ListChecksRequest:
    boto3_raw_data: "type_defs.ListChecksRequestTypeDef" = dataclasses.field()

    awsService = field("awsService")
    language = field("language")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    pillar = field("pillar")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListChecksRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChecksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationRecommendationAccountsRequest:
    boto3_raw_data: "type_defs.ListOrganizationRecommendationAccountsRequestTypeDef" = (
        dataclasses.field()
    )

    organizationRecommendationIdentifier = field("organizationRecommendationIdentifier")
    affectedAccountId = field("affectedAccountId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationRecommendationAccountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationRecommendationAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationRecommendationResourcesRequest:
    boto3_raw_data: (
        "type_defs.ListOrganizationRecommendationResourcesRequestTypeDef"
    ) = dataclasses.field()

    organizationRecommendationIdentifier = field("organizationRecommendationIdentifier")
    affectedAccountId = field("affectedAccountId")
    exclusionStatus = field("exclusionStatus")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    regionCode = field("regionCode")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationRecommendationResourcesRequestTypeDef"
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
                "type_defs.ListOrganizationRecommendationResourcesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationRecommendationResourceSummary:
    boto3_raw_data: "type_defs.OrganizationRecommendationResourceSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    awsResourceId = field("awsResourceId")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    metadata = field("metadata")
    recommendationArn = field("recommendationArn")
    regionCode = field("regionCode")
    status = field("status")
    accountId = field("accountId")
    exclusionStatus = field("exclusionStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationRecommendationResourceSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationRecommendationResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationResourcesRequest:
    boto3_raw_data: "type_defs.ListRecommendationResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    recommendationIdentifier = field("recommendationIdentifier")
    exclusionStatus = field("exclusionStatus")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    regionCode = field("regionCode")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationResourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationResourceSummary:
    boto3_raw_data: "type_defs.RecommendationResourceSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    awsResourceId = field("awsResourceId")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    metadata = field("metadata")
    recommendationArn = field("recommendationArn")
    regionCode = field("regionCode")
    status = field("status")
    exclusionStatus = field("exclusionStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RecommendationResourceSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationResourcesAggregates:
    boto3_raw_data: "type_defs.RecommendationResourcesAggregatesTypeDef" = (
        dataclasses.field()
    )

    errorCount = field("errorCount")
    okCount = field("okCount")
    warningCount = field("warningCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecommendationResourcesAggregatesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationResourcesAggregatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationCostOptimizingAggregates:
    boto3_raw_data: "type_defs.RecommendationCostOptimizingAggregatesTypeDef" = (
        dataclasses.field()
    )

    estimatedMonthlySavings = field("estimatedMonthlySavings")
    estimatedPercentMonthlySavings = field("estimatedPercentMonthlySavings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecommendationCostOptimizingAggregatesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationCostOptimizingAggregatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOrganizationRecommendationLifecycleRequest:
    boto3_raw_data: (
        "type_defs.UpdateOrganizationRecommendationLifecycleRequestTypeDef"
    ) = dataclasses.field()

    lifecycleStage = field("lifecycleStage")
    organizationRecommendationIdentifier = field("organizationRecommendationIdentifier")
    updateReason = field("updateReason")
    updateReasonCode = field("updateReasonCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOrganizationRecommendationLifecycleRequestTypeDef"
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
                "type_defs.UpdateOrganizationRecommendationLifecycleRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecommendationLifecycleRequest:
    boto3_raw_data: "type_defs.UpdateRecommendationLifecycleRequestTypeDef" = (
        dataclasses.field()
    )

    lifecycleStage = field("lifecycleStage")
    recommendationIdentifier = field("recommendationIdentifier")
    updateReason = field("updateReason")
    updateReasonCode = field("updateReasonCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRecommendationLifecycleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecommendationLifecycleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateRecommendationResourceExclusionRequest:
    boto3_raw_data: (
        "type_defs.BatchUpdateRecommendationResourceExclusionRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def recommendationResourceExclusions(self):  # pragma: no cover
        return RecommendationResourceExclusion.make_many(
            self.boto3_raw_data["recommendationResourceExclusions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateRecommendationResourceExclusionRequestTypeDef"
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
                "type_defs.BatchUpdateRecommendationResourceExclusionRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationRecommendationAccountsResponse:
    boto3_raw_data: (
        "type_defs.ListOrganizationRecommendationAccountsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def accountRecommendationLifecycleSummaries(self):  # pragma: no cover
        return AccountRecommendationLifecycleSummary.make_many(
            self.boto3_raw_data["accountRecommendationLifecycleSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationRecommendationAccountsResponseTypeDef"
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
                "type_defs.ListOrganizationRecommendationAccountsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateRecommendationResourceExclusionResponse:
    boto3_raw_data: (
        "type_defs.BatchUpdateRecommendationResourceExclusionResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def batchUpdateRecommendationResourceExclusionErrors(self):  # pragma: no cover
        return UpdateRecommendationResourceExclusionError.make_many(
            self.boto3_raw_data["batchUpdateRecommendationResourceExclusionErrors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateRecommendationResourceExclusionResponseTypeDef"
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
                "type_defs.BatchUpdateRecommendationResourceExclusionResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChecksResponse:
    boto3_raw_data: "type_defs.ListChecksResponseTypeDef" = dataclasses.field()

    @cached_property
    def checkSummaries(self):  # pragma: no cover
        return CheckSummary.make_many(self.boto3_raw_data["checkSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChecksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChecksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChecksRequestPaginate:
    boto3_raw_data: "type_defs.ListChecksRequestPaginateTypeDef" = dataclasses.field()

    awsService = field("awsService")
    language = field("language")
    pillar = field("pillar")
    source = field("source")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChecksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChecksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationRecommendationAccountsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListOrganizationRecommendationAccountsRequestPaginateTypeDef"
    ) = dataclasses.field()

    organizationRecommendationIdentifier = field("organizationRecommendationIdentifier")
    affectedAccountId = field("affectedAccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationRecommendationAccountsRequestPaginateTypeDef"
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
                "type_defs.ListOrganizationRecommendationAccountsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationRecommendationResourcesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListOrganizationRecommendationResourcesRequestPaginateTypeDef"
    ) = dataclasses.field()

    organizationRecommendationIdentifier = field("organizationRecommendationIdentifier")
    affectedAccountId = field("affectedAccountId")
    exclusionStatus = field("exclusionStatus")
    regionCode = field("regionCode")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationRecommendationResourcesRequestPaginateTypeDef"
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
                "type_defs.ListOrganizationRecommendationResourcesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationResourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListRecommendationResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    recommendationIdentifier = field("recommendationIdentifier")
    exclusionStatus = field("exclusionStatus")
    regionCode = field("regionCode")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationRecommendationResourcesResponse:
    boto3_raw_data: (
        "type_defs.ListOrganizationRecommendationResourcesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def organizationRecommendationResourceSummaries(self):  # pragma: no cover
        return OrganizationRecommendationResourceSummary.make_many(
            self.boto3_raw_data["organizationRecommendationResourceSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationRecommendationResourcesResponseTypeDef"
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
                "type_defs.ListOrganizationRecommendationResourcesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationRecommendationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListOrganizationRecommendationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    afterLastUpdatedAt = field("afterLastUpdatedAt")
    awsService = field("awsService")
    beforeLastUpdatedAt = field("beforeLastUpdatedAt")
    checkIdentifier = field("checkIdentifier")
    pillar = field("pillar")
    source = field("source")
    status = field("status")
    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationRecommendationsRequestPaginateTypeDef"
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
                "type_defs.ListOrganizationRecommendationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationRecommendationsRequest:
    boto3_raw_data: "type_defs.ListOrganizationRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    afterLastUpdatedAt = field("afterLastUpdatedAt")
    awsService = field("awsService")
    beforeLastUpdatedAt = field("beforeLastUpdatedAt")
    checkIdentifier = field("checkIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    pillar = field("pillar")
    source = field("source")
    status = field("status")
    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsRequestPaginate:
    boto3_raw_data: "type_defs.ListRecommendationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    afterLastUpdatedAt = field("afterLastUpdatedAt")
    awsService = field("awsService")
    beforeLastUpdatedAt = field("beforeLastUpdatedAt")
    checkIdentifier = field("checkIdentifier")
    pillar = field("pillar")
    source = field("source")
    status = field("status")
    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsRequest:
    boto3_raw_data: "type_defs.ListRecommendationsRequestTypeDef" = dataclasses.field()

    afterLastUpdatedAt = field("afterLastUpdatedAt")
    awsService = field("awsService")
    beforeLastUpdatedAt = field("beforeLastUpdatedAt")
    checkIdentifier = field("checkIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    pillar = field("pillar")
    source = field("source")
    status = field("status")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationResourcesResponse:
    boto3_raw_data: "type_defs.ListRecommendationResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def recommendationResourceSummaries(self):  # pragma: no cover
        return RecommendationResourceSummary.make_many(
            self.boto3_raw_data["recommendationResourceSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationResourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationPillarSpecificAggregates:
    boto3_raw_data: "type_defs.RecommendationPillarSpecificAggregatesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def costOptimizing(self):  # pragma: no cover
        return RecommendationCostOptimizingAggregates.make_one(
            self.boto3_raw_data["costOptimizing"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecommendationPillarSpecificAggregatesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationPillarSpecificAggregatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationRecommendationSummary:
    boto3_raw_data: "type_defs.OrganizationRecommendationSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")
    name = field("name")
    pillars = field("pillars")

    @cached_property
    def resourcesAggregates(self):  # pragma: no cover
        return RecommendationResourcesAggregates.make_one(
            self.boto3_raw_data["resourcesAggregates"]
        )

    source = field("source")
    status = field("status")
    type = field("type")
    awsServices = field("awsServices")
    checkArn = field("checkArn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    lifecycleStage = field("lifecycleStage")

    @cached_property
    def pillarSpecificAggregates(self):  # pragma: no cover
        return RecommendationPillarSpecificAggregates.make_one(
            self.boto3_raw_data["pillarSpecificAggregates"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationRecommendationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationRecommendationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationRecommendation:
    boto3_raw_data: "type_defs.OrganizationRecommendationTypeDef" = dataclasses.field()

    arn = field("arn")
    description = field("description")
    id = field("id")
    name = field("name")
    pillars = field("pillars")

    @cached_property
    def resourcesAggregates(self):  # pragma: no cover
        return RecommendationResourcesAggregates.make_one(
            self.boto3_raw_data["resourcesAggregates"]
        )

    source = field("source")
    status = field("status")
    type = field("type")
    awsServices = field("awsServices")
    checkArn = field("checkArn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    lastUpdatedAt = field("lastUpdatedAt")
    lifecycleStage = field("lifecycleStage")

    @cached_property
    def pillarSpecificAggregates(self):  # pragma: no cover
        return RecommendationPillarSpecificAggregates.make_one(
            self.boto3_raw_data["pillarSpecificAggregates"]
        )

    resolvedAt = field("resolvedAt")
    updateReason = field("updateReason")
    updateReasonCode = field("updateReasonCode")
    updatedOnBehalfOf = field("updatedOnBehalfOf")
    updatedOnBehalfOfJobTitle = field("updatedOnBehalfOfJobTitle")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationSummary:
    boto3_raw_data: "type_defs.RecommendationSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    name = field("name")
    pillars = field("pillars")

    @cached_property
    def resourcesAggregates(self):  # pragma: no cover
        return RecommendationResourcesAggregates.make_one(
            self.boto3_raw_data["resourcesAggregates"]
        )

    source = field("source")
    status = field("status")
    type = field("type")
    awsServices = field("awsServices")
    checkArn = field("checkArn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    lifecycleStage = field("lifecycleStage")

    @cached_property
    def pillarSpecificAggregates(self):  # pragma: no cover
        return RecommendationPillarSpecificAggregates.make_one(
            self.boto3_raw_data["pillarSpecificAggregates"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recommendation:
    boto3_raw_data: "type_defs.RecommendationTypeDef" = dataclasses.field()

    arn = field("arn")
    description = field("description")
    id = field("id")
    name = field("name")
    pillars = field("pillars")

    @cached_property
    def resourcesAggregates(self):  # pragma: no cover
        return RecommendationResourcesAggregates.make_one(
            self.boto3_raw_data["resourcesAggregates"]
        )

    source = field("source")
    status = field("status")
    type = field("type")
    awsServices = field("awsServices")
    checkArn = field("checkArn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    lastUpdatedAt = field("lastUpdatedAt")
    lifecycleStage = field("lifecycleStage")

    @cached_property
    def pillarSpecificAggregates(self):  # pragma: no cover
        return RecommendationPillarSpecificAggregates.make_one(
            self.boto3_raw_data["pillarSpecificAggregates"]
        )

    resolvedAt = field("resolvedAt")
    updateReason = field("updateReason")
    updateReasonCode = field("updateReasonCode")
    updatedOnBehalfOf = field("updatedOnBehalfOf")
    updatedOnBehalfOfJobTitle = field("updatedOnBehalfOfJobTitle")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommendationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationRecommendationsResponse:
    boto3_raw_data: "type_defs.ListOrganizationRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def organizationRecommendationSummaries(self):  # pragma: no cover
        return OrganizationRecommendationSummary.make_many(
            self.boto3_raw_data["organizationRecommendationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationRecommendationResponse:
    boto3_raw_data: "type_defs.GetOrganizationRecommendationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def organizationRecommendation(self):  # pragma: no cover
        return OrganizationRecommendation.make_one(
            self.boto3_raw_data["organizationRecommendation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationRecommendationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOrganizationRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsResponse:
    boto3_raw_data: "type_defs.ListRecommendationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def recommendationSummaries(self):  # pragma: no cover
        return RecommendationSummary.make_many(
            self.boto3_raw_data["recommendationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationResponse:
    boto3_raw_data: "type_defs.GetRecommendationResponseTypeDef" = dataclasses.field()

    @cached_property
    def recommendation(self):  # pragma: no cover
        return Recommendation.make_one(self.boto3_raw_data["recommendation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
