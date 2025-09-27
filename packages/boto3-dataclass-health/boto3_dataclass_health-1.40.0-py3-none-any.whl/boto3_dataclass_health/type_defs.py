# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_health import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountEntityAggregate:
    boto3_raw_data: "type_defs.AccountEntityAggregateTypeDef" = dataclasses.field()

    accountId = field("accountId")
    count = field("count")
    statuses = field("statuses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountEntityAggregateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountEntityAggregateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AffectedEntity:
    boto3_raw_data: "type_defs.AffectedEntityTypeDef" = dataclasses.field()

    entityArn = field("entityArn")
    eventArn = field("eventArn")
    entityValue = field("entityValue")
    entityUrl = field("entityUrl")
    awsAccountId = field("awsAccountId")
    lastUpdatedTime = field("lastUpdatedTime")
    statusCode = field("statusCode")
    tags = field("tags")
    entityMetadata = field("entityMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AffectedEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AffectedEntityTypeDef"]],
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
class DescribeAffectedAccountsForOrganizationRequest:
    boto3_raw_data: (
        "type_defs.DescribeAffectedAccountsForOrganizationRequestTypeDef"
    ) = dataclasses.field()

    eventArn = field("eventArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAffectedAccountsForOrganizationRequestTypeDef"
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
                "type_defs.DescribeAffectedAccountsForOrganizationRequestTypeDef"
            ]
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
class EntityAccountFilter:
    boto3_raw_data: "type_defs.EntityAccountFilterTypeDef" = dataclasses.field()

    eventArn = field("eventArn")
    awsAccountId = field("awsAccountId")
    statusCodes = field("statusCodes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityAccountFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityAccountFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventAccountFilter:
    boto3_raw_data: "type_defs.EventAccountFilterTypeDef" = dataclasses.field()

    eventArn = field("eventArn")
    awsAccountId = field("awsAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventAccountFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventAccountFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationAffectedEntitiesErrorItem:
    boto3_raw_data: "type_defs.OrganizationAffectedEntitiesErrorItemTypeDef" = (
        dataclasses.field()
    )

    awsAccountId = field("awsAccountId")
    eventArn = field("eventArn")
    errorName = field("errorName")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationAffectedEntitiesErrorItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationAffectedEntitiesErrorItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityAggregatesForOrganizationRequest:
    boto3_raw_data: (
        "type_defs.DescribeEntityAggregatesForOrganizationRequestTypeDef"
    ) = dataclasses.field()

    eventArns = field("eventArns")
    awsAccountIds = field("awsAccountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEntityAggregatesForOrganizationRequestTypeDef"
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
                "type_defs.DescribeEntityAggregatesForOrganizationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityAggregatesRequest:
    boto3_raw_data: "type_defs.DescribeEntityAggregatesRequestTypeDef" = (
        dataclasses.field()
    )

    eventArns = field("eventArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEntityAggregatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntityAggregatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityAggregate:
    boto3_raw_data: "type_defs.EntityAggregateTypeDef" = dataclasses.field()

    eventArn = field("eventArn")
    count = field("count")
    statuses = field("statuses")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityAggregateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityAggregateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventAggregate:
    boto3_raw_data: "type_defs.EventAggregateTypeDef" = dataclasses.field()

    aggregateValue = field("aggregateValue")
    count = field("count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventAggregateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventAggregateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationEventDetailsErrorItem:
    boto3_raw_data: "type_defs.OrganizationEventDetailsErrorItemTypeDef" = (
        dataclasses.field()
    )

    awsAccountId = field("awsAccountId")
    eventArn = field("eventArn")
    errorName = field("errorName")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationEventDetailsErrorItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationEventDetailsErrorItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventDetailsRequest:
    boto3_raw_data: "type_defs.DescribeEventDetailsRequestTypeDef" = dataclasses.field()

    eventArns = field("eventArns")
    locale = field("locale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventDetailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDetailsErrorItem:
    boto3_raw_data: "type_defs.EventDetailsErrorItemTypeDef" = dataclasses.field()

    eventArn = field("eventArn")
    errorName = field("errorName")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventDetailsErrorItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDetailsErrorItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTypeFilter:
    boto3_raw_data: "type_defs.EventTypeFilterTypeDef" = dataclasses.field()

    eventTypeCodes = field("eventTypeCodes")
    services = field("services")
    eventTypeCategories = field("eventTypeCategories")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventType:
    boto3_raw_data: "type_defs.EventTypeTypeDef" = dataclasses.field()

    service = field("service")
    code = field("code")
    category = field("category")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationEvent:
    boto3_raw_data: "type_defs.OrganizationEventTypeDef" = dataclasses.field()

    arn = field("arn")
    service = field("service")
    eventTypeCode = field("eventTypeCode")
    eventTypeCategory = field("eventTypeCategory")
    eventScopeCode = field("eventScopeCode")
    region = field("region")
    startTime = field("startTime")
    endTime = field("endTime")
    lastUpdatedTime = field("lastUpdatedTime")
    statusCode = field("statusCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrganizationEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    arn = field("arn")
    service = field("service")
    eventTypeCode = field("eventTypeCode")
    eventTypeCategory = field("eventTypeCategory")
    region = field("region")
    availabilityZone = field("availabilityZone")
    startTime = field("startTime")
    endTime = field("endTime")
    lastUpdatedTime = field("lastUpdatedTime")
    statusCode = field("statusCode")
    eventScopeCode = field("eventScopeCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDescription:
    boto3_raw_data: "type_defs.EventDescriptionTypeDef" = dataclasses.field()

    latestDescription = field("latestDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationEntityAggregate:
    boto3_raw_data: "type_defs.OrganizationEntityAggregateTypeDef" = dataclasses.field()

    eventArn = field("eventArn")
    count = field("count")
    statuses = field("statuses")

    @cached_property
    def accounts(self):  # pragma: no cover
        return AccountEntityAggregate.make_many(self.boto3_raw_data["accounts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationEntityAggregateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationEntityAggregateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateTimeRange:
    boto3_raw_data: "type_defs.DateTimeRangeTypeDef" = dataclasses.field()

    from_ = field("from")
    to = field("to")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateTimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateTimeRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAffectedAccountsForOrganizationRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeAffectedAccountsForOrganizationRequestPaginateTypeDef"
    ) = dataclasses.field()

    eventArn = field("eventArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAffectedAccountsForOrganizationRequestPaginateTypeDef"
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
                "type_defs.DescribeAffectedAccountsForOrganizationRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAffectedAccountsForOrganizationResponse:
    boto3_raw_data: (
        "type_defs.DescribeAffectedAccountsForOrganizationResponseTypeDef"
    ) = dataclasses.field()

    affectedAccounts = field("affectedAccounts")
    eventScopeCode = field("eventScopeCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAffectedAccountsForOrganizationResponseTypeDef"
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
                "type_defs.DescribeAffectedAccountsForOrganizationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAffectedEntitiesResponse:
    boto3_raw_data: "type_defs.DescribeAffectedEntitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entities(self):  # pragma: no cover
        return AffectedEntity.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAffectedEntitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAffectedEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHealthServiceStatusForOrganizationResponse:
    boto3_raw_data: (
        "type_defs.DescribeHealthServiceStatusForOrganizationResponseTypeDef"
    ) = dataclasses.field()

    healthServiceAccessStatusForOrganization = field(
        "healthServiceAccessStatusForOrganization"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeHealthServiceStatusForOrganizationResponseTypeDef"
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
                "type_defs.DescribeHealthServiceStatusForOrganizationResponseTypeDef"
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
class DescribeAffectedEntitiesForOrganizationRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeAffectedEntitiesForOrganizationRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def organizationEntityFilters(self):  # pragma: no cover
        return EventAccountFilter.make_many(
            self.boto3_raw_data["organizationEntityFilters"]
        )

    locale = field("locale")

    @cached_property
    def organizationEntityAccountFilters(self):  # pragma: no cover
        return EntityAccountFilter.make_many(
            self.boto3_raw_data["organizationEntityAccountFilters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAffectedEntitiesForOrganizationRequestPaginateTypeDef"
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
                "type_defs.DescribeAffectedEntitiesForOrganizationRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAffectedEntitiesForOrganizationRequest:
    boto3_raw_data: (
        "type_defs.DescribeAffectedEntitiesForOrganizationRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def organizationEntityFilters(self):  # pragma: no cover
        return EventAccountFilter.make_many(
            self.boto3_raw_data["organizationEntityFilters"]
        )

    locale = field("locale")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def organizationEntityAccountFilters(self):  # pragma: no cover
        return EntityAccountFilter.make_many(
            self.boto3_raw_data["organizationEntityAccountFilters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAffectedEntitiesForOrganizationRequestTypeDef"
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
                "type_defs.DescribeAffectedEntitiesForOrganizationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventDetailsForOrganizationRequest:
    boto3_raw_data: "type_defs.DescribeEventDetailsForOrganizationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def organizationEventDetailFilters(self):  # pragma: no cover
        return EventAccountFilter.make_many(
            self.boto3_raw_data["organizationEventDetailFilters"]
        )

    locale = field("locale")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventDetailsForOrganizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventDetailsForOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAffectedEntitiesForOrganizationResponse:
    boto3_raw_data: (
        "type_defs.DescribeAffectedEntitiesForOrganizationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def entities(self):  # pragma: no cover
        return AffectedEntity.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def failedSet(self):  # pragma: no cover
        return OrganizationAffectedEntitiesErrorItem.make_many(
            self.boto3_raw_data["failedSet"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAffectedEntitiesForOrganizationResponseTypeDef"
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
                "type_defs.DescribeAffectedEntitiesForOrganizationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityAggregatesResponse:
    boto3_raw_data: "type_defs.DescribeEntityAggregatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entityAggregates(self):  # pragma: no cover
        return EntityAggregate.make_many(self.boto3_raw_data["entityAggregates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEntityAggregatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntityAggregatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventAggregatesResponse:
    boto3_raw_data: "type_defs.DescribeEventAggregatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def eventAggregates(self):  # pragma: no cover
        return EventAggregate.make_many(self.boto3_raw_data["eventAggregates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventAggregatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventAggregatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventTypesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeEventTypesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return EventTypeFilter.make_one(self.boto3_raw_data["filter"])

    locale = field("locale")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventTypesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventTypesRequest:
    boto3_raw_data: "type_defs.DescribeEventTypesRequestTypeDef" = dataclasses.field()

    @cached_property
    def filter(self):  # pragma: no cover
        return EventTypeFilter.make_one(self.boto3_raw_data["filter"])

    locale = field("locale")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventTypesResponse:
    boto3_raw_data: "type_defs.DescribeEventTypesResponseTypeDef" = dataclasses.field()

    @cached_property
    def eventTypes(self):  # pragma: no cover
        return EventType.make_many(self.boto3_raw_data["eventTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventTypesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsForOrganizationResponse:
    boto3_raw_data: "type_defs.DescribeEventsForOrganizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def events(self):  # pragma: no cover
        return OrganizationEvent.make_many(self.boto3_raw_data["events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventsForOrganizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsForOrganizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsResponse:
    boto3_raw_data: "type_defs.DescribeEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDetails:
    boto3_raw_data: "type_defs.EventDetailsTypeDef" = dataclasses.field()

    @cached_property
    def event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["event"])

    @cached_property
    def eventDescription(self):  # pragma: no cover
        return EventDescription.make_one(self.boto3_raw_data["eventDescription"])

    eventMetadata = field("eventMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationEventDetails:
    boto3_raw_data: "type_defs.OrganizationEventDetailsTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")

    @cached_property
    def event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["event"])

    @cached_property
    def eventDescription(self):  # pragma: no cover
        return EventDescription.make_one(self.boto3_raw_data["eventDescription"])

    eventMetadata = field("eventMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationEventDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationEventDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityAggregatesForOrganizationResponse:
    boto3_raw_data: (
        "type_defs.DescribeEntityAggregatesForOrganizationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def organizationEntityAggregates(self):  # pragma: no cover
        return OrganizationEntityAggregate.make_many(
            self.boto3_raw_data["organizationEntityAggregates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEntityAggregatesForOrganizationResponseTypeDef"
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
                "type_defs.DescribeEntityAggregatesForOrganizationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityFilter:
    boto3_raw_data: "type_defs.EntityFilterTypeDef" = dataclasses.field()

    eventArns = field("eventArns")
    entityArns = field("entityArns")
    entityValues = field("entityValues")

    @cached_property
    def lastUpdatedTimes(self):  # pragma: no cover
        return DateTimeRange.make_many(self.boto3_raw_data["lastUpdatedTimes"])

    tags = field("tags")
    statusCodes = field("statusCodes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventFilter:
    boto3_raw_data: "type_defs.EventFilterTypeDef" = dataclasses.field()

    eventArns = field("eventArns")
    eventTypeCodes = field("eventTypeCodes")
    services = field("services")
    regions = field("regions")
    availabilityZones = field("availabilityZones")

    @cached_property
    def startTimes(self):  # pragma: no cover
        return DateTimeRange.make_many(self.boto3_raw_data["startTimes"])

    @cached_property
    def endTimes(self):  # pragma: no cover
        return DateTimeRange.make_many(self.boto3_raw_data["endTimes"])

    @cached_property
    def lastUpdatedTimes(self):  # pragma: no cover
        return DateTimeRange.make_many(self.boto3_raw_data["lastUpdatedTimes"])

    entityArns = field("entityArns")
    entityValues = field("entityValues")
    eventTypeCategories = field("eventTypeCategories")
    tags = field("tags")
    eventStatusCodes = field("eventStatusCodes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationEventFilter:
    boto3_raw_data: "type_defs.OrganizationEventFilterTypeDef" = dataclasses.field()

    eventTypeCodes = field("eventTypeCodes")
    awsAccountIds = field("awsAccountIds")
    services = field("services")
    regions = field("regions")

    @cached_property
    def startTime(self):  # pragma: no cover
        return DateTimeRange.make_one(self.boto3_raw_data["startTime"])

    @cached_property
    def endTime(self):  # pragma: no cover
        return DateTimeRange.make_one(self.boto3_raw_data["endTime"])

    @cached_property
    def lastUpdatedTime(self):  # pragma: no cover
        return DateTimeRange.make_one(self.boto3_raw_data["lastUpdatedTime"])

    entityArns = field("entityArns")
    entityValues = field("entityValues")
    eventTypeCategories = field("eventTypeCategories")
    eventStatusCodes = field("eventStatusCodes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationEventFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationEventFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventDetailsResponse:
    boto3_raw_data: "type_defs.DescribeEventDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def successfulSet(self):  # pragma: no cover
        return EventDetails.make_many(self.boto3_raw_data["successfulSet"])

    @cached_property
    def failedSet(self):  # pragma: no cover
        return EventDetailsErrorItem.make_many(self.boto3_raw_data["failedSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventDetailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventDetailsForOrganizationResponse:
    boto3_raw_data: "type_defs.DescribeEventDetailsForOrganizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def successfulSet(self):  # pragma: no cover
        return OrganizationEventDetails.make_many(self.boto3_raw_data["successfulSet"])

    @cached_property
    def failedSet(self):  # pragma: no cover
        return OrganizationEventDetailsErrorItem.make_many(
            self.boto3_raw_data["failedSet"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventDetailsForOrganizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventDetailsForOrganizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAffectedEntitiesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeAffectedEntitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return EntityFilter.make_one(self.boto3_raw_data["filter"])

    locale = field("locale")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAffectedEntitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAffectedEntitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAffectedEntitiesRequest:
    boto3_raw_data: "type_defs.DescribeAffectedEntitiesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return EntityFilter.make_one(self.boto3_raw_data["filter"])

    locale = field("locale")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAffectedEntitiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAffectedEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventAggregatesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeEventAggregatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    aggregateField = field("aggregateField")

    @cached_property
    def filter(self):  # pragma: no cover
        return EventFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventAggregatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventAggregatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventAggregatesRequest:
    boto3_raw_data: "type_defs.DescribeEventAggregatesRequestTypeDef" = (
        dataclasses.field()
    )

    aggregateField = field("aggregateField")

    @cached_property
    def filter(self):  # pragma: no cover
        return EventFilter.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventAggregatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventAggregatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return EventFilter.make_one(self.boto3_raw_data["filter"])

    locale = field("locale")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsRequest:
    boto3_raw_data: "type_defs.DescribeEventsRequestTypeDef" = dataclasses.field()

    @cached_property
    def filter(self):  # pragma: no cover
        return EventFilter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    locale = field("locale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsForOrganizationRequestPaginate:
    boto3_raw_data: "type_defs.DescribeEventsForOrganizationRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return OrganizationEventFilter.make_one(self.boto3_raw_data["filter"])

    locale = field("locale")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventsForOrganizationRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsForOrganizationRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsForOrganizationRequest:
    boto3_raw_data: "type_defs.DescribeEventsForOrganizationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return OrganizationEventFilter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    locale = field("locale")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventsForOrganizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsForOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
