# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pinpoint_email import type_defs as bs_td


class PINPOINT_EMAILCaster:

    def create_deliverability_test_report(
        self,
        res: "bs_td.CreateDeliverabilityTestReportResponseTypeDef",
    ) -> "dc_td.CreateDeliverabilityTestReportResponse":
        return dc_td.CreateDeliverabilityTestReportResponse.make_one(res)

    def create_email_identity(
        self,
        res: "bs_td.CreateEmailIdentityResponseTypeDef",
    ) -> "dc_td.CreateEmailIdentityResponse":
        return dc_td.CreateEmailIdentityResponse.make_one(res)

    def get_account(
        self,
        res: "bs_td.GetAccountResponseTypeDef",
    ) -> "dc_td.GetAccountResponse":
        return dc_td.GetAccountResponse.make_one(res)

    def get_blacklist_reports(
        self,
        res: "bs_td.GetBlacklistReportsResponseTypeDef",
    ) -> "dc_td.GetBlacklistReportsResponse":
        return dc_td.GetBlacklistReportsResponse.make_one(res)

    def get_configuration_set(
        self,
        res: "bs_td.GetConfigurationSetResponseTypeDef",
    ) -> "dc_td.GetConfigurationSetResponse":
        return dc_td.GetConfigurationSetResponse.make_one(res)

    def get_configuration_set_event_destinations(
        self,
        res: "bs_td.GetConfigurationSetEventDestinationsResponseTypeDef",
    ) -> "dc_td.GetConfigurationSetEventDestinationsResponse":
        return dc_td.GetConfigurationSetEventDestinationsResponse.make_one(res)

    def get_dedicated_ip(
        self,
        res: "bs_td.GetDedicatedIpResponseTypeDef",
    ) -> "dc_td.GetDedicatedIpResponse":
        return dc_td.GetDedicatedIpResponse.make_one(res)

    def get_dedicated_ips(
        self,
        res: "bs_td.GetDedicatedIpsResponseTypeDef",
    ) -> "dc_td.GetDedicatedIpsResponse":
        return dc_td.GetDedicatedIpsResponse.make_one(res)

    def get_deliverability_dashboard_options(
        self,
        res: "bs_td.GetDeliverabilityDashboardOptionsResponseTypeDef",
    ) -> "dc_td.GetDeliverabilityDashboardOptionsResponse":
        return dc_td.GetDeliverabilityDashboardOptionsResponse.make_one(res)

    def get_deliverability_test_report(
        self,
        res: "bs_td.GetDeliverabilityTestReportResponseTypeDef",
    ) -> "dc_td.GetDeliverabilityTestReportResponse":
        return dc_td.GetDeliverabilityTestReportResponse.make_one(res)

    def get_domain_deliverability_campaign(
        self,
        res: "bs_td.GetDomainDeliverabilityCampaignResponseTypeDef",
    ) -> "dc_td.GetDomainDeliverabilityCampaignResponse":
        return dc_td.GetDomainDeliverabilityCampaignResponse.make_one(res)

    def get_domain_statistics_report(
        self,
        res: "bs_td.GetDomainStatisticsReportResponseTypeDef",
    ) -> "dc_td.GetDomainStatisticsReportResponse":
        return dc_td.GetDomainStatisticsReportResponse.make_one(res)

    def get_email_identity(
        self,
        res: "bs_td.GetEmailIdentityResponseTypeDef",
    ) -> "dc_td.GetEmailIdentityResponse":
        return dc_td.GetEmailIdentityResponse.make_one(res)

    def list_configuration_sets(
        self,
        res: "bs_td.ListConfigurationSetsResponseTypeDef",
    ) -> "dc_td.ListConfigurationSetsResponse":
        return dc_td.ListConfigurationSetsResponse.make_one(res)

    def list_dedicated_ip_pools(
        self,
        res: "bs_td.ListDedicatedIpPoolsResponseTypeDef",
    ) -> "dc_td.ListDedicatedIpPoolsResponse":
        return dc_td.ListDedicatedIpPoolsResponse.make_one(res)

    def list_deliverability_test_reports(
        self,
        res: "bs_td.ListDeliverabilityTestReportsResponseTypeDef",
    ) -> "dc_td.ListDeliverabilityTestReportsResponse":
        return dc_td.ListDeliverabilityTestReportsResponse.make_one(res)

    def list_domain_deliverability_campaigns(
        self,
        res: "bs_td.ListDomainDeliverabilityCampaignsResponseTypeDef",
    ) -> "dc_td.ListDomainDeliverabilityCampaignsResponse":
        return dc_td.ListDomainDeliverabilityCampaignsResponse.make_one(res)

    def list_email_identities(
        self,
        res: "bs_td.ListEmailIdentitiesResponseTypeDef",
    ) -> "dc_td.ListEmailIdentitiesResponse":
        return dc_td.ListEmailIdentitiesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def send_email(
        self,
        res: "bs_td.SendEmailResponseTypeDef",
    ) -> "dc_td.SendEmailResponse":
        return dc_td.SendEmailResponse.make_one(res)


pinpoint_email_caster = PINPOINT_EMAILCaster()
