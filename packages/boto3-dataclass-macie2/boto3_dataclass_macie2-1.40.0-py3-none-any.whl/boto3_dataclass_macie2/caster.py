# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_macie2 import type_defs as bs_td


class MACIE2Caster:

    def batch_get_custom_data_identifiers(
        self,
        res: "bs_td.BatchGetCustomDataIdentifiersResponseTypeDef",
    ) -> "dc_td.BatchGetCustomDataIdentifiersResponse":
        return dc_td.BatchGetCustomDataIdentifiersResponse.make_one(res)

    def batch_update_automated_discovery_accounts(
        self,
        res: "bs_td.BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef",
    ) -> "dc_td.BatchUpdateAutomatedDiscoveryAccountsResponse":
        return dc_td.BatchUpdateAutomatedDiscoveryAccountsResponse.make_one(res)

    def create_allow_list(
        self,
        res: "bs_td.CreateAllowListResponseTypeDef",
    ) -> "dc_td.CreateAllowListResponse":
        return dc_td.CreateAllowListResponse.make_one(res)

    def create_classification_job(
        self,
        res: "bs_td.CreateClassificationJobResponseTypeDef",
    ) -> "dc_td.CreateClassificationJobResponse":
        return dc_td.CreateClassificationJobResponse.make_one(res)

    def create_custom_data_identifier(
        self,
        res: "bs_td.CreateCustomDataIdentifierResponseTypeDef",
    ) -> "dc_td.CreateCustomDataIdentifierResponse":
        return dc_td.CreateCustomDataIdentifierResponse.make_one(res)

    def create_findings_filter(
        self,
        res: "bs_td.CreateFindingsFilterResponseTypeDef",
    ) -> "dc_td.CreateFindingsFilterResponse":
        return dc_td.CreateFindingsFilterResponse.make_one(res)

    def create_invitations(
        self,
        res: "bs_td.CreateInvitationsResponseTypeDef",
    ) -> "dc_td.CreateInvitationsResponse":
        return dc_td.CreateInvitationsResponse.make_one(res)

    def create_member(
        self,
        res: "bs_td.CreateMemberResponseTypeDef",
    ) -> "dc_td.CreateMemberResponse":
        return dc_td.CreateMemberResponse.make_one(res)

    def decline_invitations(
        self,
        res: "bs_td.DeclineInvitationsResponseTypeDef",
    ) -> "dc_td.DeclineInvitationsResponse":
        return dc_td.DeclineInvitationsResponse.make_one(res)

    def delete_invitations(
        self,
        res: "bs_td.DeleteInvitationsResponseTypeDef",
    ) -> "dc_td.DeleteInvitationsResponse":
        return dc_td.DeleteInvitationsResponse.make_one(res)

    def describe_buckets(
        self,
        res: "bs_td.DescribeBucketsResponseTypeDef",
    ) -> "dc_td.DescribeBucketsResponse":
        return dc_td.DescribeBucketsResponse.make_one(res)

    def describe_classification_job(
        self,
        res: "bs_td.DescribeClassificationJobResponseTypeDef",
    ) -> "dc_td.DescribeClassificationJobResponse":
        return dc_td.DescribeClassificationJobResponse.make_one(res)

    def describe_organization_configuration(
        self,
        res: "bs_td.DescribeOrganizationConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationConfigurationResponse":
        return dc_td.DescribeOrganizationConfigurationResponse.make_one(res)

    def get_administrator_account(
        self,
        res: "bs_td.GetAdministratorAccountResponseTypeDef",
    ) -> "dc_td.GetAdministratorAccountResponse":
        return dc_td.GetAdministratorAccountResponse.make_one(res)

    def get_allow_list(
        self,
        res: "bs_td.GetAllowListResponseTypeDef",
    ) -> "dc_td.GetAllowListResponse":
        return dc_td.GetAllowListResponse.make_one(res)

    def get_automated_discovery_configuration(
        self,
        res: "bs_td.GetAutomatedDiscoveryConfigurationResponseTypeDef",
    ) -> "dc_td.GetAutomatedDiscoveryConfigurationResponse":
        return dc_td.GetAutomatedDiscoveryConfigurationResponse.make_one(res)

    def get_bucket_statistics(
        self,
        res: "bs_td.GetBucketStatisticsResponseTypeDef",
    ) -> "dc_td.GetBucketStatisticsResponse":
        return dc_td.GetBucketStatisticsResponse.make_one(res)

    def get_classification_export_configuration(
        self,
        res: "bs_td.GetClassificationExportConfigurationResponseTypeDef",
    ) -> "dc_td.GetClassificationExportConfigurationResponse":
        return dc_td.GetClassificationExportConfigurationResponse.make_one(res)

    def get_classification_scope(
        self,
        res: "bs_td.GetClassificationScopeResponseTypeDef",
    ) -> "dc_td.GetClassificationScopeResponse":
        return dc_td.GetClassificationScopeResponse.make_one(res)

    def get_custom_data_identifier(
        self,
        res: "bs_td.GetCustomDataIdentifierResponseTypeDef",
    ) -> "dc_td.GetCustomDataIdentifierResponse":
        return dc_td.GetCustomDataIdentifierResponse.make_one(res)

    def get_finding_statistics(
        self,
        res: "bs_td.GetFindingStatisticsResponseTypeDef",
    ) -> "dc_td.GetFindingStatisticsResponse":
        return dc_td.GetFindingStatisticsResponse.make_one(res)

    def get_findings(
        self,
        res: "bs_td.GetFindingsResponseTypeDef",
    ) -> "dc_td.GetFindingsResponse":
        return dc_td.GetFindingsResponse.make_one(res)

    def get_findings_filter(
        self,
        res: "bs_td.GetFindingsFilterResponseTypeDef",
    ) -> "dc_td.GetFindingsFilterResponse":
        return dc_td.GetFindingsFilterResponse.make_one(res)

    def get_findings_publication_configuration(
        self,
        res: "bs_td.GetFindingsPublicationConfigurationResponseTypeDef",
    ) -> "dc_td.GetFindingsPublicationConfigurationResponse":
        return dc_td.GetFindingsPublicationConfigurationResponse.make_one(res)

    def get_invitations_count(
        self,
        res: "bs_td.GetInvitationsCountResponseTypeDef",
    ) -> "dc_td.GetInvitationsCountResponse":
        return dc_td.GetInvitationsCountResponse.make_one(res)

    def get_macie_session(
        self,
        res: "bs_td.GetMacieSessionResponseTypeDef",
    ) -> "dc_td.GetMacieSessionResponse":
        return dc_td.GetMacieSessionResponse.make_one(res)

    def get_master_account(
        self,
        res: "bs_td.GetMasterAccountResponseTypeDef",
    ) -> "dc_td.GetMasterAccountResponse":
        return dc_td.GetMasterAccountResponse.make_one(res)

    def get_member(
        self,
        res: "bs_td.GetMemberResponseTypeDef",
    ) -> "dc_td.GetMemberResponse":
        return dc_td.GetMemberResponse.make_one(res)

    def get_resource_profile(
        self,
        res: "bs_td.GetResourceProfileResponseTypeDef",
    ) -> "dc_td.GetResourceProfileResponse":
        return dc_td.GetResourceProfileResponse.make_one(res)

    def get_reveal_configuration(
        self,
        res: "bs_td.GetRevealConfigurationResponseTypeDef",
    ) -> "dc_td.GetRevealConfigurationResponse":
        return dc_td.GetRevealConfigurationResponse.make_one(res)

    def get_sensitive_data_occurrences(
        self,
        res: "bs_td.GetSensitiveDataOccurrencesResponseTypeDef",
    ) -> "dc_td.GetSensitiveDataOccurrencesResponse":
        return dc_td.GetSensitiveDataOccurrencesResponse.make_one(res)

    def get_sensitive_data_occurrences_availability(
        self,
        res: "bs_td.GetSensitiveDataOccurrencesAvailabilityResponseTypeDef",
    ) -> "dc_td.GetSensitiveDataOccurrencesAvailabilityResponse":
        return dc_td.GetSensitiveDataOccurrencesAvailabilityResponse.make_one(res)

    def get_sensitivity_inspection_template(
        self,
        res: "bs_td.GetSensitivityInspectionTemplateResponseTypeDef",
    ) -> "dc_td.GetSensitivityInspectionTemplateResponse":
        return dc_td.GetSensitivityInspectionTemplateResponse.make_one(res)

    def get_usage_statistics(
        self,
        res: "bs_td.GetUsageStatisticsResponseTypeDef",
    ) -> "dc_td.GetUsageStatisticsResponse":
        return dc_td.GetUsageStatisticsResponse.make_one(res)

    def get_usage_totals(
        self,
        res: "bs_td.GetUsageTotalsResponseTypeDef",
    ) -> "dc_td.GetUsageTotalsResponse":
        return dc_td.GetUsageTotalsResponse.make_one(res)

    def list_allow_lists(
        self,
        res: "bs_td.ListAllowListsResponseTypeDef",
    ) -> "dc_td.ListAllowListsResponse":
        return dc_td.ListAllowListsResponse.make_one(res)

    def list_automated_discovery_accounts(
        self,
        res: "bs_td.ListAutomatedDiscoveryAccountsResponseTypeDef",
    ) -> "dc_td.ListAutomatedDiscoveryAccountsResponse":
        return dc_td.ListAutomatedDiscoveryAccountsResponse.make_one(res)

    def list_classification_jobs(
        self,
        res: "bs_td.ListClassificationJobsResponseTypeDef",
    ) -> "dc_td.ListClassificationJobsResponse":
        return dc_td.ListClassificationJobsResponse.make_one(res)

    def list_classification_scopes(
        self,
        res: "bs_td.ListClassificationScopesResponseTypeDef",
    ) -> "dc_td.ListClassificationScopesResponse":
        return dc_td.ListClassificationScopesResponse.make_one(res)

    def list_custom_data_identifiers(
        self,
        res: "bs_td.ListCustomDataIdentifiersResponseTypeDef",
    ) -> "dc_td.ListCustomDataIdentifiersResponse":
        return dc_td.ListCustomDataIdentifiersResponse.make_one(res)

    def list_findings(
        self,
        res: "bs_td.ListFindingsResponseTypeDef",
    ) -> "dc_td.ListFindingsResponse":
        return dc_td.ListFindingsResponse.make_one(res)

    def list_findings_filters(
        self,
        res: "bs_td.ListFindingsFiltersResponseTypeDef",
    ) -> "dc_td.ListFindingsFiltersResponse":
        return dc_td.ListFindingsFiltersResponse.make_one(res)

    def list_invitations(
        self,
        res: "bs_td.ListInvitationsResponseTypeDef",
    ) -> "dc_td.ListInvitationsResponse":
        return dc_td.ListInvitationsResponse.make_one(res)

    def list_managed_data_identifiers(
        self,
        res: "bs_td.ListManagedDataIdentifiersResponseTypeDef",
    ) -> "dc_td.ListManagedDataIdentifiersResponse":
        return dc_td.ListManagedDataIdentifiersResponse.make_one(res)

    def list_members(
        self,
        res: "bs_td.ListMembersResponseTypeDef",
    ) -> "dc_td.ListMembersResponse":
        return dc_td.ListMembersResponse.make_one(res)

    def list_organization_admin_accounts(
        self,
        res: "bs_td.ListOrganizationAdminAccountsResponseTypeDef",
    ) -> "dc_td.ListOrganizationAdminAccountsResponse":
        return dc_td.ListOrganizationAdminAccountsResponse.make_one(res)

    def list_resource_profile_artifacts(
        self,
        res: "bs_td.ListResourceProfileArtifactsResponseTypeDef",
    ) -> "dc_td.ListResourceProfileArtifactsResponse":
        return dc_td.ListResourceProfileArtifactsResponse.make_one(res)

    def list_resource_profile_detections(
        self,
        res: "bs_td.ListResourceProfileDetectionsResponseTypeDef",
    ) -> "dc_td.ListResourceProfileDetectionsResponse":
        return dc_td.ListResourceProfileDetectionsResponse.make_one(res)

    def list_sensitivity_inspection_templates(
        self,
        res: "bs_td.ListSensitivityInspectionTemplatesResponseTypeDef",
    ) -> "dc_td.ListSensitivityInspectionTemplatesResponse":
        return dc_td.ListSensitivityInspectionTemplatesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_classification_export_configuration(
        self,
        res: "bs_td.PutClassificationExportConfigurationResponseTypeDef",
    ) -> "dc_td.PutClassificationExportConfigurationResponse":
        return dc_td.PutClassificationExportConfigurationResponse.make_one(res)

    def search_resources(
        self,
        res: "bs_td.SearchResourcesResponseTypeDef",
    ) -> "dc_td.SearchResourcesResponse":
        return dc_td.SearchResourcesResponse.make_one(res)

    def test_custom_data_identifier(
        self,
        res: "bs_td.TestCustomDataIdentifierResponseTypeDef",
    ) -> "dc_td.TestCustomDataIdentifierResponse":
        return dc_td.TestCustomDataIdentifierResponse.make_one(res)

    def update_allow_list(
        self,
        res: "bs_td.UpdateAllowListResponseTypeDef",
    ) -> "dc_td.UpdateAllowListResponse":
        return dc_td.UpdateAllowListResponse.make_one(res)

    def update_findings_filter(
        self,
        res: "bs_td.UpdateFindingsFilterResponseTypeDef",
    ) -> "dc_td.UpdateFindingsFilterResponse":
        return dc_td.UpdateFindingsFilterResponse.make_one(res)

    def update_reveal_configuration(
        self,
        res: "bs_td.UpdateRevealConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateRevealConfigurationResponse":
        return dc_td.UpdateRevealConfigurationResponse.make_one(res)


macie2_caster = MACIE2Caster()
