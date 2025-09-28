# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_osis import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BufferOptions:
    boto3_raw_data: "type_defs.BufferOptionsTypeDef" = dataclasses.field()

    PersistentBufferEnabled = field("PersistentBufferEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BufferOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BufferOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeProgressStage:
    boto3_raw_data: "type_defs.ChangeProgressStageTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    Description = field("Description")
    LastUpdatedAt = field("LastUpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeProgressStageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeProgressStageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogDestination:
    boto3_raw_data: "type_defs.CloudWatchLogDestinationTypeDef" = dataclasses.field()

    LogGroup = field("LogGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogDestinationTypeDef"]
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
class EncryptionAtRestOptions:
    boto3_raw_data: "type_defs.EncryptionAtRestOptionsTypeDef" = dataclasses.field()

    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionAtRestOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionAtRestOptionsTypeDef"]
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
class DeletePipelineEndpointRequest:
    boto3_raw_data: "type_defs.DeletePipelineEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    EndpointId = field("EndpointId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePipelineEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePipelineEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePipelineRequest:
    boto3_raw_data: "type_defs.DeletePipelineRequestTypeDef" = dataclasses.field()

    PipelineName = field("PipelineName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineBlueprintRequest:
    boto3_raw_data: "type_defs.GetPipelineBlueprintRequestTypeDef" = dataclasses.field()

    BlueprintName = field("BlueprintName")
    Format = field("Format")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineBlueprintRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineBlueprintRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineBlueprint:
    boto3_raw_data: "type_defs.PipelineBlueprintTypeDef" = dataclasses.field()

    BlueprintName = field("BlueprintName")
    PipelineConfigurationBody = field("PipelineConfigurationBody")
    DisplayName = field("DisplayName")
    DisplayDescription = field("DisplayDescription")
    Service = field("Service")
    UseCase = field("UseCase")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineBlueprintTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineBlueprintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineChangeProgressRequest:
    boto3_raw_data: "type_defs.GetPipelineChangeProgressRequestTypeDef" = (
        dataclasses.field()
    )

    PipelineName = field("PipelineName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPipelineChangeProgressRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineChangeProgressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineRequest:
    boto3_raw_data: "type_defs.GetPipelineRequestTypeDef" = dataclasses.field()

    PipelineName = field("PipelineName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineBlueprintSummary:
    boto3_raw_data: "type_defs.PipelineBlueprintSummaryTypeDef" = dataclasses.field()

    BlueprintName = field("BlueprintName")
    DisplayName = field("DisplayName")
    DisplayDescription = field("DisplayDescription")
    Service = field("Service")
    UseCase = field("UseCase")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineBlueprintSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineBlueprintSummaryTypeDef"]
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
class ListPipelineEndpointConnectionsRequest:
    boto3_raw_data: "type_defs.ListPipelineEndpointConnectionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPipelineEndpointConnectionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelineEndpointConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineEndpointConnection:
    boto3_raw_data: "type_defs.PipelineEndpointConnectionTypeDef" = dataclasses.field()

    PipelineArn = field("PipelineArn")
    EndpointId = field("EndpointId")
    Status = field("Status")
    VpcEndpointOwner = field("VpcEndpointOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineEndpointConnectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineEndpointConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelineEndpointsRequest:
    boto3_raw_data: "type_defs.ListPipelineEndpointsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelineEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelineEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesRequest:
    boto3_raw_data: "type_defs.ListPipelinesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesRequestTypeDef"]
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

    Arn = field("Arn")

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
class PipelineDestination:
    boto3_raw_data: "type_defs.PipelineDestinationTypeDef" = dataclasses.field()

    ServiceName = field("ServiceName")
    Endpoint = field("Endpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineEndpointVpcOptionsOutput:
    boto3_raw_data: "type_defs.PipelineEndpointVpcOptionsOutputTypeDef" = (
        dataclasses.field()
    )

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PipelineEndpointVpcOptionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineEndpointVpcOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineEndpointVpcOptions:
    boto3_raw_data: "type_defs.PipelineEndpointVpcOptionsTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineEndpointVpcOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineEndpointVpcOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineStatusReason:
    boto3_raw_data: "type_defs.PipelineStatusReasonTypeDef" = dataclasses.field()

    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineStatusReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineStatusReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceVpcEndpoint:
    boto3_raw_data: "type_defs.ServiceVpcEndpointTypeDef" = dataclasses.field()

    ServiceName = field("ServiceName")
    VpcEndpointId = field("VpcEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceVpcEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceVpcEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokePipelineEndpointConnectionsRequest:
    boto3_raw_data: "type_defs.RevokePipelineEndpointConnectionsRequestTypeDef" = (
        dataclasses.field()
    )

    PipelineArn = field("PipelineArn")
    EndpointIds = field("EndpointIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RevokePipelineEndpointConnectionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokePipelineEndpointConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPipelineRequest:
    boto3_raw_data: "type_defs.StartPipelineRequestTypeDef" = dataclasses.field()

    PipelineName = field("PipelineName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPipelineRequest:
    boto3_raw_data: "type_defs.StopPipelineRequestTypeDef" = dataclasses.field()

    PipelineName = field("PipelineName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopPipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopPipelineRequestTypeDef"]
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

    Arn = field("Arn")
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
class ValidatePipelineRequest:
    boto3_raw_data: "type_defs.ValidatePipelineRequestTypeDef" = dataclasses.field()

    PipelineConfigurationBody = field("PipelineConfigurationBody")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidatePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationMessage:
    boto3_raw_data: "type_defs.ValidationMessageTypeDef" = dataclasses.field()

    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidationMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcAttachmentOptions:
    boto3_raw_data: "type_defs.VpcAttachmentOptionsTypeDef" = dataclasses.field()

    AttachToVpc = field("AttachToVpc")
    CidrBlock = field("CidrBlock")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcAttachmentOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcAttachmentOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeProgressStatus:
    boto3_raw_data: "type_defs.ChangeProgressStatusTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    Status = field("Status")
    TotalNumberOfStages = field("TotalNumberOfStages")

    @cached_property
    def ChangeProgressStages(self):  # pragma: no cover
        return ChangeProgressStage.make_many(
            self.boto3_raw_data["ChangeProgressStages"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeProgressStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeProgressStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogPublishingOptions:
    boto3_raw_data: "type_defs.LogPublishingOptionsTypeDef" = dataclasses.field()

    IsLoggingEnabled = field("IsLoggingEnabled")

    @cached_property
    def CloudWatchLogDestination(self):  # pragma: no cover
        return CloudWatchLogDestination.make_one(
            self.boto3_raw_data["CloudWatchLogDestination"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogPublishingOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogPublishingOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineEndpointResponse:
    boto3_raw_data: "type_defs.CreatePipelineEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    PipelineArn = field("PipelineArn")
    EndpointId = field("EndpointId")
    Status = field("Status")
    VpcId = field("VpcId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePipelineEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyResponse:
    boto3_raw_data: "type_defs.GetResourcePolicyResponseTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyResponse:
    boto3_raw_data: "type_defs.PutResourcePolicyResponseTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokePipelineEndpointConnectionsResponse:
    boto3_raw_data: "type_defs.RevokePipelineEndpointConnectionsResponseTypeDef" = (
        dataclasses.field()
    )

    PipelineArn = field("PipelineArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RevokePipelineEndpointConnectionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokePipelineEndpointConnectionsResponseTypeDef"]
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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")

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
class GetPipelineBlueprintResponse:
    boto3_raw_data: "type_defs.GetPipelineBlueprintResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Blueprint(self):  # pragma: no cover
        return PipelineBlueprint.make_one(self.boto3_raw_data["Blueprint"])

    Format = field("Format")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineBlueprintResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineBlueprintResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelineBlueprintsResponse:
    boto3_raw_data: "type_defs.ListPipelineBlueprintsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Blueprints(self):  # pragma: no cover
        return PipelineBlueprintSummary.make_many(self.boto3_raw_data["Blueprints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPipelineBlueprintsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelineBlueprintsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelineEndpointConnectionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListPipelineEndpointConnectionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPipelineEndpointConnectionsRequestPaginateTypeDef"
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
                "type_defs.ListPipelineEndpointConnectionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelineEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListPipelineEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPipelineEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelineEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelineEndpointConnectionsResponse:
    boto3_raw_data: "type_defs.ListPipelineEndpointConnectionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PipelineEndpointConnections(self):  # pragma: no cover
        return PipelineEndpointConnection.make_many(
            self.boto3_raw_data["PipelineEndpointConnections"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPipelineEndpointConnectionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelineEndpointConnectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineEndpoint:
    boto3_raw_data: "type_defs.PipelineEndpointTypeDef" = dataclasses.field()

    PipelineArn = field("PipelineArn")
    EndpointId = field("EndpointId")
    Status = field("Status")
    VpcId = field("VpcId")

    @cached_property
    def VpcOptions(self):  # pragma: no cover
        return PipelineEndpointVpcOptionsOutput.make_one(
            self.boto3_raw_data["VpcOptions"]
        )

    IngestEndpointUrl = field("IngestEndpointUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineSummary:
    boto3_raw_data: "type_defs.PipelineSummaryTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def StatusReason(self):  # pragma: no cover
        return PipelineStatusReason.make_one(self.boto3_raw_data["StatusReason"])

    PipelineName = field("PipelineName")
    PipelineArn = field("PipelineArn")
    MinUnits = field("MinUnits")
    MaxUnits = field("MaxUnits")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return PipelineDestination.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidatePipelineResponse:
    boto3_raw_data: "type_defs.ValidatePipelineResponseTypeDef" = dataclasses.field()

    isValid = field("isValid")

    @cached_property
    def Errors(self):  # pragma: no cover
        return ValidationMessage.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidatePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOptionsOutput:
    boto3_raw_data: "type_defs.VpcOptionsOutputTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @cached_property
    def VpcAttachmentOptions(self):  # pragma: no cover
        return VpcAttachmentOptions.make_one(
            self.boto3_raw_data["VpcAttachmentOptions"]
        )

    VpcEndpointManagement = field("VpcEndpointManagement")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcOptionsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOptions:
    boto3_raw_data: "type_defs.VpcOptionsTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @cached_property
    def VpcAttachmentOptions(self):  # pragma: no cover
        return VpcAttachmentOptions.make_one(
            self.boto3_raw_data["VpcAttachmentOptions"]
        )

    VpcEndpointManagement = field("VpcEndpointManagement")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineChangeProgressResponse:
    boto3_raw_data: "type_defs.GetPipelineChangeProgressResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChangeProgressStatuses(self):  # pragma: no cover
        return ChangeProgressStatus.make_many(
            self.boto3_raw_data["ChangeProgressStatuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPipelineChangeProgressResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineChangeProgressResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineRequest:
    boto3_raw_data: "type_defs.UpdatePipelineRequestTypeDef" = dataclasses.field()

    PipelineName = field("PipelineName")
    MinUnits = field("MinUnits")
    MaxUnits = field("MaxUnits")
    PipelineConfigurationBody = field("PipelineConfigurationBody")

    @cached_property
    def LogPublishingOptions(self):  # pragma: no cover
        return LogPublishingOptions.make_one(
            self.boto3_raw_data["LogPublishingOptions"]
        )

    @cached_property
    def BufferOptions(self):  # pragma: no cover
        return BufferOptions.make_one(self.boto3_raw_data["BufferOptions"])

    @cached_property
    def EncryptionAtRestOptions(self):  # pragma: no cover
        return EncryptionAtRestOptions.make_one(
            self.boto3_raw_data["EncryptionAtRestOptions"]
        )

    PipelineRoleArn = field("PipelineRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelineEndpointsResponse:
    boto3_raw_data: "type_defs.ListPipelineEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PipelineEndpoints(self):  # pragma: no cover
        return PipelineEndpoint.make_many(self.boto3_raw_data["PipelineEndpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPipelineEndpointsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelineEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineEndpointRequest:
    boto3_raw_data: "type_defs.CreatePipelineEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    PipelineArn = field("PipelineArn")
    VpcOptions = field("VpcOptions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePipelineEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesResponse:
    boto3_raw_data: "type_defs.ListPipelinesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipelines(self):  # pragma: no cover
        return PipelineSummary.make_many(self.boto3_raw_data["Pipelines"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcEndpoint:
    boto3_raw_data: "type_defs.VpcEndpointTypeDef" = dataclasses.field()

    VpcEndpointId = field("VpcEndpointId")
    VpcId = field("VpcId")

    @cached_property
    def VpcOptions(self):  # pragma: no cover
        return VpcOptionsOutput.make_one(self.boto3_raw_data["VpcOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcEndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Pipeline:
    boto3_raw_data: "type_defs.PipelineTypeDef" = dataclasses.field()

    PipelineName = field("PipelineName")
    PipelineArn = field("PipelineArn")
    MinUnits = field("MinUnits")
    MaxUnits = field("MaxUnits")
    Status = field("Status")

    @cached_property
    def StatusReason(self):  # pragma: no cover
        return PipelineStatusReason.make_one(self.boto3_raw_data["StatusReason"])

    PipelineConfigurationBody = field("PipelineConfigurationBody")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    IngestEndpointUrls = field("IngestEndpointUrls")

    @cached_property
    def LogPublishingOptions(self):  # pragma: no cover
        return LogPublishingOptions.make_one(
            self.boto3_raw_data["LogPublishingOptions"]
        )

    @cached_property
    def VpcEndpoints(self):  # pragma: no cover
        return VpcEndpoint.make_many(self.boto3_raw_data["VpcEndpoints"])

    @cached_property
    def BufferOptions(self):  # pragma: no cover
        return BufferOptions.make_one(self.boto3_raw_data["BufferOptions"])

    @cached_property
    def EncryptionAtRestOptions(self):  # pragma: no cover
        return EncryptionAtRestOptions.make_one(
            self.boto3_raw_data["EncryptionAtRestOptions"]
        )

    VpcEndpointService = field("VpcEndpointService")

    @cached_property
    def ServiceVpcEndpoints(self):  # pragma: no cover
        return ServiceVpcEndpoint.make_many(self.boto3_raw_data["ServiceVpcEndpoints"])

    @cached_property
    def Destinations(self):  # pragma: no cover
        return PipelineDestination.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    PipelineRoleArn = field("PipelineRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineRequest:
    boto3_raw_data: "type_defs.CreatePipelineRequestTypeDef" = dataclasses.field()

    PipelineName = field("PipelineName")
    MinUnits = field("MinUnits")
    MaxUnits = field("MaxUnits")
    PipelineConfigurationBody = field("PipelineConfigurationBody")

    @cached_property
    def LogPublishingOptions(self):  # pragma: no cover
        return LogPublishingOptions.make_one(
            self.boto3_raw_data["LogPublishingOptions"]
        )

    VpcOptions = field("VpcOptions")

    @cached_property
    def BufferOptions(self):  # pragma: no cover
        return BufferOptions.make_one(self.boto3_raw_data["BufferOptions"])

    @cached_property
    def EncryptionAtRestOptions(self):  # pragma: no cover
        return EncryptionAtRestOptions.make_one(
            self.boto3_raw_data["EncryptionAtRestOptions"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    PipelineRoleArn = field("PipelineRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineResponse:
    boto3_raw_data: "type_defs.CreatePipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineResponse:
    boto3_raw_data: "type_defs.GetPipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPipelineResponse:
    boto3_raw_data: "type_defs.StartPipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPipelineResponse:
    boto3_raw_data: "type_defs.StopPipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopPipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineResponse:
    boto3_raw_data: "type_defs.UpdatePipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
