# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_inspector2 import type_defs as bs_td


class INSPECTOR2Caster:

    def associate_member(
        self,
        res: "bs_td.AssociateMemberResponseTypeDef",
    ) -> "dc_td.AssociateMemberResponse":
        return dc_td.AssociateMemberResponse.make_one(res)

    def batch_associate_code_security_scan_configuration(
        self,
        res: "bs_td.BatchAssociateCodeSecurityScanConfigurationResponseTypeDef",
    ) -> "dc_td.BatchAssociateCodeSecurityScanConfigurationResponse":
        return dc_td.BatchAssociateCodeSecurityScanConfigurationResponse.make_one(res)

    def batch_disassociate_code_security_scan_configuration(
        self,
        res: "bs_td.BatchDisassociateCodeSecurityScanConfigurationResponseTypeDef",
    ) -> "dc_td.BatchDisassociateCodeSecurityScanConfigurationResponse":
        return dc_td.BatchDisassociateCodeSecurityScanConfigurationResponse.make_one(
            res
        )

    def batch_get_account_status(
        self,
        res: "bs_td.BatchGetAccountStatusResponseTypeDef",
    ) -> "dc_td.BatchGetAccountStatusResponse":
        return dc_td.BatchGetAccountStatusResponse.make_one(res)

    def batch_get_code_snippet(
        self,
        res: "bs_td.BatchGetCodeSnippetResponseTypeDef",
    ) -> "dc_td.BatchGetCodeSnippetResponse":
        return dc_td.BatchGetCodeSnippetResponse.make_one(res)

    def batch_get_finding_details(
        self,
        res: "bs_td.BatchGetFindingDetailsResponseTypeDef",
    ) -> "dc_td.BatchGetFindingDetailsResponse":
        return dc_td.BatchGetFindingDetailsResponse.make_one(res)

    def batch_get_free_trial_info(
        self,
        res: "bs_td.BatchGetFreeTrialInfoResponseTypeDef",
    ) -> "dc_td.BatchGetFreeTrialInfoResponse":
        return dc_td.BatchGetFreeTrialInfoResponse.make_one(res)

    def batch_get_member_ec2_deep_inspection_status(
        self,
        res: "bs_td.BatchGetMemberEc2DeepInspectionStatusResponseTypeDef",
    ) -> "dc_td.BatchGetMemberEc2DeepInspectionStatusResponse":
        return dc_td.BatchGetMemberEc2DeepInspectionStatusResponse.make_one(res)

    def batch_update_member_ec2_deep_inspection_status(
        self,
        res: "bs_td.BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef",
    ) -> "dc_td.BatchUpdateMemberEc2DeepInspectionStatusResponse":
        return dc_td.BatchUpdateMemberEc2DeepInspectionStatusResponse.make_one(res)

    def cancel_findings_report(
        self,
        res: "bs_td.CancelFindingsReportResponseTypeDef",
    ) -> "dc_td.CancelFindingsReportResponse":
        return dc_td.CancelFindingsReportResponse.make_one(res)

    def cancel_sbom_export(
        self,
        res: "bs_td.CancelSbomExportResponseTypeDef",
    ) -> "dc_td.CancelSbomExportResponse":
        return dc_td.CancelSbomExportResponse.make_one(res)

    def create_cis_scan_configuration(
        self,
        res: "bs_td.CreateCisScanConfigurationResponseTypeDef",
    ) -> "dc_td.CreateCisScanConfigurationResponse":
        return dc_td.CreateCisScanConfigurationResponse.make_one(res)

    def create_code_security_integration(
        self,
        res: "bs_td.CreateCodeSecurityIntegrationResponseTypeDef",
    ) -> "dc_td.CreateCodeSecurityIntegrationResponse":
        return dc_td.CreateCodeSecurityIntegrationResponse.make_one(res)

    def create_code_security_scan_configuration(
        self,
        res: "bs_td.CreateCodeSecurityScanConfigurationResponseTypeDef",
    ) -> "dc_td.CreateCodeSecurityScanConfigurationResponse":
        return dc_td.CreateCodeSecurityScanConfigurationResponse.make_one(res)

    def create_filter(
        self,
        res: "bs_td.CreateFilterResponseTypeDef",
    ) -> "dc_td.CreateFilterResponse":
        return dc_td.CreateFilterResponse.make_one(res)

    def create_findings_report(
        self,
        res: "bs_td.CreateFindingsReportResponseTypeDef",
    ) -> "dc_td.CreateFindingsReportResponse":
        return dc_td.CreateFindingsReportResponse.make_one(res)

    def create_sbom_export(
        self,
        res: "bs_td.CreateSbomExportResponseTypeDef",
    ) -> "dc_td.CreateSbomExportResponse":
        return dc_td.CreateSbomExportResponse.make_one(res)

    def delete_cis_scan_configuration(
        self,
        res: "bs_td.DeleteCisScanConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteCisScanConfigurationResponse":
        return dc_td.DeleteCisScanConfigurationResponse.make_one(res)

    def delete_code_security_integration(
        self,
        res: "bs_td.DeleteCodeSecurityIntegrationResponseTypeDef",
    ) -> "dc_td.DeleteCodeSecurityIntegrationResponse":
        return dc_td.DeleteCodeSecurityIntegrationResponse.make_one(res)

    def delete_code_security_scan_configuration(
        self,
        res: "bs_td.DeleteCodeSecurityScanConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteCodeSecurityScanConfigurationResponse":
        return dc_td.DeleteCodeSecurityScanConfigurationResponse.make_one(res)

    def delete_filter(
        self,
        res: "bs_td.DeleteFilterResponseTypeDef",
    ) -> "dc_td.DeleteFilterResponse":
        return dc_td.DeleteFilterResponse.make_one(res)

    def describe_organization_configuration(
        self,
        res: "bs_td.DescribeOrganizationConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationConfigurationResponse":
        return dc_td.DescribeOrganizationConfigurationResponse.make_one(res)

    def disable(
        self,
        res: "bs_td.DisableResponseTypeDef",
    ) -> "dc_td.DisableResponse":
        return dc_td.DisableResponse.make_one(res)

    def disable_delegated_admin_account(
        self,
        res: "bs_td.DisableDelegatedAdminAccountResponseTypeDef",
    ) -> "dc_td.DisableDelegatedAdminAccountResponse":
        return dc_td.DisableDelegatedAdminAccountResponse.make_one(res)

    def disassociate_member(
        self,
        res: "bs_td.DisassociateMemberResponseTypeDef",
    ) -> "dc_td.DisassociateMemberResponse":
        return dc_td.DisassociateMemberResponse.make_one(res)

    def enable(
        self,
        res: "bs_td.EnableResponseTypeDef",
    ) -> "dc_td.EnableResponse":
        return dc_td.EnableResponse.make_one(res)

    def enable_delegated_admin_account(
        self,
        res: "bs_td.EnableDelegatedAdminAccountResponseTypeDef",
    ) -> "dc_td.EnableDelegatedAdminAccountResponse":
        return dc_td.EnableDelegatedAdminAccountResponse.make_one(res)

    def get_cis_scan_report(
        self,
        res: "bs_td.GetCisScanReportResponseTypeDef",
    ) -> "dc_td.GetCisScanReportResponse":
        return dc_td.GetCisScanReportResponse.make_one(res)

    def get_cis_scan_result_details(
        self,
        res: "bs_td.GetCisScanResultDetailsResponseTypeDef",
    ) -> "dc_td.GetCisScanResultDetailsResponse":
        return dc_td.GetCisScanResultDetailsResponse.make_one(res)

    def get_clusters_for_image(
        self,
        res: "bs_td.GetClustersForImageResponseTypeDef",
    ) -> "dc_td.GetClustersForImageResponse":
        return dc_td.GetClustersForImageResponse.make_one(res)

    def get_code_security_integration(
        self,
        res: "bs_td.GetCodeSecurityIntegrationResponseTypeDef",
    ) -> "dc_td.GetCodeSecurityIntegrationResponse":
        return dc_td.GetCodeSecurityIntegrationResponse.make_one(res)

    def get_code_security_scan(
        self,
        res: "bs_td.GetCodeSecurityScanResponseTypeDef",
    ) -> "dc_td.GetCodeSecurityScanResponse":
        return dc_td.GetCodeSecurityScanResponse.make_one(res)

    def get_code_security_scan_configuration(
        self,
        res: "bs_td.GetCodeSecurityScanConfigurationResponseTypeDef",
    ) -> "dc_td.GetCodeSecurityScanConfigurationResponse":
        return dc_td.GetCodeSecurityScanConfigurationResponse.make_one(res)

    def get_configuration(
        self,
        res: "bs_td.GetConfigurationResponseTypeDef",
    ) -> "dc_td.GetConfigurationResponse":
        return dc_td.GetConfigurationResponse.make_one(res)

    def get_delegated_admin_account(
        self,
        res: "bs_td.GetDelegatedAdminAccountResponseTypeDef",
    ) -> "dc_td.GetDelegatedAdminAccountResponse":
        return dc_td.GetDelegatedAdminAccountResponse.make_one(res)

    def get_ec2_deep_inspection_configuration(
        self,
        res: "bs_td.GetEc2DeepInspectionConfigurationResponseTypeDef",
    ) -> "dc_td.GetEc2DeepInspectionConfigurationResponse":
        return dc_td.GetEc2DeepInspectionConfigurationResponse.make_one(res)

    def get_encryption_key(
        self,
        res: "bs_td.GetEncryptionKeyResponseTypeDef",
    ) -> "dc_td.GetEncryptionKeyResponse":
        return dc_td.GetEncryptionKeyResponse.make_one(res)

    def get_findings_report_status(
        self,
        res: "bs_td.GetFindingsReportStatusResponseTypeDef",
    ) -> "dc_td.GetFindingsReportStatusResponse":
        return dc_td.GetFindingsReportStatusResponse.make_one(res)

    def get_member(
        self,
        res: "bs_td.GetMemberResponseTypeDef",
    ) -> "dc_td.GetMemberResponse":
        return dc_td.GetMemberResponse.make_one(res)

    def get_sbom_export(
        self,
        res: "bs_td.GetSbomExportResponseTypeDef",
    ) -> "dc_td.GetSbomExportResponse":
        return dc_td.GetSbomExportResponse.make_one(res)

    def list_account_permissions(
        self,
        res: "bs_td.ListAccountPermissionsResponseTypeDef",
    ) -> "dc_td.ListAccountPermissionsResponse":
        return dc_td.ListAccountPermissionsResponse.make_one(res)

    def list_cis_scan_configurations(
        self,
        res: "bs_td.ListCisScanConfigurationsResponseTypeDef",
    ) -> "dc_td.ListCisScanConfigurationsResponse":
        return dc_td.ListCisScanConfigurationsResponse.make_one(res)

    def list_cis_scan_results_aggregated_by_checks(
        self,
        res: "bs_td.ListCisScanResultsAggregatedByChecksResponseTypeDef",
    ) -> "dc_td.ListCisScanResultsAggregatedByChecksResponse":
        return dc_td.ListCisScanResultsAggregatedByChecksResponse.make_one(res)

    def list_cis_scan_results_aggregated_by_target_resource(
        self,
        res: "bs_td.ListCisScanResultsAggregatedByTargetResourceResponseTypeDef",
    ) -> "dc_td.ListCisScanResultsAggregatedByTargetResourceResponse":
        return dc_td.ListCisScanResultsAggregatedByTargetResourceResponse.make_one(res)

    def list_cis_scans(
        self,
        res: "bs_td.ListCisScansResponseTypeDef",
    ) -> "dc_td.ListCisScansResponse":
        return dc_td.ListCisScansResponse.make_one(res)

    def list_code_security_integrations(
        self,
        res: "bs_td.ListCodeSecurityIntegrationsResponseTypeDef",
    ) -> "dc_td.ListCodeSecurityIntegrationsResponse":
        return dc_td.ListCodeSecurityIntegrationsResponse.make_one(res)

    def list_code_security_scan_configuration_associations(
        self,
        res: "bs_td.ListCodeSecurityScanConfigurationAssociationsResponseTypeDef",
    ) -> "dc_td.ListCodeSecurityScanConfigurationAssociationsResponse":
        return dc_td.ListCodeSecurityScanConfigurationAssociationsResponse.make_one(res)

    def list_code_security_scan_configurations(
        self,
        res: "bs_td.ListCodeSecurityScanConfigurationsResponseTypeDef",
    ) -> "dc_td.ListCodeSecurityScanConfigurationsResponse":
        return dc_td.ListCodeSecurityScanConfigurationsResponse.make_one(res)

    def list_coverage(
        self,
        res: "bs_td.ListCoverageResponseTypeDef",
    ) -> "dc_td.ListCoverageResponse":
        return dc_td.ListCoverageResponse.make_one(res)

    def list_coverage_statistics(
        self,
        res: "bs_td.ListCoverageStatisticsResponseTypeDef",
    ) -> "dc_td.ListCoverageStatisticsResponse":
        return dc_td.ListCoverageStatisticsResponse.make_one(res)

    def list_delegated_admin_accounts(
        self,
        res: "bs_td.ListDelegatedAdminAccountsResponseTypeDef",
    ) -> "dc_td.ListDelegatedAdminAccountsResponse":
        return dc_td.ListDelegatedAdminAccountsResponse.make_one(res)

    def list_filters(
        self,
        res: "bs_td.ListFiltersResponseTypeDef",
    ) -> "dc_td.ListFiltersResponse":
        return dc_td.ListFiltersResponse.make_one(res)

    def list_finding_aggregations(
        self,
        res: "bs_td.ListFindingAggregationsResponseTypeDef",
    ) -> "dc_td.ListFindingAggregationsResponse":
        return dc_td.ListFindingAggregationsResponse.make_one(res)

    def list_findings(
        self,
        res: "bs_td.ListFindingsResponseTypeDef",
    ) -> "dc_td.ListFindingsResponse":
        return dc_td.ListFindingsResponse.make_one(res)

    def list_members(
        self,
        res: "bs_td.ListMembersResponseTypeDef",
    ) -> "dc_td.ListMembersResponse":
        return dc_td.ListMembersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_usage_totals(
        self,
        res: "bs_td.ListUsageTotalsResponseTypeDef",
    ) -> "dc_td.ListUsageTotalsResponse":
        return dc_td.ListUsageTotalsResponse.make_one(res)

    def search_vulnerabilities(
        self,
        res: "bs_td.SearchVulnerabilitiesResponseTypeDef",
    ) -> "dc_td.SearchVulnerabilitiesResponse":
        return dc_td.SearchVulnerabilitiesResponse.make_one(res)

    def start_code_security_scan(
        self,
        res: "bs_td.StartCodeSecurityScanResponseTypeDef",
    ) -> "dc_td.StartCodeSecurityScanResponse":
        return dc_td.StartCodeSecurityScanResponse.make_one(res)

    def update_cis_scan_configuration(
        self,
        res: "bs_td.UpdateCisScanConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateCisScanConfigurationResponse":
        return dc_td.UpdateCisScanConfigurationResponse.make_one(res)

    def update_code_security_integration(
        self,
        res: "bs_td.UpdateCodeSecurityIntegrationResponseTypeDef",
    ) -> "dc_td.UpdateCodeSecurityIntegrationResponse":
        return dc_td.UpdateCodeSecurityIntegrationResponse.make_one(res)

    def update_code_security_scan_configuration(
        self,
        res: "bs_td.UpdateCodeSecurityScanConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateCodeSecurityScanConfigurationResponse":
        return dc_td.UpdateCodeSecurityScanConfigurationResponse.make_one(res)

    def update_ec2_deep_inspection_configuration(
        self,
        res: "bs_td.UpdateEc2DeepInspectionConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateEc2DeepInspectionConfigurationResponse":
        return dc_td.UpdateEc2DeepInspectionConfigurationResponse.make_one(res)

    def update_filter(
        self,
        res: "bs_td.UpdateFilterResponseTypeDef",
    ) -> "dc_td.UpdateFilterResponse":
        return dc_td.UpdateFilterResponse.make_one(res)

    def update_organization_configuration(
        self,
        res: "bs_td.UpdateOrganizationConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateOrganizationConfigurationResponse":
        return dc_td.UpdateOrganizationConfigurationResponse.make_one(res)


inspector2_caster = INSPECTOR2Caster()
