# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iot import type_defs as bs_td


class IOTCaster:

    def accept_certificate_transfer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_sbom_with_package_version(
        self,
        res: "bs_td.AssociateSbomWithPackageVersionResponseTypeDef",
    ) -> "dc_td.AssociateSbomWithPackageVersionResponse":
        return dc_td.AssociateSbomWithPackageVersionResponse.make_one(res)

    def associate_targets_with_job(
        self,
        res: "bs_td.AssociateTargetsWithJobResponseTypeDef",
    ) -> "dc_td.AssociateTargetsWithJobResponse":
        return dc_td.AssociateTargetsWithJobResponse.make_one(res)

    def attach_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def attach_principal_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def cancel_certificate_transfer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def cancel_job(
        self,
        res: "bs_td.CancelJobResponseTypeDef",
    ) -> "dc_td.CancelJobResponse":
        return dc_td.CancelJobResponse.make_one(res)

    def cancel_job_execution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_authorizer(
        self,
        res: "bs_td.CreateAuthorizerResponseTypeDef",
    ) -> "dc_td.CreateAuthorizerResponse":
        return dc_td.CreateAuthorizerResponse.make_one(res)

    def create_billing_group(
        self,
        res: "bs_td.CreateBillingGroupResponseTypeDef",
    ) -> "dc_td.CreateBillingGroupResponse":
        return dc_td.CreateBillingGroupResponse.make_one(res)

    def create_certificate_from_csr(
        self,
        res: "bs_td.CreateCertificateFromCsrResponseTypeDef",
    ) -> "dc_td.CreateCertificateFromCsrResponse":
        return dc_td.CreateCertificateFromCsrResponse.make_one(res)

    def create_certificate_provider(
        self,
        res: "bs_td.CreateCertificateProviderResponseTypeDef",
    ) -> "dc_td.CreateCertificateProviderResponse":
        return dc_td.CreateCertificateProviderResponse.make_one(res)

    def create_command(
        self,
        res: "bs_td.CreateCommandResponseTypeDef",
    ) -> "dc_td.CreateCommandResponse":
        return dc_td.CreateCommandResponse.make_one(res)

    def create_custom_metric(
        self,
        res: "bs_td.CreateCustomMetricResponseTypeDef",
    ) -> "dc_td.CreateCustomMetricResponse":
        return dc_td.CreateCustomMetricResponse.make_one(res)

    def create_dimension(
        self,
        res: "bs_td.CreateDimensionResponseTypeDef",
    ) -> "dc_td.CreateDimensionResponse":
        return dc_td.CreateDimensionResponse.make_one(res)

    def create_domain_configuration(
        self,
        res: "bs_td.CreateDomainConfigurationResponseTypeDef",
    ) -> "dc_td.CreateDomainConfigurationResponse":
        return dc_td.CreateDomainConfigurationResponse.make_one(res)

    def create_dynamic_thing_group(
        self,
        res: "bs_td.CreateDynamicThingGroupResponseTypeDef",
    ) -> "dc_td.CreateDynamicThingGroupResponse":
        return dc_td.CreateDynamicThingGroupResponse.make_one(res)

    def create_fleet_metric(
        self,
        res: "bs_td.CreateFleetMetricResponseTypeDef",
    ) -> "dc_td.CreateFleetMetricResponse":
        return dc_td.CreateFleetMetricResponse.make_one(res)

    def create_job(
        self,
        res: "bs_td.CreateJobResponseTypeDef",
    ) -> "dc_td.CreateJobResponse":
        return dc_td.CreateJobResponse.make_one(res)

    def create_job_template(
        self,
        res: "bs_td.CreateJobTemplateResponseTypeDef",
    ) -> "dc_td.CreateJobTemplateResponse":
        return dc_td.CreateJobTemplateResponse.make_one(res)

    def create_keys_and_certificate(
        self,
        res: "bs_td.CreateKeysAndCertificateResponseTypeDef",
    ) -> "dc_td.CreateKeysAndCertificateResponse":
        return dc_td.CreateKeysAndCertificateResponse.make_one(res)

    def create_mitigation_action(
        self,
        res: "bs_td.CreateMitigationActionResponseTypeDef",
    ) -> "dc_td.CreateMitigationActionResponse":
        return dc_td.CreateMitigationActionResponse.make_one(res)

    def create_ota_update(
        self,
        res: "bs_td.CreateOTAUpdateResponseTypeDef",
    ) -> "dc_td.CreateOTAUpdateResponse":
        return dc_td.CreateOTAUpdateResponse.make_one(res)

    def create_package(
        self,
        res: "bs_td.CreatePackageResponseTypeDef",
    ) -> "dc_td.CreatePackageResponse":
        return dc_td.CreatePackageResponse.make_one(res)

    def create_package_version(
        self,
        res: "bs_td.CreatePackageVersionResponseTypeDef",
    ) -> "dc_td.CreatePackageVersionResponse":
        return dc_td.CreatePackageVersionResponse.make_one(res)

    def create_policy(
        self,
        res: "bs_td.CreatePolicyResponseTypeDef",
    ) -> "dc_td.CreatePolicyResponse":
        return dc_td.CreatePolicyResponse.make_one(res)

    def create_policy_version(
        self,
        res: "bs_td.CreatePolicyVersionResponseTypeDef",
    ) -> "dc_td.CreatePolicyVersionResponse":
        return dc_td.CreatePolicyVersionResponse.make_one(res)

    def create_provisioning_claim(
        self,
        res: "bs_td.CreateProvisioningClaimResponseTypeDef",
    ) -> "dc_td.CreateProvisioningClaimResponse":
        return dc_td.CreateProvisioningClaimResponse.make_one(res)

    def create_provisioning_template(
        self,
        res: "bs_td.CreateProvisioningTemplateResponseTypeDef",
    ) -> "dc_td.CreateProvisioningTemplateResponse":
        return dc_td.CreateProvisioningTemplateResponse.make_one(res)

    def create_provisioning_template_version(
        self,
        res: "bs_td.CreateProvisioningTemplateVersionResponseTypeDef",
    ) -> "dc_td.CreateProvisioningTemplateVersionResponse":
        return dc_td.CreateProvisioningTemplateVersionResponse.make_one(res)

    def create_role_alias(
        self,
        res: "bs_td.CreateRoleAliasResponseTypeDef",
    ) -> "dc_td.CreateRoleAliasResponse":
        return dc_td.CreateRoleAliasResponse.make_one(res)

    def create_scheduled_audit(
        self,
        res: "bs_td.CreateScheduledAuditResponseTypeDef",
    ) -> "dc_td.CreateScheduledAuditResponse":
        return dc_td.CreateScheduledAuditResponse.make_one(res)

    def create_security_profile(
        self,
        res: "bs_td.CreateSecurityProfileResponseTypeDef",
    ) -> "dc_td.CreateSecurityProfileResponse":
        return dc_td.CreateSecurityProfileResponse.make_one(res)

    def create_stream(
        self,
        res: "bs_td.CreateStreamResponseTypeDef",
    ) -> "dc_td.CreateStreamResponse":
        return dc_td.CreateStreamResponse.make_one(res)

    def create_thing(
        self,
        res: "bs_td.CreateThingResponseTypeDef",
    ) -> "dc_td.CreateThingResponse":
        return dc_td.CreateThingResponse.make_one(res)

    def create_thing_group(
        self,
        res: "bs_td.CreateThingGroupResponseTypeDef",
    ) -> "dc_td.CreateThingGroupResponse":
        return dc_td.CreateThingGroupResponse.make_one(res)

    def create_thing_type(
        self,
        res: "bs_td.CreateThingTypeResponseTypeDef",
    ) -> "dc_td.CreateThingTypeResponse":
        return dc_td.CreateThingTypeResponse.make_one(res)

    def create_topic_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_topic_rule_destination(
        self,
        res: "bs_td.CreateTopicRuleDestinationResponseTypeDef",
    ) -> "dc_td.CreateTopicRuleDestinationResponse":
        return dc_td.CreateTopicRuleDestinationResponse.make_one(res)

    def delete_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_command(
        self,
        res: "bs_td.DeleteCommandResponseTypeDef",
    ) -> "dc_td.DeleteCommandResponse":
        return dc_td.DeleteCommandResponse.make_one(res)

    def delete_fleet_metric(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_job_execution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_job_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_policy_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_topic_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_v2_logging_level(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_account_audit_configuration(
        self,
        res: "bs_td.DescribeAccountAuditConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeAccountAuditConfigurationResponse":
        return dc_td.DescribeAccountAuditConfigurationResponse.make_one(res)

    def describe_audit_finding(
        self,
        res: "bs_td.DescribeAuditFindingResponseTypeDef",
    ) -> "dc_td.DescribeAuditFindingResponse":
        return dc_td.DescribeAuditFindingResponse.make_one(res)

    def describe_audit_mitigation_actions_task(
        self,
        res: "bs_td.DescribeAuditMitigationActionsTaskResponseTypeDef",
    ) -> "dc_td.DescribeAuditMitigationActionsTaskResponse":
        return dc_td.DescribeAuditMitigationActionsTaskResponse.make_one(res)

    def describe_audit_suppression(
        self,
        res: "bs_td.DescribeAuditSuppressionResponseTypeDef",
    ) -> "dc_td.DescribeAuditSuppressionResponse":
        return dc_td.DescribeAuditSuppressionResponse.make_one(res)

    def describe_audit_task(
        self,
        res: "bs_td.DescribeAuditTaskResponseTypeDef",
    ) -> "dc_td.DescribeAuditTaskResponse":
        return dc_td.DescribeAuditTaskResponse.make_one(res)

    def describe_authorizer(
        self,
        res: "bs_td.DescribeAuthorizerResponseTypeDef",
    ) -> "dc_td.DescribeAuthorizerResponse":
        return dc_td.DescribeAuthorizerResponse.make_one(res)

    def describe_billing_group(
        self,
        res: "bs_td.DescribeBillingGroupResponseTypeDef",
    ) -> "dc_td.DescribeBillingGroupResponse":
        return dc_td.DescribeBillingGroupResponse.make_one(res)

    def describe_ca_certificate(
        self,
        res: "bs_td.DescribeCACertificateResponseTypeDef",
    ) -> "dc_td.DescribeCACertificateResponse":
        return dc_td.DescribeCACertificateResponse.make_one(res)

    def describe_certificate(
        self,
        res: "bs_td.DescribeCertificateResponseTypeDef",
    ) -> "dc_td.DescribeCertificateResponse":
        return dc_td.DescribeCertificateResponse.make_one(res)

    def describe_certificate_provider(
        self,
        res: "bs_td.DescribeCertificateProviderResponseTypeDef",
    ) -> "dc_td.DescribeCertificateProviderResponse":
        return dc_td.DescribeCertificateProviderResponse.make_one(res)

    def describe_custom_metric(
        self,
        res: "bs_td.DescribeCustomMetricResponseTypeDef",
    ) -> "dc_td.DescribeCustomMetricResponse":
        return dc_td.DescribeCustomMetricResponse.make_one(res)

    def describe_default_authorizer(
        self,
        res: "bs_td.DescribeDefaultAuthorizerResponseTypeDef",
    ) -> "dc_td.DescribeDefaultAuthorizerResponse":
        return dc_td.DescribeDefaultAuthorizerResponse.make_one(res)

    def describe_detect_mitigation_actions_task(
        self,
        res: "bs_td.DescribeDetectMitigationActionsTaskResponseTypeDef",
    ) -> "dc_td.DescribeDetectMitigationActionsTaskResponse":
        return dc_td.DescribeDetectMitigationActionsTaskResponse.make_one(res)

    def describe_dimension(
        self,
        res: "bs_td.DescribeDimensionResponseTypeDef",
    ) -> "dc_td.DescribeDimensionResponse":
        return dc_td.DescribeDimensionResponse.make_one(res)

    def describe_domain_configuration(
        self,
        res: "bs_td.DescribeDomainConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeDomainConfigurationResponse":
        return dc_td.DescribeDomainConfigurationResponse.make_one(res)

    def describe_encryption_configuration(
        self,
        res: "bs_td.DescribeEncryptionConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeEncryptionConfigurationResponse":
        return dc_td.DescribeEncryptionConfigurationResponse.make_one(res)

    def describe_endpoint(
        self,
        res: "bs_td.DescribeEndpointResponseTypeDef",
    ) -> "dc_td.DescribeEndpointResponse":
        return dc_td.DescribeEndpointResponse.make_one(res)

    def describe_event_configurations(
        self,
        res: "bs_td.DescribeEventConfigurationsResponseTypeDef",
    ) -> "dc_td.DescribeEventConfigurationsResponse":
        return dc_td.DescribeEventConfigurationsResponse.make_one(res)

    def describe_fleet_metric(
        self,
        res: "bs_td.DescribeFleetMetricResponseTypeDef",
    ) -> "dc_td.DescribeFleetMetricResponse":
        return dc_td.DescribeFleetMetricResponse.make_one(res)

    def describe_index(
        self,
        res: "bs_td.DescribeIndexResponseTypeDef",
    ) -> "dc_td.DescribeIndexResponse":
        return dc_td.DescribeIndexResponse.make_one(res)

    def describe_job(
        self,
        res: "bs_td.DescribeJobResponseTypeDef",
    ) -> "dc_td.DescribeJobResponse":
        return dc_td.DescribeJobResponse.make_one(res)

    def describe_job_execution(
        self,
        res: "bs_td.DescribeJobExecutionResponseTypeDef",
    ) -> "dc_td.DescribeJobExecutionResponse":
        return dc_td.DescribeJobExecutionResponse.make_one(res)

    def describe_job_template(
        self,
        res: "bs_td.DescribeJobTemplateResponseTypeDef",
    ) -> "dc_td.DescribeJobTemplateResponse":
        return dc_td.DescribeJobTemplateResponse.make_one(res)

    def describe_managed_job_template(
        self,
        res: "bs_td.DescribeManagedJobTemplateResponseTypeDef",
    ) -> "dc_td.DescribeManagedJobTemplateResponse":
        return dc_td.DescribeManagedJobTemplateResponse.make_one(res)

    def describe_mitigation_action(
        self,
        res: "bs_td.DescribeMitigationActionResponseTypeDef",
    ) -> "dc_td.DescribeMitigationActionResponse":
        return dc_td.DescribeMitigationActionResponse.make_one(res)

    def describe_provisioning_template(
        self,
        res: "bs_td.DescribeProvisioningTemplateResponseTypeDef",
    ) -> "dc_td.DescribeProvisioningTemplateResponse":
        return dc_td.DescribeProvisioningTemplateResponse.make_one(res)

    def describe_provisioning_template_version(
        self,
        res: "bs_td.DescribeProvisioningTemplateVersionResponseTypeDef",
    ) -> "dc_td.DescribeProvisioningTemplateVersionResponse":
        return dc_td.DescribeProvisioningTemplateVersionResponse.make_one(res)

    def describe_role_alias(
        self,
        res: "bs_td.DescribeRoleAliasResponseTypeDef",
    ) -> "dc_td.DescribeRoleAliasResponse":
        return dc_td.DescribeRoleAliasResponse.make_one(res)

    def describe_scheduled_audit(
        self,
        res: "bs_td.DescribeScheduledAuditResponseTypeDef",
    ) -> "dc_td.DescribeScheduledAuditResponse":
        return dc_td.DescribeScheduledAuditResponse.make_one(res)

    def describe_security_profile(
        self,
        res: "bs_td.DescribeSecurityProfileResponseTypeDef",
    ) -> "dc_td.DescribeSecurityProfileResponse":
        return dc_td.DescribeSecurityProfileResponse.make_one(res)

    def describe_stream(
        self,
        res: "bs_td.DescribeStreamResponseTypeDef",
    ) -> "dc_td.DescribeStreamResponse":
        return dc_td.DescribeStreamResponse.make_one(res)

    def describe_thing(
        self,
        res: "bs_td.DescribeThingResponseTypeDef",
    ) -> "dc_td.DescribeThingResponse":
        return dc_td.DescribeThingResponse.make_one(res)

    def describe_thing_group(
        self,
        res: "bs_td.DescribeThingGroupResponseTypeDef",
    ) -> "dc_td.DescribeThingGroupResponse":
        return dc_td.DescribeThingGroupResponse.make_one(res)

    def describe_thing_registration_task(
        self,
        res: "bs_td.DescribeThingRegistrationTaskResponseTypeDef",
    ) -> "dc_td.DescribeThingRegistrationTaskResponse":
        return dc_td.DescribeThingRegistrationTaskResponse.make_one(res)

    def describe_thing_type(
        self,
        res: "bs_td.DescribeThingTypeResponseTypeDef",
    ) -> "dc_td.DescribeThingTypeResponse":
        return dc_td.DescribeThingTypeResponse.make_one(res)

    def detach_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def detach_principal_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_topic_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_topic_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_behavior_model_training_summaries(
        self,
        res: "bs_td.GetBehaviorModelTrainingSummariesResponseTypeDef",
    ) -> "dc_td.GetBehaviorModelTrainingSummariesResponse":
        return dc_td.GetBehaviorModelTrainingSummariesResponse.make_one(res)

    def get_buckets_aggregation(
        self,
        res: "bs_td.GetBucketsAggregationResponseTypeDef",
    ) -> "dc_td.GetBucketsAggregationResponse":
        return dc_td.GetBucketsAggregationResponse.make_one(res)

    def get_cardinality(
        self,
        res: "bs_td.GetCardinalityResponseTypeDef",
    ) -> "dc_td.GetCardinalityResponse":
        return dc_td.GetCardinalityResponse.make_one(res)

    def get_command(
        self,
        res: "bs_td.GetCommandResponseTypeDef",
    ) -> "dc_td.GetCommandResponse":
        return dc_td.GetCommandResponse.make_one(res)

    def get_command_execution(
        self,
        res: "bs_td.GetCommandExecutionResponseTypeDef",
    ) -> "dc_td.GetCommandExecutionResponse":
        return dc_td.GetCommandExecutionResponse.make_one(res)

    def get_effective_policies(
        self,
        res: "bs_td.GetEffectivePoliciesResponseTypeDef",
    ) -> "dc_td.GetEffectivePoliciesResponse":
        return dc_td.GetEffectivePoliciesResponse.make_one(res)

    def get_indexing_configuration(
        self,
        res: "bs_td.GetIndexingConfigurationResponseTypeDef",
    ) -> "dc_td.GetIndexingConfigurationResponse":
        return dc_td.GetIndexingConfigurationResponse.make_one(res)

    def get_job_document(
        self,
        res: "bs_td.GetJobDocumentResponseTypeDef",
    ) -> "dc_td.GetJobDocumentResponse":
        return dc_td.GetJobDocumentResponse.make_one(res)

    def get_logging_options(
        self,
        res: "bs_td.GetLoggingOptionsResponseTypeDef",
    ) -> "dc_td.GetLoggingOptionsResponse":
        return dc_td.GetLoggingOptionsResponse.make_one(res)

    def get_ota_update(
        self,
        res: "bs_td.GetOTAUpdateResponseTypeDef",
    ) -> "dc_td.GetOTAUpdateResponse":
        return dc_td.GetOTAUpdateResponse.make_one(res)

    def get_package(
        self,
        res: "bs_td.GetPackageResponseTypeDef",
    ) -> "dc_td.GetPackageResponse":
        return dc_td.GetPackageResponse.make_one(res)

    def get_package_configuration(
        self,
        res: "bs_td.GetPackageConfigurationResponseTypeDef",
    ) -> "dc_td.GetPackageConfigurationResponse":
        return dc_td.GetPackageConfigurationResponse.make_one(res)

    def get_package_version(
        self,
        res: "bs_td.GetPackageVersionResponseTypeDef",
    ) -> "dc_td.GetPackageVersionResponse":
        return dc_td.GetPackageVersionResponse.make_one(res)

    def get_percentiles(
        self,
        res: "bs_td.GetPercentilesResponseTypeDef",
    ) -> "dc_td.GetPercentilesResponse":
        return dc_td.GetPercentilesResponse.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyResponseTypeDef",
    ) -> "dc_td.GetPolicyResponse":
        return dc_td.GetPolicyResponse.make_one(res)

    def get_policy_version(
        self,
        res: "bs_td.GetPolicyVersionResponseTypeDef",
    ) -> "dc_td.GetPolicyVersionResponse":
        return dc_td.GetPolicyVersionResponse.make_one(res)

    def get_registration_code(
        self,
        res: "bs_td.GetRegistrationCodeResponseTypeDef",
    ) -> "dc_td.GetRegistrationCodeResponse":
        return dc_td.GetRegistrationCodeResponse.make_one(res)

    def get_statistics(
        self,
        res: "bs_td.GetStatisticsResponseTypeDef",
    ) -> "dc_td.GetStatisticsResponse":
        return dc_td.GetStatisticsResponse.make_one(res)

    def get_thing_connectivity_data(
        self,
        res: "bs_td.GetThingConnectivityDataResponseTypeDef",
    ) -> "dc_td.GetThingConnectivityDataResponse":
        return dc_td.GetThingConnectivityDataResponse.make_one(res)

    def get_topic_rule(
        self,
        res: "bs_td.GetTopicRuleResponseTypeDef",
    ) -> "dc_td.GetTopicRuleResponse":
        return dc_td.GetTopicRuleResponse.make_one(res)

    def get_topic_rule_destination(
        self,
        res: "bs_td.GetTopicRuleDestinationResponseTypeDef",
    ) -> "dc_td.GetTopicRuleDestinationResponse":
        return dc_td.GetTopicRuleDestinationResponse.make_one(res)

    def get_v2_logging_options(
        self,
        res: "bs_td.GetV2LoggingOptionsResponseTypeDef",
    ) -> "dc_td.GetV2LoggingOptionsResponse":
        return dc_td.GetV2LoggingOptionsResponse.make_one(res)

    def list_active_violations(
        self,
        res: "bs_td.ListActiveViolationsResponseTypeDef",
    ) -> "dc_td.ListActiveViolationsResponse":
        return dc_td.ListActiveViolationsResponse.make_one(res)

    def list_attached_policies(
        self,
        res: "bs_td.ListAttachedPoliciesResponseTypeDef",
    ) -> "dc_td.ListAttachedPoliciesResponse":
        return dc_td.ListAttachedPoliciesResponse.make_one(res)

    def list_audit_findings(
        self,
        res: "bs_td.ListAuditFindingsResponseTypeDef",
    ) -> "dc_td.ListAuditFindingsResponse":
        return dc_td.ListAuditFindingsResponse.make_one(res)

    def list_audit_mitigation_actions_executions(
        self,
        res: "bs_td.ListAuditMitigationActionsExecutionsResponseTypeDef",
    ) -> "dc_td.ListAuditMitigationActionsExecutionsResponse":
        return dc_td.ListAuditMitigationActionsExecutionsResponse.make_one(res)

    def list_audit_mitigation_actions_tasks(
        self,
        res: "bs_td.ListAuditMitigationActionsTasksResponseTypeDef",
    ) -> "dc_td.ListAuditMitigationActionsTasksResponse":
        return dc_td.ListAuditMitigationActionsTasksResponse.make_one(res)

    def list_audit_suppressions(
        self,
        res: "bs_td.ListAuditSuppressionsResponseTypeDef",
    ) -> "dc_td.ListAuditSuppressionsResponse":
        return dc_td.ListAuditSuppressionsResponse.make_one(res)

    def list_audit_tasks(
        self,
        res: "bs_td.ListAuditTasksResponseTypeDef",
    ) -> "dc_td.ListAuditTasksResponse":
        return dc_td.ListAuditTasksResponse.make_one(res)

    def list_authorizers(
        self,
        res: "bs_td.ListAuthorizersResponseTypeDef",
    ) -> "dc_td.ListAuthorizersResponse":
        return dc_td.ListAuthorizersResponse.make_one(res)

    def list_billing_groups(
        self,
        res: "bs_td.ListBillingGroupsResponseTypeDef",
    ) -> "dc_td.ListBillingGroupsResponse":
        return dc_td.ListBillingGroupsResponse.make_one(res)

    def list_ca_certificates(
        self,
        res: "bs_td.ListCACertificatesResponseTypeDef",
    ) -> "dc_td.ListCACertificatesResponse":
        return dc_td.ListCACertificatesResponse.make_one(res)

    def list_certificate_providers(
        self,
        res: "bs_td.ListCertificateProvidersResponseTypeDef",
    ) -> "dc_td.ListCertificateProvidersResponse":
        return dc_td.ListCertificateProvidersResponse.make_one(res)

    def list_certificates(
        self,
        res: "bs_td.ListCertificatesResponseTypeDef",
    ) -> "dc_td.ListCertificatesResponse":
        return dc_td.ListCertificatesResponse.make_one(res)

    def list_certificates_by_ca(
        self,
        res: "bs_td.ListCertificatesByCAResponseTypeDef",
    ) -> "dc_td.ListCertificatesByCAResponse":
        return dc_td.ListCertificatesByCAResponse.make_one(res)

    def list_command_executions(
        self,
        res: "bs_td.ListCommandExecutionsResponseTypeDef",
    ) -> "dc_td.ListCommandExecutionsResponse":
        return dc_td.ListCommandExecutionsResponse.make_one(res)

    def list_commands(
        self,
        res: "bs_td.ListCommandsResponseTypeDef",
    ) -> "dc_td.ListCommandsResponse":
        return dc_td.ListCommandsResponse.make_one(res)

    def list_custom_metrics(
        self,
        res: "bs_td.ListCustomMetricsResponseTypeDef",
    ) -> "dc_td.ListCustomMetricsResponse":
        return dc_td.ListCustomMetricsResponse.make_one(res)

    def list_detect_mitigation_actions_executions(
        self,
        res: "bs_td.ListDetectMitigationActionsExecutionsResponseTypeDef",
    ) -> "dc_td.ListDetectMitigationActionsExecutionsResponse":
        return dc_td.ListDetectMitigationActionsExecutionsResponse.make_one(res)

    def list_detect_mitigation_actions_tasks(
        self,
        res: "bs_td.ListDetectMitigationActionsTasksResponseTypeDef",
    ) -> "dc_td.ListDetectMitigationActionsTasksResponse":
        return dc_td.ListDetectMitigationActionsTasksResponse.make_one(res)

    def list_dimensions(
        self,
        res: "bs_td.ListDimensionsResponseTypeDef",
    ) -> "dc_td.ListDimensionsResponse":
        return dc_td.ListDimensionsResponse.make_one(res)

    def list_domain_configurations(
        self,
        res: "bs_td.ListDomainConfigurationsResponseTypeDef",
    ) -> "dc_td.ListDomainConfigurationsResponse":
        return dc_td.ListDomainConfigurationsResponse.make_one(res)

    def list_fleet_metrics(
        self,
        res: "bs_td.ListFleetMetricsResponseTypeDef",
    ) -> "dc_td.ListFleetMetricsResponse":
        return dc_td.ListFleetMetricsResponse.make_one(res)

    def list_indices(
        self,
        res: "bs_td.ListIndicesResponseTypeDef",
    ) -> "dc_td.ListIndicesResponse":
        return dc_td.ListIndicesResponse.make_one(res)

    def list_job_executions_for_job(
        self,
        res: "bs_td.ListJobExecutionsForJobResponseTypeDef",
    ) -> "dc_td.ListJobExecutionsForJobResponse":
        return dc_td.ListJobExecutionsForJobResponse.make_one(res)

    def list_job_executions_for_thing(
        self,
        res: "bs_td.ListJobExecutionsForThingResponseTypeDef",
    ) -> "dc_td.ListJobExecutionsForThingResponse":
        return dc_td.ListJobExecutionsForThingResponse.make_one(res)

    def list_job_templates(
        self,
        res: "bs_td.ListJobTemplatesResponseTypeDef",
    ) -> "dc_td.ListJobTemplatesResponse":
        return dc_td.ListJobTemplatesResponse.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResponseTypeDef",
    ) -> "dc_td.ListJobsResponse":
        return dc_td.ListJobsResponse.make_one(res)

    def list_managed_job_templates(
        self,
        res: "bs_td.ListManagedJobTemplatesResponseTypeDef",
    ) -> "dc_td.ListManagedJobTemplatesResponse":
        return dc_td.ListManagedJobTemplatesResponse.make_one(res)

    def list_metric_values(
        self,
        res: "bs_td.ListMetricValuesResponseTypeDef",
    ) -> "dc_td.ListMetricValuesResponse":
        return dc_td.ListMetricValuesResponse.make_one(res)

    def list_mitigation_actions(
        self,
        res: "bs_td.ListMitigationActionsResponseTypeDef",
    ) -> "dc_td.ListMitigationActionsResponse":
        return dc_td.ListMitigationActionsResponse.make_one(res)

    def list_ota_updates(
        self,
        res: "bs_td.ListOTAUpdatesResponseTypeDef",
    ) -> "dc_td.ListOTAUpdatesResponse":
        return dc_td.ListOTAUpdatesResponse.make_one(res)

    def list_outgoing_certificates(
        self,
        res: "bs_td.ListOutgoingCertificatesResponseTypeDef",
    ) -> "dc_td.ListOutgoingCertificatesResponse":
        return dc_td.ListOutgoingCertificatesResponse.make_one(res)

    def list_package_versions(
        self,
        res: "bs_td.ListPackageVersionsResponseTypeDef",
    ) -> "dc_td.ListPackageVersionsResponse":
        return dc_td.ListPackageVersionsResponse.make_one(res)

    def list_packages(
        self,
        res: "bs_td.ListPackagesResponseTypeDef",
    ) -> "dc_td.ListPackagesResponse":
        return dc_td.ListPackagesResponse.make_one(res)

    def list_policies(
        self,
        res: "bs_td.ListPoliciesResponseTypeDef",
    ) -> "dc_td.ListPoliciesResponse":
        return dc_td.ListPoliciesResponse.make_one(res)

    def list_policy_principals(
        self,
        res: "bs_td.ListPolicyPrincipalsResponseTypeDef",
    ) -> "dc_td.ListPolicyPrincipalsResponse":
        return dc_td.ListPolicyPrincipalsResponse.make_one(res)

    def list_policy_versions(
        self,
        res: "bs_td.ListPolicyVersionsResponseTypeDef",
    ) -> "dc_td.ListPolicyVersionsResponse":
        return dc_td.ListPolicyVersionsResponse.make_one(res)

    def list_principal_policies(
        self,
        res: "bs_td.ListPrincipalPoliciesResponseTypeDef",
    ) -> "dc_td.ListPrincipalPoliciesResponse":
        return dc_td.ListPrincipalPoliciesResponse.make_one(res)

    def list_principal_things(
        self,
        res: "bs_td.ListPrincipalThingsResponseTypeDef",
    ) -> "dc_td.ListPrincipalThingsResponse":
        return dc_td.ListPrincipalThingsResponse.make_one(res)

    def list_principal_things_v2(
        self,
        res: "bs_td.ListPrincipalThingsV2ResponseTypeDef",
    ) -> "dc_td.ListPrincipalThingsV2Response":
        return dc_td.ListPrincipalThingsV2Response.make_one(res)

    def list_provisioning_template_versions(
        self,
        res: "bs_td.ListProvisioningTemplateVersionsResponseTypeDef",
    ) -> "dc_td.ListProvisioningTemplateVersionsResponse":
        return dc_td.ListProvisioningTemplateVersionsResponse.make_one(res)

    def list_provisioning_templates(
        self,
        res: "bs_td.ListProvisioningTemplatesResponseTypeDef",
    ) -> "dc_td.ListProvisioningTemplatesResponse":
        return dc_td.ListProvisioningTemplatesResponse.make_one(res)

    def list_related_resources_for_audit_finding(
        self,
        res: "bs_td.ListRelatedResourcesForAuditFindingResponseTypeDef",
    ) -> "dc_td.ListRelatedResourcesForAuditFindingResponse":
        return dc_td.ListRelatedResourcesForAuditFindingResponse.make_one(res)

    def list_role_aliases(
        self,
        res: "bs_td.ListRoleAliasesResponseTypeDef",
    ) -> "dc_td.ListRoleAliasesResponse":
        return dc_td.ListRoleAliasesResponse.make_one(res)

    def list_sbom_validation_results(
        self,
        res: "bs_td.ListSbomValidationResultsResponseTypeDef",
    ) -> "dc_td.ListSbomValidationResultsResponse":
        return dc_td.ListSbomValidationResultsResponse.make_one(res)

    def list_scheduled_audits(
        self,
        res: "bs_td.ListScheduledAuditsResponseTypeDef",
    ) -> "dc_td.ListScheduledAuditsResponse":
        return dc_td.ListScheduledAuditsResponse.make_one(res)

    def list_security_profiles(
        self,
        res: "bs_td.ListSecurityProfilesResponseTypeDef",
    ) -> "dc_td.ListSecurityProfilesResponse":
        return dc_td.ListSecurityProfilesResponse.make_one(res)

    def list_security_profiles_for_target(
        self,
        res: "bs_td.ListSecurityProfilesForTargetResponseTypeDef",
    ) -> "dc_td.ListSecurityProfilesForTargetResponse":
        return dc_td.ListSecurityProfilesForTargetResponse.make_one(res)

    def list_streams(
        self,
        res: "bs_td.ListStreamsResponseTypeDef",
    ) -> "dc_td.ListStreamsResponse":
        return dc_td.ListStreamsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_targets_for_policy(
        self,
        res: "bs_td.ListTargetsForPolicyResponseTypeDef",
    ) -> "dc_td.ListTargetsForPolicyResponse":
        return dc_td.ListTargetsForPolicyResponse.make_one(res)

    def list_targets_for_security_profile(
        self,
        res: "bs_td.ListTargetsForSecurityProfileResponseTypeDef",
    ) -> "dc_td.ListTargetsForSecurityProfileResponse":
        return dc_td.ListTargetsForSecurityProfileResponse.make_one(res)

    def list_thing_groups(
        self,
        res: "bs_td.ListThingGroupsResponseTypeDef",
    ) -> "dc_td.ListThingGroupsResponse":
        return dc_td.ListThingGroupsResponse.make_one(res)

    def list_thing_groups_for_thing(
        self,
        res: "bs_td.ListThingGroupsForThingResponseTypeDef",
    ) -> "dc_td.ListThingGroupsForThingResponse":
        return dc_td.ListThingGroupsForThingResponse.make_one(res)

    def list_thing_principals(
        self,
        res: "bs_td.ListThingPrincipalsResponseTypeDef",
    ) -> "dc_td.ListThingPrincipalsResponse":
        return dc_td.ListThingPrincipalsResponse.make_one(res)

    def list_thing_principals_v2(
        self,
        res: "bs_td.ListThingPrincipalsV2ResponseTypeDef",
    ) -> "dc_td.ListThingPrincipalsV2Response":
        return dc_td.ListThingPrincipalsV2Response.make_one(res)

    def list_thing_registration_task_reports(
        self,
        res: "bs_td.ListThingRegistrationTaskReportsResponseTypeDef",
    ) -> "dc_td.ListThingRegistrationTaskReportsResponse":
        return dc_td.ListThingRegistrationTaskReportsResponse.make_one(res)

    def list_thing_registration_tasks(
        self,
        res: "bs_td.ListThingRegistrationTasksResponseTypeDef",
    ) -> "dc_td.ListThingRegistrationTasksResponse":
        return dc_td.ListThingRegistrationTasksResponse.make_one(res)

    def list_thing_types(
        self,
        res: "bs_td.ListThingTypesResponseTypeDef",
    ) -> "dc_td.ListThingTypesResponse":
        return dc_td.ListThingTypesResponse.make_one(res)

    def list_things(
        self,
        res: "bs_td.ListThingsResponseTypeDef",
    ) -> "dc_td.ListThingsResponse":
        return dc_td.ListThingsResponse.make_one(res)

    def list_things_in_billing_group(
        self,
        res: "bs_td.ListThingsInBillingGroupResponseTypeDef",
    ) -> "dc_td.ListThingsInBillingGroupResponse":
        return dc_td.ListThingsInBillingGroupResponse.make_one(res)

    def list_things_in_thing_group(
        self,
        res: "bs_td.ListThingsInThingGroupResponseTypeDef",
    ) -> "dc_td.ListThingsInThingGroupResponse":
        return dc_td.ListThingsInThingGroupResponse.make_one(res)

    def list_topic_rule_destinations(
        self,
        res: "bs_td.ListTopicRuleDestinationsResponseTypeDef",
    ) -> "dc_td.ListTopicRuleDestinationsResponse":
        return dc_td.ListTopicRuleDestinationsResponse.make_one(res)

    def list_topic_rules(
        self,
        res: "bs_td.ListTopicRulesResponseTypeDef",
    ) -> "dc_td.ListTopicRulesResponse":
        return dc_td.ListTopicRulesResponse.make_one(res)

    def list_v2_logging_levels(
        self,
        res: "bs_td.ListV2LoggingLevelsResponseTypeDef",
    ) -> "dc_td.ListV2LoggingLevelsResponse":
        return dc_td.ListV2LoggingLevelsResponse.make_one(res)

    def list_violation_events(
        self,
        res: "bs_td.ListViolationEventsResponseTypeDef",
    ) -> "dc_td.ListViolationEventsResponse":
        return dc_td.ListViolationEventsResponse.make_one(res)

    def register_ca_certificate(
        self,
        res: "bs_td.RegisterCACertificateResponseTypeDef",
    ) -> "dc_td.RegisterCACertificateResponse":
        return dc_td.RegisterCACertificateResponse.make_one(res)

    def register_certificate(
        self,
        res: "bs_td.RegisterCertificateResponseTypeDef",
    ) -> "dc_td.RegisterCertificateResponse":
        return dc_td.RegisterCertificateResponse.make_one(res)

    def register_certificate_without_ca(
        self,
        res: "bs_td.RegisterCertificateWithoutCAResponseTypeDef",
    ) -> "dc_td.RegisterCertificateWithoutCAResponse":
        return dc_td.RegisterCertificateWithoutCAResponse.make_one(res)

    def register_thing(
        self,
        res: "bs_td.RegisterThingResponseTypeDef",
    ) -> "dc_td.RegisterThingResponse":
        return dc_td.RegisterThingResponse.make_one(res)

    def reject_certificate_transfer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def replace_topic_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def search_index(
        self,
        res: "bs_td.SearchIndexResponseTypeDef",
    ) -> "dc_td.SearchIndexResponse":
        return dc_td.SearchIndexResponse.make_one(res)

    def set_default_authorizer(
        self,
        res: "bs_td.SetDefaultAuthorizerResponseTypeDef",
    ) -> "dc_td.SetDefaultAuthorizerResponse":
        return dc_td.SetDefaultAuthorizerResponse.make_one(res)

    def set_default_policy_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_logging_options(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_v2_logging_level(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_v2_logging_options(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_audit_mitigation_actions_task(
        self,
        res: "bs_td.StartAuditMitigationActionsTaskResponseTypeDef",
    ) -> "dc_td.StartAuditMitigationActionsTaskResponse":
        return dc_td.StartAuditMitigationActionsTaskResponse.make_one(res)

    def start_detect_mitigation_actions_task(
        self,
        res: "bs_td.StartDetectMitigationActionsTaskResponseTypeDef",
    ) -> "dc_td.StartDetectMitigationActionsTaskResponse":
        return dc_td.StartDetectMitigationActionsTaskResponse.make_one(res)

    def start_on_demand_audit_task(
        self,
        res: "bs_td.StartOnDemandAuditTaskResponseTypeDef",
    ) -> "dc_td.StartOnDemandAuditTaskResponse":
        return dc_td.StartOnDemandAuditTaskResponse.make_one(res)

    def start_thing_registration_task(
        self,
        res: "bs_td.StartThingRegistrationTaskResponseTypeDef",
    ) -> "dc_td.StartThingRegistrationTaskResponse":
        return dc_td.StartThingRegistrationTaskResponse.make_one(res)

    def test_authorization(
        self,
        res: "bs_td.TestAuthorizationResponseTypeDef",
    ) -> "dc_td.TestAuthorizationResponse":
        return dc_td.TestAuthorizationResponse.make_one(res)

    def test_invoke_authorizer(
        self,
        res: "bs_td.TestInvokeAuthorizerResponseTypeDef",
    ) -> "dc_td.TestInvokeAuthorizerResponse":
        return dc_td.TestInvokeAuthorizerResponse.make_one(res)

    def transfer_certificate(
        self,
        res: "bs_td.TransferCertificateResponseTypeDef",
    ) -> "dc_td.TransferCertificateResponse":
        return dc_td.TransferCertificateResponse.make_one(res)

    def update_authorizer(
        self,
        res: "bs_td.UpdateAuthorizerResponseTypeDef",
    ) -> "dc_td.UpdateAuthorizerResponse":
        return dc_td.UpdateAuthorizerResponse.make_one(res)

    def update_billing_group(
        self,
        res: "bs_td.UpdateBillingGroupResponseTypeDef",
    ) -> "dc_td.UpdateBillingGroupResponse":
        return dc_td.UpdateBillingGroupResponse.make_one(res)

    def update_ca_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_certificate_provider(
        self,
        res: "bs_td.UpdateCertificateProviderResponseTypeDef",
    ) -> "dc_td.UpdateCertificateProviderResponse":
        return dc_td.UpdateCertificateProviderResponse.make_one(res)

    def update_command(
        self,
        res: "bs_td.UpdateCommandResponseTypeDef",
    ) -> "dc_td.UpdateCommandResponse":
        return dc_td.UpdateCommandResponse.make_one(res)

    def update_custom_metric(
        self,
        res: "bs_td.UpdateCustomMetricResponseTypeDef",
    ) -> "dc_td.UpdateCustomMetricResponse":
        return dc_td.UpdateCustomMetricResponse.make_one(res)

    def update_dimension(
        self,
        res: "bs_td.UpdateDimensionResponseTypeDef",
    ) -> "dc_td.UpdateDimensionResponse":
        return dc_td.UpdateDimensionResponse.make_one(res)

    def update_domain_configuration(
        self,
        res: "bs_td.UpdateDomainConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateDomainConfigurationResponse":
        return dc_td.UpdateDomainConfigurationResponse.make_one(res)

    def update_dynamic_thing_group(
        self,
        res: "bs_td.UpdateDynamicThingGroupResponseTypeDef",
    ) -> "dc_td.UpdateDynamicThingGroupResponse":
        return dc_td.UpdateDynamicThingGroupResponse.make_one(res)

    def update_fleet_metric(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_mitigation_action(
        self,
        res: "bs_td.UpdateMitigationActionResponseTypeDef",
    ) -> "dc_td.UpdateMitigationActionResponse":
        return dc_td.UpdateMitigationActionResponse.make_one(res)

    def update_role_alias(
        self,
        res: "bs_td.UpdateRoleAliasResponseTypeDef",
    ) -> "dc_td.UpdateRoleAliasResponse":
        return dc_td.UpdateRoleAliasResponse.make_one(res)

    def update_scheduled_audit(
        self,
        res: "bs_td.UpdateScheduledAuditResponseTypeDef",
    ) -> "dc_td.UpdateScheduledAuditResponse":
        return dc_td.UpdateScheduledAuditResponse.make_one(res)

    def update_security_profile(
        self,
        res: "bs_td.UpdateSecurityProfileResponseTypeDef",
    ) -> "dc_td.UpdateSecurityProfileResponse":
        return dc_td.UpdateSecurityProfileResponse.make_one(res)

    def update_stream(
        self,
        res: "bs_td.UpdateStreamResponseTypeDef",
    ) -> "dc_td.UpdateStreamResponse":
        return dc_td.UpdateStreamResponse.make_one(res)

    def update_thing_group(
        self,
        res: "bs_td.UpdateThingGroupResponseTypeDef",
    ) -> "dc_td.UpdateThingGroupResponse":
        return dc_td.UpdateThingGroupResponse.make_one(res)

    def validate_security_profile_behaviors(
        self,
        res: "bs_td.ValidateSecurityProfileBehaviorsResponseTypeDef",
    ) -> "dc_td.ValidateSecurityProfileBehaviorsResponse":
        return dc_td.ValidateSecurityProfileBehaviorsResponse.make_one(res)


iot_caster = IOTCaster()
