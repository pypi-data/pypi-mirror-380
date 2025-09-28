# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_observabilityadmin import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class SourceLogsConfiguration:
    boto3_raw_data: "type_defs.SourceLogsConfigurationTypeDef" = dataclasses.field()

    LogGroupSelectionCriteria = field("LogGroupSelectionCriteria")
    EncryptedLogGroupStrategy = field("EncryptedLogGroupStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceLogsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceLogsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CentralizationRuleSummary:
    boto3_raw_data: "type_defs.CentralizationRuleSummaryTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    RuleArn = field("RuleArn")
    CreatorAccountId = field("CreatorAccountId")
    CreatedTimeStamp = field("CreatedTimeStamp")
    CreatedRegion = field("CreatedRegion")
    LastUpdateTimeStamp = field("LastUpdateTimeStamp")
    RuleHealth = field("RuleHealth")
    FailureReason = field("FailureReason")
    DestinationAccountId = field("DestinationAccountId")
    DestinationRegion = field("DestinationRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CentralizationRuleSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CentralizationRuleSummaryTypeDef"]
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
class DeleteCentralizationRuleForOrganizationInput:
    boto3_raw_data: "type_defs.DeleteCentralizationRuleForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleIdentifier = field("RuleIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCentralizationRuleForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCentralizationRuleForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTelemetryRuleForOrganizationInput:
    boto3_raw_data: "type_defs.DeleteTelemetryRuleForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleIdentifier = field("RuleIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTelemetryRuleForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTelemetryRuleForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTelemetryRuleInput:
    boto3_raw_data: "type_defs.DeleteTelemetryRuleInputTypeDef" = dataclasses.field()

    RuleIdentifier = field("RuleIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTelemetryRuleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTelemetryRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogsBackupConfiguration:
    boto3_raw_data: "type_defs.LogsBackupConfigurationTypeDef" = dataclasses.field()

    Region = field("Region")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogsBackupConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogsBackupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogsEncryptionConfiguration:
    boto3_raw_data: "type_defs.LogsEncryptionConfigurationTypeDef" = dataclasses.field()

    EncryptionStrategy = field("EncryptionStrategy")
    KmsKeyArn = field("KmsKeyArn")
    EncryptionConflictResolutionStrategy = field("EncryptionConflictResolutionStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogsEncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogsEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCentralizationRuleForOrganizationInput:
    boto3_raw_data: "type_defs.GetCentralizationRuleForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleIdentifier = field("RuleIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCentralizationRuleForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCentralizationRuleForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTelemetryRuleForOrganizationInput:
    boto3_raw_data: "type_defs.GetTelemetryRuleForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleIdentifier = field("RuleIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTelemetryRuleForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTelemetryRuleForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTelemetryRuleInput:
    boto3_raw_data: "type_defs.GetTelemetryRuleInputTypeDef" = dataclasses.field()

    RuleIdentifier = field("RuleIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTelemetryRuleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTelemetryRuleInputTypeDef"]
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
class ListCentralizationRulesForOrganizationInput:
    boto3_raw_data: "type_defs.ListCentralizationRulesForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleNamePrefix = field("RuleNamePrefix")
    AllRegions = field("AllRegions")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCentralizationRulesForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCentralizationRulesForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTelemetryForOrganizationInput:
    boto3_raw_data: "type_defs.ListResourceTelemetryForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    AccountIdentifiers = field("AccountIdentifiers")
    ResourceIdentifierPrefix = field("ResourceIdentifierPrefix")
    ResourceTypes = field("ResourceTypes")
    TelemetryConfigurationState = field("TelemetryConfigurationState")
    ResourceTags = field("ResourceTags")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceTelemetryForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTelemetryForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelemetryConfiguration:
    boto3_raw_data: "type_defs.TelemetryConfigurationTypeDef" = dataclasses.field()

    AccountIdentifier = field("AccountIdentifier")
    TelemetryConfigurationState = field("TelemetryConfigurationState")
    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceTags = field("ResourceTags")
    LastUpdateTimeStamp = field("LastUpdateTimeStamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TelemetryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelemetryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTelemetryInput:
    boto3_raw_data: "type_defs.ListResourceTelemetryInputTypeDef" = dataclasses.field()

    ResourceIdentifierPrefix = field("ResourceIdentifierPrefix")
    ResourceTypes = field("ResourceTypes")
    TelemetryConfigurationState = field("TelemetryConfigurationState")
    ResourceTags = field("ResourceTags")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceTelemetryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTelemetryInputTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class ListTelemetryRulesForOrganizationInput:
    boto3_raw_data: "type_defs.ListTelemetryRulesForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleNamePrefix = field("RuleNamePrefix")
    SourceAccountIds = field("SourceAccountIds")
    SourceOrganizationUnitIds = field("SourceOrganizationUnitIds")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTelemetryRulesForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTelemetryRulesForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelemetryRuleSummary:
    boto3_raw_data: "type_defs.TelemetryRuleSummaryTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    RuleArn = field("RuleArn")
    CreatedTimeStamp = field("CreatedTimeStamp")
    LastUpdateTimeStamp = field("LastUpdateTimeStamp")
    ResourceType = field("ResourceType")
    TelemetryType = field("TelemetryType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TelemetryRuleSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelemetryRuleSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTelemetryRulesInput:
    boto3_raw_data: "type_defs.ListTelemetryRulesInputTypeDef" = dataclasses.field()

    RuleNamePrefix = field("RuleNamePrefix")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTelemetryRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTelemetryRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
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
class VPCFlowLogParameters:
    boto3_raw_data: "type_defs.VPCFlowLogParametersTypeDef" = dataclasses.field()

    LogFormat = field("LogFormat")
    TrafficType = field("TrafficType")
    MaxAggregationInterval = field("MaxAggregationInterval")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VPCFlowLogParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VPCFlowLogParametersTypeDef"]
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

    ResourceARN = field("ResourceARN")
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
class CentralizationRuleSourceOutput:
    boto3_raw_data: "type_defs.CentralizationRuleSourceOutputTypeDef" = (
        dataclasses.field()
    )

    Regions = field("Regions")
    Scope = field("Scope")

    @cached_property
    def SourceLogsConfiguration(self):  # pragma: no cover
        return SourceLogsConfiguration.make_one(
            self.boto3_raw_data["SourceLogsConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CentralizationRuleSourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CentralizationRuleSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CentralizationRuleSource:
    boto3_raw_data: "type_defs.CentralizationRuleSourceTypeDef" = dataclasses.field()

    Regions = field("Regions")
    Scope = field("Scope")

    @cached_property
    def SourceLogsConfiguration(self):  # pragma: no cover
        return SourceLogsConfiguration.make_one(
            self.boto3_raw_data["SourceLogsConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CentralizationRuleSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CentralizationRuleSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCentralizationRuleForOrganizationOutput:
    boto3_raw_data: "type_defs.CreateCentralizationRuleForOrganizationOutputTypeDef" = (
        dataclasses.field()
    )

    RuleArn = field("RuleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCentralizationRuleForOrganizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCentralizationRuleForOrganizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTelemetryRuleForOrganizationOutput:
    boto3_raw_data: "type_defs.CreateTelemetryRuleForOrganizationOutputTypeDef" = (
        dataclasses.field()
    )

    RuleArn = field("RuleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTelemetryRuleForOrganizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTelemetryRuleForOrganizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTelemetryRuleOutput:
    boto3_raw_data: "type_defs.CreateTelemetryRuleOutputTypeDef" = dataclasses.field()

    RuleArn = field("RuleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTelemetryRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTelemetryRuleOutputTypeDef"]
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
class GetTelemetryEvaluationStatusForOrganizationOutput:
    boto3_raw_data: (
        "type_defs.GetTelemetryEvaluationStatusForOrganizationOutputTypeDef"
    ) = dataclasses.field()

    Status = field("Status")
    FailureReason = field("FailureReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTelemetryEvaluationStatusForOrganizationOutputTypeDef"
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
                "type_defs.GetTelemetryEvaluationStatusForOrganizationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTelemetryEvaluationStatusOutput:
    boto3_raw_data: "type_defs.GetTelemetryEvaluationStatusOutputTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    FailureReason = field("FailureReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTelemetryEvaluationStatusOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTelemetryEvaluationStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCentralizationRulesForOrganizationOutput:
    boto3_raw_data: "type_defs.ListCentralizationRulesForOrganizationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CentralizationRuleSummaries(self):  # pragma: no cover
        return CentralizationRuleSummary.make_many(
            self.boto3_raw_data["CentralizationRuleSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCentralizationRulesForOrganizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCentralizationRulesForOrganizationOutputTypeDef"]
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
class UpdateCentralizationRuleForOrganizationOutput:
    boto3_raw_data: "type_defs.UpdateCentralizationRuleForOrganizationOutputTypeDef" = (
        dataclasses.field()
    )

    RuleArn = field("RuleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCentralizationRuleForOrganizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCentralizationRuleForOrganizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTelemetryRuleForOrganizationOutput:
    boto3_raw_data: "type_defs.UpdateTelemetryRuleForOrganizationOutputTypeDef" = (
        dataclasses.field()
    )

    RuleArn = field("RuleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTelemetryRuleForOrganizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTelemetryRuleForOrganizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTelemetryRuleOutput:
    boto3_raw_data: "type_defs.UpdateTelemetryRuleOutputTypeDef" = dataclasses.field()

    RuleArn = field("RuleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTelemetryRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTelemetryRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationLogsConfiguration:
    boto3_raw_data: "type_defs.DestinationLogsConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LogsEncryptionConfiguration(self):  # pragma: no cover
        return LogsEncryptionConfiguration.make_one(
            self.boto3_raw_data["LogsEncryptionConfiguration"]
        )

    @cached_property
    def BackupConfiguration(self):  # pragma: no cover
        return LogsBackupConfiguration.make_one(
            self.boto3_raw_data["BackupConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationLogsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationLogsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCentralizationRulesForOrganizationInputPaginate:
    boto3_raw_data: (
        "type_defs.ListCentralizationRulesForOrganizationInputPaginateTypeDef"
    ) = dataclasses.field()

    RuleNamePrefix = field("RuleNamePrefix")
    AllRegions = field("AllRegions")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCentralizationRulesForOrganizationInputPaginateTypeDef"
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
                "type_defs.ListCentralizationRulesForOrganizationInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTelemetryForOrganizationInputPaginate:
    boto3_raw_data: (
        "type_defs.ListResourceTelemetryForOrganizationInputPaginateTypeDef"
    ) = dataclasses.field()

    AccountIdentifiers = field("AccountIdentifiers")
    ResourceIdentifierPrefix = field("ResourceIdentifierPrefix")
    ResourceTypes = field("ResourceTypes")
    TelemetryConfigurationState = field("TelemetryConfigurationState")
    ResourceTags = field("ResourceTags")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceTelemetryForOrganizationInputPaginateTypeDef"
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
                "type_defs.ListResourceTelemetryForOrganizationInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTelemetryInputPaginate:
    boto3_raw_data: "type_defs.ListResourceTelemetryInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifierPrefix = field("ResourceIdentifierPrefix")
    ResourceTypes = field("ResourceTypes")
    TelemetryConfigurationState = field("TelemetryConfigurationState")
    ResourceTags = field("ResourceTags")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceTelemetryInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTelemetryInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTelemetryRulesForOrganizationInputPaginate:
    boto3_raw_data: (
        "type_defs.ListTelemetryRulesForOrganizationInputPaginateTypeDef"
    ) = dataclasses.field()

    RuleNamePrefix = field("RuleNamePrefix")
    SourceAccountIds = field("SourceAccountIds")
    SourceOrganizationUnitIds = field("SourceOrganizationUnitIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTelemetryRulesForOrganizationInputPaginateTypeDef"
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
                "type_defs.ListTelemetryRulesForOrganizationInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTelemetryRulesInputPaginate:
    boto3_raw_data: "type_defs.ListTelemetryRulesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    RuleNamePrefix = field("RuleNamePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTelemetryRulesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTelemetryRulesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTelemetryForOrganizationOutput:
    boto3_raw_data: "type_defs.ListResourceTelemetryForOrganizationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TelemetryConfigurations(self):  # pragma: no cover
        return TelemetryConfiguration.make_many(
            self.boto3_raw_data["TelemetryConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceTelemetryForOrganizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTelemetryForOrganizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTelemetryOutput:
    boto3_raw_data: "type_defs.ListResourceTelemetryOutputTypeDef" = dataclasses.field()

    @cached_property
    def TelemetryConfigurations(self):  # pragma: no cover
        return TelemetryConfiguration.make_many(
            self.boto3_raw_data["TelemetryConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceTelemetryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTelemetryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTelemetryRulesForOrganizationOutput:
    boto3_raw_data: "type_defs.ListTelemetryRulesForOrganizationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TelemetryRuleSummaries(self):  # pragma: no cover
        return TelemetryRuleSummary.make_many(
            self.boto3_raw_data["TelemetryRuleSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTelemetryRulesForOrganizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTelemetryRulesForOrganizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTelemetryRulesOutput:
    boto3_raw_data: "type_defs.ListTelemetryRulesOutputTypeDef" = dataclasses.field()

    @cached_property
    def TelemetryRuleSummaries(self):  # pragma: no cover
        return TelemetryRuleSummary.make_many(
            self.boto3_raw_data["TelemetryRuleSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTelemetryRulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTelemetryRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelemetryDestinationConfiguration:
    boto3_raw_data: "type_defs.TelemetryDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    DestinationType = field("DestinationType")
    DestinationPattern = field("DestinationPattern")
    RetentionInDays = field("RetentionInDays")

    @cached_property
    def VPCFlowLogParameters(self):  # pragma: no cover
        return VPCFlowLogParameters.make_one(
            self.boto3_raw_data["VPCFlowLogParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TelemetryDestinationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelemetryDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CentralizationRuleDestination:
    boto3_raw_data: "type_defs.CentralizationRuleDestinationTypeDef" = (
        dataclasses.field()
    )

    Region = field("Region")
    Account = field("Account")

    @cached_property
    def DestinationLogsConfiguration(self):  # pragma: no cover
        return DestinationLogsConfiguration.make_one(
            self.boto3_raw_data["DestinationLogsConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CentralizationRuleDestinationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CentralizationRuleDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelemetryRule:
    boto3_raw_data: "type_defs.TelemetryRuleTypeDef" = dataclasses.field()

    TelemetryType = field("TelemetryType")
    ResourceType = field("ResourceType")

    @cached_property
    def DestinationConfiguration(self):  # pragma: no cover
        return TelemetryDestinationConfiguration.make_one(
            self.boto3_raw_data["DestinationConfiguration"]
        )

    Scope = field("Scope")
    SelectionCriteria = field("SelectionCriteria")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TelemetryRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TelemetryRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CentralizationRuleOutput:
    boto3_raw_data: "type_defs.CentralizationRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def Source(self):  # pragma: no cover
        return CentralizationRuleSourceOutput.make_one(self.boto3_raw_data["Source"])

    @cached_property
    def Destination(self):  # pragma: no cover
        return CentralizationRuleDestination.make_one(
            self.boto3_raw_data["Destination"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CentralizationRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CentralizationRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CentralizationRule:
    boto3_raw_data: "type_defs.CentralizationRuleTypeDef" = dataclasses.field()

    @cached_property
    def Source(self):  # pragma: no cover
        return CentralizationRuleSource.make_one(self.boto3_raw_data["Source"])

    @cached_property
    def Destination(self):  # pragma: no cover
        return CentralizationRuleDestination.make_one(
            self.boto3_raw_data["Destination"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CentralizationRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CentralizationRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTelemetryRuleForOrganizationInput:
    boto3_raw_data: "type_defs.CreateTelemetryRuleForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleName = field("RuleName")

    @cached_property
    def Rule(self):  # pragma: no cover
        return TelemetryRule.make_one(self.boto3_raw_data["Rule"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTelemetryRuleForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTelemetryRuleForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTelemetryRuleInput:
    boto3_raw_data: "type_defs.CreateTelemetryRuleInputTypeDef" = dataclasses.field()

    RuleName = field("RuleName")

    @cached_property
    def Rule(self):  # pragma: no cover
        return TelemetryRule.make_one(self.boto3_raw_data["Rule"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTelemetryRuleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTelemetryRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTelemetryRuleForOrganizationOutput:
    boto3_raw_data: "type_defs.GetTelemetryRuleForOrganizationOutputTypeDef" = (
        dataclasses.field()
    )

    RuleName = field("RuleName")
    RuleArn = field("RuleArn")
    CreatedTimeStamp = field("CreatedTimeStamp")
    LastUpdateTimeStamp = field("LastUpdateTimeStamp")

    @cached_property
    def TelemetryRule(self):  # pragma: no cover
        return TelemetryRule.make_one(self.boto3_raw_data["TelemetryRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTelemetryRuleForOrganizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTelemetryRuleForOrganizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTelemetryRuleOutput:
    boto3_raw_data: "type_defs.GetTelemetryRuleOutputTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    RuleArn = field("RuleArn")
    CreatedTimeStamp = field("CreatedTimeStamp")
    LastUpdateTimeStamp = field("LastUpdateTimeStamp")

    @cached_property
    def TelemetryRule(self):  # pragma: no cover
        return TelemetryRule.make_one(self.boto3_raw_data["TelemetryRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTelemetryRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTelemetryRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTelemetryRuleForOrganizationInput:
    boto3_raw_data: "type_defs.UpdateTelemetryRuleForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleIdentifier = field("RuleIdentifier")

    @cached_property
    def Rule(self):  # pragma: no cover
        return TelemetryRule.make_one(self.boto3_raw_data["Rule"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTelemetryRuleForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTelemetryRuleForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTelemetryRuleInput:
    boto3_raw_data: "type_defs.UpdateTelemetryRuleInputTypeDef" = dataclasses.field()

    RuleIdentifier = field("RuleIdentifier")

    @cached_property
    def Rule(self):  # pragma: no cover
        return TelemetryRule.make_one(self.boto3_raw_data["Rule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTelemetryRuleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTelemetryRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCentralizationRuleForOrganizationOutput:
    boto3_raw_data: "type_defs.GetCentralizationRuleForOrganizationOutputTypeDef" = (
        dataclasses.field()
    )

    RuleName = field("RuleName")
    RuleArn = field("RuleArn")
    CreatorAccountId = field("CreatorAccountId")
    CreatedTimeStamp = field("CreatedTimeStamp")
    CreatedRegion = field("CreatedRegion")
    LastUpdateTimeStamp = field("LastUpdateTimeStamp")
    RuleHealth = field("RuleHealth")
    FailureReason = field("FailureReason")

    @cached_property
    def CentralizationRule(self):  # pragma: no cover
        return CentralizationRuleOutput.make_one(
            self.boto3_raw_data["CentralizationRule"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCentralizationRuleForOrganizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCentralizationRuleForOrganizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCentralizationRuleForOrganizationInput:
    boto3_raw_data: "type_defs.CreateCentralizationRuleForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleName = field("RuleName")
    Rule = field("Rule")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCentralizationRuleForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCentralizationRuleForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCentralizationRuleForOrganizationInput:
    boto3_raw_data: "type_defs.UpdateCentralizationRuleForOrganizationInputTypeDef" = (
        dataclasses.field()
    )

    RuleIdentifier = field("RuleIdentifier")
    Rule = field("Rule")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCentralizationRuleForOrganizationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCentralizationRuleForOrganizationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
