# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_guardduty import type_defs as bs_td


class GUARDDUTYCaster:

    def create_detector(
        self,
        res: "bs_td.CreateDetectorResponseTypeDef",
    ) -> "dc_td.CreateDetectorResponse":
        return dc_td.CreateDetectorResponse.make_one(res)

    def create_filter(
        self,
        res: "bs_td.CreateFilterResponseTypeDef",
    ) -> "dc_td.CreateFilterResponse":
        return dc_td.CreateFilterResponse.make_one(res)

    def create_ip_set(
        self,
        res: "bs_td.CreateIPSetResponseTypeDef",
    ) -> "dc_td.CreateIPSetResponse":
        return dc_td.CreateIPSetResponse.make_one(res)

    def create_malware_protection_plan(
        self,
        res: "bs_td.CreateMalwareProtectionPlanResponseTypeDef",
    ) -> "dc_td.CreateMalwareProtectionPlanResponse":
        return dc_td.CreateMalwareProtectionPlanResponse.make_one(res)

    def create_members(
        self,
        res: "bs_td.CreateMembersResponseTypeDef",
    ) -> "dc_td.CreateMembersResponse":
        return dc_td.CreateMembersResponse.make_one(res)

    def create_publishing_destination(
        self,
        res: "bs_td.CreatePublishingDestinationResponseTypeDef",
    ) -> "dc_td.CreatePublishingDestinationResponse":
        return dc_td.CreatePublishingDestinationResponse.make_one(res)

    def create_threat_entity_set(
        self,
        res: "bs_td.CreateThreatEntitySetResponseTypeDef",
    ) -> "dc_td.CreateThreatEntitySetResponse":
        return dc_td.CreateThreatEntitySetResponse.make_one(res)

    def create_threat_intel_set(
        self,
        res: "bs_td.CreateThreatIntelSetResponseTypeDef",
    ) -> "dc_td.CreateThreatIntelSetResponse":
        return dc_td.CreateThreatIntelSetResponse.make_one(res)

    def create_trusted_entity_set(
        self,
        res: "bs_td.CreateTrustedEntitySetResponseTypeDef",
    ) -> "dc_td.CreateTrustedEntitySetResponse":
        return dc_td.CreateTrustedEntitySetResponse.make_one(res)

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

    def delete_malware_protection_plan(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_members(
        self,
        res: "bs_td.DeleteMembersResponseTypeDef",
    ) -> "dc_td.DeleteMembersResponse":
        return dc_td.DeleteMembersResponse.make_one(res)

    def describe_malware_scans(
        self,
        res: "bs_td.DescribeMalwareScansResponseTypeDef",
    ) -> "dc_td.DescribeMalwareScansResponse":
        return dc_td.DescribeMalwareScansResponse.make_one(res)

    def describe_organization_configuration(
        self,
        res: "bs_td.DescribeOrganizationConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationConfigurationResponse":
        return dc_td.DescribeOrganizationConfigurationResponse.make_one(res)

    def describe_publishing_destination(
        self,
        res: "bs_td.DescribePublishingDestinationResponseTypeDef",
    ) -> "dc_td.DescribePublishingDestinationResponse":
        return dc_td.DescribePublishingDestinationResponse.make_one(res)

    def disassociate_members(
        self,
        res: "bs_td.DisassociateMembersResponseTypeDef",
    ) -> "dc_td.DisassociateMembersResponse":
        return dc_td.DisassociateMembersResponse.make_one(res)

    def get_administrator_account(
        self,
        res: "bs_td.GetAdministratorAccountResponseTypeDef",
    ) -> "dc_td.GetAdministratorAccountResponse":
        return dc_td.GetAdministratorAccountResponse.make_one(res)

    def get_coverage_statistics(
        self,
        res: "bs_td.GetCoverageStatisticsResponseTypeDef",
    ) -> "dc_td.GetCoverageStatisticsResponse":
        return dc_td.GetCoverageStatisticsResponse.make_one(res)

    def get_detector(
        self,
        res: "bs_td.GetDetectorResponseTypeDef",
    ) -> "dc_td.GetDetectorResponse":
        return dc_td.GetDetectorResponse.make_one(res)

    def get_filter(
        self,
        res: "bs_td.GetFilterResponseTypeDef",
    ) -> "dc_td.GetFilterResponse":
        return dc_td.GetFilterResponse.make_one(res)

    def get_findings(
        self,
        res: "bs_td.GetFindingsResponseTypeDef",
    ) -> "dc_td.GetFindingsResponse":
        return dc_td.GetFindingsResponse.make_one(res)

    def get_findings_statistics(
        self,
        res: "bs_td.GetFindingsStatisticsResponseTypeDef",
    ) -> "dc_td.GetFindingsStatisticsResponse":
        return dc_td.GetFindingsStatisticsResponse.make_one(res)

    def get_ip_set(
        self,
        res: "bs_td.GetIPSetResponseTypeDef",
    ) -> "dc_td.GetIPSetResponse":
        return dc_td.GetIPSetResponse.make_one(res)

    def get_invitations_count(
        self,
        res: "bs_td.GetInvitationsCountResponseTypeDef",
    ) -> "dc_td.GetInvitationsCountResponse":
        return dc_td.GetInvitationsCountResponse.make_one(res)

    def get_malware_protection_plan(
        self,
        res: "bs_td.GetMalwareProtectionPlanResponseTypeDef",
    ) -> "dc_td.GetMalwareProtectionPlanResponse":
        return dc_td.GetMalwareProtectionPlanResponse.make_one(res)

    def get_malware_scan_settings(
        self,
        res: "bs_td.GetMalwareScanSettingsResponseTypeDef",
    ) -> "dc_td.GetMalwareScanSettingsResponse":
        return dc_td.GetMalwareScanSettingsResponse.make_one(res)

    def get_master_account(
        self,
        res: "bs_td.GetMasterAccountResponseTypeDef",
    ) -> "dc_td.GetMasterAccountResponse":
        return dc_td.GetMasterAccountResponse.make_one(res)

    def get_member_detectors(
        self,
        res: "bs_td.GetMemberDetectorsResponseTypeDef",
    ) -> "dc_td.GetMemberDetectorsResponse":
        return dc_td.GetMemberDetectorsResponse.make_one(res)

    def get_members(
        self,
        res: "bs_td.GetMembersResponseTypeDef",
    ) -> "dc_td.GetMembersResponse":
        return dc_td.GetMembersResponse.make_one(res)

    def get_organization_statistics(
        self,
        res: "bs_td.GetOrganizationStatisticsResponseTypeDef",
    ) -> "dc_td.GetOrganizationStatisticsResponse":
        return dc_td.GetOrganizationStatisticsResponse.make_one(res)

    def get_remaining_free_trial_days(
        self,
        res: "bs_td.GetRemainingFreeTrialDaysResponseTypeDef",
    ) -> "dc_td.GetRemainingFreeTrialDaysResponse":
        return dc_td.GetRemainingFreeTrialDaysResponse.make_one(res)

    def get_threat_entity_set(
        self,
        res: "bs_td.GetThreatEntitySetResponseTypeDef",
    ) -> "dc_td.GetThreatEntitySetResponse":
        return dc_td.GetThreatEntitySetResponse.make_one(res)

    def get_threat_intel_set(
        self,
        res: "bs_td.GetThreatIntelSetResponseTypeDef",
    ) -> "dc_td.GetThreatIntelSetResponse":
        return dc_td.GetThreatIntelSetResponse.make_one(res)

    def get_trusted_entity_set(
        self,
        res: "bs_td.GetTrustedEntitySetResponseTypeDef",
    ) -> "dc_td.GetTrustedEntitySetResponse":
        return dc_td.GetTrustedEntitySetResponse.make_one(res)

    def get_usage_statistics(
        self,
        res: "bs_td.GetUsageStatisticsResponseTypeDef",
    ) -> "dc_td.GetUsageStatisticsResponse":
        return dc_td.GetUsageStatisticsResponse.make_one(res)

    def invite_members(
        self,
        res: "bs_td.InviteMembersResponseTypeDef",
    ) -> "dc_td.InviteMembersResponse":
        return dc_td.InviteMembersResponse.make_one(res)

    def list_coverage(
        self,
        res: "bs_td.ListCoverageResponseTypeDef",
    ) -> "dc_td.ListCoverageResponse":
        return dc_td.ListCoverageResponse.make_one(res)

    def list_detectors(
        self,
        res: "bs_td.ListDetectorsResponseTypeDef",
    ) -> "dc_td.ListDetectorsResponse":
        return dc_td.ListDetectorsResponse.make_one(res)

    def list_filters(
        self,
        res: "bs_td.ListFiltersResponseTypeDef",
    ) -> "dc_td.ListFiltersResponse":
        return dc_td.ListFiltersResponse.make_one(res)

    def list_findings(
        self,
        res: "bs_td.ListFindingsResponseTypeDef",
    ) -> "dc_td.ListFindingsResponse":
        return dc_td.ListFindingsResponse.make_one(res)

    def list_ip_sets(
        self,
        res: "bs_td.ListIPSetsResponseTypeDef",
    ) -> "dc_td.ListIPSetsResponse":
        return dc_td.ListIPSetsResponse.make_one(res)

    def list_invitations(
        self,
        res: "bs_td.ListInvitationsResponseTypeDef",
    ) -> "dc_td.ListInvitationsResponse":
        return dc_td.ListInvitationsResponse.make_one(res)

    def list_malware_protection_plans(
        self,
        res: "bs_td.ListMalwareProtectionPlansResponseTypeDef",
    ) -> "dc_td.ListMalwareProtectionPlansResponse":
        return dc_td.ListMalwareProtectionPlansResponse.make_one(res)

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

    def list_publishing_destinations(
        self,
        res: "bs_td.ListPublishingDestinationsResponseTypeDef",
    ) -> "dc_td.ListPublishingDestinationsResponse":
        return dc_td.ListPublishingDestinationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_threat_entity_sets(
        self,
        res: "bs_td.ListThreatEntitySetsResponseTypeDef",
    ) -> "dc_td.ListThreatEntitySetsResponse":
        return dc_td.ListThreatEntitySetsResponse.make_one(res)

    def list_threat_intel_sets(
        self,
        res: "bs_td.ListThreatIntelSetsResponseTypeDef",
    ) -> "dc_td.ListThreatIntelSetsResponse":
        return dc_td.ListThreatIntelSetsResponse.make_one(res)

    def list_trusted_entity_sets(
        self,
        res: "bs_td.ListTrustedEntitySetsResponseTypeDef",
    ) -> "dc_td.ListTrustedEntitySetsResponse":
        return dc_td.ListTrustedEntitySetsResponse.make_one(res)

    def start_malware_scan(
        self,
        res: "bs_td.StartMalwareScanResponseTypeDef",
    ) -> "dc_td.StartMalwareScanResponse":
        return dc_td.StartMalwareScanResponse.make_one(res)

    def start_monitoring_members(
        self,
        res: "bs_td.StartMonitoringMembersResponseTypeDef",
    ) -> "dc_td.StartMonitoringMembersResponse":
        return dc_td.StartMonitoringMembersResponse.make_one(res)

    def stop_monitoring_members(
        self,
        res: "bs_td.StopMonitoringMembersResponseTypeDef",
    ) -> "dc_td.StopMonitoringMembersResponse":
        return dc_td.StopMonitoringMembersResponse.make_one(res)

    def update_filter(
        self,
        res: "bs_td.UpdateFilterResponseTypeDef",
    ) -> "dc_td.UpdateFilterResponse":
        return dc_td.UpdateFilterResponse.make_one(res)

    def update_malware_protection_plan(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_member_detectors(
        self,
        res: "bs_td.UpdateMemberDetectorsResponseTypeDef",
    ) -> "dc_td.UpdateMemberDetectorsResponse":
        return dc_td.UpdateMemberDetectorsResponse.make_one(res)


guardduty_caster = GUARDDUTYCaster()
