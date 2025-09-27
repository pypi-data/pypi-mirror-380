# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_inspector import type_defs as bs_td


class INSPECTORCaster:

    def add_attributes_to_findings(
        self,
        res: "bs_td.AddAttributesToFindingsResponseTypeDef",
    ) -> "dc_td.AddAttributesToFindingsResponse":
        return dc_td.AddAttributesToFindingsResponse.make_one(res)

    def create_assessment_target(
        self,
        res: "bs_td.CreateAssessmentTargetResponseTypeDef",
    ) -> "dc_td.CreateAssessmentTargetResponse":
        return dc_td.CreateAssessmentTargetResponse.make_one(res)

    def create_assessment_template(
        self,
        res: "bs_td.CreateAssessmentTemplateResponseTypeDef",
    ) -> "dc_td.CreateAssessmentTemplateResponse":
        return dc_td.CreateAssessmentTemplateResponse.make_one(res)

    def create_exclusions_preview(
        self,
        res: "bs_td.CreateExclusionsPreviewResponseTypeDef",
    ) -> "dc_td.CreateExclusionsPreviewResponse":
        return dc_td.CreateExclusionsPreviewResponse.make_one(res)

    def create_resource_group(
        self,
        res: "bs_td.CreateResourceGroupResponseTypeDef",
    ) -> "dc_td.CreateResourceGroupResponse":
        return dc_td.CreateResourceGroupResponse.make_one(res)

    def delete_assessment_run(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_assessment_target(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_assessment_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_assessment_runs(
        self,
        res: "bs_td.DescribeAssessmentRunsResponseTypeDef",
    ) -> "dc_td.DescribeAssessmentRunsResponse":
        return dc_td.DescribeAssessmentRunsResponse.make_one(res)

    def describe_assessment_targets(
        self,
        res: "bs_td.DescribeAssessmentTargetsResponseTypeDef",
    ) -> "dc_td.DescribeAssessmentTargetsResponse":
        return dc_td.DescribeAssessmentTargetsResponse.make_one(res)

    def describe_assessment_templates(
        self,
        res: "bs_td.DescribeAssessmentTemplatesResponseTypeDef",
    ) -> "dc_td.DescribeAssessmentTemplatesResponse":
        return dc_td.DescribeAssessmentTemplatesResponse.make_one(res)

    def describe_cross_account_access_role(
        self,
        res: "bs_td.DescribeCrossAccountAccessRoleResponseTypeDef",
    ) -> "dc_td.DescribeCrossAccountAccessRoleResponse":
        return dc_td.DescribeCrossAccountAccessRoleResponse.make_one(res)

    def describe_exclusions(
        self,
        res: "bs_td.DescribeExclusionsResponseTypeDef",
    ) -> "dc_td.DescribeExclusionsResponse":
        return dc_td.DescribeExclusionsResponse.make_one(res)

    def describe_findings(
        self,
        res: "bs_td.DescribeFindingsResponseTypeDef",
    ) -> "dc_td.DescribeFindingsResponse":
        return dc_td.DescribeFindingsResponse.make_one(res)

    def describe_resource_groups(
        self,
        res: "bs_td.DescribeResourceGroupsResponseTypeDef",
    ) -> "dc_td.DescribeResourceGroupsResponse":
        return dc_td.DescribeResourceGroupsResponse.make_one(res)

    def describe_rules_packages(
        self,
        res: "bs_td.DescribeRulesPackagesResponseTypeDef",
    ) -> "dc_td.DescribeRulesPackagesResponse":
        return dc_td.DescribeRulesPackagesResponse.make_one(res)

    def get_assessment_report(
        self,
        res: "bs_td.GetAssessmentReportResponseTypeDef",
    ) -> "dc_td.GetAssessmentReportResponse":
        return dc_td.GetAssessmentReportResponse.make_one(res)

    def get_exclusions_preview(
        self,
        res: "bs_td.GetExclusionsPreviewResponseTypeDef",
    ) -> "dc_td.GetExclusionsPreviewResponse":
        return dc_td.GetExclusionsPreviewResponse.make_one(res)

    def get_telemetry_metadata(
        self,
        res: "bs_td.GetTelemetryMetadataResponseTypeDef",
    ) -> "dc_td.GetTelemetryMetadataResponse":
        return dc_td.GetTelemetryMetadataResponse.make_one(res)

    def list_assessment_run_agents(
        self,
        res: "bs_td.ListAssessmentRunAgentsResponseTypeDef",
    ) -> "dc_td.ListAssessmentRunAgentsResponse":
        return dc_td.ListAssessmentRunAgentsResponse.make_one(res)

    def list_assessment_runs(
        self,
        res: "bs_td.ListAssessmentRunsResponseTypeDef",
    ) -> "dc_td.ListAssessmentRunsResponse":
        return dc_td.ListAssessmentRunsResponse.make_one(res)

    def list_assessment_targets(
        self,
        res: "bs_td.ListAssessmentTargetsResponseTypeDef",
    ) -> "dc_td.ListAssessmentTargetsResponse":
        return dc_td.ListAssessmentTargetsResponse.make_one(res)

    def list_assessment_templates(
        self,
        res: "bs_td.ListAssessmentTemplatesResponseTypeDef",
    ) -> "dc_td.ListAssessmentTemplatesResponse":
        return dc_td.ListAssessmentTemplatesResponse.make_one(res)

    def list_event_subscriptions(
        self,
        res: "bs_td.ListEventSubscriptionsResponseTypeDef",
    ) -> "dc_td.ListEventSubscriptionsResponse":
        return dc_td.ListEventSubscriptionsResponse.make_one(res)

    def list_exclusions(
        self,
        res: "bs_td.ListExclusionsResponseTypeDef",
    ) -> "dc_td.ListExclusionsResponse":
        return dc_td.ListExclusionsResponse.make_one(res)

    def list_findings(
        self,
        res: "bs_td.ListFindingsResponseTypeDef",
    ) -> "dc_td.ListFindingsResponse":
        return dc_td.ListFindingsResponse.make_one(res)

    def list_rules_packages(
        self,
        res: "bs_td.ListRulesPackagesResponseTypeDef",
    ) -> "dc_td.ListRulesPackagesResponse":
        return dc_td.ListRulesPackagesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def preview_agents(
        self,
        res: "bs_td.PreviewAgentsResponseTypeDef",
    ) -> "dc_td.PreviewAgentsResponse":
        return dc_td.PreviewAgentsResponse.make_one(res)

    def register_cross_account_access_role(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_attributes_from_findings(
        self,
        res: "bs_td.RemoveAttributesFromFindingsResponseTypeDef",
    ) -> "dc_td.RemoveAttributesFromFindingsResponse":
        return dc_td.RemoveAttributesFromFindingsResponse.make_one(res)

    def set_tags_for_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_assessment_run(
        self,
        res: "bs_td.StartAssessmentRunResponseTypeDef",
    ) -> "dc_td.StartAssessmentRunResponse":
        return dc_td.StartAssessmentRunResponse.make_one(res)

    def stop_assessment_run(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def subscribe_to_event(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def unsubscribe_from_event(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_assessment_target(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


inspector_caster = INSPECTORCaster()
