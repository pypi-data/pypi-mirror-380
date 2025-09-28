# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_wafv2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class APIKeySummary:
    boto3_raw_data: "type_defs.APIKeySummaryTypeDef" = dataclasses.field()

    TokenDomains = field("TokenDomains")
    APIKey = field("APIKey")
    CreationTimestamp = field("CreationTimestamp")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.APIKeySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.APIKeySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AWSManagedRulesBotControlRuleSet:
    boto3_raw_data: "type_defs.AWSManagedRulesBotControlRuleSetTypeDef" = (
        dataclasses.field()
    )

    InspectionLevel = field("InspectionLevel")
    EnableMachineLearning = field("EnableMachineLearning")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AWSManagedRulesBotControlRuleSetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AWSManagedRulesBotControlRuleSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionCondition:
    boto3_raw_data: "type_defs.ActionConditionTypeDef" = dataclasses.field()

    Action = field("Action")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddressField:
    boto3_raw_data: "type_defs.AddressFieldTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AndStatementOutput:
    boto3_raw_data: "type_defs.AndStatementOutputTypeDef" = dataclasses.field()

    Statements = field("Statements")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AndStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AndStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AndStatement:
    boto3_raw_data: "type_defs.AndStatementTypeDef" = dataclasses.field()

    Statements = field("Statements")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AndStatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AndStatementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationAttributeOutput:
    boto3_raw_data: "type_defs.ApplicationAttributeOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationAttributeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationAttributeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationAttribute:
    boto3_raw_data: "type_defs.ApplicationAttributeTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForwardedIPConfig:
    boto3_raw_data: "type_defs.ForwardedIPConfigTypeDef" = dataclasses.field()

    HeaderName = field("HeaderName")
    FallbackBehavior = field("FallbackBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ForwardedIPConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForwardedIPConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateWebACLRequest:
    boto3_raw_data: "type_defs.AssociateWebACLRequestTypeDef" = dataclasses.field()

    WebACLArn = field("WebACLArn")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateWebACLRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestBodyAssociatedResourceTypeConfig:
    boto3_raw_data: "type_defs.RequestBodyAssociatedResourceTypeConfigTypeDef" = (
        dataclasses.field()
    )

    DefaultSizeInspectionLimit = field("DefaultSizeInspectionLimit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestBodyAssociatedResourceTypeConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestBodyAssociatedResourceTypeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Body:
    boto3_raw_data: "type_defs.BodyTypeDef" = dataclasses.field()

    OversizeHandling = field("OversizeHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BodyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BodyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextTransformation:
    boto3_raw_data: "type_defs.TextTransformationTypeDef" = dataclasses.field()

    Priority = field("Priority")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextTransformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextTransformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImmunityTimeProperty:
    boto3_raw_data: "type_defs.ImmunityTimePropertyTypeDef" = dataclasses.field()

    ImmunityTime = field("ImmunityTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImmunityTimePropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImmunityTimePropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptchaResponse:
    boto3_raw_data: "type_defs.CaptchaResponseTypeDef" = dataclasses.field()

    ResponseCode = field("ResponseCode")
    SolveTimestamp = field("SolveTimestamp")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaptchaResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaptchaResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChallengeResponse:
    boto3_raw_data: "type_defs.ChallengeResponseTypeDef" = dataclasses.field()

    ResponseCode = field("ResponseCode")
    SolveTimestamp = field("SolveTimestamp")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChallengeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChallengeResponseTypeDef"]
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
class Regex:
    boto3_raw_data: "type_defs.RegexTypeDef" = dataclasses.field()

    RegexString = field("RegexString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegexTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegexTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelNameCondition:
    boto3_raw_data: "type_defs.LabelNameConditionTypeDef" = dataclasses.field()

    LabelName = field("LabelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LabelNameConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LabelNameConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookieMatchPatternOutput:
    boto3_raw_data: "type_defs.CookieMatchPatternOutputTypeDef" = dataclasses.field()

    All = field("All")
    IncludedCookies = field("IncludedCookies")
    ExcludedCookies = field("ExcludedCookies")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CookieMatchPatternOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CookieMatchPatternOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookieMatchPattern:
    boto3_raw_data: "type_defs.CookieMatchPatternTypeDef" = dataclasses.field()

    All = field("All")
    IncludedCookies = field("IncludedCookies")
    ExcludedCookies = field("ExcludedCookies")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CookieMatchPatternTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CookieMatchPatternTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAPIKeyRequest:
    boto3_raw_data: "type_defs.CreateAPIKeyRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    TokenDomains = field("TokenDomains")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAPIKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAPIKeyRequestTypeDef"]
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

    Key = field("Key")
    Value = field("Value")

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
class IPSetSummary:
    boto3_raw_data: "type_defs.IPSetSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Description = field("Description")
    LockToken = field("LockToken")
    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IPSetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IPSetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegexPatternSetSummary:
    boto3_raw_data: "type_defs.RegexPatternSetSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Description = field("Description")
    LockToken = field("LockToken")
    ARN = field("ARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegexPatternSetSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegexPatternSetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomResponseBody:
    boto3_raw_data: "type_defs.CustomResponseBodyTypeDef" = dataclasses.field()

    ContentType = field("ContentType")
    Content = field("Content")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomResponseBodyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomResponseBodyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VisibilityConfig:
    boto3_raw_data: "type_defs.VisibilityConfigTypeDef" = dataclasses.field()

    SampledRequestsEnabled = field("SampledRequestsEnabled")
    CloudWatchMetricsEnabled = field("CloudWatchMetricsEnabled")
    MetricName = field("MetricName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VisibilityConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VisibilityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleGroupSummary:
    boto3_raw_data: "type_defs.RuleGroupSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Description = field("Description")
    LockToken = field("LockToken")
    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleGroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnSourceDDoSProtectionConfig:
    boto3_raw_data: "type_defs.OnSourceDDoSProtectionConfigTypeDef" = (
        dataclasses.field()
    )

    ALBLowReputationMode = field("ALBLowReputationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnSourceDDoSProtectionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnSourceDDoSProtectionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebACLSummary:
    boto3_raw_data: "type_defs.WebACLSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Description = field("Description")
    LockToken = field("LockToken")
    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebACLSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WebACLSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomHTTPHeader:
    boto3_raw_data: "type_defs.CustomHTTPHeaderTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomHTTPHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomHTTPHeaderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldToProtectOutput:
    boto3_raw_data: "type_defs.FieldToProtectOutputTypeDef" = dataclasses.field()

    FieldType = field("FieldType")
    FieldKeys = field("FieldKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldToProtectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldToProtectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldToProtect:
    boto3_raw_data: "type_defs.FieldToProtectTypeDef" = dataclasses.field()

    FieldType = field("FieldType")
    FieldKeys = field("FieldKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldToProtectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldToProtectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAPIKeyRequest:
    boto3_raw_data: "type_defs.DeleteAPIKeyRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    APIKey = field("APIKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAPIKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAPIKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallManagerRuleGroupsRequest:
    boto3_raw_data: "type_defs.DeleteFirewallManagerRuleGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    WebACLArn = field("WebACLArn")
    WebACLLockToken = field("WebACLLockToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFirewallManagerRuleGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallManagerRuleGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIPSetRequest:
    boto3_raw_data: "type_defs.DeleteIPSetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    LockToken = field("LockToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIPSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIPSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoggingConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteLoggingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    LogType = field("LogType")
    LogScope = field("LogScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLoggingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoggingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePermissionPolicyRequest:
    boto3_raw_data: "type_defs.DeletePermissionPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePermissionPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePermissionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRegexPatternSetRequest:
    boto3_raw_data: "type_defs.DeleteRegexPatternSetRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    LockToken = field("LockToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRegexPatternSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRegexPatternSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRuleGroupRequest:
    boto3_raw_data: "type_defs.DeleteRuleGroupRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    LockToken = field("LockToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWebACLRequest:
    boto3_raw_data: "type_defs.DeleteWebACLRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    LockToken = field("LockToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWebACLRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAllManagedProductsRequest:
    boto3_raw_data: "type_defs.DescribeAllManagedProductsRequestTypeDef" = (
        dataclasses.field()
    )

    Scope = field("Scope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAllManagedProductsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAllManagedProductsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedProductDescriptor:
    boto3_raw_data: "type_defs.ManagedProductDescriptorTypeDef" = dataclasses.field()

    VendorName = field("VendorName")
    ManagedRuleSetName = field("ManagedRuleSetName")
    ProductId = field("ProductId")
    ProductLink = field("ProductLink")
    ProductTitle = field("ProductTitle")
    ProductDescription = field("ProductDescription")
    SnsTopicArn = field("SnsTopicArn")
    IsVersioningSupported = field("IsVersioningSupported")
    IsAdvancedManagedRuleSet = field("IsAdvancedManagedRuleSet")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedProductDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedProductDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedProductsByVendorRequest:
    boto3_raw_data: "type_defs.DescribeManagedProductsByVendorRequestTypeDef" = (
        dataclasses.field()
    )

    VendorName = field("VendorName")
    Scope = field("Scope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeManagedProductsByVendorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedProductsByVendorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedRuleGroupRequest:
    boto3_raw_data: "type_defs.DescribeManagedRuleGroupRequestTypeDef" = (
        dataclasses.field()
    )

    VendorName = field("VendorName")
    Name = field("Name")
    Scope = field("Scope")
    VersionName = field("VersionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeManagedRuleGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelSummary:
    boto3_raw_data: "type_defs.LabelSummaryTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateWebACLRequest:
    boto3_raw_data: "type_defs.DisassociateWebACLRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateWebACLRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailField:
    boto3_raw_data: "type_defs.EmailFieldTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailFieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExcludedRule:
    boto3_raw_data: "type_defs.ExcludedRuleTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExcludedRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExcludedRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeaderOrder:
    boto3_raw_data: "type_defs.HeaderOrderTypeDef" = dataclasses.field()

    OversizeHandling = field("OversizeHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeaderOrderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeaderOrderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JA3Fingerprint:
    boto3_raw_data: "type_defs.JA3FingerprintTypeDef" = dataclasses.field()

    FallbackBehavior = field("FallbackBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JA3FingerprintTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JA3FingerprintTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JA4Fingerprint:
    boto3_raw_data: "type_defs.JA4FingerprintTypeDef" = dataclasses.field()

    FallbackBehavior = field("FallbackBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JA4FingerprintTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JA4FingerprintTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SingleHeader:
    boto3_raw_data: "type_defs.SingleHeaderTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SingleHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SingleHeaderTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SingleQueryArgument:
    boto3_raw_data: "type_defs.SingleQueryArgumentTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SingleQueryArgumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingleQueryArgumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UriFragment:
    boto3_raw_data: "type_defs.UriFragmentTypeDef" = dataclasses.field()

    FallbackBehavior = field("FallbackBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UriFragmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UriFragmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMobileSdkReleaseUrlRequest:
    boto3_raw_data: "type_defs.GenerateMobileSdkReleaseUrlRequestTypeDef" = (
        dataclasses.field()
    )

    Platform = field("Platform")
    ReleaseVersion = field("ReleaseVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateMobileSdkReleaseUrlRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMobileSdkReleaseUrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDecryptedAPIKeyRequest:
    boto3_raw_data: "type_defs.GetDecryptedAPIKeyRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    APIKey = field("APIKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDecryptedAPIKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDecryptedAPIKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIPSetRequest:
    boto3_raw_data: "type_defs.GetIPSetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIPSetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetIPSetRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IPSet:
    boto3_raw_data: "type_defs.IPSetTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    ARN = field("ARN")
    IPAddressVersion = field("IPAddressVersion")
    Addresses = field("Addresses")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IPSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IPSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoggingConfigurationRequest:
    boto3_raw_data: "type_defs.GetLoggingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    LogType = field("LogType")
    LogScope = field("LogScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLoggingConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoggingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedRuleSetRequest:
    boto3_raw_data: "type_defs.GetManagedRuleSetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetManagedRuleSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedRuleSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMobileSdkReleaseRequest:
    boto3_raw_data: "type_defs.GetMobileSdkReleaseRequestTypeDef" = dataclasses.field()

    Platform = field("Platform")
    ReleaseVersion = field("ReleaseVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMobileSdkReleaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMobileSdkReleaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPermissionPolicyRequest:
    boto3_raw_data: "type_defs.GetPermissionPolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPermissionPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPermissionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRateBasedStatementManagedKeysRequest:
    boto3_raw_data: "type_defs.GetRateBasedStatementManagedKeysRequestTypeDef" = (
        dataclasses.field()
    )

    Scope = field("Scope")
    WebACLName = field("WebACLName")
    WebACLId = field("WebACLId")
    RuleName = field("RuleName")
    RuleGroupRuleName = field("RuleGroupRuleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRateBasedStatementManagedKeysRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRateBasedStatementManagedKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateBasedStatementManagedKeysIPSet:
    boto3_raw_data: "type_defs.RateBasedStatementManagedKeysIPSetTypeDef" = (
        dataclasses.field()
    )

    IPAddressVersion = field("IPAddressVersion")
    Addresses = field("Addresses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RateBasedStatementManagedKeysIPSetTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateBasedStatementManagedKeysIPSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRegexPatternSetRequest:
    boto3_raw_data: "type_defs.GetRegexPatternSetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRegexPatternSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRegexPatternSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleGroupRequest:
    boto3_raw_data: "type_defs.GetRuleGroupRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    ARN = field("ARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRuleGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeWindowOutput:
    boto3_raw_data: "type_defs.TimeWindowOutputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeWindowOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeWindowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWebACLForResourceRequest:
    boto3_raw_data: "type_defs.GetWebACLForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWebACLForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWebACLForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWebACLRequest:
    boto3_raw_data: "type_defs.GetWebACLRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetWebACLRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HTTPHeader:
    boto3_raw_data: "type_defs.HTTPHeaderTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HTTPHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HTTPHeaderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeaderMatchPatternOutput:
    boto3_raw_data: "type_defs.HeaderMatchPatternOutputTypeDef" = dataclasses.field()

    All = field("All")
    IncludedHeaders = field("IncludedHeaders")
    ExcludedHeaders = field("ExcludedHeaders")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HeaderMatchPatternOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeaderMatchPatternOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeaderMatchPattern:
    boto3_raw_data: "type_defs.HeaderMatchPatternTypeDef" = dataclasses.field()

    All = field("All")
    IncludedHeaders = field("IncludedHeaders")
    ExcludedHeaders = field("ExcludedHeaders")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HeaderMatchPatternTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeaderMatchPatternTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IPSetForwardedIPConfig:
    boto3_raw_data: "type_defs.IPSetForwardedIPConfigTypeDef" = dataclasses.field()

    HeaderName = field("HeaderName")
    FallbackBehavior = field("FallbackBehavior")
    Position = field("Position")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IPSetForwardedIPConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IPSetForwardedIPConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JsonMatchPatternOutput:
    boto3_raw_data: "type_defs.JsonMatchPatternOutputTypeDef" = dataclasses.field()

    All = field("All")
    IncludedPaths = field("IncludedPaths")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JsonMatchPatternOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JsonMatchPatternOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JsonMatchPattern:
    boto3_raw_data: "type_defs.JsonMatchPatternTypeDef" = dataclasses.field()

    All = field("All")
    IncludedPaths = field("IncludedPaths")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JsonMatchPatternTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JsonMatchPatternTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelMatchStatement:
    boto3_raw_data: "type_defs.LabelMatchStatementTypeDef" = dataclasses.field()

    Scope = field("Scope")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LabelMatchStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LabelMatchStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Label:
    boto3_raw_data: "type_defs.LabelTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAPIKeysRequest:
    boto3_raw_data: "type_defs.ListAPIKeysRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAPIKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAPIKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableManagedRuleGroupVersionsRequest:
    boto3_raw_data: "type_defs.ListAvailableManagedRuleGroupVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    VendorName = field("VendorName")
    Name = field("Name")
    Scope = field("Scope")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableManagedRuleGroupVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableManagedRuleGroupVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleGroupVersion:
    boto3_raw_data: "type_defs.ManagedRuleGroupVersionTypeDef" = dataclasses.field()

    Name = field("Name")
    LastUpdateTimestamp = field("LastUpdateTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleGroupVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleGroupVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableManagedRuleGroupsRequest:
    boto3_raw_data: "type_defs.ListAvailableManagedRuleGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    Scope = field("Scope")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableManagedRuleGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableManagedRuleGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleGroupSummary:
    boto3_raw_data: "type_defs.ManagedRuleGroupSummaryTypeDef" = dataclasses.field()

    VendorName = field("VendorName")
    Name = field("Name")
    VersioningSupported = field("VersioningSupported")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIPSetsRequest:
    boto3_raw_data: "type_defs.ListIPSetsRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListIPSetsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIPSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoggingConfigurationsRequest:
    boto3_raw_data: "type_defs.ListLoggingConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    Scope = field("Scope")
    NextMarker = field("NextMarker")
    Limit = field("Limit")
    LogScope = field("LogScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLoggingConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoggingConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedRuleSetsRequest:
    boto3_raw_data: "type_defs.ListManagedRuleSetsRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedRuleSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedRuleSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleSetSummary:
    boto3_raw_data: "type_defs.ManagedRuleSetSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Description = field("Description")
    LockToken = field("LockToken")
    ARN = field("ARN")
    LabelNamespace = field("LabelNamespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleSetSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleSetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMobileSdkReleasesRequest:
    boto3_raw_data: "type_defs.ListMobileSdkReleasesRequestTypeDef" = (
        dataclasses.field()
    )

    Platform = field("Platform")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMobileSdkReleasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMobileSdkReleasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleaseSummary:
    boto3_raw_data: "type_defs.ReleaseSummaryTypeDef" = dataclasses.field()

    ReleaseVersion = field("ReleaseVersion")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReleaseSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReleaseSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegexPatternSetsRequest:
    boto3_raw_data: "type_defs.ListRegexPatternSetsRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRegexPatternSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegexPatternSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesForWebACLRequest:
    boto3_raw_data: "type_defs.ListResourcesForWebACLRequestTypeDef" = (
        dataclasses.field()
    )

    WebACLArn = field("WebACLArn")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourcesForWebACLRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesForWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleGroupsRequest:
    boto3_raw_data: "type_defs.ListRuleGroupsRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleGroupsRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

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
class ListWebACLsRequest:
    boto3_raw_data: "type_defs.ListWebACLsRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    NextMarker = field("NextMarker")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebACLsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebACLsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PasswordField:
    boto3_raw_data: "type_defs.PasswordFieldTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PasswordFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PasswordFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsernameField:
    boto3_raw_data: "type_defs.UsernameFieldTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsernameFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsernameFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleSetVersion:
    boto3_raw_data: "type_defs.ManagedRuleSetVersionTypeDef" = dataclasses.field()

    AssociatedRuleGroupArn = field("AssociatedRuleGroupArn")
    Capacity = field("Capacity")
    ForecastedLifetime = field("ForecastedLifetime")
    PublishTimestamp = field("PublishTimestamp")
    LastUpdateTimestamp = field("LastUpdateTimestamp")
    ExpiryTimestamp = field("ExpiryTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleSetVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleSetVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotStatementOutput:
    boto3_raw_data: "type_defs.NotStatementOutputTypeDef" = dataclasses.field()

    Statement = field("Statement")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotStatement:
    boto3_raw_data: "type_defs.NotStatementTypeDef" = dataclasses.field()

    Statement = field("Statement")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotStatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NotStatementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrStatementOutput:
    boto3_raw_data: "type_defs.OrStatementOutputTypeDef" = dataclasses.field()

    Statements = field("Statements")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrStatementOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrStatement:
    boto3_raw_data: "type_defs.OrStatementTypeDef" = dataclasses.field()

    Statements = field("Statements")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrStatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OrStatementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberField:
    boto3_raw_data: "type_defs.PhoneNumberFieldTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionToPublish:
    boto3_raw_data: "type_defs.VersionToPublishTypeDef" = dataclasses.field()

    AssociatedRuleGroupArn = field("AssociatedRuleGroupArn")
    ForecastedLifetime = field("ForecastedLifetime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VersionToPublishTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersionToPublishTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPermissionPolicyRequest:
    boto3_raw_data: "type_defs.PutPermissionPolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPermissionPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPermissionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitJA3Fingerprint:
    boto3_raw_data: "type_defs.RateLimitJA3FingerprintTypeDef" = dataclasses.field()

    FallbackBehavior = field("FallbackBehavior")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitJA3FingerprintTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitJA3FingerprintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitJA4Fingerprint:
    boto3_raw_data: "type_defs.RateLimitJA4FingerprintTypeDef" = dataclasses.field()

    FallbackBehavior = field("FallbackBehavior")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitJA4FingerprintTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitJA4FingerprintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitLabelNamespace:
    boto3_raw_data: "type_defs.RateLimitLabelNamespaceTypeDef" = dataclasses.field()

    Namespace = field("Namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitLabelNamespaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitLabelNamespaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspectionBodyContainsOutput:
    boto3_raw_data: "type_defs.ResponseInspectionBodyContainsOutputTypeDef" = (
        dataclasses.field()
    )

    SuccessStrings = field("SuccessStrings")
    FailureStrings = field("FailureStrings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseInspectionBodyContainsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionBodyContainsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspectionBodyContains:
    boto3_raw_data: "type_defs.ResponseInspectionBodyContainsTypeDef" = (
        dataclasses.field()
    )

    SuccessStrings = field("SuccessStrings")
    FailureStrings = field("FailureStrings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResponseInspectionBodyContainsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionBodyContainsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspectionHeaderOutput:
    boto3_raw_data: "type_defs.ResponseInspectionHeaderOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    SuccessValues = field("SuccessValues")
    FailureValues = field("FailureValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResponseInspectionHeaderOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionHeaderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspectionHeader:
    boto3_raw_data: "type_defs.ResponseInspectionHeaderTypeDef" = dataclasses.field()

    Name = field("Name")
    SuccessValues = field("SuccessValues")
    FailureValues = field("FailureValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseInspectionHeaderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionHeaderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspectionJsonOutput:
    boto3_raw_data: "type_defs.ResponseInspectionJsonOutputTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    SuccessValues = field("SuccessValues")
    FailureValues = field("FailureValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseInspectionJsonOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionJsonOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspectionJson:
    boto3_raw_data: "type_defs.ResponseInspectionJsonTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    SuccessValues = field("SuccessValues")
    FailureValues = field("FailureValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseInspectionJsonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionJsonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspectionStatusCodeOutput:
    boto3_raw_data: "type_defs.ResponseInspectionStatusCodeOutputTypeDef" = (
        dataclasses.field()
    )

    SuccessCodes = field("SuccessCodes")
    FailureCodes = field("FailureCodes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseInspectionStatusCodeOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionStatusCodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspectionStatusCode:
    boto3_raw_data: "type_defs.ResponseInspectionStatusCodeTypeDef" = (
        dataclasses.field()
    )

    SuccessCodes = field("SuccessCodes")
    FailureCodes = field("FailureCodes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseInspectionStatusCodeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionStatusCodeTypeDef"]
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

    ResourceARN = field("ResourceARN")
    TagKeys = field("TagKeys")

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
class UpdateIPSetRequest:
    boto3_raw_data: "type_defs.UpdateIPSetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    Addresses = field("Addresses")
    LockToken = field("LockToken")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIPSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIPSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationConfigOutput:
    boto3_raw_data: "type_defs.ApplicationConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def Attributes(self):  # pragma: no cover
        return ApplicationAttributeOutput.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationConfig:
    boto3_raw_data: "type_defs.ApplicationConfigTypeDef" = dataclasses.field()

    @cached_property
    def Attributes(self):  # pragma: no cover
        return ApplicationAttribute.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AsnMatchStatementOutput:
    boto3_raw_data: "type_defs.AsnMatchStatementOutputTypeDef" = dataclasses.field()

    AsnList = field("AsnList")

    @cached_property
    def ForwardedIPConfig(self):  # pragma: no cover
        return ForwardedIPConfig.make_one(self.boto3_raw_data["ForwardedIPConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AsnMatchStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AsnMatchStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AsnMatchStatement:
    boto3_raw_data: "type_defs.AsnMatchStatementTypeDef" = dataclasses.field()

    AsnList = field("AsnList")

    @cached_property
    def ForwardedIPConfig(self):  # pragma: no cover
        return ForwardedIPConfig.make_one(self.boto3_raw_data["ForwardedIPConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AsnMatchStatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AsnMatchStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoMatchStatementOutput:
    boto3_raw_data: "type_defs.GeoMatchStatementOutputTypeDef" = dataclasses.field()

    CountryCodes = field("CountryCodes")

    @cached_property
    def ForwardedIPConfig(self):  # pragma: no cover
        return ForwardedIPConfig.make_one(self.boto3_raw_data["ForwardedIPConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeoMatchStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoMatchStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoMatchStatement:
    boto3_raw_data: "type_defs.GeoMatchStatementTypeDef" = dataclasses.field()

    CountryCodes = field("CountryCodes")

    @cached_property
    def ForwardedIPConfig(self):  # pragma: no cover
        return ForwardedIPConfig.make_one(self.boto3_raw_data["ForwardedIPConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeoMatchStatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoMatchStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationConfigOutput:
    boto3_raw_data: "type_defs.AssociationConfigOutputTypeDef" = dataclasses.field()

    RequestBody = field("RequestBody")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationConfig:
    boto3_raw_data: "type_defs.AssociationConfigTypeDef" = dataclasses.field()

    RequestBody = field("RequestBody")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssociationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitCookieOutput:
    boto3_raw_data: "type_defs.RateLimitCookieOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitCookieOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitCookieOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitCookie:
    boto3_raw_data: "type_defs.RateLimitCookieTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RateLimitCookieTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RateLimitCookieTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitHeaderOutput:
    boto3_raw_data: "type_defs.RateLimitHeaderOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitHeaderOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitHeaderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitHeader:
    boto3_raw_data: "type_defs.RateLimitHeaderTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RateLimitHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RateLimitHeaderTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitQueryArgumentOutput:
    boto3_raw_data: "type_defs.RateLimitQueryArgumentOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitQueryArgumentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitQueryArgumentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitQueryArgument:
    boto3_raw_data: "type_defs.RateLimitQueryArgumentTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitQueryArgumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitQueryArgumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitQueryStringOutput:
    boto3_raw_data: "type_defs.RateLimitQueryStringOutputTypeDef" = dataclasses.field()

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitQueryStringOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitQueryStringOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitQueryString:
    boto3_raw_data: "type_defs.RateLimitQueryStringTypeDef" = dataclasses.field()

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitQueryStringTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitQueryStringTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitUriPathOutput:
    boto3_raw_data: "type_defs.RateLimitUriPathOutputTypeDef" = dataclasses.field()

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateLimitUriPathOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitUriPathOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateLimitUriPath:
    boto3_raw_data: "type_defs.RateLimitUriPathTypeDef" = dataclasses.field()

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RateLimitUriPathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateLimitUriPathTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptchaConfig:
    boto3_raw_data: "type_defs.CaptchaConfigTypeDef" = dataclasses.field()

    @cached_property
    def ImmunityTimeProperty(self):  # pragma: no cover
        return ImmunityTimeProperty.make_one(
            self.boto3_raw_data["ImmunityTimeProperty"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaptchaConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaptchaConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChallengeConfig:
    boto3_raw_data: "type_defs.ChallengeConfigTypeDef" = dataclasses.field()

    @cached_property
    def ImmunityTimeProperty(self):  # pragma: no cover
        return ImmunityTimeProperty.make_one(
            self.boto3_raw_data["ImmunityTimeProperty"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChallengeConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChallengeConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckCapacityResponse:
    boto3_raw_data: "type_defs.CheckCapacityResponseTypeDef" = dataclasses.field()

    Capacity = field("Capacity")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckCapacityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckCapacityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAPIKeyResponse:
    boto3_raw_data: "type_defs.CreateAPIKeyResponseTypeDef" = dataclasses.field()

    APIKey = field("APIKey")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAPIKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAPIKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallManagerRuleGroupsResponse:
    boto3_raw_data: "type_defs.DeleteFirewallManagerRuleGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    NextWebACLLockToken = field("NextWebACLLockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFirewallManagerRuleGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallManagerRuleGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMobileSdkReleaseUrlResponse:
    boto3_raw_data: "type_defs.GenerateMobileSdkReleaseUrlResponseTypeDef" = (
        dataclasses.field()
    )

    Url = field("Url")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateMobileSdkReleaseUrlResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMobileSdkReleaseUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDecryptedAPIKeyResponse:
    boto3_raw_data: "type_defs.GetDecryptedAPIKeyResponseTypeDef" = dataclasses.field()

    TokenDomains = field("TokenDomains")
    CreationTimestamp = field("CreationTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDecryptedAPIKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDecryptedAPIKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPermissionPolicyResponse:
    boto3_raw_data: "type_defs.GetPermissionPolicyResponseTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPermissionPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPermissionPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAPIKeysResponse:
    boto3_raw_data: "type_defs.ListAPIKeysResponseTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")

    @cached_property
    def APIKeySummaries(self):  # pragma: no cover
        return APIKeySummary.make_many(self.boto3_raw_data["APIKeySummaries"])

    ApplicationIntegrationURL = field("ApplicationIntegrationURL")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAPIKeysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAPIKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesForWebACLResponse:
    boto3_raw_data: "type_defs.ListResourcesForWebACLResponseTypeDef" = (
        dataclasses.field()
    )

    ResourceArns = field("ResourceArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourcesForWebACLResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesForWebACLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutManagedRuleSetVersionsResponse:
    boto3_raw_data: "type_defs.PutManagedRuleSetVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    NextLockToken = field("NextLockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutManagedRuleSetVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutManagedRuleSetVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIPSetResponse:
    boto3_raw_data: "type_defs.UpdateIPSetResponseTypeDef" = dataclasses.field()

    NextLockToken = field("NextLockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIPSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIPSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateManagedRuleSetVersionExpiryDateResponse:
    boto3_raw_data: "type_defs.UpdateManagedRuleSetVersionExpiryDateResponseTypeDef" = (
        dataclasses.field()
    )

    ExpiringVersion = field("ExpiringVersion")
    ExpiryTimestamp = field("ExpiryTimestamp")
    NextLockToken = field("NextLockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateManagedRuleSetVersionExpiryDateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateManagedRuleSetVersionExpiryDateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRegexPatternSetResponse:
    boto3_raw_data: "type_defs.UpdateRegexPatternSetResponseTypeDef" = (
        dataclasses.field()
    )

    NextLockToken = field("NextLockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRegexPatternSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRegexPatternSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleGroupResponse:
    boto3_raw_data: "type_defs.UpdateRuleGroupResponseTypeDef" = dataclasses.field()

    NextLockToken = field("NextLockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebACLResponse:
    boto3_raw_data: "type_defs.UpdateWebACLResponseTypeDef" = dataclasses.field()

    NextLockToken = field("NextLockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWebACLResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebACLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientSideActionOutput:
    boto3_raw_data: "type_defs.ClientSideActionOutputTypeDef" = dataclasses.field()

    UsageOfAction = field("UsageOfAction")
    Sensitivity = field("Sensitivity")

    @cached_property
    def ExemptUriRegularExpressions(self):  # pragma: no cover
        return Regex.make_many(self.boto3_raw_data["ExemptUriRegularExpressions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientSideActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientSideActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientSideAction:
    boto3_raw_data: "type_defs.ClientSideActionTypeDef" = dataclasses.field()

    UsageOfAction = field("UsageOfAction")
    Sensitivity = field("Sensitivity")

    @cached_property
    def ExemptUriRegularExpressions(self):  # pragma: no cover
        return Regex.make_many(self.boto3_raw_data["ExemptUriRegularExpressions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClientSideActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientSideActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegexPatternSet:
    boto3_raw_data: "type_defs.RegexPatternSetTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    ARN = field("ARN")
    Description = field("Description")

    @cached_property
    def RegularExpressionList(self):  # pragma: no cover
        return Regex.make_many(self.boto3_raw_data["RegularExpressionList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegexPatternSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegexPatternSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRegexPatternSetRequest:
    boto3_raw_data: "type_defs.UpdateRegexPatternSetRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")

    @cached_property
    def RegularExpressionList(self):  # pragma: no cover
        return Regex.make_many(self.boto3_raw_data["RegularExpressionList"])

    LockToken = field("LockToken")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRegexPatternSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRegexPatternSetRequestTypeDef"]
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

    @cached_property
    def ActionCondition(self):  # pragma: no cover
        return ActionCondition.make_one(self.boto3_raw_data["ActionCondition"])

    @cached_property
    def LabelNameCondition(self):  # pragma: no cover
        return LabelNameCondition.make_one(self.boto3_raw_data["LabelNameCondition"])

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
class CookiesOutput:
    boto3_raw_data: "type_defs.CookiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def MatchPattern(self):  # pragma: no cover
        return CookieMatchPatternOutput.make_one(self.boto3_raw_data["MatchPattern"])

    MatchScope = field("MatchScope")
    OversizeHandling = field("OversizeHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CookiesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CookiesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIPSetRequest:
    boto3_raw_data: "type_defs.CreateIPSetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    IPAddressVersion = field("IPAddressVersion")
    Addresses = field("Addresses")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIPSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIPSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegexPatternSetRequest:
    boto3_raw_data: "type_defs.CreateRegexPatternSetRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Scope = field("Scope")

    @cached_property
    def RegularExpressionList(self):  # pragma: no cover
        return Regex.make_many(self.boto3_raw_data["RegularExpressionList"])

    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRegexPatternSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegexPatternSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MobileSdkRelease:
    boto3_raw_data: "type_defs.MobileSdkReleaseTypeDef" = dataclasses.field()

    ReleaseVersion = field("ReleaseVersion")
    Timestamp = field("Timestamp")
    ReleaseNotes = field("ReleaseNotes")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MobileSdkReleaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MobileSdkReleaseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagInfoForResource:
    boto3_raw_data: "type_defs.TagInfoForResourceTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagInfoForResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagInfoForResourceTypeDef"]
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

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateIPSetResponse:
    boto3_raw_data: "type_defs.CreateIPSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Summary(self):  # pragma: no cover
        return IPSetSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIPSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIPSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIPSetsResponse:
    boto3_raw_data: "type_defs.ListIPSetsResponseTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")

    @cached_property
    def IPSets(self):  # pragma: no cover
        return IPSetSummary.make_many(self.boto3_raw_data["IPSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIPSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIPSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegexPatternSetResponse:
    boto3_raw_data: "type_defs.CreateRegexPatternSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summary(self):  # pragma: no cover
        return RegexPatternSetSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRegexPatternSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegexPatternSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegexPatternSetsResponse:
    boto3_raw_data: "type_defs.ListRegexPatternSetsResponseTypeDef" = (
        dataclasses.field()
    )

    NextMarker = field("NextMarker")

    @cached_property
    def RegexPatternSets(self):  # pragma: no cover
        return RegexPatternSetSummary.make_many(self.boto3_raw_data["RegexPatternSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRegexPatternSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegexPatternSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleGroupResponse:
    boto3_raw_data: "type_defs.CreateRuleGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Summary(self):  # pragma: no cover
        return RuleGroupSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRuleGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleGroupsResponse:
    boto3_raw_data: "type_defs.ListRuleGroupsResponseTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")

    @cached_property
    def RuleGroups(self):  # pragma: no cover
        return RuleGroupSummary.make_many(self.boto3_raw_data["RuleGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebACLResponse:
    boto3_raw_data: "type_defs.CreateWebACLResponseTypeDef" = dataclasses.field()

    @cached_property
    def Summary(self):  # pragma: no cover
        return WebACLSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebACLResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebACLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebACLsResponse:
    boto3_raw_data: "type_defs.ListWebACLsResponseTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")

    @cached_property
    def WebACLs(self):  # pragma: no cover
        return WebACLSummary.make_many(self.boto3_raw_data["WebACLs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebACLsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebACLsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRequestHandlingOutput:
    boto3_raw_data: "type_defs.CustomRequestHandlingOutputTypeDef" = dataclasses.field()

    @cached_property
    def InsertHeaders(self):  # pragma: no cover
        return CustomHTTPHeader.make_many(self.boto3_raw_data["InsertHeaders"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomRequestHandlingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRequestHandlingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRequestHandling:
    boto3_raw_data: "type_defs.CustomRequestHandlingTypeDef" = dataclasses.field()

    @cached_property
    def InsertHeaders(self):  # pragma: no cover
        return CustomHTTPHeader.make_many(self.boto3_raw_data["InsertHeaders"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomRequestHandlingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomRequestHandlingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomResponseOutput:
    boto3_raw_data: "type_defs.CustomResponseOutputTypeDef" = dataclasses.field()

    ResponseCode = field("ResponseCode")
    CustomResponseBodyKey = field("CustomResponseBodyKey")

    @cached_property
    def ResponseHeaders(self):  # pragma: no cover
        return CustomHTTPHeader.make_many(self.boto3_raw_data["ResponseHeaders"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomResponseOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomResponseOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomResponse:
    boto3_raw_data: "type_defs.CustomResponseTypeDef" = dataclasses.field()

    ResponseCode = field("ResponseCode")
    CustomResponseBodyKey = field("CustomResponseBodyKey")

    @cached_property
    def ResponseHeaders(self):  # pragma: no cover
        return CustomHTTPHeader.make_many(self.boto3_raw_data["ResponseHeaders"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProtectionOutput:
    boto3_raw_data: "type_defs.DataProtectionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Field(self):  # pragma: no cover
        return FieldToProtectOutput.make_one(self.boto3_raw_data["Field"])

    Action = field("Action")
    ExcludeRuleMatchDetails = field("ExcludeRuleMatchDetails")
    ExcludeRateBasedDetails = field("ExcludeRateBasedDetails")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProtectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProtectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProtection:
    boto3_raw_data: "type_defs.DataProtectionTypeDef" = dataclasses.field()

    @cached_property
    def Field(self):  # pragma: no cover
        return FieldToProtect.make_one(self.boto3_raw_data["Field"])

    Action = field("Action")
    ExcludeRuleMatchDetails = field("ExcludeRuleMatchDetails")
    ExcludeRateBasedDetails = field("ExcludeRateBasedDetails")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataProtectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataProtectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAllManagedProductsResponse:
    boto3_raw_data: "type_defs.DescribeAllManagedProductsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedProducts(self):  # pragma: no cover
        return ManagedProductDescriptor.make_many(
            self.boto3_raw_data["ManagedProducts"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAllManagedProductsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAllManagedProductsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedProductsByVendorResponse:
    boto3_raw_data: "type_defs.DescribeManagedProductsByVendorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedProducts(self):  # pragma: no cover
        return ManagedProductDescriptor.make_many(
            self.boto3_raw_data["ManagedProducts"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeManagedProductsByVendorResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedProductsByVendorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIPSetResponse:
    boto3_raw_data: "type_defs.GetIPSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def IPSet(self):  # pragma: no cover
        return IPSet.make_one(self.boto3_raw_data["IPSet"])

    LockToken = field("LockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIPSetResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIPSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRateBasedStatementManagedKeysResponse:
    boto3_raw_data: "type_defs.GetRateBasedStatementManagedKeysResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedKeysIPV4(self):  # pragma: no cover
        return RateBasedStatementManagedKeysIPSet.make_one(
            self.boto3_raw_data["ManagedKeysIPV4"]
        )

    @cached_property
    def ManagedKeysIPV6(self):  # pragma: no cover
        return RateBasedStatementManagedKeysIPSet.make_one(
            self.boto3_raw_data["ManagedKeysIPV6"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRateBasedStatementManagedKeysResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRateBasedStatementManagedKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HTTPRequest:
    boto3_raw_data: "type_defs.HTTPRequestTypeDef" = dataclasses.field()

    ClientIP = field("ClientIP")
    Country = field("Country")
    URI = field("URI")
    Method = field("Method")
    HTTPVersion = field("HTTPVersion")

    @cached_property
    def Headers(self):  # pragma: no cover
        return HTTPHeader.make_many(self.boto3_raw_data["Headers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HTTPRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HTTPRequestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadersOutput:
    boto3_raw_data: "type_defs.HeadersOutputTypeDef" = dataclasses.field()

    @cached_property
    def MatchPattern(self):  # pragma: no cover
        return HeaderMatchPatternOutput.make_one(self.boto3_raw_data["MatchPattern"])

    MatchScope = field("MatchScope")
    OversizeHandling = field("OversizeHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeadersOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeadersOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IPSetReferenceStatement:
    boto3_raw_data: "type_defs.IPSetReferenceStatementTypeDef" = dataclasses.field()

    ARN = field("ARN")

    @cached_property
    def IPSetForwardedIPConfig(self):  # pragma: no cover
        return IPSetForwardedIPConfig.make_one(
            self.boto3_raw_data["IPSetForwardedIPConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IPSetReferenceStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IPSetReferenceStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JsonBodyOutput:
    boto3_raw_data: "type_defs.JsonBodyOutputTypeDef" = dataclasses.field()

    @cached_property
    def MatchPattern(self):  # pragma: no cover
        return JsonMatchPatternOutput.make_one(self.boto3_raw_data["MatchPattern"])

    MatchScope = field("MatchScope")
    InvalidFallbackBehavior = field("InvalidFallbackBehavior")
    OversizeHandling = field("OversizeHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JsonBodyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JsonBodyOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableManagedRuleGroupVersionsResponse:
    boto3_raw_data: "type_defs.ListAvailableManagedRuleGroupVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    NextMarker = field("NextMarker")

    @cached_property
    def Versions(self):  # pragma: no cover
        return ManagedRuleGroupVersion.make_many(self.boto3_raw_data["Versions"])

    CurrentDefaultVersion = field("CurrentDefaultVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableManagedRuleGroupVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableManagedRuleGroupVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableManagedRuleGroupsResponse:
    boto3_raw_data: "type_defs.ListAvailableManagedRuleGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    NextMarker = field("NextMarker")

    @cached_property
    def ManagedRuleGroups(self):  # pragma: no cover
        return ManagedRuleGroupSummary.make_many(
            self.boto3_raw_data["ManagedRuleGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableManagedRuleGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableManagedRuleGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedRuleSetsResponse:
    boto3_raw_data: "type_defs.ListManagedRuleSetsResponseTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")

    @cached_property
    def ManagedRuleSets(self):  # pragma: no cover
        return ManagedRuleSetSummary.make_many(self.boto3_raw_data["ManagedRuleSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedRuleSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedRuleSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMobileSdkReleasesResponse:
    boto3_raw_data: "type_defs.ListMobileSdkReleasesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReleaseSummaries(self):  # pragma: no cover
        return ReleaseSummary.make_many(self.boto3_raw_data["ReleaseSummaries"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMobileSdkReleasesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMobileSdkReleasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestInspection:
    boto3_raw_data: "type_defs.RequestInspectionTypeDef" = dataclasses.field()

    PayloadType = field("PayloadType")

    @cached_property
    def UsernameField(self):  # pragma: no cover
        return UsernameField.make_one(self.boto3_raw_data["UsernameField"])

    @cached_property
    def PasswordField(self):  # pragma: no cover
        return PasswordField.make_one(self.boto3_raw_data["PasswordField"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequestInspectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestInspectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleSet:
    boto3_raw_data: "type_defs.ManagedRuleSetTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    ARN = field("ARN")
    Description = field("Description")
    PublishedVersions = field("PublishedVersions")
    RecommendedVersion = field("RecommendedVersion")
    LabelNamespace = field("LabelNamespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManagedRuleSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestInspectionACFPOutput:
    boto3_raw_data: "type_defs.RequestInspectionACFPOutputTypeDef" = dataclasses.field()

    PayloadType = field("PayloadType")

    @cached_property
    def UsernameField(self):  # pragma: no cover
        return UsernameField.make_one(self.boto3_raw_data["UsernameField"])

    @cached_property
    def PasswordField(self):  # pragma: no cover
        return PasswordField.make_one(self.boto3_raw_data["PasswordField"])

    @cached_property
    def EmailField(self):  # pragma: no cover
        return EmailField.make_one(self.boto3_raw_data["EmailField"])

    @cached_property
    def PhoneNumberFields(self):  # pragma: no cover
        return PhoneNumberField.make_many(self.boto3_raw_data["PhoneNumberFields"])

    @cached_property
    def AddressFields(self):  # pragma: no cover
        return AddressField.make_many(self.boto3_raw_data["AddressFields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestInspectionACFPOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestInspectionACFPOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestInspectionACFP:
    boto3_raw_data: "type_defs.RequestInspectionACFPTypeDef" = dataclasses.field()

    PayloadType = field("PayloadType")

    @cached_property
    def UsernameField(self):  # pragma: no cover
        return UsernameField.make_one(self.boto3_raw_data["UsernameField"])

    @cached_property
    def PasswordField(self):  # pragma: no cover
        return PasswordField.make_one(self.boto3_raw_data["PasswordField"])

    @cached_property
    def EmailField(self):  # pragma: no cover
        return EmailField.make_one(self.boto3_raw_data["EmailField"])

    @cached_property
    def PhoneNumberFields(self):  # pragma: no cover
        return PhoneNumberField.make_many(self.boto3_raw_data["PhoneNumberFields"])

    @cached_property
    def AddressFields(self):  # pragma: no cover
        return AddressField.make_many(self.boto3_raw_data["AddressFields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestInspectionACFPTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestInspectionACFPTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutManagedRuleSetVersionsRequest:
    boto3_raw_data: "type_defs.PutManagedRuleSetVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    LockToken = field("LockToken")
    RecommendedVersion = field("RecommendedVersion")
    VersionsToPublish = field("VersionsToPublish")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutManagedRuleSetVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutManagedRuleSetVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspectionOutput:
    boto3_raw_data: "type_defs.ResponseInspectionOutputTypeDef" = dataclasses.field()

    @cached_property
    def StatusCode(self):  # pragma: no cover
        return ResponseInspectionStatusCodeOutput.make_one(
            self.boto3_raw_data["StatusCode"]
        )

    @cached_property
    def Header(self):  # pragma: no cover
        return ResponseInspectionHeaderOutput.make_one(self.boto3_raw_data["Header"])

    @cached_property
    def BodyContains(self):  # pragma: no cover
        return ResponseInspectionBodyContainsOutput.make_one(
            self.boto3_raw_data["BodyContains"]
        )

    @cached_property
    def Json(self):  # pragma: no cover
        return ResponseInspectionJsonOutput.make_one(self.boto3_raw_data["Json"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseInspectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeWindow:
    boto3_raw_data: "type_defs.TimeWindowTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeWindowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateManagedRuleSetVersionExpiryDateRequest:
    boto3_raw_data: "type_defs.UpdateManagedRuleSetVersionExpiryDateRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    LockToken = field("LockToken")
    VersionToExpire = field("VersionToExpire")
    ExpiryTimestamp = field("ExpiryTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateManagedRuleSetVersionExpiryDateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateManagedRuleSetVersionExpiryDateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateBasedStatementCustomKeyOutput:
    boto3_raw_data: "type_defs.RateBasedStatementCustomKeyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Header(self):  # pragma: no cover
        return RateLimitHeaderOutput.make_one(self.boto3_raw_data["Header"])

    @cached_property
    def Cookie(self):  # pragma: no cover
        return RateLimitCookieOutput.make_one(self.boto3_raw_data["Cookie"])

    @cached_property
    def QueryArgument(self):  # pragma: no cover
        return RateLimitQueryArgumentOutput.make_one(
            self.boto3_raw_data["QueryArgument"]
        )

    @cached_property
    def QueryString(self):  # pragma: no cover
        return RateLimitQueryStringOutput.make_one(self.boto3_raw_data["QueryString"])

    HTTPMethod = field("HTTPMethod")
    ForwardedIP = field("ForwardedIP")
    IP = field("IP")

    @cached_property
    def LabelNamespace(self):  # pragma: no cover
        return RateLimitLabelNamespace.make_one(self.boto3_raw_data["LabelNamespace"])

    @cached_property
    def UriPath(self):  # pragma: no cover
        return RateLimitUriPathOutput.make_one(self.boto3_raw_data["UriPath"])

    @cached_property
    def JA3Fingerprint(self):  # pragma: no cover
        return RateLimitJA3Fingerprint.make_one(self.boto3_raw_data["JA3Fingerprint"])

    @cached_property
    def JA4Fingerprint(self):  # pragma: no cover
        return RateLimitJA4Fingerprint.make_one(self.boto3_raw_data["JA4Fingerprint"])

    ASN = field("ASN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RateBasedStatementCustomKeyOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateBasedStatementCustomKeyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientSideActionConfigOutput:
    boto3_raw_data: "type_defs.ClientSideActionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Challenge(self):  # pragma: no cover
        return ClientSideActionOutput.make_one(self.boto3_raw_data["Challenge"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientSideActionConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientSideActionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRegexPatternSetResponse:
    boto3_raw_data: "type_defs.GetRegexPatternSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def RegexPatternSet(self):  # pragma: no cover
        return RegexPatternSet.make_one(self.boto3_raw_data["RegexPatternSet"])

    LockToken = field("LockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRegexPatternSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRegexPatternSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterOutput:
    boto3_raw_data: "type_defs.FilterOutputTypeDef" = dataclasses.field()

    Behavior = field("Behavior")
    Requirement = field("Requirement")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["Conditions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Behavior = field("Behavior")
    Requirement = field("Requirement")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["Conditions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cookies:
    boto3_raw_data: "type_defs.CookiesTypeDef" = dataclasses.field()

    MatchPattern = field("MatchPattern")
    MatchScope = field("MatchScope")
    OversizeHandling = field("OversizeHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CookiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CookiesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMobileSdkReleaseResponse:
    boto3_raw_data: "type_defs.GetMobileSdkReleaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def MobileSdkRelease(self):  # pragma: no cover
        return MobileSdkRelease.make_one(self.boto3_raw_data["MobileSdkRelease"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMobileSdkReleaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMobileSdkReleaseResponseTypeDef"]
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

    NextMarker = field("NextMarker")

    @cached_property
    def TagInfoForResource(self):  # pragma: no cover
        return TagInfoForResource.make_one(self.boto3_raw_data["TagInfoForResource"])

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
class AllowActionOutput:
    boto3_raw_data: "type_defs.AllowActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def CustomRequestHandling(self):  # pragma: no cover
        return CustomRequestHandlingOutput.make_one(
            self.boto3_raw_data["CustomRequestHandling"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptchaActionOutput:
    boto3_raw_data: "type_defs.CaptchaActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def CustomRequestHandling(self):  # pragma: no cover
        return CustomRequestHandlingOutput.make_one(
            self.boto3_raw_data["CustomRequestHandling"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaptchaActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaptchaActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChallengeActionOutput:
    boto3_raw_data: "type_defs.ChallengeActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def CustomRequestHandling(self):  # pragma: no cover
        return CustomRequestHandlingOutput.make_one(
            self.boto3_raw_data["CustomRequestHandling"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChallengeActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChallengeActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountActionOutput:
    boto3_raw_data: "type_defs.CountActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def CustomRequestHandling(self):  # pragma: no cover
        return CustomRequestHandlingOutput.make_one(
            self.boto3_raw_data["CustomRequestHandling"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CountActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CountActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockActionOutput:
    boto3_raw_data: "type_defs.BlockActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def CustomResponse(self):  # pragma: no cover
        return CustomResponseOutput.make_one(self.boto3_raw_data["CustomResponse"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProtectionConfigOutput:
    boto3_raw_data: "type_defs.DataProtectionConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def DataProtections(self):  # pragma: no cover
        return DataProtectionOutput.make_many(self.boto3_raw_data["DataProtections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProtectionConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProtectionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProtectionConfig:
    boto3_raw_data: "type_defs.DataProtectionConfigTypeDef" = dataclasses.field()

    @cached_property
    def DataProtections(self):  # pragma: no cover
        return DataProtection.make_many(self.boto3_raw_data["DataProtections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProtectionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProtectionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampledHTTPRequest:
    boto3_raw_data: "type_defs.SampledHTTPRequestTypeDef" = dataclasses.field()

    @cached_property
    def Request(self):  # pragma: no cover
        return HTTPRequest.make_one(self.boto3_raw_data["Request"])

    Weight = field("Weight")
    Timestamp = field("Timestamp")
    Action = field("Action")
    RuleNameWithinRuleGroup = field("RuleNameWithinRuleGroup")

    @cached_property
    def RequestHeadersInserted(self):  # pragma: no cover
        return HTTPHeader.make_many(self.boto3_raw_data["RequestHeadersInserted"])

    ResponseCodeSent = field("ResponseCodeSent")

    @cached_property
    def Labels(self):  # pragma: no cover
        return Label.make_many(self.boto3_raw_data["Labels"])

    @cached_property
    def CaptchaResponse(self):  # pragma: no cover
        return CaptchaResponse.make_one(self.boto3_raw_data["CaptchaResponse"])

    @cached_property
    def ChallengeResponse(self):  # pragma: no cover
        return ChallengeResponse.make_one(self.boto3_raw_data["ChallengeResponse"])

    OverriddenAction = field("OverriddenAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SampledHTTPRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SampledHTTPRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Headers:
    boto3_raw_data: "type_defs.HeadersTypeDef" = dataclasses.field()

    MatchPattern = field("MatchPattern")
    MatchScope = field("MatchScope")
    OversizeHandling = field("OversizeHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeadersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeadersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldToMatchOutput:
    boto3_raw_data: "type_defs.FieldToMatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def SingleHeader(self):  # pragma: no cover
        return SingleHeader.make_one(self.boto3_raw_data["SingleHeader"])

    @cached_property
    def SingleQueryArgument(self):  # pragma: no cover
        return SingleQueryArgument.make_one(self.boto3_raw_data["SingleQueryArgument"])

    AllQueryArguments = field("AllQueryArguments")
    UriPath = field("UriPath")
    QueryString = field("QueryString")

    @cached_property
    def Body(self):  # pragma: no cover
        return Body.make_one(self.boto3_raw_data["Body"])

    Method = field("Method")

    @cached_property
    def JsonBody(self):  # pragma: no cover
        return JsonBodyOutput.make_one(self.boto3_raw_data["JsonBody"])

    @cached_property
    def Headers(self):  # pragma: no cover
        return HeadersOutput.make_one(self.boto3_raw_data["Headers"])

    @cached_property
    def Cookies(self):  # pragma: no cover
        return CookiesOutput.make_one(self.boto3_raw_data["Cookies"])

    @cached_property
    def HeaderOrder(self):  # pragma: no cover
        return HeaderOrder.make_one(self.boto3_raw_data["HeaderOrder"])

    @cached_property
    def JA3Fingerprint(self):  # pragma: no cover
        return JA3Fingerprint.make_one(self.boto3_raw_data["JA3Fingerprint"])

    @cached_property
    def JA4Fingerprint(self):  # pragma: no cover
        return JA4Fingerprint.make_one(self.boto3_raw_data["JA4Fingerprint"])

    @cached_property
    def UriFragment(self):  # pragma: no cover
        return UriFragment.make_one(self.boto3_raw_data["UriFragment"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldToMatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldToMatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JsonBody:
    boto3_raw_data: "type_defs.JsonBodyTypeDef" = dataclasses.field()

    MatchPattern = field("MatchPattern")
    MatchScope = field("MatchScope")
    InvalidFallbackBehavior = field("InvalidFallbackBehavior")
    OversizeHandling = field("OversizeHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JsonBodyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JsonBodyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedRuleSetResponse:
    boto3_raw_data: "type_defs.GetManagedRuleSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def ManagedRuleSet(self):  # pragma: no cover
        return ManagedRuleSet.make_one(self.boto3_raw_data["ManagedRuleSet"])

    LockToken = field("LockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetManagedRuleSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedRuleSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AWSManagedRulesACFPRuleSetOutput:
    boto3_raw_data: "type_defs.AWSManagedRulesACFPRuleSetOutputTypeDef" = (
        dataclasses.field()
    )

    CreationPath = field("CreationPath")
    RegistrationPagePath = field("RegistrationPagePath")

    @cached_property
    def RequestInspection(self):  # pragma: no cover
        return RequestInspectionACFPOutput.make_one(
            self.boto3_raw_data["RequestInspection"]
        )

    @cached_property
    def ResponseInspection(self):  # pragma: no cover
        return ResponseInspectionOutput.make_one(
            self.boto3_raw_data["ResponseInspection"]
        )

    EnableRegexInPath = field("EnableRegexInPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AWSManagedRulesACFPRuleSetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AWSManagedRulesACFPRuleSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AWSManagedRulesATPRuleSetOutput:
    boto3_raw_data: "type_defs.AWSManagedRulesATPRuleSetOutputTypeDef" = (
        dataclasses.field()
    )

    LoginPath = field("LoginPath")

    @cached_property
    def RequestInspection(self):  # pragma: no cover
        return RequestInspection.make_one(self.boto3_raw_data["RequestInspection"])

    @cached_property
    def ResponseInspection(self):  # pragma: no cover
        return ResponseInspectionOutput.make_one(
            self.boto3_raw_data["ResponseInspection"]
        )

    EnableRegexInPath = field("EnableRegexInPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AWSManagedRulesATPRuleSetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AWSManagedRulesATPRuleSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseInspection:
    boto3_raw_data: "type_defs.ResponseInspectionTypeDef" = dataclasses.field()

    StatusCode = field("StatusCode")
    Header = field("Header")
    BodyContains = field("BodyContains")
    Json = field("Json")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseInspectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseInspectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateBasedStatementOutput:
    boto3_raw_data: "type_defs.RateBasedStatementOutputTypeDef" = dataclasses.field()

    Limit = field("Limit")
    AggregateKeyType = field("AggregateKeyType")
    EvaluationWindowSec = field("EvaluationWindowSec")
    ScopeDownStatement = field("ScopeDownStatement")

    @cached_property
    def ForwardedIPConfig(self):  # pragma: no cover
        return ForwardedIPConfig.make_one(self.boto3_raw_data["ForwardedIPConfig"])

    @cached_property
    def CustomKeys(self):  # pragma: no cover
        return RateBasedStatementCustomKeyOutput.make_many(
            self.boto3_raw_data["CustomKeys"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateBasedStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateBasedStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateBasedStatementCustomKey:
    boto3_raw_data: "type_defs.RateBasedStatementCustomKeyTypeDef" = dataclasses.field()

    Header = field("Header")
    Cookie = field("Cookie")
    QueryArgument = field("QueryArgument")
    QueryString = field("QueryString")
    HTTPMethod = field("HTTPMethod")
    ForwardedIP = field("ForwardedIP")
    IP = field("IP")

    @cached_property
    def LabelNamespace(self):  # pragma: no cover
        return RateLimitLabelNamespace.make_one(self.boto3_raw_data["LabelNamespace"])

    UriPath = field("UriPath")

    @cached_property
    def JA3Fingerprint(self):  # pragma: no cover
        return RateLimitJA3Fingerprint.make_one(self.boto3_raw_data["JA3Fingerprint"])

    @cached_property
    def JA4Fingerprint(self):  # pragma: no cover
        return RateLimitJA4Fingerprint.make_one(self.boto3_raw_data["JA4Fingerprint"])

    ASN = field("ASN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateBasedStatementCustomKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateBasedStatementCustomKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AWSManagedRulesAntiDDoSRuleSetOutput:
    boto3_raw_data: "type_defs.AWSManagedRulesAntiDDoSRuleSetOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClientSideActionConfig(self):  # pragma: no cover
        return ClientSideActionConfigOutput.make_one(
            self.boto3_raw_data["ClientSideActionConfig"]
        )

    SensitivityToBlock = field("SensitivityToBlock")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AWSManagedRulesAntiDDoSRuleSetOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AWSManagedRulesAntiDDoSRuleSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientSideActionConfig:
    boto3_raw_data: "type_defs.ClientSideActionConfigTypeDef" = dataclasses.field()

    Challenge = field("Challenge")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientSideActionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientSideActionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingFilterOutput:
    boto3_raw_data: "type_defs.LoggingFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return FilterOutput.make_many(self.boto3_raw_data["Filters"])

    DefaultBehavior = field("DefaultBehavior")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingFilter:
    boto3_raw_data: "type_defs.LoggingFilterTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    DefaultBehavior = field("DefaultBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverrideActionOutput:
    boto3_raw_data: "type_defs.OverrideActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Count(self):  # pragma: no cover
        return CountActionOutput.make_one(self.boto3_raw_data["Count"])

    None_ = field("None")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OverrideActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverrideActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowAction:
    boto3_raw_data: "type_defs.AllowActionTypeDef" = dataclasses.field()

    CustomRequestHandling = field("CustomRequestHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AllowActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptchaAction:
    boto3_raw_data: "type_defs.CaptchaActionTypeDef" = dataclasses.field()

    CustomRequestHandling = field("CustomRequestHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaptchaActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaptchaActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChallengeAction:
    boto3_raw_data: "type_defs.ChallengeActionTypeDef" = dataclasses.field()

    CustomRequestHandling = field("CustomRequestHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChallengeActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChallengeActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountAction:
    boto3_raw_data: "type_defs.CountActionTypeDef" = dataclasses.field()

    CustomRequestHandling = field("CustomRequestHandling")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CountActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CountActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultActionOutput:
    boto3_raw_data: "type_defs.DefaultActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Block(self):  # pragma: no cover
        return BlockActionOutput.make_one(self.boto3_raw_data["Block"])

    @cached_property
    def Allow(self):  # pragma: no cover
        return AllowActionOutput.make_one(self.boto3_raw_data["Allow"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleActionOutput:
    boto3_raw_data: "type_defs.RuleActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Block(self):  # pragma: no cover
        return BlockActionOutput.make_one(self.boto3_raw_data["Block"])

    @cached_property
    def Allow(self):  # pragma: no cover
        return AllowActionOutput.make_one(self.boto3_raw_data["Allow"])

    @cached_property
    def Count(self):  # pragma: no cover
        return CountActionOutput.make_one(self.boto3_raw_data["Count"])

    @cached_property
    def Captcha(self):  # pragma: no cover
        return CaptchaActionOutput.make_one(self.boto3_raw_data["Captcha"])

    @cached_property
    def Challenge(self):  # pragma: no cover
        return ChallengeActionOutput.make_one(self.boto3_raw_data["Challenge"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockAction:
    boto3_raw_data: "type_defs.BlockActionTypeDef" = dataclasses.field()

    CustomResponse = field("CustomResponse")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlockActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSampledRequestsResponse:
    boto3_raw_data: "type_defs.GetSampledRequestsResponseTypeDef" = dataclasses.field()

    @cached_property
    def SampledRequests(self):  # pragma: no cover
        return SampledHTTPRequest.make_many(self.boto3_raw_data["SampledRequests"])

    PopulationSize = field("PopulationSize")

    @cached_property
    def TimeWindow(self):  # pragma: no cover
        return TimeWindowOutput.make_one(self.boto3_raw_data["TimeWindow"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSampledRequestsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSampledRequestsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ByteMatchStatementOutput:
    boto3_raw_data: "type_defs.ByteMatchStatementOutputTypeDef" = dataclasses.field()

    SearchString = field("SearchString")

    @cached_property
    def FieldToMatch(self):  # pragma: no cover
        return FieldToMatchOutput.make_one(self.boto3_raw_data["FieldToMatch"])

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    PositionalConstraint = field("PositionalConstraint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ByteMatchStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ByteMatchStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegexMatchStatementOutput:
    boto3_raw_data: "type_defs.RegexMatchStatementOutputTypeDef" = dataclasses.field()

    RegexString = field("RegexString")

    @cached_property
    def FieldToMatch(self):  # pragma: no cover
        return FieldToMatchOutput.make_one(self.boto3_raw_data["FieldToMatch"])

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegexMatchStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegexMatchStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegexPatternSetReferenceStatementOutput:
    boto3_raw_data: "type_defs.RegexPatternSetReferenceStatementOutputTypeDef" = (
        dataclasses.field()
    )

    ARN = field("ARN")

    @cached_property
    def FieldToMatch(self):  # pragma: no cover
        return FieldToMatchOutput.make_one(self.boto3_raw_data["FieldToMatch"])

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegexPatternSetReferenceStatementOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegexPatternSetReferenceStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SizeConstraintStatementOutput:
    boto3_raw_data: "type_defs.SizeConstraintStatementOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldToMatch(self):  # pragma: no cover
        return FieldToMatchOutput.make_one(self.boto3_raw_data["FieldToMatch"])

    ComparisonOperator = field("ComparisonOperator")
    Size = field("Size")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SizeConstraintStatementOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SizeConstraintStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqliMatchStatementOutput:
    boto3_raw_data: "type_defs.SqliMatchStatementOutputTypeDef" = dataclasses.field()

    @cached_property
    def FieldToMatch(self):  # pragma: no cover
        return FieldToMatchOutput.make_one(self.boto3_raw_data["FieldToMatch"])

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    SensitivityLevel = field("SensitivityLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SqliMatchStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqliMatchStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class XssMatchStatementOutput:
    boto3_raw_data: "type_defs.XssMatchStatementOutputTypeDef" = dataclasses.field()

    @cached_property
    def FieldToMatch(self):  # pragma: no cover
        return FieldToMatchOutput.make_one(self.boto3_raw_data["FieldToMatch"])

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.XssMatchStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.XssMatchStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSampledRequestsRequest:
    boto3_raw_data: "type_defs.GetSampledRequestsRequestTypeDef" = dataclasses.field()

    WebAclArn = field("WebAclArn")
    RuleMetricName = field("RuleMetricName")
    Scope = field("Scope")
    TimeWindow = field("TimeWindow")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSampledRequestsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSampledRequestsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleGroupConfigOutput:
    boto3_raw_data: "type_defs.ManagedRuleGroupConfigOutputTypeDef" = (
        dataclasses.field()
    )

    LoginPath = field("LoginPath")
    PayloadType = field("PayloadType")

    @cached_property
    def UsernameField(self):  # pragma: no cover
        return UsernameField.make_one(self.boto3_raw_data["UsernameField"])

    @cached_property
    def PasswordField(self):  # pragma: no cover
        return PasswordField.make_one(self.boto3_raw_data["PasswordField"])

    @cached_property
    def AWSManagedRulesBotControlRuleSet(self):  # pragma: no cover
        return AWSManagedRulesBotControlRuleSet.make_one(
            self.boto3_raw_data["AWSManagedRulesBotControlRuleSet"]
        )

    @cached_property
    def AWSManagedRulesATPRuleSet(self):  # pragma: no cover
        return AWSManagedRulesATPRuleSetOutput.make_one(
            self.boto3_raw_data["AWSManagedRulesATPRuleSet"]
        )

    @cached_property
    def AWSManagedRulesACFPRuleSet(self):  # pragma: no cover
        return AWSManagedRulesACFPRuleSetOutput.make_one(
            self.boto3_raw_data["AWSManagedRulesACFPRuleSet"]
        )

    @cached_property
    def AWSManagedRulesAntiDDoSRuleSet(self):  # pragma: no cover
        return AWSManagedRulesAntiDDoSRuleSetOutput.make_one(
            self.boto3_raw_data["AWSManagedRulesAntiDDoSRuleSet"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleGroupConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleGroupConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfigurationOutput:
    boto3_raw_data: "type_defs.LoggingConfigurationOutputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    LogDestinationConfigs = field("LogDestinationConfigs")

    @cached_property
    def RedactedFields(self):  # pragma: no cover
        return FieldToMatchOutput.make_many(self.boto3_raw_data["RedactedFields"])

    ManagedByFirewallManager = field("ManagedByFirewallManager")

    @cached_property
    def LoggingFilter(self):  # pragma: no cover
        return LoggingFilterOutput.make_one(self.boto3_raw_data["LoggingFilter"])

    LogType = field("LogType")
    LogScope = field("LogScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleActionOverrideOutput:
    boto3_raw_data: "type_defs.RuleActionOverrideOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ActionToUse(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["ActionToUse"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleActionOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleActionOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleSummary:
    boto3_raw_data: "type_defs.RuleSummaryTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Action(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["Action"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultAction:
    boto3_raw_data: "type_defs.DefaultActionTypeDef" = dataclasses.field()

    @cached_property
    def Block(self):  # pragma: no cover
        return BlockAction.make_one(self.boto3_raw_data["Block"])

    @cached_property
    def Allow(self):  # pragma: no cover
        return AllowAction.make_one(self.boto3_raw_data["Allow"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefaultActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DefaultActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldToMatch:
    boto3_raw_data: "type_defs.FieldToMatchTypeDef" = dataclasses.field()

    @cached_property
    def SingleHeader(self):  # pragma: no cover
        return SingleHeader.make_one(self.boto3_raw_data["SingleHeader"])

    @cached_property
    def SingleQueryArgument(self):  # pragma: no cover
        return SingleQueryArgument.make_one(self.boto3_raw_data["SingleQueryArgument"])

    AllQueryArguments = field("AllQueryArguments")
    UriPath = field("UriPath")
    QueryString = field("QueryString")

    @cached_property
    def Body(self):  # pragma: no cover
        return Body.make_one(self.boto3_raw_data["Body"])

    Method = field("Method")
    JsonBody = field("JsonBody")
    Headers = field("Headers")
    Cookies = field("Cookies")

    @cached_property
    def HeaderOrder(self):  # pragma: no cover
        return HeaderOrder.make_one(self.boto3_raw_data["HeaderOrder"])

    @cached_property
    def JA3Fingerprint(self):  # pragma: no cover
        return JA3Fingerprint.make_one(self.boto3_raw_data["JA3Fingerprint"])

    @cached_property
    def JA4Fingerprint(self):  # pragma: no cover
        return JA4Fingerprint.make_one(self.boto3_raw_data["JA4Fingerprint"])

    @cached_property
    def UriFragment(self):  # pragma: no cover
        return UriFragment.make_one(self.boto3_raw_data["UriFragment"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldToMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldToMatchTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AWSManagedRulesACFPRuleSet:
    boto3_raw_data: "type_defs.AWSManagedRulesACFPRuleSetTypeDef" = dataclasses.field()

    CreationPath = field("CreationPath")
    RegistrationPagePath = field("RegistrationPagePath")
    RequestInspection = field("RequestInspection")
    ResponseInspection = field("ResponseInspection")
    EnableRegexInPath = field("EnableRegexInPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AWSManagedRulesACFPRuleSetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AWSManagedRulesACFPRuleSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AWSManagedRulesATPRuleSet:
    boto3_raw_data: "type_defs.AWSManagedRulesATPRuleSetTypeDef" = dataclasses.field()

    LoginPath = field("LoginPath")

    @cached_property
    def RequestInspection(self):  # pragma: no cover
        return RequestInspection.make_one(self.boto3_raw_data["RequestInspection"])

    ResponseInspection = field("ResponseInspection")
    EnableRegexInPath = field("EnableRegexInPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AWSManagedRulesATPRuleSetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AWSManagedRulesATPRuleSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateBasedStatement:
    boto3_raw_data: "type_defs.RateBasedStatementTypeDef" = dataclasses.field()

    Limit = field("Limit")
    AggregateKeyType = field("AggregateKeyType")
    EvaluationWindowSec = field("EvaluationWindowSec")
    ScopeDownStatement = field("ScopeDownStatement")

    @cached_property
    def ForwardedIPConfig(self):  # pragma: no cover
        return ForwardedIPConfig.make_one(self.boto3_raw_data["ForwardedIPConfig"])

    CustomKeys = field("CustomKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateBasedStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateBasedStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AWSManagedRulesAntiDDoSRuleSet:
    boto3_raw_data: "type_defs.AWSManagedRulesAntiDDoSRuleSetTypeDef" = (
        dataclasses.field()
    )

    ClientSideActionConfig = field("ClientSideActionConfig")
    SensitivityToBlock = field("SensitivityToBlock")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AWSManagedRulesAntiDDoSRuleSetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AWSManagedRulesAntiDDoSRuleSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoggingConfigurationResponse:
    boto3_raw_data: "type_defs.GetLoggingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfigurationOutput.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLoggingConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoggingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoggingConfigurationsResponse:
    boto3_raw_data: "type_defs.ListLoggingConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoggingConfigurations(self):  # pragma: no cover
        return LoggingConfigurationOutput.make_many(
            self.boto3_raw_data["LoggingConfigurations"]
        )

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLoggingConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoggingConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLoggingConfigurationResponse:
    boto3_raw_data: "type_defs.PutLoggingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfigurationOutput.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutLoggingConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLoggingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverrideAction:
    boto3_raw_data: "type_defs.OverrideActionTypeDef" = dataclasses.field()

    Count = field("Count")
    None_ = field("None")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OverrideActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OverrideActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleGroupStatementOutput:
    boto3_raw_data: "type_defs.ManagedRuleGroupStatementOutputTypeDef" = (
        dataclasses.field()
    )

    VendorName = field("VendorName")
    Name = field("Name")
    Version = field("Version")

    @cached_property
    def ExcludedRules(self):  # pragma: no cover
        return ExcludedRule.make_many(self.boto3_raw_data["ExcludedRules"])

    ScopeDownStatement = field("ScopeDownStatement")

    @cached_property
    def ManagedRuleGroupConfigs(self):  # pragma: no cover
        return ManagedRuleGroupConfigOutput.make_many(
            self.boto3_raw_data["ManagedRuleGroupConfigs"]
        )

    @cached_property
    def RuleActionOverrides(self):  # pragma: no cover
        return RuleActionOverrideOutput.make_many(
            self.boto3_raw_data["RuleActionOverrides"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ManagedRuleGroupStatementOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleGroupStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleGroupReferenceStatementOutput:
    boto3_raw_data: "type_defs.RuleGroupReferenceStatementOutputTypeDef" = (
        dataclasses.field()
    )

    ARN = field("ARN")

    @cached_property
    def ExcludedRules(self):  # pragma: no cover
        return ExcludedRule.make_many(self.boto3_raw_data["ExcludedRules"])

    @cached_property
    def RuleActionOverrides(self):  # pragma: no cover
        return RuleActionOverrideOutput.make_many(
            self.boto3_raw_data["RuleActionOverrides"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RuleGroupReferenceStatementOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleGroupReferenceStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedRuleGroupResponse:
    boto3_raw_data: "type_defs.DescribeManagedRuleGroupResponseTypeDef" = (
        dataclasses.field()
    )

    VersionName = field("VersionName")
    SnsTopicArn = field("SnsTopicArn")
    Capacity = field("Capacity")

    @cached_property
    def Rules(self):  # pragma: no cover
        return RuleSummary.make_many(self.boto3_raw_data["Rules"])

    LabelNamespace = field("LabelNamespace")

    @cached_property
    def AvailableLabels(self):  # pragma: no cover
        return LabelSummary.make_many(self.boto3_raw_data["AvailableLabels"])

    @cached_property
    def ConsumedLabels(self):  # pragma: no cover
        return LabelSummary.make_many(self.boto3_raw_data["ConsumedLabels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeManagedRuleGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleAction:
    boto3_raw_data: "type_defs.RuleActionTypeDef" = dataclasses.field()

    Block = field("Block")
    Allow = field("Allow")
    Count = field("Count")
    Captcha = field("Captcha")
    Challenge = field("Challenge")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfiguration:
    boto3_raw_data: "type_defs.LoggingConfigurationTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    LogDestinationConfigs = field("LogDestinationConfigs")

    @cached_property
    def RedactedFields(self):  # pragma: no cover
        return FieldToMatch.make_many(self.boto3_raw_data["RedactedFields"])

    ManagedByFirewallManager = field("ManagedByFirewallManager")

    @cached_property
    def LoggingFilter(self):  # pragma: no cover
        return LoggingFilter.make_one(self.boto3_raw_data["LoggingFilter"])

    LogType = field("LogType")
    LogScope = field("LogScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallManagerStatement:
    boto3_raw_data: "type_defs.FirewallManagerStatementTypeDef" = dataclasses.field()

    @cached_property
    def ManagedRuleGroupStatement(self):  # pragma: no cover
        return ManagedRuleGroupStatementOutput.make_one(
            self.boto3_raw_data["ManagedRuleGroupStatement"]
        )

    @cached_property
    def RuleGroupReferenceStatement(self):  # pragma: no cover
        return RuleGroupReferenceStatementOutput.make_one(
            self.boto3_raw_data["RuleGroupReferenceStatement"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirewallManagerStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallManagerStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatementOutput:
    boto3_raw_data: "type_defs.StatementOutputTypeDef" = dataclasses.field()

    @cached_property
    def ByteMatchStatement(self):  # pragma: no cover
        return ByteMatchStatementOutput.make_one(
            self.boto3_raw_data["ByteMatchStatement"]
        )

    @cached_property
    def SqliMatchStatement(self):  # pragma: no cover
        return SqliMatchStatementOutput.make_one(
            self.boto3_raw_data["SqliMatchStatement"]
        )

    @cached_property
    def XssMatchStatement(self):  # pragma: no cover
        return XssMatchStatementOutput.make_one(
            self.boto3_raw_data["XssMatchStatement"]
        )

    @cached_property
    def SizeConstraintStatement(self):  # pragma: no cover
        return SizeConstraintStatementOutput.make_one(
            self.boto3_raw_data["SizeConstraintStatement"]
        )

    @cached_property
    def GeoMatchStatement(self):  # pragma: no cover
        return GeoMatchStatementOutput.make_one(
            self.boto3_raw_data["GeoMatchStatement"]
        )

    @cached_property
    def RuleGroupReferenceStatement(self):  # pragma: no cover
        return RuleGroupReferenceStatementOutput.make_one(
            self.boto3_raw_data["RuleGroupReferenceStatement"]
        )

    @cached_property
    def IPSetReferenceStatement(self):  # pragma: no cover
        return IPSetReferenceStatement.make_one(
            self.boto3_raw_data["IPSetReferenceStatement"]
        )

    @cached_property
    def RegexPatternSetReferenceStatement(self):  # pragma: no cover
        return RegexPatternSetReferenceStatementOutput.make_one(
            self.boto3_raw_data["RegexPatternSetReferenceStatement"]
        )

    @cached_property
    def RateBasedStatement(self):  # pragma: no cover
        return RateBasedStatementOutput.make_one(
            self.boto3_raw_data["RateBasedStatement"]
        )

    @cached_property
    def AndStatement(self):  # pragma: no cover
        return AndStatementOutput.make_one(self.boto3_raw_data["AndStatement"])

    @cached_property
    def OrStatement(self):  # pragma: no cover
        return OrStatementOutput.make_one(self.boto3_raw_data["OrStatement"])

    @cached_property
    def NotStatement(self):  # pragma: no cover
        return NotStatementOutput.make_one(self.boto3_raw_data["NotStatement"])

    @cached_property
    def ManagedRuleGroupStatement(self):  # pragma: no cover
        return ManagedRuleGroupStatementOutput.make_one(
            self.boto3_raw_data["ManagedRuleGroupStatement"]
        )

    @cached_property
    def LabelMatchStatement(self):  # pragma: no cover
        return LabelMatchStatement.make_one(self.boto3_raw_data["LabelMatchStatement"])

    @cached_property
    def RegexMatchStatement(self):  # pragma: no cover
        return RegexMatchStatementOutput.make_one(
            self.boto3_raw_data["RegexMatchStatement"]
        )

    @cached_property
    def AsnMatchStatement(self):  # pragma: no cover
        return AsnMatchStatementOutput.make_one(
            self.boto3_raw_data["AsnMatchStatement"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatementOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatementOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ByteMatchStatement:
    boto3_raw_data: "type_defs.ByteMatchStatementTypeDef" = dataclasses.field()

    SearchString = field("SearchString")
    FieldToMatch = field("FieldToMatch")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    PositionalConstraint = field("PositionalConstraint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ByteMatchStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ByteMatchStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegexMatchStatement:
    boto3_raw_data: "type_defs.RegexMatchStatementTypeDef" = dataclasses.field()

    RegexString = field("RegexString")
    FieldToMatch = field("FieldToMatch")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegexMatchStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegexMatchStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegexPatternSetReferenceStatement:
    boto3_raw_data: "type_defs.RegexPatternSetReferenceStatementTypeDef" = (
        dataclasses.field()
    )

    ARN = field("ARN")
    FieldToMatch = field("FieldToMatch")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegexPatternSetReferenceStatementTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegexPatternSetReferenceStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SizeConstraintStatement:
    boto3_raw_data: "type_defs.SizeConstraintStatementTypeDef" = dataclasses.field()

    FieldToMatch = field("FieldToMatch")
    ComparisonOperator = field("ComparisonOperator")
    Size = field("Size")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SizeConstraintStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SizeConstraintStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqliMatchStatement:
    boto3_raw_data: "type_defs.SqliMatchStatementTypeDef" = dataclasses.field()

    FieldToMatch = field("FieldToMatch")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    SensitivityLevel = field("SensitivityLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SqliMatchStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqliMatchStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class XssMatchStatement:
    boto3_raw_data: "type_defs.XssMatchStatementTypeDef" = dataclasses.field()

    FieldToMatch = field("FieldToMatch")

    @cached_property
    def TextTransformations(self):  # pragma: no cover
        return TextTransformation.make_many(self.boto3_raw_data["TextTransformations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.XssMatchStatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.XssMatchStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleGroupConfig:
    boto3_raw_data: "type_defs.ManagedRuleGroupConfigTypeDef" = dataclasses.field()

    LoginPath = field("LoginPath")
    PayloadType = field("PayloadType")

    @cached_property
    def UsernameField(self):  # pragma: no cover
        return UsernameField.make_one(self.boto3_raw_data["UsernameField"])

    @cached_property
    def PasswordField(self):  # pragma: no cover
        return PasswordField.make_one(self.boto3_raw_data["PasswordField"])

    @cached_property
    def AWSManagedRulesBotControlRuleSet(self):  # pragma: no cover
        return AWSManagedRulesBotControlRuleSet.make_one(
            self.boto3_raw_data["AWSManagedRulesBotControlRuleSet"]
        )

    AWSManagedRulesATPRuleSet = field("AWSManagedRulesATPRuleSet")
    AWSManagedRulesACFPRuleSet = field("AWSManagedRulesACFPRuleSet")
    AWSManagedRulesAntiDDoSRuleSet = field("AWSManagedRulesAntiDDoSRuleSet")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleGroupConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleGroupConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallManagerRuleGroup:
    boto3_raw_data: "type_defs.FirewallManagerRuleGroupTypeDef" = dataclasses.field()

    Name = field("Name")
    Priority = field("Priority")

    @cached_property
    def FirewallManagerStatement(self):  # pragma: no cover
        return FirewallManagerStatement.make_one(
            self.boto3_raw_data["FirewallManagerStatement"]
        )

    @cached_property
    def OverrideAction(self):  # pragma: no cover
        return OverrideActionOutput.make_one(self.boto3_raw_data["OverrideAction"])

    @cached_property
    def VisibilityConfig(self):  # pragma: no cover
        return VisibilityConfig.make_one(self.boto3_raw_data["VisibilityConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirewallManagerRuleGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallManagerRuleGroupTypeDef"]
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

    Name = field("Name")
    Priority = field("Priority")

    @cached_property
    def Statement(self):  # pragma: no cover
        return StatementOutput.make_one(self.boto3_raw_data["Statement"])

    @cached_property
    def VisibilityConfig(self):  # pragma: no cover
        return VisibilityConfig.make_one(self.boto3_raw_data["VisibilityConfig"])

    @cached_property
    def Action(self):  # pragma: no cover
        return RuleActionOutput.make_one(self.boto3_raw_data["Action"])

    @cached_property
    def OverrideAction(self):  # pragma: no cover
        return OverrideActionOutput.make_one(self.boto3_raw_data["OverrideAction"])

    @cached_property
    def RuleLabels(self):  # pragma: no cover
        return Label.make_many(self.boto3_raw_data["RuleLabels"])

    @cached_property
    def CaptchaConfig(self):  # pragma: no cover
        return CaptchaConfig.make_one(self.boto3_raw_data["CaptchaConfig"])

    @cached_property
    def ChallengeConfig(self):  # pragma: no cover
        return ChallengeConfig.make_one(self.boto3_raw_data["ChallengeConfig"])

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
class RuleActionOverride:
    boto3_raw_data: "type_defs.RuleActionOverrideTypeDef" = dataclasses.field()

    Name = field("Name")
    ActionToUse = field("ActionToUse")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleActionOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleActionOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLoggingConfigurationRequest:
    boto3_raw_data: "type_defs.PutLoggingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    LoggingConfiguration = field("LoggingConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutLoggingConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLoggingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleGroup:
    boto3_raw_data: "type_defs.RuleGroupTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Capacity = field("Capacity")
    ARN = field("ARN")

    @cached_property
    def VisibilityConfig(self):  # pragma: no cover
        return VisibilityConfig.make_one(self.boto3_raw_data["VisibilityConfig"])

    Description = field("Description")

    @cached_property
    def Rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["Rules"])

    LabelNamespace = field("LabelNamespace")
    CustomResponseBodies = field("CustomResponseBodies")

    @cached_property
    def AvailableLabels(self):  # pragma: no cover
        return LabelSummary.make_many(self.boto3_raw_data["AvailableLabels"])

    @cached_property
    def ConsumedLabels(self):  # pragma: no cover
        return LabelSummary.make_many(self.boto3_raw_data["ConsumedLabels"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebACL:
    boto3_raw_data: "type_defs.WebACLTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    ARN = field("ARN")

    @cached_property
    def DefaultAction(self):  # pragma: no cover
        return DefaultActionOutput.make_one(self.boto3_raw_data["DefaultAction"])

    @cached_property
    def VisibilityConfig(self):  # pragma: no cover
        return VisibilityConfig.make_one(self.boto3_raw_data["VisibilityConfig"])

    Description = field("Description")

    @cached_property
    def Rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def DataProtectionConfig(self):  # pragma: no cover
        return DataProtectionConfigOutput.make_one(
            self.boto3_raw_data["DataProtectionConfig"]
        )

    Capacity = field("Capacity")

    @cached_property
    def PreProcessFirewallManagerRuleGroups(self):  # pragma: no cover
        return FirewallManagerRuleGroup.make_many(
            self.boto3_raw_data["PreProcessFirewallManagerRuleGroups"]
        )

    @cached_property
    def PostProcessFirewallManagerRuleGroups(self):  # pragma: no cover
        return FirewallManagerRuleGroup.make_many(
            self.boto3_raw_data["PostProcessFirewallManagerRuleGroups"]
        )

    ManagedByFirewallManager = field("ManagedByFirewallManager")
    LabelNamespace = field("LabelNamespace")
    CustomResponseBodies = field("CustomResponseBodies")

    @cached_property
    def CaptchaConfig(self):  # pragma: no cover
        return CaptchaConfig.make_one(self.boto3_raw_data["CaptchaConfig"])

    @cached_property
    def ChallengeConfig(self):  # pragma: no cover
        return ChallengeConfig.make_one(self.boto3_raw_data["ChallengeConfig"])

    TokenDomains = field("TokenDomains")

    @cached_property
    def AssociationConfig(self):  # pragma: no cover
        return AssociationConfigOutput.make_one(
            self.boto3_raw_data["AssociationConfig"]
        )

    RetrofittedByFirewallManager = field("RetrofittedByFirewallManager")

    @cached_property
    def OnSourceDDoSProtectionConfig(self):  # pragma: no cover
        return OnSourceDDoSProtectionConfig.make_one(
            self.boto3_raw_data["OnSourceDDoSProtectionConfig"]
        )

    @cached_property
    def ApplicationConfig(self):  # pragma: no cover
        return ApplicationConfigOutput.make_one(
            self.boto3_raw_data["ApplicationConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebACLTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WebACLTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleGroupResponse:
    boto3_raw_data: "type_defs.GetRuleGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def RuleGroup(self):  # pragma: no cover
        return RuleGroup.make_one(self.boto3_raw_data["RuleGroup"])

    LockToken = field("LockToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRuleGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWebACLForResourceResponse:
    boto3_raw_data: "type_defs.GetWebACLForResourceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WebACL(self):  # pragma: no cover
        return WebACL.make_one(self.boto3_raw_data["WebACL"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWebACLForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWebACLForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWebACLResponse:
    boto3_raw_data: "type_defs.GetWebACLResponseTypeDef" = dataclasses.field()

    @cached_property
    def WebACL(self):  # pragma: no cover
        return WebACL.make_one(self.boto3_raw_data["WebACL"])

    LockToken = field("LockToken")
    ApplicationIntegrationURL = field("ApplicationIntegrationURL")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetWebACLResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWebACLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleGroupStatement:
    boto3_raw_data: "type_defs.ManagedRuleGroupStatementTypeDef" = dataclasses.field()

    VendorName = field("VendorName")
    Name = field("Name")
    Version = field("Version")

    @cached_property
    def ExcludedRules(self):  # pragma: no cover
        return ExcludedRule.make_many(self.boto3_raw_data["ExcludedRules"])

    ScopeDownStatement = field("ScopeDownStatement")
    ManagedRuleGroupConfigs = field("ManagedRuleGroupConfigs")
    RuleActionOverrides = field("RuleActionOverrides")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleGroupStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleGroupStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleGroupReferenceStatement:
    boto3_raw_data: "type_defs.RuleGroupReferenceStatementTypeDef" = dataclasses.field()

    ARN = field("ARN")

    @cached_property
    def ExcludedRules(self):  # pragma: no cover
        return ExcludedRule.make_many(self.boto3_raw_data["ExcludedRules"])

    RuleActionOverrides = field("RuleActionOverrides")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleGroupReferenceStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleGroupReferenceStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Statement:
    boto3_raw_data: "type_defs.StatementTypeDef" = dataclasses.field()

    ByteMatchStatement = field("ByteMatchStatement")
    SqliMatchStatement = field("SqliMatchStatement")
    XssMatchStatement = field("XssMatchStatement")
    SizeConstraintStatement = field("SizeConstraintStatement")
    GeoMatchStatement = field("GeoMatchStatement")
    RuleGroupReferenceStatement = field("RuleGroupReferenceStatement")

    @cached_property
    def IPSetReferenceStatement(self):  # pragma: no cover
        return IPSetReferenceStatement.make_one(
            self.boto3_raw_data["IPSetReferenceStatement"]
        )

    RegexPatternSetReferenceStatement = field("RegexPatternSetReferenceStatement")
    RateBasedStatement = field("RateBasedStatement")
    AndStatement = field("AndStatement")
    OrStatement = field("OrStatement")
    NotStatement = field("NotStatement")
    ManagedRuleGroupStatement = field("ManagedRuleGroupStatement")

    @cached_property
    def LabelMatchStatement(self):  # pragma: no cover
        return LabelMatchStatement.make_one(self.boto3_raw_data["LabelMatchStatement"])

    RegexMatchStatement = field("RegexMatchStatement")
    AsnMatchStatement = field("AsnMatchStatement")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    Name = field("Name")
    Priority = field("Priority")
    Statement = field("Statement")

    @cached_property
    def VisibilityConfig(self):  # pragma: no cover
        return VisibilityConfig.make_one(self.boto3_raw_data["VisibilityConfig"])

    Action = field("Action")
    OverrideAction = field("OverrideAction")

    @cached_property
    def RuleLabels(self):  # pragma: no cover
        return Label.make_many(self.boto3_raw_data["RuleLabels"])

    @cached_property
    def CaptchaConfig(self):  # pragma: no cover
        return CaptchaConfig.make_one(self.boto3_raw_data["CaptchaConfig"])

    @cached_property
    def ChallengeConfig(self):  # pragma: no cover
        return ChallengeConfig.make_one(self.boto3_raw_data["ChallengeConfig"])

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
class CheckCapacityRequest:
    boto3_raw_data: "type_defs.CheckCapacityRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    Rules = field("Rules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckCapacityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckCapacityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleGroupRequest:
    boto3_raw_data: "type_defs.CreateRuleGroupRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Capacity = field("Capacity")

    @cached_property
    def VisibilityConfig(self):  # pragma: no cover
        return VisibilityConfig.make_one(self.boto3_raw_data["VisibilityConfig"])

    Description = field("Description")
    Rules = field("Rules")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CustomResponseBodies = field("CustomResponseBodies")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRuleGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebACLRequest:
    boto3_raw_data: "type_defs.CreateWebACLRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    DefaultAction = field("DefaultAction")

    @cached_property
    def VisibilityConfig(self):  # pragma: no cover
        return VisibilityConfig.make_one(self.boto3_raw_data["VisibilityConfig"])

    Description = field("Description")
    Rules = field("Rules")
    DataProtectionConfig = field("DataProtectionConfig")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CustomResponseBodies = field("CustomResponseBodies")

    @cached_property
    def CaptchaConfig(self):  # pragma: no cover
        return CaptchaConfig.make_one(self.boto3_raw_data["CaptchaConfig"])

    @cached_property
    def ChallengeConfig(self):  # pragma: no cover
        return ChallengeConfig.make_one(self.boto3_raw_data["ChallengeConfig"])

    TokenDomains = field("TokenDomains")
    AssociationConfig = field("AssociationConfig")

    @cached_property
    def OnSourceDDoSProtectionConfig(self):  # pragma: no cover
        return OnSourceDDoSProtectionConfig.make_one(
            self.boto3_raw_data["OnSourceDDoSProtectionConfig"]
        )

    ApplicationConfig = field("ApplicationConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebACLRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleGroupRequest:
    boto3_raw_data: "type_defs.UpdateRuleGroupRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")

    @cached_property
    def VisibilityConfig(self):  # pragma: no cover
        return VisibilityConfig.make_one(self.boto3_raw_data["VisibilityConfig"])

    LockToken = field("LockToken")
    Description = field("Description")
    Rules = field("Rules")
    CustomResponseBodies = field("CustomResponseBodies")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebACLRequest:
    boto3_raw_data: "type_defs.UpdateWebACLRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Id = field("Id")
    DefaultAction = field("DefaultAction")

    @cached_property
    def VisibilityConfig(self):  # pragma: no cover
        return VisibilityConfig.make_one(self.boto3_raw_data["VisibilityConfig"])

    LockToken = field("LockToken")
    Description = field("Description")
    Rules = field("Rules")
    DataProtectionConfig = field("DataProtectionConfig")
    CustomResponseBodies = field("CustomResponseBodies")

    @cached_property
    def CaptchaConfig(self):  # pragma: no cover
        return CaptchaConfig.make_one(self.boto3_raw_data["CaptchaConfig"])

    @cached_property
    def ChallengeConfig(self):  # pragma: no cover
        return ChallengeConfig.make_one(self.boto3_raw_data["ChallengeConfig"])

    TokenDomains = field("TokenDomains")
    AssociationConfig = field("AssociationConfig")

    @cached_property
    def OnSourceDDoSProtectionConfig(self):  # pragma: no cover
        return OnSourceDDoSProtectionConfig.make_one(
            self.boto3_raw_data["OnSourceDDoSProtectionConfig"]
        )

    ApplicationConfig = field("ApplicationConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWebACLRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
