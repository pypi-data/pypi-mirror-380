# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_greengrass import type_defs as bs_td


class GREENGRASSCaster:

    def associate_role_to_group(
        self,
        res: "bs_td.AssociateRoleToGroupResponseTypeDef",
    ) -> "dc_td.AssociateRoleToGroupResponse":
        return dc_td.AssociateRoleToGroupResponse.make_one(res)

    def associate_service_role_to_account(
        self,
        res: "bs_td.AssociateServiceRoleToAccountResponseTypeDef",
    ) -> "dc_td.AssociateServiceRoleToAccountResponse":
        return dc_td.AssociateServiceRoleToAccountResponse.make_one(res)

    def create_connector_definition(
        self,
        res: "bs_td.CreateConnectorDefinitionResponseTypeDef",
    ) -> "dc_td.CreateConnectorDefinitionResponse":
        return dc_td.CreateConnectorDefinitionResponse.make_one(res)

    def create_connector_definition_version(
        self,
        res: "bs_td.CreateConnectorDefinitionVersionResponseTypeDef",
    ) -> "dc_td.CreateConnectorDefinitionVersionResponse":
        return dc_td.CreateConnectorDefinitionVersionResponse.make_one(res)

    def create_core_definition(
        self,
        res: "bs_td.CreateCoreDefinitionResponseTypeDef",
    ) -> "dc_td.CreateCoreDefinitionResponse":
        return dc_td.CreateCoreDefinitionResponse.make_one(res)

    def create_core_definition_version(
        self,
        res: "bs_td.CreateCoreDefinitionVersionResponseTypeDef",
    ) -> "dc_td.CreateCoreDefinitionVersionResponse":
        return dc_td.CreateCoreDefinitionVersionResponse.make_one(res)

    def create_deployment(
        self,
        res: "bs_td.CreateDeploymentResponseTypeDef",
    ) -> "dc_td.CreateDeploymentResponse":
        return dc_td.CreateDeploymentResponse.make_one(res)

    def create_device_definition(
        self,
        res: "bs_td.CreateDeviceDefinitionResponseTypeDef",
    ) -> "dc_td.CreateDeviceDefinitionResponse":
        return dc_td.CreateDeviceDefinitionResponse.make_one(res)

    def create_device_definition_version(
        self,
        res: "bs_td.CreateDeviceDefinitionVersionResponseTypeDef",
    ) -> "dc_td.CreateDeviceDefinitionVersionResponse":
        return dc_td.CreateDeviceDefinitionVersionResponse.make_one(res)

    def create_function_definition(
        self,
        res: "bs_td.CreateFunctionDefinitionResponseTypeDef",
    ) -> "dc_td.CreateFunctionDefinitionResponse":
        return dc_td.CreateFunctionDefinitionResponse.make_one(res)

    def create_function_definition_version(
        self,
        res: "bs_td.CreateFunctionDefinitionVersionResponseTypeDef",
    ) -> "dc_td.CreateFunctionDefinitionVersionResponse":
        return dc_td.CreateFunctionDefinitionVersionResponse.make_one(res)

    def create_group(
        self,
        res: "bs_td.CreateGroupResponseTypeDef",
    ) -> "dc_td.CreateGroupResponse":
        return dc_td.CreateGroupResponse.make_one(res)

    def create_group_certificate_authority(
        self,
        res: "bs_td.CreateGroupCertificateAuthorityResponseTypeDef",
    ) -> "dc_td.CreateGroupCertificateAuthorityResponse":
        return dc_td.CreateGroupCertificateAuthorityResponse.make_one(res)

    def create_group_version(
        self,
        res: "bs_td.CreateGroupVersionResponseTypeDef",
    ) -> "dc_td.CreateGroupVersionResponse":
        return dc_td.CreateGroupVersionResponse.make_one(res)

    def create_logger_definition(
        self,
        res: "bs_td.CreateLoggerDefinitionResponseTypeDef",
    ) -> "dc_td.CreateLoggerDefinitionResponse":
        return dc_td.CreateLoggerDefinitionResponse.make_one(res)

    def create_logger_definition_version(
        self,
        res: "bs_td.CreateLoggerDefinitionVersionResponseTypeDef",
    ) -> "dc_td.CreateLoggerDefinitionVersionResponse":
        return dc_td.CreateLoggerDefinitionVersionResponse.make_one(res)

    def create_resource_definition(
        self,
        res: "bs_td.CreateResourceDefinitionResponseTypeDef",
    ) -> "dc_td.CreateResourceDefinitionResponse":
        return dc_td.CreateResourceDefinitionResponse.make_one(res)

    def create_resource_definition_version(
        self,
        res: "bs_td.CreateResourceDefinitionVersionResponseTypeDef",
    ) -> "dc_td.CreateResourceDefinitionVersionResponse":
        return dc_td.CreateResourceDefinitionVersionResponse.make_one(res)

    def create_software_update_job(
        self,
        res: "bs_td.CreateSoftwareUpdateJobResponseTypeDef",
    ) -> "dc_td.CreateSoftwareUpdateJobResponse":
        return dc_td.CreateSoftwareUpdateJobResponse.make_one(res)

    def create_subscription_definition(
        self,
        res: "bs_td.CreateSubscriptionDefinitionResponseTypeDef",
    ) -> "dc_td.CreateSubscriptionDefinitionResponse":
        return dc_td.CreateSubscriptionDefinitionResponse.make_one(res)

    def create_subscription_definition_version(
        self,
        res: "bs_td.CreateSubscriptionDefinitionVersionResponseTypeDef",
    ) -> "dc_td.CreateSubscriptionDefinitionVersionResponse":
        return dc_td.CreateSubscriptionDefinitionVersionResponse.make_one(res)

    def disassociate_role_from_group(
        self,
        res: "bs_td.DisassociateRoleFromGroupResponseTypeDef",
    ) -> "dc_td.DisassociateRoleFromGroupResponse":
        return dc_td.DisassociateRoleFromGroupResponse.make_one(res)

    def disassociate_service_role_from_account(
        self,
        res: "bs_td.DisassociateServiceRoleFromAccountResponseTypeDef",
    ) -> "dc_td.DisassociateServiceRoleFromAccountResponse":
        return dc_td.DisassociateServiceRoleFromAccountResponse.make_one(res)

    def get_associated_role(
        self,
        res: "bs_td.GetAssociatedRoleResponseTypeDef",
    ) -> "dc_td.GetAssociatedRoleResponse":
        return dc_td.GetAssociatedRoleResponse.make_one(res)

    def get_bulk_deployment_status(
        self,
        res: "bs_td.GetBulkDeploymentStatusResponseTypeDef",
    ) -> "dc_td.GetBulkDeploymentStatusResponse":
        return dc_td.GetBulkDeploymentStatusResponse.make_one(res)

    def get_connectivity_info(
        self,
        res: "bs_td.GetConnectivityInfoResponseTypeDef",
    ) -> "dc_td.GetConnectivityInfoResponse":
        return dc_td.GetConnectivityInfoResponse.make_one(res)

    def get_connector_definition(
        self,
        res: "bs_td.GetConnectorDefinitionResponseTypeDef",
    ) -> "dc_td.GetConnectorDefinitionResponse":
        return dc_td.GetConnectorDefinitionResponse.make_one(res)

    def get_connector_definition_version(
        self,
        res: "bs_td.GetConnectorDefinitionVersionResponseTypeDef",
    ) -> "dc_td.GetConnectorDefinitionVersionResponse":
        return dc_td.GetConnectorDefinitionVersionResponse.make_one(res)

    def get_core_definition(
        self,
        res: "bs_td.GetCoreDefinitionResponseTypeDef",
    ) -> "dc_td.GetCoreDefinitionResponse":
        return dc_td.GetCoreDefinitionResponse.make_one(res)

    def get_core_definition_version(
        self,
        res: "bs_td.GetCoreDefinitionVersionResponseTypeDef",
    ) -> "dc_td.GetCoreDefinitionVersionResponse":
        return dc_td.GetCoreDefinitionVersionResponse.make_one(res)

    def get_deployment_status(
        self,
        res: "bs_td.GetDeploymentStatusResponseTypeDef",
    ) -> "dc_td.GetDeploymentStatusResponse":
        return dc_td.GetDeploymentStatusResponse.make_one(res)

    def get_device_definition(
        self,
        res: "bs_td.GetDeviceDefinitionResponseTypeDef",
    ) -> "dc_td.GetDeviceDefinitionResponse":
        return dc_td.GetDeviceDefinitionResponse.make_one(res)

    def get_device_definition_version(
        self,
        res: "bs_td.GetDeviceDefinitionVersionResponseTypeDef",
    ) -> "dc_td.GetDeviceDefinitionVersionResponse":
        return dc_td.GetDeviceDefinitionVersionResponse.make_one(res)

    def get_function_definition(
        self,
        res: "bs_td.GetFunctionDefinitionResponseTypeDef",
    ) -> "dc_td.GetFunctionDefinitionResponse":
        return dc_td.GetFunctionDefinitionResponse.make_one(res)

    def get_function_definition_version(
        self,
        res: "bs_td.GetFunctionDefinitionVersionResponseTypeDef",
    ) -> "dc_td.GetFunctionDefinitionVersionResponse":
        return dc_td.GetFunctionDefinitionVersionResponse.make_one(res)

    def get_group(
        self,
        res: "bs_td.GetGroupResponseTypeDef",
    ) -> "dc_td.GetGroupResponse":
        return dc_td.GetGroupResponse.make_one(res)

    def get_group_certificate_authority(
        self,
        res: "bs_td.GetGroupCertificateAuthorityResponseTypeDef",
    ) -> "dc_td.GetGroupCertificateAuthorityResponse":
        return dc_td.GetGroupCertificateAuthorityResponse.make_one(res)

    def get_group_certificate_configuration(
        self,
        res: "bs_td.GetGroupCertificateConfigurationResponseTypeDef",
    ) -> "dc_td.GetGroupCertificateConfigurationResponse":
        return dc_td.GetGroupCertificateConfigurationResponse.make_one(res)

    def get_group_version(
        self,
        res: "bs_td.GetGroupVersionResponseTypeDef",
    ) -> "dc_td.GetGroupVersionResponse":
        return dc_td.GetGroupVersionResponse.make_one(res)

    def get_logger_definition(
        self,
        res: "bs_td.GetLoggerDefinitionResponseTypeDef",
    ) -> "dc_td.GetLoggerDefinitionResponse":
        return dc_td.GetLoggerDefinitionResponse.make_one(res)

    def get_logger_definition_version(
        self,
        res: "bs_td.GetLoggerDefinitionVersionResponseTypeDef",
    ) -> "dc_td.GetLoggerDefinitionVersionResponse":
        return dc_td.GetLoggerDefinitionVersionResponse.make_one(res)

    def get_resource_definition(
        self,
        res: "bs_td.GetResourceDefinitionResponseTypeDef",
    ) -> "dc_td.GetResourceDefinitionResponse":
        return dc_td.GetResourceDefinitionResponse.make_one(res)

    def get_resource_definition_version(
        self,
        res: "bs_td.GetResourceDefinitionVersionResponseTypeDef",
    ) -> "dc_td.GetResourceDefinitionVersionResponse":
        return dc_td.GetResourceDefinitionVersionResponse.make_one(res)

    def get_service_role_for_account(
        self,
        res: "bs_td.GetServiceRoleForAccountResponseTypeDef",
    ) -> "dc_td.GetServiceRoleForAccountResponse":
        return dc_td.GetServiceRoleForAccountResponse.make_one(res)

    def get_subscription_definition(
        self,
        res: "bs_td.GetSubscriptionDefinitionResponseTypeDef",
    ) -> "dc_td.GetSubscriptionDefinitionResponse":
        return dc_td.GetSubscriptionDefinitionResponse.make_one(res)

    def get_subscription_definition_version(
        self,
        res: "bs_td.GetSubscriptionDefinitionVersionResponseTypeDef",
    ) -> "dc_td.GetSubscriptionDefinitionVersionResponse":
        return dc_td.GetSubscriptionDefinitionVersionResponse.make_one(res)

    def get_thing_runtime_configuration(
        self,
        res: "bs_td.GetThingRuntimeConfigurationResponseTypeDef",
    ) -> "dc_td.GetThingRuntimeConfigurationResponse":
        return dc_td.GetThingRuntimeConfigurationResponse.make_one(res)

    def list_bulk_deployment_detailed_reports(
        self,
        res: "bs_td.ListBulkDeploymentDetailedReportsResponseTypeDef",
    ) -> "dc_td.ListBulkDeploymentDetailedReportsResponse":
        return dc_td.ListBulkDeploymentDetailedReportsResponse.make_one(res)

    def list_bulk_deployments(
        self,
        res: "bs_td.ListBulkDeploymentsResponseTypeDef",
    ) -> "dc_td.ListBulkDeploymentsResponse":
        return dc_td.ListBulkDeploymentsResponse.make_one(res)

    def list_connector_definition_versions(
        self,
        res: "bs_td.ListConnectorDefinitionVersionsResponseTypeDef",
    ) -> "dc_td.ListConnectorDefinitionVersionsResponse":
        return dc_td.ListConnectorDefinitionVersionsResponse.make_one(res)

    def list_connector_definitions(
        self,
        res: "bs_td.ListConnectorDefinitionsResponseTypeDef",
    ) -> "dc_td.ListConnectorDefinitionsResponse":
        return dc_td.ListConnectorDefinitionsResponse.make_one(res)

    def list_core_definition_versions(
        self,
        res: "bs_td.ListCoreDefinitionVersionsResponseTypeDef",
    ) -> "dc_td.ListCoreDefinitionVersionsResponse":
        return dc_td.ListCoreDefinitionVersionsResponse.make_one(res)

    def list_core_definitions(
        self,
        res: "bs_td.ListCoreDefinitionsResponseTypeDef",
    ) -> "dc_td.ListCoreDefinitionsResponse":
        return dc_td.ListCoreDefinitionsResponse.make_one(res)

    def list_deployments(
        self,
        res: "bs_td.ListDeploymentsResponseTypeDef",
    ) -> "dc_td.ListDeploymentsResponse":
        return dc_td.ListDeploymentsResponse.make_one(res)

    def list_device_definition_versions(
        self,
        res: "bs_td.ListDeviceDefinitionVersionsResponseTypeDef",
    ) -> "dc_td.ListDeviceDefinitionVersionsResponse":
        return dc_td.ListDeviceDefinitionVersionsResponse.make_one(res)

    def list_device_definitions(
        self,
        res: "bs_td.ListDeviceDefinitionsResponseTypeDef",
    ) -> "dc_td.ListDeviceDefinitionsResponse":
        return dc_td.ListDeviceDefinitionsResponse.make_one(res)

    def list_function_definition_versions(
        self,
        res: "bs_td.ListFunctionDefinitionVersionsResponseTypeDef",
    ) -> "dc_td.ListFunctionDefinitionVersionsResponse":
        return dc_td.ListFunctionDefinitionVersionsResponse.make_one(res)

    def list_function_definitions(
        self,
        res: "bs_td.ListFunctionDefinitionsResponseTypeDef",
    ) -> "dc_td.ListFunctionDefinitionsResponse":
        return dc_td.ListFunctionDefinitionsResponse.make_one(res)

    def list_group_certificate_authorities(
        self,
        res: "bs_td.ListGroupCertificateAuthoritiesResponseTypeDef",
    ) -> "dc_td.ListGroupCertificateAuthoritiesResponse":
        return dc_td.ListGroupCertificateAuthoritiesResponse.make_one(res)

    def list_group_versions(
        self,
        res: "bs_td.ListGroupVersionsResponseTypeDef",
    ) -> "dc_td.ListGroupVersionsResponse":
        return dc_td.ListGroupVersionsResponse.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsResponseTypeDef",
    ) -> "dc_td.ListGroupsResponse":
        return dc_td.ListGroupsResponse.make_one(res)

    def list_logger_definition_versions(
        self,
        res: "bs_td.ListLoggerDefinitionVersionsResponseTypeDef",
    ) -> "dc_td.ListLoggerDefinitionVersionsResponse":
        return dc_td.ListLoggerDefinitionVersionsResponse.make_one(res)

    def list_logger_definitions(
        self,
        res: "bs_td.ListLoggerDefinitionsResponseTypeDef",
    ) -> "dc_td.ListLoggerDefinitionsResponse":
        return dc_td.ListLoggerDefinitionsResponse.make_one(res)

    def list_resource_definition_versions(
        self,
        res: "bs_td.ListResourceDefinitionVersionsResponseTypeDef",
    ) -> "dc_td.ListResourceDefinitionVersionsResponse":
        return dc_td.ListResourceDefinitionVersionsResponse.make_one(res)

    def list_resource_definitions(
        self,
        res: "bs_td.ListResourceDefinitionsResponseTypeDef",
    ) -> "dc_td.ListResourceDefinitionsResponse":
        return dc_td.ListResourceDefinitionsResponse.make_one(res)

    def list_subscription_definition_versions(
        self,
        res: "bs_td.ListSubscriptionDefinitionVersionsResponseTypeDef",
    ) -> "dc_td.ListSubscriptionDefinitionVersionsResponse":
        return dc_td.ListSubscriptionDefinitionVersionsResponse.make_one(res)

    def list_subscription_definitions(
        self,
        res: "bs_td.ListSubscriptionDefinitionsResponseTypeDef",
    ) -> "dc_td.ListSubscriptionDefinitionsResponse":
        return dc_td.ListSubscriptionDefinitionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def reset_deployments(
        self,
        res: "bs_td.ResetDeploymentsResponseTypeDef",
    ) -> "dc_td.ResetDeploymentsResponse":
        return dc_td.ResetDeploymentsResponse.make_one(res)

    def start_bulk_deployment(
        self,
        res: "bs_td.StartBulkDeploymentResponseTypeDef",
    ) -> "dc_td.StartBulkDeploymentResponse":
        return dc_td.StartBulkDeploymentResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_connectivity_info(
        self,
        res: "bs_td.UpdateConnectivityInfoResponseTypeDef",
    ) -> "dc_td.UpdateConnectivityInfoResponse":
        return dc_td.UpdateConnectivityInfoResponse.make_one(res)

    def update_group_certificate_configuration(
        self,
        res: "bs_td.UpdateGroupCertificateConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateGroupCertificateConfigurationResponse":
        return dc_td.UpdateGroupCertificateConfigurationResponse.make_one(res)


greengrass_caster = GREENGRASSCaster()
