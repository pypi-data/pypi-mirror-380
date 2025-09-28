# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_partnercentral_selling import type_defs as bs_td


class PARTNERCENTRAL_SELLINGCaster:

    def accept_engagement_invitation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def assign_opportunity(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_opportunity(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_engagement(
        self,
        res: "bs_td.CreateEngagementResponseTypeDef",
    ) -> "dc_td.CreateEngagementResponse":
        return dc_td.CreateEngagementResponse.make_one(res)

    def create_engagement_invitation(
        self,
        res: "bs_td.CreateEngagementInvitationResponseTypeDef",
    ) -> "dc_td.CreateEngagementInvitationResponse":
        return dc_td.CreateEngagementInvitationResponse.make_one(res)

    def create_opportunity(
        self,
        res: "bs_td.CreateOpportunityResponseTypeDef",
    ) -> "dc_td.CreateOpportunityResponse":
        return dc_td.CreateOpportunityResponse.make_one(res)

    def create_resource_snapshot(
        self,
        res: "bs_td.CreateResourceSnapshotResponseTypeDef",
    ) -> "dc_td.CreateResourceSnapshotResponse":
        return dc_td.CreateResourceSnapshotResponse.make_one(res)

    def create_resource_snapshot_job(
        self,
        res: "bs_td.CreateResourceSnapshotJobResponseTypeDef",
    ) -> "dc_td.CreateResourceSnapshotJobResponse":
        return dc_td.CreateResourceSnapshotJobResponse.make_one(res)

    def delete_resource_snapshot_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_opportunity(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_aws_opportunity_summary(
        self,
        res: "bs_td.GetAwsOpportunitySummaryResponseTypeDef",
    ) -> "dc_td.GetAwsOpportunitySummaryResponse":
        return dc_td.GetAwsOpportunitySummaryResponse.make_one(res)

    def get_engagement(
        self,
        res: "bs_td.GetEngagementResponseTypeDef",
    ) -> "dc_td.GetEngagementResponse":
        return dc_td.GetEngagementResponse.make_one(res)

    def get_engagement_invitation(
        self,
        res: "bs_td.GetEngagementInvitationResponseTypeDef",
    ) -> "dc_td.GetEngagementInvitationResponse":
        return dc_td.GetEngagementInvitationResponse.make_one(res)

    def get_opportunity(
        self,
        res: "bs_td.GetOpportunityResponseTypeDef",
    ) -> "dc_td.GetOpportunityResponse":
        return dc_td.GetOpportunityResponse.make_one(res)

    def get_resource_snapshot(
        self,
        res: "bs_td.GetResourceSnapshotResponseTypeDef",
    ) -> "dc_td.GetResourceSnapshotResponse":
        return dc_td.GetResourceSnapshotResponse.make_one(res)

    def get_resource_snapshot_job(
        self,
        res: "bs_td.GetResourceSnapshotJobResponseTypeDef",
    ) -> "dc_td.GetResourceSnapshotJobResponse":
        return dc_td.GetResourceSnapshotJobResponse.make_one(res)

    def get_selling_system_settings(
        self,
        res: "bs_td.GetSellingSystemSettingsResponseTypeDef",
    ) -> "dc_td.GetSellingSystemSettingsResponse":
        return dc_td.GetSellingSystemSettingsResponse.make_one(res)

    def list_engagement_by_accepting_invitation_tasks(
        self,
        res: "bs_td.ListEngagementByAcceptingInvitationTasksResponseTypeDef",
    ) -> "dc_td.ListEngagementByAcceptingInvitationTasksResponse":
        return dc_td.ListEngagementByAcceptingInvitationTasksResponse.make_one(res)

    def list_engagement_from_opportunity_tasks(
        self,
        res: "bs_td.ListEngagementFromOpportunityTasksResponseTypeDef",
    ) -> "dc_td.ListEngagementFromOpportunityTasksResponse":
        return dc_td.ListEngagementFromOpportunityTasksResponse.make_one(res)

    def list_engagement_invitations(
        self,
        res: "bs_td.ListEngagementInvitationsResponseTypeDef",
    ) -> "dc_td.ListEngagementInvitationsResponse":
        return dc_td.ListEngagementInvitationsResponse.make_one(res)

    def list_engagement_members(
        self,
        res: "bs_td.ListEngagementMembersResponseTypeDef",
    ) -> "dc_td.ListEngagementMembersResponse":
        return dc_td.ListEngagementMembersResponse.make_one(res)

    def list_engagement_resource_associations(
        self,
        res: "bs_td.ListEngagementResourceAssociationsResponseTypeDef",
    ) -> "dc_td.ListEngagementResourceAssociationsResponse":
        return dc_td.ListEngagementResourceAssociationsResponse.make_one(res)

    def list_engagements(
        self,
        res: "bs_td.ListEngagementsResponseTypeDef",
    ) -> "dc_td.ListEngagementsResponse":
        return dc_td.ListEngagementsResponse.make_one(res)

    def list_opportunities(
        self,
        res: "bs_td.ListOpportunitiesResponseTypeDef",
    ) -> "dc_td.ListOpportunitiesResponse":
        return dc_td.ListOpportunitiesResponse.make_one(res)

    def list_resource_snapshot_jobs(
        self,
        res: "bs_td.ListResourceSnapshotJobsResponseTypeDef",
    ) -> "dc_td.ListResourceSnapshotJobsResponse":
        return dc_td.ListResourceSnapshotJobsResponse.make_one(res)

    def list_resource_snapshots(
        self,
        res: "bs_td.ListResourceSnapshotsResponseTypeDef",
    ) -> "dc_td.ListResourceSnapshotsResponse":
        return dc_td.ListResourceSnapshotsResponse.make_one(res)

    def list_solutions(
        self,
        res: "bs_td.ListSolutionsResponseTypeDef",
    ) -> "dc_td.ListSolutionsResponse":
        return dc_td.ListSolutionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_selling_system_settings(
        self,
        res: "bs_td.PutSellingSystemSettingsResponseTypeDef",
    ) -> "dc_td.PutSellingSystemSettingsResponse":
        return dc_td.PutSellingSystemSettingsResponse.make_one(res)

    def reject_engagement_invitation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_engagement_by_accepting_invitation_task(
        self,
        res: "bs_td.StartEngagementByAcceptingInvitationTaskResponseTypeDef",
    ) -> "dc_td.StartEngagementByAcceptingInvitationTaskResponse":
        return dc_td.StartEngagementByAcceptingInvitationTaskResponse.make_one(res)

    def start_engagement_from_opportunity_task(
        self,
        res: "bs_td.StartEngagementFromOpportunityTaskResponseTypeDef",
    ) -> "dc_td.StartEngagementFromOpportunityTaskResponse":
        return dc_td.StartEngagementFromOpportunityTaskResponse.make_one(res)

    def start_resource_snapshot_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_resource_snapshot_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def submit_opportunity(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_opportunity(
        self,
        res: "bs_td.UpdateOpportunityResponseTypeDef",
    ) -> "dc_td.UpdateOpportunityResponse":
        return dc_td.UpdateOpportunityResponse.make_one(res)


partnercentral_selling_caster = PARTNERCENTRAL_SELLINGCaster()
