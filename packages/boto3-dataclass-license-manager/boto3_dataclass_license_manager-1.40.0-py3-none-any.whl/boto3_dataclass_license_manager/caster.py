# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_license_manager import type_defs as bs_td


class LICENSE_MANAGERCaster:

    def accept_grant(
        self,
        res: "bs_td.AcceptGrantResponseTypeDef",
    ) -> "dc_td.AcceptGrantResponse":
        return dc_td.AcceptGrantResponse.make_one(res)

    def checkout_borrow_license(
        self,
        res: "bs_td.CheckoutBorrowLicenseResponseTypeDef",
    ) -> "dc_td.CheckoutBorrowLicenseResponse":
        return dc_td.CheckoutBorrowLicenseResponse.make_one(res)

    def checkout_license(
        self,
        res: "bs_td.CheckoutLicenseResponseTypeDef",
    ) -> "dc_td.CheckoutLicenseResponse":
        return dc_td.CheckoutLicenseResponse.make_one(res)

    def create_grant(
        self,
        res: "bs_td.CreateGrantResponseTypeDef",
    ) -> "dc_td.CreateGrantResponse":
        return dc_td.CreateGrantResponse.make_one(res)

    def create_grant_version(
        self,
        res: "bs_td.CreateGrantVersionResponseTypeDef",
    ) -> "dc_td.CreateGrantVersionResponse":
        return dc_td.CreateGrantVersionResponse.make_one(res)

    def create_license(
        self,
        res: "bs_td.CreateLicenseResponseTypeDef",
    ) -> "dc_td.CreateLicenseResponse":
        return dc_td.CreateLicenseResponse.make_one(res)

    def create_license_configuration(
        self,
        res: "bs_td.CreateLicenseConfigurationResponseTypeDef",
    ) -> "dc_td.CreateLicenseConfigurationResponse":
        return dc_td.CreateLicenseConfigurationResponse.make_one(res)

    def create_license_conversion_task_for_resource(
        self,
        res: "bs_td.CreateLicenseConversionTaskForResourceResponseTypeDef",
    ) -> "dc_td.CreateLicenseConversionTaskForResourceResponse":
        return dc_td.CreateLicenseConversionTaskForResourceResponse.make_one(res)

    def create_license_manager_report_generator(
        self,
        res: "bs_td.CreateLicenseManagerReportGeneratorResponseTypeDef",
    ) -> "dc_td.CreateLicenseManagerReportGeneratorResponse":
        return dc_td.CreateLicenseManagerReportGeneratorResponse.make_one(res)

    def create_license_version(
        self,
        res: "bs_td.CreateLicenseVersionResponseTypeDef",
    ) -> "dc_td.CreateLicenseVersionResponse":
        return dc_td.CreateLicenseVersionResponse.make_one(res)

    def create_token(
        self,
        res: "bs_td.CreateTokenResponseTypeDef",
    ) -> "dc_td.CreateTokenResponse":
        return dc_td.CreateTokenResponse.make_one(res)

    def delete_grant(
        self,
        res: "bs_td.DeleteGrantResponseTypeDef",
    ) -> "dc_td.DeleteGrantResponse":
        return dc_td.DeleteGrantResponse.make_one(res)

    def delete_license(
        self,
        res: "bs_td.DeleteLicenseResponseTypeDef",
    ) -> "dc_td.DeleteLicenseResponse":
        return dc_td.DeleteLicenseResponse.make_one(res)

    def extend_license_consumption(
        self,
        res: "bs_td.ExtendLicenseConsumptionResponseTypeDef",
    ) -> "dc_td.ExtendLicenseConsumptionResponse":
        return dc_td.ExtendLicenseConsumptionResponse.make_one(res)

    def get_access_token(
        self,
        res: "bs_td.GetAccessTokenResponseTypeDef",
    ) -> "dc_td.GetAccessTokenResponse":
        return dc_td.GetAccessTokenResponse.make_one(res)

    def get_grant(
        self,
        res: "bs_td.GetGrantResponseTypeDef",
    ) -> "dc_td.GetGrantResponse":
        return dc_td.GetGrantResponse.make_one(res)

    def get_license(
        self,
        res: "bs_td.GetLicenseResponseTypeDef",
    ) -> "dc_td.GetLicenseResponse":
        return dc_td.GetLicenseResponse.make_one(res)

    def get_license_configuration(
        self,
        res: "bs_td.GetLicenseConfigurationResponseTypeDef",
    ) -> "dc_td.GetLicenseConfigurationResponse":
        return dc_td.GetLicenseConfigurationResponse.make_one(res)

    def get_license_conversion_task(
        self,
        res: "bs_td.GetLicenseConversionTaskResponseTypeDef",
    ) -> "dc_td.GetLicenseConversionTaskResponse":
        return dc_td.GetLicenseConversionTaskResponse.make_one(res)

    def get_license_manager_report_generator(
        self,
        res: "bs_td.GetLicenseManagerReportGeneratorResponseTypeDef",
    ) -> "dc_td.GetLicenseManagerReportGeneratorResponse":
        return dc_td.GetLicenseManagerReportGeneratorResponse.make_one(res)

    def get_license_usage(
        self,
        res: "bs_td.GetLicenseUsageResponseTypeDef",
    ) -> "dc_td.GetLicenseUsageResponse":
        return dc_td.GetLicenseUsageResponse.make_one(res)

    def get_service_settings(
        self,
        res: "bs_td.GetServiceSettingsResponseTypeDef",
    ) -> "dc_td.GetServiceSettingsResponse":
        return dc_td.GetServiceSettingsResponse.make_one(res)

    def list_associations_for_license_configuration(
        self,
        res: "bs_td.ListAssociationsForLicenseConfigurationResponseTypeDef",
    ) -> "dc_td.ListAssociationsForLicenseConfigurationResponse":
        return dc_td.ListAssociationsForLicenseConfigurationResponse.make_one(res)

    def list_distributed_grants(
        self,
        res: "bs_td.ListDistributedGrantsResponseTypeDef",
    ) -> "dc_td.ListDistributedGrantsResponse":
        return dc_td.ListDistributedGrantsResponse.make_one(res)

    def list_failures_for_license_configuration_operations(
        self,
        res: "bs_td.ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    ) -> "dc_td.ListFailuresForLicenseConfigurationOperationsResponse":
        return dc_td.ListFailuresForLicenseConfigurationOperationsResponse.make_one(res)

    def list_license_configurations(
        self,
        res: "bs_td.ListLicenseConfigurationsResponseTypeDef",
    ) -> "dc_td.ListLicenseConfigurationsResponse":
        return dc_td.ListLicenseConfigurationsResponse.make_one(res)

    def list_license_conversion_tasks(
        self,
        res: "bs_td.ListLicenseConversionTasksResponseTypeDef",
    ) -> "dc_td.ListLicenseConversionTasksResponse":
        return dc_td.ListLicenseConversionTasksResponse.make_one(res)

    def list_license_manager_report_generators(
        self,
        res: "bs_td.ListLicenseManagerReportGeneratorsResponseTypeDef",
    ) -> "dc_td.ListLicenseManagerReportGeneratorsResponse":
        return dc_td.ListLicenseManagerReportGeneratorsResponse.make_one(res)

    def list_license_specifications_for_resource(
        self,
        res: "bs_td.ListLicenseSpecificationsForResourceResponseTypeDef",
    ) -> "dc_td.ListLicenseSpecificationsForResourceResponse":
        return dc_td.ListLicenseSpecificationsForResourceResponse.make_one(res)

    def list_license_versions(
        self,
        res: "bs_td.ListLicenseVersionsResponseTypeDef",
    ) -> "dc_td.ListLicenseVersionsResponse":
        return dc_td.ListLicenseVersionsResponse.make_one(res)

    def list_licenses(
        self,
        res: "bs_td.ListLicensesResponseTypeDef",
    ) -> "dc_td.ListLicensesResponse":
        return dc_td.ListLicensesResponse.make_one(res)

    def list_received_grants(
        self,
        res: "bs_td.ListReceivedGrantsResponseTypeDef",
    ) -> "dc_td.ListReceivedGrantsResponse":
        return dc_td.ListReceivedGrantsResponse.make_one(res)

    def list_received_grants_for_organization(
        self,
        res: "bs_td.ListReceivedGrantsForOrganizationResponseTypeDef",
    ) -> "dc_td.ListReceivedGrantsForOrganizationResponse":
        return dc_td.ListReceivedGrantsForOrganizationResponse.make_one(res)

    def list_received_licenses(
        self,
        res: "bs_td.ListReceivedLicensesResponseTypeDef",
    ) -> "dc_td.ListReceivedLicensesResponse":
        return dc_td.ListReceivedLicensesResponse.make_one(res)

    def list_received_licenses_for_organization(
        self,
        res: "bs_td.ListReceivedLicensesForOrganizationResponseTypeDef",
    ) -> "dc_td.ListReceivedLicensesForOrganizationResponse":
        return dc_td.ListReceivedLicensesForOrganizationResponse.make_one(res)

    def list_resource_inventory(
        self,
        res: "bs_td.ListResourceInventoryResponseTypeDef",
    ) -> "dc_td.ListResourceInventoryResponse":
        return dc_td.ListResourceInventoryResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_tokens(
        self,
        res: "bs_td.ListTokensResponseTypeDef",
    ) -> "dc_td.ListTokensResponse":
        return dc_td.ListTokensResponse.make_one(res)

    def list_usage_for_license_configuration(
        self,
        res: "bs_td.ListUsageForLicenseConfigurationResponseTypeDef",
    ) -> "dc_td.ListUsageForLicenseConfigurationResponse":
        return dc_td.ListUsageForLicenseConfigurationResponse.make_one(res)

    def reject_grant(
        self,
        res: "bs_td.RejectGrantResponseTypeDef",
    ) -> "dc_td.RejectGrantResponse":
        return dc_td.RejectGrantResponse.make_one(res)


license_manager_caster = LICENSE_MANAGERCaster()
