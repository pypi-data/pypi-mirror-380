# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_resiliencehub import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptGroupingRecommendationEntry:
    boto3_raw_data: "type_defs.AcceptGroupingRecommendationEntryTypeDef" = (
        dataclasses.field()
    )

    groupingRecommendationId = field("groupingRecommendationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptGroupingRecommendationEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptGroupingRecommendationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedGroupingRecommendationEntry:
    boto3_raw_data: "type_defs.FailedGroupingRecommendationEntryTypeDef" = (
        dataclasses.field()
    )

    errorMessage = field("errorMessage")
    groupingRecommendationId = field("groupingRecommendationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailedGroupingRecommendationEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedGroupingRecommendationEntryTypeDef"]
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
class Alarm:
    boto3_raw_data: "type_defs.AlarmTypeDef" = dataclasses.field()

    alarmArn = field("alarmArn")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cost:
    boto3_raw_data: "type_defs.CostTypeDef" = dataclasses.field()

    amount = field("amount")
    currency = field("currency")
    frequency = field("frequency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CostTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisruptionCompliance:
    boto3_raw_data: "type_defs.DisruptionComplianceTypeDef" = dataclasses.field()

    complianceStatus = field("complianceStatus")
    achievableRpoInSecs = field("achievableRpoInSecs")
    achievableRtoInSecs = field("achievableRtoInSecs")
    currentRpoInSecs = field("currentRpoInSecs")
    currentRtoInSecs = field("currentRtoInSecs")
    message = field("message")
    rpoDescription = field("rpoDescription")
    rpoReferenceId = field("rpoReferenceId")
    rtoDescription = field("rtoDescription")
    rtoReferenceId = field("rtoReferenceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisruptionComplianceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisruptionComplianceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppComponent:
    boto3_raw_data: "type_defs.AppComponentTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    additionalInfo = field("additionalInfo")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppComponentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppComponentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksSourceClusterNamespace:
    boto3_raw_data: "type_defs.EksSourceClusterNamespaceTypeDef" = dataclasses.field()

    eksClusterArn = field("eksClusterArn")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksSourceClusterNamespaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksSourceClusterNamespaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerraformSource:
    boto3_raw_data: "type_defs.TerraformSourceTypeDef" = dataclasses.field()

    s3StateFileUrl = field("s3StateFileUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TerraformSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TerraformSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppSummary:
    boto3_raw_data: "type_defs.AppSummaryTypeDef" = dataclasses.field()

    appArn = field("appArn")
    creationTime = field("creationTime")
    name = field("name")
    assessmentSchedule = field("assessmentSchedule")
    awsApplicationArn = field("awsApplicationArn")
    complianceStatus = field("complianceStatus")
    description = field("description")
    driftStatus = field("driftStatus")
    lastAppComplianceEvaluationTime = field("lastAppComplianceEvaluationTime")
    resiliencyScore = field("resiliencyScore")
    rpoInSecs = field("rpoInSecs")
    rtoInSecs = field("rtoInSecs")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSubscription:
    boto3_raw_data: "type_defs.EventSubscriptionTypeDef" = dataclasses.field()

    eventType = field("eventType")
    name = field("name")
    snsTopicArn = field("snsTopicArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSubscriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionModelOutput:
    boto3_raw_data: "type_defs.PermissionModelOutputTypeDef" = dataclasses.field()

    type = field("type")
    crossAccountRoleArns = field("crossAccountRoleArns")
    invokerRoleName = field("invokerRoleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PermissionModelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionModelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppVersionSummary:
    boto3_raw_data: "type_defs.AppVersionSummaryTypeDef" = dataclasses.field()

    appVersion = field("appVersion")
    creationTime = field("creationTime")
    identifier = field("identifier")
    versionName = field("versionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppVersionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentRiskRecommendation:
    boto3_raw_data: "type_defs.AssessmentRiskRecommendationTypeDef" = (
        dataclasses.field()
    )

    appComponents = field("appComponents")
    recommendation = field("recommendation")
    risk = field("risk")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentRiskRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentRiskRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateRecommendationStatusFailedEntry:
    boto3_raw_data: "type_defs.BatchUpdateRecommendationStatusFailedEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateRecommendationStatusFailedEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateRecommendationStatusFailedEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecommendationStatusItem:
    boto3_raw_data: "type_defs.UpdateRecommendationStatusItemTypeDef" = (
        dataclasses.field()
    )

    resourceId = field("resourceId")
    targetAccountId = field("targetAccountId")
    targetRegion = field("targetRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRecommendationStatusItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecommendationStatusItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    field = field("field")
    operator = field("operator")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationDisruptionCompliance:
    boto3_raw_data: "type_defs.RecommendationDisruptionComplianceTypeDef" = (
        dataclasses.field()
    )

    expectedComplianceStatus = field("expectedComplianceStatus")
    expectedRpoDescription = field("expectedRpoDescription")
    expectedRpoInSecs = field("expectedRpoInSecs")
    expectedRtoDescription = field("expectedRtoDescription")
    expectedRtoInSecs = field("expectedRtoInSecs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecommendationDisruptionComplianceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationDisruptionComplianceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppVersionAppComponentRequest:
    boto3_raw_data: "type_defs.CreateAppVersionAppComponentRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    name = field("name")
    type = field("type")
    additionalInfo = field("additionalInfo")
    clientToken = field("clientToken")
    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAppVersionAppComponentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppVersionAppComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogicalResourceId:
    boto3_raw_data: "type_defs.LogicalResourceIdTypeDef" = dataclasses.field()

    identifier = field("identifier")
    eksSourceName = field("eksSourceName")
    logicalStackName = field("logicalStackName")
    resourceGroupName = field("resourceGroupName")
    terraformSourceName = field("terraformSourceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogicalResourceIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogicalResourceIdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecommendationTemplateRequest:
    boto3_raw_data: "type_defs.CreateRecommendationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")
    name = field("name")
    bucketName = field("bucketName")
    clientToken = field("clientToken")
    format = field("format")
    recommendationIds = field("recommendationIds")
    recommendationTypes = field("recommendationTypes")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRecommendationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecommendationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailurePolicy:
    boto3_raw_data: "type_defs.FailurePolicyTypeDef" = dataclasses.field()

    rpoInSecs = field("rpoInSecs")
    rtoInSecs = field("rtoInSecs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailurePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailurePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppAssessmentRequest:
    boto3_raw_data: "type_defs.DeleteAppAssessmentRequestTypeDef" = dataclasses.field()

    assessmentArn = field("assessmentArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAppAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppRequest:
    boto3_raw_data: "type_defs.DeleteAppRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    clientToken = field("clientToken")
    forceDelete = field("forceDelete")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppVersionAppComponentRequest:
    boto3_raw_data: "type_defs.DeleteAppVersionAppComponentRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    id = field("id")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAppVersionAppComponentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppVersionAppComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecommendationTemplateRequest:
    boto3_raw_data: "type_defs.DeleteRecommendationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    recommendationTemplateArn = field("recommendationTemplateArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRecommendationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecommendationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResiliencyPolicyRequest:
    boto3_raw_data: "type_defs.DeleteResiliencyPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteResiliencyPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResiliencyPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppAssessmentRequest:
    boto3_raw_data: "type_defs.DescribeAppAssessmentRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppRequest:
    boto3_raw_data: "type_defs.DescribeAppRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionAppComponentRequest:
    boto3_raw_data: "type_defs.DescribeAppVersionAppComponentRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")
    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppVersionAppComponentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppVersionAppComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionRequest:
    boto3_raw_data: "type_defs.DescribeAppVersionRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    appVersion = field("appVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionResourcesResolutionStatusRequest:
    boto3_raw_data: (
        "type_defs.DescribeAppVersionResourcesResolutionStatusRequestTypeDef"
    ) = dataclasses.field()

    appArn = field("appArn")
    appVersion = field("appVersion")
    resolutionId = field("resolutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppVersionResourcesResolutionStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeAppVersionResourcesResolutionStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionTemplateRequest:
    boto3_raw_data: "type_defs.DescribeAppVersionTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppVersionTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppVersionTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDraftAppVersionResourcesImportStatusRequest:
    boto3_raw_data: (
        "type_defs.DescribeDraftAppVersionResourcesImportStatusRequestTypeDef"
    ) = dataclasses.field()

    appArn = field("appArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDraftAppVersionResourcesImportStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeDraftAppVersionResourcesImportStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetail:
    boto3_raw_data: "type_defs.ErrorDetailTypeDef" = dataclasses.field()

    errorMessage = field("errorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetricsExportRequest:
    boto3_raw_data: "type_defs.DescribeMetricsExportRequestTypeDef" = (
        dataclasses.field()
    )

    metricsExportId = field("metricsExportId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMetricsExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricsExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResiliencyPolicyRequest:
    boto3_raw_data: "type_defs.DescribeResiliencyPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResiliencyPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResiliencyPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceGroupingRecommendationTaskRequest:
    boto3_raw_data: (
        "type_defs.DescribeResourceGroupingRecommendationTaskRequestTypeDef"
    ) = dataclasses.field()

    appArn = field("appArn")
    groupingId = field("groupingId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeResourceGroupingRecommendationTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeResourceGroupingRecommendationTaskRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksSourceOutput:
    boto3_raw_data: "type_defs.EksSourceOutputTypeDef" = dataclasses.field()

    eksClusterArn = field("eksClusterArn")
    namespaces = field("namespaces")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksSourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksSourceOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksSource:
    boto3_raw_data: "type_defs.EksSourceTypeDef" = dataclasses.field()

    eksClusterArn = field("eksClusterArn")
    namespaces = field("namespaces")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Experiment:
    boto3_raw_data: "type_defs.ExperimentTypeDef" = dataclasses.field()

    experimentArn = field("experimentArn")
    experimentTemplateId = field("experimentTemplateId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExperimentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Field:
    boto3_raw_data: "type_defs.FieldTypeDef" = dataclasses.field()

    name = field("name")
    aggregation = field("aggregation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupingAppComponent:
    boto3_raw_data: "type_defs.GroupingAppComponentTypeDef" = dataclasses.field()

    appComponentId = field("appComponentId")
    appComponentName = field("appComponentName")
    appComponentType = field("appComponentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GroupingAppComponentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupingAppComponentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhysicalResourceId:
    boto3_raw_data: "type_defs.PhysicalResourceIdTypeDef" = dataclasses.field()

    identifier = field("identifier")
    type = field("type")
    awsAccountId = field("awsAccountId")
    awsRegion = field("awsRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhysicalResourceIdTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhysicalResourceIdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlarmRecommendationsRequest:
    boto3_raw_data: "type_defs.ListAlarmRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAlarmRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlarmRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppAssessmentComplianceDriftsRequest:
    boto3_raw_data: "type_defs.ListAppAssessmentComplianceDriftsRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppAssessmentComplianceDriftsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppAssessmentComplianceDriftsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppAssessmentResourceDriftsRequest:
    boto3_raw_data: "type_defs.ListAppAssessmentResourceDriftsRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppAssessmentResourceDriftsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppAssessmentResourceDriftsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppAssessmentsRequest:
    boto3_raw_data: "type_defs.ListAppAssessmentsRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    assessmentName = field("assessmentName")
    assessmentStatus = field("assessmentStatus")
    complianceStatus = field("complianceStatus")
    invoker = field("invoker")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    reverseOrder = field("reverseOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppAssessmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppAssessmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppComponentCompliancesRequest:
    boto3_raw_data: "type_defs.ListAppComponentCompliancesRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppComponentCompliancesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppComponentCompliancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppComponentRecommendationsRequest:
    boto3_raw_data: "type_defs.ListAppComponentRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppComponentRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppComponentRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppInputSourcesRequest:
    boto3_raw_data: "type_defs.ListAppInputSourcesRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    appVersion = field("appVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppInputSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppInputSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppVersionAppComponentsRequest:
    boto3_raw_data: "type_defs.ListAppVersionAppComponentsRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppVersionAppComponentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppVersionAppComponentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppVersionResourceMappingsRequest:
    boto3_raw_data: "type_defs.ListAppVersionResourceMappingsRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppVersionResourceMappingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppVersionResourceMappingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppVersionResourcesRequest:
    boto3_raw_data: "type_defs.ListAppVersionResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    resolutionId = field("resolutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAppVersionResourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppVersionResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sort:
    boto3_raw_data: "type_defs.SortTypeDef" = dataclasses.field()

    field = field("field")
    ascending = field("ascending")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationTemplatesRequest:
    boto3_raw_data: "type_defs.ListRecommendationTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")
    recommendationTemplateArn = field("recommendationTemplateArn")
    reverseOrder = field("reverseOrder")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResiliencyPoliciesRequest:
    boto3_raw_data: "type_defs.ListResiliencyPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    policyName = field("policyName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResiliencyPoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResiliencyPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceGroupingRecommendationsRequest:
    boto3_raw_data: "type_defs.ListResourceGroupingRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceGroupingRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceGroupingRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSopRecommendationsRequest:
    boto3_raw_data: "type_defs.ListSopRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSopRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSopRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSuggestedResiliencyPoliciesRequest:
    boto3_raw_data: "type_defs.ListSuggestedResiliencyPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSuggestedResiliencyPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSuggestedResiliencyPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRecommendationsRequest:
    boto3_raw_data: "type_defs.ListTestRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentArn = field("assessmentArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTestRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUnsupportedAppVersionResourcesRequest:
    boto3_raw_data: "type_defs.ListUnsupportedAppVersionResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    resolutionId = field("resolutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUnsupportedAppVersionResourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUnsupportedAppVersionResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionModel:
    boto3_raw_data: "type_defs.PermissionModelTypeDef" = dataclasses.field()

    type = field("type")
    crossAccountRoleArns = field("crossAccountRoleArns")
    invokerRoleName = field("invokerRoleName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionModelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishAppVersionRequest:
    boto3_raw_data: "type_defs.PublishAppVersionRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    versionName = field("versionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishAppVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishAppVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDraftAppVersionTemplateRequest:
    boto3_raw_data: "type_defs.PutDraftAppVersionTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appTemplateBody = field("appTemplateBody")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDraftAppVersionTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDraftAppVersionTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectGroupingRecommendationEntry:
    boto3_raw_data: "type_defs.RejectGroupingRecommendationEntryTypeDef" = (
        dataclasses.field()
    )

    groupingRecommendationId = field("groupingRecommendationId")
    rejectionReason = field("rejectionReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectGroupingRecommendationEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectGroupingRecommendationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveDraftAppVersionResourceMappingsRequest:
    boto3_raw_data: "type_defs.RemoveDraftAppVersionResourceMappingsRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appRegistryAppNames = field("appRegistryAppNames")
    eksSourceNames = field("eksSourceNames")
    logicalStackNames = field("logicalStackNames")
    resourceGroupNames = field("resourceGroupNames")
    resourceNames = field("resourceNames")
    terraformSourceNames = field("terraformSourceNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveDraftAppVersionResourceMappingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveDraftAppVersionResourceMappingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScoringComponentResiliencyScore:
    boto3_raw_data: "type_defs.ScoringComponentResiliencyScoreTypeDef" = (
        dataclasses.field()
    )

    excludedCount = field("excludedCount")
    outstandingCount = field("outstandingCount")
    possibleScore = field("possibleScore")
    score = field("score")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ScoringComponentResiliencyScoreTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScoringComponentResiliencyScoreTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolveAppVersionResourcesRequest:
    boto3_raw_data: "type_defs.ResolveAppVersionResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResolveAppVersionResourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolveAppVersionResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceError:
    boto3_raw_data: "type_defs.ResourceErrorTypeDef" = dataclasses.field()

    logicalResourceId = field("logicalResourceId")
    physicalResourceId = field("physicalResourceId")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAppAssessmentRequest:
    boto3_raw_data: "type_defs.StartAppAssessmentRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    appVersion = field("appVersion")
    assessmentName = field("assessmentName")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAppAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAppAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetricsExportRequest:
    boto3_raw_data: "type_defs.StartMetricsExportRequestTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMetricsExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetricsExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceGroupingRecommendationTaskRequest:
    boto3_raw_data: (
        "type_defs.StartResourceGroupingRecommendationTaskRequestTypeDef"
    ) = dataclasses.field()

    appArn = field("appArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartResourceGroupingRecommendationTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StartResourceGroupingRecommendationTaskRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppVersionAppComponentRequest:
    boto3_raw_data: "type_defs.UpdateAppVersionAppComponentRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    id = field("id")
    additionalInfo = field("additionalInfo")
    name = field("name")
    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAppVersionAppComponentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppVersionAppComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppVersionRequest:
    boto3_raw_data: "type_defs.UpdateAppVersionRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    additionalInfo = field("additionalInfo")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAppVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptResourceGroupingRecommendationsRequest:
    boto3_raw_data: "type_defs.AcceptResourceGroupingRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def entries(self):  # pragma: no cover
        return AcceptGroupingRecommendationEntry.make_many(
            self.boto3_raw_data["entries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptResourceGroupingRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptResourceGroupingRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptResourceGroupingRecommendationsResponse:
    boto3_raw_data: "type_defs.AcceptResourceGroupingRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def failedEntries(self):  # pragma: no cover
        return FailedGroupingRecommendationEntry.make_many(
            self.boto3_raw_data["failedEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptResourceGroupingRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptResourceGroupingRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppAssessmentResponse:
    boto3_raw_data: "type_defs.DeleteAppAssessmentResponseTypeDef" = dataclasses.field()

    assessmentArn = field("assessmentArn")
    assessmentStatus = field("assessmentStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAppAssessmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppResponse:
    boto3_raw_data: "type_defs.DeleteAppResponseTypeDef" = dataclasses.field()

    appArn = field("appArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAppResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecommendationTemplateResponse:
    boto3_raw_data: "type_defs.DeleteRecommendationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    recommendationTemplateArn = field("recommendationTemplateArn")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRecommendationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecommendationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResiliencyPolicyResponse:
    boto3_raw_data: "type_defs.DeleteResiliencyPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteResiliencyPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResiliencyPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionResourcesResolutionStatusResponse:
    boto3_raw_data: (
        "type_defs.DescribeAppVersionResourcesResolutionStatusResponseTypeDef"
    ) = dataclasses.field()

    appArn = field("appArn")
    appVersion = field("appVersion")
    errorMessage = field("errorMessage")
    resolutionId = field("resolutionId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppVersionResourcesResolutionStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeAppVersionResourcesResolutionStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionResponse:
    boto3_raw_data: "type_defs.DescribeAppVersionResponseTypeDef" = dataclasses.field()

    additionalInfo = field("additionalInfo")
    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionTemplateResponse:
    boto3_raw_data: "type_defs.DescribeAppVersionTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appTemplateBody = field("appTemplateBody")
    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppVersionTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppVersionTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceGroupingRecommendationTaskResponse:
    boto3_raw_data: (
        "type_defs.DescribeResourceGroupingRecommendationTaskResponseTypeDef"
    ) = dataclasses.field()

    errorMessage = field("errorMessage")
    groupingId = field("groupingId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeResourceGroupingRecommendationTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeResourceGroupingRecommendationTaskResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricsResponse:
    boto3_raw_data: "type_defs.ListMetricsResponseTypeDef" = dataclasses.field()

    rows = field("rows")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishAppVersionResponse:
    boto3_raw_data: "type_defs.PublishAppVersionResponseTypeDef" = dataclasses.field()

    appArn = field("appArn")
    appVersion = field("appVersion")
    identifier = field("identifier")
    versionName = field("versionName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishAppVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishAppVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDraftAppVersionTemplateResponse:
    boto3_raw_data: "type_defs.PutDraftAppVersionTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDraftAppVersionTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDraftAppVersionTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectResourceGroupingRecommendationsResponse:
    boto3_raw_data: "type_defs.RejectResourceGroupingRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def failedEntries(self):  # pragma: no cover
        return FailedGroupingRecommendationEntry.make_many(
            self.boto3_raw_data["failedEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectResourceGroupingRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectResourceGroupingRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveDraftAppVersionResourceMappingsResponse:
    boto3_raw_data: "type_defs.RemoveDraftAppVersionResourceMappingsResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveDraftAppVersionResourceMappingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveDraftAppVersionResourceMappingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolveAppVersionResourcesResponse:
    boto3_raw_data: "type_defs.ResolveAppVersionResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")
    resolutionId = field("resolutionId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResolveAppVersionResourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolveAppVersionResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetricsExportResponse:
    boto3_raw_data: "type_defs.StartMetricsExportResponseTypeDef" = dataclasses.field()

    metricsExportId = field("metricsExportId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMetricsExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetricsExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceGroupingRecommendationTaskResponse:
    boto3_raw_data: (
        "type_defs.StartResourceGroupingRecommendationTaskResponseTypeDef"
    ) = dataclasses.field()

    appArn = field("appArn")
    errorMessage = field("errorMessage")
    groupingId = field("groupingId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartResourceGroupingRecommendationTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StartResourceGroupingRecommendationTaskResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppVersionResponse:
    boto3_raw_data: "type_defs.UpdateAppVersionResponseTypeDef" = dataclasses.field()

    additionalInfo = field("additionalInfo")
    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAppVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppAssessmentSummary:
    boto3_raw_data: "type_defs.AppAssessmentSummaryTypeDef" = dataclasses.field()

    assessmentArn = field("assessmentArn")
    assessmentStatus = field("assessmentStatus")
    appArn = field("appArn")
    appVersion = field("appVersion")
    assessmentName = field("assessmentName")
    complianceStatus = field("complianceStatus")

    @cached_property
    def cost(self):  # pragma: no cover
        return Cost.make_one(self.boto3_raw_data["cost"])

    driftStatus = field("driftStatus")
    endTime = field("endTime")
    invoker = field("invoker")
    message = field("message")
    resiliencyScore = field("resiliencyScore")
    startTime = field("startTime")
    versionName = field("versionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppAssessmentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppAssessmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceDrift:
    boto3_raw_data: "type_defs.ComplianceDriftTypeDef" = dataclasses.field()

    actualReferenceId = field("actualReferenceId")
    actualValue = field("actualValue")
    appId = field("appId")
    appVersion = field("appVersion")
    diffType = field("diffType")
    driftType = field("driftType")
    entityId = field("entityId")
    entityType = field("entityType")
    expectedReferenceId = field("expectedReferenceId")
    expectedValue = field("expectedValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComplianceDriftTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComplianceDriftTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppVersionAppComponentResponse:
    boto3_raw_data: "type_defs.CreateAppVersionAppComponentResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def appComponent(self):  # pragma: no cover
        return AppComponent.make_one(self.boto3_raw_data["appComponent"])

    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAppVersionAppComponentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppVersionAppComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppVersionAppComponentResponse:
    boto3_raw_data: "type_defs.DeleteAppVersionAppComponentResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def appComponent(self):  # pragma: no cover
        return AppComponent.make_one(self.boto3_raw_data["appComponent"])

    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAppVersionAppComponentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppVersionAppComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionAppComponentResponse:
    boto3_raw_data: "type_defs.DescribeAppVersionAppComponentResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def appComponent(self):  # pragma: no cover
        return AppComponent.make_one(self.boto3_raw_data["appComponent"])

    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppVersionAppComponentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppVersionAppComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppVersionAppComponentsResponse:
    boto3_raw_data: "type_defs.ListAppVersionAppComponentsResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def appComponents(self):  # pragma: no cover
        return AppComponent.make_many(self.boto3_raw_data["appComponents"])

    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppVersionAppComponentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppVersionAppComponentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppVersionAppComponentResponse:
    boto3_raw_data: "type_defs.UpdateAppVersionAppComponentResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def appComponent(self):  # pragma: no cover
        return AppComponent.make_one(self.boto3_raw_data["appComponent"])

    appVersion = field("appVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAppVersionAppComponentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppVersionAppComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppInputSource:
    boto3_raw_data: "type_defs.AppInputSourceTypeDef" = dataclasses.field()

    importType = field("importType")

    @cached_property
    def eksSourceClusterNamespace(self):  # pragma: no cover
        return EksSourceClusterNamespace.make_one(
            self.boto3_raw_data["eksSourceClusterNamespace"]
        )

    resourceCount = field("resourceCount")
    sourceArn = field("sourceArn")
    sourceName = field("sourceName")

    @cached_property
    def terraformSource(self):  # pragma: no cover
        return TerraformSource.make_one(self.boto3_raw_data["terraformSource"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppInputSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppInputSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppInputSourceRequest:
    boto3_raw_data: "type_defs.DeleteAppInputSourceRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    clientToken = field("clientToken")

    @cached_property
    def eksSourceClusterNamespace(self):  # pragma: no cover
        return EksSourceClusterNamespace.make_one(
            self.boto3_raw_data["eksSourceClusterNamespace"]
        )

    sourceArn = field("sourceArn")

    @cached_property
    def terraformSource(self):  # pragma: no cover
        return TerraformSource.make_one(self.boto3_raw_data["terraformSource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAppInputSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppInputSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsResponse:
    boto3_raw_data: "type_defs.ListAppsResponseTypeDef" = dataclasses.field()

    @cached_property
    def appSummaries(self):  # pragma: no cover
        return AppSummary.make_many(self.boto3_raw_data["appSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAppsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class App:
    boto3_raw_data: "type_defs.AppTypeDef" = dataclasses.field()

    appArn = field("appArn")
    creationTime = field("creationTime")
    name = field("name")
    assessmentSchedule = field("assessmentSchedule")
    awsApplicationArn = field("awsApplicationArn")
    complianceStatus = field("complianceStatus")
    description = field("description")
    driftStatus = field("driftStatus")

    @cached_property
    def eventSubscriptions(self):  # pragma: no cover
        return EventSubscription.make_many(self.boto3_raw_data["eventSubscriptions"])

    lastAppComplianceEvaluationTime = field("lastAppComplianceEvaluationTime")
    lastDriftEvaluationTime = field("lastDriftEvaluationTime")
    lastResiliencyScoreEvaluationTime = field("lastResiliencyScoreEvaluationTime")

    @cached_property
    def permissionModel(self):  # pragma: no cover
        return PermissionModelOutput.make_one(self.boto3_raw_data["permissionModel"])

    policyArn = field("policyArn")
    resiliencyScore = field("resiliencyScore")
    rpoInSecs = field("rpoInSecs")
    rtoInSecs = field("rtoInSecs")
    status = field("status")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppVersionsResponse:
    boto3_raw_data: "type_defs.ListAppVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def appVersions(self):  # pragma: no cover
        return AppVersionSummary.make_many(self.boto3_raw_data["appVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentSummary:
    boto3_raw_data: "type_defs.AssessmentSummaryTypeDef" = dataclasses.field()

    @cached_property
    def riskRecommendations(self):  # pragma: no cover
        return AssessmentRiskRecommendation.make_many(
            self.boto3_raw_data["riskRecommendations"]
        )

    summary = field("summary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateRecommendationStatusSuccessfulEntry:
    boto3_raw_data: (
        "type_defs.BatchUpdateRecommendationStatusSuccessfulEntryTypeDef"
    ) = dataclasses.field()

    entryId = field("entryId")
    excluded = field("excluded")
    referenceId = field("referenceId")
    appComponentId = field("appComponentId")
    excludeReason = field("excludeReason")

    @cached_property
    def item(self):  # pragma: no cover
        return UpdateRecommendationStatusItem.make_one(self.boto3_raw_data["item"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateRecommendationStatusSuccessfulEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.BatchUpdateRecommendationStatusSuccessfulEntryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecommendationStatusRequestEntry:
    boto3_raw_data: "type_defs.UpdateRecommendationStatusRequestEntryTypeDef" = (
        dataclasses.field()
    )

    entryId = field("entryId")
    excluded = field("excluded")
    referenceId = field("referenceId")
    appComponentId = field("appComponentId")
    excludeReason = field("excludeReason")

    @cached_property
    def item(self):  # pragma: no cover
        return UpdateRecommendationStatusItem.make_one(self.boto3_raw_data["item"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRecommendationStatusRequestEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecommendationStatusRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigRecommendation:
    boto3_raw_data: "type_defs.ConfigRecommendationTypeDef" = dataclasses.field()

    name = field("name")
    optimizationType = field("optimizationType")
    referenceId = field("referenceId")
    appComponentName = field("appComponentName")
    compliance = field("compliance")

    @cached_property
    def cost(self):  # pragma: no cover
        return Cost.make_one(self.boto3_raw_data["cost"])

    description = field("description")
    haArchitecture = field("haArchitecture")
    recommendationCompliance = field("recommendationCompliance")
    suggestedChanges = field("suggestedChanges")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppVersionResourceRequest:
    boto3_raw_data: "type_defs.CreateAppVersionResourceRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appComponents = field("appComponents")

    @cached_property
    def logicalResourceId(self):  # pragma: no cover
        return LogicalResourceId.make_one(self.boto3_raw_data["logicalResourceId"])

    physicalResourceId = field("physicalResourceId")
    resourceType = field("resourceType")
    additionalInfo = field("additionalInfo")
    awsAccountId = field("awsAccountId")
    awsRegion = field("awsRegion")
    clientToken = field("clientToken")
    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAppVersionResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppVersionResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppVersionResourceRequest:
    boto3_raw_data: "type_defs.DeleteAppVersionResourceRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    awsAccountId = field("awsAccountId")
    awsRegion = field("awsRegion")
    clientToken = field("clientToken")

    @cached_property
    def logicalResourceId(self):  # pragma: no cover
        return LogicalResourceId.make_one(self.boto3_raw_data["logicalResourceId"])

    physicalResourceId = field("physicalResourceId")
    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAppVersionResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppVersionResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionResourceRequest:
    boto3_raw_data: "type_defs.DescribeAppVersionResourceRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")
    awsAccountId = field("awsAccountId")
    awsRegion = field("awsRegion")

    @cached_property
    def logicalResourceId(self):  # pragma: no cover
        return LogicalResourceId.make_one(self.boto3_raw_data["logicalResourceId"])

    physicalResourceId = field("physicalResourceId")
    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppVersionResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppVersionResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceIdentifier:
    boto3_raw_data: "type_defs.ResourceIdentifierTypeDef" = dataclasses.field()

    @cached_property
    def logicalResourceId(self):  # pragma: no cover
        return LogicalResourceId.make_one(self.boto3_raw_data["logicalResourceId"])

    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppVersionResourceRequest:
    boto3_raw_data: "type_defs.UpdateAppVersionResourceRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    additionalInfo = field("additionalInfo")
    appComponents = field("appComponents")
    awsAccountId = field("awsAccountId")
    awsRegion = field("awsRegion")
    excluded = field("excluded")

    @cached_property
    def logicalResourceId(self):  # pragma: no cover
        return LogicalResourceId.make_one(self.boto3_raw_data["logicalResourceId"])

    physicalResourceId = field("physicalResourceId")
    resourceName = field("resourceName")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAppVersionResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppVersionResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResiliencyPolicyRequest:
    boto3_raw_data: "type_defs.CreateResiliencyPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    policy = field("policy")
    policyName = field("policyName")
    tier = field("tier")
    clientToken = field("clientToken")
    dataLocationConstraint = field("dataLocationConstraint")
    policyDescription = field("policyDescription")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResiliencyPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResiliencyPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResiliencyPolicy:
    boto3_raw_data: "type_defs.ResiliencyPolicyTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    dataLocationConstraint = field("dataLocationConstraint")
    estimatedCostTier = field("estimatedCostTier")
    policy = field("policy")
    policyArn = field("policyArn")
    policyDescription = field("policyDescription")
    policyName = field("policyName")
    tags = field("tags")
    tier = field("tier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResiliencyPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResiliencyPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResiliencyPolicyRequest:
    boto3_raw_data: "type_defs.UpdateResiliencyPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    dataLocationConstraint = field("dataLocationConstraint")
    policy = field("policy")
    policyDescription = field("policyDescription")
    policyName = field("policyName")
    tier = field("tier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResiliencyPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResiliencyPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDraftAppVersionResourcesImportStatusResponse:
    boto3_raw_data: (
        "type_defs.DescribeDraftAppVersionResourcesImportStatusResponseTypeDef"
    ) = dataclasses.field()

    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def errorDetails(self):  # pragma: no cover
        return ErrorDetail.make_many(self.boto3_raw_data["errorDetails"])

    errorMessage = field("errorMessage")
    status = field("status")
    statusChangeTime = field("statusChangeTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDraftAppVersionResourcesImportStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeDraftAppVersionResourcesImportStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetricsExportResponse:
    boto3_raw_data: "type_defs.DescribeMetricsExportResponseTypeDef" = (
        dataclasses.field()
    )

    errorMessage = field("errorMessage")

    @cached_property
    def exportLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["exportLocation"])

    metricsExportId = field("metricsExportId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMetricsExportResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricsExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationTemplate:
    boto3_raw_data: "type_defs.RecommendationTemplateTypeDef" = dataclasses.field()

    assessmentArn = field("assessmentArn")
    format = field("format")
    name = field("name")
    recommendationTemplateArn = field("recommendationTemplateArn")
    recommendationTypes = field("recommendationTypes")
    status = field("status")
    appArn = field("appArn")
    endTime = field("endTime")
    message = field("message")
    needsReplacements = field("needsReplacements")
    recommendationIds = field("recommendationIds")
    startTime = field("startTime")
    tags = field("tags")

    @cached_property
    def templatesLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["templatesLocation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportResourcesToDraftAppVersionResponse:
    boto3_raw_data: "type_defs.ImportResourcesToDraftAppVersionResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def eksSources(self):  # pragma: no cover
        return EksSourceOutput.make_many(self.boto3_raw_data["eksSources"])

    sourceArns = field("sourceArns")
    status = field("status")

    @cached_property
    def terraformSources(self):  # pragma: no cover
        return TerraformSource.make_many(self.boto3_raw_data["terraformSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportResourcesToDraftAppVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportResourcesToDraftAppVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationItem:
    boto3_raw_data: "type_defs.RecommendationItemTypeDef" = dataclasses.field()

    alreadyImplemented = field("alreadyImplemented")

    @cached_property
    def discoveredAlarm(self):  # pragma: no cover
        return Alarm.make_one(self.boto3_raw_data["discoveredAlarm"])

    excludeReason = field("excludeReason")
    excluded = field("excluded")

    @cached_property
    def latestDiscoveredExperiment(self):  # pragma: no cover
        return Experiment.make_one(self.boto3_raw_data["latestDiscoveredExperiment"])

    resourceId = field("resourceId")
    targetAccountId = field("targetAccountId")
    targetRegion = field("targetRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupingResource:
    boto3_raw_data: "type_defs.GroupingResourceTypeDef" = dataclasses.field()

    @cached_property
    def logicalResourceId(self):  # pragma: no cover
        return LogicalResourceId.make_one(self.boto3_raw_data["logicalResourceId"])

    @cached_property
    def physicalResourceId(self):  # pragma: no cover
        return PhysicalResourceId.make_one(self.boto3_raw_data["physicalResourceId"])

    resourceName = field("resourceName")
    resourceType = field("resourceType")
    sourceAppComponentIds = field("sourceAppComponentIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupingResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupingResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhysicalResource:
    boto3_raw_data: "type_defs.PhysicalResourceTypeDef" = dataclasses.field()

    @cached_property
    def logicalResourceId(self):  # pragma: no cover
        return LogicalResourceId.make_one(self.boto3_raw_data["logicalResourceId"])

    @cached_property
    def physicalResourceId(self):  # pragma: no cover
        return PhysicalResourceId.make_one(self.boto3_raw_data["physicalResourceId"])

    resourceType = field("resourceType")
    additionalInfo = field("additionalInfo")

    @cached_property
    def appComponents(self):  # pragma: no cover
        return AppComponent.make_many(self.boto3_raw_data["appComponents"])

    excluded = field("excluded")
    parentResourceName = field("parentResourceName")
    resourceName = field("resourceName")
    sourceType = field("sourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhysicalResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhysicalResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceMapping:
    boto3_raw_data: "type_defs.ResourceMappingTypeDef" = dataclasses.field()

    mappingType = field("mappingType")

    @cached_property
    def physicalResourceId(self):  # pragma: no cover
        return PhysicalResourceId.make_one(self.boto3_raw_data["physicalResourceId"])

    appRegistryAppName = field("appRegistryAppName")
    eksSourceName = field("eksSourceName")
    logicalStackName = field("logicalStackName")
    resourceGroupName = field("resourceGroupName")
    resourceName = field("resourceName")
    terraformSourceName = field("terraformSourceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnsupportedResource:
    boto3_raw_data: "type_defs.UnsupportedResourceTypeDef" = dataclasses.field()

    @cached_property
    def logicalResourceId(self):  # pragma: no cover
        return LogicalResourceId.make_one(self.boto3_raw_data["logicalResourceId"])

    @cached_property
    def physicalResourceId(self):  # pragma: no cover
        return PhysicalResourceId.make_one(self.boto3_raw_data["physicalResourceId"])

    resourceType = field("resourceType")
    unsupportedResourceStatus = field("unsupportedResourceStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnsupportedResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnsupportedResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppAssessmentResourceDriftsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAppAssessmentResourceDriftsRequestPaginateTypeDef"
    ) = dataclasses.field()

    assessmentArn = field("assessmentArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppAssessmentResourceDriftsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListAppAssessmentResourceDriftsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceGroupingRecommendationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListResourceGroupingRecommendationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    appArn = field("appArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceGroupingRecommendationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListResourceGroupingRecommendationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppVersionsRequest:
    boto3_raw_data: "type_defs.ListAppVersionsRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    endTime = field("endTime")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    startTime = field("startTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsRequest:
    boto3_raw_data: "type_defs.ListAppsRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    awsApplicationArn = field("awsApplicationArn")
    fromLastAssessmentTime = field("fromLastAssessmentTime")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")
    reverseOrder = field("reverseOrder")
    toLastAssessmentTime = field("toLastAssessmentTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAppsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListAppsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricsRequestPaginate:
    boto3_raw_data: "type_defs.ListMetricsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def conditions(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["conditions"])

    dataSource = field("dataSource")

    @cached_property
    def fields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["fields"])

    @cached_property
    def sorts(self):  # pragma: no cover
        return Sort.make_many(self.boto3_raw_data["sorts"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricsRequest:
    boto3_raw_data: "type_defs.ListMetricsRequestTypeDef" = dataclasses.field()

    @cached_property
    def conditions(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["conditions"])

    dataSource = field("dataSource")

    @cached_property
    def fields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["fields"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def sorts(self):  # pragma: no cover
        return Sort.make_many(self.boto3_raw_data["sorts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectResourceGroupingRecommendationsRequest:
    boto3_raw_data: "type_defs.RejectResourceGroupingRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def entries(self):  # pragma: no cover
        return RejectGroupingRecommendationEntry.make_many(
            self.boto3_raw_data["entries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectResourceGroupingRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectResourceGroupingRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResiliencyScore:
    boto3_raw_data: "type_defs.ResiliencyScoreTypeDef" = dataclasses.field()

    disruptionScore = field("disruptionScore")
    score = field("score")
    componentScore = field("componentScore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResiliencyScoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResiliencyScoreTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceErrorsDetails:
    boto3_raw_data: "type_defs.ResourceErrorsDetailsTypeDef" = dataclasses.field()

    hasMoreErrors = field("hasMoreErrors")

    @cached_property
    def resourceErrors(self):  # pragma: no cover
        return ResourceError.make_many(self.boto3_raw_data["resourceErrors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceErrorsDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceErrorsDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppAssessmentsResponse:
    boto3_raw_data: "type_defs.ListAppAssessmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def assessmentSummaries(self):  # pragma: no cover
        return AppAssessmentSummary.make_many(
            self.boto3_raw_data["assessmentSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppAssessmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppAssessmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppAssessmentComplianceDriftsResponse:
    boto3_raw_data: "type_defs.ListAppAssessmentComplianceDriftsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def complianceDrifts(self):  # pragma: no cover
        return ComplianceDrift.make_many(self.boto3_raw_data["complianceDrifts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppAssessmentComplianceDriftsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppAssessmentComplianceDriftsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppInputSourceResponse:
    boto3_raw_data: "type_defs.DeleteAppInputSourceResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def appInputSource(self):  # pragma: no cover
        return AppInputSource.make_one(self.boto3_raw_data["appInputSource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAppInputSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppInputSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppInputSourcesResponse:
    boto3_raw_data: "type_defs.ListAppInputSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def appInputSources(self):  # pragma: no cover
        return AppInputSource.make_many(self.boto3_raw_data["appInputSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppInputSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppInputSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppResponse:
    boto3_raw_data: "type_defs.CreateAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def app(self):  # pragma: no cover
        return App.make_one(self.boto3_raw_data["app"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppResponse:
    boto3_raw_data: "type_defs.DescribeAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def app(self):  # pragma: no cover
        return App.make_one(self.boto3_raw_data["app"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppResponse:
    boto3_raw_data: "type_defs.UpdateAppResponseTypeDef" = dataclasses.field()

    @cached_property
    def app(self):  # pragma: no cover
        return App.make_one(self.boto3_raw_data["app"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAppResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateRecommendationStatusResponse:
    boto3_raw_data: "type_defs.BatchUpdateRecommendationStatusResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def failedEntries(self):  # pragma: no cover
        return BatchUpdateRecommendationStatusFailedEntry.make_many(
            self.boto3_raw_data["failedEntries"]
        )

    @cached_property
    def successfulEntries(self):  # pragma: no cover
        return BatchUpdateRecommendationStatusSuccessfulEntry.make_many(
            self.boto3_raw_data["successfulEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateRecommendationStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateRecommendationStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateRecommendationStatusRequest:
    boto3_raw_data: "type_defs.BatchUpdateRecommendationStatusRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def requestEntries(self):  # pragma: no cover
        return UpdateRecommendationStatusRequestEntry.make_many(
            self.boto3_raw_data["requestEntries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateRecommendationStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateRecommendationStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentRecommendation:
    boto3_raw_data: "type_defs.ComponentRecommendationTypeDef" = dataclasses.field()

    appComponentName = field("appComponentName")

    @cached_property
    def configRecommendations(self):  # pragma: no cover
        return ConfigRecommendation.make_many(
            self.boto3_raw_data["configRecommendations"]
        )

    recommendationStatus = field("recommendationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDrift:
    boto3_raw_data: "type_defs.ResourceDriftTypeDef" = dataclasses.field()

    appArn = field("appArn")
    appVersion = field("appVersion")
    diffType = field("diffType")
    referenceId = field("referenceId")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceDriftTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceDriftTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResiliencyPolicyResponse:
    boto3_raw_data: "type_defs.CreateResiliencyPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return ResiliencyPolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResiliencyPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResiliencyPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResiliencyPolicyResponse:
    boto3_raw_data: "type_defs.DescribeResiliencyPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return ResiliencyPolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResiliencyPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResiliencyPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResiliencyPoliciesResponse:
    boto3_raw_data: "type_defs.ListResiliencyPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resiliencyPolicies(self):  # pragma: no cover
        return ResiliencyPolicy.make_many(self.boto3_raw_data["resiliencyPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResiliencyPoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResiliencyPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSuggestedResiliencyPoliciesResponse:
    boto3_raw_data: "type_defs.ListSuggestedResiliencyPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resiliencyPolicies(self):  # pragma: no cover
        return ResiliencyPolicy.make_many(self.boto3_raw_data["resiliencyPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSuggestedResiliencyPoliciesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSuggestedResiliencyPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResiliencyPolicyResponse:
    boto3_raw_data: "type_defs.UpdateResiliencyPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return ResiliencyPolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResiliencyPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResiliencyPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecommendationTemplateResponse:
    boto3_raw_data: "type_defs.CreateRecommendationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def recommendationTemplate(self):  # pragma: no cover
        return RecommendationTemplate.make_one(
            self.boto3_raw_data["recommendationTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRecommendationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecommendationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationTemplatesResponse:
    boto3_raw_data: "type_defs.ListRecommendationTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def recommendationTemplates(self):  # pragma: no cover
        return RecommendationTemplate.make_many(
            self.boto3_raw_data["recommendationTemplates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportResourcesToDraftAppVersionRequest:
    boto3_raw_data: "type_defs.ImportResourcesToDraftAppVersionRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    eksSources = field("eksSources")
    importStrategy = field("importStrategy")
    sourceArns = field("sourceArns")

    @cached_property
    def terraformSources(self):  # pragma: no cover
        return TerraformSource.make_many(self.boto3_raw_data["terraformSources"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportResourcesToDraftAppVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportResourcesToDraftAppVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmRecommendation:
    boto3_raw_data: "type_defs.AlarmRecommendationTypeDef" = dataclasses.field()

    name = field("name")
    recommendationId = field("recommendationId")
    referenceId = field("referenceId")
    type = field("type")
    appComponentName = field("appComponentName")
    appComponentNames = field("appComponentNames")
    description = field("description")

    @cached_property
    def items(self):  # pragma: no cover
        return RecommendationItem.make_many(self.boto3_raw_data["items"])

    prerequisite = field("prerequisite")
    recommendationStatus = field("recommendationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlarmRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SopRecommendation:
    boto3_raw_data: "type_defs.SopRecommendationTypeDef" = dataclasses.field()

    recommendationId = field("recommendationId")
    referenceId = field("referenceId")
    serviceType = field("serviceType")
    appComponentName = field("appComponentName")
    description = field("description")

    @cached_property
    def items(self):  # pragma: no cover
        return RecommendationItem.make_many(self.boto3_raw_data["items"])

    name = field("name")
    prerequisite = field("prerequisite")
    recommendationStatus = field("recommendationStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SopRecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SopRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRecommendation:
    boto3_raw_data: "type_defs.TestRecommendationTypeDef" = dataclasses.field()

    referenceId = field("referenceId")
    appComponentId = field("appComponentId")
    appComponentName = field("appComponentName")
    dependsOnAlarms = field("dependsOnAlarms")
    description = field("description")
    intent = field("intent")

    @cached_property
    def items(self):  # pragma: no cover
        return RecommendationItem.make_many(self.boto3_raw_data["items"])

    name = field("name")
    prerequisite = field("prerequisite")
    recommendationId = field("recommendationId")
    recommendationStatus = field("recommendationStatus")
    risk = field("risk")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupingRecommendation:
    boto3_raw_data: "type_defs.GroupingRecommendationTypeDef" = dataclasses.field()

    confidenceLevel = field("confidenceLevel")
    creationTime = field("creationTime")

    @cached_property
    def groupingAppComponent(self):  # pragma: no cover
        return GroupingAppComponent.make_one(
            self.boto3_raw_data["groupingAppComponent"]
        )

    groupingRecommendationId = field("groupingRecommendationId")
    recommendationReasons = field("recommendationReasons")

    @cached_property
    def resources(self):  # pragma: no cover
        return GroupingResource.make_many(self.boto3_raw_data["resources"])

    score = field("score")
    status = field("status")
    rejectionReason = field("rejectionReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GroupingRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupingRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppVersionResourceResponse:
    boto3_raw_data: "type_defs.CreateAppVersionResourceResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def physicalResource(self):  # pragma: no cover
        return PhysicalResource.make_one(self.boto3_raw_data["physicalResource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAppVersionResourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppVersionResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppVersionResourceResponse:
    boto3_raw_data: "type_defs.DeleteAppVersionResourceResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def physicalResource(self):  # pragma: no cover
        return PhysicalResource.make_one(self.boto3_raw_data["physicalResource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAppVersionResourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppVersionResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppVersionResourceResponse:
    boto3_raw_data: "type_defs.DescribeAppVersionResourceResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def physicalResource(self):  # pragma: no cover
        return PhysicalResource.make_one(self.boto3_raw_data["physicalResource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppVersionResourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppVersionResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppVersionResourcesResponse:
    boto3_raw_data: "type_defs.ListAppVersionResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def physicalResources(self):  # pragma: no cover
        return PhysicalResource.make_many(self.boto3_raw_data["physicalResources"])

    resolutionId = field("resolutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAppVersionResourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppVersionResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppVersionResourceResponse:
    boto3_raw_data: "type_defs.UpdateAppVersionResourceResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def physicalResource(self):  # pragma: no cover
        return PhysicalResource.make_one(self.boto3_raw_data["physicalResource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAppVersionResourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppVersionResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddDraftAppVersionResourceMappingsRequest:
    boto3_raw_data: "type_defs.AddDraftAppVersionResourceMappingsRequestTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")

    @cached_property
    def resourceMappings(self):  # pragma: no cover
        return ResourceMapping.make_many(self.boto3_raw_data["resourceMappings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddDraftAppVersionResourceMappingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddDraftAppVersionResourceMappingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddDraftAppVersionResourceMappingsResponse:
    boto3_raw_data: "type_defs.AddDraftAppVersionResourceMappingsResponseTypeDef" = (
        dataclasses.field()
    )

    appArn = field("appArn")
    appVersion = field("appVersion")

    @cached_property
    def resourceMappings(self):  # pragma: no cover
        return ResourceMapping.make_many(self.boto3_raw_data["resourceMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddDraftAppVersionResourceMappingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddDraftAppVersionResourceMappingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppVersionResourceMappingsResponse:
    boto3_raw_data: "type_defs.ListAppVersionResourceMappingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resourceMappings(self):  # pragma: no cover
        return ResourceMapping.make_many(self.boto3_raw_data["resourceMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppVersionResourceMappingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppVersionResourceMappingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUnsupportedAppVersionResourcesResponse:
    boto3_raw_data: "type_defs.ListUnsupportedAppVersionResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    resolutionId = field("resolutionId")

    @cached_property
    def unsupportedResources(self):  # pragma: no cover
        return UnsupportedResource.make_many(
            self.boto3_raw_data["unsupportedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUnsupportedAppVersionResourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUnsupportedAppVersionResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppRequest:
    boto3_raw_data: "type_defs.CreateAppRequestTypeDef" = dataclasses.field()

    name = field("name")
    assessmentSchedule = field("assessmentSchedule")
    awsApplicationArn = field("awsApplicationArn")
    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def eventSubscriptions(self):  # pragma: no cover
        return EventSubscription.make_many(self.boto3_raw_data["eventSubscriptions"])

    permissionModel = field("permissionModel")
    policyArn = field("policyArn")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppRequest:
    boto3_raw_data: "type_defs.UpdateAppRequestTypeDef" = dataclasses.field()

    appArn = field("appArn")
    assessmentSchedule = field("assessmentSchedule")
    clearResiliencyPolicyArn = field("clearResiliencyPolicyArn")
    description = field("description")

    @cached_property
    def eventSubscriptions(self):  # pragma: no cover
        return EventSubscription.make_many(self.boto3_raw_data["eventSubscriptions"])

    permissionModel = field("permissionModel")
    policyArn = field("policyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppComponentCompliance:
    boto3_raw_data: "type_defs.AppComponentComplianceTypeDef" = dataclasses.field()

    appComponentName = field("appComponentName")
    compliance = field("compliance")

    @cached_property
    def cost(self):  # pragma: no cover
        return Cost.make_one(self.boto3_raw_data["cost"])

    message = field("message")

    @cached_property
    def resiliencyScore(self):  # pragma: no cover
        return ResiliencyScore.make_one(self.boto3_raw_data["resiliencyScore"])

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppComponentComplianceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppComponentComplianceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppAssessment:
    boto3_raw_data: "type_defs.AppAssessmentTypeDef" = dataclasses.field()

    assessmentArn = field("assessmentArn")
    assessmentStatus = field("assessmentStatus")
    invoker = field("invoker")
    appArn = field("appArn")
    appVersion = field("appVersion")
    assessmentName = field("assessmentName")
    compliance = field("compliance")
    complianceStatus = field("complianceStatus")

    @cached_property
    def cost(self):  # pragma: no cover
        return Cost.make_one(self.boto3_raw_data["cost"])

    driftStatus = field("driftStatus")
    endTime = field("endTime")
    message = field("message")

    @cached_property
    def policy(self):  # pragma: no cover
        return ResiliencyPolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def resiliencyScore(self):  # pragma: no cover
        return ResiliencyScore.make_one(self.boto3_raw_data["resiliencyScore"])

    @cached_property
    def resourceErrorsDetails(self):  # pragma: no cover
        return ResourceErrorsDetails.make_one(
            self.boto3_raw_data["resourceErrorsDetails"]
        )

    startTime = field("startTime")

    @cached_property
    def summary(self):  # pragma: no cover
        return AssessmentSummary.make_one(self.boto3_raw_data["summary"])

    tags = field("tags")
    versionName = field("versionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppAssessmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppAssessmentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppComponentRecommendationsResponse:
    boto3_raw_data: "type_defs.ListAppComponentRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def componentRecommendations(self):  # pragma: no cover
        return ComponentRecommendation.make_many(
            self.boto3_raw_data["componentRecommendations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppComponentRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppComponentRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppAssessmentResourceDriftsResponse:
    boto3_raw_data: "type_defs.ListAppAssessmentResourceDriftsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resourceDrifts(self):  # pragma: no cover
        return ResourceDrift.make_many(self.boto3_raw_data["resourceDrifts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppAssessmentResourceDriftsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppAssessmentResourceDriftsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAlarmRecommendationsResponse:
    boto3_raw_data: "type_defs.ListAlarmRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def alarmRecommendations(self):  # pragma: no cover
        return AlarmRecommendation.make_many(
            self.boto3_raw_data["alarmRecommendations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAlarmRecommendationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAlarmRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSopRecommendationsResponse:
    boto3_raw_data: "type_defs.ListSopRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sopRecommendations(self):  # pragma: no cover
        return SopRecommendation.make_many(self.boto3_raw_data["sopRecommendations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSopRecommendationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSopRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRecommendationsResponse:
    boto3_raw_data: "type_defs.ListTestRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def testRecommendations(self):  # pragma: no cover
        return TestRecommendation.make_many(self.boto3_raw_data["testRecommendations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTestRecommendationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceGroupingRecommendationsResponse:
    boto3_raw_data: "type_defs.ListResourceGroupingRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def groupingRecommendations(self):  # pragma: no cover
        return GroupingRecommendation.make_many(
            self.boto3_raw_data["groupingRecommendations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceGroupingRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceGroupingRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppComponentCompliancesResponse:
    boto3_raw_data: "type_defs.ListAppComponentCompliancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def componentCompliances(self):  # pragma: no cover
        return AppComponentCompliance.make_many(
            self.boto3_raw_data["componentCompliances"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppComponentCompliancesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppComponentCompliancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppAssessmentResponse:
    boto3_raw_data: "type_defs.DescribeAppAssessmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessment(self):  # pragma: no cover
        return AppAssessment.make_one(self.boto3_raw_data["assessment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAppAssessmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAppAssessmentResponse:
    boto3_raw_data: "type_defs.StartAppAssessmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def assessment(self):  # pragma: no cover
        return AppAssessment.make_one(self.boto3_raw_data["assessment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAppAssessmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAppAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
