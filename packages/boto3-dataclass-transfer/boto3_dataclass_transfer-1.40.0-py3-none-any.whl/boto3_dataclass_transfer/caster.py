# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_transfer import type_defs as bs_td


class TRANSFERCaster:

    def create_access(
        self,
        res: "bs_td.CreateAccessResponseTypeDef",
    ) -> "dc_td.CreateAccessResponse":
        return dc_td.CreateAccessResponse.make_one(res)

    def create_agreement(
        self,
        res: "bs_td.CreateAgreementResponseTypeDef",
    ) -> "dc_td.CreateAgreementResponse":
        return dc_td.CreateAgreementResponse.make_one(res)

    def create_connector(
        self,
        res: "bs_td.CreateConnectorResponseTypeDef",
    ) -> "dc_td.CreateConnectorResponse":
        return dc_td.CreateConnectorResponse.make_one(res)

    def create_profile(
        self,
        res: "bs_td.CreateProfileResponseTypeDef",
    ) -> "dc_td.CreateProfileResponse":
        return dc_td.CreateProfileResponse.make_one(res)

    def create_server(
        self,
        res: "bs_td.CreateServerResponseTypeDef",
    ) -> "dc_td.CreateServerResponse":
        return dc_td.CreateServerResponse.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResponseTypeDef",
    ) -> "dc_td.CreateUserResponse":
        return dc_td.CreateUserResponse.make_one(res)

    def create_web_app(
        self,
        res: "bs_td.CreateWebAppResponseTypeDef",
    ) -> "dc_td.CreateWebAppResponse":
        return dc_td.CreateWebAppResponse.make_one(res)

    def create_workflow(
        self,
        res: "bs_td.CreateWorkflowResponseTypeDef",
    ) -> "dc_td.CreateWorkflowResponse":
        return dc_td.CreateWorkflowResponse.make_one(res)

    def delete_access(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_agreement(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_connector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_host_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_server(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_ssh_public_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_web_app(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_web_app_customization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_workflow(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_access(
        self,
        res: "bs_td.DescribeAccessResponseTypeDef",
    ) -> "dc_td.DescribeAccessResponse":
        return dc_td.DescribeAccessResponse.make_one(res)

    def describe_agreement(
        self,
        res: "bs_td.DescribeAgreementResponseTypeDef",
    ) -> "dc_td.DescribeAgreementResponse":
        return dc_td.DescribeAgreementResponse.make_one(res)

    def describe_certificate(
        self,
        res: "bs_td.DescribeCertificateResponseTypeDef",
    ) -> "dc_td.DescribeCertificateResponse":
        return dc_td.DescribeCertificateResponse.make_one(res)

    def describe_connector(
        self,
        res: "bs_td.DescribeConnectorResponseTypeDef",
    ) -> "dc_td.DescribeConnectorResponse":
        return dc_td.DescribeConnectorResponse.make_one(res)

    def describe_execution(
        self,
        res: "bs_td.DescribeExecutionResponseTypeDef",
    ) -> "dc_td.DescribeExecutionResponse":
        return dc_td.DescribeExecutionResponse.make_one(res)

    def describe_host_key(
        self,
        res: "bs_td.DescribeHostKeyResponseTypeDef",
    ) -> "dc_td.DescribeHostKeyResponse":
        return dc_td.DescribeHostKeyResponse.make_one(res)

    def describe_profile(
        self,
        res: "bs_td.DescribeProfileResponseTypeDef",
    ) -> "dc_td.DescribeProfileResponse":
        return dc_td.DescribeProfileResponse.make_one(res)

    def describe_security_policy(
        self,
        res: "bs_td.DescribeSecurityPolicyResponseTypeDef",
    ) -> "dc_td.DescribeSecurityPolicyResponse":
        return dc_td.DescribeSecurityPolicyResponse.make_one(res)

    def describe_server(
        self,
        res: "bs_td.DescribeServerResponseTypeDef",
    ) -> "dc_td.DescribeServerResponse":
        return dc_td.DescribeServerResponse.make_one(res)

    def describe_user(
        self,
        res: "bs_td.DescribeUserResponseTypeDef",
    ) -> "dc_td.DescribeUserResponse":
        return dc_td.DescribeUserResponse.make_one(res)

    def describe_web_app(
        self,
        res: "bs_td.DescribeWebAppResponseTypeDef",
    ) -> "dc_td.DescribeWebAppResponse":
        return dc_td.DescribeWebAppResponse.make_one(res)

    def describe_web_app_customization(
        self,
        res: "bs_td.DescribeWebAppCustomizationResponseTypeDef",
    ) -> "dc_td.DescribeWebAppCustomizationResponse":
        return dc_td.DescribeWebAppCustomizationResponse.make_one(res)

    def describe_workflow(
        self,
        res: "bs_td.DescribeWorkflowResponseTypeDef",
    ) -> "dc_td.DescribeWorkflowResponse":
        return dc_td.DescribeWorkflowResponse.make_one(res)

    def import_certificate(
        self,
        res: "bs_td.ImportCertificateResponseTypeDef",
    ) -> "dc_td.ImportCertificateResponse":
        return dc_td.ImportCertificateResponse.make_one(res)

    def import_host_key(
        self,
        res: "bs_td.ImportHostKeyResponseTypeDef",
    ) -> "dc_td.ImportHostKeyResponse":
        return dc_td.ImportHostKeyResponse.make_one(res)

    def import_ssh_public_key(
        self,
        res: "bs_td.ImportSshPublicKeyResponseTypeDef",
    ) -> "dc_td.ImportSshPublicKeyResponse":
        return dc_td.ImportSshPublicKeyResponse.make_one(res)

    def list_accesses(
        self,
        res: "bs_td.ListAccessesResponseTypeDef",
    ) -> "dc_td.ListAccessesResponse":
        return dc_td.ListAccessesResponse.make_one(res)

    def list_agreements(
        self,
        res: "bs_td.ListAgreementsResponseTypeDef",
    ) -> "dc_td.ListAgreementsResponse":
        return dc_td.ListAgreementsResponse.make_one(res)

    def list_certificates(
        self,
        res: "bs_td.ListCertificatesResponseTypeDef",
    ) -> "dc_td.ListCertificatesResponse":
        return dc_td.ListCertificatesResponse.make_one(res)

    def list_connectors(
        self,
        res: "bs_td.ListConnectorsResponseTypeDef",
    ) -> "dc_td.ListConnectorsResponse":
        return dc_td.ListConnectorsResponse.make_one(res)

    def list_executions(
        self,
        res: "bs_td.ListExecutionsResponseTypeDef",
    ) -> "dc_td.ListExecutionsResponse":
        return dc_td.ListExecutionsResponse.make_one(res)

    def list_file_transfer_results(
        self,
        res: "bs_td.ListFileTransferResultsResponseTypeDef",
    ) -> "dc_td.ListFileTransferResultsResponse":
        return dc_td.ListFileTransferResultsResponse.make_one(res)

    def list_host_keys(
        self,
        res: "bs_td.ListHostKeysResponseTypeDef",
    ) -> "dc_td.ListHostKeysResponse":
        return dc_td.ListHostKeysResponse.make_one(res)

    def list_profiles(
        self,
        res: "bs_td.ListProfilesResponseTypeDef",
    ) -> "dc_td.ListProfilesResponse":
        return dc_td.ListProfilesResponse.make_one(res)

    def list_security_policies(
        self,
        res: "bs_td.ListSecurityPoliciesResponseTypeDef",
    ) -> "dc_td.ListSecurityPoliciesResponse":
        return dc_td.ListSecurityPoliciesResponse.make_one(res)

    def list_servers(
        self,
        res: "bs_td.ListServersResponseTypeDef",
    ) -> "dc_td.ListServersResponse":
        return dc_td.ListServersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def list_web_apps(
        self,
        res: "bs_td.ListWebAppsResponseTypeDef",
    ) -> "dc_td.ListWebAppsResponse":
        return dc_td.ListWebAppsResponse.make_one(res)

    def list_workflows(
        self,
        res: "bs_td.ListWorkflowsResponseTypeDef",
    ) -> "dc_td.ListWorkflowsResponse":
        return dc_td.ListWorkflowsResponse.make_one(res)

    def start_directory_listing(
        self,
        res: "bs_td.StartDirectoryListingResponseTypeDef",
    ) -> "dc_td.StartDirectoryListingResponse":
        return dc_td.StartDirectoryListingResponse.make_one(res)

    def start_file_transfer(
        self,
        res: "bs_td.StartFileTransferResponseTypeDef",
    ) -> "dc_td.StartFileTransferResponse":
        return dc_td.StartFileTransferResponse.make_one(res)

    def start_remote_delete(
        self,
        res: "bs_td.StartRemoteDeleteResponseTypeDef",
    ) -> "dc_td.StartRemoteDeleteResponse":
        return dc_td.StartRemoteDeleteResponse.make_one(res)

    def start_remote_move(
        self,
        res: "bs_td.StartRemoteMoveResponseTypeDef",
    ) -> "dc_td.StartRemoteMoveResponse":
        return dc_td.StartRemoteMoveResponse.make_one(res)

    def start_server(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_server(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def test_connection(
        self,
        res: "bs_td.TestConnectionResponseTypeDef",
    ) -> "dc_td.TestConnectionResponse":
        return dc_td.TestConnectionResponse.make_one(res)

    def test_identity_provider(
        self,
        res: "bs_td.TestIdentityProviderResponseTypeDef",
    ) -> "dc_td.TestIdentityProviderResponse":
        return dc_td.TestIdentityProviderResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_access(
        self,
        res: "bs_td.UpdateAccessResponseTypeDef",
    ) -> "dc_td.UpdateAccessResponse":
        return dc_td.UpdateAccessResponse.make_one(res)

    def update_agreement(
        self,
        res: "bs_td.UpdateAgreementResponseTypeDef",
    ) -> "dc_td.UpdateAgreementResponse":
        return dc_td.UpdateAgreementResponse.make_one(res)

    def update_certificate(
        self,
        res: "bs_td.UpdateCertificateResponseTypeDef",
    ) -> "dc_td.UpdateCertificateResponse":
        return dc_td.UpdateCertificateResponse.make_one(res)

    def update_connector(
        self,
        res: "bs_td.UpdateConnectorResponseTypeDef",
    ) -> "dc_td.UpdateConnectorResponse":
        return dc_td.UpdateConnectorResponse.make_one(res)

    def update_host_key(
        self,
        res: "bs_td.UpdateHostKeyResponseTypeDef",
    ) -> "dc_td.UpdateHostKeyResponse":
        return dc_td.UpdateHostKeyResponse.make_one(res)

    def update_profile(
        self,
        res: "bs_td.UpdateProfileResponseTypeDef",
    ) -> "dc_td.UpdateProfileResponse":
        return dc_td.UpdateProfileResponse.make_one(res)

    def update_server(
        self,
        res: "bs_td.UpdateServerResponseTypeDef",
    ) -> "dc_td.UpdateServerResponse":
        return dc_td.UpdateServerResponse.make_one(res)

    def update_user(
        self,
        res: "bs_td.UpdateUserResponseTypeDef",
    ) -> "dc_td.UpdateUserResponse":
        return dc_td.UpdateUserResponse.make_one(res)

    def update_web_app(
        self,
        res: "bs_td.UpdateWebAppResponseTypeDef",
    ) -> "dc_td.UpdateWebAppResponse":
        return dc_td.UpdateWebAppResponse.make_one(res)

    def update_web_app_customization(
        self,
        res: "bs_td.UpdateWebAppCustomizationResponseTypeDef",
    ) -> "dc_td.UpdateWebAppCustomizationResponse":
        return dc_td.UpdateWebAppCustomizationResponse.make_one(res)


transfer_caster = TRANSFERCaster()
