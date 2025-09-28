# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_resiliencehub import type_defs as bs_td


class RESILIENCEHUBCaster:

    def accept_resource_grouping_recommendations(
        self,
        res: "bs_td.AcceptResourceGroupingRecommendationsResponseTypeDef",
    ) -> "dc_td.AcceptResourceGroupingRecommendationsResponse":
        return dc_td.AcceptResourceGroupingRecommendationsResponse.make_one(res)

    def add_draft_app_version_resource_mappings(
        self,
        res: "bs_td.AddDraftAppVersionResourceMappingsResponseTypeDef",
    ) -> "dc_td.AddDraftAppVersionResourceMappingsResponse":
        return dc_td.AddDraftAppVersionResourceMappingsResponse.make_one(res)

    def batch_update_recommendation_status(
        self,
        res: "bs_td.BatchUpdateRecommendationStatusResponseTypeDef",
    ) -> "dc_td.BatchUpdateRecommendationStatusResponse":
        return dc_td.BatchUpdateRecommendationStatusResponse.make_one(res)

    def create_app(
        self,
        res: "bs_td.CreateAppResponseTypeDef",
    ) -> "dc_td.CreateAppResponse":
        return dc_td.CreateAppResponse.make_one(res)

    def create_app_version_app_component(
        self,
        res: "bs_td.CreateAppVersionAppComponentResponseTypeDef",
    ) -> "dc_td.CreateAppVersionAppComponentResponse":
        return dc_td.CreateAppVersionAppComponentResponse.make_one(res)

    def create_app_version_resource(
        self,
        res: "bs_td.CreateAppVersionResourceResponseTypeDef",
    ) -> "dc_td.CreateAppVersionResourceResponse":
        return dc_td.CreateAppVersionResourceResponse.make_one(res)

    def create_recommendation_template(
        self,
        res: "bs_td.CreateRecommendationTemplateResponseTypeDef",
    ) -> "dc_td.CreateRecommendationTemplateResponse":
        return dc_td.CreateRecommendationTemplateResponse.make_one(res)

    def create_resiliency_policy(
        self,
        res: "bs_td.CreateResiliencyPolicyResponseTypeDef",
    ) -> "dc_td.CreateResiliencyPolicyResponse":
        return dc_td.CreateResiliencyPolicyResponse.make_one(res)

    def delete_app(
        self,
        res: "bs_td.DeleteAppResponseTypeDef",
    ) -> "dc_td.DeleteAppResponse":
        return dc_td.DeleteAppResponse.make_one(res)

    def delete_app_assessment(
        self,
        res: "bs_td.DeleteAppAssessmentResponseTypeDef",
    ) -> "dc_td.DeleteAppAssessmentResponse":
        return dc_td.DeleteAppAssessmentResponse.make_one(res)

    def delete_app_input_source(
        self,
        res: "bs_td.DeleteAppInputSourceResponseTypeDef",
    ) -> "dc_td.DeleteAppInputSourceResponse":
        return dc_td.DeleteAppInputSourceResponse.make_one(res)

    def delete_app_version_app_component(
        self,
        res: "bs_td.DeleteAppVersionAppComponentResponseTypeDef",
    ) -> "dc_td.DeleteAppVersionAppComponentResponse":
        return dc_td.DeleteAppVersionAppComponentResponse.make_one(res)

    def delete_app_version_resource(
        self,
        res: "bs_td.DeleteAppVersionResourceResponseTypeDef",
    ) -> "dc_td.DeleteAppVersionResourceResponse":
        return dc_td.DeleteAppVersionResourceResponse.make_one(res)

    def delete_recommendation_template(
        self,
        res: "bs_td.DeleteRecommendationTemplateResponseTypeDef",
    ) -> "dc_td.DeleteRecommendationTemplateResponse":
        return dc_td.DeleteRecommendationTemplateResponse.make_one(res)

    def delete_resiliency_policy(
        self,
        res: "bs_td.DeleteResiliencyPolicyResponseTypeDef",
    ) -> "dc_td.DeleteResiliencyPolicyResponse":
        return dc_td.DeleteResiliencyPolicyResponse.make_one(res)

    def describe_app(
        self,
        res: "bs_td.DescribeAppResponseTypeDef",
    ) -> "dc_td.DescribeAppResponse":
        return dc_td.DescribeAppResponse.make_one(res)

    def describe_app_assessment(
        self,
        res: "bs_td.DescribeAppAssessmentResponseTypeDef",
    ) -> "dc_td.DescribeAppAssessmentResponse":
        return dc_td.DescribeAppAssessmentResponse.make_one(res)

    def describe_app_version(
        self,
        res: "bs_td.DescribeAppVersionResponseTypeDef",
    ) -> "dc_td.DescribeAppVersionResponse":
        return dc_td.DescribeAppVersionResponse.make_one(res)

    def describe_app_version_app_component(
        self,
        res: "bs_td.DescribeAppVersionAppComponentResponseTypeDef",
    ) -> "dc_td.DescribeAppVersionAppComponentResponse":
        return dc_td.DescribeAppVersionAppComponentResponse.make_one(res)

    def describe_app_version_resource(
        self,
        res: "bs_td.DescribeAppVersionResourceResponseTypeDef",
    ) -> "dc_td.DescribeAppVersionResourceResponse":
        return dc_td.DescribeAppVersionResourceResponse.make_one(res)

    def describe_app_version_resources_resolution_status(
        self,
        res: "bs_td.DescribeAppVersionResourcesResolutionStatusResponseTypeDef",
    ) -> "dc_td.DescribeAppVersionResourcesResolutionStatusResponse":
        return dc_td.DescribeAppVersionResourcesResolutionStatusResponse.make_one(res)

    def describe_app_version_template(
        self,
        res: "bs_td.DescribeAppVersionTemplateResponseTypeDef",
    ) -> "dc_td.DescribeAppVersionTemplateResponse":
        return dc_td.DescribeAppVersionTemplateResponse.make_one(res)

    def describe_draft_app_version_resources_import_status(
        self,
        res: "bs_td.DescribeDraftAppVersionResourcesImportStatusResponseTypeDef",
    ) -> "dc_td.DescribeDraftAppVersionResourcesImportStatusResponse":
        return dc_td.DescribeDraftAppVersionResourcesImportStatusResponse.make_one(res)

    def describe_metrics_export(
        self,
        res: "bs_td.DescribeMetricsExportResponseTypeDef",
    ) -> "dc_td.DescribeMetricsExportResponse":
        return dc_td.DescribeMetricsExportResponse.make_one(res)

    def describe_resiliency_policy(
        self,
        res: "bs_td.DescribeResiliencyPolicyResponseTypeDef",
    ) -> "dc_td.DescribeResiliencyPolicyResponse":
        return dc_td.DescribeResiliencyPolicyResponse.make_one(res)

    def describe_resource_grouping_recommendation_task(
        self,
        res: "bs_td.DescribeResourceGroupingRecommendationTaskResponseTypeDef",
    ) -> "dc_td.DescribeResourceGroupingRecommendationTaskResponse":
        return dc_td.DescribeResourceGroupingRecommendationTaskResponse.make_one(res)

    def import_resources_to_draft_app_version(
        self,
        res: "bs_td.ImportResourcesToDraftAppVersionResponseTypeDef",
    ) -> "dc_td.ImportResourcesToDraftAppVersionResponse":
        return dc_td.ImportResourcesToDraftAppVersionResponse.make_one(res)

    def list_alarm_recommendations(
        self,
        res: "bs_td.ListAlarmRecommendationsResponseTypeDef",
    ) -> "dc_td.ListAlarmRecommendationsResponse":
        return dc_td.ListAlarmRecommendationsResponse.make_one(res)

    def list_app_assessment_compliance_drifts(
        self,
        res: "bs_td.ListAppAssessmentComplianceDriftsResponseTypeDef",
    ) -> "dc_td.ListAppAssessmentComplianceDriftsResponse":
        return dc_td.ListAppAssessmentComplianceDriftsResponse.make_one(res)

    def list_app_assessment_resource_drifts(
        self,
        res: "bs_td.ListAppAssessmentResourceDriftsResponseTypeDef",
    ) -> "dc_td.ListAppAssessmentResourceDriftsResponse":
        return dc_td.ListAppAssessmentResourceDriftsResponse.make_one(res)

    def list_app_assessments(
        self,
        res: "bs_td.ListAppAssessmentsResponseTypeDef",
    ) -> "dc_td.ListAppAssessmentsResponse":
        return dc_td.ListAppAssessmentsResponse.make_one(res)

    def list_app_component_compliances(
        self,
        res: "bs_td.ListAppComponentCompliancesResponseTypeDef",
    ) -> "dc_td.ListAppComponentCompliancesResponse":
        return dc_td.ListAppComponentCompliancesResponse.make_one(res)

    def list_app_component_recommendations(
        self,
        res: "bs_td.ListAppComponentRecommendationsResponseTypeDef",
    ) -> "dc_td.ListAppComponentRecommendationsResponse":
        return dc_td.ListAppComponentRecommendationsResponse.make_one(res)

    def list_app_input_sources(
        self,
        res: "bs_td.ListAppInputSourcesResponseTypeDef",
    ) -> "dc_td.ListAppInputSourcesResponse":
        return dc_td.ListAppInputSourcesResponse.make_one(res)

    def list_app_version_app_components(
        self,
        res: "bs_td.ListAppVersionAppComponentsResponseTypeDef",
    ) -> "dc_td.ListAppVersionAppComponentsResponse":
        return dc_td.ListAppVersionAppComponentsResponse.make_one(res)

    def list_app_version_resource_mappings(
        self,
        res: "bs_td.ListAppVersionResourceMappingsResponseTypeDef",
    ) -> "dc_td.ListAppVersionResourceMappingsResponse":
        return dc_td.ListAppVersionResourceMappingsResponse.make_one(res)

    def list_app_version_resources(
        self,
        res: "bs_td.ListAppVersionResourcesResponseTypeDef",
    ) -> "dc_td.ListAppVersionResourcesResponse":
        return dc_td.ListAppVersionResourcesResponse.make_one(res)

    def list_app_versions(
        self,
        res: "bs_td.ListAppVersionsResponseTypeDef",
    ) -> "dc_td.ListAppVersionsResponse":
        return dc_td.ListAppVersionsResponse.make_one(res)

    def list_apps(
        self,
        res: "bs_td.ListAppsResponseTypeDef",
    ) -> "dc_td.ListAppsResponse":
        return dc_td.ListAppsResponse.make_one(res)

    def list_metrics(
        self,
        res: "bs_td.ListMetricsResponseTypeDef",
    ) -> "dc_td.ListMetricsResponse":
        return dc_td.ListMetricsResponse.make_one(res)

    def list_recommendation_templates(
        self,
        res: "bs_td.ListRecommendationTemplatesResponseTypeDef",
    ) -> "dc_td.ListRecommendationTemplatesResponse":
        return dc_td.ListRecommendationTemplatesResponse.make_one(res)

    def list_resiliency_policies(
        self,
        res: "bs_td.ListResiliencyPoliciesResponseTypeDef",
    ) -> "dc_td.ListResiliencyPoliciesResponse":
        return dc_td.ListResiliencyPoliciesResponse.make_one(res)

    def list_resource_grouping_recommendations(
        self,
        res: "bs_td.ListResourceGroupingRecommendationsResponseTypeDef",
    ) -> "dc_td.ListResourceGroupingRecommendationsResponse":
        return dc_td.ListResourceGroupingRecommendationsResponse.make_one(res)

    def list_sop_recommendations(
        self,
        res: "bs_td.ListSopRecommendationsResponseTypeDef",
    ) -> "dc_td.ListSopRecommendationsResponse":
        return dc_td.ListSopRecommendationsResponse.make_one(res)

    def list_suggested_resiliency_policies(
        self,
        res: "bs_td.ListSuggestedResiliencyPoliciesResponseTypeDef",
    ) -> "dc_td.ListSuggestedResiliencyPoliciesResponse":
        return dc_td.ListSuggestedResiliencyPoliciesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_test_recommendations(
        self,
        res: "bs_td.ListTestRecommendationsResponseTypeDef",
    ) -> "dc_td.ListTestRecommendationsResponse":
        return dc_td.ListTestRecommendationsResponse.make_one(res)

    def list_unsupported_app_version_resources(
        self,
        res: "bs_td.ListUnsupportedAppVersionResourcesResponseTypeDef",
    ) -> "dc_td.ListUnsupportedAppVersionResourcesResponse":
        return dc_td.ListUnsupportedAppVersionResourcesResponse.make_one(res)

    def publish_app_version(
        self,
        res: "bs_td.PublishAppVersionResponseTypeDef",
    ) -> "dc_td.PublishAppVersionResponse":
        return dc_td.PublishAppVersionResponse.make_one(res)

    def put_draft_app_version_template(
        self,
        res: "bs_td.PutDraftAppVersionTemplateResponseTypeDef",
    ) -> "dc_td.PutDraftAppVersionTemplateResponse":
        return dc_td.PutDraftAppVersionTemplateResponse.make_one(res)

    def reject_resource_grouping_recommendations(
        self,
        res: "bs_td.RejectResourceGroupingRecommendationsResponseTypeDef",
    ) -> "dc_td.RejectResourceGroupingRecommendationsResponse":
        return dc_td.RejectResourceGroupingRecommendationsResponse.make_one(res)

    def remove_draft_app_version_resource_mappings(
        self,
        res: "bs_td.RemoveDraftAppVersionResourceMappingsResponseTypeDef",
    ) -> "dc_td.RemoveDraftAppVersionResourceMappingsResponse":
        return dc_td.RemoveDraftAppVersionResourceMappingsResponse.make_one(res)

    def resolve_app_version_resources(
        self,
        res: "bs_td.ResolveAppVersionResourcesResponseTypeDef",
    ) -> "dc_td.ResolveAppVersionResourcesResponse":
        return dc_td.ResolveAppVersionResourcesResponse.make_one(res)

    def start_app_assessment(
        self,
        res: "bs_td.StartAppAssessmentResponseTypeDef",
    ) -> "dc_td.StartAppAssessmentResponse":
        return dc_td.StartAppAssessmentResponse.make_one(res)

    def start_metrics_export(
        self,
        res: "bs_td.StartMetricsExportResponseTypeDef",
    ) -> "dc_td.StartMetricsExportResponse":
        return dc_td.StartMetricsExportResponse.make_one(res)

    def start_resource_grouping_recommendation_task(
        self,
        res: "bs_td.StartResourceGroupingRecommendationTaskResponseTypeDef",
    ) -> "dc_td.StartResourceGroupingRecommendationTaskResponse":
        return dc_td.StartResourceGroupingRecommendationTaskResponse.make_one(res)

    def update_app(
        self,
        res: "bs_td.UpdateAppResponseTypeDef",
    ) -> "dc_td.UpdateAppResponse":
        return dc_td.UpdateAppResponse.make_one(res)

    def update_app_version(
        self,
        res: "bs_td.UpdateAppVersionResponseTypeDef",
    ) -> "dc_td.UpdateAppVersionResponse":
        return dc_td.UpdateAppVersionResponse.make_one(res)

    def update_app_version_app_component(
        self,
        res: "bs_td.UpdateAppVersionAppComponentResponseTypeDef",
    ) -> "dc_td.UpdateAppVersionAppComponentResponse":
        return dc_td.UpdateAppVersionAppComponentResponse.make_one(res)

    def update_app_version_resource(
        self,
        res: "bs_td.UpdateAppVersionResourceResponseTypeDef",
    ) -> "dc_td.UpdateAppVersionResourceResponse":
        return dc_td.UpdateAppVersionResourceResponse.make_one(res)

    def update_resiliency_policy(
        self,
        res: "bs_td.UpdateResiliencyPolicyResponseTypeDef",
    ) -> "dc_td.UpdateResiliencyPolicyResponse":
        return dc_td.UpdateResiliencyPolicyResponse.make_one(res)


resiliencehub_caster = RESILIENCEHUBCaster()
