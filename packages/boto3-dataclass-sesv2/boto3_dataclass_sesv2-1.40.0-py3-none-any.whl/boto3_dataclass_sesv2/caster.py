# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sesv2 import type_defs as bs_td


class SESV2Caster:

    def batch_get_metric_data(
        self,
        res: "bs_td.BatchGetMetricDataResponseTypeDef",
    ) -> "dc_td.BatchGetMetricDataResponse":
        return dc_td.BatchGetMetricDataResponse.make_one(res)

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

    def create_export_job(
        self,
        res: "bs_td.CreateExportJobResponseTypeDef",
    ) -> "dc_td.CreateExportJobResponse":
        return dc_td.CreateExportJobResponse.make_one(res)

    def create_import_job(
        self,
        res: "bs_td.CreateImportJobResponseTypeDef",
    ) -> "dc_td.CreateImportJobResponse":
        return dc_td.CreateImportJobResponse.make_one(res)

    def create_multi_region_endpoint(
        self,
        res: "bs_td.CreateMultiRegionEndpointResponseTypeDef",
    ) -> "dc_td.CreateMultiRegionEndpointResponse":
        return dc_td.CreateMultiRegionEndpointResponse.make_one(res)

    def create_tenant(
        self,
        res: "bs_td.CreateTenantResponseTypeDef",
    ) -> "dc_td.CreateTenantResponse":
        return dc_td.CreateTenantResponse.make_one(res)

    def delete_multi_region_endpoint(
        self,
        res: "bs_td.DeleteMultiRegionEndpointResponseTypeDef",
    ) -> "dc_td.DeleteMultiRegionEndpointResponse":
        return dc_td.DeleteMultiRegionEndpointResponse.make_one(res)

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

    def get_contact(
        self,
        res: "bs_td.GetContactResponseTypeDef",
    ) -> "dc_td.GetContactResponse":
        return dc_td.GetContactResponse.make_one(res)

    def get_contact_list(
        self,
        res: "bs_td.GetContactListResponseTypeDef",
    ) -> "dc_td.GetContactListResponse":
        return dc_td.GetContactListResponse.make_one(res)

    def get_custom_verification_email_template(
        self,
        res: "bs_td.GetCustomVerificationEmailTemplateResponseTypeDef",
    ) -> "dc_td.GetCustomVerificationEmailTemplateResponse":
        return dc_td.GetCustomVerificationEmailTemplateResponse.make_one(res)

    def get_dedicated_ip(
        self,
        res: "bs_td.GetDedicatedIpResponseTypeDef",
    ) -> "dc_td.GetDedicatedIpResponse":
        return dc_td.GetDedicatedIpResponse.make_one(res)

    def get_dedicated_ip_pool(
        self,
        res: "bs_td.GetDedicatedIpPoolResponseTypeDef",
    ) -> "dc_td.GetDedicatedIpPoolResponse":
        return dc_td.GetDedicatedIpPoolResponse.make_one(res)

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

    def get_email_identity_policies(
        self,
        res: "bs_td.GetEmailIdentityPoliciesResponseTypeDef",
    ) -> "dc_td.GetEmailIdentityPoliciesResponse":
        return dc_td.GetEmailIdentityPoliciesResponse.make_one(res)

    def get_email_template(
        self,
        res: "bs_td.GetEmailTemplateResponseTypeDef",
    ) -> "dc_td.GetEmailTemplateResponse":
        return dc_td.GetEmailTemplateResponse.make_one(res)

    def get_export_job(
        self,
        res: "bs_td.GetExportJobResponseTypeDef",
    ) -> "dc_td.GetExportJobResponse":
        return dc_td.GetExportJobResponse.make_one(res)

    def get_import_job(
        self,
        res: "bs_td.GetImportJobResponseTypeDef",
    ) -> "dc_td.GetImportJobResponse":
        return dc_td.GetImportJobResponse.make_one(res)

    def get_message_insights(
        self,
        res: "bs_td.GetMessageInsightsResponseTypeDef",
    ) -> "dc_td.GetMessageInsightsResponse":
        return dc_td.GetMessageInsightsResponse.make_one(res)

    def get_multi_region_endpoint(
        self,
        res: "bs_td.GetMultiRegionEndpointResponseTypeDef",
    ) -> "dc_td.GetMultiRegionEndpointResponse":
        return dc_td.GetMultiRegionEndpointResponse.make_one(res)

    def get_reputation_entity(
        self,
        res: "bs_td.GetReputationEntityResponseTypeDef",
    ) -> "dc_td.GetReputationEntityResponse":
        return dc_td.GetReputationEntityResponse.make_one(res)

    def get_suppressed_destination(
        self,
        res: "bs_td.GetSuppressedDestinationResponseTypeDef",
    ) -> "dc_td.GetSuppressedDestinationResponse":
        return dc_td.GetSuppressedDestinationResponse.make_one(res)

    def get_tenant(
        self,
        res: "bs_td.GetTenantResponseTypeDef",
    ) -> "dc_td.GetTenantResponse":
        return dc_td.GetTenantResponse.make_one(res)

    def list_configuration_sets(
        self,
        res: "bs_td.ListConfigurationSetsResponseTypeDef",
    ) -> "dc_td.ListConfigurationSetsResponse":
        return dc_td.ListConfigurationSetsResponse.make_one(res)

    def list_contact_lists(
        self,
        res: "bs_td.ListContactListsResponseTypeDef",
    ) -> "dc_td.ListContactListsResponse":
        return dc_td.ListContactListsResponse.make_one(res)

    def list_contacts(
        self,
        res: "bs_td.ListContactsResponseTypeDef",
    ) -> "dc_td.ListContactsResponse":
        return dc_td.ListContactsResponse.make_one(res)

    def list_custom_verification_email_templates(
        self,
        res: "bs_td.ListCustomVerificationEmailTemplatesResponseTypeDef",
    ) -> "dc_td.ListCustomVerificationEmailTemplatesResponse":
        return dc_td.ListCustomVerificationEmailTemplatesResponse.make_one(res)

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

    def list_email_templates(
        self,
        res: "bs_td.ListEmailTemplatesResponseTypeDef",
    ) -> "dc_td.ListEmailTemplatesResponse":
        return dc_td.ListEmailTemplatesResponse.make_one(res)

    def list_export_jobs(
        self,
        res: "bs_td.ListExportJobsResponseTypeDef",
    ) -> "dc_td.ListExportJobsResponse":
        return dc_td.ListExportJobsResponse.make_one(res)

    def list_import_jobs(
        self,
        res: "bs_td.ListImportJobsResponseTypeDef",
    ) -> "dc_td.ListImportJobsResponse":
        return dc_td.ListImportJobsResponse.make_one(res)

    def list_multi_region_endpoints(
        self,
        res: "bs_td.ListMultiRegionEndpointsResponseTypeDef",
    ) -> "dc_td.ListMultiRegionEndpointsResponse":
        return dc_td.ListMultiRegionEndpointsResponse.make_one(res)

    def list_recommendations(
        self,
        res: "bs_td.ListRecommendationsResponseTypeDef",
    ) -> "dc_td.ListRecommendationsResponse":
        return dc_td.ListRecommendationsResponse.make_one(res)

    def list_reputation_entities(
        self,
        res: "bs_td.ListReputationEntitiesResponseTypeDef",
    ) -> "dc_td.ListReputationEntitiesResponse":
        return dc_td.ListReputationEntitiesResponse.make_one(res)

    def list_resource_tenants(
        self,
        res: "bs_td.ListResourceTenantsResponseTypeDef",
    ) -> "dc_td.ListResourceTenantsResponse":
        return dc_td.ListResourceTenantsResponse.make_one(res)

    def list_suppressed_destinations(
        self,
        res: "bs_td.ListSuppressedDestinationsResponseTypeDef",
    ) -> "dc_td.ListSuppressedDestinationsResponse":
        return dc_td.ListSuppressedDestinationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_tenant_resources(
        self,
        res: "bs_td.ListTenantResourcesResponseTypeDef",
    ) -> "dc_td.ListTenantResourcesResponse":
        return dc_td.ListTenantResourcesResponse.make_one(res)

    def list_tenants(
        self,
        res: "bs_td.ListTenantsResponseTypeDef",
    ) -> "dc_td.ListTenantsResponse":
        return dc_td.ListTenantsResponse.make_one(res)

    def put_email_identity_dkim_signing_attributes(
        self,
        res: "bs_td.PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    ) -> "dc_td.PutEmailIdentityDkimSigningAttributesResponse":
        return dc_td.PutEmailIdentityDkimSigningAttributesResponse.make_one(res)

    def send_bulk_email(
        self,
        res: "bs_td.SendBulkEmailResponseTypeDef",
    ) -> "dc_td.SendBulkEmailResponse":
        return dc_td.SendBulkEmailResponse.make_one(res)

    def send_custom_verification_email(
        self,
        res: "bs_td.SendCustomVerificationEmailResponseTypeDef",
    ) -> "dc_td.SendCustomVerificationEmailResponse":
        return dc_td.SendCustomVerificationEmailResponse.make_one(res)

    def send_email(
        self,
        res: "bs_td.SendEmailResponseTypeDef",
    ) -> "dc_td.SendEmailResponse":
        return dc_td.SendEmailResponse.make_one(res)

    def test_render_email_template(
        self,
        res: "bs_td.TestRenderEmailTemplateResponseTypeDef",
    ) -> "dc_td.TestRenderEmailTemplateResponse":
        return dc_td.TestRenderEmailTemplateResponse.make_one(res)


sesv2_caster = SESV2Caster()
