# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_health import type_defs as bs_td


class HEALTHCaster:

    def describe_affected_accounts_for_organization(
        self,
        res: "bs_td.DescribeAffectedAccountsForOrganizationResponseTypeDef",
    ) -> "dc_td.DescribeAffectedAccountsForOrganizationResponse":
        return dc_td.DescribeAffectedAccountsForOrganizationResponse.make_one(res)

    def describe_affected_entities(
        self,
        res: "bs_td.DescribeAffectedEntitiesResponseTypeDef",
    ) -> "dc_td.DescribeAffectedEntitiesResponse":
        return dc_td.DescribeAffectedEntitiesResponse.make_one(res)

    def describe_affected_entities_for_organization(
        self,
        res: "bs_td.DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    ) -> "dc_td.DescribeAffectedEntitiesForOrganizationResponse":
        return dc_td.DescribeAffectedEntitiesForOrganizationResponse.make_one(res)

    def describe_entity_aggregates(
        self,
        res: "bs_td.DescribeEntityAggregatesResponseTypeDef",
    ) -> "dc_td.DescribeEntityAggregatesResponse":
        return dc_td.DescribeEntityAggregatesResponse.make_one(res)

    def describe_entity_aggregates_for_organization(
        self,
        res: "bs_td.DescribeEntityAggregatesForOrganizationResponseTypeDef",
    ) -> "dc_td.DescribeEntityAggregatesForOrganizationResponse":
        return dc_td.DescribeEntityAggregatesForOrganizationResponse.make_one(res)

    def describe_event_aggregates(
        self,
        res: "bs_td.DescribeEventAggregatesResponseTypeDef",
    ) -> "dc_td.DescribeEventAggregatesResponse":
        return dc_td.DescribeEventAggregatesResponse.make_one(res)

    def describe_event_details(
        self,
        res: "bs_td.DescribeEventDetailsResponseTypeDef",
    ) -> "dc_td.DescribeEventDetailsResponse":
        return dc_td.DescribeEventDetailsResponse.make_one(res)

    def describe_event_details_for_organization(
        self,
        res: "bs_td.DescribeEventDetailsForOrganizationResponseTypeDef",
    ) -> "dc_td.DescribeEventDetailsForOrganizationResponse":
        return dc_td.DescribeEventDetailsForOrganizationResponse.make_one(res)

    def describe_event_types(
        self,
        res: "bs_td.DescribeEventTypesResponseTypeDef",
    ) -> "dc_td.DescribeEventTypesResponse":
        return dc_td.DescribeEventTypesResponse.make_one(res)

    def describe_events(
        self,
        res: "bs_td.DescribeEventsResponseTypeDef",
    ) -> "dc_td.DescribeEventsResponse":
        return dc_td.DescribeEventsResponse.make_one(res)

    def describe_events_for_organization(
        self,
        res: "bs_td.DescribeEventsForOrganizationResponseTypeDef",
    ) -> "dc_td.DescribeEventsForOrganizationResponse":
        return dc_td.DescribeEventsForOrganizationResponse.make_one(res)

    def describe_health_service_status_for_organization(
        self,
        res: "bs_td.DescribeHealthServiceStatusForOrganizationResponseTypeDef",
    ) -> "dc_td.DescribeHealthServiceStatusForOrganizationResponse":
        return dc_td.DescribeHealthServiceStatusForOrganizationResponse.make_one(res)

    def disable_health_service_access_for_organization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_health_service_access_for_organization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


health_caster = HEALTHCaster()
