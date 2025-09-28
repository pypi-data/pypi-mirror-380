# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_qbusiness import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class S3:
    boto3_raw_data: "type_defs.S3TypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecutionPayloadFieldOutput:
    boto3_raw_data: "type_defs.ActionExecutionPayloadFieldOutputTypeDef" = (
        dataclasses.field()
    )

    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActionExecutionPayloadFieldOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionExecutionPayloadFieldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecutionPayloadField:
    boto3_raw_data: "type_defs.ActionExecutionPayloadFieldTypeDef" = dataclasses.field()

    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionPayloadFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionExecutionPayloadFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionReviewPayloadFieldAllowedValue:
    boto3_raw_data: "type_defs.ActionReviewPayloadFieldAllowedValueTypeDef" = (
        dataclasses.field()
    )

    value = field("value")
    displayValue = field("displayValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActionReviewPayloadFieldAllowedValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionReviewPayloadFieldAllowedValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionSummary:
    boto3_raw_data: "type_defs.ActionSummaryTypeDef" = dataclasses.field()

    actionIdentifier = field("actionIdentifier")
    displayName = field("displayName")
    instructionExample = field("instructionExample")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickSightConfiguration:
    boto3_raw_data: "type_defs.QuickSightConfigurationTypeDef" = dataclasses.field()

    clientNamespace = field("clientNamespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickSightConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickSightConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppliedAttachmentsConfiguration:
    boto3_raw_data: "type_defs.AppliedAttachmentsConfigurationTypeDef" = (
        dataclasses.field()
    )

    attachmentsControlMode = field("attachmentsControlMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AppliedAttachmentsConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppliedAttachmentsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppliedCreatorModeConfiguration:
    boto3_raw_data: "type_defs.AppliedCreatorModeConfigurationTypeDef" = (
        dataclasses.field()
    )

    creatorModeControl = field("creatorModeControl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AppliedCreatorModeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppliedCreatorModeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppliedOrchestrationConfiguration:
    boto3_raw_data: "type_defs.AppliedOrchestrationConfigurationTypeDef" = (
        dataclasses.field()
    )

    control = field("control")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AppliedOrchestrationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppliedOrchestrationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionCondition:
    boto3_raw_data: "type_defs.PermissionConditionTypeDef" = dataclasses.field()

    conditionOperator = field("conditionOperator")
    conditionKey = field("conditionKey")
    conditionValues = field("conditionValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PermissionConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionConditionTypeDef"]
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
class AssociatedGroup:
    boto3_raw_data: "type_defs.AssociatedGroupTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssociatedGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssociatedGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedUser:
    boto3_raw_data: "type_defs.AssociatedUserTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssociatedUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssociatedUserTypeDef"]],
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
    errorCode = field("errorCode")

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
class AttachmentsConfiguration:
    boto3_raw_data: "type_defs.AttachmentsConfigurationTypeDef" = dataclasses.field()

    attachmentsControlMode = field("attachmentsControlMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachmentsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioExtractionConfiguration:
    boto3_raw_data: "type_defs.AudioExtractionConfigurationTypeDef" = (
        dataclasses.field()
    )

    audioExtractionStatus = field("audioExtractionStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioExtractionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioExtractionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioSourceDetails:
    boto3_raw_data: "type_defs.AudioSourceDetailsTypeDef" = dataclasses.field()

    mediaId = field("mediaId")
    mediaMimeType = field("mediaMimeType")
    startTimeMilliseconds = field("startTimeMilliseconds")
    endTimeMilliseconds = field("endTimeMilliseconds")
    audioExtractionType = field("audioExtractionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioSourceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioSourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthChallengeRequestEvent:
    boto3_raw_data: "type_defs.AuthChallengeRequestEventTypeDef" = dataclasses.field()

    authorizationUrl = field("authorizationUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthChallengeRequestEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthChallengeRequestEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthChallengeRequest:
    boto3_raw_data: "type_defs.AuthChallengeRequestTypeDef" = dataclasses.field()

    authorizationUrl = field("authorizationUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthChallengeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthChallengeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthChallengeResponseEvent:
    boto3_raw_data: "type_defs.AuthChallengeResponseEventTypeDef" = dataclasses.field()

    responseMap = field("responseMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthChallengeResponseEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthChallengeResponseEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthChallengeResponse:
    boto3_raw_data: "type_defs.AuthChallengeResponseTypeDef" = dataclasses.field()

    responseMap = field("responseMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthChallengeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthChallengeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoSubscriptionConfiguration:
    boto3_raw_data: "type_defs.AutoSubscriptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    autoSubscribe = field("autoSubscribe")
    defaultSubscriptionType = field("defaultSubscriptionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutoSubscriptionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoSubscriptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BasicAuthConfiguration:
    boto3_raw_data: "type_defs.BasicAuthConfigurationTypeDef" = dataclasses.field()

    secretArn = field("secretArn")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BasicAuthConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BasicAuthConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDocument:
    boto3_raw_data: "type_defs.DeleteDocumentTypeDef" = dataclasses.field()

    documentId = field("documentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockedPhrasesConfiguration:
    boto3_raw_data: "type_defs.BlockedPhrasesConfigurationTypeDef" = dataclasses.field()

    blockedPhrases = field("blockedPhrases")
    systemMessageOverride = field("systemMessageOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BlockedPhrasesConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockedPhrasesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockedPhrasesConfigurationUpdate:
    boto3_raw_data: "type_defs.BlockedPhrasesConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    blockedPhrasesToCreateOrUpdate = field("blockedPhrasesToCreateOrUpdate")
    blockedPhrasesToDelete = field("blockedPhrasesToDelete")
    systemMessageOverride = field("systemMessageOverride")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BlockedPhrasesConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockedPhrasesConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserExtensionConfigurationOutput:
    boto3_raw_data: "type_defs.BrowserExtensionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    enabledBrowserExtensions = field("enabledBrowserExtensions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BrowserExtensionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrowserExtensionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserExtensionConfiguration:
    boto3_raw_data: "type_defs.BrowserExtensionConfigurationTypeDef" = (
        dataclasses.field()
    )

    enabledBrowserExtensions = field("enabledBrowserExtensions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BrowserExtensionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrowserExtensionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelSubscriptionRequest:
    boto3_raw_data: "type_defs.CancelSubscriptionRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    subscriptionId = field("subscriptionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSubscriptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionDetails:
    boto3_raw_data: "type_defs.SubscriptionDetailsTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscriptionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextInputEvent:
    boto3_raw_data: "type_defs.TextInputEventTypeDef" = dataclasses.field()

    userMessage = field("userMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextInputEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextInputEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PluginConfiguration:
    boto3_raw_data: "type_defs.PluginConfigurationTypeDef" = dataclasses.field()

    pluginId = field("pluginId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PluginConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PluginConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextOutputEvent:
    boto3_raw_data: "type_defs.TextOutputEventTypeDef" = dataclasses.field()

    systemMessageType = field("systemMessageType")
    conversationId = field("conversationId")
    userMessageId = field("userMessageId")
    systemMessageId = field("systemMessageId")
    systemMessage = field("systemMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextOutputEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextOutputEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatResponseConfiguration:
    boto3_raw_data: "type_defs.ChatResponseConfigurationTypeDef" = dataclasses.field()

    chatResponseConfigurationId = field("chatResponseConfigurationId")
    chatResponseConfigurationArn = field("chatResponseConfigurationArn")
    displayName = field("displayName")
    status = field("status")
    responseConfigurationSummary = field("responseConfigurationSummary")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChatResponseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChatResponseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckDocumentAccessRequest:
    boto3_raw_data: "type_defs.CheckDocumentAccessRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    userId = field("userId")
    documentId = field("documentId")
    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckDocumentAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckDocumentAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBlockerRule:
    boto3_raw_data: "type_defs.ContentBlockerRuleTypeDef" = dataclasses.field()

    systemMessageOverride = field("systemMessageOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentBlockerRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentBlockerRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EligibleDataSource:
    boto3_raw_data: "type_defs.EligibleDataSourceTypeDef" = dataclasses.field()

    indexId = field("indexId")
    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EligibleDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EligibleDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieverContentSource:
    boto3_raw_data: "type_defs.RetrieverContentSourceTypeDef" = dataclasses.field()

    retrieverId = field("retrieverId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieverContentSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieverContentSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationSource:
    boto3_raw_data: "type_defs.ConversationSourceTypeDef" = dataclasses.field()

    conversationId = field("conversationId")
    attachmentId = field("attachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversationSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Conversation:
    boto3_raw_data: "type_defs.ConversationTypeDef" = dataclasses.field()

    conversationId = field("conversationId")
    title = field("title")
    startTime = field("startTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConversationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConversationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnonymousWebExperienceUrlRequest:
    boto3_raw_data: "type_defs.CreateAnonymousWebExperienceUrlRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    webExperienceId = field("webExperienceId")
    sessionDurationInMinutes = field("sessionDurationInMinutes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAnonymousWebExperienceUrlRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnonymousWebExperienceUrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PersonalizationConfiguration:
    boto3_raw_data: "type_defs.PersonalizationConfigurationTypeDef" = (
        dataclasses.field()
    )

    personalizationControlMode = field("personalizationControlMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PersonalizationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PersonalizationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QAppsConfiguration:
    boto3_raw_data: "type_defs.QAppsConfigurationTypeDef" = dataclasses.field()

    qAppsControlMode = field("qAppsControlMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QAppsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QAppsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexCapacityConfiguration:
    boto3_raw_data: "type_defs.IndexCapacityConfigurationTypeDef" = dataclasses.field()

    units = field("units")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndexCapacityConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexCapacityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionPrincipal:
    boto3_raw_data: "type_defs.SubscriptionPrincipalTypeDef" = dataclasses.field()

    user = field("user")
    group = field("group")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscriptionPrincipalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserAlias:
    boto3_raw_data: "type_defs.UserAliasTypeDef" = dataclasses.field()

    userId = field("userId")
    indexId = field("indexId")
    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserAliasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserAliasTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizationConfiguration:
    boto3_raw_data: "type_defs.CustomizationConfigurationTypeDef" = dataclasses.field()

    customCSSUrl = field("customCSSUrl")
    logoUrl = field("logoUrl")
    fontUrl = field("fontUrl")
    faviconUrl = field("faviconUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomizationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatorModeConfiguration:
    boto3_raw_data: "type_defs.CreatorModeConfigurationTypeDef" = dataclasses.field()

    creatorModeControl = field("creatorModeControl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatorModeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatorModeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataAccessorIdcTrustedTokenIssuerConfiguration:
    boto3_raw_data: (
        "type_defs.DataAccessorIdcTrustedTokenIssuerConfigurationTypeDef"
    ) = dataclasses.field()

    idcTrustedTokenIssuerArn = field("idcTrustedTokenIssuerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataAccessorIdcTrustedTokenIssuerConfigurationTypeDef"
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
                "type_defs.DataAccessorIdcTrustedTokenIssuerConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceSyncJobMetrics:
    boto3_raw_data: "type_defs.DataSourceSyncJobMetricsTypeDef" = dataclasses.field()

    documentsAdded = field("documentsAdded")
    documentsModified = field("documentsModified")
    documentsDeleted = field("documentsDeleted")
    documentsFailed = field("documentsFailed")
    documentsScanned = field("documentsScanned")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceSyncJobMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceSyncJobMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    displayName = field("displayName")
    dataSourceId = field("dataSourceId")
    type = field("type")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceVpcConfigurationOutput:
    boto3_raw_data: "type_defs.DataSourceVpcConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceVpcConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceVpcConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceVpcConfiguration:
    boto3_raw_data: "type_defs.DataSourceVpcConfigurationTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceVpcConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceVpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateAttributeBoostingConfiguration:
    boto3_raw_data: "type_defs.DateAttributeBoostingConfigurationTypeDef" = (
        dataclasses.field()
    )

    boostingLevel = field("boostingLevel")
    boostingDurationInSeconds = field("boostingDurationInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DateAttributeBoostingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DateAttributeBoostingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationRequest:
    boto3_raw_data: "type_defs.DeleteApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAttachmentRequest:
    boto3_raw_data: "type_defs.DeleteAttachmentRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    conversationId = field("conversationId")
    attachmentId = field("attachmentId")
    userId = field("userId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChatControlsConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteChatControlsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteChatControlsConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChatControlsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChatResponseConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteChatResponseConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    chatResponseConfigurationId = field("chatResponseConfigurationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteChatResponseConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChatResponseConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConversationRequest:
    boto3_raw_data: "type_defs.DeleteConversationRequestTypeDef" = dataclasses.field()

    conversationId = field("conversationId")
    applicationId = field("applicationId")
    userId = field("userId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConversationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConversationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataAccessorRequest:
    boto3_raw_data: "type_defs.DeleteDataAccessorRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    dataAccessorId = field("dataAccessorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataAccessorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataAccessorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceRequest:
    boto3_raw_data: "type_defs.DeleteDataSourceRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGroupRequest:
    boto3_raw_data: "type_defs.DeleteGroupRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    groupName = field("groupName")
    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIndexRequest:
    boto3_raw_data: "type_defs.DeleteIndexRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePluginRequest:
    boto3_raw_data: "type_defs.DeletePluginRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    pluginId = field("pluginId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePluginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePluginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRetrieverRequest:
    boto3_raw_data: "type_defs.DeleteRetrieverRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    retrieverId = field("retrieverId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRetrieverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRetrieverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserRequest:
    boto3_raw_data: "type_defs.DeleteUserRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    userId = field("userId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWebExperienceRequest:
    boto3_raw_data: "type_defs.DeleteWebExperienceRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    webExperienceId = field("webExperienceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWebExperienceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWebExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePermissionRequest:
    boto3_raw_data: "type_defs.DisassociatePermissionRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    statementId = field("statementId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociatePermissionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociatePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAclGroup:
    boto3_raw_data: "type_defs.DocumentAclGroupTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentAclGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAclGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAclUser:
    boto3_raw_data: "type_defs.DocumentAclUserTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentAclUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentAclUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NumberAttributeBoostingConfiguration:
    boto3_raw_data: "type_defs.NumberAttributeBoostingConfigurationTypeDef" = (
        dataclasses.field()
    )

    boostingLevel = field("boostingLevel")
    boostingType = field("boostingType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NumberAttributeBoostingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NumberAttributeBoostingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringAttributeBoostingConfigurationOutput:
    boto3_raw_data: "type_defs.StringAttributeBoostingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    boostingLevel = field("boostingLevel")
    attributeValueBoosting = field("attributeValueBoosting")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StringAttributeBoostingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StringAttributeBoostingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringListAttributeBoostingConfiguration:
    boto3_raw_data: "type_defs.StringListAttributeBoostingConfigurationTypeDef" = (
        dataclasses.field()
    )

    boostingLevel = field("boostingLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StringListAttributeBoostingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StringListAttributeBoostingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringAttributeBoostingConfiguration:
    boto3_raw_data: "type_defs.StringAttributeBoostingConfigurationTypeDef" = (
        dataclasses.field()
    )

    boostingLevel = field("boostingLevel")
    attributeValueBoosting = field("attributeValueBoosting")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StringAttributeBoostingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StringAttributeBoostingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeValueOutput:
    boto3_raw_data: "type_defs.DocumentAttributeValueOutputTypeDef" = (
        dataclasses.field()
    )

    stringValue = field("stringValue")
    stringListValue = field("stringListValue")
    longValue = field("longValue")
    dateValue = field("dateValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeConfiguration:
    boto3_raw_data: "type_defs.DocumentAttributeConfigurationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    type = field("type")
    search = field("search")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentAttributeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationRequest:
    boto3_raw_data: "type_defs.GetApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationRequestTypeDef"]
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
class GetChatControlsConfigurationRequest:
    boto3_raw_data: "type_defs.GetChatControlsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetChatControlsConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChatControlsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HallucinationReductionConfiguration:
    boto3_raw_data: "type_defs.HallucinationReductionConfigurationTypeDef" = (
        dataclasses.field()
    )

    hallucinationReductionControl = field("hallucinationReductionControl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HallucinationReductionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HallucinationReductionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChatResponseConfigurationRequest:
    boto3_raw_data: "type_defs.GetChatResponseConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    chatResponseConfigurationId = field("chatResponseConfigurationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetChatResponseConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChatResponseConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataAccessorRequest:
    boto3_raw_data: "type_defs.GetDataAccessorRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    dataAccessorId = field("dataAccessorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataAccessorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataAccessorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceRequest:
    boto3_raw_data: "type_defs.GetDataSourceRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentContentRequest:
    boto3_raw_data: "type_defs.GetDocumentContentRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    documentId = field("documentId")
    dataSourceId = field("dataSourceId")
    outputFormat = field("outputFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupRequest:
    boto3_raw_data: "type_defs.GetGroupRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    groupName = field("groupName")
    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGroupRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIndexRequest:
    boto3_raw_data: "type_defs.GetIndexRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIndexRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetIndexRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaRequest:
    boto3_raw_data: "type_defs.GetMediaRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    conversationId = field("conversationId")
    messageId = field("messageId")
    mediaId = field("mediaId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMediaRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetMediaRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPluginRequest:
    boto3_raw_data: "type_defs.GetPluginRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    pluginId = field("pluginId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPluginRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPluginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyRequest:
    boto3_raw_data: "type_defs.GetPolicyRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRetrieverRequest:
    boto3_raw_data: "type_defs.GetRetrieverRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    retrieverId = field("retrieverId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRetrieverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRetrieverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserRequest:
    boto3_raw_data: "type_defs.GetUserRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    userId = field("userId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetUserRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWebExperienceRequest:
    boto3_raw_data: "type_defs.GetWebExperienceRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    webExperienceId = field("webExperienceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWebExperienceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWebExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberGroup:
    boto3_raw_data: "type_defs.MemberGroupTypeDef" = dataclasses.field()

    groupName = field("groupName")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberUser:
    boto3_raw_data: "type_defs.MemberUserTypeDef" = dataclasses.field()

    userId = field("userId")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupSummary:
    boto3_raw_data: "type_defs.GroupSummaryTypeDef" = dataclasses.field()

    groupName = field("groupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdcAuthConfiguration:
    boto3_raw_data: "type_defs.IdcAuthConfigurationTypeDef" = dataclasses.field()

    idcApplicationArn = field("idcApplicationArn")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdcAuthConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdcAuthConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIDConnectProviderConfiguration:
    boto3_raw_data: "type_defs.OpenIDConnectProviderConfigurationTypeDef" = (
        dataclasses.field()
    )

    secretsArn = field("secretsArn")
    secretsRole = field("secretsRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIDConnectProviderConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIDConnectProviderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamlProviderConfiguration:
    boto3_raw_data: "type_defs.SamlProviderConfigurationTypeDef" = dataclasses.field()

    authenticationUrl = field("authenticationUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SamlProviderConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamlProviderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageExtractionConfiguration:
    boto3_raw_data: "type_defs.ImageExtractionConfigurationTypeDef" = (
        dataclasses.field()
    )

    imageExtractionStatus = field("imageExtractionStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageExtractionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageExtractionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageSourceDetails:
    boto3_raw_data: "type_defs.ImageSourceDetailsTypeDef" = dataclasses.field()

    mediaId = field("mediaId")
    mediaMimeType = field("mediaMimeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageSourceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageSourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextDocumentStatistics:
    boto3_raw_data: "type_defs.TextDocumentStatisticsTypeDef" = dataclasses.field()

    indexedTextBytes = field("indexedTextBytes")
    indexedTextDocumentCount = field("indexedTextDocumentCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextDocumentStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextDocumentStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Index:
    boto3_raw_data: "type_defs.IndexTypeDef" = dataclasses.field()

    displayName = field("displayName")
    indexId = field("indexId")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstructionCollection:
    boto3_raw_data: "type_defs.InstructionCollectionTypeDef" = dataclasses.field()

    responseLength = field("responseLength")
    targetAudience = field("targetAudience")
    perspective = field("perspective")
    outputStyle = field("outputStyle")
    identity = field("identity")
    tone = field("tone")
    customInstructions = field("customInstructions")
    examples = field("examples")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstructionCollectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstructionCollectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KendraIndexConfiguration:
    boto3_raw_data: "type_defs.KendraIndexConfigurationTypeDef" = dataclasses.field()

    indexId = field("indexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KendraIndexConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KendraIndexConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachmentsRequest:
    boto3_raw_data: "type_defs.ListAttachmentsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    conversationId = field("conversationId")
    userId = field("userId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttachmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChatResponseConfigurationsRequest:
    boto3_raw_data: "type_defs.ListChatResponseConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChatResponseConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChatResponseConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConversationsRequest:
    boto3_raw_data: "type_defs.ListConversationsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    userId = field("userId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConversationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConversationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataAccessorsRequest:
    boto3_raw_data: "type_defs.ListDataAccessorsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataAccessorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataAccessorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesRequest:
    boto3_raw_data: "type_defs.ListDataSourcesRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentsRequest:
    boto3_raw_data: "type_defs.ListDocumentsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    dataSourceIds = field("dataSourceIds")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDocumentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicesRequest:
    boto3_raw_data: "type_defs.ListIndicesRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessagesRequest:
    boto3_raw_data: "type_defs.ListMessagesRequestTypeDef" = dataclasses.field()

    conversationId = field("conversationId")
    applicationId = field("applicationId")
    userId = field("userId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginActionsRequest:
    boto3_raw_data: "type_defs.ListPluginActionsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    pluginId = field("pluginId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPluginActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginTypeActionsRequest:
    boto3_raw_data: "type_defs.ListPluginTypeActionsRequestTypeDef" = (
        dataclasses.field()
    )

    pluginType = field("pluginType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPluginTypeActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginTypeActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginTypeMetadataRequest:
    boto3_raw_data: "type_defs.ListPluginTypeMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPluginTypeMetadataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginTypeMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PluginTypeMetadataSummary:
    boto3_raw_data: "type_defs.PluginTypeMetadataSummaryTypeDef" = dataclasses.field()

    type = field("type")
    category = field("category")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PluginTypeMetadataSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PluginTypeMetadataSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginsRequest:
    boto3_raw_data: "type_defs.ListPluginsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPluginsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Plugin:
    boto3_raw_data: "type_defs.PluginTypeDef" = dataclasses.field()

    pluginId = field("pluginId")
    displayName = field("displayName")
    type = field("type")
    serverUrl = field("serverUrl")
    state = field("state")
    buildStatus = field("buildStatus")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PluginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PluginTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRetrieversRequest:
    boto3_raw_data: "type_defs.ListRetrieversRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRetrieversRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRetrieversRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Retriever:
    boto3_raw_data: "type_defs.RetrieverTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    retrieverId = field("retrieverId")
    type = field("type")
    status = field("status")
    displayName = field("displayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrieverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetrieverTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionsRequest:
    boto3_raw_data: "type_defs.ListSubscriptionsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubscriptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionsRequestTypeDef"]
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

    resourceARN = field("resourceARN")

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
class ListWebExperiencesRequest:
    boto3_raw_data: "type_defs.ListWebExperiencesRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebExperiencesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebExperiencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebExperience:
    boto3_raw_data: "type_defs.WebExperienceTypeDef" = dataclasses.field()

    webExperienceId = field("webExperienceId")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    defaultEndpoint = field("defaultEndpoint")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebExperienceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WebExperienceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoExtractionConfiguration:
    boto3_raw_data: "type_defs.VideoExtractionConfigurationTypeDef" = (
        dataclasses.field()
    )

    videoExtractionStatus = field("videoExtractionStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoExtractionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoExtractionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuth2ClientCredentialConfiguration:
    boto3_raw_data: "type_defs.OAuth2ClientCredentialConfigurationTypeDef" = (
        dataclasses.field()
    )

    secretArn = field("secretArn")
    roleArn = field("roleArn")
    authorizationUrl = field("authorizationUrl")
    tokenUrl = field("tokenUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OAuth2ClientCredentialConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuth2ClientCredentialConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrchestrationConfiguration:
    boto3_raw_data: "type_defs.OrchestrationConfigurationTypeDef" = dataclasses.field()

    control = field("control")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrchestrationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrchestrationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrincipalGroup:
    boto3_raw_data: "type_defs.PrincipalGroupTypeDef" = dataclasses.field()

    access = field("access")
    name = field("name")
    membershipType = field("membershipType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrincipalGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrincipalGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrincipalUser:
    boto3_raw_data: "type_defs.PrincipalUserTypeDef" = dataclasses.field()

    access = field("access")
    id = field("id")
    membershipType = field("membershipType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrincipalUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrincipalUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScoreAttributes:
    boto3_raw_data: "type_defs.ScoreAttributesTypeDef" = dataclasses.field()

    scoreConfidence = field("scoreConfidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScoreAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScoreAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsersAndGroupsOutput:
    boto3_raw_data: "type_defs.UsersAndGroupsOutputTypeDef" = dataclasses.field()

    userIds = field("userIds")
    userGroups = field("userGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsersAndGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsersAndGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamlConfiguration:
    boto3_raw_data: "type_defs.SamlConfigurationTypeDef" = dataclasses.field()

    metadataXML = field("metadataXML")
    roleArn = field("roleArn")
    userIdAttribute = field("userIdAttribute")
    userGroupAttribute = field("userGroupAttribute")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SamlConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamlConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnippetExcerpt:
    boto3_raw_data: "type_defs.SnippetExcerptTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnippetExcerptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnippetExcerptTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoSourceDetails:
    boto3_raw_data: "type_defs.VideoSourceDetailsTypeDef" = dataclasses.field()

    mediaId = field("mediaId")
    mediaMimeType = field("mediaMimeType")
    startTimeMilliseconds = field("startTimeMilliseconds")
    endTimeMilliseconds = field("endTimeMilliseconds")
    videoExtractionType = field("videoExtractionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoSourceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoSourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataSourceSyncJobRequest:
    boto3_raw_data: "type_defs.StartDataSourceSyncJobRequestTypeDef" = (
        dataclasses.field()
    )

    dataSourceId = field("dataSourceId")
    applicationId = field("applicationId")
    indexId = field("indexId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDataSourceSyncJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataSourceSyncJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDataSourceSyncJobRequest:
    boto3_raw_data: "type_defs.StopDataSourceSyncJobRequestTypeDef" = (
        dataclasses.field()
    )

    dataSourceId = field("dataSourceId")
    applicationId = field("applicationId")
    indexId = field("indexId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDataSourceSyncJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDataSourceSyncJobRequestTypeDef"]
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

    resourceARN = field("resourceARN")
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
class UpdateSubscriptionRequest:
    boto3_raw_data: "type_defs.UpdateSubscriptionRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    subscriptionId = field("subscriptionId")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSubscriptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsersAndGroups:
    boto3_raw_data: "type_defs.UsersAndGroupsTypeDef" = dataclasses.field()

    userIds = field("userIds")
    userGroups = field("userGroups")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsersAndGroupsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsersAndGroupsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APISchema:
    boto3_raw_data: "type_defs.APISchemaTypeDef" = dataclasses.field()

    payload = field("payload")

    @cached_property
    def s3(self):  # pragma: no cover
        return S3.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.APISchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.APISchemaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecutionOutput:
    boto3_raw_data: "type_defs.ActionExecutionOutputTypeDef" = dataclasses.field()

    pluginId = field("pluginId")
    payload = field("payload")
    payloadFieldNameSeparator = field("payloadFieldNameSeparator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecution:
    boto3_raw_data: "type_defs.ActionExecutionTypeDef" = dataclasses.field()

    pluginId = field("pluginId")
    payload = field("payload")
    payloadFieldNameSeparator = field("payloadFieldNameSeparator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionReviewPayloadField:
    boto3_raw_data: "type_defs.ActionReviewPayloadFieldTypeDef" = dataclasses.field()

    displayName = field("displayName")
    displayOrder = field("displayOrder")
    displayDescription = field("displayDescription")
    type = field("type")
    value = field("value")

    @cached_property
    def allowedValues(self):  # pragma: no cover
        return ActionReviewPayloadFieldAllowedValue.make_many(
            self.boto3_raw_data["allowedValues"]
        )

    allowedFormat = field("allowedFormat")
    arrayItemJsonSchema = field("arrayItemJsonSchema")
    required = field("required")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionReviewPayloadFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionReviewPayloadFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Application:
    boto3_raw_data: "type_defs.ApplicationTypeDef" = dataclasses.field()

    displayName = field("displayName")
    applicationId = field("applicationId")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")
    identityType = field("identityType")

    @cached_property
    def quickSightConfiguration(self):  # pragma: no cover
        return QuickSightConfiguration.make_one(
            self.boto3_raw_data["quickSightConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApplicationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePermissionRequest:
    boto3_raw_data: "type_defs.AssociatePermissionRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    statementId = field("statementId")
    actions = field("actions")
    principal = field("principal")

    @cached_property
    def conditions(self):  # pragma: no cover
        return PermissionCondition.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatePermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePermissionResponse:
    boto3_raw_data: "type_defs.AssociatePermissionResponseTypeDef" = dataclasses.field()

    statement = field("statement")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatePermissionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePermissionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnonymousWebExperienceUrlResponse:
    boto3_raw_data: "type_defs.CreateAnonymousWebExperienceUrlResponseTypeDef" = (
        dataclasses.field()
    )

    anonymousUrl = field("anonymousUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAnonymousWebExperienceUrlResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnonymousWebExperienceUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationResponse:
    boto3_raw_data: "type_defs.CreateApplicationResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    applicationArn = field("applicationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChatResponseConfigurationResponse:
    boto3_raw_data: "type_defs.CreateChatResponseConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    chatResponseConfigurationId = field("chatResponseConfigurationId")
    chatResponseConfigurationArn = field("chatResponseConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateChatResponseConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChatResponseConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataAccessorResponse:
    boto3_raw_data: "type_defs.CreateDataAccessorResponseTypeDef" = dataclasses.field()

    dataAccessorId = field("dataAccessorId")
    idcApplicationArn = field("idcApplicationArn")
    dataAccessorArn = field("dataAccessorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataAccessorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataAccessorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceResponse:
    boto3_raw_data: "type_defs.CreateDataSourceResponseTypeDef" = dataclasses.field()

    dataSourceId = field("dataSourceId")
    dataSourceArn = field("dataSourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIndexResponse:
    boto3_raw_data: "type_defs.CreateIndexResponseTypeDef" = dataclasses.field()

    indexId = field("indexId")
    indexArn = field("indexArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePluginResponse:
    boto3_raw_data: "type_defs.CreatePluginResponseTypeDef" = dataclasses.field()

    pluginId = field("pluginId")
    pluginArn = field("pluginArn")
    buildStatus = field("buildStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePluginResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePluginResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRetrieverResponse:
    boto3_raw_data: "type_defs.CreateRetrieverResponseTypeDef" = dataclasses.field()

    retrieverId = field("retrieverId")
    retrieverArn = field("retrieverArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRetrieverResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRetrieverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebExperienceResponse:
    boto3_raw_data: "type_defs.CreateWebExperienceResponseTypeDef" = dataclasses.field()

    webExperienceId = field("webExperienceId")
    webExperienceArn = field("webExperienceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebExperienceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebExperienceResponseTypeDef"]
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
class GetDocumentContentResponse:
    boto3_raw_data: "type_defs.GetDocumentContentResponseTypeDef" = dataclasses.field()

    presignedUrl = field("presignedUrl")
    mimeType = field("mimeType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaResponse:
    boto3_raw_data: "type_defs.GetMediaResponseTypeDef" = dataclasses.field()

    mediaBytes = field("mediaBytes")
    mediaMimeType = field("mediaMimeType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMediaResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyResponse:
    boto3_raw_data: "type_defs.GetPolicyResponseTypeDef" = dataclasses.field()

    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginActionsResponse:
    boto3_raw_data: "type_defs.ListPluginActionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ActionSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPluginActionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginTypeActionsResponse:
    boto3_raw_data: "type_defs.ListPluginTypeActionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return ActionSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPluginTypeActionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginTypeActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataSourceSyncJobResponse:
    boto3_raw_data: "type_defs.StartDataSourceSyncJobResponseTypeDef" = (
        dataclasses.field()
    )

    executionId = field("executionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDataSourceSyncJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataSourceSyncJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentContent:
    boto3_raw_data: "type_defs.DocumentContentTypeDef" = dataclasses.field()

    blob = field("blob")

    @cached_property
    def s3(self):  # pragma: no cover
        return S3.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentOutput:
    boto3_raw_data: "type_defs.AttachmentOutputTypeDef" = dataclasses.field()

    name = field("name")
    status = field("status")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    attachmentId = field("attachmentId")
    conversationId = field("conversationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentDetails:
    boto3_raw_data: "type_defs.DocumentDetailsTypeDef" = dataclasses.field()

    documentId = field("documentId")
    status = field("status")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedDocument:
    boto3_raw_data: "type_defs.FailedDocumentTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailedDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailedDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupStatusDetail:
    boto3_raw_data: "type_defs.GroupStatusDetailTypeDef" = dataclasses.field()

    status = field("status")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def errorDetail(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["errorDetail"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupStatusDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupStatusDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDocumentRequest:
    boto3_raw_data: "type_defs.BatchDeleteDocumentRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")

    @cached_property
    def documents(self):  # pragma: no cover
        return DeleteDocument.make_many(self.boto3_raw_data["documents"])

    dataSourceSyncId = field("dataSourceSyncId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelSubscriptionResponse:
    boto3_raw_data: "type_defs.CancelSubscriptionResponseTypeDef" = dataclasses.field()

    subscriptionArn = field("subscriptionArn")

    @cached_property
    def currentSubscription(self):  # pragma: no cover
        return SubscriptionDetails.make_one(self.boto3_raw_data["currentSubscription"])

    @cached_property
    def nextSubscription(self):  # pragma: no cover
        return SubscriptionDetails.make_one(self.boto3_raw_data["nextSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSubscriptionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionResponse:
    boto3_raw_data: "type_defs.CreateSubscriptionResponseTypeDef" = dataclasses.field()

    subscriptionId = field("subscriptionId")
    subscriptionArn = field("subscriptionArn")

    @cached_property
    def currentSubscription(self):  # pragma: no cover
        return SubscriptionDetails.make_one(self.boto3_raw_data["currentSubscription"])

    @cached_property
    def nextSubscription(self):  # pragma: no cover
        return SubscriptionDetails.make_one(self.boto3_raw_data["nextSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSubscriptionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionResponse:
    boto3_raw_data: "type_defs.UpdateSubscriptionResponseTypeDef" = dataclasses.field()

    subscriptionArn = field("subscriptionArn")

    @cached_property
    def currentSubscription(self):  # pragma: no cover
        return SubscriptionDetails.make_one(self.boto3_raw_data["currentSubscription"])

    @cached_property
    def nextSubscription(self):  # pragma: no cover
        return SubscriptionDetails.make_one(self.boto3_raw_data["nextSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSubscriptionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatModeConfiguration:
    boto3_raw_data: "type_defs.ChatModeConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def pluginConfiguration(self):  # pragma: no cover
        return PluginConfiguration.make_one(self.boto3_raw_data["pluginConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChatModeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChatModeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChatResponseConfigurationsResponse:
    boto3_raw_data: "type_defs.ListChatResponseConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def chatResponseConfigurations(self):  # pragma: no cover
        return ChatResponseConfiguration.make_many(
            self.boto3_raw_data["chatResponseConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChatResponseConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChatResponseConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentRetrievalRuleOutput:
    boto3_raw_data: "type_defs.ContentRetrievalRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def eligibleDataSources(self):  # pragma: no cover
        return EligibleDataSource.make_many(self.boto3_raw_data["eligibleDataSources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentRetrievalRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentRetrievalRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentRetrievalRule:
    boto3_raw_data: "type_defs.ContentRetrievalRuleTypeDef" = dataclasses.field()

    @cached_property
    def eligibleDataSources(self):  # pragma: no cover
        return EligibleDataSource.make_many(self.boto3_raw_data["eligibleDataSources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentRetrievalRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentRetrievalRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentSource:
    boto3_raw_data: "type_defs.ContentSourceTypeDef" = dataclasses.field()

    @cached_property
    def retriever(self):  # pragma: no cover
        return RetrieverContentSource.make_one(self.boto3_raw_data["retriever"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyFromSource:
    boto3_raw_data: "type_defs.CopyFromSourceTypeDef" = dataclasses.field()

    @cached_property
    def conversation(self):  # pragma: no cover
        return ConversationSource.make_one(self.boto3_raw_data["conversation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyFromSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyFromSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConversationsResponse:
    boto3_raw_data: "type_defs.ListConversationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def conversations(self):  # pragma: no cover
        return Conversation.make_many(self.boto3_raw_data["conversations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConversationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConversationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationResponse:
    boto3_raw_data: "type_defs.GetApplicationResponseTypeDef" = dataclasses.field()

    displayName = field("displayName")
    applicationId = field("applicationId")
    applicationArn = field("applicationArn")
    identityType = field("identityType")
    iamIdentityProviderArn = field("iamIdentityProviderArn")
    identityCenterApplicationArn = field("identityCenterApplicationArn")
    roleArn = field("roleArn")
    status = field("status")
    description = field("description")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    @cached_property
    def attachmentsConfiguration(self):  # pragma: no cover
        return AppliedAttachmentsConfiguration.make_one(
            self.boto3_raw_data["attachmentsConfiguration"]
        )

    @cached_property
    def qAppsConfiguration(self):  # pragma: no cover
        return QAppsConfiguration.make_one(self.boto3_raw_data["qAppsConfiguration"])

    @cached_property
    def personalizationConfiguration(self):  # pragma: no cover
        return PersonalizationConfiguration.make_one(
            self.boto3_raw_data["personalizationConfiguration"]
        )

    @cached_property
    def autoSubscriptionConfiguration(self):  # pragma: no cover
        return AutoSubscriptionConfiguration.make_one(
            self.boto3_raw_data["autoSubscriptionConfiguration"]
        )

    clientIdsForOIDC = field("clientIdsForOIDC")

    @cached_property
    def quickSightConfiguration(self):  # pragma: no cover
        return QuickSightConfiguration.make_one(
            self.boto3_raw_data["quickSightConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    identityCenterInstanceArn = field("identityCenterInstanceArn")
    displayName = field("displayName")
    description = field("description")
    roleArn = field("roleArn")

    @cached_property
    def attachmentsConfiguration(self):  # pragma: no cover
        return AttachmentsConfiguration.make_one(
            self.boto3_raw_data["attachmentsConfiguration"]
        )

    @cached_property
    def qAppsConfiguration(self):  # pragma: no cover
        return QAppsConfiguration.make_one(self.boto3_raw_data["qAppsConfiguration"])

    @cached_property
    def personalizationConfiguration(self):  # pragma: no cover
        return PersonalizationConfiguration.make_one(
            self.boto3_raw_data["personalizationConfiguration"]
        )

    @cached_property
    def autoSubscriptionConfiguration(self):  # pragma: no cover
        return AutoSubscriptionConfiguration.make_one(
            self.boto3_raw_data["autoSubscriptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    displayName = field("displayName")
    roleArn = field("roleArn")
    identityType = field("identityType")
    iamIdentityProviderArn = field("iamIdentityProviderArn")
    identityCenterInstanceArn = field("identityCenterInstanceArn")
    clientIdsForOIDC = field("clientIdsForOIDC")
    description = field("description")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientToken = field("clientToken")

    @cached_property
    def attachmentsConfiguration(self):  # pragma: no cover
        return AttachmentsConfiguration.make_one(
            self.boto3_raw_data["attachmentsConfiguration"]
        )

    @cached_property
    def qAppsConfiguration(self):  # pragma: no cover
        return QAppsConfiguration.make_one(self.boto3_raw_data["qAppsConfiguration"])

    @cached_property
    def personalizationConfiguration(self):  # pragma: no cover
        return PersonalizationConfiguration.make_one(
            self.boto3_raw_data["personalizationConfiguration"]
        )

    @cached_property
    def quickSightConfiguration(self):  # pragma: no cover
        return QuickSightConfiguration.make_one(
            self.boto3_raw_data["quickSightConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationRequestTypeDef"]
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

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class CreateIndexRequest:
    boto3_raw_data: "type_defs.CreateIndexRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    displayName = field("displayName")
    description = field("description")
    type = field("type")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def capacityConfiguration(self):  # pragma: no cover
        return IndexCapacityConfiguration.make_one(
            self.boto3_raw_data["capacityConfiguration"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionRequest:
    boto3_raw_data: "type_defs.CreateSubscriptionRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @cached_property
    def principal(self):  # pragma: no cover
        return SubscriptionPrincipal.make_one(self.boto3_raw_data["principal"])

    type = field("type")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSubscriptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subscription:
    boto3_raw_data: "type_defs.SubscriptionTypeDef" = dataclasses.field()

    subscriptionId = field("subscriptionId")
    subscriptionArn = field("subscriptionArn")

    @cached_property
    def principal(self):  # pragma: no cover
        return SubscriptionPrincipal.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def currentSubscription(self):  # pragma: no cover
        return SubscriptionDetails.make_one(self.boto3_raw_data["currentSubscription"])

    @cached_property
    def nextSubscription(self):  # pragma: no cover
        return SubscriptionDetails.make_one(self.boto3_raw_data["nextSubscription"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubscriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequest:
    boto3_raw_data: "type_defs.CreateUserRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    userId = field("userId")

    @cached_property
    def userAliases(self):  # pragma: no cover
        return UserAlias.make_many(self.boto3_raw_data["userAliases"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserResponse:
    boto3_raw_data: "type_defs.GetUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def userAliases(self):  # pragma: no cover
        return UserAlias.make_many(self.boto3_raw_data["userAliases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetUserResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetUserResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserRequest:
    boto3_raw_data: "type_defs.UpdateUserRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    userId = field("userId")

    @cached_property
    def userAliasesToUpdate(self):  # pragma: no cover
        return UserAlias.make_many(self.boto3_raw_data["userAliasesToUpdate"])

    @cached_property
    def userAliasesToDelete(self):  # pragma: no cover
        return UserAlias.make_many(self.boto3_raw_data["userAliasesToDelete"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserResponse:
    boto3_raw_data: "type_defs.UpdateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def userAliasesAdded(self):  # pragma: no cover
        return UserAlias.make_many(self.boto3_raw_data["userAliasesAdded"])

    @cached_property
    def userAliasesUpdated(self):  # pragma: no cover
        return UserAlias.make_many(self.boto3_raw_data["userAliasesUpdated"])

    @cached_property
    def userAliasesDeleted(self):  # pragma: no cover
        return UserAlias.make_many(self.boto3_raw_data["userAliasesDeleted"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataAccessorAuthenticationConfiguration:
    boto3_raw_data: "type_defs.DataAccessorAuthenticationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def idcTrustedTokenIssuerConfiguration(self):  # pragma: no cover
        return DataAccessorIdcTrustedTokenIssuerConfiguration.make_one(
            self.boto3_raw_data["idcTrustedTokenIssuerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataAccessorAuthenticationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataAccessorAuthenticationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceSyncJob:
    boto3_raw_data: "type_defs.DataSourceSyncJobTypeDef" = dataclasses.field()

    executionId = field("executionId")
    startTime = field("startTime")
    endTime = field("endTime")
    status = field("status")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    dataSourceErrorCode = field("dataSourceErrorCode")

    @cached_property
    def metrics(self):  # pragma: no cover
        return DataSourceSyncJobMetrics.make_one(self.boto3_raw_data["metrics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceSyncJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceSyncJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesResponse:
    boto3_raw_data: "type_defs.ListDataSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAclCondition:
    boto3_raw_data: "type_defs.DocumentAclConditionTypeDef" = dataclasses.field()

    memberRelation = field("memberRelation")

    @cached_property
    def users(self):  # pragma: no cover
        return DocumentAclUser.make_many(self.boto3_raw_data["users"])

    @cached_property
    def groups(self):  # pragma: no cover
        return DocumentAclGroup.make_many(self.boto3_raw_data["groups"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAclConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAclConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeBoostingConfigurationOutput:
    boto3_raw_data: "type_defs.DocumentAttributeBoostingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def numberConfiguration(self):  # pragma: no cover
        return NumberAttributeBoostingConfiguration.make_one(
            self.boto3_raw_data["numberConfiguration"]
        )

    @cached_property
    def stringConfiguration(self):  # pragma: no cover
        return StringAttributeBoostingConfigurationOutput.make_one(
            self.boto3_raw_data["stringConfiguration"]
        )

    @cached_property
    def dateConfiguration(self):  # pragma: no cover
        return DateAttributeBoostingConfiguration.make_one(
            self.boto3_raw_data["dateConfiguration"]
        )

    @cached_property
    def stringListConfiguration(self):  # pragma: no cover
        return StringListAttributeBoostingConfiguration.make_one(
            self.boto3_raw_data["stringListConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentAttributeBoostingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeBoostingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeBoostingConfiguration:
    boto3_raw_data: "type_defs.DocumentAttributeBoostingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def numberConfiguration(self):  # pragma: no cover
        return NumberAttributeBoostingConfiguration.make_one(
            self.boto3_raw_data["numberConfiguration"]
        )

    @cached_property
    def stringConfiguration(self):  # pragma: no cover
        return StringAttributeBoostingConfiguration.make_one(
            self.boto3_raw_data["stringConfiguration"]
        )

    @cached_property
    def dateConfiguration(self):  # pragma: no cover
        return DateAttributeBoostingConfiguration.make_one(
            self.boto3_raw_data["dateConfiguration"]
        )

    @cached_property
    def stringListConfiguration(self):  # pragma: no cover
        return StringListAttributeBoostingConfiguration.make_one(
            self.boto3_raw_data["stringListConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentAttributeBoostingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeBoostingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeConditionOutput:
    boto3_raw_data: "type_defs.DocumentAttributeConditionOutputTypeDef" = (
        dataclasses.field()
    )

    key = field("key")
    operator = field("operator")

    @cached_property
    def value(self):  # pragma: no cover
        return DocumentAttributeValueOutput.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentAttributeConditionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeOutput:
    boto3_raw_data: "type_defs.DocumentAttributeOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def value(self):  # pragma: no cover
        return DocumentAttributeValueOutput.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeTargetOutput:
    boto3_raw_data: "type_defs.DocumentAttributeTargetOutputTypeDef" = (
        dataclasses.field()
    )

    key = field("key")

    @cached_property
    def value(self):  # pragma: no cover
        return DocumentAttributeValueOutput.make_one(self.boto3_raw_data["value"])

    attributeValueOperator = field("attributeValueOperator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentAttributeTargetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIndexRequest:
    boto3_raw_data: "type_defs.UpdateIndexRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    displayName = field("displayName")
    description = field("description")

    @cached_property
    def capacityConfiguration(self):  # pragma: no cover
        return IndexCapacityConfiguration.make_one(
            self.boto3_raw_data["capacityConfiguration"]
        )

    @cached_property
    def documentAttributeConfigurations(self):  # pragma: no cover
        return DocumentAttributeConfiguration.make_many(
            self.boto3_raw_data["documentAttributeConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeValue:
    boto3_raw_data: "type_defs.DocumentAttributeValueTypeDef" = dataclasses.field()

    stringValue = field("stringValue")
    stringListValue = field("stringListValue")
    longValue = field("longValue")
    dateValue = field("dateValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceSyncJobsRequest:
    boto3_raw_data: "type_defs.ListDataSourceSyncJobsRequestTypeDef" = (
        dataclasses.field()
    )

    dataSourceId = field("dataSourceId")
    applicationId = field("applicationId")
    indexId = field("indexId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    startTime = field("startTime")
    endTime = field("endTime")
    statusFilter = field("statusFilter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSourceSyncJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceSyncJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequest:
    boto3_raw_data: "type_defs.ListGroupsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    updatedEarlierThan = field("updatedEarlierThan")
    dataSourceId = field("dataSourceId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageUsefulnessFeedback:
    boto3_raw_data: "type_defs.MessageUsefulnessFeedbackTypeDef" = dataclasses.field()

    usefulness = field("usefulness")
    submittedAt = field("submittedAt")
    reason = field("reason")
    comment = field("comment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageUsefulnessFeedbackTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageUsefulnessFeedbackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChatControlsConfigurationRequestPaginate:
    boto3_raw_data: "type_defs.GetChatControlsConfigurationRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetChatControlsConfigurationRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChatControlsConfigurationRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListAttachmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    conversationId = field("conversationId")
    userId = field("userId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAttachmentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChatResponseConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListChatResponseConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChatResponseConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChatResponseConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConversationsRequestPaginate:
    boto3_raw_data: "type_defs.ListConversationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    userId = field("userId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConversationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConversationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataAccessorsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataAccessorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataAccessorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataAccessorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceSyncJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataSourceSyncJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    dataSourceId = field("dataSourceId")
    applicationId = field("applicationId")
    indexId = field("indexId")
    startTime = field("startTime")
    endTime = field("endTime")
    statusFilter = field("statusFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataSourceSyncJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceSyncJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListDataSourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    indexId = field("indexId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSourcesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentsRequestPaginate:
    boto3_raw_data: "type_defs.ListDocumentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    indexId = field("indexId")
    dataSourceIds = field("dataSourceIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDocumentsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupsRequestPaginateTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    updatedEarlierThan = field("updatedEarlierThan")
    dataSourceId = field("dataSourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicesRequestPaginate:
    boto3_raw_data: "type_defs.ListIndicesRequestPaginateTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessagesRequestPaginate:
    boto3_raw_data: "type_defs.ListMessagesRequestPaginateTypeDef" = dataclasses.field()

    conversationId = field("conversationId")
    applicationId = field("applicationId")
    userId = field("userId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessagesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPluginActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    pluginId = field("pluginId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPluginActionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginTypeActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPluginTypeActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    pluginType = field("pluginType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPluginTypeActionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginTypeActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginTypeMetadataRequestPaginate:
    boto3_raw_data: "type_defs.ListPluginTypeMetadataRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPluginTypeMetadataRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginTypeMetadataRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginsRequestPaginate:
    boto3_raw_data: "type_defs.ListPluginsRequestPaginateTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPluginsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRetrieversRequestPaginate:
    boto3_raw_data: "type_defs.ListRetrieversRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRetrieversRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRetrieversRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSubscriptionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSubscriptionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebExperiencesRequestPaginate:
    boto3_raw_data: "type_defs.ListWebExperiencesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWebExperiencesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebExperiencesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupMembers:
    boto3_raw_data: "type_defs.GroupMembersTypeDef" = dataclasses.field()

    @cached_property
    def memberGroups(self):  # pragma: no cover
        return MemberGroup.make_many(self.boto3_raw_data["memberGroups"])

    @cached_property
    def memberUsers(self):  # pragma: no cover
        return MemberUser.make_many(self.boto3_raw_data["memberUsers"])

    @cached_property
    def s3PathForGroupMembers(self):  # pragma: no cover
        return S3.make_one(self.boto3_raw_data["s3PathForGroupMembers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupMembersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupMembersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsResponse:
    boto3_raw_data: "type_defs.ListGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return GroupSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityProviderConfiguration:
    boto3_raw_data: "type_defs.IdentityProviderConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def samlConfiguration(self):  # pragma: no cover
        return SamlProviderConfiguration.make_one(
            self.boto3_raw_data["samlConfiguration"]
        )

    @cached_property
    def openIDConnectConfiguration(self):  # pragma: no cover
        return OpenIDConnectProviderConfiguration.make_one(
            self.boto3_raw_data["openIDConnectConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdentityProviderConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexStatistics:
    boto3_raw_data: "type_defs.IndexStatisticsTypeDef" = dataclasses.field()

    @cached_property
    def textDocumentStatistics(self):  # pragma: no cover
        return TextDocumentStatistics.make_one(
            self.boto3_raw_data["textDocumentStatistics"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicesResponse:
    boto3_raw_data: "type_defs.ListIndicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def indices(self):  # pragma: no cover
        return Index.make_many(self.boto3_raw_data["indices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseConfiguration:
    boto3_raw_data: "type_defs.ResponseConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def instructionCollection(self):  # pragma: no cover
        return InstructionCollection.make_one(
            self.boto3_raw_data["instructionCollection"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginTypeMetadataResponse:
    boto3_raw_data: "type_defs.ListPluginTypeMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return PluginTypeMetadataSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPluginTypeMetadataResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginTypeMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginsResponse:
    boto3_raw_data: "type_defs.ListPluginsResponseTypeDef" = dataclasses.field()

    @cached_property
    def plugins(self):  # pragma: no cover
        return Plugin.make_many(self.boto3_raw_data["plugins"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPluginsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRetrieversResponse:
    boto3_raw_data: "type_defs.ListRetrieversResponseTypeDef" = dataclasses.field()

    @cached_property
    def retrievers(self):  # pragma: no cover
        return Retriever.make_many(self.boto3_raw_data["retrievers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRetrieversResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRetrieversResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebExperiencesResponse:
    boto3_raw_data: "type_defs.ListWebExperiencesResponseTypeDef" = dataclasses.field()

    @cached_property
    def webExperiences(self):  # pragma: no cover
        return WebExperience.make_many(self.boto3_raw_data["webExperiences"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebExperiencesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebExperiencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaExtractionConfiguration:
    boto3_raw_data: "type_defs.MediaExtractionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def imageExtractionConfiguration(self):  # pragma: no cover
        return ImageExtractionConfiguration.make_one(
            self.boto3_raw_data["imageExtractionConfiguration"]
        )

    @cached_property
    def audioExtractionConfiguration(self):  # pragma: no cover
        return AudioExtractionConfiguration.make_one(
            self.boto3_raw_data["audioExtractionConfiguration"]
        )

    @cached_property
    def videoExtractionConfiguration(self):  # pragma: no cover
        return VideoExtractionConfiguration.make_one(
            self.boto3_raw_data["videoExtractionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaExtractionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaExtractionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PluginAuthConfigurationOutput:
    boto3_raw_data: "type_defs.PluginAuthConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def basicAuthConfiguration(self):  # pragma: no cover
        return BasicAuthConfiguration.make_one(
            self.boto3_raw_data["basicAuthConfiguration"]
        )

    @cached_property
    def oAuth2ClientCredentialConfiguration(self):  # pragma: no cover
        return OAuth2ClientCredentialConfiguration.make_one(
            self.boto3_raw_data["oAuth2ClientCredentialConfiguration"]
        )

    noAuthConfiguration = field("noAuthConfiguration")

    @cached_property
    def idcAuthConfiguration(self):  # pragma: no cover
        return IdcAuthConfiguration.make_one(
            self.boto3_raw_data["idcAuthConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PluginAuthConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PluginAuthConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PluginAuthConfiguration:
    boto3_raw_data: "type_defs.PluginAuthConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def basicAuthConfiguration(self):  # pragma: no cover
        return BasicAuthConfiguration.make_one(
            self.boto3_raw_data["basicAuthConfiguration"]
        )

    @cached_property
    def oAuth2ClientCredentialConfiguration(self):  # pragma: no cover
        return OAuth2ClientCredentialConfiguration.make_one(
            self.boto3_raw_data["oAuth2ClientCredentialConfiguration"]
        )

    noAuthConfiguration = field("noAuthConfiguration")

    @cached_property
    def idcAuthConfiguration(self):  # pragma: no cover
        return IdcAuthConfiguration.make_one(
            self.boto3_raw_data["idcAuthConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PluginAuthConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PluginAuthConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Principal:
    boto3_raw_data: "type_defs.PrincipalTypeDef" = dataclasses.field()

    @cached_property
    def user(self):  # pragma: no cover
        return PrincipalUser.make_one(self.boto3_raw_data["user"])

    @cached_property
    def group(self):  # pragma: no cover
        return PrincipalGroup.make_one(self.boto3_raw_data["group"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrincipalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrincipalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebExperienceAuthConfiguration:
    boto3_raw_data: "type_defs.WebExperienceAuthConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def samlConfiguration(self):  # pragma: no cover
        return SamlConfiguration.make_one(self.boto3_raw_data["samlConfiguration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WebExperienceAuthConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebExperienceAuthConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceDetails:
    boto3_raw_data: "type_defs.SourceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def imageSourceDetails(self):  # pragma: no cover
        return ImageSourceDetails.make_one(self.boto3_raw_data["imageSourceDetails"])

    @cached_property
    def audioSourceDetails(self):  # pragma: no cover
        return AudioSourceDetails.make_one(self.boto3_raw_data["audioSourceDetails"])

    @cached_property
    def videoSourceDetails(self):  # pragma: no cover
        return VideoSourceDetails.make_one(self.boto3_raw_data["videoSourceDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPluginConfiguration:
    boto3_raw_data: "type_defs.CustomPluginConfigurationTypeDef" = dataclasses.field()

    description = field("description")
    apiSchemaType = field("apiSchemaType")

    @cached_property
    def apiSchema(self):  # pragma: no cover
        return APISchema.make_one(self.boto3_raw_data["apiSchema"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomPluginConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomPluginConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecutionEvent:
    boto3_raw_data: "type_defs.ActionExecutionEventTypeDef" = dataclasses.field()

    pluginId = field("pluginId")
    payload = field("payload")
    payloadFieldNameSeparator = field("payloadFieldNameSeparator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionExecutionEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionReviewEvent:
    boto3_raw_data: "type_defs.ActionReviewEventTypeDef" = dataclasses.field()

    conversationId = field("conversationId")
    userMessageId = field("userMessageId")
    systemMessageId = field("systemMessageId")
    pluginId = field("pluginId")
    pluginType = field("pluginType")
    payload = field("payload")
    payloadFieldNameSeparator = field("payloadFieldNameSeparator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionReviewEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionReviewEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionReview:
    boto3_raw_data: "type_defs.ActionReviewTypeDef" = dataclasses.field()

    pluginId = field("pluginId")
    pluginType = field("pluginType")
    payload = field("payload")
    payloadFieldNameSeparator = field("payloadFieldNameSeparator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionReviewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionReviewTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsResponse:
    boto3_raw_data: "type_defs.ListApplicationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def applications(self):  # pragma: no cover
        return Application.make_many(self.boto3_raw_data["applications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedAttachmentEvent:
    boto3_raw_data: "type_defs.FailedAttachmentEventTypeDef" = dataclasses.field()

    conversationId = field("conversationId")
    userMessageId = field("userMessageId")
    systemMessageId = field("systemMessageId")

    @cached_property
    def attachment(self):  # pragma: no cover
        return AttachmentOutput.make_one(self.boto3_raw_data["attachment"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailedAttachmentEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedAttachmentEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentsResponse:
    boto3_raw_data: "type_defs.ListDocumentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def documentDetailList(self):  # pragma: no cover
        return DocumentDetails.make_many(self.boto3_raw_data["documentDetailList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDocumentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDocumentResponse:
    boto3_raw_data: "type_defs.BatchDeleteDocumentResponseTypeDef" = dataclasses.field()

    @cached_property
    def failedDocuments(self):  # pragma: no cover
        return FailedDocument.make_many(self.boto3_raw_data["failedDocuments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteDocumentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutDocumentResponse:
    boto3_raw_data: "type_defs.BatchPutDocumentResponseTypeDef" = dataclasses.field()

    @cached_property
    def failedDocuments(self):  # pragma: no cover
        return FailedDocument.make_many(self.boto3_raw_data["failedDocuments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutDocumentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupResponse:
    boto3_raw_data: "type_defs.GetGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def status(self):  # pragma: no cover
        return GroupStatusDetail.make_one(self.boto3_raw_data["status"])

    @cached_property
    def statusHistory(self):  # pragma: no cover
        return GroupStatusDetail.make_many(self.boto3_raw_data["statusHistory"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleConfigurationOutput:
    boto3_raw_data: "type_defs.RuleConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def contentBlockerRule(self):  # pragma: no cover
        return ContentBlockerRule.make_one(self.boto3_raw_data["contentBlockerRule"])

    @cached_property
    def contentRetrievalRule(self):  # pragma: no cover
        return ContentRetrievalRuleOutput.make_one(
            self.boto3_raw_data["contentRetrievalRule"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentInput:
    boto3_raw_data: "type_defs.AttachmentInputTypeDef" = dataclasses.field()

    data = field("data")
    name = field("name")

    @cached_property
    def copyFrom(self):  # pragma: no cover
        return CopyFromSource.make_one(self.boto3_raw_data["copyFrom"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attachment:
    boto3_raw_data: "type_defs.AttachmentTypeDef" = dataclasses.field()

    attachmentId = field("attachmentId")
    conversationId = field("conversationId")
    name = field("name")

    @cached_property
    def copyFrom(self):  # pragma: no cover
        return CopyFromSource.make_one(self.boto3_raw_data["copyFrom"])

    fileType = field("fileType")
    fileSize = field("fileSize")
    md5chksum = field("md5chksum")
    createdAt = field("createdAt")
    status = field("status")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionsResponse:
    boto3_raw_data: "type_defs.ListSubscriptionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def subscriptions(self):  # pragma: no cover
        return Subscription.make_many(self.boto3_raw_data["subscriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubscriptionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataAccessorAuthenticationDetailOutput:
    boto3_raw_data: "type_defs.DataAccessorAuthenticationDetailOutputTypeDef" = (
        dataclasses.field()
    )

    authenticationType = field("authenticationType")

    @cached_property
    def authenticationConfiguration(self):  # pragma: no cover
        return DataAccessorAuthenticationConfiguration.make_one(
            self.boto3_raw_data["authenticationConfiguration"]
        )

    externalIds = field("externalIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataAccessorAuthenticationDetailOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataAccessorAuthenticationDetailOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataAccessorAuthenticationDetail:
    boto3_raw_data: "type_defs.DataAccessorAuthenticationDetailTypeDef" = (
        dataclasses.field()
    )

    authenticationType = field("authenticationType")

    @cached_property
    def authenticationConfiguration(self):  # pragma: no cover
        return DataAccessorAuthenticationConfiguration.make_one(
            self.boto3_raw_data["authenticationConfiguration"]
        )

    externalIds = field("externalIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataAccessorAuthenticationDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataAccessorAuthenticationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceSyncJobsResponse:
    boto3_raw_data: "type_defs.ListDataSourceSyncJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def history(self):  # pragma: no cover
        return DataSourceSyncJob.make_many(self.boto3_raw_data["history"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSourceSyncJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceSyncJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAclMembership:
    boto3_raw_data: "type_defs.DocumentAclMembershipTypeDef" = dataclasses.field()

    memberRelation = field("memberRelation")

    @cached_property
    def conditions(self):  # pragma: no cover
        return DocumentAclCondition.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAclMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAclMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NativeIndexConfigurationOutput:
    boto3_raw_data: "type_defs.NativeIndexConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    indexId = field("indexId")
    version = field("version")
    boostingOverride = field("boostingOverride")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NativeIndexConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NativeIndexConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NativeIndexConfiguration:
    boto3_raw_data: "type_defs.NativeIndexConfigurationTypeDef" = dataclasses.field()

    indexId = field("indexId")
    version = field("version")
    boostingOverride = field("boostingOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NativeIndexConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NativeIndexConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HookConfigurationOutput:
    boto3_raw_data: "type_defs.HookConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def invocationCondition(self):  # pragma: no cover
        return DocumentAttributeConditionOutput.make_one(
            self.boto3_raw_data["invocationCondition"]
        )

    lambdaArn = field("lambdaArn")
    s3BucketName = field("s3BucketName")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HookConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HookConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeFilterOutput:
    boto3_raw_data: "type_defs.AttributeFilterOutputTypeDef" = dataclasses.field()

    andAllFilters = field("andAllFilters")
    orAllFilters = field("orAllFilters")
    notFilter = field("notFilter")

    @cached_property
    def equalsTo(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["equalsTo"])

    @cached_property
    def containsAll(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["containsAll"])

    @cached_property
    def containsAny(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["containsAny"])

    @cached_property
    def greaterThan(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["greaterThan"])

    @cached_property
    def greaterThanOrEquals(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(
            self.boto3_raw_data["greaterThanOrEquals"]
        )

    @cached_property
    def lessThan(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["lessThan"])

    @cached_property
    def lessThanOrEquals(self):  # pragma: no cover
        return DocumentAttributeOutput.make_one(self.boto3_raw_data["lessThanOrEquals"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelevantContent:
    boto3_raw_data: "type_defs.RelevantContentTypeDef" = dataclasses.field()

    content = field("content")
    documentId = field("documentId")
    documentTitle = field("documentTitle")
    documentUri = field("documentUri")

    @cached_property
    def documentAttributes(self):  # pragma: no cover
        return DocumentAttributeOutput.make_many(
            self.boto3_raw_data["documentAttributes"]
        )

    @cached_property
    def scoreAttributes(self):  # pragma: no cover
        return ScoreAttributes.make_one(self.boto3_raw_data["scoreAttributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelevantContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelevantContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineDocumentEnrichmentConfigurationOutput:
    boto3_raw_data: "type_defs.InlineDocumentEnrichmentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def condition(self):  # pragma: no cover
        return DocumentAttributeConditionOutput.make_one(
            self.boto3_raw_data["condition"]
        )

    @cached_property
    def target(self):  # pragma: no cover
        return DocumentAttributeTargetOutput.make_one(self.boto3_raw_data["target"])

    documentContentOperator = field("documentContentOperator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InlineDocumentEnrichmentConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineDocumentEnrichmentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFeedbackRequest:
    boto3_raw_data: "type_defs.PutFeedbackRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    conversationId = field("conversationId")
    messageId = field("messageId")
    userId = field("userId")
    messageCopiedAt = field("messageCopiedAt")

    @cached_property
    def messageUsefulness(self):  # pragma: no cover
        return MessageUsefulnessFeedback.make_one(
            self.boto3_raw_data["messageUsefulness"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutFeedbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutGroupRequest:
    boto3_raw_data: "type_defs.PutGroupRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    groupName = field("groupName")
    type = field("type")

    @cached_property
    def groupMembers(self):  # pragma: no cover
        return GroupMembers.make_one(self.boto3_raw_data["groupMembers"])

    dataSourceId = field("dataSourceId")
    roleArn = field("roleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutGroupRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutGroupRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebExperienceRequest:
    boto3_raw_data: "type_defs.CreateWebExperienceRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    title = field("title")
    subtitle = field("subtitle")
    welcomeMessage = field("welcomeMessage")
    samplePromptsControlMode = field("samplePromptsControlMode")
    origins = field("origins")
    roleArn = field("roleArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientToken = field("clientToken")

    @cached_property
    def identityProviderConfiguration(self):  # pragma: no cover
        return IdentityProviderConfiguration.make_one(
            self.boto3_raw_data["identityProviderConfiguration"]
        )

    browserExtensionConfiguration = field("browserExtensionConfiguration")

    @cached_property
    def customizationConfiguration(self):  # pragma: no cover
        return CustomizationConfiguration.make_one(
            self.boto3_raw_data["customizationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebExperienceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIndexResponse:
    boto3_raw_data: "type_defs.GetIndexResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    displayName = field("displayName")
    indexArn = field("indexArn")
    status = field("status")
    type = field("type")
    description = field("description")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def capacityConfiguration(self):  # pragma: no cover
        return IndexCapacityConfiguration.make_one(
            self.boto3_raw_data["capacityConfiguration"]
        )

    @cached_property
    def documentAttributeConfigurations(self):  # pragma: no cover
        return DocumentAttributeConfiguration.make_many(
            self.boto3_raw_data["documentAttributeConfigurations"]
        )

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    @cached_property
    def indexStatistics(self):  # pragma: no cover
        return IndexStatistics.make_one(self.boto3_raw_data["indexStatistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIndexResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatResponseConfigurationDetail:
    boto3_raw_data: "type_defs.ChatResponseConfigurationDetailTypeDef" = (
        dataclasses.field()
    )

    responseConfigurations = field("responseConfigurations")
    responseConfigurationSummary = field("responseConfigurationSummary")
    status = field("status")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ChatResponseConfigurationDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChatResponseConfigurationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChatResponseConfigurationRequest:
    boto3_raw_data: "type_defs.CreateChatResponseConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    displayName = field("displayName")
    responseConfigurations = field("responseConfigurations")
    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateChatResponseConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChatResponseConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChatResponseConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateChatResponseConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    chatResponseConfigurationId = field("chatResponseConfigurationId")
    responseConfigurations = field("responseConfigurations")
    displayName = field("displayName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateChatResponseConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChatResponseConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControl:
    boto3_raw_data: "type_defs.AccessControlTypeDef" = dataclasses.field()

    @cached_property
    def principals(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["principals"])

    memberRelation = field("memberRelation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessControlTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessControlTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWebExperienceResponse:
    boto3_raw_data: "type_defs.GetWebExperienceResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    webExperienceId = field("webExperienceId")
    webExperienceArn = field("webExperienceArn")
    defaultEndpoint = field("defaultEndpoint")
    status = field("status")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    title = field("title")
    subtitle = field("subtitle")
    welcomeMessage = field("welcomeMessage")
    samplePromptsControlMode = field("samplePromptsControlMode")
    origins = field("origins")
    roleArn = field("roleArn")

    @cached_property
    def identityProviderConfiguration(self):  # pragma: no cover
        return IdentityProviderConfiguration.make_one(
            self.boto3_raw_data["identityProviderConfiguration"]
        )

    @cached_property
    def authenticationConfiguration(self):  # pragma: no cover
        return WebExperienceAuthConfiguration.make_one(
            self.boto3_raw_data["authenticationConfiguration"]
        )

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    @cached_property
    def browserExtensionConfiguration(self):  # pragma: no cover
        return BrowserExtensionConfigurationOutput.make_one(
            self.boto3_raw_data["browserExtensionConfiguration"]
        )

    @cached_property
    def customizationConfiguration(self):  # pragma: no cover
        return CustomizationConfiguration.make_one(
            self.boto3_raw_data["customizationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWebExperienceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWebExperienceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebExperienceRequest:
    boto3_raw_data: "type_defs.UpdateWebExperienceRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    webExperienceId = field("webExperienceId")
    roleArn = field("roleArn")

    @cached_property
    def authenticationConfiguration(self):  # pragma: no cover
        return WebExperienceAuthConfiguration.make_one(
            self.boto3_raw_data["authenticationConfiguration"]
        )

    title = field("title")
    subtitle = field("subtitle")
    welcomeMessage = field("welcomeMessage")
    samplePromptsControlMode = field("samplePromptsControlMode")

    @cached_property
    def identityProviderConfiguration(self):  # pragma: no cover
        return IdentityProviderConfiguration.make_one(
            self.boto3_raw_data["identityProviderConfiguration"]
        )

    origins = field("origins")
    browserExtensionConfiguration = field("browserExtensionConfiguration")

    @cached_property
    def customizationConfiguration(self):  # pragma: no cover
        return CustomizationConfiguration.make_one(
            self.boto3_raw_data["customizationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWebExperienceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebExperienceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextSegment:
    boto3_raw_data: "type_defs.TextSegmentTypeDef" = dataclasses.field()

    beginOffset = field("beginOffset")
    endOffset = field("endOffset")

    @cached_property
    def snippetExcerpt(self):  # pragma: no cover
        return SnippetExcerpt.make_one(self.boto3_raw_data["snippetExcerpt"])

    mediaId = field("mediaId")
    mediaMimeType = field("mediaMimeType")

    @cached_property
    def sourceDetails(self):  # pragma: no cover
        return SourceDetails.make_one(self.boto3_raw_data["sourceDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextSegmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextSegmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPluginResponse:
    boto3_raw_data: "type_defs.GetPluginResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    pluginId = field("pluginId")
    displayName = field("displayName")
    type = field("type")
    serverUrl = field("serverUrl")

    @cached_property
    def authConfiguration(self):  # pragma: no cover
        return PluginAuthConfigurationOutput.make_one(
            self.boto3_raw_data["authConfiguration"]
        )

    @cached_property
    def customPluginConfiguration(self):  # pragma: no cover
        return CustomPluginConfiguration.make_one(
            self.boto3_raw_data["customPluginConfiguration"]
        )

    buildStatus = field("buildStatus")
    pluginArn = field("pluginArn")
    state = field("state")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPluginResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPluginResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleOutput:
    boto3_raw_data: "type_defs.RuleOutputTypeDef" = dataclasses.field()

    ruleType = field("ruleType")

    @cached_property
    def includedUsersAndGroups(self):  # pragma: no cover
        return UsersAndGroupsOutput.make_one(
            self.boto3_raw_data["includedUsersAndGroups"]
        )

    @cached_property
    def excludedUsersAndGroups(self):  # pragma: no cover
        return UsersAndGroupsOutput.make_one(
            self.boto3_raw_data["excludedUsersAndGroups"]
        )

    @cached_property
    def ruleConfiguration(self):  # pragma: no cover
        return RuleConfigurationOutput.make_one(
            self.boto3_raw_data["ruleConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleConfiguration:
    boto3_raw_data: "type_defs.RuleConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def contentBlockerRule(self):  # pragma: no cover
        return ContentBlockerRule.make_one(self.boto3_raw_data["contentBlockerRule"])

    contentRetrievalRule = field("contentRetrievalRule")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentInputEvent:
    boto3_raw_data: "type_defs.AttachmentInputEventTypeDef" = dataclasses.field()

    @cached_property
    def attachment(self):  # pragma: no cover
        return AttachmentInput.make_one(self.boto3_raw_data["attachment"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachmentInputEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentInputEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachmentsResponse:
    boto3_raw_data: "type_defs.ListAttachmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def attachments(self):  # pragma: no cover
        return Attachment.make_many(self.boto3_raw_data["attachments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttachmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataAccessor:
    boto3_raw_data: "type_defs.DataAccessorTypeDef" = dataclasses.field()

    displayName = field("displayName")
    dataAccessorId = field("dataAccessorId")
    dataAccessorArn = field("dataAccessorArn")
    idcApplicationArn = field("idcApplicationArn")
    principal = field("principal")

    @cached_property
    def authenticationDetail(self):  # pragma: no cover
        return DataAccessorAuthenticationDetailOutput.make_one(
            self.boto3_raw_data["authenticationDetail"]
        )

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataAccessorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataAccessorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAcl:
    boto3_raw_data: "type_defs.DocumentAclTypeDef" = dataclasses.field()

    @cached_property
    def allowlist(self):  # pragma: no cover
        return DocumentAclMembership.make_one(self.boto3_raw_data["allowlist"])

    @cached_property
    def denyList(self):  # pragma: no cover
        return DocumentAclMembership.make_one(self.boto3_raw_data["denyList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentAclTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentAclTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieverConfigurationOutput:
    boto3_raw_data: "type_defs.RetrieverConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def nativeIndexConfiguration(self):  # pragma: no cover
        return NativeIndexConfigurationOutput.make_one(
            self.boto3_raw_data["nativeIndexConfiguration"]
        )

    @cached_property
    def kendraIndexConfiguration(self):  # pragma: no cover
        return KendraIndexConfiguration.make_one(
            self.boto3_raw_data["kendraIndexConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieverConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieverConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieverConfiguration:
    boto3_raw_data: "type_defs.RetrieverConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def nativeIndexConfiguration(self):  # pragma: no cover
        return NativeIndexConfiguration.make_one(
            self.boto3_raw_data["nativeIndexConfiguration"]
        )

    @cached_property
    def kendraIndexConfiguration(self):  # pragma: no cover
        return KendraIndexConfiguration.make_one(
            self.boto3_raw_data["kendraIndexConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieverConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieverConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionFilterConfigurationOutput:
    boto3_raw_data: "type_defs.ActionFilterConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def documentAttributeFilter(self):  # pragma: no cover
        return AttributeFilterOutput.make_one(
            self.boto3_raw_data["documentAttributeFilter"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActionFilterConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionFilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRelevantContentResponse:
    boto3_raw_data: "type_defs.SearchRelevantContentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def relevantContent(self):  # pragma: no cover
        return RelevantContent.make_many(self.boto3_raw_data["relevantContent"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchRelevantContentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRelevantContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentEnrichmentConfigurationOutput:
    boto3_raw_data: "type_defs.DocumentEnrichmentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def inlineConfigurations(self):  # pragma: no cover
        return InlineDocumentEnrichmentConfigurationOutput.make_many(
            self.boto3_raw_data["inlineConfigurations"]
        )

    @cached_property
    def preExtractionHookConfiguration(self):  # pragma: no cover
        return HookConfigurationOutput.make_one(
            self.boto3_raw_data["preExtractionHookConfiguration"]
        )

    @cached_property
    def postExtractionHookConfiguration(self):  # pragma: no cover
        return HookConfigurationOutput.make_one(
            self.boto3_raw_data["postExtractionHookConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentEnrichmentConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentEnrichmentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeCondition:
    boto3_raw_data: "type_defs.DocumentAttributeConditionTypeDef" = dataclasses.field()

    key = field("key")
    operator = field("operator")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttributeTarget:
    boto3_raw_data: "type_defs.DocumentAttributeTargetTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")
    attributeValueOperator = field("attributeValueOperator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentAttribute:
    boto3_raw_data: "type_defs.DocumentAttributeTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChatResponseConfigurationResponse:
    boto3_raw_data: "type_defs.GetChatResponseConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    chatResponseConfigurationId = field("chatResponseConfigurationId")
    chatResponseConfigurationArn = field("chatResponseConfigurationArn")
    displayName = field("displayName")
    createdAt = field("createdAt")

    @cached_property
    def inUseConfiguration(self):  # pragma: no cover
        return ChatResponseConfigurationDetail.make_one(
            self.boto3_raw_data["inUseConfiguration"]
        )

    @cached_property
    def lastUpdateConfiguration(self):  # pragma: no cover
        return ChatResponseConfigurationDetail.make_one(
            self.boto3_raw_data["lastUpdateConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetChatResponseConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChatResponseConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePluginRequest:
    boto3_raw_data: "type_defs.CreatePluginRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    displayName = field("displayName")
    type = field("type")
    authConfiguration = field("authConfiguration")
    serverUrl = field("serverUrl")

    @cached_property
    def customPluginConfiguration(self):  # pragma: no cover
        return CustomPluginConfiguration.make_one(
            self.boto3_raw_data["customPluginConfiguration"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePluginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePluginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePluginRequest:
    boto3_raw_data: "type_defs.UpdatePluginRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    pluginId = field("pluginId")
    displayName = field("displayName")
    state = field("state")
    serverUrl = field("serverUrl")

    @cached_property
    def customPluginConfiguration(self):  # pragma: no cover
        return CustomPluginConfiguration.make_one(
            self.boto3_raw_data["customPluginConfiguration"]
        )

    authConfiguration = field("authConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePluginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePluginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessConfiguration:
    boto3_raw_data: "type_defs.AccessConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def accessControls(self):  # pragma: no cover
        return AccessControl.make_many(self.boto3_raw_data["accessControls"])

    memberRelation = field("memberRelation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceAttribution:
    boto3_raw_data: "type_defs.SourceAttributionTypeDef" = dataclasses.field()

    title = field("title")
    snippet = field("snippet")
    url = field("url")
    citationNumber = field("citationNumber")
    updatedAt = field("updatedAt")

    @cached_property
    def textMessageSegments(self):  # pragma: no cover
        return TextSegment.make_many(self.boto3_raw_data["textMessageSegments"])

    documentId = field("documentId")
    indexId = field("indexId")
    datasourceId = field("datasourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceAttributionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceAttributionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicConfigurationOutput:
    boto3_raw_data: "type_defs.TopicConfigurationOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["rules"])

    description = field("description")
    exampleChatMessages = field("exampleChatMessages")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataAccessorsResponse:
    boto3_raw_data: "type_defs.ListDataAccessorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataAccessors(self):  # pragma: no cover
        return DataAccessor.make_many(self.boto3_raw_data["dataAccessors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataAccessorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataAccessorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckDocumentAccessResponse:
    boto3_raw_data: "type_defs.CheckDocumentAccessResponseTypeDef" = dataclasses.field()

    @cached_property
    def userGroups(self):  # pragma: no cover
        return AssociatedGroup.make_many(self.boto3_raw_data["userGroups"])

    @cached_property
    def userAliases(self):  # pragma: no cover
        return AssociatedUser.make_many(self.boto3_raw_data["userAliases"])

    hasAccess = field("hasAccess")

    @cached_property
    def documentAcl(self):  # pragma: no cover
        return DocumentAcl.make_one(self.boto3_raw_data["documentAcl"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckDocumentAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckDocumentAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRetrieverResponse:
    boto3_raw_data: "type_defs.GetRetrieverResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    retrieverId = field("retrieverId")
    retrieverArn = field("retrieverArn")
    type = field("type")
    status = field("status")
    displayName = field("displayName")

    @cached_property
    def configuration(self):  # pragma: no cover
        return RetrieverConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    roleArn = field("roleArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRetrieverResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRetrieverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionConfigurationOutput:
    boto3_raw_data: "type_defs.ActionConfigurationOutputTypeDef" = dataclasses.field()

    action = field("action")

    @cached_property
    def filterConfiguration(self):  # pragma: no cover
        return ActionFilterConfigurationOutput.make_one(
            self.boto3_raw_data["filterConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceResponse:
    boto3_raw_data: "type_defs.GetDataSourceResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    dataSourceId = field("dataSourceId")
    dataSourceArn = field("dataSourceArn")
    displayName = field("displayName")
    type = field("type")
    configuration = field("configuration")

    @cached_property
    def vpcConfiguration(self):  # pragma: no cover
        return DataSourceVpcConfigurationOutput.make_one(
            self.boto3_raw_data["vpcConfiguration"]
        )

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")
    status = field("status")
    syncSchedule = field("syncSchedule")
    roleArn = field("roleArn")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    @cached_property
    def documentEnrichmentConfiguration(self):  # pragma: no cover
        return DocumentEnrichmentConfigurationOutput.make_one(
            self.boto3_raw_data["documentEnrichmentConfiguration"]
        )

    @cached_property
    def mediaExtractionConfiguration(self):  # pragma: no cover
        return MediaExtractionConfiguration.make_one(
            self.boto3_raw_data["mediaExtractionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatSyncOutput:
    boto3_raw_data: "type_defs.ChatSyncOutputTypeDef" = dataclasses.field()

    conversationId = field("conversationId")
    systemMessage = field("systemMessage")
    systemMessageId = field("systemMessageId")
    userMessageId = field("userMessageId")

    @cached_property
    def actionReview(self):  # pragma: no cover
        return ActionReview.make_one(self.boto3_raw_data["actionReview"])

    @cached_property
    def authChallengeRequest(self):  # pragma: no cover
        return AuthChallengeRequest.make_one(
            self.boto3_raw_data["authChallengeRequest"]
        )

    @cached_property
    def sourceAttributions(self):  # pragma: no cover
        return SourceAttribution.make_many(self.boto3_raw_data["sourceAttributions"])

    @cached_property
    def failedAttachments(self):  # pragma: no cover
        return AttachmentOutput.make_many(self.boto3_raw_data["failedAttachments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChatSyncOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChatSyncOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Message:
    boto3_raw_data: "type_defs.MessageTypeDef" = dataclasses.field()

    messageId = field("messageId")
    body = field("body")
    time = field("time")
    type = field("type")

    @cached_property
    def attachments(self):  # pragma: no cover
        return AttachmentOutput.make_many(self.boto3_raw_data["attachments"])

    @cached_property
    def sourceAttribution(self):  # pragma: no cover
        return SourceAttribution.make_many(self.boto3_raw_data["sourceAttribution"])

    @cached_property
    def actionReview(self):  # pragma: no cover
        return ActionReview.make_one(self.boto3_raw_data["actionReview"])

    @cached_property
    def actionExecution(self):  # pragma: no cover
        return ActionExecutionOutput.make_one(self.boto3_raw_data["actionExecution"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataEvent:
    boto3_raw_data: "type_defs.MetadataEventTypeDef" = dataclasses.field()

    conversationId = field("conversationId")
    userMessageId = field("userMessageId")
    systemMessageId = field("systemMessageId")

    @cached_property
    def sourceAttributions(self):  # pragma: no cover
        return SourceAttribution.make_many(self.boto3_raw_data["sourceAttributions"])

    finalTextMessage = field("finalTextMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChatControlsConfigurationResponse:
    boto3_raw_data: "type_defs.GetChatControlsConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    responseScope = field("responseScope")

    @cached_property
    def orchestrationConfiguration(self):  # pragma: no cover
        return AppliedOrchestrationConfiguration.make_one(
            self.boto3_raw_data["orchestrationConfiguration"]
        )

    @cached_property
    def blockedPhrases(self):  # pragma: no cover
        return BlockedPhrasesConfiguration.make_one(
            self.boto3_raw_data["blockedPhrases"]
        )

    @cached_property
    def topicConfigurations(self):  # pragma: no cover
        return TopicConfigurationOutput.make_many(
            self.boto3_raw_data["topicConfigurations"]
        )

    @cached_property
    def creatorModeConfiguration(self):  # pragma: no cover
        return AppliedCreatorModeConfiguration.make_one(
            self.boto3_raw_data["creatorModeConfiguration"]
        )

    @cached_property
    def hallucinationReductionConfiguration(self):  # pragma: no cover
        return HallucinationReductionConfiguration.make_one(
            self.boto3_raw_data["hallucinationReductionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetChatControlsConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChatControlsConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    ruleType = field("ruleType")
    includedUsersAndGroups = field("includedUsersAndGroups")
    excludedUsersAndGroups = field("excludedUsersAndGroups")
    ruleConfiguration = field("ruleConfiguration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRetrieverRequest:
    boto3_raw_data: "type_defs.CreateRetrieverRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    type = field("type")
    displayName = field("displayName")
    configuration = field("configuration")
    roleArn = field("roleArn")
    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRetrieverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRetrieverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRetrieverRequest:
    boto3_raw_data: "type_defs.UpdateRetrieverRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    retrieverId = field("retrieverId")
    configuration = field("configuration")
    displayName = field("displayName")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRetrieverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRetrieverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataAccessorResponse:
    boto3_raw_data: "type_defs.GetDataAccessorResponseTypeDef" = dataclasses.field()

    displayName = field("displayName")
    dataAccessorId = field("dataAccessorId")
    dataAccessorArn = field("dataAccessorArn")
    applicationId = field("applicationId")
    idcApplicationArn = field("idcApplicationArn")
    principal = field("principal")

    @cached_property
    def actionConfigurations(self):  # pragma: no cover
        return ActionConfigurationOutput.make_many(
            self.boto3_raw_data["actionConfigurations"]
        )

    @cached_property
    def authenticationDetail(self):  # pragma: no cover
        return DataAccessorAuthenticationDetailOutput.make_one(
            self.boto3_raw_data["authenticationDetail"]
        )

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataAccessorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataAccessorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HookConfiguration:
    boto3_raw_data: "type_defs.HookConfigurationTypeDef" = dataclasses.field()

    invocationCondition = field("invocationCondition")
    lambdaArn = field("lambdaArn")
    s3BucketName = field("s3BucketName")
    roleArn = field("roleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HookConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HookConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineDocumentEnrichmentConfiguration:
    boto3_raw_data: "type_defs.InlineDocumentEnrichmentConfigurationTypeDef" = (
        dataclasses.field()
    )

    condition = field("condition")
    target = field("target")
    documentContentOperator = field("documentContentOperator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InlineDocumentEnrichmentConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineDocumentEnrichmentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeFilterPaginator:
    boto3_raw_data: "type_defs.AttributeFilterPaginatorTypeDef" = dataclasses.field()

    andAllFilters = field("andAllFilters")
    orAllFilters = field("orAllFilters")
    notFilter = field("notFilter")
    equalsTo = field("equalsTo")
    containsAll = field("containsAll")
    containsAny = field("containsAny")
    greaterThan = field("greaterThan")
    greaterThanOrEquals = field("greaterThanOrEquals")
    lessThan = field("lessThan")
    lessThanOrEquals = field("lessThanOrEquals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeFilterPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeFilterPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeFilter:
    boto3_raw_data: "type_defs.AttributeFilterTypeDef" = dataclasses.field()

    andAllFilters = field("andAllFilters")
    orAllFilters = field("orAllFilters")
    notFilter = field("notFilter")
    equalsTo = field("equalsTo")
    containsAll = field("containsAll")
    containsAny = field("containsAny")
    greaterThan = field("greaterThan")
    greaterThanOrEquals = field("greaterThanOrEquals")
    lessThan = field("lessThan")
    lessThanOrEquals = field("lessThanOrEquals")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessagesResponse:
    boto3_raw_data: "type_defs.ListMessagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["messages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatOutputStream:
    boto3_raw_data: "type_defs.ChatOutputStreamTypeDef" = dataclasses.field()

    @cached_property
    def textEvent(self):  # pragma: no cover
        return TextOutputEvent.make_one(self.boto3_raw_data["textEvent"])

    @cached_property
    def metadataEvent(self):  # pragma: no cover
        return MetadataEvent.make_one(self.boto3_raw_data["metadataEvent"])

    @cached_property
    def actionReviewEvent(self):  # pragma: no cover
        return ActionReviewEvent.make_one(self.boto3_raw_data["actionReviewEvent"])

    @cached_property
    def failedAttachmentEvent(self):  # pragma: no cover
        return FailedAttachmentEvent.make_one(
            self.boto3_raw_data["failedAttachmentEvent"]
        )

    @cached_property
    def authChallengeRequestEvent(self):  # pragma: no cover
        return AuthChallengeRequestEvent.make_one(
            self.boto3_raw_data["authChallengeRequestEvent"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChatOutputStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChatOutputStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRelevantContentRequestPaginate:
    boto3_raw_data: "type_defs.SearchRelevantContentRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    queryText = field("queryText")

    @cached_property
    def contentSource(self):  # pragma: no cover
        return ContentSource.make_one(self.boto3_raw_data["contentSource"])

    @cached_property
    def attributeFilter(self):  # pragma: no cover
        return AttributeFilterPaginator.make_one(self.boto3_raw_data["attributeFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchRelevantContentRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRelevantContentRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatOutput:
    boto3_raw_data: "type_defs.ChatOutputTypeDef" = dataclasses.field()

    outputStream = field("outputStream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChatOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChatOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicConfiguration:
    boto3_raw_data: "type_defs.TopicConfigurationTypeDef" = dataclasses.field()

    name = field("name")
    rules = field("rules")
    description = field("description")
    exampleChatMessages = field("exampleChatMessages")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentEnrichmentConfiguration:
    boto3_raw_data: "type_defs.DocumentEnrichmentConfigurationTypeDef" = (
        dataclasses.field()
    )

    inlineConfigurations = field("inlineConfigurations")
    preExtractionHookConfiguration = field("preExtractionHookConfiguration")
    postExtractionHookConfiguration = field("postExtractionHookConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentEnrichmentConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentEnrichmentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionFilterConfiguration:
    boto3_raw_data: "type_defs.ActionFilterConfigurationTypeDef" = dataclasses.field()

    documentAttributeFilter = field("documentAttributeFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionFilterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionFilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatSyncInput:
    boto3_raw_data: "type_defs.ChatSyncInputTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    userId = field("userId")
    userGroups = field("userGroups")
    userMessage = field("userMessage")

    @cached_property
    def attachments(self):  # pragma: no cover
        return AttachmentInput.make_many(self.boto3_raw_data["attachments"])

    actionExecution = field("actionExecution")

    @cached_property
    def authChallengeResponse(self):  # pragma: no cover
        return AuthChallengeResponse.make_one(
            self.boto3_raw_data["authChallengeResponse"]
        )

    conversationId = field("conversationId")
    parentMessageId = field("parentMessageId")
    attributeFilter = field("attributeFilter")
    chatMode = field("chatMode")

    @cached_property
    def chatModeConfiguration(self):  # pragma: no cover
        return ChatModeConfiguration.make_one(
            self.boto3_raw_data["chatModeConfiguration"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChatSyncInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChatSyncInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationEvent:
    boto3_raw_data: "type_defs.ConfigurationEventTypeDef" = dataclasses.field()

    chatMode = field("chatMode")

    @cached_property
    def chatModeConfiguration(self):  # pragma: no cover
        return ChatModeConfiguration.make_one(
            self.boto3_raw_data["chatModeConfiguration"]
        )

    attributeFilter = field("attributeFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRelevantContentRequest:
    boto3_raw_data: "type_defs.SearchRelevantContentRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    queryText = field("queryText")

    @cached_property
    def contentSource(self):  # pragma: no cover
        return ContentSource.make_one(self.boto3_raw_data["contentSource"])

    attributeFilter = field("attributeFilter")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchRelevantContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRelevantContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatInputStream:
    boto3_raw_data: "type_defs.ChatInputStreamTypeDef" = dataclasses.field()

    @cached_property
    def configurationEvent(self):  # pragma: no cover
        return ConfigurationEvent.make_one(self.boto3_raw_data["configurationEvent"])

    @cached_property
    def textEvent(self):  # pragma: no cover
        return TextInputEvent.make_one(self.boto3_raw_data["textEvent"])

    @cached_property
    def attachmentEvent(self):  # pragma: no cover
        return AttachmentInputEvent.make_one(self.boto3_raw_data["attachmentEvent"])

    @cached_property
    def actionExecutionEvent(self):  # pragma: no cover
        return ActionExecutionEvent.make_one(
            self.boto3_raw_data["actionExecutionEvent"]
        )

    endOfInputEvent = field("endOfInputEvent")

    @cached_property
    def authChallengeResponseEvent(self):  # pragma: no cover
        return AuthChallengeResponseEvent.make_one(
            self.boto3_raw_data["authChallengeResponseEvent"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChatInputStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChatInputStreamTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChatControlsConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateChatControlsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    clientToken = field("clientToken")
    responseScope = field("responseScope")

    @cached_property
    def orchestrationConfiguration(self):  # pragma: no cover
        return OrchestrationConfiguration.make_one(
            self.boto3_raw_data["orchestrationConfiguration"]
        )

    @cached_property
    def blockedPhrasesConfigurationUpdate(self):  # pragma: no cover
        return BlockedPhrasesConfigurationUpdate.make_one(
            self.boto3_raw_data["blockedPhrasesConfigurationUpdate"]
        )

    topicConfigurationsToCreateOrUpdate = field("topicConfigurationsToCreateOrUpdate")
    topicConfigurationsToDelete = field("topicConfigurationsToDelete")

    @cached_property
    def creatorModeConfiguration(self):  # pragma: no cover
        return CreatorModeConfiguration.make_one(
            self.boto3_raw_data["creatorModeConfiguration"]
        )

    @cached_property
    def hallucinationReductionConfiguration(self):  # pragma: no cover
        return HallucinationReductionConfiguration.make_one(
            self.boto3_raw_data["hallucinationReductionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateChatControlsConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChatControlsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceRequest:
    boto3_raw_data: "type_defs.CreateDataSourceRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    displayName = field("displayName")
    configuration = field("configuration")
    vpcConfiguration = field("vpcConfiguration")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    syncSchedule = field("syncSchedule")
    roleArn = field("roleArn")
    clientToken = field("clientToken")
    documentEnrichmentConfiguration = field("documentEnrichmentConfiguration")

    @cached_property
    def mediaExtractionConfiguration(self):  # pragma: no cover
        return MediaExtractionConfiguration.make_one(
            self.boto3_raw_data["mediaExtractionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Document:
    boto3_raw_data: "type_defs.DocumentTypeDef" = dataclasses.field()

    id = field("id")
    attributes = field("attributes")

    @cached_property
    def content(self):  # pragma: no cover
        return DocumentContent.make_one(self.boto3_raw_data["content"])

    contentType = field("contentType")
    title = field("title")

    @cached_property
    def accessConfiguration(self):  # pragma: no cover
        return AccessConfiguration.make_one(self.boto3_raw_data["accessConfiguration"])

    documentEnrichmentConfiguration = field("documentEnrichmentConfiguration")

    @cached_property
    def mediaExtractionConfiguration(self):  # pragma: no cover
        return MediaExtractionConfiguration.make_one(
            self.boto3_raw_data["mediaExtractionConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceRequest:
    boto3_raw_data: "type_defs.UpdateDataSourceRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")
    dataSourceId = field("dataSourceId")
    displayName = field("displayName")
    configuration = field("configuration")
    vpcConfiguration = field("vpcConfiguration")
    description = field("description")
    syncSchedule = field("syncSchedule")
    roleArn = field("roleArn")
    documentEnrichmentConfiguration = field("documentEnrichmentConfiguration")

    @cached_property
    def mediaExtractionConfiguration(self):  # pragma: no cover
        return MediaExtractionConfiguration.make_one(
            self.boto3_raw_data["mediaExtractionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionConfiguration:
    boto3_raw_data: "type_defs.ActionConfigurationTypeDef" = dataclasses.field()

    action = field("action")
    filterConfiguration = field("filterConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatInput:
    boto3_raw_data: "type_defs.ChatInputTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    userId = field("userId")
    userGroups = field("userGroups")
    conversationId = field("conversationId")
    parentMessageId = field("parentMessageId")
    clientToken = field("clientToken")
    inputStream = field("inputStream")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChatInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChatInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutDocumentRequest:
    boto3_raw_data: "type_defs.BatchPutDocumentRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    indexId = field("indexId")

    @cached_property
    def documents(self):  # pragma: no cover
        return Document.make_many(self.boto3_raw_data["documents"])

    roleArn = field("roleArn")
    dataSourceSyncId = field("dataSourceSyncId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataAccessorRequest:
    boto3_raw_data: "type_defs.CreateDataAccessorRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    principal = field("principal")
    actionConfigurations = field("actionConfigurations")
    displayName = field("displayName")
    clientToken = field("clientToken")
    authenticationDetail = field("authenticationDetail")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataAccessorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataAccessorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataAccessorRequest:
    boto3_raw_data: "type_defs.UpdateDataAccessorRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    dataAccessorId = field("dataAccessorId")
    actionConfigurations = field("actionConfigurations")
    authenticationDetail = field("authenticationDetail")
    displayName = field("displayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataAccessorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataAccessorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
