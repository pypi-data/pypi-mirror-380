# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_migration_hub_refactor_spaces import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ApiGatewayProxyConfig:
    boto3_raw_data: "type_defs.ApiGatewayProxyConfigTypeDef" = dataclasses.field()

    ApiGatewayId = field("ApiGatewayId")
    EndpointType = field("EndpointType")
    NlbArn = field("NlbArn")
    NlbName = field("NlbName")
    ProxyUrl = field("ProxyUrl")
    StageName = field("StageName")
    VpcLinkId = field("VpcLinkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiGatewayProxyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiGatewayProxyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiGatewayProxyInput:
    boto3_raw_data: "type_defs.ApiGatewayProxyInputTypeDef" = dataclasses.field()

    EndpointType = field("EndpointType")
    StageName = field("StageName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiGatewayProxyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiGatewayProxyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiGatewayProxySummary:
    boto3_raw_data: "type_defs.ApiGatewayProxySummaryTypeDef" = dataclasses.field()

    ApiGatewayId = field("ApiGatewayId")
    EndpointType = field("EndpointType")
    NlbArn = field("NlbArn")
    NlbName = field("NlbName")
    ProxyUrl = field("ProxyUrl")
    StageName = field("StageName")
    VpcLinkId = field("VpcLinkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiGatewayProxySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiGatewayProxySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorResponse:
    boto3_raw_data: "type_defs.ErrorResponseTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    AdditionalDetails = field("AdditionalDetails")
    Code = field("Code")
    Message = field("Message")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorResponseTypeDef"]],
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
class CreateEnvironmentRequest:
    boto3_raw_data: "type_defs.CreateEnvironmentRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    NetworkFabricType = field("NetworkFabricType")
    ClientToken = field("ClientToken")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultRouteInput:
    boto3_raw_data: "type_defs.DefaultRouteInputTypeDef" = dataclasses.field()

    ActivationState = field("ActivationState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefaultRouteInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultRouteInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UriPathRouteInputOutput:
    boto3_raw_data: "type_defs.UriPathRouteInputOutputTypeDef" = dataclasses.field()

    ActivationState = field("ActivationState")
    SourcePath = field("SourcePath")
    AppendSourcePath = field("AppendSourcePath")
    IncludeChildPaths = field("IncludeChildPaths")
    Methods = field("Methods")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UriPathRouteInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UriPathRouteInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaEndpointInput:
    boto3_raw_data: "type_defs.LambdaEndpointInputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaEndpointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UrlEndpointInput:
    boto3_raw_data: "type_defs.UrlEndpointInputTypeDef" = dataclasses.field()

    Url = field("Url")
    HealthUrl = field("HealthUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UrlEndpointInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UrlEndpointInputTypeDef"]
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

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")

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
class DeleteEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteEnvironmentRequestTypeDef" = dataclasses.field()

    EnvironmentIdentifier = field("EnvironmentIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentRequestTypeDef"]
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

    Identifier = field("Identifier")

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
class DeleteRouteRequest:
    boto3_raw_data: "type_defs.DeleteRouteRequestTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")
    RouteIdentifier = field("RouteIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRouteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRouteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceRequest:
    boto3_raw_data: "type_defs.DeleteServiceRequestTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")
    ServiceIdentifier = field("ServiceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentVpc:
    boto3_raw_data: "type_defs.EnvironmentVpcTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    CidrBlocks = field("CidrBlocks")
    CreatedTime = field("CreatedTime")
    EnvironmentId = field("EnvironmentId")
    LastUpdatedTime = field("LastUpdatedTime")
    VpcId = field("VpcId")
    VpcName = field("VpcName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentVpcTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentVpcTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationRequest:
    boto3_raw_data: "type_defs.GetApplicationRequestTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")

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
class GetEnvironmentRequest:
    boto3_raw_data: "type_defs.GetEnvironmentRequestTypeDef" = dataclasses.field()

    EnvironmentIdentifier = field("EnvironmentIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentRequestTypeDef"]
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

    Identifier = field("Identifier")

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
class GetRouteRequest:
    boto3_raw_data: "type_defs.GetRouteRequestTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")
    RouteIdentifier = field("RouteIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRouteRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRouteRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceRequest:
    boto3_raw_data: "type_defs.GetServiceRequestTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")
    ServiceIdentifier = field("ServiceIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetServiceRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaEndpointConfig:
    boto3_raw_data: "type_defs.LambdaEndpointConfigTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaEndpointConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaEndpointConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UrlEndpointConfig:
    boto3_raw_data: "type_defs.UrlEndpointConfigTypeDef" = dataclasses.field()

    HealthUrl = field("HealthUrl")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UrlEndpointConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UrlEndpointConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaEndpointSummary:
    boto3_raw_data: "type_defs.LambdaEndpointSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaEndpointSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaEndpointSummaryTypeDef"]
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
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    EnvironmentIdentifier = field("EnvironmentIdentifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class ListEnvironmentVpcsRequest:
    boto3_raw_data: "type_defs.ListEnvironmentVpcsRequestTypeDef" = dataclasses.field()

    EnvironmentIdentifier = field("EnvironmentIdentifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentVpcsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentVpcsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsRequest:
    boto3_raw_data: "type_defs.ListEnvironmentsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutesRequest:
    boto3_raw_data: "type_defs.ListRoutesRequestTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRoutesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesRequest:
    boto3_raw_data: "type_defs.ListServicesRequestTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesRequestTypeDef"]
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
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    Policy = field("Policy")
    ResourceArn = field("ResourceArn")

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
class UrlEndpointSummary:
    boto3_raw_data: "type_defs.UrlEndpointSummaryTypeDef" = dataclasses.field()

    HealthUrl = field("HealthUrl")
    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UrlEndpointSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UrlEndpointSummaryTypeDef"]
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
    Tags = field("Tags")

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
class UpdateRouteRequest:
    boto3_raw_data: "type_defs.UpdateRouteRequestTypeDef" = dataclasses.field()

    ActivationState = field("ActivationState")
    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")
    RouteIdentifier = field("RouteIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRouteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UriPathRouteInput:
    boto3_raw_data: "type_defs.UriPathRouteInputTypeDef" = dataclasses.field()

    ActivationState = field("ActivationState")
    SourcePath = field("SourcePath")
    AppendSourcePath = field("AppendSourcePath")
    IncludeChildPaths = field("IncludeChildPaths")
    Methods = field("Methods")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UriPathRouteInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UriPathRouteInputTypeDef"]
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

    EnvironmentIdentifier = field("EnvironmentIdentifier")
    Name = field("Name")
    ProxyType = field("ProxyType")
    VpcId = field("VpcId")

    @cached_property
    def ApiGatewayProxy(self):  # pragma: no cover
        return ApiGatewayProxyInput.make_one(self.boto3_raw_data["ApiGatewayProxy"])

    ClientToken = field("ClientToken")
    Tags = field("Tags")

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
class ApplicationSummary:
    boto3_raw_data: "type_defs.ApplicationSummaryTypeDef" = dataclasses.field()

    @cached_property
    def ApiGatewayProxy(self):  # pragma: no cover
        return ApiGatewayProxySummary.make_one(self.boto3_raw_data["ApiGatewayProxy"])

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreatedByAccountId = field("CreatedByAccountId")
    CreatedTime = field("CreatedTime")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorResponse.make_one(self.boto3_raw_data["Error"])

    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    OwnerAccountId = field("OwnerAccountId")
    ProxyType = field("ProxyType")
    State = field("State")
    Tags = field("Tags")
    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentSummary:
    boto3_raw_data: "type_defs.EnvironmentSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedTime = field("CreatedTime")
    Description = field("Description")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorResponse.make_one(self.boto3_raw_data["Error"])

    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    NetworkFabricType = field("NetworkFabricType")
    OwnerAccountId = field("OwnerAccountId")
    State = field("State")
    Tags = field("Tags")
    TransitGatewayId = field("TransitGatewayId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteSummary:
    boto3_raw_data: "type_defs.RouteSummaryTypeDef" = dataclasses.field()

    AppendSourcePath = field("AppendSourcePath")
    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreatedByAccountId = field("CreatedByAccountId")
    CreatedTime = field("CreatedTime")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorResponse.make_one(self.boto3_raw_data["Error"])

    IncludeChildPaths = field("IncludeChildPaths")
    LastUpdatedTime = field("LastUpdatedTime")
    Methods = field("Methods")
    OwnerAccountId = field("OwnerAccountId")
    PathResourceToId = field("PathResourceToId")
    RouteId = field("RouteId")
    RouteType = field("RouteType")
    ServiceId = field("ServiceId")
    SourcePath = field("SourcePath")
    State = field("State")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationResponse:
    boto3_raw_data: "type_defs.CreateApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApiGatewayProxy(self):  # pragma: no cover
        return ApiGatewayProxyInput.make_one(self.boto3_raw_data["ApiGatewayProxy"])

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreatedByAccountId = field("CreatedByAccountId")
    CreatedTime = field("CreatedTime")
    EnvironmentId = field("EnvironmentId")
    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    OwnerAccountId = field("OwnerAccountId")
    ProxyType = field("ProxyType")
    State = field("State")
    Tags = field("Tags")
    VpcId = field("VpcId")

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
class CreateEnvironmentResponse:
    boto3_raw_data: "type_defs.CreateEnvironmentResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedTime = field("CreatedTime")
    Description = field("Description")
    EnvironmentId = field("EnvironmentId")
    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    NetworkFabricType = field("NetworkFabricType")
    OwnerAccountId = field("OwnerAccountId")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationResponse:
    boto3_raw_data: "type_defs.DeleteApplicationResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    EnvironmentId = field("EnvironmentId")
    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentResponse:
    boto3_raw_data: "type_defs.DeleteEnvironmentResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    EnvironmentId = field("EnvironmentId")
    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRouteResponse:
    boto3_raw_data: "type_defs.DeleteRouteResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    LastUpdatedTime = field("LastUpdatedTime")
    RouteId = field("RouteId")
    ServiceId = field("ServiceId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRouteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRouteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceResponse:
    boto3_raw_data: "type_defs.DeleteServiceResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    EnvironmentId = field("EnvironmentId")
    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    ServiceId = field("ServiceId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceResponseTypeDef"]
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

    @cached_property
    def ApiGatewayProxy(self):  # pragma: no cover
        return ApiGatewayProxyConfig.make_one(self.boto3_raw_data["ApiGatewayProxy"])

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreatedByAccountId = field("CreatedByAccountId")
    CreatedTime = field("CreatedTime")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorResponse.make_one(self.boto3_raw_data["Error"])

    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    OwnerAccountId = field("OwnerAccountId")
    ProxyType = field("ProxyType")
    State = field("State")
    Tags = field("Tags")
    VpcId = field("VpcId")

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
class GetEnvironmentResponse:
    boto3_raw_data: "type_defs.GetEnvironmentResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedTime = field("CreatedTime")
    Description = field("Description")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorResponse.make_one(self.boto3_raw_data["Error"])

    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    NetworkFabricType = field("NetworkFabricType")
    OwnerAccountId = field("OwnerAccountId")
    State = field("State")
    Tags = field("Tags")
    TransitGatewayId = field("TransitGatewayId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentResponseTypeDef"]
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
class GetRouteResponse:
    boto3_raw_data: "type_defs.GetRouteResponseTypeDef" = dataclasses.field()

    AppendSourcePath = field("AppendSourcePath")
    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreatedByAccountId = field("CreatedByAccountId")
    CreatedTime = field("CreatedTime")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorResponse.make_one(self.boto3_raw_data["Error"])

    IncludeChildPaths = field("IncludeChildPaths")
    LastUpdatedTime = field("LastUpdatedTime")
    Methods = field("Methods")
    OwnerAccountId = field("OwnerAccountId")
    PathResourceToId = field("PathResourceToId")
    RouteId = field("RouteId")
    RouteType = field("RouteType")
    ServiceId = field("ServiceId")
    SourcePath = field("SourcePath")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRouteResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRouteResponseTypeDef"]
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

    Tags = field("Tags")

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
class UpdateRouteResponse:
    boto3_raw_data: "type_defs.UpdateRouteResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    LastUpdatedTime = field("LastUpdatedTime")
    RouteId = field("RouteId")
    ServiceId = field("ServiceId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRouteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRouteResponse:
    boto3_raw_data: "type_defs.CreateRouteResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreatedByAccountId = field("CreatedByAccountId")
    CreatedTime = field("CreatedTime")
    LastUpdatedTime = field("LastUpdatedTime")
    OwnerAccountId = field("OwnerAccountId")
    RouteId = field("RouteId")
    RouteType = field("RouteType")
    ServiceId = field("ServiceId")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def UriPathRoute(self):  # pragma: no cover
        return UriPathRouteInputOutput.make_one(self.boto3_raw_data["UriPathRoute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRouteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceRequest:
    boto3_raw_data: "type_defs.CreateServiceRequestTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EndpointType = field("EndpointType")
    EnvironmentIdentifier = field("EnvironmentIdentifier")
    Name = field("Name")
    ClientToken = field("ClientToken")
    Description = field("Description")

    @cached_property
    def LambdaEndpoint(self):  # pragma: no cover
        return LambdaEndpointInput.make_one(self.boto3_raw_data["LambdaEndpoint"])

    Tags = field("Tags")

    @cached_property
    def UrlEndpoint(self):  # pragma: no cover
        return UrlEndpointInput.make_one(self.boto3_raw_data["UrlEndpoint"])

    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceResponse:
    boto3_raw_data: "type_defs.CreateServiceResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreatedByAccountId = field("CreatedByAccountId")
    CreatedTime = field("CreatedTime")
    Description = field("Description")
    EndpointType = field("EndpointType")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def LambdaEndpoint(self):  # pragma: no cover
        return LambdaEndpointInput.make_one(self.boto3_raw_data["LambdaEndpoint"])

    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    OwnerAccountId = field("OwnerAccountId")
    ServiceId = field("ServiceId")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def UrlEndpoint(self):  # pragma: no cover
        return UrlEndpointInput.make_one(self.boto3_raw_data["UrlEndpoint"])

    VpcId = field("VpcId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentVpcsResponse:
    boto3_raw_data: "type_defs.ListEnvironmentVpcsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EnvironmentVpcList(self):  # pragma: no cover
        return EnvironmentVpc.make_many(self.boto3_raw_data["EnvironmentVpcList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentVpcsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentVpcsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceResponse:
    boto3_raw_data: "type_defs.GetServiceResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreatedByAccountId = field("CreatedByAccountId")
    CreatedTime = field("CreatedTime")
    Description = field("Description")
    EndpointType = field("EndpointType")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorResponse.make_one(self.boto3_raw_data["Error"])

    @cached_property
    def LambdaEndpoint(self):  # pragma: no cover
        return LambdaEndpointConfig.make_one(self.boto3_raw_data["LambdaEndpoint"])

    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    OwnerAccountId = field("OwnerAccountId")
    ServiceId = field("ServiceId")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def UrlEndpoint(self):  # pragma: no cover
        return UrlEndpointConfig.make_one(self.boto3_raw_data["UrlEndpoint"])

    VpcId = field("VpcId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceResponseTypeDef"]
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

    EnvironmentIdentifier = field("EnvironmentIdentifier")

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
class ListEnvironmentVpcsRequestPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentVpcsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    EnvironmentIdentifier = field("EnvironmentIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentVpcsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentVpcsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutesRequestPaginate:
    boto3_raw_data: "type_defs.ListRoutesRequestPaginateTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoutesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesRequestPaginate:
    boto3_raw_data: "type_defs.ListServicesRequestPaginateTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSummary:
    boto3_raw_data: "type_defs.ServiceSummaryTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Arn = field("Arn")
    CreatedByAccountId = field("CreatedByAccountId")
    CreatedTime = field("CreatedTime")
    Description = field("Description")
    EndpointType = field("EndpointType")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorResponse.make_one(self.boto3_raw_data["Error"])

    @cached_property
    def LambdaEndpoint(self):  # pragma: no cover
        return LambdaEndpointSummary.make_one(self.boto3_raw_data["LambdaEndpoint"])

    LastUpdatedTime = field("LastUpdatedTime")
    Name = field("Name")
    OwnerAccountId = field("OwnerAccountId")
    ServiceId = field("ServiceId")
    State = field("State")
    Tags = field("Tags")

    @cached_property
    def UrlEndpoint(self):  # pragma: no cover
        return UrlEndpointSummary.make_one(self.boto3_raw_data["UrlEndpoint"])

    VpcId = field("VpcId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceSummaryTypeDef"]],
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
    def ApplicationSummaryList(self):  # pragma: no cover
        return ApplicationSummary.make_many(
            self.boto3_raw_data["ApplicationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class ListEnvironmentsResponse:
    boto3_raw_data: "type_defs.ListEnvironmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EnvironmentSummaryList(self):  # pragma: no cover
        return EnvironmentSummary.make_many(
            self.boto3_raw_data["EnvironmentSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutesResponse:
    boto3_raw_data: "type_defs.ListRoutesResponseTypeDef" = dataclasses.field()

    @cached_property
    def RouteSummaryList(self):  # pragma: no cover
        return RouteSummary.make_many(self.boto3_raw_data["RouteSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoutesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesResponse:
    boto3_raw_data: "type_defs.ListServicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def ServiceSummaryList(self):  # pragma: no cover
        return ServiceSummary.make_many(self.boto3_raw_data["ServiceSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRouteRequest:
    boto3_raw_data: "type_defs.CreateRouteRequestTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")
    EnvironmentIdentifier = field("EnvironmentIdentifier")
    RouteType = field("RouteType")
    ServiceIdentifier = field("ServiceIdentifier")
    ClientToken = field("ClientToken")

    @cached_property
    def DefaultRoute(self):  # pragma: no cover
        return DefaultRouteInput.make_one(self.boto3_raw_data["DefaultRoute"])

    Tags = field("Tags")
    UriPathRoute = field("UriPathRoute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRouteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
