# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mwaa import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CreateCliTokenRequest:
    boto3_raw_data: "type_defs.CreateCliTokenRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCliTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCliTokenRequestTypeDef"]
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
class CreateWebLoginTokenRequest:
    boto3_raw_data: "type_defs.CreateWebLoginTokenRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebLoginTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebLoginTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimension:
    boto3_raw_data: "type_defs.DimensionTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfigurationOutput:
    boto3_raw_data: "type_defs.NetworkConfigurationOutputTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

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
class GetEnvironmentInput:
    boto3_raw_data: "type_defs.GetEnvironmentInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeRestApiRequest:
    boto3_raw_data: "type_defs.InvokeRestApiRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Path = field("Path")
    Method = field("Method")
    QueryParameters = field("QueryParameters")
    Body = field("Body")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeRestApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeRestApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateError:
    boto3_raw_data: "type_defs.UpdateErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateErrorTypeDef"]]
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
class ListEnvironmentsInput:
    boto3_raw_data: "type_defs.ListEnvironmentsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsInputTypeDef"]
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
class ModuleLoggingConfigurationInput:
    boto3_raw_data: "type_defs.ModuleLoggingConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")
    LogLevel = field("LogLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModuleLoggingConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModuleLoggingConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModuleLoggingConfiguration:
    boto3_raw_data: "type_defs.ModuleLoggingConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    LogLevel = field("LogLevel")
    CloudWatchLogGroupArn = field("CloudWatchLogGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModuleLoggingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModuleLoggingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatisticSet:
    boto3_raw_data: "type_defs.StatisticSetTypeDef" = dataclasses.field()

    SampleCount = field("SampleCount")
    Sum = field("Sum")
    Minimum = field("Minimum")
    Maximum = field("Maximum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatisticSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatisticSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfiguration:
    boto3_raw_data: "type_defs.NetworkConfigurationTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

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
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
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

    ResourceArn = field("ResourceArn")
    tagKeys = field("tagKeys")

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
class UpdateNetworkConfigurationInput:
    boto3_raw_data: "type_defs.UpdateNetworkConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateNetworkConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNetworkConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCliTokenResponse:
    boto3_raw_data: "type_defs.CreateCliTokenResponseTypeDef" = dataclasses.field()

    CliToken = field("CliToken")
    WebServerHostname = field("WebServerHostname")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCliTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCliTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentOutput:
    boto3_raw_data: "type_defs.CreateEnvironmentOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebLoginTokenResponse:
    boto3_raw_data: "type_defs.CreateWebLoginTokenResponseTypeDef" = dataclasses.field()

    WebToken = field("WebToken")
    WebServerHostname = field("WebServerHostname")
    IamIdentity = field("IamIdentity")
    AirflowIdentity = field("AirflowIdentity")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebLoginTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebLoginTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeRestApiResponse:
    boto3_raw_data: "type_defs.InvokeRestApiResponseTypeDef" = dataclasses.field()

    RestApiStatusCode = field("RestApiStatusCode")
    RestApiResponse = field("RestApiResponse")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeRestApiResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeRestApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsOutput:
    boto3_raw_data: "type_defs.ListEnvironmentsOutputTypeDef" = dataclasses.field()

    Environments = field("Environments")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsOutputTypeDef"]
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
class UpdateEnvironmentOutput:
    boto3_raw_data: "type_defs.UpdateEnvironmentOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LastUpdate:
    boto3_raw_data: "type_defs.LastUpdateTypeDef" = dataclasses.field()

    Status = field("Status")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Error(self):  # pragma: no cover
        return UpdateError.make_one(self.boto3_raw_data["Error"])

    Source = field("Source")
    WorkerReplacementStrategy = field("WorkerReplacementStrategy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LastUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LastUpdateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsInputPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfigurationInput:
    boto3_raw_data: "type_defs.LoggingConfigurationInputTypeDef" = dataclasses.field()

    @cached_property
    def DagProcessingLogs(self):  # pragma: no cover
        return ModuleLoggingConfigurationInput.make_one(
            self.boto3_raw_data["DagProcessingLogs"]
        )

    @cached_property
    def SchedulerLogs(self):  # pragma: no cover
        return ModuleLoggingConfigurationInput.make_one(
            self.boto3_raw_data["SchedulerLogs"]
        )

    @cached_property
    def WebserverLogs(self):  # pragma: no cover
        return ModuleLoggingConfigurationInput.make_one(
            self.boto3_raw_data["WebserverLogs"]
        )

    @cached_property
    def WorkerLogs(self):  # pragma: no cover
        return ModuleLoggingConfigurationInput.make_one(
            self.boto3_raw_data["WorkerLogs"]
        )

    @cached_property
    def TaskLogs(self):  # pragma: no cover
        return ModuleLoggingConfigurationInput.make_one(self.boto3_raw_data["TaskLogs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfiguration:
    boto3_raw_data: "type_defs.LoggingConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def DagProcessingLogs(self):  # pragma: no cover
        return ModuleLoggingConfiguration.make_one(
            self.boto3_raw_data["DagProcessingLogs"]
        )

    @cached_property
    def SchedulerLogs(self):  # pragma: no cover
        return ModuleLoggingConfiguration.make_one(self.boto3_raw_data["SchedulerLogs"])

    @cached_property
    def WebserverLogs(self):  # pragma: no cover
        return ModuleLoggingConfiguration.make_one(self.boto3_raw_data["WebserverLogs"])

    @cached_property
    def WorkerLogs(self):  # pragma: no cover
        return ModuleLoggingConfiguration.make_one(self.boto3_raw_data["WorkerLogs"])

    @cached_property
    def TaskLogs(self):  # pragma: no cover
        return ModuleLoggingConfiguration.make_one(self.boto3_raw_data["TaskLogs"])

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
class MetricDatum:
    boto3_raw_data: "type_defs.MetricDatumTypeDef" = dataclasses.field()

    MetricName = field("MetricName")
    Timestamp = field("Timestamp")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Value = field("Value")
    Unit = field("Unit")

    @cached_property
    def StatisticValues(self):  # pragma: no cover
        return StatisticSet.make_one(self.boto3_raw_data["StatisticValues"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDatumTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDatumTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentInput:
    boto3_raw_data: "type_defs.UpdateEnvironmentInputTypeDef" = dataclasses.field()

    Name = field("Name")
    ExecutionRoleArn = field("ExecutionRoleArn")
    AirflowConfigurationOptions = field("AirflowConfigurationOptions")
    AirflowVersion = field("AirflowVersion")
    DagS3Path = field("DagS3Path")
    EnvironmentClass = field("EnvironmentClass")

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfigurationInput.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    MaxWorkers = field("MaxWorkers")
    MinWorkers = field("MinWorkers")
    MaxWebservers = field("MaxWebservers")
    MinWebservers = field("MinWebservers")
    WorkerReplacementStrategy = field("WorkerReplacementStrategy")

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return UpdateNetworkConfigurationInput.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    PluginsS3Path = field("PluginsS3Path")
    PluginsS3ObjectVersion = field("PluginsS3ObjectVersion")
    RequirementsS3Path = field("RequirementsS3Path")
    RequirementsS3ObjectVersion = field("RequirementsS3ObjectVersion")
    Schedulers = field("Schedulers")
    SourceBucketArn = field("SourceBucketArn")
    StartupScriptS3Path = field("StartupScriptS3Path")
    StartupScriptS3ObjectVersion = field("StartupScriptS3ObjectVersion")
    WebserverAccessMode = field("WebserverAccessMode")
    WeeklyMaintenanceWindowStart = field("WeeklyMaintenanceWindowStart")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Environment:
    boto3_raw_data: "type_defs.EnvironmentTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    WebserverUrl = field("WebserverUrl")
    ExecutionRoleArn = field("ExecutionRoleArn")
    ServiceRoleArn = field("ServiceRoleArn")
    KmsKey = field("KmsKey")
    AirflowVersion = field("AirflowVersion")
    SourceBucketArn = field("SourceBucketArn")
    DagS3Path = field("DagS3Path")
    PluginsS3Path = field("PluginsS3Path")
    PluginsS3ObjectVersion = field("PluginsS3ObjectVersion")
    RequirementsS3Path = field("RequirementsS3Path")
    RequirementsS3ObjectVersion = field("RequirementsS3ObjectVersion")
    StartupScriptS3Path = field("StartupScriptS3Path")
    StartupScriptS3ObjectVersion = field("StartupScriptS3ObjectVersion")
    AirflowConfigurationOptions = field("AirflowConfigurationOptions")
    EnvironmentClass = field("EnvironmentClass")
    MaxWorkers = field("MaxWorkers")

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfiguration.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    @cached_property
    def LastUpdate(self):  # pragma: no cover
        return LastUpdate.make_one(self.boto3_raw_data["LastUpdate"])

    WeeklyMaintenanceWindowStart = field("WeeklyMaintenanceWindowStart")
    Tags = field("Tags")
    WebserverAccessMode = field("WebserverAccessMode")
    MinWorkers = field("MinWorkers")
    Schedulers = field("Schedulers")
    WebserverVpcEndpointService = field("WebserverVpcEndpointService")
    DatabaseVpcEndpointService = field("DatabaseVpcEndpointService")
    CeleryExecutorQueue = field("CeleryExecutorQueue")
    EndpointManagement = field("EndpointManagement")
    MinWebservers = field("MinWebservers")
    MaxWebservers = field("MaxWebservers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishMetricsInput:
    boto3_raw_data: "type_defs.PublishMetricsInputTypeDef" = dataclasses.field()

    EnvironmentName = field("EnvironmentName")

    @cached_property
    def MetricData(self):  # pragma: no cover
        return MetricDatum.make_many(self.boto3_raw_data["MetricData"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishMetricsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishMetricsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentInput:
    boto3_raw_data: "type_defs.CreateEnvironmentInputTypeDef" = dataclasses.field()

    Name = field("Name")
    ExecutionRoleArn = field("ExecutionRoleArn")
    SourceBucketArn = field("SourceBucketArn")
    DagS3Path = field("DagS3Path")
    NetworkConfiguration = field("NetworkConfiguration")
    PluginsS3Path = field("PluginsS3Path")
    PluginsS3ObjectVersion = field("PluginsS3ObjectVersion")
    RequirementsS3Path = field("RequirementsS3Path")
    RequirementsS3ObjectVersion = field("RequirementsS3ObjectVersion")
    StartupScriptS3Path = field("StartupScriptS3Path")
    StartupScriptS3ObjectVersion = field("StartupScriptS3ObjectVersion")
    AirflowConfigurationOptions = field("AirflowConfigurationOptions")
    EnvironmentClass = field("EnvironmentClass")
    MaxWorkers = field("MaxWorkers")
    KmsKey = field("KmsKey")
    AirflowVersion = field("AirflowVersion")

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfigurationInput.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    WeeklyMaintenanceWindowStart = field("WeeklyMaintenanceWindowStart")
    Tags = field("Tags")
    WebserverAccessMode = field("WebserverAccessMode")
    MinWorkers = field("MinWorkers")
    Schedulers = field("Schedulers")
    EndpointManagement = field("EndpointManagement")
    MinWebservers = field("MinWebservers")
    MaxWebservers = field("MaxWebservers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentOutput:
    boto3_raw_data: "type_defs.GetEnvironmentOutputTypeDef" = dataclasses.field()

    @cached_property
    def Environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["Environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
