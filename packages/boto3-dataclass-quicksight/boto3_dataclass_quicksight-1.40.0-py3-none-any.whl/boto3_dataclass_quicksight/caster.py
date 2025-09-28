# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_quicksight import type_defs as bs_td


class QUICKSIGHTCaster:

    def batch_create_topic_reviewed_answer(
        self,
        res: "bs_td.BatchCreateTopicReviewedAnswerResponseTypeDef",
    ) -> "dc_td.BatchCreateTopicReviewedAnswerResponse":
        return dc_td.BatchCreateTopicReviewedAnswerResponse.make_one(res)

    def batch_delete_topic_reviewed_answer(
        self,
        res: "bs_td.BatchDeleteTopicReviewedAnswerResponseTypeDef",
    ) -> "dc_td.BatchDeleteTopicReviewedAnswerResponse":
        return dc_td.BatchDeleteTopicReviewedAnswerResponse.make_one(res)

    def cancel_ingestion(
        self,
        res: "bs_td.CancelIngestionResponseTypeDef",
    ) -> "dc_td.CancelIngestionResponse":
        return dc_td.CancelIngestionResponse.make_one(res)

    def create_account_customization(
        self,
        res: "bs_td.CreateAccountCustomizationResponseTypeDef",
    ) -> "dc_td.CreateAccountCustomizationResponse":
        return dc_td.CreateAccountCustomizationResponse.make_one(res)

    def create_account_subscription(
        self,
        res: "bs_td.CreateAccountSubscriptionResponseTypeDef",
    ) -> "dc_td.CreateAccountSubscriptionResponse":
        return dc_td.CreateAccountSubscriptionResponse.make_one(res)

    def create_analysis(
        self,
        res: "bs_td.CreateAnalysisResponseTypeDef",
    ) -> "dc_td.CreateAnalysisResponse":
        return dc_td.CreateAnalysisResponse.make_one(res)

    def create_brand(
        self,
        res: "bs_td.CreateBrandResponseTypeDef",
    ) -> "dc_td.CreateBrandResponse":
        return dc_td.CreateBrandResponse.make_one(res)

    def create_custom_permissions(
        self,
        res: "bs_td.CreateCustomPermissionsResponseTypeDef",
    ) -> "dc_td.CreateCustomPermissionsResponse":
        return dc_td.CreateCustomPermissionsResponse.make_one(res)

    def create_dashboard(
        self,
        res: "bs_td.CreateDashboardResponseTypeDef",
    ) -> "dc_td.CreateDashboardResponse":
        return dc_td.CreateDashboardResponse.make_one(res)

    def create_data_set(
        self,
        res: "bs_td.CreateDataSetResponseTypeDef",
    ) -> "dc_td.CreateDataSetResponse":
        return dc_td.CreateDataSetResponse.make_one(res)

    def create_data_source(
        self,
        res: "bs_td.CreateDataSourceResponseTypeDef",
    ) -> "dc_td.CreateDataSourceResponse":
        return dc_td.CreateDataSourceResponse.make_one(res)

    def create_folder(
        self,
        res: "bs_td.CreateFolderResponseTypeDef",
    ) -> "dc_td.CreateFolderResponse":
        return dc_td.CreateFolderResponse.make_one(res)

    def create_folder_membership(
        self,
        res: "bs_td.CreateFolderMembershipResponseTypeDef",
    ) -> "dc_td.CreateFolderMembershipResponse":
        return dc_td.CreateFolderMembershipResponse.make_one(res)

    def create_group(
        self,
        res: "bs_td.CreateGroupResponseTypeDef",
    ) -> "dc_td.CreateGroupResponse":
        return dc_td.CreateGroupResponse.make_one(res)

    def create_group_membership(
        self,
        res: "bs_td.CreateGroupMembershipResponseTypeDef",
    ) -> "dc_td.CreateGroupMembershipResponse":
        return dc_td.CreateGroupMembershipResponse.make_one(res)

    def create_iam_policy_assignment(
        self,
        res: "bs_td.CreateIAMPolicyAssignmentResponseTypeDef",
    ) -> "dc_td.CreateIAMPolicyAssignmentResponse":
        return dc_td.CreateIAMPolicyAssignmentResponse.make_one(res)

    def create_ingestion(
        self,
        res: "bs_td.CreateIngestionResponseTypeDef",
    ) -> "dc_td.CreateIngestionResponse":
        return dc_td.CreateIngestionResponse.make_one(res)

    def create_namespace(
        self,
        res: "bs_td.CreateNamespaceResponseTypeDef",
    ) -> "dc_td.CreateNamespaceResponse":
        return dc_td.CreateNamespaceResponse.make_one(res)

    def create_refresh_schedule(
        self,
        res: "bs_td.CreateRefreshScheduleResponseTypeDef",
    ) -> "dc_td.CreateRefreshScheduleResponse":
        return dc_td.CreateRefreshScheduleResponse.make_one(res)

    def create_role_membership(
        self,
        res: "bs_td.CreateRoleMembershipResponseTypeDef",
    ) -> "dc_td.CreateRoleMembershipResponse":
        return dc_td.CreateRoleMembershipResponse.make_one(res)

    def create_template(
        self,
        res: "bs_td.CreateTemplateResponseTypeDef",
    ) -> "dc_td.CreateTemplateResponse":
        return dc_td.CreateTemplateResponse.make_one(res)

    def create_template_alias(
        self,
        res: "bs_td.CreateTemplateAliasResponseTypeDef",
    ) -> "dc_td.CreateTemplateAliasResponse":
        return dc_td.CreateTemplateAliasResponse.make_one(res)

    def create_theme(
        self,
        res: "bs_td.CreateThemeResponseTypeDef",
    ) -> "dc_td.CreateThemeResponse":
        return dc_td.CreateThemeResponse.make_one(res)

    def create_theme_alias(
        self,
        res: "bs_td.CreateThemeAliasResponseTypeDef",
    ) -> "dc_td.CreateThemeAliasResponse":
        return dc_td.CreateThemeAliasResponse.make_one(res)

    def create_topic(
        self,
        res: "bs_td.CreateTopicResponseTypeDef",
    ) -> "dc_td.CreateTopicResponse":
        return dc_td.CreateTopicResponse.make_one(res)

    def create_topic_refresh_schedule(
        self,
        res: "bs_td.CreateTopicRefreshScheduleResponseTypeDef",
    ) -> "dc_td.CreateTopicRefreshScheduleResponse":
        return dc_td.CreateTopicRefreshScheduleResponse.make_one(res)

    def create_vpc_connection(
        self,
        res: "bs_td.CreateVPCConnectionResponseTypeDef",
    ) -> "dc_td.CreateVPCConnectionResponse":
        return dc_td.CreateVPCConnectionResponse.make_one(res)

    def delete_account_custom_permission(
        self,
        res: "bs_td.DeleteAccountCustomPermissionResponseTypeDef",
    ) -> "dc_td.DeleteAccountCustomPermissionResponse":
        return dc_td.DeleteAccountCustomPermissionResponse.make_one(res)

    def delete_account_customization(
        self,
        res: "bs_td.DeleteAccountCustomizationResponseTypeDef",
    ) -> "dc_td.DeleteAccountCustomizationResponse":
        return dc_td.DeleteAccountCustomizationResponse.make_one(res)

    def delete_account_subscription(
        self,
        res: "bs_td.DeleteAccountSubscriptionResponseTypeDef",
    ) -> "dc_td.DeleteAccountSubscriptionResponse":
        return dc_td.DeleteAccountSubscriptionResponse.make_one(res)

    def delete_analysis(
        self,
        res: "bs_td.DeleteAnalysisResponseTypeDef",
    ) -> "dc_td.DeleteAnalysisResponse":
        return dc_td.DeleteAnalysisResponse.make_one(res)

    def delete_brand(
        self,
        res: "bs_td.DeleteBrandResponseTypeDef",
    ) -> "dc_td.DeleteBrandResponse":
        return dc_td.DeleteBrandResponse.make_one(res)

    def delete_brand_assignment(
        self,
        res: "bs_td.DeleteBrandAssignmentResponseTypeDef",
    ) -> "dc_td.DeleteBrandAssignmentResponse":
        return dc_td.DeleteBrandAssignmentResponse.make_one(res)

    def delete_custom_permissions(
        self,
        res: "bs_td.DeleteCustomPermissionsResponseTypeDef",
    ) -> "dc_td.DeleteCustomPermissionsResponse":
        return dc_td.DeleteCustomPermissionsResponse.make_one(res)

    def delete_dashboard(
        self,
        res: "bs_td.DeleteDashboardResponseTypeDef",
    ) -> "dc_td.DeleteDashboardResponse":
        return dc_td.DeleteDashboardResponse.make_one(res)

    def delete_data_set(
        self,
        res: "bs_td.DeleteDataSetResponseTypeDef",
    ) -> "dc_td.DeleteDataSetResponse":
        return dc_td.DeleteDataSetResponse.make_one(res)

    def delete_data_set_refresh_properties(
        self,
        res: "bs_td.DeleteDataSetRefreshPropertiesResponseTypeDef",
    ) -> "dc_td.DeleteDataSetRefreshPropertiesResponse":
        return dc_td.DeleteDataSetRefreshPropertiesResponse.make_one(res)

    def delete_data_source(
        self,
        res: "bs_td.DeleteDataSourceResponseTypeDef",
    ) -> "dc_td.DeleteDataSourceResponse":
        return dc_td.DeleteDataSourceResponse.make_one(res)

    def delete_default_q_business_application(
        self,
        res: "bs_td.DeleteDefaultQBusinessApplicationResponseTypeDef",
    ) -> "dc_td.DeleteDefaultQBusinessApplicationResponse":
        return dc_td.DeleteDefaultQBusinessApplicationResponse.make_one(res)

    def delete_folder(
        self,
        res: "bs_td.DeleteFolderResponseTypeDef",
    ) -> "dc_td.DeleteFolderResponse":
        return dc_td.DeleteFolderResponse.make_one(res)

    def delete_folder_membership(
        self,
        res: "bs_td.DeleteFolderMembershipResponseTypeDef",
    ) -> "dc_td.DeleteFolderMembershipResponse":
        return dc_td.DeleteFolderMembershipResponse.make_one(res)

    def delete_group(
        self,
        res: "bs_td.DeleteGroupResponseTypeDef",
    ) -> "dc_td.DeleteGroupResponse":
        return dc_td.DeleteGroupResponse.make_one(res)

    def delete_group_membership(
        self,
        res: "bs_td.DeleteGroupMembershipResponseTypeDef",
    ) -> "dc_td.DeleteGroupMembershipResponse":
        return dc_td.DeleteGroupMembershipResponse.make_one(res)

    def delete_iam_policy_assignment(
        self,
        res: "bs_td.DeleteIAMPolicyAssignmentResponseTypeDef",
    ) -> "dc_td.DeleteIAMPolicyAssignmentResponse":
        return dc_td.DeleteIAMPolicyAssignmentResponse.make_one(res)

    def delete_identity_propagation_config(
        self,
        res: "bs_td.DeleteIdentityPropagationConfigResponseTypeDef",
    ) -> "dc_td.DeleteIdentityPropagationConfigResponse":
        return dc_td.DeleteIdentityPropagationConfigResponse.make_one(res)

    def delete_namespace(
        self,
        res: "bs_td.DeleteNamespaceResponseTypeDef",
    ) -> "dc_td.DeleteNamespaceResponse":
        return dc_td.DeleteNamespaceResponse.make_one(res)

    def delete_refresh_schedule(
        self,
        res: "bs_td.DeleteRefreshScheduleResponseTypeDef",
    ) -> "dc_td.DeleteRefreshScheduleResponse":
        return dc_td.DeleteRefreshScheduleResponse.make_one(res)

    def delete_role_custom_permission(
        self,
        res: "bs_td.DeleteRoleCustomPermissionResponseTypeDef",
    ) -> "dc_td.DeleteRoleCustomPermissionResponse":
        return dc_td.DeleteRoleCustomPermissionResponse.make_one(res)

    def delete_role_membership(
        self,
        res: "bs_td.DeleteRoleMembershipResponseTypeDef",
    ) -> "dc_td.DeleteRoleMembershipResponse":
        return dc_td.DeleteRoleMembershipResponse.make_one(res)

    def delete_template(
        self,
        res: "bs_td.DeleteTemplateResponseTypeDef",
    ) -> "dc_td.DeleteTemplateResponse":
        return dc_td.DeleteTemplateResponse.make_one(res)

    def delete_template_alias(
        self,
        res: "bs_td.DeleteTemplateAliasResponseTypeDef",
    ) -> "dc_td.DeleteTemplateAliasResponse":
        return dc_td.DeleteTemplateAliasResponse.make_one(res)

    def delete_theme(
        self,
        res: "bs_td.DeleteThemeResponseTypeDef",
    ) -> "dc_td.DeleteThemeResponse":
        return dc_td.DeleteThemeResponse.make_one(res)

    def delete_theme_alias(
        self,
        res: "bs_td.DeleteThemeAliasResponseTypeDef",
    ) -> "dc_td.DeleteThemeAliasResponse":
        return dc_td.DeleteThemeAliasResponse.make_one(res)

    def delete_topic(
        self,
        res: "bs_td.DeleteTopicResponseTypeDef",
    ) -> "dc_td.DeleteTopicResponse":
        return dc_td.DeleteTopicResponse.make_one(res)

    def delete_topic_refresh_schedule(
        self,
        res: "bs_td.DeleteTopicRefreshScheduleResponseTypeDef",
    ) -> "dc_td.DeleteTopicRefreshScheduleResponse":
        return dc_td.DeleteTopicRefreshScheduleResponse.make_one(res)

    def delete_user(
        self,
        res: "bs_td.DeleteUserResponseTypeDef",
    ) -> "dc_td.DeleteUserResponse":
        return dc_td.DeleteUserResponse.make_one(res)

    def delete_user_by_principal_id(
        self,
        res: "bs_td.DeleteUserByPrincipalIdResponseTypeDef",
    ) -> "dc_td.DeleteUserByPrincipalIdResponse":
        return dc_td.DeleteUserByPrincipalIdResponse.make_one(res)

    def delete_user_custom_permission(
        self,
        res: "bs_td.DeleteUserCustomPermissionResponseTypeDef",
    ) -> "dc_td.DeleteUserCustomPermissionResponse":
        return dc_td.DeleteUserCustomPermissionResponse.make_one(res)

    def delete_vpc_connection(
        self,
        res: "bs_td.DeleteVPCConnectionResponseTypeDef",
    ) -> "dc_td.DeleteVPCConnectionResponse":
        return dc_td.DeleteVPCConnectionResponse.make_one(res)

    def describe_account_custom_permission(
        self,
        res: "bs_td.DescribeAccountCustomPermissionResponseTypeDef",
    ) -> "dc_td.DescribeAccountCustomPermissionResponse":
        return dc_td.DescribeAccountCustomPermissionResponse.make_one(res)

    def describe_account_customization(
        self,
        res: "bs_td.DescribeAccountCustomizationResponseTypeDef",
    ) -> "dc_td.DescribeAccountCustomizationResponse":
        return dc_td.DescribeAccountCustomizationResponse.make_one(res)

    def describe_account_settings(
        self,
        res: "bs_td.DescribeAccountSettingsResponseTypeDef",
    ) -> "dc_td.DescribeAccountSettingsResponse":
        return dc_td.DescribeAccountSettingsResponse.make_one(res)

    def describe_account_subscription(
        self,
        res: "bs_td.DescribeAccountSubscriptionResponseTypeDef",
    ) -> "dc_td.DescribeAccountSubscriptionResponse":
        return dc_td.DescribeAccountSubscriptionResponse.make_one(res)

    def describe_analysis(
        self,
        res: "bs_td.DescribeAnalysisResponseTypeDef",
    ) -> "dc_td.DescribeAnalysisResponse":
        return dc_td.DescribeAnalysisResponse.make_one(res)

    def describe_analysis_definition(
        self,
        res: "bs_td.DescribeAnalysisDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeAnalysisDefinitionResponse":
        return dc_td.DescribeAnalysisDefinitionResponse.make_one(res)

    def describe_analysis_permissions(
        self,
        res: "bs_td.DescribeAnalysisPermissionsResponseTypeDef",
    ) -> "dc_td.DescribeAnalysisPermissionsResponse":
        return dc_td.DescribeAnalysisPermissionsResponse.make_one(res)

    def describe_asset_bundle_export_job(
        self,
        res: "bs_td.DescribeAssetBundleExportJobResponseTypeDef",
    ) -> "dc_td.DescribeAssetBundleExportJobResponse":
        return dc_td.DescribeAssetBundleExportJobResponse.make_one(res)

    def describe_asset_bundle_import_job(
        self,
        res: "bs_td.DescribeAssetBundleImportJobResponseTypeDef",
    ) -> "dc_td.DescribeAssetBundleImportJobResponse":
        return dc_td.DescribeAssetBundleImportJobResponse.make_one(res)

    def describe_brand(
        self,
        res: "bs_td.DescribeBrandResponseTypeDef",
    ) -> "dc_td.DescribeBrandResponse":
        return dc_td.DescribeBrandResponse.make_one(res)

    def describe_brand_assignment(
        self,
        res: "bs_td.DescribeBrandAssignmentResponseTypeDef",
    ) -> "dc_td.DescribeBrandAssignmentResponse":
        return dc_td.DescribeBrandAssignmentResponse.make_one(res)

    def describe_brand_published_version(
        self,
        res: "bs_td.DescribeBrandPublishedVersionResponseTypeDef",
    ) -> "dc_td.DescribeBrandPublishedVersionResponse":
        return dc_td.DescribeBrandPublishedVersionResponse.make_one(res)

    def describe_custom_permissions(
        self,
        res: "bs_td.DescribeCustomPermissionsResponseTypeDef",
    ) -> "dc_td.DescribeCustomPermissionsResponse":
        return dc_td.DescribeCustomPermissionsResponse.make_one(res)

    def describe_dashboard(
        self,
        res: "bs_td.DescribeDashboardResponseTypeDef",
    ) -> "dc_td.DescribeDashboardResponse":
        return dc_td.DescribeDashboardResponse.make_one(res)

    def describe_dashboard_definition(
        self,
        res: "bs_td.DescribeDashboardDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeDashboardDefinitionResponse":
        return dc_td.DescribeDashboardDefinitionResponse.make_one(res)

    def describe_dashboard_permissions(
        self,
        res: "bs_td.DescribeDashboardPermissionsResponseTypeDef",
    ) -> "dc_td.DescribeDashboardPermissionsResponse":
        return dc_td.DescribeDashboardPermissionsResponse.make_one(res)

    def describe_dashboard_snapshot_job(
        self,
        res: "bs_td.DescribeDashboardSnapshotJobResponseTypeDef",
    ) -> "dc_td.DescribeDashboardSnapshotJobResponse":
        return dc_td.DescribeDashboardSnapshotJobResponse.make_one(res)

    def describe_dashboard_snapshot_job_result(
        self,
        res: "bs_td.DescribeDashboardSnapshotJobResultResponseTypeDef",
    ) -> "dc_td.DescribeDashboardSnapshotJobResultResponse":
        return dc_td.DescribeDashboardSnapshotJobResultResponse.make_one(res)

    def describe_dashboards_qa_configuration(
        self,
        res: "bs_td.DescribeDashboardsQAConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeDashboardsQAConfigurationResponse":
        return dc_td.DescribeDashboardsQAConfigurationResponse.make_one(res)

    def describe_data_set(
        self,
        res: "bs_td.DescribeDataSetResponseTypeDef",
    ) -> "dc_td.DescribeDataSetResponse":
        return dc_td.DescribeDataSetResponse.make_one(res)

    def describe_data_set_permissions(
        self,
        res: "bs_td.DescribeDataSetPermissionsResponseTypeDef",
    ) -> "dc_td.DescribeDataSetPermissionsResponse":
        return dc_td.DescribeDataSetPermissionsResponse.make_one(res)

    def describe_data_set_refresh_properties(
        self,
        res: "bs_td.DescribeDataSetRefreshPropertiesResponseTypeDef",
    ) -> "dc_td.DescribeDataSetRefreshPropertiesResponse":
        return dc_td.DescribeDataSetRefreshPropertiesResponse.make_one(res)

    def describe_data_source(
        self,
        res: "bs_td.DescribeDataSourceResponseTypeDef",
    ) -> "dc_td.DescribeDataSourceResponse":
        return dc_td.DescribeDataSourceResponse.make_one(res)

    def describe_data_source_permissions(
        self,
        res: "bs_td.DescribeDataSourcePermissionsResponseTypeDef",
    ) -> "dc_td.DescribeDataSourcePermissionsResponse":
        return dc_td.DescribeDataSourcePermissionsResponse.make_one(res)

    def describe_default_q_business_application(
        self,
        res: "bs_td.DescribeDefaultQBusinessApplicationResponseTypeDef",
    ) -> "dc_td.DescribeDefaultQBusinessApplicationResponse":
        return dc_td.DescribeDefaultQBusinessApplicationResponse.make_one(res)

    def describe_folder(
        self,
        res: "bs_td.DescribeFolderResponseTypeDef",
    ) -> "dc_td.DescribeFolderResponse":
        return dc_td.DescribeFolderResponse.make_one(res)

    def describe_folder_permissions(
        self,
        res: "bs_td.DescribeFolderPermissionsResponseTypeDef",
    ) -> "dc_td.DescribeFolderPermissionsResponse":
        return dc_td.DescribeFolderPermissionsResponse.make_one(res)

    def describe_folder_resolved_permissions(
        self,
        res: "bs_td.DescribeFolderResolvedPermissionsResponseTypeDef",
    ) -> "dc_td.DescribeFolderResolvedPermissionsResponse":
        return dc_td.DescribeFolderResolvedPermissionsResponse.make_one(res)

    def describe_group(
        self,
        res: "bs_td.DescribeGroupResponseTypeDef",
    ) -> "dc_td.DescribeGroupResponse":
        return dc_td.DescribeGroupResponse.make_one(res)

    def describe_group_membership(
        self,
        res: "bs_td.DescribeGroupMembershipResponseTypeDef",
    ) -> "dc_td.DescribeGroupMembershipResponse":
        return dc_td.DescribeGroupMembershipResponse.make_one(res)

    def describe_iam_policy_assignment(
        self,
        res: "bs_td.DescribeIAMPolicyAssignmentResponseTypeDef",
    ) -> "dc_td.DescribeIAMPolicyAssignmentResponse":
        return dc_td.DescribeIAMPolicyAssignmentResponse.make_one(res)

    def describe_ingestion(
        self,
        res: "bs_td.DescribeIngestionResponseTypeDef",
    ) -> "dc_td.DescribeIngestionResponse":
        return dc_td.DescribeIngestionResponse.make_one(res)

    def describe_ip_restriction(
        self,
        res: "bs_td.DescribeIpRestrictionResponseTypeDef",
    ) -> "dc_td.DescribeIpRestrictionResponse":
        return dc_td.DescribeIpRestrictionResponse.make_one(res)

    def describe_key_registration(
        self,
        res: "bs_td.DescribeKeyRegistrationResponseTypeDef",
    ) -> "dc_td.DescribeKeyRegistrationResponse":
        return dc_td.DescribeKeyRegistrationResponse.make_one(res)

    def describe_namespace(
        self,
        res: "bs_td.DescribeNamespaceResponseTypeDef",
    ) -> "dc_td.DescribeNamespaceResponse":
        return dc_td.DescribeNamespaceResponse.make_one(res)

    def describe_q_personalization_configuration(
        self,
        res: "bs_td.DescribeQPersonalizationConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeQPersonalizationConfigurationResponse":
        return dc_td.DescribeQPersonalizationConfigurationResponse.make_one(res)

    def describe_quick_sight_q_search_configuration(
        self,
        res: "bs_td.DescribeQuickSightQSearchConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeQuickSightQSearchConfigurationResponse":
        return dc_td.DescribeQuickSightQSearchConfigurationResponse.make_one(res)

    def describe_refresh_schedule(
        self,
        res: "bs_td.DescribeRefreshScheduleResponseTypeDef",
    ) -> "dc_td.DescribeRefreshScheduleResponse":
        return dc_td.DescribeRefreshScheduleResponse.make_one(res)

    def describe_role_custom_permission(
        self,
        res: "bs_td.DescribeRoleCustomPermissionResponseTypeDef",
    ) -> "dc_td.DescribeRoleCustomPermissionResponse":
        return dc_td.DescribeRoleCustomPermissionResponse.make_one(res)

    def describe_template(
        self,
        res: "bs_td.DescribeTemplateResponseTypeDef",
    ) -> "dc_td.DescribeTemplateResponse":
        return dc_td.DescribeTemplateResponse.make_one(res)

    def describe_template_alias(
        self,
        res: "bs_td.DescribeTemplateAliasResponseTypeDef",
    ) -> "dc_td.DescribeTemplateAliasResponse":
        return dc_td.DescribeTemplateAliasResponse.make_one(res)

    def describe_template_definition(
        self,
        res: "bs_td.DescribeTemplateDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeTemplateDefinitionResponse":
        return dc_td.DescribeTemplateDefinitionResponse.make_one(res)

    def describe_template_permissions(
        self,
        res: "bs_td.DescribeTemplatePermissionsResponseTypeDef",
    ) -> "dc_td.DescribeTemplatePermissionsResponse":
        return dc_td.DescribeTemplatePermissionsResponse.make_one(res)

    def describe_theme(
        self,
        res: "bs_td.DescribeThemeResponseTypeDef",
    ) -> "dc_td.DescribeThemeResponse":
        return dc_td.DescribeThemeResponse.make_one(res)

    def describe_theme_alias(
        self,
        res: "bs_td.DescribeThemeAliasResponseTypeDef",
    ) -> "dc_td.DescribeThemeAliasResponse":
        return dc_td.DescribeThemeAliasResponse.make_one(res)

    def describe_theme_permissions(
        self,
        res: "bs_td.DescribeThemePermissionsResponseTypeDef",
    ) -> "dc_td.DescribeThemePermissionsResponse":
        return dc_td.DescribeThemePermissionsResponse.make_one(res)

    def describe_topic(
        self,
        res: "bs_td.DescribeTopicResponseTypeDef",
    ) -> "dc_td.DescribeTopicResponse":
        return dc_td.DescribeTopicResponse.make_one(res)

    def describe_topic_permissions(
        self,
        res: "bs_td.DescribeTopicPermissionsResponseTypeDef",
    ) -> "dc_td.DescribeTopicPermissionsResponse":
        return dc_td.DescribeTopicPermissionsResponse.make_one(res)

    def describe_topic_refresh(
        self,
        res: "bs_td.DescribeTopicRefreshResponseTypeDef",
    ) -> "dc_td.DescribeTopicRefreshResponse":
        return dc_td.DescribeTopicRefreshResponse.make_one(res)

    def describe_topic_refresh_schedule(
        self,
        res: "bs_td.DescribeTopicRefreshScheduleResponseTypeDef",
    ) -> "dc_td.DescribeTopicRefreshScheduleResponse":
        return dc_td.DescribeTopicRefreshScheduleResponse.make_one(res)

    def describe_user(
        self,
        res: "bs_td.DescribeUserResponseTypeDef",
    ) -> "dc_td.DescribeUserResponse":
        return dc_td.DescribeUserResponse.make_one(res)

    def describe_vpc_connection(
        self,
        res: "bs_td.DescribeVPCConnectionResponseTypeDef",
    ) -> "dc_td.DescribeVPCConnectionResponse":
        return dc_td.DescribeVPCConnectionResponse.make_one(res)

    def generate_embed_url_for_anonymous_user(
        self,
        res: "bs_td.GenerateEmbedUrlForAnonymousUserResponseTypeDef",
    ) -> "dc_td.GenerateEmbedUrlForAnonymousUserResponse":
        return dc_td.GenerateEmbedUrlForAnonymousUserResponse.make_one(res)

    def generate_embed_url_for_registered_user(
        self,
        res: "bs_td.GenerateEmbedUrlForRegisteredUserResponseTypeDef",
    ) -> "dc_td.GenerateEmbedUrlForRegisteredUserResponse":
        return dc_td.GenerateEmbedUrlForRegisteredUserResponse.make_one(res)

    def generate_embed_url_for_registered_user_with_identity(
        self,
        res: "bs_td.GenerateEmbedUrlForRegisteredUserWithIdentityResponseTypeDef",
    ) -> "dc_td.GenerateEmbedUrlForRegisteredUserWithIdentityResponse":
        return dc_td.GenerateEmbedUrlForRegisteredUserWithIdentityResponse.make_one(res)

    def get_dashboard_embed_url(
        self,
        res: "bs_td.GetDashboardEmbedUrlResponseTypeDef",
    ) -> "dc_td.GetDashboardEmbedUrlResponse":
        return dc_td.GetDashboardEmbedUrlResponse.make_one(res)

    def get_session_embed_url(
        self,
        res: "bs_td.GetSessionEmbedUrlResponseTypeDef",
    ) -> "dc_td.GetSessionEmbedUrlResponse":
        return dc_td.GetSessionEmbedUrlResponse.make_one(res)

    def list_analyses(
        self,
        res: "bs_td.ListAnalysesResponseTypeDef",
    ) -> "dc_td.ListAnalysesResponse":
        return dc_td.ListAnalysesResponse.make_one(res)

    def list_asset_bundle_export_jobs(
        self,
        res: "bs_td.ListAssetBundleExportJobsResponseTypeDef",
    ) -> "dc_td.ListAssetBundleExportJobsResponse":
        return dc_td.ListAssetBundleExportJobsResponse.make_one(res)

    def list_asset_bundle_import_jobs(
        self,
        res: "bs_td.ListAssetBundleImportJobsResponseTypeDef",
    ) -> "dc_td.ListAssetBundleImportJobsResponse":
        return dc_td.ListAssetBundleImportJobsResponse.make_one(res)

    def list_brands(
        self,
        res: "bs_td.ListBrandsResponseTypeDef",
    ) -> "dc_td.ListBrandsResponse":
        return dc_td.ListBrandsResponse.make_one(res)

    def list_custom_permissions(
        self,
        res: "bs_td.ListCustomPermissionsResponseTypeDef",
    ) -> "dc_td.ListCustomPermissionsResponse":
        return dc_td.ListCustomPermissionsResponse.make_one(res)

    def list_dashboard_versions(
        self,
        res: "bs_td.ListDashboardVersionsResponseTypeDef",
    ) -> "dc_td.ListDashboardVersionsResponse":
        return dc_td.ListDashboardVersionsResponse.make_one(res)

    def list_dashboards(
        self,
        res: "bs_td.ListDashboardsResponseTypeDef",
    ) -> "dc_td.ListDashboardsResponse":
        return dc_td.ListDashboardsResponse.make_one(res)

    def list_data_sets(
        self,
        res: "bs_td.ListDataSetsResponseTypeDef",
    ) -> "dc_td.ListDataSetsResponse":
        return dc_td.ListDataSetsResponse.make_one(res)

    def list_data_sources(
        self,
        res: "bs_td.ListDataSourcesResponseTypeDef",
    ) -> "dc_td.ListDataSourcesResponse":
        return dc_td.ListDataSourcesResponse.make_one(res)

    def list_folder_members(
        self,
        res: "bs_td.ListFolderMembersResponseTypeDef",
    ) -> "dc_td.ListFolderMembersResponse":
        return dc_td.ListFolderMembersResponse.make_one(res)

    def list_folders(
        self,
        res: "bs_td.ListFoldersResponseTypeDef",
    ) -> "dc_td.ListFoldersResponse":
        return dc_td.ListFoldersResponse.make_one(res)

    def list_folders_for_resource(
        self,
        res: "bs_td.ListFoldersForResourceResponseTypeDef",
    ) -> "dc_td.ListFoldersForResourceResponse":
        return dc_td.ListFoldersForResourceResponse.make_one(res)

    def list_group_memberships(
        self,
        res: "bs_td.ListGroupMembershipsResponseTypeDef",
    ) -> "dc_td.ListGroupMembershipsResponse":
        return dc_td.ListGroupMembershipsResponse.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsResponseTypeDef",
    ) -> "dc_td.ListGroupsResponse":
        return dc_td.ListGroupsResponse.make_one(res)

    def list_iam_policy_assignments(
        self,
        res: "bs_td.ListIAMPolicyAssignmentsResponseTypeDef",
    ) -> "dc_td.ListIAMPolicyAssignmentsResponse":
        return dc_td.ListIAMPolicyAssignmentsResponse.make_one(res)

    def list_iam_policy_assignments_for_user(
        self,
        res: "bs_td.ListIAMPolicyAssignmentsForUserResponseTypeDef",
    ) -> "dc_td.ListIAMPolicyAssignmentsForUserResponse":
        return dc_td.ListIAMPolicyAssignmentsForUserResponse.make_one(res)

    def list_identity_propagation_configs(
        self,
        res: "bs_td.ListIdentityPropagationConfigsResponseTypeDef",
    ) -> "dc_td.ListIdentityPropagationConfigsResponse":
        return dc_td.ListIdentityPropagationConfigsResponse.make_one(res)

    def list_ingestions(
        self,
        res: "bs_td.ListIngestionsResponseTypeDef",
    ) -> "dc_td.ListIngestionsResponse":
        return dc_td.ListIngestionsResponse.make_one(res)

    def list_namespaces(
        self,
        res: "bs_td.ListNamespacesResponseTypeDef",
    ) -> "dc_td.ListNamespacesResponse":
        return dc_td.ListNamespacesResponse.make_one(res)

    def list_refresh_schedules(
        self,
        res: "bs_td.ListRefreshSchedulesResponseTypeDef",
    ) -> "dc_td.ListRefreshSchedulesResponse":
        return dc_td.ListRefreshSchedulesResponse.make_one(res)

    def list_role_memberships(
        self,
        res: "bs_td.ListRoleMembershipsResponseTypeDef",
    ) -> "dc_td.ListRoleMembershipsResponse":
        return dc_td.ListRoleMembershipsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_template_aliases(
        self,
        res: "bs_td.ListTemplateAliasesResponseTypeDef",
    ) -> "dc_td.ListTemplateAliasesResponse":
        return dc_td.ListTemplateAliasesResponse.make_one(res)

    def list_template_versions(
        self,
        res: "bs_td.ListTemplateVersionsResponseTypeDef",
    ) -> "dc_td.ListTemplateVersionsResponse":
        return dc_td.ListTemplateVersionsResponse.make_one(res)

    def list_templates(
        self,
        res: "bs_td.ListTemplatesResponseTypeDef",
    ) -> "dc_td.ListTemplatesResponse":
        return dc_td.ListTemplatesResponse.make_one(res)

    def list_theme_aliases(
        self,
        res: "bs_td.ListThemeAliasesResponseTypeDef",
    ) -> "dc_td.ListThemeAliasesResponse":
        return dc_td.ListThemeAliasesResponse.make_one(res)

    def list_theme_versions(
        self,
        res: "bs_td.ListThemeVersionsResponseTypeDef",
    ) -> "dc_td.ListThemeVersionsResponse":
        return dc_td.ListThemeVersionsResponse.make_one(res)

    def list_themes(
        self,
        res: "bs_td.ListThemesResponseTypeDef",
    ) -> "dc_td.ListThemesResponse":
        return dc_td.ListThemesResponse.make_one(res)

    def list_topic_refresh_schedules(
        self,
        res: "bs_td.ListTopicRefreshSchedulesResponseTypeDef",
    ) -> "dc_td.ListTopicRefreshSchedulesResponse":
        return dc_td.ListTopicRefreshSchedulesResponse.make_one(res)

    def list_topic_reviewed_answers(
        self,
        res: "bs_td.ListTopicReviewedAnswersResponseTypeDef",
    ) -> "dc_td.ListTopicReviewedAnswersResponse":
        return dc_td.ListTopicReviewedAnswersResponse.make_one(res)

    def list_topics(
        self,
        res: "bs_td.ListTopicsResponseTypeDef",
    ) -> "dc_td.ListTopicsResponse":
        return dc_td.ListTopicsResponse.make_one(res)

    def list_user_groups(
        self,
        res: "bs_td.ListUserGroupsResponseTypeDef",
    ) -> "dc_td.ListUserGroupsResponse":
        return dc_td.ListUserGroupsResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def list_vpc_connections(
        self,
        res: "bs_td.ListVPCConnectionsResponseTypeDef",
    ) -> "dc_td.ListVPCConnectionsResponse":
        return dc_td.ListVPCConnectionsResponse.make_one(res)

    def predict_qa_results(
        self,
        res: "bs_td.PredictQAResultsResponseTypeDef",
    ) -> "dc_td.PredictQAResultsResponse":
        return dc_td.PredictQAResultsResponse.make_one(res)

    def put_data_set_refresh_properties(
        self,
        res: "bs_td.PutDataSetRefreshPropertiesResponseTypeDef",
    ) -> "dc_td.PutDataSetRefreshPropertiesResponse":
        return dc_td.PutDataSetRefreshPropertiesResponse.make_one(res)

    def register_user(
        self,
        res: "bs_td.RegisterUserResponseTypeDef",
    ) -> "dc_td.RegisterUserResponse":
        return dc_td.RegisterUserResponse.make_one(res)

    def restore_analysis(
        self,
        res: "bs_td.RestoreAnalysisResponseTypeDef",
    ) -> "dc_td.RestoreAnalysisResponse":
        return dc_td.RestoreAnalysisResponse.make_one(res)

    def search_analyses(
        self,
        res: "bs_td.SearchAnalysesResponseTypeDef",
    ) -> "dc_td.SearchAnalysesResponse":
        return dc_td.SearchAnalysesResponse.make_one(res)

    def search_dashboards(
        self,
        res: "bs_td.SearchDashboardsResponseTypeDef",
    ) -> "dc_td.SearchDashboardsResponse":
        return dc_td.SearchDashboardsResponse.make_one(res)

    def search_data_sets(
        self,
        res: "bs_td.SearchDataSetsResponseTypeDef",
    ) -> "dc_td.SearchDataSetsResponse":
        return dc_td.SearchDataSetsResponse.make_one(res)

    def search_data_sources(
        self,
        res: "bs_td.SearchDataSourcesResponseTypeDef",
    ) -> "dc_td.SearchDataSourcesResponse":
        return dc_td.SearchDataSourcesResponse.make_one(res)

    def search_folders(
        self,
        res: "bs_td.SearchFoldersResponseTypeDef",
    ) -> "dc_td.SearchFoldersResponse":
        return dc_td.SearchFoldersResponse.make_one(res)

    def search_groups(
        self,
        res: "bs_td.SearchGroupsResponseTypeDef",
    ) -> "dc_td.SearchGroupsResponse":
        return dc_td.SearchGroupsResponse.make_one(res)

    def search_topics(
        self,
        res: "bs_td.SearchTopicsResponseTypeDef",
    ) -> "dc_td.SearchTopicsResponse":
        return dc_td.SearchTopicsResponse.make_one(res)

    def start_asset_bundle_export_job(
        self,
        res: "bs_td.StartAssetBundleExportJobResponseTypeDef",
    ) -> "dc_td.StartAssetBundleExportJobResponse":
        return dc_td.StartAssetBundleExportJobResponse.make_one(res)

    def start_asset_bundle_import_job(
        self,
        res: "bs_td.StartAssetBundleImportJobResponseTypeDef",
    ) -> "dc_td.StartAssetBundleImportJobResponse":
        return dc_td.StartAssetBundleImportJobResponse.make_one(res)

    def start_dashboard_snapshot_job(
        self,
        res: "bs_td.StartDashboardSnapshotJobResponseTypeDef",
    ) -> "dc_td.StartDashboardSnapshotJobResponse":
        return dc_td.StartDashboardSnapshotJobResponse.make_one(res)

    def start_dashboard_snapshot_job_schedule(
        self,
        res: "bs_td.StartDashboardSnapshotJobScheduleResponseTypeDef",
    ) -> "dc_td.StartDashboardSnapshotJobScheduleResponse":
        return dc_td.StartDashboardSnapshotJobScheduleResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.TagResourceResponseTypeDef",
    ) -> "dc_td.TagResourceResponse":
        return dc_td.TagResourceResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.UntagResourceResponseTypeDef",
    ) -> "dc_td.UntagResourceResponse":
        return dc_td.UntagResourceResponse.make_one(res)

    def update_account_custom_permission(
        self,
        res: "bs_td.UpdateAccountCustomPermissionResponseTypeDef",
    ) -> "dc_td.UpdateAccountCustomPermissionResponse":
        return dc_td.UpdateAccountCustomPermissionResponse.make_one(res)

    def update_account_customization(
        self,
        res: "bs_td.UpdateAccountCustomizationResponseTypeDef",
    ) -> "dc_td.UpdateAccountCustomizationResponse":
        return dc_td.UpdateAccountCustomizationResponse.make_one(res)

    def update_account_settings(
        self,
        res: "bs_td.UpdateAccountSettingsResponseTypeDef",
    ) -> "dc_td.UpdateAccountSettingsResponse":
        return dc_td.UpdateAccountSettingsResponse.make_one(res)

    def update_analysis(
        self,
        res: "bs_td.UpdateAnalysisResponseTypeDef",
    ) -> "dc_td.UpdateAnalysisResponse":
        return dc_td.UpdateAnalysisResponse.make_one(res)

    def update_analysis_permissions(
        self,
        res: "bs_td.UpdateAnalysisPermissionsResponseTypeDef",
    ) -> "dc_td.UpdateAnalysisPermissionsResponse":
        return dc_td.UpdateAnalysisPermissionsResponse.make_one(res)

    def update_application_with_token_exchange_grant(
        self,
        res: "bs_td.UpdateApplicationWithTokenExchangeGrantResponseTypeDef",
    ) -> "dc_td.UpdateApplicationWithTokenExchangeGrantResponse":
        return dc_td.UpdateApplicationWithTokenExchangeGrantResponse.make_one(res)

    def update_brand(
        self,
        res: "bs_td.UpdateBrandResponseTypeDef",
    ) -> "dc_td.UpdateBrandResponse":
        return dc_td.UpdateBrandResponse.make_one(res)

    def update_brand_assignment(
        self,
        res: "bs_td.UpdateBrandAssignmentResponseTypeDef",
    ) -> "dc_td.UpdateBrandAssignmentResponse":
        return dc_td.UpdateBrandAssignmentResponse.make_one(res)

    def update_brand_published_version(
        self,
        res: "bs_td.UpdateBrandPublishedVersionResponseTypeDef",
    ) -> "dc_td.UpdateBrandPublishedVersionResponse":
        return dc_td.UpdateBrandPublishedVersionResponse.make_one(res)

    def update_custom_permissions(
        self,
        res: "bs_td.UpdateCustomPermissionsResponseTypeDef",
    ) -> "dc_td.UpdateCustomPermissionsResponse":
        return dc_td.UpdateCustomPermissionsResponse.make_one(res)

    def update_dashboard(
        self,
        res: "bs_td.UpdateDashboardResponseTypeDef",
    ) -> "dc_td.UpdateDashboardResponse":
        return dc_td.UpdateDashboardResponse.make_one(res)

    def update_dashboard_links(
        self,
        res: "bs_td.UpdateDashboardLinksResponseTypeDef",
    ) -> "dc_td.UpdateDashboardLinksResponse":
        return dc_td.UpdateDashboardLinksResponse.make_one(res)

    def update_dashboard_permissions(
        self,
        res: "bs_td.UpdateDashboardPermissionsResponseTypeDef",
    ) -> "dc_td.UpdateDashboardPermissionsResponse":
        return dc_td.UpdateDashboardPermissionsResponse.make_one(res)

    def update_dashboard_published_version(
        self,
        res: "bs_td.UpdateDashboardPublishedVersionResponseTypeDef",
    ) -> "dc_td.UpdateDashboardPublishedVersionResponse":
        return dc_td.UpdateDashboardPublishedVersionResponse.make_one(res)

    def update_dashboards_qa_configuration(
        self,
        res: "bs_td.UpdateDashboardsQAConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateDashboardsQAConfigurationResponse":
        return dc_td.UpdateDashboardsQAConfigurationResponse.make_one(res)

    def update_data_set(
        self,
        res: "bs_td.UpdateDataSetResponseTypeDef",
    ) -> "dc_td.UpdateDataSetResponse":
        return dc_td.UpdateDataSetResponse.make_one(res)

    def update_data_set_permissions(
        self,
        res: "bs_td.UpdateDataSetPermissionsResponseTypeDef",
    ) -> "dc_td.UpdateDataSetPermissionsResponse":
        return dc_td.UpdateDataSetPermissionsResponse.make_one(res)

    def update_data_source(
        self,
        res: "bs_td.UpdateDataSourceResponseTypeDef",
    ) -> "dc_td.UpdateDataSourceResponse":
        return dc_td.UpdateDataSourceResponse.make_one(res)

    def update_data_source_permissions(
        self,
        res: "bs_td.UpdateDataSourcePermissionsResponseTypeDef",
    ) -> "dc_td.UpdateDataSourcePermissionsResponse":
        return dc_td.UpdateDataSourcePermissionsResponse.make_one(res)

    def update_default_q_business_application(
        self,
        res: "bs_td.UpdateDefaultQBusinessApplicationResponseTypeDef",
    ) -> "dc_td.UpdateDefaultQBusinessApplicationResponse":
        return dc_td.UpdateDefaultQBusinessApplicationResponse.make_one(res)

    def update_folder(
        self,
        res: "bs_td.UpdateFolderResponseTypeDef",
    ) -> "dc_td.UpdateFolderResponse":
        return dc_td.UpdateFolderResponse.make_one(res)

    def update_folder_permissions(
        self,
        res: "bs_td.UpdateFolderPermissionsResponseTypeDef",
    ) -> "dc_td.UpdateFolderPermissionsResponse":
        return dc_td.UpdateFolderPermissionsResponse.make_one(res)

    def update_group(
        self,
        res: "bs_td.UpdateGroupResponseTypeDef",
    ) -> "dc_td.UpdateGroupResponse":
        return dc_td.UpdateGroupResponse.make_one(res)

    def update_iam_policy_assignment(
        self,
        res: "bs_td.UpdateIAMPolicyAssignmentResponseTypeDef",
    ) -> "dc_td.UpdateIAMPolicyAssignmentResponse":
        return dc_td.UpdateIAMPolicyAssignmentResponse.make_one(res)

    def update_identity_propagation_config(
        self,
        res: "bs_td.UpdateIdentityPropagationConfigResponseTypeDef",
    ) -> "dc_td.UpdateIdentityPropagationConfigResponse":
        return dc_td.UpdateIdentityPropagationConfigResponse.make_one(res)

    def update_ip_restriction(
        self,
        res: "bs_td.UpdateIpRestrictionResponseTypeDef",
    ) -> "dc_td.UpdateIpRestrictionResponse":
        return dc_td.UpdateIpRestrictionResponse.make_one(res)

    def update_key_registration(
        self,
        res: "bs_td.UpdateKeyRegistrationResponseTypeDef",
    ) -> "dc_td.UpdateKeyRegistrationResponse":
        return dc_td.UpdateKeyRegistrationResponse.make_one(res)

    def update_public_sharing_settings(
        self,
        res: "bs_td.UpdatePublicSharingSettingsResponseTypeDef",
    ) -> "dc_td.UpdatePublicSharingSettingsResponse":
        return dc_td.UpdatePublicSharingSettingsResponse.make_one(res)

    def update_q_personalization_configuration(
        self,
        res: "bs_td.UpdateQPersonalizationConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateQPersonalizationConfigurationResponse":
        return dc_td.UpdateQPersonalizationConfigurationResponse.make_one(res)

    def update_quick_sight_q_search_configuration(
        self,
        res: "bs_td.UpdateQuickSightQSearchConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateQuickSightQSearchConfigurationResponse":
        return dc_td.UpdateQuickSightQSearchConfigurationResponse.make_one(res)

    def update_refresh_schedule(
        self,
        res: "bs_td.UpdateRefreshScheduleResponseTypeDef",
    ) -> "dc_td.UpdateRefreshScheduleResponse":
        return dc_td.UpdateRefreshScheduleResponse.make_one(res)

    def update_role_custom_permission(
        self,
        res: "bs_td.UpdateRoleCustomPermissionResponseTypeDef",
    ) -> "dc_td.UpdateRoleCustomPermissionResponse":
        return dc_td.UpdateRoleCustomPermissionResponse.make_one(res)

    def update_spice_capacity_configuration(
        self,
        res: "bs_td.UpdateSPICECapacityConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateSPICECapacityConfigurationResponse":
        return dc_td.UpdateSPICECapacityConfigurationResponse.make_one(res)

    def update_template(
        self,
        res: "bs_td.UpdateTemplateResponseTypeDef",
    ) -> "dc_td.UpdateTemplateResponse":
        return dc_td.UpdateTemplateResponse.make_one(res)

    def update_template_alias(
        self,
        res: "bs_td.UpdateTemplateAliasResponseTypeDef",
    ) -> "dc_td.UpdateTemplateAliasResponse":
        return dc_td.UpdateTemplateAliasResponse.make_one(res)

    def update_template_permissions(
        self,
        res: "bs_td.UpdateTemplatePermissionsResponseTypeDef",
    ) -> "dc_td.UpdateTemplatePermissionsResponse":
        return dc_td.UpdateTemplatePermissionsResponse.make_one(res)

    def update_theme(
        self,
        res: "bs_td.UpdateThemeResponseTypeDef",
    ) -> "dc_td.UpdateThemeResponse":
        return dc_td.UpdateThemeResponse.make_one(res)

    def update_theme_alias(
        self,
        res: "bs_td.UpdateThemeAliasResponseTypeDef",
    ) -> "dc_td.UpdateThemeAliasResponse":
        return dc_td.UpdateThemeAliasResponse.make_one(res)

    def update_theme_permissions(
        self,
        res: "bs_td.UpdateThemePermissionsResponseTypeDef",
    ) -> "dc_td.UpdateThemePermissionsResponse":
        return dc_td.UpdateThemePermissionsResponse.make_one(res)

    def update_topic(
        self,
        res: "bs_td.UpdateTopicResponseTypeDef",
    ) -> "dc_td.UpdateTopicResponse":
        return dc_td.UpdateTopicResponse.make_one(res)

    def update_topic_permissions(
        self,
        res: "bs_td.UpdateTopicPermissionsResponseTypeDef",
    ) -> "dc_td.UpdateTopicPermissionsResponse":
        return dc_td.UpdateTopicPermissionsResponse.make_one(res)

    def update_topic_refresh_schedule(
        self,
        res: "bs_td.UpdateTopicRefreshScheduleResponseTypeDef",
    ) -> "dc_td.UpdateTopicRefreshScheduleResponse":
        return dc_td.UpdateTopicRefreshScheduleResponse.make_one(res)

    def update_user(
        self,
        res: "bs_td.UpdateUserResponseTypeDef",
    ) -> "dc_td.UpdateUserResponse":
        return dc_td.UpdateUserResponse.make_one(res)

    def update_user_custom_permission(
        self,
        res: "bs_td.UpdateUserCustomPermissionResponseTypeDef",
    ) -> "dc_td.UpdateUserCustomPermissionResponse":
        return dc_td.UpdateUserCustomPermissionResponse.make_one(res)

    def update_vpc_connection(
        self,
        res: "bs_td.UpdateVPCConnectionResponseTypeDef",
    ) -> "dc_td.UpdateVPCConnectionResponse":
        return dc_td.UpdateVPCConnectionResponse.make_one(res)


quicksight_caster = QUICKSIGHTCaster()
