# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_wellarchitected import type_defs as bs_td


class WELLARCHITECTEDCaster:

    def associate_lenses(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_profiles(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_lens_share(
        self,
        res: "bs_td.CreateLensShareOutputTypeDef",
    ) -> "dc_td.CreateLensShareOutput":
        return dc_td.CreateLensShareOutput.make_one(res)

    def create_lens_version(
        self,
        res: "bs_td.CreateLensVersionOutputTypeDef",
    ) -> "dc_td.CreateLensVersionOutput":
        return dc_td.CreateLensVersionOutput.make_one(res)

    def create_milestone(
        self,
        res: "bs_td.CreateMilestoneOutputTypeDef",
    ) -> "dc_td.CreateMilestoneOutput":
        return dc_td.CreateMilestoneOutput.make_one(res)

    def create_profile(
        self,
        res: "bs_td.CreateProfileOutputTypeDef",
    ) -> "dc_td.CreateProfileOutput":
        return dc_td.CreateProfileOutput.make_one(res)

    def create_profile_share(
        self,
        res: "bs_td.CreateProfileShareOutputTypeDef",
    ) -> "dc_td.CreateProfileShareOutput":
        return dc_td.CreateProfileShareOutput.make_one(res)

    def create_review_template(
        self,
        res: "bs_td.CreateReviewTemplateOutputTypeDef",
    ) -> "dc_td.CreateReviewTemplateOutput":
        return dc_td.CreateReviewTemplateOutput.make_one(res)

    def create_template_share(
        self,
        res: "bs_td.CreateTemplateShareOutputTypeDef",
    ) -> "dc_td.CreateTemplateShareOutput":
        return dc_td.CreateTemplateShareOutput.make_one(res)

    def create_workload(
        self,
        res: "bs_td.CreateWorkloadOutputTypeDef",
    ) -> "dc_td.CreateWorkloadOutput":
        return dc_td.CreateWorkloadOutput.make_one(res)

    def create_workload_share(
        self,
        res: "bs_td.CreateWorkloadShareOutputTypeDef",
    ) -> "dc_td.CreateWorkloadShareOutput":
        return dc_td.CreateWorkloadShareOutput.make_one(res)

    def delete_lens(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_lens_share(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_profile_share(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_review_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_template_share(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_workload(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_workload_share(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_lenses(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_profiles(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def export_lens(
        self,
        res: "bs_td.ExportLensOutputTypeDef",
    ) -> "dc_td.ExportLensOutput":
        return dc_td.ExportLensOutput.make_one(res)

    def get_answer(
        self,
        res: "bs_td.GetAnswerOutputTypeDef",
    ) -> "dc_td.GetAnswerOutput":
        return dc_td.GetAnswerOutput.make_one(res)

    def get_consolidated_report(
        self,
        res: "bs_td.GetConsolidatedReportOutputTypeDef",
    ) -> "dc_td.GetConsolidatedReportOutput":
        return dc_td.GetConsolidatedReportOutput.make_one(res)

    def get_global_settings(
        self,
        res: "bs_td.GetGlobalSettingsOutputTypeDef",
    ) -> "dc_td.GetGlobalSettingsOutput":
        return dc_td.GetGlobalSettingsOutput.make_one(res)

    def get_lens(
        self,
        res: "bs_td.GetLensOutputTypeDef",
    ) -> "dc_td.GetLensOutput":
        return dc_td.GetLensOutput.make_one(res)

    def get_lens_review(
        self,
        res: "bs_td.GetLensReviewOutputTypeDef",
    ) -> "dc_td.GetLensReviewOutput":
        return dc_td.GetLensReviewOutput.make_one(res)

    def get_lens_review_report(
        self,
        res: "bs_td.GetLensReviewReportOutputTypeDef",
    ) -> "dc_td.GetLensReviewReportOutput":
        return dc_td.GetLensReviewReportOutput.make_one(res)

    def get_lens_version_difference(
        self,
        res: "bs_td.GetLensVersionDifferenceOutputTypeDef",
    ) -> "dc_td.GetLensVersionDifferenceOutput":
        return dc_td.GetLensVersionDifferenceOutput.make_one(res)

    def get_milestone(
        self,
        res: "bs_td.GetMilestoneOutputTypeDef",
    ) -> "dc_td.GetMilestoneOutput":
        return dc_td.GetMilestoneOutput.make_one(res)

    def get_profile(
        self,
        res: "bs_td.GetProfileOutputTypeDef",
    ) -> "dc_td.GetProfileOutput":
        return dc_td.GetProfileOutput.make_one(res)

    def get_profile_template(
        self,
        res: "bs_td.GetProfileTemplateOutputTypeDef",
    ) -> "dc_td.GetProfileTemplateOutput":
        return dc_td.GetProfileTemplateOutput.make_one(res)

    def get_review_template(
        self,
        res: "bs_td.GetReviewTemplateOutputTypeDef",
    ) -> "dc_td.GetReviewTemplateOutput":
        return dc_td.GetReviewTemplateOutput.make_one(res)

    def get_review_template_answer(
        self,
        res: "bs_td.GetReviewTemplateAnswerOutputTypeDef",
    ) -> "dc_td.GetReviewTemplateAnswerOutput":
        return dc_td.GetReviewTemplateAnswerOutput.make_one(res)

    def get_review_template_lens_review(
        self,
        res: "bs_td.GetReviewTemplateLensReviewOutputTypeDef",
    ) -> "dc_td.GetReviewTemplateLensReviewOutput":
        return dc_td.GetReviewTemplateLensReviewOutput.make_one(res)

    def get_workload(
        self,
        res: "bs_td.GetWorkloadOutputTypeDef",
    ) -> "dc_td.GetWorkloadOutput":
        return dc_td.GetWorkloadOutput.make_one(res)

    def import_lens(
        self,
        res: "bs_td.ImportLensOutputTypeDef",
    ) -> "dc_td.ImportLensOutput":
        return dc_td.ImportLensOutput.make_one(res)

    def list_answers(
        self,
        res: "bs_td.ListAnswersOutputTypeDef",
    ) -> "dc_td.ListAnswersOutput":
        return dc_td.ListAnswersOutput.make_one(res)

    def list_check_details(
        self,
        res: "bs_td.ListCheckDetailsOutputTypeDef",
    ) -> "dc_td.ListCheckDetailsOutput":
        return dc_td.ListCheckDetailsOutput.make_one(res)

    def list_check_summaries(
        self,
        res: "bs_td.ListCheckSummariesOutputTypeDef",
    ) -> "dc_td.ListCheckSummariesOutput":
        return dc_td.ListCheckSummariesOutput.make_one(res)

    def list_lens_review_improvements(
        self,
        res: "bs_td.ListLensReviewImprovementsOutputTypeDef",
    ) -> "dc_td.ListLensReviewImprovementsOutput":
        return dc_td.ListLensReviewImprovementsOutput.make_one(res)

    def list_lens_reviews(
        self,
        res: "bs_td.ListLensReviewsOutputTypeDef",
    ) -> "dc_td.ListLensReviewsOutput":
        return dc_td.ListLensReviewsOutput.make_one(res)

    def list_lens_shares(
        self,
        res: "bs_td.ListLensSharesOutputTypeDef",
    ) -> "dc_td.ListLensSharesOutput":
        return dc_td.ListLensSharesOutput.make_one(res)

    def list_lenses(
        self,
        res: "bs_td.ListLensesOutputTypeDef",
    ) -> "dc_td.ListLensesOutput":
        return dc_td.ListLensesOutput.make_one(res)

    def list_milestones(
        self,
        res: "bs_td.ListMilestonesOutputTypeDef",
    ) -> "dc_td.ListMilestonesOutput":
        return dc_td.ListMilestonesOutput.make_one(res)

    def list_notifications(
        self,
        res: "bs_td.ListNotificationsOutputTypeDef",
    ) -> "dc_td.ListNotificationsOutput":
        return dc_td.ListNotificationsOutput.make_one(res)

    def list_profile_notifications(
        self,
        res: "bs_td.ListProfileNotificationsOutputTypeDef",
    ) -> "dc_td.ListProfileNotificationsOutput":
        return dc_td.ListProfileNotificationsOutput.make_one(res)

    def list_profile_shares(
        self,
        res: "bs_td.ListProfileSharesOutputTypeDef",
    ) -> "dc_td.ListProfileSharesOutput":
        return dc_td.ListProfileSharesOutput.make_one(res)

    def list_profiles(
        self,
        res: "bs_td.ListProfilesOutputTypeDef",
    ) -> "dc_td.ListProfilesOutput":
        return dc_td.ListProfilesOutput.make_one(res)

    def list_review_template_answers(
        self,
        res: "bs_td.ListReviewTemplateAnswersOutputTypeDef",
    ) -> "dc_td.ListReviewTemplateAnswersOutput":
        return dc_td.ListReviewTemplateAnswersOutput.make_one(res)

    def list_review_templates(
        self,
        res: "bs_td.ListReviewTemplatesOutputTypeDef",
    ) -> "dc_td.ListReviewTemplatesOutput":
        return dc_td.ListReviewTemplatesOutput.make_one(res)

    def list_share_invitations(
        self,
        res: "bs_td.ListShareInvitationsOutputTypeDef",
    ) -> "dc_td.ListShareInvitationsOutput":
        return dc_td.ListShareInvitationsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_template_shares(
        self,
        res: "bs_td.ListTemplateSharesOutputTypeDef",
    ) -> "dc_td.ListTemplateSharesOutput":
        return dc_td.ListTemplateSharesOutput.make_one(res)

    def list_workload_shares(
        self,
        res: "bs_td.ListWorkloadSharesOutputTypeDef",
    ) -> "dc_td.ListWorkloadSharesOutput":
        return dc_td.ListWorkloadSharesOutput.make_one(res)

    def list_workloads(
        self,
        res: "bs_td.ListWorkloadsOutputTypeDef",
    ) -> "dc_td.ListWorkloadsOutput":
        return dc_td.ListWorkloadsOutput.make_one(res)

    def update_answer(
        self,
        res: "bs_td.UpdateAnswerOutputTypeDef",
    ) -> "dc_td.UpdateAnswerOutput":
        return dc_td.UpdateAnswerOutput.make_one(res)

    def update_global_settings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_integration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_lens_review(
        self,
        res: "bs_td.UpdateLensReviewOutputTypeDef",
    ) -> "dc_td.UpdateLensReviewOutput":
        return dc_td.UpdateLensReviewOutput.make_one(res)

    def update_profile(
        self,
        res: "bs_td.UpdateProfileOutputTypeDef",
    ) -> "dc_td.UpdateProfileOutput":
        return dc_td.UpdateProfileOutput.make_one(res)

    def update_review_template(
        self,
        res: "bs_td.UpdateReviewTemplateOutputTypeDef",
    ) -> "dc_td.UpdateReviewTemplateOutput":
        return dc_td.UpdateReviewTemplateOutput.make_one(res)

    def update_review_template_answer(
        self,
        res: "bs_td.UpdateReviewTemplateAnswerOutputTypeDef",
    ) -> "dc_td.UpdateReviewTemplateAnswerOutput":
        return dc_td.UpdateReviewTemplateAnswerOutput.make_one(res)

    def update_review_template_lens_review(
        self,
        res: "bs_td.UpdateReviewTemplateLensReviewOutputTypeDef",
    ) -> "dc_td.UpdateReviewTemplateLensReviewOutput":
        return dc_td.UpdateReviewTemplateLensReviewOutput.make_one(res)

    def update_share_invitation(
        self,
        res: "bs_td.UpdateShareInvitationOutputTypeDef",
    ) -> "dc_td.UpdateShareInvitationOutput":
        return dc_td.UpdateShareInvitationOutput.make_one(res)

    def update_workload(
        self,
        res: "bs_td.UpdateWorkloadOutputTypeDef",
    ) -> "dc_td.UpdateWorkloadOutput":
        return dc_td.UpdateWorkloadOutput.make_one(res)

    def update_workload_share(
        self,
        res: "bs_td.UpdateWorkloadShareOutputTypeDef",
    ) -> "dc_td.UpdateWorkloadShareOutput":
        return dc_td.UpdateWorkloadShareOutput.make_one(res)

    def upgrade_lens_review(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def upgrade_profile_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def upgrade_review_template_lens_review(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


wellarchitected_caster = WELLARCHITECTEDCaster()
