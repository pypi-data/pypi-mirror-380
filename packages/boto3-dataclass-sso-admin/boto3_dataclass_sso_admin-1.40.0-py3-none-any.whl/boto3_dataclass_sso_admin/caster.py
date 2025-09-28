# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sso_admin import type_defs as bs_td


class SSO_ADMINCaster:

    def create_account_assignment(
        self,
        res: "bs_td.CreateAccountAssignmentResponseTypeDef",
    ) -> "dc_td.CreateAccountAssignmentResponse":
        return dc_td.CreateAccountAssignmentResponse.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_instance(
        self,
        res: "bs_td.CreateInstanceResponseTypeDef",
    ) -> "dc_td.CreateInstanceResponse":
        return dc_td.CreateInstanceResponse.make_one(res)

    def create_permission_set(
        self,
        res: "bs_td.CreatePermissionSetResponseTypeDef",
    ) -> "dc_td.CreatePermissionSetResponse":
        return dc_td.CreatePermissionSetResponse.make_one(res)

    def create_trusted_token_issuer(
        self,
        res: "bs_td.CreateTrustedTokenIssuerResponseTypeDef",
    ) -> "dc_td.CreateTrustedTokenIssuerResponse":
        return dc_td.CreateTrustedTokenIssuerResponse.make_one(res)

    def delete_account_assignment(
        self,
        res: "bs_td.DeleteAccountAssignmentResponseTypeDef",
    ) -> "dc_td.DeleteAccountAssignmentResponse":
        return dc_td.DeleteAccountAssignmentResponse.make_one(res)

    def delete_application_access_scope(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_application_authentication_method(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_application_grant(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_account_assignment_creation_status(
        self,
        res: "bs_td.DescribeAccountAssignmentCreationStatusResponseTypeDef",
    ) -> "dc_td.DescribeAccountAssignmentCreationStatusResponse":
        return dc_td.DescribeAccountAssignmentCreationStatusResponse.make_one(res)

    def describe_account_assignment_deletion_status(
        self,
        res: "bs_td.DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    ) -> "dc_td.DescribeAccountAssignmentDeletionStatusResponse":
        return dc_td.DescribeAccountAssignmentDeletionStatusResponse.make_one(res)

    def describe_application(
        self,
        res: "bs_td.DescribeApplicationResponseTypeDef",
    ) -> "dc_td.DescribeApplicationResponse":
        return dc_td.DescribeApplicationResponse.make_one(res)

    def describe_application_assignment(
        self,
        res: "bs_td.DescribeApplicationAssignmentResponseTypeDef",
    ) -> "dc_td.DescribeApplicationAssignmentResponse":
        return dc_td.DescribeApplicationAssignmentResponse.make_one(res)

    def describe_application_provider(
        self,
        res: "bs_td.DescribeApplicationProviderResponseTypeDef",
    ) -> "dc_td.DescribeApplicationProviderResponse":
        return dc_td.DescribeApplicationProviderResponse.make_one(res)

    def describe_instance(
        self,
        res: "bs_td.DescribeInstanceResponseTypeDef",
    ) -> "dc_td.DescribeInstanceResponse":
        return dc_td.DescribeInstanceResponse.make_one(res)

    def describe_instance_access_control_attribute_configuration(
        self,
        res: "bs_td.DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeInstanceAccessControlAttributeConfigurationResponse":
        return (
            dc_td.DescribeInstanceAccessControlAttributeConfigurationResponse.make_one(
                res
            )
        )

    def describe_permission_set(
        self,
        res: "bs_td.DescribePermissionSetResponseTypeDef",
    ) -> "dc_td.DescribePermissionSetResponse":
        return dc_td.DescribePermissionSetResponse.make_one(res)

    def describe_permission_set_provisioning_status(
        self,
        res: "bs_td.DescribePermissionSetProvisioningStatusResponseTypeDef",
    ) -> "dc_td.DescribePermissionSetProvisioningStatusResponse":
        return dc_td.DescribePermissionSetProvisioningStatusResponse.make_one(res)

    def describe_trusted_token_issuer(
        self,
        res: "bs_td.DescribeTrustedTokenIssuerResponseTypeDef",
    ) -> "dc_td.DescribeTrustedTokenIssuerResponse":
        return dc_td.DescribeTrustedTokenIssuerResponse.make_one(res)

    def get_application_access_scope(
        self,
        res: "bs_td.GetApplicationAccessScopeResponseTypeDef",
    ) -> "dc_td.GetApplicationAccessScopeResponse":
        return dc_td.GetApplicationAccessScopeResponse.make_one(res)

    def get_application_assignment_configuration(
        self,
        res: "bs_td.GetApplicationAssignmentConfigurationResponseTypeDef",
    ) -> "dc_td.GetApplicationAssignmentConfigurationResponse":
        return dc_td.GetApplicationAssignmentConfigurationResponse.make_one(res)

    def get_application_authentication_method(
        self,
        res: "bs_td.GetApplicationAuthenticationMethodResponseTypeDef",
    ) -> "dc_td.GetApplicationAuthenticationMethodResponse":
        return dc_td.GetApplicationAuthenticationMethodResponse.make_one(res)

    def get_application_grant(
        self,
        res: "bs_td.GetApplicationGrantResponseTypeDef",
    ) -> "dc_td.GetApplicationGrantResponse":
        return dc_td.GetApplicationGrantResponse.make_one(res)

    def get_application_session_configuration(
        self,
        res: "bs_td.GetApplicationSessionConfigurationResponseTypeDef",
    ) -> "dc_td.GetApplicationSessionConfigurationResponse":
        return dc_td.GetApplicationSessionConfigurationResponse.make_one(res)

    def get_inline_policy_for_permission_set(
        self,
        res: "bs_td.GetInlinePolicyForPermissionSetResponseTypeDef",
    ) -> "dc_td.GetInlinePolicyForPermissionSetResponse":
        return dc_td.GetInlinePolicyForPermissionSetResponse.make_one(res)

    def get_permissions_boundary_for_permission_set(
        self,
        res: "bs_td.GetPermissionsBoundaryForPermissionSetResponseTypeDef",
    ) -> "dc_td.GetPermissionsBoundaryForPermissionSetResponse":
        return dc_td.GetPermissionsBoundaryForPermissionSetResponse.make_one(res)

    def list_account_assignment_creation_status(
        self,
        res: "bs_td.ListAccountAssignmentCreationStatusResponseTypeDef",
    ) -> "dc_td.ListAccountAssignmentCreationStatusResponse":
        return dc_td.ListAccountAssignmentCreationStatusResponse.make_one(res)

    def list_account_assignment_deletion_status(
        self,
        res: "bs_td.ListAccountAssignmentDeletionStatusResponseTypeDef",
    ) -> "dc_td.ListAccountAssignmentDeletionStatusResponse":
        return dc_td.ListAccountAssignmentDeletionStatusResponse.make_one(res)

    def list_account_assignments(
        self,
        res: "bs_td.ListAccountAssignmentsResponseTypeDef",
    ) -> "dc_td.ListAccountAssignmentsResponse":
        return dc_td.ListAccountAssignmentsResponse.make_one(res)

    def list_account_assignments_for_principal(
        self,
        res: "bs_td.ListAccountAssignmentsForPrincipalResponseTypeDef",
    ) -> "dc_td.ListAccountAssignmentsForPrincipalResponse":
        return dc_td.ListAccountAssignmentsForPrincipalResponse.make_one(res)

    def list_accounts_for_provisioned_permission_set(
        self,
        res: "bs_td.ListAccountsForProvisionedPermissionSetResponseTypeDef",
    ) -> "dc_td.ListAccountsForProvisionedPermissionSetResponse":
        return dc_td.ListAccountsForProvisionedPermissionSetResponse.make_one(res)

    def list_application_access_scopes(
        self,
        res: "bs_td.ListApplicationAccessScopesResponseTypeDef",
    ) -> "dc_td.ListApplicationAccessScopesResponse":
        return dc_td.ListApplicationAccessScopesResponse.make_one(res)

    def list_application_assignments(
        self,
        res: "bs_td.ListApplicationAssignmentsResponseTypeDef",
    ) -> "dc_td.ListApplicationAssignmentsResponse":
        return dc_td.ListApplicationAssignmentsResponse.make_one(res)

    def list_application_assignments_for_principal(
        self,
        res: "bs_td.ListApplicationAssignmentsForPrincipalResponseTypeDef",
    ) -> "dc_td.ListApplicationAssignmentsForPrincipalResponse":
        return dc_td.ListApplicationAssignmentsForPrincipalResponse.make_one(res)

    def list_application_authentication_methods(
        self,
        res: "bs_td.ListApplicationAuthenticationMethodsResponseTypeDef",
    ) -> "dc_td.ListApplicationAuthenticationMethodsResponse":
        return dc_td.ListApplicationAuthenticationMethodsResponse.make_one(res)

    def list_application_grants(
        self,
        res: "bs_td.ListApplicationGrantsResponseTypeDef",
    ) -> "dc_td.ListApplicationGrantsResponse":
        return dc_td.ListApplicationGrantsResponse.make_one(res)

    def list_application_providers(
        self,
        res: "bs_td.ListApplicationProvidersResponseTypeDef",
    ) -> "dc_td.ListApplicationProvidersResponse":
        return dc_td.ListApplicationProvidersResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_customer_managed_policy_references_in_permission_set(
        self,
        res: "bs_td.ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef",
    ) -> "dc_td.ListCustomerManagedPolicyReferencesInPermissionSetResponse":
        return (
            dc_td.ListCustomerManagedPolicyReferencesInPermissionSetResponse.make_one(
                res
            )
        )

    def list_instances(
        self,
        res: "bs_td.ListInstancesResponseTypeDef",
    ) -> "dc_td.ListInstancesResponse":
        return dc_td.ListInstancesResponse.make_one(res)

    def list_managed_policies_in_permission_set(
        self,
        res: "bs_td.ListManagedPoliciesInPermissionSetResponseTypeDef",
    ) -> "dc_td.ListManagedPoliciesInPermissionSetResponse":
        return dc_td.ListManagedPoliciesInPermissionSetResponse.make_one(res)

    def list_permission_set_provisioning_status(
        self,
        res: "bs_td.ListPermissionSetProvisioningStatusResponseTypeDef",
    ) -> "dc_td.ListPermissionSetProvisioningStatusResponse":
        return dc_td.ListPermissionSetProvisioningStatusResponse.make_one(res)

    def list_permission_sets(
        self,
        res: "bs_td.ListPermissionSetsResponseTypeDef",
    ) -> "dc_td.ListPermissionSetsResponse":
        return dc_td.ListPermissionSetsResponse.make_one(res)

    def list_permission_sets_provisioned_to_account(
        self,
        res: "bs_td.ListPermissionSetsProvisionedToAccountResponseTypeDef",
    ) -> "dc_td.ListPermissionSetsProvisionedToAccountResponse":
        return dc_td.ListPermissionSetsProvisionedToAccountResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_trusted_token_issuers(
        self,
        res: "bs_td.ListTrustedTokenIssuersResponseTypeDef",
    ) -> "dc_td.ListTrustedTokenIssuersResponse":
        return dc_td.ListTrustedTokenIssuersResponse.make_one(res)

    def provision_permission_set(
        self,
        res: "bs_td.ProvisionPermissionSetResponseTypeDef",
    ) -> "dc_td.ProvisionPermissionSetResponse":
        return dc_td.ProvisionPermissionSetResponse.make_one(res)

    def put_application_access_scope(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_application_authentication_method(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_application_grant(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


sso_admin_caster = SSO_ADMINCaster()
