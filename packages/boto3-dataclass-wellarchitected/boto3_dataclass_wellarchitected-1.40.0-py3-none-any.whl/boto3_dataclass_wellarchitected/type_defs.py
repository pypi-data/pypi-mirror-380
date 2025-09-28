# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_wellarchitected import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountJiraConfigurationInput:
    boto3_raw_data: "type_defs.AccountJiraConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    IssueManagementStatus = field("IssueManagementStatus")
    IssueManagementType = field("IssueManagementType")
    JiraProjectKey = field("JiraProjectKey")
    IntegrationStatus = field("IntegrationStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AccountJiraConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountJiraConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountJiraConfigurationOutput:
    boto3_raw_data: "type_defs.AccountJiraConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    IntegrationStatus = field("IntegrationStatus")
    IssueManagementStatus = field("IssueManagementStatus")
    IssueManagementType = field("IssueManagementType")
    Subdomain = field("Subdomain")
    JiraProjectKey = field("JiraProjectKey")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AccountJiraConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountJiraConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChoiceContent:
    boto3_raw_data: "type_defs.ChoiceContentTypeDef" = dataclasses.field()

    DisplayText = field("DisplayText")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChoiceContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChoiceContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChoiceAnswerSummary:
    boto3_raw_data: "type_defs.ChoiceAnswerSummaryTypeDef" = dataclasses.field()

    ChoiceId = field("ChoiceId")
    Status = field("Status")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChoiceAnswerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChoiceAnswerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JiraConfiguration:
    boto3_raw_data: "type_defs.JiraConfigurationTypeDef" = dataclasses.field()

    JiraIssueUrl = field("JiraIssueUrl")
    LastSyncedTime = field("LastSyncedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JiraConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JiraConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChoiceAnswer:
    boto3_raw_data: "type_defs.ChoiceAnswerTypeDef" = dataclasses.field()

    ChoiceId = field("ChoiceId")
    Status = field("Status")
    Reason = field("Reason")
    Notes = field("Notes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChoiceAnswerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChoiceAnswerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateLensesInput:
    boto3_raw_data: "type_defs.AssociateLensesInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAliases = field("LensAliases")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateLensesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateLensesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateProfilesInput:
    boto3_raw_data: "type_defs.AssociateProfilesInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    ProfileArns = field("ProfileArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateProfilesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateProfilesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BestPractice:
    boto3_raw_data: "type_defs.BestPracticeTypeDef" = dataclasses.field()

    ChoiceId = field("ChoiceId")
    ChoiceTitle = field("ChoiceTitle")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BestPracticeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BestPracticeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckDetail:
    boto3_raw_data: "type_defs.CheckDetailTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    Provider = field("Provider")
    LensArn = field("LensArn")
    PillarId = field("PillarId")
    QuestionId = field("QuestionId")
    ChoiceId = field("ChoiceId")
    Status = field("Status")
    AccountId = field("AccountId")
    FlaggedResources = field("FlaggedResources")
    Reason = field("Reason")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CheckDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CheckDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckSummary:
    boto3_raw_data: "type_defs.CheckSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Provider = field("Provider")
    Description = field("Description")
    UpdatedAt = field("UpdatedAt")
    LensArn = field("LensArn")
    PillarId = field("PillarId")
    QuestionId = field("QuestionId")
    ChoiceId = field("ChoiceId")
    Status = field("Status")
    AccountSummary = field("AccountSummary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CheckSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CheckSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChoiceImprovementPlan:
    boto3_raw_data: "type_defs.ChoiceImprovementPlanTypeDef" = dataclasses.field()

    ChoiceId = field("ChoiceId")
    DisplayText = field("DisplayText")
    ImprovementPlanUrl = field("ImprovementPlanUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChoiceImprovementPlanTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChoiceImprovementPlanTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChoiceUpdate:
    boto3_raw_data: "type_defs.ChoiceUpdateTypeDef" = dataclasses.field()

    Status = field("Status")
    Reason = field("Reason")
    Notes = field("Notes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChoiceUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChoiceUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLensShareInput:
    boto3_raw_data: "type_defs.CreateLensShareInputTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    SharedWith = field("SharedWith")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLensShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLensShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLensVersionInput:
    boto3_raw_data: "type_defs.CreateLensVersionInputTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    LensVersion = field("LensVersion")
    ClientRequestToken = field("ClientRequestToken")
    IsMajorVersion = field("IsMajorVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLensVersionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLensVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMilestoneInput:
    boto3_raw_data: "type_defs.CreateMilestoneInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    MilestoneName = field("MilestoneName")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMilestoneInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMilestoneInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileQuestionUpdate:
    boto3_raw_data: "type_defs.ProfileQuestionUpdateTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    SelectedChoiceIds = field("SelectedChoiceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileQuestionUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileQuestionUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileShareInput:
    boto3_raw_data: "type_defs.CreateProfileShareInputTypeDef" = dataclasses.field()

    ProfileArn = field("ProfileArn")
    SharedWith = field("SharedWith")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReviewTemplateInput:
    boto3_raw_data: "type_defs.CreateReviewTemplateInputTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    Description = field("Description")
    Lenses = field("Lenses")
    ClientRequestToken = field("ClientRequestToken")
    Notes = field("Notes")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReviewTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReviewTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateShareInput:
    boto3_raw_data: "type_defs.CreateTemplateShareInputTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")
    SharedWith = field("SharedWith")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadJiraConfigurationInput:
    boto3_raw_data: "type_defs.WorkloadJiraConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    IssueManagementStatus = field("IssueManagementStatus")
    IssueManagementType = field("IssueManagementType")
    JiraProjectKey = field("JiraProjectKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkloadJiraConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadJiraConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkloadShareInput:
    boto3_raw_data: "type_defs.CreateWorkloadShareInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    SharedWith = field("SharedWith")
    PermissionType = field("PermissionType")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkloadShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkloadShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLensInput:
    boto3_raw_data: "type_defs.DeleteLensInputTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    ClientRequestToken = field("ClientRequestToken")
    LensStatus = field("LensStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteLensInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteLensInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLensShareInput:
    boto3_raw_data: "type_defs.DeleteLensShareInputTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    LensAlias = field("LensAlias")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLensShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLensShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileInput:
    boto3_raw_data: "type_defs.DeleteProfileInputTypeDef" = dataclasses.field()

    ProfileArn = field("ProfileArn")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileShareInput:
    boto3_raw_data: "type_defs.DeleteProfileShareInputTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    ProfileArn = field("ProfileArn")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReviewTemplateInput:
    boto3_raw_data: "type_defs.DeleteReviewTemplateInputTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReviewTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReviewTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTemplateShareInput:
    boto3_raw_data: "type_defs.DeleteTemplateShareInputTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    TemplateArn = field("TemplateArn")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTemplateShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTemplateShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkloadInput:
    boto3_raw_data: "type_defs.DeleteWorkloadInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkloadInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkloadInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkloadShareInput:
    boto3_raw_data: "type_defs.DeleteWorkloadShareInputTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    WorkloadId = field("WorkloadId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkloadShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkloadShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateLensesInput:
    boto3_raw_data: "type_defs.DisassociateLensesInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAliases = field("LensAliases")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateLensesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateLensesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateProfilesInput:
    boto3_raw_data: "type_defs.DisassociateProfilesInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    ProfileArns = field("ProfileArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateProfilesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateProfilesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportLensInput:
    boto3_raw_data: "type_defs.ExportLensInputTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    LensVersion = field("LensVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportLensInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportLensInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnswerInput:
    boto3_raw_data: "type_defs.GetAnswerInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    QuestionId = field("QuestionId")
    MilestoneNumber = field("MilestoneNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAnswerInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAnswerInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConsolidatedReportInput:
    boto3_raw_data: "type_defs.GetConsolidatedReportInputTypeDef" = dataclasses.field()

    Format = field("Format")
    IncludeSharedResources = field("IncludeSharedResources")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConsolidatedReportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConsolidatedReportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLensInput:
    boto3_raw_data: "type_defs.GetLensInputTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    LensVersion = field("LensVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLensInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetLensInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Lens:
    boto3_raw_data: "type_defs.LensTypeDef" = dataclasses.field()

    LensArn = field("LensArn")
    LensVersion = field("LensVersion")
    Name = field("Name")
    Description = field("Description")
    Owner = field("Owner")
    ShareInvitationId = field("ShareInvitationId")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LensTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LensTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLensReviewInput:
    boto3_raw_data: "type_defs.GetLensReviewInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    MilestoneNumber = field("MilestoneNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLensReviewInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLensReviewInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLensReviewReportInput:
    boto3_raw_data: "type_defs.GetLensReviewReportInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    MilestoneNumber = field("MilestoneNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLensReviewReportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLensReviewReportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LensReviewReport:
    boto3_raw_data: "type_defs.LensReviewReportTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    LensArn = field("LensArn")
    Base64String = field("Base64String")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LensReviewReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LensReviewReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLensVersionDifferenceInput:
    boto3_raw_data: "type_defs.GetLensVersionDifferenceInputTypeDef" = (
        dataclasses.field()
    )

    LensAlias = field("LensAlias")
    BaseLensVersion = field("BaseLensVersion")
    TargetLensVersion = field("TargetLensVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLensVersionDifferenceInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLensVersionDifferenceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMilestoneInput:
    boto3_raw_data: "type_defs.GetMilestoneInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    MilestoneNumber = field("MilestoneNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMilestoneInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMilestoneInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileInput:
    boto3_raw_data: "type_defs.GetProfileInputTypeDef" = dataclasses.field()

    ProfileArn = field("ProfileArn")
    ProfileVersion = field("ProfileVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetProfileInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetProfileInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReviewTemplateAnswerInput:
    boto3_raw_data: "type_defs.GetReviewTemplateAnswerInputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    LensAlias = field("LensAlias")
    QuestionId = field("QuestionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReviewTemplateAnswerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReviewTemplateAnswerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReviewTemplateInput:
    boto3_raw_data: "type_defs.GetReviewTemplateInputTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReviewTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReviewTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReviewTemplateLensReviewInput:
    boto3_raw_data: "type_defs.GetReviewTemplateLensReviewInputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    LensAlias = field("LensAlias")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReviewTemplateLensReviewInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReviewTemplateLensReviewInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewTemplate:
    boto3_raw_data: "type_defs.ReviewTemplateTypeDef" = dataclasses.field()

    Description = field("Description")
    Lenses = field("Lenses")
    Notes = field("Notes")
    QuestionCounts = field("QuestionCounts")
    Owner = field("Owner")
    UpdatedAt = field("UpdatedAt")
    TemplateArn = field("TemplateArn")
    TemplateName = field("TemplateName")
    Tags = field("Tags")
    UpdateStatus = field("UpdateStatus")
    ShareInvitationId = field("ShareInvitationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReviewTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReviewTemplateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadInput:
    boto3_raw_data: "type_defs.GetWorkloadInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetWorkloadInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportLensInput:
    boto3_raw_data: "type_defs.ImportLensInputTypeDef" = dataclasses.field()

    JSONString = field("JSONString")
    ClientRequestToken = field("ClientRequestToken")
    LensAlias = field("LensAlias")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportLensInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportLensInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectedPillarOutput:
    boto3_raw_data: "type_defs.SelectedPillarOutputTypeDef" = dataclasses.field()

    PillarId = field("PillarId")
    SelectedQuestionIds = field("SelectedQuestionIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelectedPillarOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectedPillarOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectedPillar:
    boto3_raw_data: "type_defs.SelectedPillarTypeDef" = dataclasses.field()

    PillarId = field("PillarId")
    SelectedQuestionIds = field("SelectedQuestionIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SelectedPillarTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SelectedPillarTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadProfile:
    boto3_raw_data: "type_defs.WorkloadProfileTypeDef" = dataclasses.field()

    ProfileArn = field("ProfileArn")
    ProfileVersion = field("ProfileVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkloadProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkloadProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PillarReviewSummary:
    boto3_raw_data: "type_defs.PillarReviewSummaryTypeDef" = dataclasses.field()

    PillarId = field("PillarId")
    PillarName = field("PillarName")
    Notes = field("Notes")
    RiskCounts = field("RiskCounts")
    PrioritizedRiskCounts = field("PrioritizedRiskCounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PillarReviewSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PillarReviewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LensShareSummary:
    boto3_raw_data: "type_defs.LensShareSummaryTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    SharedWith = field("SharedWith")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LensShareSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LensShareSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LensSummary:
    boto3_raw_data: "type_defs.LensSummaryTypeDef" = dataclasses.field()

    LensArn = field("LensArn")
    LensAlias = field("LensAlias")
    LensName = field("LensName")
    LensType = field("LensType")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    LensVersion = field("LensVersion")
    Owner = field("Owner")
    LensStatus = field("LensStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LensSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LensSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LensUpgradeSummary:
    boto3_raw_data: "type_defs.LensUpgradeSummaryTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    WorkloadName = field("WorkloadName")
    LensAlias = field("LensAlias")
    LensArn = field("LensArn")
    CurrentLensVersion = field("CurrentLensVersion")
    LatestLensVersion = field("LatestLensVersion")
    ResourceArn = field("ResourceArn")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LensUpgradeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LensUpgradeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnswersInput:
    boto3_raw_data: "type_defs.ListAnswersInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    PillarId = field("PillarId")
    MilestoneNumber = field("MilestoneNumber")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    QuestionPriority = field("QuestionPriority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAnswersInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnswersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCheckDetailsInput:
    boto3_raw_data: "type_defs.ListCheckDetailsInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensArn = field("LensArn")
    PillarId = field("PillarId")
    QuestionId = field("QuestionId")
    ChoiceId = field("ChoiceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCheckDetailsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCheckDetailsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCheckSummariesInput:
    boto3_raw_data: "type_defs.ListCheckSummariesInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensArn = field("LensArn")
    PillarId = field("PillarId")
    QuestionId = field("QuestionId")
    ChoiceId = field("ChoiceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCheckSummariesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCheckSummariesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLensReviewImprovementsInput:
    boto3_raw_data: "type_defs.ListLensReviewImprovementsInputTypeDef" = (
        dataclasses.field()
    )

    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    PillarId = field("PillarId")
    MilestoneNumber = field("MilestoneNumber")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    QuestionPriority = field("QuestionPriority")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLensReviewImprovementsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLensReviewImprovementsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLensReviewsInput:
    boto3_raw_data: "type_defs.ListLensReviewsInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    MilestoneNumber = field("MilestoneNumber")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLensReviewsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLensReviewsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLensSharesInput:
    boto3_raw_data: "type_defs.ListLensSharesInputTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    SharedWithPrefix = field("SharedWithPrefix")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLensSharesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLensSharesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLensesInput:
    boto3_raw_data: "type_defs.ListLensesInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    LensType = field("LensType")
    LensStatus = field("LensStatus")
    LensName = field("LensName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListLensesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListLensesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMilestonesInput:
    boto3_raw_data: "type_defs.ListMilestonesInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMilestonesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMilestonesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationsInput:
    boto3_raw_data: "type_defs.ListNotificationsInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotificationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileNotificationsInput:
    boto3_raw_data: "type_defs.ListProfileNotificationsInputTypeDef" = (
        dataclasses.field()
    )

    WorkloadId = field("WorkloadId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProfileNotificationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileNotificationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileNotificationSummary:
    boto3_raw_data: "type_defs.ProfileNotificationSummaryTypeDef" = dataclasses.field()

    CurrentProfileVersion = field("CurrentProfileVersion")
    LatestProfileVersion = field("LatestProfileVersion")
    Type = field("Type")
    ProfileArn = field("ProfileArn")
    ProfileName = field("ProfileName")
    WorkloadId = field("WorkloadId")
    WorkloadName = field("WorkloadName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileNotificationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileNotificationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileSharesInput:
    boto3_raw_data: "type_defs.ListProfileSharesInputTypeDef" = dataclasses.field()

    ProfileArn = field("ProfileArn")
    SharedWithPrefix = field("SharedWithPrefix")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfileSharesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileSharesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileShareSummary:
    boto3_raw_data: "type_defs.ProfileShareSummaryTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    SharedWith = field("SharedWith")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileShareSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileShareSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilesInput:
    boto3_raw_data: "type_defs.ListProfilesInputTypeDef" = dataclasses.field()

    ProfileNamePrefix = field("ProfileNamePrefix")
    ProfileOwnerType = field("ProfileOwnerType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListProfilesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileSummary:
    boto3_raw_data: "type_defs.ProfileSummaryTypeDef" = dataclasses.field()

    ProfileArn = field("ProfileArn")
    ProfileVersion = field("ProfileVersion")
    ProfileName = field("ProfileName")
    ProfileDescription = field("ProfileDescription")
    Owner = field("Owner")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfileSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReviewTemplateAnswersInput:
    boto3_raw_data: "type_defs.ListReviewTemplateAnswersInputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    LensAlias = field("LensAlias")
    PillarId = field("PillarId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReviewTemplateAnswersInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReviewTemplateAnswersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReviewTemplatesInput:
    boto3_raw_data: "type_defs.ListReviewTemplatesInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReviewTemplatesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReviewTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewTemplateSummary:
    boto3_raw_data: "type_defs.ReviewTemplateSummaryTypeDef" = dataclasses.field()

    Description = field("Description")
    Lenses = field("Lenses")
    Owner = field("Owner")
    UpdatedAt = field("UpdatedAt")
    TemplateArn = field("TemplateArn")
    TemplateName = field("TemplateName")
    UpdateStatus = field("UpdateStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReviewTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReviewTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListShareInvitationsInput:
    boto3_raw_data: "type_defs.ListShareInvitationsInputTypeDef" = dataclasses.field()

    WorkloadNamePrefix = field("WorkloadNamePrefix")
    LensNamePrefix = field("LensNamePrefix")
    ShareResourceType = field("ShareResourceType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ProfileNamePrefix = field("ProfileNamePrefix")
    TemplateNamePrefix = field("TemplateNamePrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListShareInvitationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListShareInvitationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareInvitationSummary:
    boto3_raw_data: "type_defs.ShareInvitationSummaryTypeDef" = dataclasses.field()

    ShareInvitationId = field("ShareInvitationId")
    SharedBy = field("SharedBy")
    SharedWith = field("SharedWith")
    PermissionType = field("PermissionType")
    ShareResourceType = field("ShareResourceType")
    WorkloadName = field("WorkloadName")
    WorkloadId = field("WorkloadId")
    LensName = field("LensName")
    LensArn = field("LensArn")
    ProfileName = field("ProfileName")
    ProfileArn = field("ProfileArn")
    TemplateName = field("TemplateName")
    TemplateArn = field("TemplateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShareInvitationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShareInvitationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    WorkloadArn = field("WorkloadArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateSharesInput:
    boto3_raw_data: "type_defs.ListTemplateSharesInputTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")
    SharedWithPrefix = field("SharedWithPrefix")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplateSharesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateSharesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateShareSummary:
    boto3_raw_data: "type_defs.TemplateShareSummaryTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    SharedWith = field("SharedWith")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateShareSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateShareSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadSharesInput:
    boto3_raw_data: "type_defs.ListWorkloadSharesInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    SharedWithPrefix = field("SharedWithPrefix")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkloadSharesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadSharesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadShareSummary:
    boto3_raw_data: "type_defs.WorkloadShareSummaryTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    SharedWith = field("SharedWith")
    PermissionType = field("PermissionType")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkloadShareSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadShareSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadsInput:
    boto3_raw_data: "type_defs.ListWorkloadsInputTypeDef" = dataclasses.field()

    WorkloadNamePrefix = field("WorkloadNamePrefix")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkloadsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuestionDifference:
    boto3_raw_data: "type_defs.QuestionDifferenceTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    QuestionTitle = field("QuestionTitle")
    DifferenceStatus = field("DifferenceStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuestionDifferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuestionDifferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileChoice:
    boto3_raw_data: "type_defs.ProfileChoiceTypeDef" = dataclasses.field()

    ChoiceId = field("ChoiceId")
    ChoiceTitle = field("ChoiceTitle")
    ChoiceDescription = field("ChoiceDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileChoiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfileChoiceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileTemplateChoice:
    boto3_raw_data: "type_defs.ProfileTemplateChoiceTypeDef" = dataclasses.field()

    ChoiceId = field("ChoiceId")
    ChoiceTitle = field("ChoiceTitle")
    ChoiceDescription = field("ChoiceDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileTemplateChoiceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileTemplateChoiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewTemplatePillarReviewSummary:
    boto3_raw_data: "type_defs.ReviewTemplatePillarReviewSummaryTypeDef" = (
        dataclasses.field()
    )

    PillarId = field("PillarId")
    PillarName = field("PillarName")
    Notes = field("Notes")
    QuestionCounts = field("QuestionCounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReviewTemplatePillarReviewSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReviewTemplatePillarReviewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareInvitation:
    boto3_raw_data: "type_defs.ShareInvitationTypeDef" = dataclasses.field()

    ShareInvitationId = field("ShareInvitationId")
    ShareResourceType = field("ShareResourceType")
    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    LensArn = field("LensArn")
    ProfileArn = field("ProfileArn")
    TemplateArn = field("TemplateArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShareInvitationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShareInvitationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    WorkloadArn = field("WorkloadArn")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    WorkloadArn = field("WorkloadArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntegrationInput:
    boto3_raw_data: "type_defs.UpdateIntegrationInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    ClientRequestToken = field("ClientRequestToken")
    IntegratingService = field("IntegratingService")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIntegrationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntegrationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReviewTemplateInput:
    boto3_raw_data: "type_defs.UpdateReviewTemplateInputTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")
    TemplateName = field("TemplateName")
    Description = field("Description")
    Notes = field("Notes")
    LensesToAssociate = field("LensesToAssociate")
    LensesToDisassociate = field("LensesToDisassociate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReviewTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReviewTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReviewTemplateLensReviewInput:
    boto3_raw_data: "type_defs.UpdateReviewTemplateLensReviewInputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    LensAlias = field("LensAlias")
    LensNotes = field("LensNotes")
    PillarNotes = field("PillarNotes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateReviewTemplateLensReviewInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReviewTemplateLensReviewInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateShareInvitationInput:
    boto3_raw_data: "type_defs.UpdateShareInvitationInputTypeDef" = dataclasses.field()

    ShareInvitationId = field("ShareInvitationId")
    ShareInvitationAction = field("ShareInvitationAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateShareInvitationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateShareInvitationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadShareInput:
    boto3_raw_data: "type_defs.UpdateWorkloadShareInputTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    WorkloadId = field("WorkloadId")
    PermissionType = field("PermissionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkloadShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadShare:
    boto3_raw_data: "type_defs.WorkloadShareTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    SharedBy = field("SharedBy")
    SharedWith = field("SharedWith")
    PermissionType = field("PermissionType")
    Status = field("Status")
    WorkloadName = field("WorkloadName")
    WorkloadId = field("WorkloadId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkloadShareTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkloadShareTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeLensReviewInput:
    boto3_raw_data: "type_defs.UpgradeLensReviewInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    MilestoneName = field("MilestoneName")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpgradeLensReviewInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeLensReviewInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeProfileVersionInput:
    boto3_raw_data: "type_defs.UpgradeProfileVersionInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    ProfileArn = field("ProfileArn")
    MilestoneName = field("MilestoneName")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpgradeProfileVersionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeProfileVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeReviewTemplateLensReviewInput:
    boto3_raw_data: "type_defs.UpgradeReviewTemplateLensReviewInputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    LensAlias = field("LensAlias")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpgradeReviewTemplateLensReviewInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeReviewTemplateLensReviewInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadDiscoveryConfigOutput:
    boto3_raw_data: "type_defs.WorkloadDiscoveryConfigOutputTypeDef" = (
        dataclasses.field()
    )

    TrustedAdvisorIntegrationStatus = field("TrustedAdvisorIntegrationStatus")
    WorkloadResourceDefinition = field("WorkloadResourceDefinition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkloadDiscoveryConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadDiscoveryConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadDiscoveryConfig:
    boto3_raw_data: "type_defs.WorkloadDiscoveryConfigTypeDef" = dataclasses.field()

    TrustedAdvisorIntegrationStatus = field("TrustedAdvisorIntegrationStatus")
    WorkloadResourceDefinition = field("WorkloadResourceDefinition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkloadDiscoveryConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadDiscoveryConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadJiraConfigurationOutput:
    boto3_raw_data: "type_defs.WorkloadJiraConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    IssueManagementStatus = field("IssueManagementStatus")
    IssueManagementType = field("IssueManagementType")
    JiraProjectKey = field("JiraProjectKey")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkloadJiraConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadJiraConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalSettingsInput:
    boto3_raw_data: "type_defs.UpdateGlobalSettingsInputTypeDef" = dataclasses.field()

    OrganizationSharingStatus = field("OrganizationSharingStatus")
    DiscoveryIntegrationStatus = field("DiscoveryIntegrationStatus")

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return AccountJiraConfigurationInput.make_one(
            self.boto3_raw_data["JiraConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlobalSettingsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalResources:
    boto3_raw_data: "type_defs.AdditionalResourcesTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Content(self):  # pragma: no cover
        return ChoiceContent.make_many(self.boto3_raw_data["Content"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdditionalResourcesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalResourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuestionMetric:
    boto3_raw_data: "type_defs.QuestionMetricTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    Risk = field("Risk")

    @cached_property
    def BestPractices(self):  # pragma: no cover
        return BestPractice.make_many(self.boto3_raw_data["BestPractices"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QuestionMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QuestionMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImprovementSummary:
    boto3_raw_data: "type_defs.ImprovementSummaryTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    PillarId = field("PillarId")
    QuestionTitle = field("QuestionTitle")
    Risk = field("Risk")
    ImprovementPlanUrl = field("ImprovementPlanUrl")

    @cached_property
    def ImprovementPlans(self):  # pragma: no cover
        return ChoiceImprovementPlan.make_many(self.boto3_raw_data["ImprovementPlans"])

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return JiraConfiguration.make_one(self.boto3_raw_data["JiraConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImprovementSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImprovementSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnswerInput:
    boto3_raw_data: "type_defs.UpdateAnswerInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    QuestionId = field("QuestionId")
    SelectedChoices = field("SelectedChoices")
    ChoiceUpdates = field("ChoiceUpdates")
    Notes = field("Notes")
    IsApplicable = field("IsApplicable")
    Reason = field("Reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAnswerInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnswerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReviewTemplateAnswerInput:
    boto3_raw_data: "type_defs.UpdateReviewTemplateAnswerInputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    LensAlias = field("LensAlias")
    QuestionId = field("QuestionId")
    SelectedChoices = field("SelectedChoices")
    ChoiceUpdates = field("ChoiceUpdates")
    Notes = field("Notes")
    IsApplicable = field("IsApplicable")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateReviewTemplateAnswerInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReviewTemplateAnswerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLensShareOutput:
    boto3_raw_data: "type_defs.CreateLensShareOutputTypeDef" = dataclasses.field()

    ShareId = field("ShareId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLensShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLensShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLensVersionOutput:
    boto3_raw_data: "type_defs.CreateLensVersionOutputTypeDef" = dataclasses.field()

    LensArn = field("LensArn")
    LensVersion = field("LensVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLensVersionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLensVersionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMilestoneOutput:
    boto3_raw_data: "type_defs.CreateMilestoneOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    MilestoneNumber = field("MilestoneNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMilestoneOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMilestoneOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileOutput:
    boto3_raw_data: "type_defs.CreateProfileOutputTypeDef" = dataclasses.field()

    ProfileArn = field("ProfileArn")
    ProfileVersion = field("ProfileVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileShareOutput:
    boto3_raw_data: "type_defs.CreateProfileShareOutputTypeDef" = dataclasses.field()

    ShareId = field("ShareId")
    ProfileArn = field("ProfileArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReviewTemplateOutput:
    boto3_raw_data: "type_defs.CreateReviewTemplateOutputTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReviewTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReviewTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateShareOutput:
    boto3_raw_data: "type_defs.CreateTemplateShareOutputTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")
    ShareId = field("ShareId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkloadOutput:
    boto3_raw_data: "type_defs.CreateWorkloadOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    WorkloadArn = field("WorkloadArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkloadOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkloadShareOutput:
    boto3_raw_data: "type_defs.CreateWorkloadShareOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    ShareId = field("ShareId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkloadShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkloadShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportLensOutput:
    boto3_raw_data: "type_defs.ExportLensOutputTypeDef" = dataclasses.field()

    LensJSON = field("LensJSON")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportLensOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportLensOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGlobalSettingsOutput:
    boto3_raw_data: "type_defs.GetGlobalSettingsOutputTypeDef" = dataclasses.field()

    OrganizationSharingStatus = field("OrganizationSharingStatus")
    DiscoveryIntegrationStatus = field("DiscoveryIntegrationStatus")

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return AccountJiraConfigurationOutput.make_one(
            self.boto3_raw_data["JiraConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGlobalSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGlobalSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportLensOutput:
    boto3_raw_data: "type_defs.ImportLensOutputTypeDef" = dataclasses.field()

    LensArn = field("LensArn")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportLensOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportLensOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCheckDetailsOutput:
    boto3_raw_data: "type_defs.ListCheckDetailsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CheckDetails(self):  # pragma: no cover
        return CheckDetail.make_many(self.boto3_raw_data["CheckDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCheckDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCheckDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCheckSummariesOutput:
    boto3_raw_data: "type_defs.ListCheckSummariesOutputTypeDef" = dataclasses.field()

    @cached_property
    def CheckSummaries(self):  # pragma: no cover
        return CheckSummary.make_many(self.boto3_raw_data["CheckSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCheckSummariesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCheckSummariesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileInput:
    boto3_raw_data: "type_defs.CreateProfileInputTypeDef" = dataclasses.field()

    ProfileName = field("ProfileName")
    ProfileDescription = field("ProfileDescription")

    @cached_property
    def ProfileQuestions(self):  # pragma: no cover
        return ProfileQuestionUpdate.make_many(self.boto3_raw_data["ProfileQuestions"])

    ClientRequestToken = field("ClientRequestToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfileInput:
    boto3_raw_data: "type_defs.UpdateProfileInputTypeDef" = dataclasses.field()

    ProfileArn = field("ProfileArn")
    ProfileDescription = field("ProfileDescription")

    @cached_property
    def ProfileQuestions(self):  # pragma: no cover
        return ProfileQuestionUpdate.make_many(self.boto3_raw_data["ProfileQuestions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLensOutput:
    boto3_raw_data: "type_defs.GetLensOutputTypeDef" = dataclasses.field()

    @cached_property
    def Lens(self):  # pragma: no cover
        return Lens.make_one(self.boto3_raw_data["Lens"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLensOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetLensOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLensReviewReportOutput:
    boto3_raw_data: "type_defs.GetLensReviewReportOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    MilestoneNumber = field("MilestoneNumber")

    @cached_property
    def LensReviewReport(self):  # pragma: no cover
        return LensReviewReport.make_one(self.boto3_raw_data["LensReviewReport"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLensReviewReportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLensReviewReportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReviewTemplateOutput:
    boto3_raw_data: "type_defs.GetReviewTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def ReviewTemplate(self):  # pragma: no cover
        return ReviewTemplate.make_one(self.boto3_raw_data["ReviewTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReviewTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReviewTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReviewTemplateOutput:
    boto3_raw_data: "type_defs.UpdateReviewTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def ReviewTemplate(self):  # pragma: no cover
        return ReviewTemplate.make_one(self.boto3_raw_data["ReviewTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReviewTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReviewTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JiraSelectedQuestionConfigurationOutput:
    boto3_raw_data: "type_defs.JiraSelectedQuestionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SelectedPillars(self):  # pragma: no cover
        return SelectedPillarOutput.make_many(self.boto3_raw_data["SelectedPillars"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.JiraSelectedQuestionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JiraSelectedQuestionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JiraSelectedQuestionConfiguration:
    boto3_raw_data: "type_defs.JiraSelectedQuestionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SelectedPillars(self):  # pragma: no cover
        return SelectedPillar.make_many(self.boto3_raw_data["SelectedPillars"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.JiraSelectedQuestionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JiraSelectedQuestionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LensReviewSummary:
    boto3_raw_data: "type_defs.LensReviewSummaryTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    LensArn = field("LensArn")
    LensVersion = field("LensVersion")
    LensName = field("LensName")
    LensStatus = field("LensStatus")
    UpdatedAt = field("UpdatedAt")
    RiskCounts = field("RiskCounts")

    @cached_property
    def Profiles(self):  # pragma: no cover
        return WorkloadProfile.make_many(self.boto3_raw_data["Profiles"])

    PrioritizedRiskCounts = field("PrioritizedRiskCounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LensReviewSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LensReviewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadSummary:
    boto3_raw_data: "type_defs.WorkloadSummaryTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    WorkloadArn = field("WorkloadArn")
    WorkloadName = field("WorkloadName")
    Owner = field("Owner")
    UpdatedAt = field("UpdatedAt")
    Lenses = field("Lenses")
    RiskCounts = field("RiskCounts")
    ImprovementStatus = field("ImprovementStatus")

    @cached_property
    def Profiles(self):  # pragma: no cover
        return WorkloadProfile.make_many(self.boto3_raw_data["Profiles"])

    PrioritizedRiskCounts = field("PrioritizedRiskCounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkloadSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkloadSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLensSharesOutput:
    boto3_raw_data: "type_defs.ListLensSharesOutputTypeDef" = dataclasses.field()

    @cached_property
    def LensShareSummaries(self):  # pragma: no cover
        return LensShareSummary.make_many(self.boto3_raw_data["LensShareSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLensSharesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLensSharesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLensesOutput:
    boto3_raw_data: "type_defs.ListLensesOutputTypeDef" = dataclasses.field()

    @cached_property
    def LensSummaries(self):  # pragma: no cover
        return LensSummary.make_many(self.boto3_raw_data["LensSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListLensesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLensesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationSummary:
    boto3_raw_data: "type_defs.NotificationSummaryTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def LensUpgradeSummary(self):  # pragma: no cover
        return LensUpgradeSummary.make_one(self.boto3_raw_data["LensUpgradeSummary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileNotificationsOutput:
    boto3_raw_data: "type_defs.ListProfileNotificationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NotificationSummaries(self):  # pragma: no cover
        return ProfileNotificationSummary.make_many(
            self.boto3_raw_data["NotificationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProfileNotificationsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileNotificationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileSharesOutput:
    boto3_raw_data: "type_defs.ListProfileSharesOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProfileShareSummaries(self):  # pragma: no cover
        return ProfileShareSummary.make_many(
            self.boto3_raw_data["ProfileShareSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfileSharesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileSharesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilesOutput:
    boto3_raw_data: "type_defs.ListProfilesOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProfileSummaries(self):  # pragma: no cover
        return ProfileSummary.make_many(self.boto3_raw_data["ProfileSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReviewTemplatesOutput:
    boto3_raw_data: "type_defs.ListReviewTemplatesOutputTypeDef" = dataclasses.field()

    @cached_property
    def ReviewTemplates(self):  # pragma: no cover
        return ReviewTemplateSummary.make_many(self.boto3_raw_data["ReviewTemplates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReviewTemplatesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReviewTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListShareInvitationsOutput:
    boto3_raw_data: "type_defs.ListShareInvitationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ShareInvitationSummaries(self):  # pragma: no cover
        return ShareInvitationSummary.make_many(
            self.boto3_raw_data["ShareInvitationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListShareInvitationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListShareInvitationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateSharesOutput:
    boto3_raw_data: "type_defs.ListTemplateSharesOutputTypeDef" = dataclasses.field()

    TemplateArn = field("TemplateArn")

    @cached_property
    def TemplateShareSummaries(self):  # pragma: no cover
        return TemplateShareSummary.make_many(
            self.boto3_raw_data["TemplateShareSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplateSharesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateSharesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadSharesOutput:
    boto3_raw_data: "type_defs.ListWorkloadSharesOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")

    @cached_property
    def WorkloadShareSummaries(self):  # pragma: no cover
        return WorkloadShareSummary.make_many(
            self.boto3_raw_data["WorkloadShareSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkloadSharesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadSharesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PillarDifference:
    boto3_raw_data: "type_defs.PillarDifferenceTypeDef" = dataclasses.field()

    PillarId = field("PillarId")
    PillarName = field("PillarName")
    DifferenceStatus = field("DifferenceStatus")

    @cached_property
    def QuestionDifferences(self):  # pragma: no cover
        return QuestionDifference.make_many(self.boto3_raw_data["QuestionDifferences"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PillarDifferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PillarDifferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileQuestion:
    boto3_raw_data: "type_defs.ProfileQuestionTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    QuestionTitle = field("QuestionTitle")
    QuestionDescription = field("QuestionDescription")

    @cached_property
    def QuestionChoices(self):  # pragma: no cover
        return ProfileChoice.make_many(self.boto3_raw_data["QuestionChoices"])

    SelectedChoiceIds = field("SelectedChoiceIds")
    MinSelectedChoices = field("MinSelectedChoices")
    MaxSelectedChoices = field("MaxSelectedChoices")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileQuestionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfileQuestionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileTemplateQuestion:
    boto3_raw_data: "type_defs.ProfileTemplateQuestionTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    QuestionTitle = field("QuestionTitle")
    QuestionDescription = field("QuestionDescription")

    @cached_property
    def QuestionChoices(self):  # pragma: no cover
        return ProfileTemplateChoice.make_many(self.boto3_raw_data["QuestionChoices"])

    MinSelectedChoices = field("MinSelectedChoices")
    MaxSelectedChoices = field("MaxSelectedChoices")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileTemplateQuestionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileTemplateQuestionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewTemplateLensReview:
    boto3_raw_data: "type_defs.ReviewTemplateLensReviewTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    LensArn = field("LensArn")
    LensVersion = field("LensVersion")
    LensName = field("LensName")
    LensStatus = field("LensStatus")

    @cached_property
    def PillarReviewSummaries(self):  # pragma: no cover
        return ReviewTemplatePillarReviewSummary.make_many(
            self.boto3_raw_data["PillarReviewSummaries"]
        )

    UpdatedAt = field("UpdatedAt")
    Notes = field("Notes")
    QuestionCounts = field("QuestionCounts")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReviewTemplateLensReviewTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReviewTemplateLensReviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateShareInvitationOutput:
    boto3_raw_data: "type_defs.UpdateShareInvitationOutputTypeDef" = dataclasses.field()

    @cached_property
    def ShareInvitation(self):  # pragma: no cover
        return ShareInvitation.make_one(self.boto3_raw_data["ShareInvitation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateShareInvitationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateShareInvitationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadShareOutput:
    boto3_raw_data: "type_defs.UpdateWorkloadShareOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")

    @cached_property
    def WorkloadShare(self):  # pragma: no cover
        return WorkloadShare.make_one(self.boto3_raw_data["WorkloadShare"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkloadShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Workload:
    boto3_raw_data: "type_defs.WorkloadTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    WorkloadArn = field("WorkloadArn")
    WorkloadName = field("WorkloadName")
    Description = field("Description")
    Environment = field("Environment")
    UpdatedAt = field("UpdatedAt")
    AccountIds = field("AccountIds")
    AwsRegions = field("AwsRegions")
    NonAwsRegions = field("NonAwsRegions")
    ArchitecturalDesign = field("ArchitecturalDesign")
    ReviewOwner = field("ReviewOwner")
    ReviewRestrictionDate = field("ReviewRestrictionDate")
    IsReviewOwnerUpdateAcknowledged = field("IsReviewOwnerUpdateAcknowledged")
    IndustryType = field("IndustryType")
    Industry = field("Industry")
    Notes = field("Notes")
    ImprovementStatus = field("ImprovementStatus")
    RiskCounts = field("RiskCounts")
    PillarPriorities = field("PillarPriorities")
    Lenses = field("Lenses")
    Owner = field("Owner")
    ShareInvitationId = field("ShareInvitationId")
    Tags = field("Tags")

    @cached_property
    def DiscoveryConfig(self):  # pragma: no cover
        return WorkloadDiscoveryConfigOutput.make_one(
            self.boto3_raw_data["DiscoveryConfig"]
        )

    Applications = field("Applications")

    @cached_property
    def Profiles(self):  # pragma: no cover
        return WorkloadProfile.make_many(self.boto3_raw_data["Profiles"])

    PrioritizedRiskCounts = field("PrioritizedRiskCounts")

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return WorkloadJiraConfigurationOutput.make_one(
            self.boto3_raw_data["JiraConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkloadTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Choice:
    boto3_raw_data: "type_defs.ChoiceTypeDef" = dataclasses.field()

    ChoiceId = field("ChoiceId")
    Title = field("Title")
    Description = field("Description")

    @cached_property
    def HelpfulResource(self):  # pragma: no cover
        return ChoiceContent.make_one(self.boto3_raw_data["HelpfulResource"])

    @cached_property
    def ImprovementPlan(self):  # pragma: no cover
        return ChoiceContent.make_one(self.boto3_raw_data["ImprovementPlan"])

    @cached_property
    def AdditionalResources(self):  # pragma: no cover
        return AdditionalResources.make_many(self.boto3_raw_data["AdditionalResources"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChoiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChoiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PillarMetric:
    boto3_raw_data: "type_defs.PillarMetricTypeDef" = dataclasses.field()

    PillarId = field("PillarId")
    RiskCounts = field("RiskCounts")

    @cached_property
    def Questions(self):  # pragma: no cover
        return QuestionMetric.make_many(self.boto3_raw_data["Questions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PillarMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PillarMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLensReviewImprovementsOutput:
    boto3_raw_data: "type_defs.ListLensReviewImprovementsOutputTypeDef" = (
        dataclasses.field()
    )

    WorkloadId = field("WorkloadId")
    MilestoneNumber = field("MilestoneNumber")
    LensAlias = field("LensAlias")
    LensArn = field("LensArn")

    @cached_property
    def ImprovementSummaries(self):  # pragma: no cover
        return ImprovementSummary.make_many(self.boto3_raw_data["ImprovementSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLensReviewImprovementsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLensReviewImprovementsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LensReview:
    boto3_raw_data: "type_defs.LensReviewTypeDef" = dataclasses.field()

    LensAlias = field("LensAlias")
    LensArn = field("LensArn")
    LensVersion = field("LensVersion")
    LensName = field("LensName")
    LensStatus = field("LensStatus")

    @cached_property
    def PillarReviewSummaries(self):  # pragma: no cover
        return PillarReviewSummary.make_many(
            self.boto3_raw_data["PillarReviewSummaries"]
        )

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return JiraSelectedQuestionConfigurationOutput.make_one(
            self.boto3_raw_data["JiraConfiguration"]
        )

    UpdatedAt = field("UpdatedAt")
    Notes = field("Notes")
    RiskCounts = field("RiskCounts")
    NextToken = field("NextToken")

    @cached_property
    def Profiles(self):  # pragma: no cover
        return WorkloadProfile.make_many(self.boto3_raw_data["Profiles"])

    PrioritizedRiskCounts = field("PrioritizedRiskCounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LensReviewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LensReviewTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLensReviewsOutput:
    boto3_raw_data: "type_defs.ListLensReviewsOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    MilestoneNumber = field("MilestoneNumber")

    @cached_property
    def LensReviewSummaries(self):  # pragma: no cover
        return LensReviewSummary.make_many(self.boto3_raw_data["LensReviewSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLensReviewsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLensReviewsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadsOutput:
    boto3_raw_data: "type_defs.ListWorkloadsOutputTypeDef" = dataclasses.field()

    @cached_property
    def WorkloadSummaries(self):  # pragma: no cover
        return WorkloadSummary.make_many(self.boto3_raw_data["WorkloadSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkloadsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MilestoneSummary:
    boto3_raw_data: "type_defs.MilestoneSummaryTypeDef" = dataclasses.field()

    MilestoneNumber = field("MilestoneNumber")
    MilestoneName = field("MilestoneName")
    RecordedAt = field("RecordedAt")

    @cached_property
    def WorkloadSummary(self):  # pragma: no cover
        return WorkloadSummary.make_one(self.boto3_raw_data["WorkloadSummary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MilestoneSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MilestoneSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationsOutput:
    boto3_raw_data: "type_defs.ListNotificationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def NotificationSummaries(self):  # pragma: no cover
        return NotificationSummary.make_many(
            self.boto3_raw_data["NotificationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotificationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionDifferences:
    boto3_raw_data: "type_defs.VersionDifferencesTypeDef" = dataclasses.field()

    @cached_property
    def PillarDifferences(self):  # pragma: no cover
        return PillarDifference.make_many(self.boto3_raw_data["PillarDifferences"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VersionDifferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersionDifferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Profile:
    boto3_raw_data: "type_defs.ProfileTypeDef" = dataclasses.field()

    ProfileArn = field("ProfileArn")
    ProfileVersion = field("ProfileVersion")
    ProfileName = field("ProfileName")
    ProfileDescription = field("ProfileDescription")

    @cached_property
    def ProfileQuestions(self):  # pragma: no cover
        return ProfileQuestion.make_many(self.boto3_raw_data["ProfileQuestions"])

    Owner = field("Owner")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    ShareInvitationId = field("ShareInvitationId")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileTemplate:
    boto3_raw_data: "type_defs.ProfileTemplateTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")

    @cached_property
    def TemplateQuestions(self):  # pragma: no cover
        return ProfileTemplateQuestion.make_many(
            self.boto3_raw_data["TemplateQuestions"]
        )

    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfileTemplateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReviewTemplateLensReviewOutput:
    boto3_raw_data: "type_defs.GetReviewTemplateLensReviewOutputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")

    @cached_property
    def LensReview(self):  # pragma: no cover
        return ReviewTemplateLensReview.make_one(self.boto3_raw_data["LensReview"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReviewTemplateLensReviewOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReviewTemplateLensReviewOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReviewTemplateLensReviewOutput:
    boto3_raw_data: "type_defs.UpdateReviewTemplateLensReviewOutputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")

    @cached_property
    def LensReview(self):  # pragma: no cover
        return ReviewTemplateLensReview.make_one(self.boto3_raw_data["LensReview"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateReviewTemplateLensReviewOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReviewTemplateLensReviewOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkloadInput:
    boto3_raw_data: "type_defs.CreateWorkloadInputTypeDef" = dataclasses.field()

    WorkloadName = field("WorkloadName")
    Description = field("Description")
    Environment = field("Environment")
    Lenses = field("Lenses")
    ClientRequestToken = field("ClientRequestToken")
    AccountIds = field("AccountIds")
    AwsRegions = field("AwsRegions")
    NonAwsRegions = field("NonAwsRegions")
    PillarPriorities = field("PillarPriorities")
    ArchitecturalDesign = field("ArchitecturalDesign")
    ReviewOwner = field("ReviewOwner")
    IndustryType = field("IndustryType")
    Industry = field("Industry")
    Notes = field("Notes")
    Tags = field("Tags")
    DiscoveryConfig = field("DiscoveryConfig")
    Applications = field("Applications")
    ProfileArns = field("ProfileArns")
    ReviewTemplateArns = field("ReviewTemplateArns")

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return WorkloadJiraConfigurationInput.make_one(
            self.boto3_raw_data["JiraConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkloadInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkloadInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadInput:
    boto3_raw_data: "type_defs.UpdateWorkloadInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    WorkloadName = field("WorkloadName")
    Description = field("Description")
    Environment = field("Environment")
    AccountIds = field("AccountIds")
    AwsRegions = field("AwsRegions")
    NonAwsRegions = field("NonAwsRegions")
    PillarPriorities = field("PillarPriorities")
    ArchitecturalDesign = field("ArchitecturalDesign")
    ReviewOwner = field("ReviewOwner")
    IsReviewOwnerUpdateAcknowledged = field("IsReviewOwnerUpdateAcknowledged")
    IndustryType = field("IndustryType")
    Industry = field("Industry")
    Notes = field("Notes")
    ImprovementStatus = field("ImprovementStatus")
    DiscoveryConfig = field("DiscoveryConfig")
    Applications = field("Applications")

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return WorkloadJiraConfigurationInput.make_one(
            self.boto3_raw_data["JiraConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkloadInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadOutput:
    boto3_raw_data: "type_defs.GetWorkloadOutputTypeDef" = dataclasses.field()

    @cached_property
    def Workload(self):  # pragma: no cover
        return Workload.make_one(self.boto3_raw_data["Workload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetWorkloadOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Milestone:
    boto3_raw_data: "type_defs.MilestoneTypeDef" = dataclasses.field()

    MilestoneNumber = field("MilestoneNumber")
    MilestoneName = field("MilestoneName")
    RecordedAt = field("RecordedAt")

    @cached_property
    def Workload(self):  # pragma: no cover
        return Workload.make_one(self.boto3_raw_data["Workload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MilestoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MilestoneTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadOutput:
    boto3_raw_data: "type_defs.UpdateWorkloadOutputTypeDef" = dataclasses.field()

    @cached_property
    def Workload(self):  # pragma: no cover
        return Workload.make_one(self.boto3_raw_data["Workload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkloadOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnswerSummary:
    boto3_raw_data: "type_defs.AnswerSummaryTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    PillarId = field("PillarId")
    QuestionTitle = field("QuestionTitle")

    @cached_property
    def Choices(self):  # pragma: no cover
        return Choice.make_many(self.boto3_raw_data["Choices"])

    SelectedChoices = field("SelectedChoices")

    @cached_property
    def ChoiceAnswerSummaries(self):  # pragma: no cover
        return ChoiceAnswerSummary.make_many(
            self.boto3_raw_data["ChoiceAnswerSummaries"]
        )

    IsApplicable = field("IsApplicable")
    Risk = field("Risk")
    Reason = field("Reason")
    QuestionType = field("QuestionType")

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return JiraConfiguration.make_one(self.boto3_raw_data["JiraConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnswerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnswerSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Answer:
    boto3_raw_data: "type_defs.AnswerTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    PillarId = field("PillarId")
    QuestionTitle = field("QuestionTitle")
    QuestionDescription = field("QuestionDescription")
    ImprovementPlanUrl = field("ImprovementPlanUrl")
    HelpfulResourceUrl = field("HelpfulResourceUrl")
    HelpfulResourceDisplayText = field("HelpfulResourceDisplayText")

    @cached_property
    def Choices(self):  # pragma: no cover
        return Choice.make_many(self.boto3_raw_data["Choices"])

    SelectedChoices = field("SelectedChoices")

    @cached_property
    def ChoiceAnswers(self):  # pragma: no cover
        return ChoiceAnswer.make_many(self.boto3_raw_data["ChoiceAnswers"])

    IsApplicable = field("IsApplicable")
    Risk = field("Risk")
    Notes = field("Notes")
    Reason = field("Reason")

    @cached_property
    def JiraConfiguration(self):  # pragma: no cover
        return JiraConfiguration.make_one(self.boto3_raw_data["JiraConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnswerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnswerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewTemplateAnswerSummary:
    boto3_raw_data: "type_defs.ReviewTemplateAnswerSummaryTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    PillarId = field("PillarId")
    QuestionTitle = field("QuestionTitle")

    @cached_property
    def Choices(self):  # pragma: no cover
        return Choice.make_many(self.boto3_raw_data["Choices"])

    SelectedChoices = field("SelectedChoices")

    @cached_property
    def ChoiceAnswerSummaries(self):  # pragma: no cover
        return ChoiceAnswerSummary.make_many(
            self.boto3_raw_data["ChoiceAnswerSummaries"]
        )

    IsApplicable = field("IsApplicable")
    AnswerStatus = field("AnswerStatus")
    Reason = field("Reason")
    QuestionType = field("QuestionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReviewTemplateAnswerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReviewTemplateAnswerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewTemplateAnswer:
    boto3_raw_data: "type_defs.ReviewTemplateAnswerTypeDef" = dataclasses.field()

    QuestionId = field("QuestionId")
    PillarId = field("PillarId")
    QuestionTitle = field("QuestionTitle")
    QuestionDescription = field("QuestionDescription")
    ImprovementPlanUrl = field("ImprovementPlanUrl")
    HelpfulResourceUrl = field("HelpfulResourceUrl")
    HelpfulResourceDisplayText = field("HelpfulResourceDisplayText")

    @cached_property
    def Choices(self):  # pragma: no cover
        return Choice.make_many(self.boto3_raw_data["Choices"])

    SelectedChoices = field("SelectedChoices")

    @cached_property
    def ChoiceAnswers(self):  # pragma: no cover
        return ChoiceAnswer.make_many(self.boto3_raw_data["ChoiceAnswers"])

    IsApplicable = field("IsApplicable")
    AnswerStatus = field("AnswerStatus")
    Notes = field("Notes")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReviewTemplateAnswerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReviewTemplateAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LensMetric:
    boto3_raw_data: "type_defs.LensMetricTypeDef" = dataclasses.field()

    LensArn = field("LensArn")

    @cached_property
    def Pillars(self):  # pragma: no cover
        return PillarMetric.make_many(self.boto3_raw_data["Pillars"])

    RiskCounts = field("RiskCounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LensMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LensMetricTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLensReviewOutput:
    boto3_raw_data: "type_defs.GetLensReviewOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    MilestoneNumber = field("MilestoneNumber")

    @cached_property
    def LensReview(self):  # pragma: no cover
        return LensReview.make_one(self.boto3_raw_data["LensReview"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLensReviewOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLensReviewOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLensReviewOutput:
    boto3_raw_data: "type_defs.UpdateLensReviewOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")

    @cached_property
    def LensReview(self):  # pragma: no cover
        return LensReview.make_one(self.boto3_raw_data["LensReview"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLensReviewOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLensReviewOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLensReviewInput:
    boto3_raw_data: "type_defs.UpdateLensReviewInputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    LensNotes = field("LensNotes")
    PillarNotes = field("PillarNotes")
    JiraConfiguration = field("JiraConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLensReviewInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLensReviewInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMilestonesOutput:
    boto3_raw_data: "type_defs.ListMilestonesOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")

    @cached_property
    def MilestoneSummaries(self):  # pragma: no cover
        return MilestoneSummary.make_many(self.boto3_raw_data["MilestoneSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMilestonesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMilestonesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLensVersionDifferenceOutput:
    boto3_raw_data: "type_defs.GetLensVersionDifferenceOutputTypeDef" = (
        dataclasses.field()
    )

    LensAlias = field("LensAlias")
    LensArn = field("LensArn")
    BaseLensVersion = field("BaseLensVersion")
    TargetLensVersion = field("TargetLensVersion")
    LatestLensVersion = field("LatestLensVersion")

    @cached_property
    def VersionDifferences(self):  # pragma: no cover
        return VersionDifferences.make_one(self.boto3_raw_data["VersionDifferences"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLensVersionDifferenceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLensVersionDifferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileOutput:
    boto3_raw_data: "type_defs.GetProfileOutputTypeDef" = dataclasses.field()

    @cached_property
    def Profile(self):  # pragma: no cover
        return Profile.make_one(self.boto3_raw_data["Profile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetProfileOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfileOutput:
    boto3_raw_data: "type_defs.UpdateProfileOutputTypeDef" = dataclasses.field()

    @cached_property
    def Profile(self):  # pragma: no cover
        return Profile.make_one(self.boto3_raw_data["Profile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileTemplateOutput:
    boto3_raw_data: "type_defs.GetProfileTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProfileTemplate(self):  # pragma: no cover
        return ProfileTemplate.make_one(self.boto3_raw_data["ProfileTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProfileTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMilestoneOutput:
    boto3_raw_data: "type_defs.GetMilestoneOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")

    @cached_property
    def Milestone(self):  # pragma: no cover
        return Milestone.make_one(self.boto3_raw_data["Milestone"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMilestoneOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMilestoneOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnswersOutput:
    boto3_raw_data: "type_defs.ListAnswersOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    MilestoneNumber = field("MilestoneNumber")
    LensAlias = field("LensAlias")
    LensArn = field("LensArn")

    @cached_property
    def AnswerSummaries(self):  # pragma: no cover
        return AnswerSummary.make_many(self.boto3_raw_data["AnswerSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAnswersOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnswersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnswerOutput:
    boto3_raw_data: "type_defs.GetAnswerOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    MilestoneNumber = field("MilestoneNumber")
    LensAlias = field("LensAlias")
    LensArn = field("LensArn")

    @cached_property
    def Answer(self):  # pragma: no cover
        return Answer.make_one(self.boto3_raw_data["Answer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAnswerOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAnswerOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnswerOutput:
    boto3_raw_data: "type_defs.UpdateAnswerOutputTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    LensAlias = field("LensAlias")
    LensArn = field("LensArn")

    @cached_property
    def Answer(self):  # pragma: no cover
        return Answer.make_one(self.boto3_raw_data["Answer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnswerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnswerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReviewTemplateAnswersOutput:
    boto3_raw_data: "type_defs.ListReviewTemplateAnswersOutputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    LensAlias = field("LensAlias")

    @cached_property
    def AnswerSummaries(self):  # pragma: no cover
        return ReviewTemplateAnswerSummary.make_many(
            self.boto3_raw_data["AnswerSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReviewTemplateAnswersOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReviewTemplateAnswersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReviewTemplateAnswerOutput:
    boto3_raw_data: "type_defs.GetReviewTemplateAnswerOutputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    LensAlias = field("LensAlias")

    @cached_property
    def Answer(self):  # pragma: no cover
        return ReviewTemplateAnswer.make_one(self.boto3_raw_data["Answer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReviewTemplateAnswerOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReviewTemplateAnswerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReviewTemplateAnswerOutput:
    boto3_raw_data: "type_defs.UpdateReviewTemplateAnswerOutputTypeDef" = (
        dataclasses.field()
    )

    TemplateArn = field("TemplateArn")
    LensAlias = field("LensAlias")

    @cached_property
    def Answer(self):  # pragma: no cover
        return ReviewTemplateAnswer.make_one(self.boto3_raw_data["Answer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateReviewTemplateAnswerOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReviewTemplateAnswerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsolidatedReportMetric:
    boto3_raw_data: "type_defs.ConsolidatedReportMetricTypeDef" = dataclasses.field()

    MetricType = field("MetricType")
    RiskCounts = field("RiskCounts")
    WorkloadId = field("WorkloadId")
    WorkloadName = field("WorkloadName")
    WorkloadArn = field("WorkloadArn")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def Lenses(self):  # pragma: no cover
        return LensMetric.make_many(self.boto3_raw_data["Lenses"])

    LensesAppliedCount = field("LensesAppliedCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsolidatedReportMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsolidatedReportMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConsolidatedReportOutput:
    boto3_raw_data: "type_defs.GetConsolidatedReportOutputTypeDef" = dataclasses.field()

    @cached_property
    def Metrics(self):  # pragma: no cover
        return ConsolidatedReportMetric.make_many(self.boto3_raw_data["Metrics"])

    Base64String = field("Base64String")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConsolidatedReportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConsolidatedReportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
