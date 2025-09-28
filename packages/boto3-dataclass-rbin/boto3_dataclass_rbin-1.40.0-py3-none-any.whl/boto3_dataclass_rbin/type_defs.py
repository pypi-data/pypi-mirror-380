# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rbin import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ResourceTag:
    boto3_raw_data: "type_defs.ResourceTagTypeDef" = dataclasses.field()

    ResourceTagKey = field("ResourceTagKey")
    ResourceTagValue = field("ResourceTagValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetentionPeriod:
    boto3_raw_data: "type_defs.RetentionPeriodTypeDef" = dataclasses.field()

    RetentionPeriodValue = field("RetentionPeriodValue")
    RetentionPeriodUnit = field("RetentionPeriodUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetentionPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetentionPeriodTypeDef"]],
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
class DeleteRuleRequest:
    boto3_raw_data: "type_defs.DeleteRuleRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleRequest:
    boto3_raw_data: "type_defs.GetRuleRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRuleRequestTypeDef"]],
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
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class UnlockDelay:
    boto3_raw_data: "type_defs.UnlockDelayTypeDef" = dataclasses.field()

    UnlockDelayValue = field("UnlockDelayValue")
    UnlockDelayUnit = field("UnlockDelayUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnlockDelayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UnlockDelayTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnlockRuleRequest:
    boto3_raw_data: "type_defs.UnlockRuleRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnlockRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnlockRuleRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")
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
class ListRulesRequest:
    boto3_raw_data: "type_defs.ListRulesRequestTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    LockState = field("LockState")

    @cached_property
    def ExcludeResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ExcludeResourceTags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesRequestTypeDef"]
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

    Identifier = field("Identifier")
    Description = field("Description")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    LockState = field("LockState")
    RuleArn = field("RuleArn")

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
class UpdateRuleRequest:
    boto3_raw_data: "type_defs.UpdateRuleRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    Description = field("Description")
    ResourceType = field("ResourceType")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @cached_property
    def ExcludeResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ExcludeResourceTags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class UpdateRuleResponse:
    boto3_raw_data: "type_defs.UpdateRuleResponseTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    Description = field("Description")
    ResourceType = field("ResourceType")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    Status = field("Status")
    LockState = field("LockState")
    LockEndTime = field("LockEndTime")
    RuleArn = field("RuleArn")

    @cached_property
    def ExcludeResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ExcludeResourceTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListRulesRequestPaginateTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    LockState = field("LockState")

    @cached_property
    def ExcludeResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ExcludeResourceTags"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LockConfiguration:
    boto3_raw_data: "type_defs.LockConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def UnlockDelay(self):  # pragma: no cover
        return UnlockDelay.make_one(self.boto3_raw_data["UnlockDelay"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LockConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LockConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesResponse:
    boto3_raw_data: "type_defs.ListRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return RuleSummary.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleRequest:
    boto3_raw_data: "type_defs.CreateRuleRequestTypeDef" = dataclasses.field()

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    ResourceType = field("ResourceType")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @cached_property
    def LockConfiguration(self):  # pragma: no cover
        return LockConfiguration.make_one(self.boto3_raw_data["LockConfiguration"])

    @cached_property
    def ExcludeResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ExcludeResourceTags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleResponse:
    boto3_raw_data: "type_defs.CreateRuleResponseTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ResourceType = field("ResourceType")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    Status = field("Status")

    @cached_property
    def LockConfiguration(self):  # pragma: no cover
        return LockConfiguration.make_one(self.boto3_raw_data["LockConfiguration"])

    LockState = field("LockState")
    RuleArn = field("RuleArn")

    @cached_property
    def ExcludeResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ExcludeResourceTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleResponse:
    boto3_raw_data: "type_defs.GetRuleResponseTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    Description = field("Description")
    ResourceType = field("ResourceType")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    Status = field("Status")

    @cached_property
    def LockConfiguration(self):  # pragma: no cover
        return LockConfiguration.make_one(self.boto3_raw_data["LockConfiguration"])

    LockState = field("LockState")
    LockEndTime = field("LockEndTime")
    RuleArn = field("RuleArn")

    @cached_property
    def ExcludeResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ExcludeResourceTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRuleResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRuleResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LockRuleRequest:
    boto3_raw_data: "type_defs.LockRuleRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @cached_property
    def LockConfiguration(self):  # pragma: no cover
        return LockConfiguration.make_one(self.boto3_raw_data["LockConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LockRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LockRuleRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LockRuleResponse:
    boto3_raw_data: "type_defs.LockRuleResponseTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    Description = field("Description")
    ResourceType = field("ResourceType")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    Status = field("Status")

    @cached_property
    def LockConfiguration(self):  # pragma: no cover
        return LockConfiguration.make_one(self.boto3_raw_data["LockConfiguration"])

    LockState = field("LockState")
    RuleArn = field("RuleArn")

    @cached_property
    def ExcludeResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ExcludeResourceTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LockRuleResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LockRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnlockRuleResponse:
    boto3_raw_data: "type_defs.UnlockRuleResponseTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    Description = field("Description")
    ResourceType = field("ResourceType")

    @cached_property
    def RetentionPeriod(self):  # pragma: no cover
        return RetentionPeriod.make_one(self.boto3_raw_data["RetentionPeriod"])

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    Status = field("Status")

    @cached_property
    def LockConfiguration(self):  # pragma: no cover
        return LockConfiguration.make_one(self.boto3_raw_data["LockConfiguration"])

    LockState = field("LockState")
    LockEndTime = field("LockEndTime")
    RuleArn = field("RuleArn")

    @cached_property
    def ExcludeResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ExcludeResourceTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnlockRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnlockRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
