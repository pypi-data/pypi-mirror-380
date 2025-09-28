# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_scheduler import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AwsVpcConfigurationOutput:
    boto3_raw_data: "type_defs.AwsVpcConfigurationOutputTypeDef" = dataclasses.field()

    Subnets = field("Subnets")
    AssignPublicIp = field("AssignPublicIp")
    SecurityGroups = field("SecurityGroups")

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
    AssignPublicIp = field("AssignPublicIp")
    SecurityGroups = field("SecurityGroups")

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
class CapacityProviderStrategyItem:
    boto3_raw_data: "type_defs.CapacityProviderStrategyItemTypeDef" = (
        dataclasses.field()
    )

    capacityProvider = field("capacityProvider")
    base = field("base")
    weight = field("weight")

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
class FlexibleTimeWindow:
    boto3_raw_data: "type_defs.FlexibleTimeWindowTypeDef" = dataclasses.field()

    Mode = field("Mode")
    MaximumWindowInMinutes = field("MaximumWindowInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlexibleTimeWindowTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlexibleTimeWindowTypeDef"]
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
class DeleteScheduleGroupInput:
    boto3_raw_data: "type_defs.DeleteScheduleGroupInputTypeDef" = dataclasses.field()

    Name = field("Name")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduleGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduleGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduleInput:
    boto3_raw_data: "type_defs.DeleteScheduleInputTypeDef" = dataclasses.field()

    Name = field("Name")
    ClientToken = field("ClientToken")
    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduleInputTypeDef"]
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

    expression = field("expression")
    type = field("type")

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

    field = field("field")
    type = field("type")

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
class EventBridgeParameters:
    boto3_raw_data: "type_defs.EventBridgeParametersTypeDef" = dataclasses.field()

    DetailType = field("DetailType")
    Source = field("Source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventBridgeParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetScheduleGroupInput:
    boto3_raw_data: "type_defs.GetScheduleGroupInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetScheduleGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetScheduleGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetScheduleInput:
    boto3_raw_data: "type_defs.GetScheduleInputTypeDef" = dataclasses.field()

    Name = field("Name")
    GroupName = field("GroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetScheduleInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetScheduleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisParameters:
    boto3_raw_data: "type_defs.KinesisParametersTypeDef" = dataclasses.field()

    PartitionKey = field("PartitionKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KinesisParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisParametersTypeDef"]
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
class ListScheduleGroupsInput:
    boto3_raw_data: "type_defs.ListScheduleGroupsInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NamePrefix = field("NamePrefix")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScheduleGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduleGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleGroupSummary:
    boto3_raw_data: "type_defs.ScheduleGroupSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationDate = field("CreationDate")
    LastModificationDate = field("LastModificationDate")
    Name = field("Name")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchedulesInput:
    boto3_raw_data: "type_defs.ListSchedulesInputTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    MaxResults = field("MaxResults")
    NamePrefix = field("NamePrefix")
    NextToken = field("NextToken")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchedulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchedulesInputTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class RetryPolicy:
    boto3_raw_data: "type_defs.RetryPolicyTypeDef" = dataclasses.field()

    MaximumEventAgeInSeconds = field("MaximumEventAgeInSeconds")
    MaximumRetryAttempts = field("MaximumRetryAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetryPolicyTypeDef"]]
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
class TargetSummary:
    boto3_raw_data: "type_defs.TargetSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqsParameters:
    boto3_raw_data: "type_defs.SqsParametersTypeDef" = dataclasses.field()

    MessageGroupId = field("MessageGroupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SqsParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SqsParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
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
class CreateScheduleGroupInput:
    boto3_raw_data: "type_defs.CreateScheduleGroupInputTypeDef" = dataclasses.field()

    Name = field("Name")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduleGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduleGroupInputTypeDef"]
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

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateScheduleGroupOutput:
    boto3_raw_data: "type_defs.CreateScheduleGroupOutputTypeDef" = dataclasses.field()

    ScheduleGroupArn = field("ScheduleGroupArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduleGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduleGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduleOutput:
    boto3_raw_data: "type_defs.CreateScheduleOutputTypeDef" = dataclasses.field()

    ScheduleArn = field("ScheduleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetScheduleGroupOutput:
    boto3_raw_data: "type_defs.GetScheduleGroupOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationDate = field("CreationDate")
    LastModificationDate = field("LastModificationDate")
    Name = field("Name")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetScheduleGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetScheduleGroupOutputTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class UpdateScheduleOutput:
    boto3_raw_data: "type_defs.UpdateScheduleOutputTypeDef" = dataclasses.field()

    ScheduleArn = field("ScheduleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScheduleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScheduleGroupsInputPaginate:
    boto3_raw_data: "type_defs.ListScheduleGroupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    NamePrefix = field("NamePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListScheduleGroupsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduleGroupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchedulesInputPaginate:
    boto3_raw_data: "type_defs.ListSchedulesInputPaginateTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    NamePrefix = field("NamePrefix")
    State = field("State")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchedulesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchedulesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScheduleGroupsOutput:
    boto3_raw_data: "type_defs.ListScheduleGroupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ScheduleGroups(self):  # pragma: no cover
        return ScheduleGroupSummary.make_many(self.boto3_raw_data["ScheduleGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScheduleGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduleGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerPipelineParametersOutput:
    boto3_raw_data: "type_defs.SageMakerPipelineParametersOutputTypeDef" = (
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
            "type_defs.SageMakerPipelineParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerPipelineParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerPipelineParameters:
    boto3_raw_data: "type_defs.SageMakerPipelineParametersTypeDef" = dataclasses.field()

    @cached_property
    def PipelineParameterList(self):  # pragma: no cover
        return SageMakerPipelineParameter.make_many(
            self.boto3_raw_data["PipelineParameterList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SageMakerPipelineParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerPipelineParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleSummary:
    boto3_raw_data: "type_defs.ScheduleSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationDate = field("CreationDate")
    GroupName = field("GroupName")
    LastModificationDate = field("LastModificationDate")
    Name = field("Name")
    State = field("State")

    @cached_property
    def Target(self):  # pragma: no cover
        return TargetSummary.make_one(self.boto3_raw_data["Target"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsParametersOutput:
    boto3_raw_data: "type_defs.EcsParametersOutputTypeDef" = dataclasses.field()

    TaskDefinitionArn = field("TaskDefinitionArn")

    @cached_property
    def CapacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["CapacityProviderStrategy"]
        )

    EnableECSManagedTags = field("EnableECSManagedTags")
    EnableExecuteCommand = field("EnableExecuteCommand")
    Group = field("Group")
    LaunchType = field("LaunchType")

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    @cached_property
    def PlacementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["PlacementConstraints"]
        )

    @cached_property
    def PlacementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["PlacementStrategy"])

    PlatformVersion = field("PlatformVersion")
    PropagateTags = field("PropagateTags")
    ReferenceId = field("ReferenceId")
    Tags = field("Tags")
    TaskCount = field("TaskCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsParameters:
    boto3_raw_data: "type_defs.EcsParametersTypeDef" = dataclasses.field()

    TaskDefinitionArn = field("TaskDefinitionArn")

    @cached_property
    def CapacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["CapacityProviderStrategy"]
        )

    EnableECSManagedTags = field("EnableECSManagedTags")
    EnableExecuteCommand = field("EnableExecuteCommand")
    Group = field("Group")
    LaunchType = field("LaunchType")

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    @cached_property
    def PlacementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["PlacementConstraints"]
        )

    @cached_property
    def PlacementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["PlacementStrategy"])

    PlatformVersion = field("PlatformVersion")
    PropagateTags = field("PropagateTags")
    ReferenceId = field("ReferenceId")
    Tags = field("Tags")
    TaskCount = field("TaskCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EcsParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchedulesOutput:
    boto3_raw_data: "type_defs.ListSchedulesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Schedules(self):  # pragma: no cover
        return ScheduleSummary.make_many(self.boto3_raw_data["Schedules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchedulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchedulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetOutput:
    boto3_raw_data: "type_defs.TargetOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    RoleArn = field("RoleArn")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def EcsParameters(self):  # pragma: no cover
        return EcsParametersOutput.make_one(self.boto3_raw_data["EcsParameters"])

    @cached_property
    def EventBridgeParameters(self):  # pragma: no cover
        return EventBridgeParameters.make_one(
            self.boto3_raw_data["EventBridgeParameters"]
        )

    Input = field("Input")

    @cached_property
    def KinesisParameters(self):  # pragma: no cover
        return KinesisParameters.make_one(self.boto3_raw_data["KinesisParameters"])

    @cached_property
    def RetryPolicy(self):  # pragma: no cover
        return RetryPolicy.make_one(self.boto3_raw_data["RetryPolicy"])

    @cached_property
    def SageMakerPipelineParameters(self):  # pragma: no cover
        return SageMakerPipelineParametersOutput.make_one(
            self.boto3_raw_data["SageMakerPipelineParameters"]
        )

    @cached_property
    def SqsParameters(self):  # pragma: no cover
        return SqsParameters.make_one(self.boto3_raw_data["SqsParameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Target:
    boto3_raw_data: "type_defs.TargetTypeDef" = dataclasses.field()

    Arn = field("Arn")
    RoleArn = field("RoleArn")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def EcsParameters(self):  # pragma: no cover
        return EcsParameters.make_one(self.boto3_raw_data["EcsParameters"])

    @cached_property
    def EventBridgeParameters(self):  # pragma: no cover
        return EventBridgeParameters.make_one(
            self.boto3_raw_data["EventBridgeParameters"]
        )

    Input = field("Input")

    @cached_property
    def KinesisParameters(self):  # pragma: no cover
        return KinesisParameters.make_one(self.boto3_raw_data["KinesisParameters"])

    @cached_property
    def RetryPolicy(self):  # pragma: no cover
        return RetryPolicy.make_one(self.boto3_raw_data["RetryPolicy"])

    @cached_property
    def SageMakerPipelineParameters(self):  # pragma: no cover
        return SageMakerPipelineParameters.make_one(
            self.boto3_raw_data["SageMakerPipelineParameters"]
        )

    @cached_property
    def SqsParameters(self):  # pragma: no cover
        return SqsParameters.make_one(self.boto3_raw_data["SqsParameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetScheduleOutput:
    boto3_raw_data: "type_defs.GetScheduleOutputTypeDef" = dataclasses.field()

    ActionAfterCompletion = field("ActionAfterCompletion")
    Arn = field("Arn")
    CreationDate = field("CreationDate")
    Description = field("Description")
    EndDate = field("EndDate")

    @cached_property
    def FlexibleTimeWindow(self):  # pragma: no cover
        return FlexibleTimeWindow.make_one(self.boto3_raw_data["FlexibleTimeWindow"])

    GroupName = field("GroupName")
    KmsKeyArn = field("KmsKeyArn")
    LastModificationDate = field("LastModificationDate")
    Name = field("Name")
    ScheduleExpression = field("ScheduleExpression")
    ScheduleExpressionTimezone = field("ScheduleExpressionTimezone")
    StartDate = field("StartDate")
    State = field("State")

    @cached_property
    def Target(self):  # pragma: no cover
        return TargetOutput.make_one(self.boto3_raw_data["Target"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetScheduleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduleInput:
    boto3_raw_data: "type_defs.CreateScheduleInputTypeDef" = dataclasses.field()

    @cached_property
    def FlexibleTimeWindow(self):  # pragma: no cover
        return FlexibleTimeWindow.make_one(self.boto3_raw_data["FlexibleTimeWindow"])

    Name = field("Name")
    ScheduleExpression = field("ScheduleExpression")
    Target = field("Target")
    ActionAfterCompletion = field("ActionAfterCompletion")
    ClientToken = field("ClientToken")
    Description = field("Description")
    EndDate = field("EndDate")
    GroupName = field("GroupName")
    KmsKeyArn = field("KmsKeyArn")
    ScheduleExpressionTimezone = field("ScheduleExpressionTimezone")
    StartDate = field("StartDate")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScheduleInput:
    boto3_raw_data: "type_defs.UpdateScheduleInputTypeDef" = dataclasses.field()

    @cached_property
    def FlexibleTimeWindow(self):  # pragma: no cover
        return FlexibleTimeWindow.make_one(self.boto3_raw_data["FlexibleTimeWindow"])

    Name = field("Name")
    ScheduleExpression = field("ScheduleExpression")
    Target = field("Target")
    ActionAfterCompletion = field("ActionAfterCompletion")
    ClientToken = field("ClientToken")
    Description = field("Description")
    EndDate = field("EndDate")
    GroupName = field("GroupName")
    KmsKeyArn = field("KmsKeyArn")
    ScheduleExpressionTimezone = field("ScheduleExpressionTimezone")
    StartDate = field("StartDate")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScheduleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScheduleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
