# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pipes import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AwsVpcConfigurationOutput:
    boto3_raw_data: "type_defs.AwsVpcConfigurationOutputTypeDef" = dataclasses.field()

    Subnets = field("Subnets")
    SecurityGroups = field("SecurityGroups")
    AssignPublicIp = field("AssignPublicIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsVpcConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsVpcConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsVpcConfiguration:
    boto3_raw_data: "type_defs.AwsVpcConfigurationTypeDef" = dataclasses.field()

    Subnets = field("Subnets")
    SecurityGroups = field("SecurityGroups")
    AssignPublicIp = field("AssignPublicIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsVpcConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsVpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchArrayProperties:
    boto3_raw_data: "type_defs.BatchArrayPropertiesTypeDef" = dataclasses.field()

    Size = field("Size")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchArrayPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchArrayPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchEnvironmentVariable:
    boto3_raw_data: "type_defs.BatchEnvironmentVariableTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchEnvironmentVariableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchEnvironmentVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchResourceRequirement:
    boto3_raw_data: "type_defs.BatchResourceRequirementTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchResourceRequirementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchResourceRequirementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchJobDependency:
    boto3_raw_data: "type_defs.BatchJobDependencyTypeDef" = dataclasses.field()

    JobId = field("JobId")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchJobDependencyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchJobDependencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchRetryStrategy:
    boto3_raw_data: "type_defs.BatchRetryStrategyTypeDef" = dataclasses.field()

    Attempts = field("Attempts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchRetryStrategyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchRetryStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityProviderStrategyItem:
    boto3_raw_data: "type_defs.CapacityProviderStrategyItemTypeDef" = (
        dataclasses.field()
    )

    capacityProvider = field("capacityProvider")
    weight = field("weight")
    base = field("base")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityProviderStrategyItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityProviderStrategyItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchLogsLogDestinationParameters:
    boto3_raw_data: "type_defs.CloudwatchLogsLogDestinationParametersTypeDef" = (
        dataclasses.field()
    )

    LogGroupArn = field("LogGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudwatchLogsLogDestinationParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchLogsLogDestinationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchLogsLogDestination:
    boto3_raw_data: "type_defs.CloudwatchLogsLogDestinationTypeDef" = (
        dataclasses.field()
    )

    LogGroupArn = field("LogGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudwatchLogsLogDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchLogsLogDestinationTypeDef"]
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
class DeadLetterConfig:
    boto3_raw_data: "type_defs.DeadLetterConfigTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeadLetterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeadLetterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePipeRequest:
    boto3_raw_data: "type_defs.DeletePipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeletePipeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePipeRequest:
    boto3_raw_data: "type_defs.DescribePipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionMapping:
    boto3_raw_data: "type_defs.DimensionMappingTypeDef" = dataclasses.field()

    DimensionValue = field("DimensionValue")
    DimensionValueType = field("DimensionValueType")
    DimensionName = field("DimensionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsEnvironmentFile:
    boto3_raw_data: "type_defs.EcsEnvironmentFileTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsEnvironmentFileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsEnvironmentFileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsEnvironmentVariable:
    boto3_raw_data: "type_defs.EcsEnvironmentVariableTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsEnvironmentVariableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsEnvironmentVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsResourceRequirement:
    boto3_raw_data: "type_defs.EcsResourceRequirementTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsResourceRequirementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsResourceRequirementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsEphemeralStorage:
    boto3_raw_data: "type_defs.EcsEphemeralStorageTypeDef" = dataclasses.field()

    sizeInGiB = field("sizeInGiB")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsEphemeralStorageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsEphemeralStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsInferenceAcceleratorOverride:
    boto3_raw_data: "type_defs.EcsInferenceAcceleratorOverrideTypeDef" = (
        dataclasses.field()
    )

    deviceName = field("deviceName")
    deviceType = field("deviceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EcsInferenceAcceleratorOverrideTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsInferenceAcceleratorOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Pattern = field("Pattern")

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
class FirehoseLogDestinationParameters:
    boto3_raw_data: "type_defs.FirehoseLogDestinationParametersTypeDef" = (
        dataclasses.field()
    )

    DeliveryStreamArn = field("DeliveryStreamArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FirehoseLogDestinationParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirehoseLogDestinationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirehoseLogDestination:
    boto3_raw_data: "type_defs.FirehoseLogDestinationTypeDef" = dataclasses.field()

    DeliveryStreamArn = field("DeliveryStreamArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirehoseLogDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirehoseLogDestinationTypeDef"]
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
class ListPipesRequest:
    boto3_raw_data: "type_defs.ListPipesRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")
    SourcePrefix = field("SourcePrefix")
    TargetPrefix = field("TargetPrefix")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListPipesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Pipe:
    boto3_raw_data: "type_defs.PipeTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")
    StateReason = field("StateReason")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    Source = field("Source")
    Target = field("Target")
    Enrichment = field("Enrichment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipeTypeDef"]]
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
class MQBrokerAccessCredentials:
    boto3_raw_data: "type_defs.MQBrokerAccessCredentialsTypeDef" = dataclasses.field()

    BasicAuth = field("BasicAuth")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MQBrokerAccessCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MQBrokerAccessCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MSKAccessCredentials:
    boto3_raw_data: "type_defs.MSKAccessCredentialsTypeDef" = dataclasses.field()

    SaslScram512Auth = field("SaslScram512Auth")
    ClientCertificateTlsAuth = field("ClientCertificateTlsAuth")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MSKAccessCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MSKAccessCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiMeasureAttributeMapping:
    boto3_raw_data: "type_defs.MultiMeasureAttributeMappingTypeDef" = (
        dataclasses.field()
    )

    MeasureValue = field("MeasureValue")
    MeasureValueType = field("MeasureValueType")
    MultiMeasureAttributeName = field("MultiMeasureAttributeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiMeasureAttributeMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiMeasureAttributeMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeEnrichmentHttpParametersOutput:
    boto3_raw_data: "type_defs.PipeEnrichmentHttpParametersOutputTypeDef" = (
        dataclasses.field()
    )

    PathParameterValues = field("PathParameterValues")
    HeaderParameters = field("HeaderParameters")
    QueryStringParameters = field("QueryStringParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeEnrichmentHttpParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeEnrichmentHttpParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeEnrichmentHttpParameters:
    boto3_raw_data: "type_defs.PipeEnrichmentHttpParametersTypeDef" = (
        dataclasses.field()
    )

    PathParameterValues = field("PathParameterValues")
    HeaderParameters = field("HeaderParameters")
    QueryStringParameters = field("QueryStringParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeEnrichmentHttpParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeEnrichmentHttpParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LogDestinationParameters:
    boto3_raw_data: "type_defs.S3LogDestinationParametersTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    BucketOwner = field("BucketOwner")
    OutputFormat = field("OutputFormat")
    Prefix = field("Prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3LogDestinationParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3LogDestinationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LogDestination:
    boto3_raw_data: "type_defs.S3LogDestinationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    Prefix = field("Prefix")
    BucketOwner = field("BucketOwner")
    OutputFormat = field("OutputFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LogDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3LogDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceSqsQueueParameters:
    boto3_raw_data: "type_defs.PipeSourceSqsQueueParametersTypeDef" = (
        dataclasses.field()
    )

    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeSourceSqsQueueParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceSqsQueueParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedKafkaAccessConfigurationCredentials:
    boto3_raw_data: (
        "type_defs.SelfManagedKafkaAccessConfigurationCredentialsTypeDef"
    ) = dataclasses.field()

    BasicAuth = field("BasicAuth")
    SaslScram512Auth = field("SaslScram512Auth")
    SaslScram256Auth = field("SaslScram256Auth")
    ClientCertificateTlsAuth = field("ClientCertificateTlsAuth")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelfManagedKafkaAccessConfigurationCredentialsTypeDef"
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
                "type_defs.SelfManagedKafkaAccessConfigurationCredentialsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedKafkaAccessConfigurationVpcOutput:
    boto3_raw_data: "type_defs.SelfManagedKafkaAccessConfigurationVpcOutputTypeDef" = (
        dataclasses.field()
    )

    Subnets = field("Subnets")
    SecurityGroup = field("SecurityGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelfManagedKafkaAccessConfigurationVpcOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManagedKafkaAccessConfigurationVpcOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedKafkaAccessConfigurationVpc:
    boto3_raw_data: "type_defs.SelfManagedKafkaAccessConfigurationVpcTypeDef" = (
        dataclasses.field()
    )

    Subnets = field("Subnets")
    SecurityGroup = field("SecurityGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelfManagedKafkaAccessConfigurationVpcTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManagedKafkaAccessConfigurationVpcTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetCloudWatchLogsParameters:
    boto3_raw_data: "type_defs.PipeTargetCloudWatchLogsParametersTypeDef" = (
        dataclasses.field()
    )

    LogStreamName = field("LogStreamName")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetCloudWatchLogsParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetCloudWatchLogsParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlacementConstraint:
    boto3_raw_data: "type_defs.PlacementConstraintTypeDef" = dataclasses.field()

    type = field("type")
    expression = field("expression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlacementConstraintTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlacementConstraintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlacementStrategy:
    boto3_raw_data: "type_defs.PlacementStrategyTypeDef" = dataclasses.field()

    type = field("type")
    field = field("field")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlacementStrategyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlacementStrategyTypeDef"]
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
class PipeTargetEventBridgeEventBusParametersOutput:
    boto3_raw_data: "type_defs.PipeTargetEventBridgeEventBusParametersOutputTypeDef" = (
        dataclasses.field()
    )

    EndpointId = field("EndpointId")
    DetailType = field("DetailType")
    Source = field("Source")
    Resources = field("Resources")
    Time = field("Time")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetEventBridgeEventBusParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetEventBridgeEventBusParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetEventBridgeEventBusParameters:
    boto3_raw_data: "type_defs.PipeTargetEventBridgeEventBusParametersTypeDef" = (
        dataclasses.field()
    )

    EndpointId = field("EndpointId")
    DetailType = field("DetailType")
    Source = field("Source")
    Resources = field("Resources")
    Time = field("Time")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetEventBridgeEventBusParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetEventBridgeEventBusParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetHttpParametersOutput:
    boto3_raw_data: "type_defs.PipeTargetHttpParametersOutputTypeDef" = (
        dataclasses.field()
    )

    PathParameterValues = field("PathParameterValues")
    HeaderParameters = field("HeaderParameters")
    QueryStringParameters = field("QueryStringParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PipeTargetHttpParametersOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetHttpParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetHttpParameters:
    boto3_raw_data: "type_defs.PipeTargetHttpParametersTypeDef" = dataclasses.field()

    PathParameterValues = field("PathParameterValues")
    HeaderParameters = field("HeaderParameters")
    QueryStringParameters = field("QueryStringParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeTargetHttpParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetHttpParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetKinesisStreamParameters:
    boto3_raw_data: "type_defs.PipeTargetKinesisStreamParametersTypeDef" = (
        dataclasses.field()
    )

    PartitionKey = field("PartitionKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetKinesisStreamParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetKinesisStreamParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetLambdaFunctionParameters:
    boto3_raw_data: "type_defs.PipeTargetLambdaFunctionParametersTypeDef" = (
        dataclasses.field()
    )

    InvocationType = field("InvocationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetLambdaFunctionParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetLambdaFunctionParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetRedshiftDataParametersOutput:
    boto3_raw_data: "type_defs.PipeTargetRedshiftDataParametersOutputTypeDef" = (
        dataclasses.field()
    )

    Database = field("Database")
    Sqls = field("Sqls")
    SecretManagerArn = field("SecretManagerArn")
    DbUser = field("DbUser")
    StatementName = field("StatementName")
    WithEvent = field("WithEvent")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetRedshiftDataParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetRedshiftDataParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetSqsQueueParameters:
    boto3_raw_data: "type_defs.PipeTargetSqsQueueParametersTypeDef" = (
        dataclasses.field()
    )

    MessageGroupId = field("MessageGroupId")
    MessageDeduplicationId = field("MessageDeduplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeTargetSqsQueueParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetSqsQueueParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetStateMachineParameters:
    boto3_raw_data: "type_defs.PipeTargetStateMachineParametersTypeDef" = (
        dataclasses.field()
    )

    InvocationType = field("InvocationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PipeTargetStateMachineParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetStateMachineParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetRedshiftDataParameters:
    boto3_raw_data: "type_defs.PipeTargetRedshiftDataParametersTypeDef" = (
        dataclasses.field()
    )

    Database = field("Database")
    Sqls = field("Sqls")
    SecretManagerArn = field("SecretManagerArn")
    DbUser = field("DbUser")
    StatementName = field("StatementName")
    WithEvent = field("WithEvent")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PipeTargetRedshiftDataParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetRedshiftDataParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerPipelineParameter:
    boto3_raw_data: "type_defs.SageMakerPipelineParameterTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SageMakerPipelineParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerPipelineParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SingleMeasureMapping:
    boto3_raw_data: "type_defs.SingleMeasureMappingTypeDef" = dataclasses.field()

    MeasureValue = field("MeasureValue")
    MeasureValueType = field("MeasureValueType")
    MeasureName = field("MeasureName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SingleMeasureMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingleMeasureMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPipeRequest:
    boto3_raw_data: "type_defs.StartPipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartPipeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPipeRequest:
    boto3_raw_data: "type_defs.StopPipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopPipeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopPipeRequestTypeDef"]],
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
class UpdatePipeSourceSqsQueueParameters:
    boto3_raw_data: "type_defs.UpdatePipeSourceSqsQueueParametersTypeDef" = (
        dataclasses.field()
    )

    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePipeSourceSqsQueueParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipeSourceSqsQueueParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfigurationOutput:
    boto3_raw_data: "type_defs.NetworkConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def awsvpcConfiguration(self):  # pragma: no cover
        return AwsVpcConfigurationOutput.make_one(
            self.boto3_raw_data["awsvpcConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfiguration:
    boto3_raw_data: "type_defs.NetworkConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def awsvpcConfiguration(self):  # pragma: no cover
        return AwsVpcConfiguration.make_one(self.boto3_raw_data["awsvpcConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchContainerOverridesOutput:
    boto3_raw_data: "type_defs.BatchContainerOverridesOutputTypeDef" = (
        dataclasses.field()
    )

    Command = field("Command")

    @cached_property
    def Environment(self):  # pragma: no cover
        return BatchEnvironmentVariable.make_many(self.boto3_raw_data["Environment"])

    InstanceType = field("InstanceType")

    @cached_property
    def ResourceRequirements(self):  # pragma: no cover
        return BatchResourceRequirement.make_many(
            self.boto3_raw_data["ResourceRequirements"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchContainerOverridesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchContainerOverridesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchContainerOverrides:
    boto3_raw_data: "type_defs.BatchContainerOverridesTypeDef" = dataclasses.field()

    Command = field("Command")

    @cached_property
    def Environment(self):  # pragma: no cover
        return BatchEnvironmentVariable.make_many(self.boto3_raw_data["Environment"])

    InstanceType = field("InstanceType")

    @cached_property
    def ResourceRequirements(self):  # pragma: no cover
        return BatchResourceRequirement.make_many(
            self.boto3_raw_data["ResourceRequirements"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchContainerOverridesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchContainerOverridesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipeResponse:
    boto3_raw_data: "type_defs.CreatePipeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePipeResponse:
    boto3_raw_data: "type_defs.DeletePipeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePipeResponseTypeDef"]
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
class StartPipeResponse:
    boto3_raw_data: "type_defs.StartPipeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartPipeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPipeResponse:
    boto3_raw_data: "type_defs.StopPipeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopPipeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopPipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipeResponse:
    boto3_raw_data: "type_defs.UpdatePipeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceDynamoDBStreamParameters:
    boto3_raw_data: "type_defs.PipeSourceDynamoDBStreamParametersTypeDef" = (
        dataclasses.field()
    )

    StartingPosition = field("StartingPosition")
    BatchSize = field("BatchSize")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    OnPartialBatchItemFailure = field("OnPartialBatchItemFailure")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    MaximumRecordAgeInSeconds = field("MaximumRecordAgeInSeconds")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    ParallelizationFactor = field("ParallelizationFactor")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeSourceDynamoDBStreamParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceDynamoDBStreamParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceKinesisStreamParametersOutput:
    boto3_raw_data: "type_defs.PipeSourceKinesisStreamParametersOutputTypeDef" = (
        dataclasses.field()
    )

    StartingPosition = field("StartingPosition")
    BatchSize = field("BatchSize")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    OnPartialBatchItemFailure = field("OnPartialBatchItemFailure")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    MaximumRecordAgeInSeconds = field("MaximumRecordAgeInSeconds")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    ParallelizationFactor = field("ParallelizationFactor")
    StartingPositionTimestamp = field("StartingPositionTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeSourceKinesisStreamParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceKinesisStreamParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipeSourceDynamoDBStreamParameters:
    boto3_raw_data: "type_defs.UpdatePipeSourceDynamoDBStreamParametersTypeDef" = (
        dataclasses.field()
    )

    BatchSize = field("BatchSize")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    OnPartialBatchItemFailure = field("OnPartialBatchItemFailure")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    MaximumRecordAgeInSeconds = field("MaximumRecordAgeInSeconds")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    ParallelizationFactor = field("ParallelizationFactor")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePipeSourceDynamoDBStreamParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipeSourceDynamoDBStreamParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipeSourceKinesisStreamParameters:
    boto3_raw_data: "type_defs.UpdatePipeSourceKinesisStreamParametersTypeDef" = (
        dataclasses.field()
    )

    BatchSize = field("BatchSize")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    OnPartialBatchItemFailure = field("OnPartialBatchItemFailure")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    MaximumRecordAgeInSeconds = field("MaximumRecordAgeInSeconds")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    ParallelizationFactor = field("ParallelizationFactor")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePipeSourceKinesisStreamParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipeSourceKinesisStreamParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsContainerOverrideOutput:
    boto3_raw_data: "type_defs.EcsContainerOverrideOutputTypeDef" = dataclasses.field()

    Command = field("Command")
    Cpu = field("Cpu")

    @cached_property
    def Environment(self):  # pragma: no cover
        return EcsEnvironmentVariable.make_many(self.boto3_raw_data["Environment"])

    @cached_property
    def EnvironmentFiles(self):  # pragma: no cover
        return EcsEnvironmentFile.make_many(self.boto3_raw_data["EnvironmentFiles"])

    Memory = field("Memory")
    MemoryReservation = field("MemoryReservation")
    Name = field("Name")

    @cached_property
    def ResourceRequirements(self):  # pragma: no cover
        return EcsResourceRequirement.make_many(
            self.boto3_raw_data["ResourceRequirements"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsContainerOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsContainerOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsContainerOverride:
    boto3_raw_data: "type_defs.EcsContainerOverrideTypeDef" = dataclasses.field()

    Command = field("Command")
    Cpu = field("Cpu")

    @cached_property
    def Environment(self):  # pragma: no cover
        return EcsEnvironmentVariable.make_many(self.boto3_raw_data["Environment"])

    @cached_property
    def EnvironmentFiles(self):  # pragma: no cover
        return EcsEnvironmentFile.make_many(self.boto3_raw_data["EnvironmentFiles"])

    Memory = field("Memory")
    MemoryReservation = field("MemoryReservation")
    Name = field("Name")

    @cached_property
    def ResourceRequirements(self):  # pragma: no cover
        return EcsResourceRequirement.make_many(
            self.boto3_raw_data["ResourceRequirements"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsContainerOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsContainerOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriteriaOutput:
    boto3_raw_data: "type_defs.FilterCriteriaOutputTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriteria:
    boto3_raw_data: "type_defs.FilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipesRequestPaginate:
    boto3_raw_data: "type_defs.ListPipesRequestPaginateTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")
    SourcePrefix = field("SourcePrefix")
    TargetPrefix = field("TargetPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipesResponse:
    boto3_raw_data: "type_defs.ListPipesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipes(self):  # pragma: no cover
        return Pipe.make_many(self.boto3_raw_data["Pipes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListPipesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceActiveMQBrokerParameters:
    boto3_raw_data: "type_defs.PipeSourceActiveMQBrokerParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Credentials(self):  # pragma: no cover
        return MQBrokerAccessCredentials.make_one(self.boto3_raw_data["Credentials"])

    QueueName = field("QueueName")
    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeSourceActiveMQBrokerParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceActiveMQBrokerParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceRabbitMQBrokerParameters:
    boto3_raw_data: "type_defs.PipeSourceRabbitMQBrokerParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Credentials(self):  # pragma: no cover
        return MQBrokerAccessCredentials.make_one(self.boto3_raw_data["Credentials"])

    QueueName = field("QueueName")
    VirtualHost = field("VirtualHost")
    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeSourceRabbitMQBrokerParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceRabbitMQBrokerParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipeSourceActiveMQBrokerParameters:
    boto3_raw_data: "type_defs.UpdatePipeSourceActiveMQBrokerParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Credentials(self):  # pragma: no cover
        return MQBrokerAccessCredentials.make_one(self.boto3_raw_data["Credentials"])

    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePipeSourceActiveMQBrokerParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipeSourceActiveMQBrokerParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipeSourceRabbitMQBrokerParameters:
    boto3_raw_data: "type_defs.UpdatePipeSourceRabbitMQBrokerParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Credentials(self):  # pragma: no cover
        return MQBrokerAccessCredentials.make_one(self.boto3_raw_data["Credentials"])

    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePipeSourceRabbitMQBrokerParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipeSourceRabbitMQBrokerParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceManagedStreamingKafkaParameters:
    boto3_raw_data: "type_defs.PipeSourceManagedStreamingKafkaParametersTypeDef" = (
        dataclasses.field()
    )

    TopicName = field("TopicName")
    StartingPosition = field("StartingPosition")
    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    ConsumerGroupID = field("ConsumerGroupID")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return MSKAccessCredentials.make_one(self.boto3_raw_data["Credentials"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeSourceManagedStreamingKafkaParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceManagedStreamingKafkaParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipeSourceManagedStreamingKafkaParameters:
    boto3_raw_data: (
        "type_defs.UpdatePipeSourceManagedStreamingKafkaParametersTypeDef"
    ) = dataclasses.field()

    BatchSize = field("BatchSize")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return MSKAccessCredentials.make_one(self.boto3_raw_data["Credentials"])

    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePipeSourceManagedStreamingKafkaParametersTypeDef"
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
                "type_defs.UpdatePipeSourceManagedStreamingKafkaParametersTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiMeasureMappingOutput:
    boto3_raw_data: "type_defs.MultiMeasureMappingOutputTypeDef" = dataclasses.field()

    MultiMeasureName = field("MultiMeasureName")

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiMeasureMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiMeasureMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiMeasureMapping:
    boto3_raw_data: "type_defs.MultiMeasureMappingTypeDef" = dataclasses.field()

    MultiMeasureName = field("MultiMeasureName")

    @cached_property
    def MultiMeasureAttributeMappings(self):  # pragma: no cover
        return MultiMeasureAttributeMapping.make_many(
            self.boto3_raw_data["MultiMeasureAttributeMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiMeasureMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiMeasureMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeEnrichmentParametersOutput:
    boto3_raw_data: "type_defs.PipeEnrichmentParametersOutputTypeDef" = (
        dataclasses.field()
    )

    InputTemplate = field("InputTemplate")

    @cached_property
    def HttpParameters(self):  # pragma: no cover
        return PipeEnrichmentHttpParametersOutput.make_one(
            self.boto3_raw_data["HttpParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PipeEnrichmentParametersOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeEnrichmentParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeEnrichmentParameters:
    boto3_raw_data: "type_defs.PipeEnrichmentParametersTypeDef" = dataclasses.field()

    InputTemplate = field("InputTemplate")

    @cached_property
    def HttpParameters(self):  # pragma: no cover
        return PipeEnrichmentHttpParameters.make_one(
            self.boto3_raw_data["HttpParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeEnrichmentParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeEnrichmentParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeLogConfigurationParameters:
    boto3_raw_data: "type_defs.PipeLogConfigurationParametersTypeDef" = (
        dataclasses.field()
    )

    Level = field("Level")

    @cached_property
    def S3LogDestination(self):  # pragma: no cover
        return S3LogDestinationParameters.make_one(
            self.boto3_raw_data["S3LogDestination"]
        )

    @cached_property
    def FirehoseLogDestination(self):  # pragma: no cover
        return FirehoseLogDestinationParameters.make_one(
            self.boto3_raw_data["FirehoseLogDestination"]
        )

    @cached_property
    def CloudwatchLogsLogDestination(self):  # pragma: no cover
        return CloudwatchLogsLogDestinationParameters.make_one(
            self.boto3_raw_data["CloudwatchLogsLogDestination"]
        )

    IncludeExecutionData = field("IncludeExecutionData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PipeLogConfigurationParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeLogConfigurationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeLogConfiguration:
    boto3_raw_data: "type_defs.PipeLogConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def S3LogDestination(self):  # pragma: no cover
        return S3LogDestination.make_one(self.boto3_raw_data["S3LogDestination"])

    @cached_property
    def FirehoseLogDestination(self):  # pragma: no cover
        return FirehoseLogDestination.make_one(
            self.boto3_raw_data["FirehoseLogDestination"]
        )

    @cached_property
    def CloudwatchLogsLogDestination(self):  # pragma: no cover
        return CloudwatchLogsLogDestination.make_one(
            self.boto3_raw_data["CloudwatchLogsLogDestination"]
        )

    Level = field("Level")
    IncludeExecutionData = field("IncludeExecutionData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeLogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeLogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceKinesisStreamParameters:
    boto3_raw_data: "type_defs.PipeSourceKinesisStreamParametersTypeDef" = (
        dataclasses.field()
    )

    StartingPosition = field("StartingPosition")
    BatchSize = field("BatchSize")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    OnPartialBatchItemFailure = field("OnPartialBatchItemFailure")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    MaximumRecordAgeInSeconds = field("MaximumRecordAgeInSeconds")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    ParallelizationFactor = field("ParallelizationFactor")
    StartingPositionTimestamp = field("StartingPositionTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeSourceKinesisStreamParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceKinesisStreamParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceSelfManagedKafkaParametersOutput:
    boto3_raw_data: "type_defs.PipeSourceSelfManagedKafkaParametersOutputTypeDef" = (
        dataclasses.field()
    )

    TopicName = field("TopicName")
    StartingPosition = field("StartingPosition")
    AdditionalBootstrapServers = field("AdditionalBootstrapServers")
    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    ConsumerGroupID = field("ConsumerGroupID")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return SelfManagedKafkaAccessConfigurationCredentials.make_one(
            self.boto3_raw_data["Credentials"]
        )

    ServerRootCaCertificate = field("ServerRootCaCertificate")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return SelfManagedKafkaAccessConfigurationVpcOutput.make_one(
            self.boto3_raw_data["Vpc"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeSourceSelfManagedKafkaParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceSelfManagedKafkaParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceSelfManagedKafkaParameters:
    boto3_raw_data: "type_defs.PipeSourceSelfManagedKafkaParametersTypeDef" = (
        dataclasses.field()
    )

    TopicName = field("TopicName")
    StartingPosition = field("StartingPosition")
    AdditionalBootstrapServers = field("AdditionalBootstrapServers")
    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    ConsumerGroupID = field("ConsumerGroupID")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return SelfManagedKafkaAccessConfigurationCredentials.make_one(
            self.boto3_raw_data["Credentials"]
        )

    ServerRootCaCertificate = field("ServerRootCaCertificate")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return SelfManagedKafkaAccessConfigurationVpc.make_one(
            self.boto3_raw_data["Vpc"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeSourceSelfManagedKafkaParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceSelfManagedKafkaParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetSageMakerPipelineParametersOutput:
    boto3_raw_data: "type_defs.PipeTargetSageMakerPipelineParametersOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PipelineParameterList(self):  # pragma: no cover
        return SageMakerPipelineParameter.make_many(
            self.boto3_raw_data["PipelineParameterList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetSageMakerPipelineParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetSageMakerPipelineParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetSageMakerPipelineParameters:
    boto3_raw_data: "type_defs.PipeTargetSageMakerPipelineParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PipelineParameterList(self):  # pragma: no cover
        return SageMakerPipelineParameter.make_many(
            self.boto3_raw_data["PipelineParameterList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetSageMakerPipelineParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetSageMakerPipelineParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetBatchJobParametersOutput:
    boto3_raw_data: "type_defs.PipeTargetBatchJobParametersOutputTypeDef" = (
        dataclasses.field()
    )

    JobDefinition = field("JobDefinition")
    JobName = field("JobName")

    @cached_property
    def ArrayProperties(self):  # pragma: no cover
        return BatchArrayProperties.make_one(self.boto3_raw_data["ArrayProperties"])

    @cached_property
    def RetryStrategy(self):  # pragma: no cover
        return BatchRetryStrategy.make_one(self.boto3_raw_data["RetryStrategy"])

    @cached_property
    def ContainerOverrides(self):  # pragma: no cover
        return BatchContainerOverridesOutput.make_one(
            self.boto3_raw_data["ContainerOverrides"]
        )

    @cached_property
    def DependsOn(self):  # pragma: no cover
        return BatchJobDependency.make_many(self.boto3_raw_data["DependsOn"])

    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetBatchJobParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetBatchJobParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetBatchJobParameters:
    boto3_raw_data: "type_defs.PipeTargetBatchJobParametersTypeDef" = (
        dataclasses.field()
    )

    JobDefinition = field("JobDefinition")
    JobName = field("JobName")

    @cached_property
    def ArrayProperties(self):  # pragma: no cover
        return BatchArrayProperties.make_one(self.boto3_raw_data["ArrayProperties"])

    @cached_property
    def RetryStrategy(self):  # pragma: no cover
        return BatchRetryStrategy.make_one(self.boto3_raw_data["RetryStrategy"])

    @cached_property
    def ContainerOverrides(self):  # pragma: no cover
        return BatchContainerOverrides.make_one(
            self.boto3_raw_data["ContainerOverrides"]
        )

    @cached_property
    def DependsOn(self):  # pragma: no cover
        return BatchJobDependency.make_many(self.boto3_raw_data["DependsOn"])

    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeTargetBatchJobParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetBatchJobParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsTaskOverrideOutput:
    boto3_raw_data: "type_defs.EcsTaskOverrideOutputTypeDef" = dataclasses.field()

    @cached_property
    def ContainerOverrides(self):  # pragma: no cover
        return EcsContainerOverrideOutput.make_many(
            self.boto3_raw_data["ContainerOverrides"]
        )

    Cpu = field("Cpu")

    @cached_property
    def EphemeralStorage(self):  # pragma: no cover
        return EcsEphemeralStorage.make_one(self.boto3_raw_data["EphemeralStorage"])

    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def InferenceAcceleratorOverrides(self):  # pragma: no cover
        return EcsInferenceAcceleratorOverride.make_many(
            self.boto3_raw_data["InferenceAcceleratorOverrides"]
        )

    Memory = field("Memory")
    TaskRoleArn = field("TaskRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsTaskOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsTaskOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsTaskOverride:
    boto3_raw_data: "type_defs.EcsTaskOverrideTypeDef" = dataclasses.field()

    @cached_property
    def ContainerOverrides(self):  # pragma: no cover
        return EcsContainerOverride.make_many(self.boto3_raw_data["ContainerOverrides"])

    Cpu = field("Cpu")

    @cached_property
    def EphemeralStorage(self):  # pragma: no cover
        return EcsEphemeralStorage.make_one(self.boto3_raw_data["EphemeralStorage"])

    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def InferenceAcceleratorOverrides(self):  # pragma: no cover
        return EcsInferenceAcceleratorOverride.make_many(
            self.boto3_raw_data["InferenceAcceleratorOverrides"]
        )

    Memory = field("Memory")
    TaskRoleArn = field("TaskRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsTaskOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EcsTaskOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetTimestreamParametersOutput:
    boto3_raw_data: "type_defs.PipeTargetTimestreamParametersOutputTypeDef" = (
        dataclasses.field()
    )

    TimeValue = field("TimeValue")
    VersionValue = field("VersionValue")

    @cached_property
    def DimensionMappings(self):  # pragma: no cover
        return DimensionMapping.make_many(self.boto3_raw_data["DimensionMappings"])

    EpochTimeUnit = field("EpochTimeUnit")
    TimeFieldType = field("TimeFieldType")
    TimestampFormat = field("TimestampFormat")

    @cached_property
    def SingleMeasureMappings(self):  # pragma: no cover
        return SingleMeasureMapping.make_many(
            self.boto3_raw_data["SingleMeasureMappings"]
        )

    @cached_property
    def MultiMeasureMappings(self):  # pragma: no cover
        return MultiMeasureMappingOutput.make_many(
            self.boto3_raw_data["MultiMeasureMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetTimestreamParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetTimestreamParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetTimestreamParameters:
    boto3_raw_data: "type_defs.PipeTargetTimestreamParametersTypeDef" = (
        dataclasses.field()
    )

    TimeValue = field("TimeValue")
    VersionValue = field("VersionValue")

    @cached_property
    def DimensionMappings(self):  # pragma: no cover
        return DimensionMapping.make_many(self.boto3_raw_data["DimensionMappings"])

    EpochTimeUnit = field("EpochTimeUnit")
    TimeFieldType = field("TimeFieldType")
    TimestampFormat = field("TimestampFormat")

    @cached_property
    def SingleMeasureMappings(self):  # pragma: no cover
        return SingleMeasureMapping.make_many(
            self.boto3_raw_data["SingleMeasureMappings"]
        )

    @cached_property
    def MultiMeasureMappings(self):  # pragma: no cover
        return MultiMeasureMapping.make_many(
            self.boto3_raw_data["MultiMeasureMappings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PipeTargetTimestreamParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetTimestreamParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceParametersOutput:
    boto3_raw_data: "type_defs.PipeSourceParametersOutputTypeDef" = dataclasses.field()

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return FilterCriteriaOutput.make_one(self.boto3_raw_data["FilterCriteria"])

    @cached_property
    def KinesisStreamParameters(self):  # pragma: no cover
        return PipeSourceKinesisStreamParametersOutput.make_one(
            self.boto3_raw_data["KinesisStreamParameters"]
        )

    @cached_property
    def DynamoDBStreamParameters(self):  # pragma: no cover
        return PipeSourceDynamoDBStreamParameters.make_one(
            self.boto3_raw_data["DynamoDBStreamParameters"]
        )

    @cached_property
    def SqsQueueParameters(self):  # pragma: no cover
        return PipeSourceSqsQueueParameters.make_one(
            self.boto3_raw_data["SqsQueueParameters"]
        )

    @cached_property
    def ActiveMQBrokerParameters(self):  # pragma: no cover
        return PipeSourceActiveMQBrokerParameters.make_one(
            self.boto3_raw_data["ActiveMQBrokerParameters"]
        )

    @cached_property
    def RabbitMQBrokerParameters(self):  # pragma: no cover
        return PipeSourceRabbitMQBrokerParameters.make_one(
            self.boto3_raw_data["RabbitMQBrokerParameters"]
        )

    @cached_property
    def ManagedStreamingKafkaParameters(self):  # pragma: no cover
        return PipeSourceManagedStreamingKafkaParameters.make_one(
            self.boto3_raw_data["ManagedStreamingKafkaParameters"]
        )

    @cached_property
    def SelfManagedKafkaParameters(self):  # pragma: no cover
        return PipeSourceSelfManagedKafkaParametersOutput.make_one(
            self.boto3_raw_data["SelfManagedKafkaParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeSourceParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeSourceParameters:
    boto3_raw_data: "type_defs.PipeSourceParametersTypeDef" = dataclasses.field()

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return FilterCriteria.make_one(self.boto3_raw_data["FilterCriteria"])

    @cached_property
    def KinesisStreamParameters(self):  # pragma: no cover
        return PipeSourceKinesisStreamParameters.make_one(
            self.boto3_raw_data["KinesisStreamParameters"]
        )

    @cached_property
    def DynamoDBStreamParameters(self):  # pragma: no cover
        return PipeSourceDynamoDBStreamParameters.make_one(
            self.boto3_raw_data["DynamoDBStreamParameters"]
        )

    @cached_property
    def SqsQueueParameters(self):  # pragma: no cover
        return PipeSourceSqsQueueParameters.make_one(
            self.boto3_raw_data["SqsQueueParameters"]
        )

    @cached_property
    def ActiveMQBrokerParameters(self):  # pragma: no cover
        return PipeSourceActiveMQBrokerParameters.make_one(
            self.boto3_raw_data["ActiveMQBrokerParameters"]
        )

    @cached_property
    def RabbitMQBrokerParameters(self):  # pragma: no cover
        return PipeSourceRabbitMQBrokerParameters.make_one(
            self.boto3_raw_data["RabbitMQBrokerParameters"]
        )

    @cached_property
    def ManagedStreamingKafkaParameters(self):  # pragma: no cover
        return PipeSourceManagedStreamingKafkaParameters.make_one(
            self.boto3_raw_data["ManagedStreamingKafkaParameters"]
        )

    @cached_property
    def SelfManagedKafkaParameters(self):  # pragma: no cover
        return PipeSourceSelfManagedKafkaParameters.make_one(
            self.boto3_raw_data["SelfManagedKafkaParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeSourceParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeSourceParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipeSourceSelfManagedKafkaParameters:
    boto3_raw_data: "type_defs.UpdatePipeSourceSelfManagedKafkaParametersTypeDef" = (
        dataclasses.field()
    )

    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return SelfManagedKafkaAccessConfigurationCredentials.make_one(
            self.boto3_raw_data["Credentials"]
        )

    ServerRootCaCertificate = field("ServerRootCaCertificate")
    Vpc = field("Vpc")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePipeSourceSelfManagedKafkaParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipeSourceSelfManagedKafkaParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetEcsTaskParametersOutput:
    boto3_raw_data: "type_defs.PipeTargetEcsTaskParametersOutputTypeDef" = (
        dataclasses.field()
    )

    TaskDefinitionArn = field("TaskDefinitionArn")
    TaskCount = field("TaskCount")
    LaunchType = field("LaunchType")

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    PlatformVersion = field("PlatformVersion")
    Group = field("Group")

    @cached_property
    def CapacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["CapacityProviderStrategy"]
        )

    EnableECSManagedTags = field("EnableECSManagedTags")
    EnableExecuteCommand = field("EnableExecuteCommand")

    @cached_property
    def PlacementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["PlacementConstraints"]
        )

    @cached_property
    def PlacementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["PlacementStrategy"])

    PropagateTags = field("PropagateTags")
    ReferenceId = field("ReferenceId")

    @cached_property
    def Overrides(self):  # pragma: no cover
        return EcsTaskOverrideOutput.make_one(self.boto3_raw_data["Overrides"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PipeTargetEcsTaskParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetEcsTaskParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetEcsTaskParameters:
    boto3_raw_data: "type_defs.PipeTargetEcsTaskParametersTypeDef" = dataclasses.field()

    TaskDefinitionArn = field("TaskDefinitionArn")
    TaskCount = field("TaskCount")
    LaunchType = field("LaunchType")

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    PlatformVersion = field("PlatformVersion")
    Group = field("Group")

    @cached_property
    def CapacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["CapacityProviderStrategy"]
        )

    EnableECSManagedTags = field("EnableECSManagedTags")
    EnableExecuteCommand = field("EnableExecuteCommand")

    @cached_property
    def PlacementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["PlacementConstraints"]
        )

    @cached_property
    def PlacementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["PlacementStrategy"])

    PropagateTags = field("PropagateTags")
    ReferenceId = field("ReferenceId")

    @cached_property
    def Overrides(self):  # pragma: no cover
        return EcsTaskOverride.make_one(self.boto3_raw_data["Overrides"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeTargetEcsTaskParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetEcsTaskParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipeSourceParameters:
    boto3_raw_data: "type_defs.UpdatePipeSourceParametersTypeDef" = dataclasses.field()

    FilterCriteria = field("FilterCriteria")

    @cached_property
    def KinesisStreamParameters(self):  # pragma: no cover
        return UpdatePipeSourceKinesisStreamParameters.make_one(
            self.boto3_raw_data["KinesisStreamParameters"]
        )

    @cached_property
    def DynamoDBStreamParameters(self):  # pragma: no cover
        return UpdatePipeSourceDynamoDBStreamParameters.make_one(
            self.boto3_raw_data["DynamoDBStreamParameters"]
        )

    @cached_property
    def SqsQueueParameters(self):  # pragma: no cover
        return UpdatePipeSourceSqsQueueParameters.make_one(
            self.boto3_raw_data["SqsQueueParameters"]
        )

    @cached_property
    def ActiveMQBrokerParameters(self):  # pragma: no cover
        return UpdatePipeSourceActiveMQBrokerParameters.make_one(
            self.boto3_raw_data["ActiveMQBrokerParameters"]
        )

    @cached_property
    def RabbitMQBrokerParameters(self):  # pragma: no cover
        return UpdatePipeSourceRabbitMQBrokerParameters.make_one(
            self.boto3_raw_data["RabbitMQBrokerParameters"]
        )

    @cached_property
    def ManagedStreamingKafkaParameters(self):  # pragma: no cover
        return UpdatePipeSourceManagedStreamingKafkaParameters.make_one(
            self.boto3_raw_data["ManagedStreamingKafkaParameters"]
        )

    @cached_property
    def SelfManagedKafkaParameters(self):  # pragma: no cover
        return UpdatePipeSourceSelfManagedKafkaParameters.make_one(
            self.boto3_raw_data["SelfManagedKafkaParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipeSourceParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipeSourceParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetParametersOutput:
    boto3_raw_data: "type_defs.PipeTargetParametersOutputTypeDef" = dataclasses.field()

    InputTemplate = field("InputTemplate")

    @cached_property
    def LambdaFunctionParameters(self):  # pragma: no cover
        return PipeTargetLambdaFunctionParameters.make_one(
            self.boto3_raw_data["LambdaFunctionParameters"]
        )

    @cached_property
    def StepFunctionStateMachineParameters(self):  # pragma: no cover
        return PipeTargetStateMachineParameters.make_one(
            self.boto3_raw_data["StepFunctionStateMachineParameters"]
        )

    @cached_property
    def KinesisStreamParameters(self):  # pragma: no cover
        return PipeTargetKinesisStreamParameters.make_one(
            self.boto3_raw_data["KinesisStreamParameters"]
        )

    @cached_property
    def EcsTaskParameters(self):  # pragma: no cover
        return PipeTargetEcsTaskParametersOutput.make_one(
            self.boto3_raw_data["EcsTaskParameters"]
        )

    @cached_property
    def BatchJobParameters(self):  # pragma: no cover
        return PipeTargetBatchJobParametersOutput.make_one(
            self.boto3_raw_data["BatchJobParameters"]
        )

    @cached_property
    def SqsQueueParameters(self):  # pragma: no cover
        return PipeTargetSqsQueueParameters.make_one(
            self.boto3_raw_data["SqsQueueParameters"]
        )

    @cached_property
    def HttpParameters(self):  # pragma: no cover
        return PipeTargetHttpParametersOutput.make_one(
            self.boto3_raw_data["HttpParameters"]
        )

    @cached_property
    def RedshiftDataParameters(self):  # pragma: no cover
        return PipeTargetRedshiftDataParametersOutput.make_one(
            self.boto3_raw_data["RedshiftDataParameters"]
        )

    @cached_property
    def SageMakerPipelineParameters(self):  # pragma: no cover
        return PipeTargetSageMakerPipelineParametersOutput.make_one(
            self.boto3_raw_data["SageMakerPipelineParameters"]
        )

    @cached_property
    def EventBridgeEventBusParameters(self):  # pragma: no cover
        return PipeTargetEventBridgeEventBusParametersOutput.make_one(
            self.boto3_raw_data["EventBridgeEventBusParameters"]
        )

    @cached_property
    def CloudWatchLogsParameters(self):  # pragma: no cover
        return PipeTargetCloudWatchLogsParameters.make_one(
            self.boto3_raw_data["CloudWatchLogsParameters"]
        )

    @cached_property
    def TimestreamParameters(self):  # pragma: no cover
        return PipeTargetTimestreamParametersOutput.make_one(
            self.boto3_raw_data["TimestreamParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeTargetParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipeTargetParameters:
    boto3_raw_data: "type_defs.PipeTargetParametersTypeDef" = dataclasses.field()

    InputTemplate = field("InputTemplate")

    @cached_property
    def LambdaFunctionParameters(self):  # pragma: no cover
        return PipeTargetLambdaFunctionParameters.make_one(
            self.boto3_raw_data["LambdaFunctionParameters"]
        )

    @cached_property
    def StepFunctionStateMachineParameters(self):  # pragma: no cover
        return PipeTargetStateMachineParameters.make_one(
            self.boto3_raw_data["StepFunctionStateMachineParameters"]
        )

    @cached_property
    def KinesisStreamParameters(self):  # pragma: no cover
        return PipeTargetKinesisStreamParameters.make_one(
            self.boto3_raw_data["KinesisStreamParameters"]
        )

    @cached_property
    def EcsTaskParameters(self):  # pragma: no cover
        return PipeTargetEcsTaskParameters.make_one(
            self.boto3_raw_data["EcsTaskParameters"]
        )

    @cached_property
    def BatchJobParameters(self):  # pragma: no cover
        return PipeTargetBatchJobParameters.make_one(
            self.boto3_raw_data["BatchJobParameters"]
        )

    @cached_property
    def SqsQueueParameters(self):  # pragma: no cover
        return PipeTargetSqsQueueParameters.make_one(
            self.boto3_raw_data["SqsQueueParameters"]
        )

    @cached_property
    def HttpParameters(self):  # pragma: no cover
        return PipeTargetHttpParameters.make_one(self.boto3_raw_data["HttpParameters"])

    @cached_property
    def RedshiftDataParameters(self):  # pragma: no cover
        return PipeTargetRedshiftDataParameters.make_one(
            self.boto3_raw_data["RedshiftDataParameters"]
        )

    @cached_property
    def SageMakerPipelineParameters(self):  # pragma: no cover
        return PipeTargetSageMakerPipelineParameters.make_one(
            self.boto3_raw_data["SageMakerPipelineParameters"]
        )

    @cached_property
    def EventBridgeEventBusParameters(self):  # pragma: no cover
        return PipeTargetEventBridgeEventBusParameters.make_one(
            self.boto3_raw_data["EventBridgeEventBusParameters"]
        )

    @cached_property
    def CloudWatchLogsParameters(self):  # pragma: no cover
        return PipeTargetCloudWatchLogsParameters.make_one(
            self.boto3_raw_data["CloudWatchLogsParameters"]
        )

    @cached_property
    def TimestreamParameters(self):  # pragma: no cover
        return PipeTargetTimestreamParameters.make_one(
            self.boto3_raw_data["TimestreamParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipeTargetParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipeTargetParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePipeResponse:
    boto3_raw_data: "type_defs.DescribePipeResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")
    StateReason = field("StateReason")
    Source = field("Source")

    @cached_property
    def SourceParameters(self):  # pragma: no cover
        return PipeSourceParametersOutput.make_one(
            self.boto3_raw_data["SourceParameters"]
        )

    Enrichment = field("Enrichment")

    @cached_property
    def EnrichmentParameters(self):  # pragma: no cover
        return PipeEnrichmentParametersOutput.make_one(
            self.boto3_raw_data["EnrichmentParameters"]
        )

    Target = field("Target")

    @cached_property
    def TargetParameters(self):  # pragma: no cover
        return PipeTargetParametersOutput.make_one(
            self.boto3_raw_data["TargetParameters"]
        )

    RoleArn = field("RoleArn")
    Tags = field("Tags")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return PipeLogConfiguration.make_one(self.boto3_raw_data["LogConfiguration"])

    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipeRequest:
    boto3_raw_data: "type_defs.CreatePipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Source = field("Source")
    Target = field("Target")
    RoleArn = field("RoleArn")
    Description = field("Description")
    DesiredState = field("DesiredState")
    SourceParameters = field("SourceParameters")
    Enrichment = field("Enrichment")
    EnrichmentParameters = field("EnrichmentParameters")
    TargetParameters = field("TargetParameters")
    Tags = field("Tags")

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return PipeLogConfigurationParameters.make_one(
            self.boto3_raw_data["LogConfiguration"]
        )

    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreatePipeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipeRequest:
    boto3_raw_data: "type_defs.UpdatePipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RoleArn = field("RoleArn")
    Description = field("Description")
    DesiredState = field("DesiredState")

    @cached_property
    def SourceParameters(self):  # pragma: no cover
        return UpdatePipeSourceParameters.make_one(
            self.boto3_raw_data["SourceParameters"]
        )

    Enrichment = field("Enrichment")
    EnrichmentParameters = field("EnrichmentParameters")
    Target = field("Target")
    TargetParameters = field("TargetParameters")

    @cached_property
    def LogConfiguration(self):  # pragma: no cover
        return PipeLogConfigurationParameters.make_one(
            self.boto3_raw_data["LogConfiguration"]
        )

    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdatePipeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
