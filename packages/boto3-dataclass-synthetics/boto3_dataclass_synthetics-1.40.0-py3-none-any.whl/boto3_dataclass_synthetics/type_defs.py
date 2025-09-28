# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_synthetics import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class S3EncryptionConfig:
    boto3_raw_data: "type_defs.S3EncryptionConfigTypeDef" = dataclasses.field()

    EncryptionMode = field("EncryptionMode")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3EncryptionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3EncryptionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResourceRequest:
    boto3_raw_data: "type_defs.AssociateResourceRequestTypeDef" = dataclasses.field()

    GroupIdentifier = field("GroupIdentifier")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaseScreenshotOutput:
    boto3_raw_data: "type_defs.BaseScreenshotOutputTypeDef" = dataclasses.field()

    ScreenshotName = field("ScreenshotName")
    IgnoreCoordinates = field("IgnoreCoordinates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BaseScreenshotOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BaseScreenshotOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaseScreenshot:
    boto3_raw_data: "type_defs.BaseScreenshotTypeDef" = dataclasses.field()

    ScreenshotName = field("ScreenshotName")
    IgnoreCoordinates = field("IgnoreCoordinates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BaseScreenshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BaseScreenshotTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserConfig:
    boto3_raw_data: "type_defs.BrowserConfigTypeDef" = dataclasses.field()

    BrowserType = field("BrowserType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BrowserConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BrowserConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dependency:
    boto3_raw_data: "type_defs.DependencyTypeDef" = dataclasses.field()

    Reference = field("Reference")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DependencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DependencyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryDryRunConfigOutput:
    boto3_raw_data: "type_defs.CanaryDryRunConfigOutputTypeDef" = dataclasses.field()

    DryRunId = field("DryRunId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CanaryDryRunConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanaryDryRunConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryRunConfigInput:
    boto3_raw_data: "type_defs.CanaryRunConfigInputTypeDef" = dataclasses.field()

    TimeoutInSeconds = field("TimeoutInSeconds")
    MemoryInMB = field("MemoryInMB")
    ActiveTracing = field("ActiveTracing")
    EnvironmentVariables = field("EnvironmentVariables")
    EphemeralStorage = field("EphemeralStorage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CanaryRunConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanaryRunConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryRunConfigOutput:
    boto3_raw_data: "type_defs.CanaryRunConfigOutputTypeDef" = dataclasses.field()

    TimeoutInSeconds = field("TimeoutInSeconds")
    MemoryInMB = field("MemoryInMB")
    ActiveTracing = field("ActiveTracing")
    EphemeralStorage = field("EphemeralStorage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CanaryRunConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanaryRunConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryRunStatus:
    boto3_raw_data: "type_defs.CanaryRunStatusTypeDef" = dataclasses.field()

    State = field("State")
    StateReason = field("StateReason")
    StateReasonCode = field("StateReasonCode")
    TestResult = field("TestResult")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanaryRunStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanaryRunStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryRunTimeline:
    boto3_raw_data: "type_defs.CanaryRunTimelineTypeDef" = dataclasses.field()

    Started = field("Started")
    Completed = field("Completed")
    MetricTimestampForRunAndRetries = field("MetricTimestampForRunAndRetries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanaryRunTimelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanaryRunTimelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryConfigInput:
    boto3_raw_data: "type_defs.RetryConfigInputTypeDef" = dataclasses.field()

    MaxRetries = field("MaxRetries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryConfigInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryConfigOutput:
    boto3_raw_data: "type_defs.RetryConfigOutputTypeDef" = dataclasses.field()

    MaxRetries = field("MaxRetries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryStatus:
    boto3_raw_data: "type_defs.CanaryStatusTypeDef" = dataclasses.field()

    State = field("State")
    StateReason = field("StateReason")
    StateReasonCode = field("StateReasonCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanaryStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanaryStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryTimeline:
    boto3_raw_data: "type_defs.CanaryTimelineTypeDef" = dataclasses.field()

    Created = field("Created")
    LastModified = field("LastModified")
    LastStarted = field("LastStarted")
    LastStopped = field("LastStopped")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanaryTimelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanaryTimelineTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DryRunConfigOutput:
    boto3_raw_data: "type_defs.DryRunConfigOutputTypeDef" = dataclasses.field()

    DryRunId = field("DryRunId")
    LastDryRunExecutionStatus = field("LastDryRunExecutionStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DryRunConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DryRunConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineConfig:
    boto3_raw_data: "type_defs.EngineConfigTypeDef" = dataclasses.field()

    EngineArn = field("EngineArn")
    BrowserType = field("BrowserType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngineConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EngineConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigOutput:
    boto3_raw_data: "type_defs.VpcConfigOutputTypeDef" = dataclasses.field()

    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")
    Ipv6AllowedForDualStack = field("Ipv6AllowedForDualStack")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigInput:
    boto3_raw_data: "type_defs.VpcConfigInputTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")
    Ipv6AllowedForDualStack = field("Ipv6AllowedForDualStack")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigInputTypeDef"]],
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
class CreateGroupRequest:
    boto3_raw_data: "type_defs.CreateGroupRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Group:
    boto3_raw_data: "type_defs.GroupTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Arn = field("Arn")
    Tags = field("Tags")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCanaryRequest:
    boto3_raw_data: "type_defs.DeleteCanaryRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    DeleteLambda = field("DeleteLambda")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCanaryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCanaryRequestTypeDef"]
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

    GroupIdentifier = field("GroupIdentifier")

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
class DescribeCanariesLastRunRequest:
    boto3_raw_data: "type_defs.DescribeCanariesLastRunRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Names = field("Names")
    BrowserType = field("BrowserType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCanariesLastRunRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCanariesLastRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCanariesRequest:
    boto3_raw_data: "type_defs.DescribeCanariesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Names = field("Names")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCanariesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCanariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuntimeVersionsRequest:
    boto3_raw_data: "type_defs.DescribeRuntimeVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRuntimeVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuntimeVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeVersion:
    boto3_raw_data: "type_defs.RuntimeVersionTypeDef" = dataclasses.field()

    VersionName = field("VersionName")
    Description = field("Description")
    ReleaseDate = field("ReleaseDate")
    DeprecationDate = field("DeprecationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuntimeVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuntimeVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResourceRequest:
    boto3_raw_data: "type_defs.DisassociateResourceRequestTypeDef" = dataclasses.field()

    GroupIdentifier = field("GroupIdentifier")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCanaryRequest:
    boto3_raw_data: "type_defs.GetCanaryRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    DryRunId = field("DryRunId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetCanaryRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCanaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCanaryRunsRequest:
    boto3_raw_data: "type_defs.GetCanaryRunsRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    DryRunId = field("DryRunId")
    RunType = field("RunType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCanaryRunsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCanaryRunsRequestTypeDef"]
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

    GroupIdentifier = field("GroupIdentifier")

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
class GroupSummary:
    boto3_raw_data: "type_defs.GroupSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Arn = field("Arn")

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
class ListAssociatedGroupsRequest:
    boto3_raw_data: "type_defs.ListAssociatedGroupsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociatedGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupResourcesRequest:
    boto3_raw_data: "type_defs.ListGroupResourcesRequestTypeDef" = dataclasses.field()

    GroupIdentifier = field("GroupIdentifier")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupResourcesRequestTypeDef"]
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

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

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
class StartCanaryRequest:
    boto3_raw_data: "type_defs.StartCanaryRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCanaryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCanaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCanaryRequest:
    boto3_raw_data: "type_defs.StopCanaryRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopCanaryRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCanaryRequestTypeDef"]
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
class ArtifactConfigInput:
    boto3_raw_data: "type_defs.ArtifactConfigInputTypeDef" = dataclasses.field()

    @cached_property
    def S3Encryption(self):  # pragma: no cover
        return S3EncryptionConfig.make_one(self.boto3_raw_data["S3Encryption"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArtifactConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArtifactConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArtifactConfigOutput:
    boto3_raw_data: "type_defs.ArtifactConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def S3Encryption(self):  # pragma: no cover
        return S3EncryptionConfig.make_one(self.boto3_raw_data["S3Encryption"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArtifactConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArtifactConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VisualReferenceOutput:
    boto3_raw_data: "type_defs.VisualReferenceOutputTypeDef" = dataclasses.field()

    @cached_property
    def BaseScreenshots(self):  # pragma: no cover
        return BaseScreenshotOutput.make_many(self.boto3_raw_data["BaseScreenshots"])

    BaseCanaryRunId = field("BaseCanaryRunId")
    BrowserType = field("BrowserType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VisualReferenceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VisualReferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryCodeInput:
    boto3_raw_data: "type_defs.CanaryCodeInputTypeDef" = dataclasses.field()

    Handler = field("Handler")
    S3Bucket = field("S3Bucket")
    S3Key = field("S3Key")
    S3Version = field("S3Version")
    ZipFile = field("ZipFile")

    @cached_property
    def Dependencies(self):  # pragma: no cover
        return Dependency.make_many(self.boto3_raw_data["Dependencies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanaryCodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanaryCodeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryCodeOutput:
    boto3_raw_data: "type_defs.CanaryCodeOutputTypeDef" = dataclasses.field()

    SourceLocationArn = field("SourceLocationArn")
    Handler = field("Handler")

    @cached_property
    def Dependencies(self):  # pragma: no cover
        return Dependency.make_many(self.boto3_raw_data["Dependencies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanaryCodeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanaryCodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryRun:
    boto3_raw_data: "type_defs.CanaryRunTypeDef" = dataclasses.field()

    Id = field("Id")
    ScheduledRunId = field("ScheduledRunId")
    RetryAttempt = field("RetryAttempt")
    Name = field("Name")

    @cached_property
    def Status(self):  # pragma: no cover
        return CanaryRunStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Timeline(self):  # pragma: no cover
        return CanaryRunTimeline.make_one(self.boto3_raw_data["Timeline"])

    ArtifactS3Location = field("ArtifactS3Location")

    @cached_property
    def DryRunConfig(self):  # pragma: no cover
        return CanaryDryRunConfigOutput.make_one(self.boto3_raw_data["DryRunConfig"])

    BrowserType = field("BrowserType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanaryRunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanaryRunTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryScheduleInput:
    boto3_raw_data: "type_defs.CanaryScheduleInputTypeDef" = dataclasses.field()

    Expression = field("Expression")
    DurationInSeconds = field("DurationInSeconds")

    @cached_property
    def RetryConfig(self):  # pragma: no cover
        return RetryConfigInput.make_one(self.boto3_raw_data["RetryConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CanaryScheduleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanaryScheduleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryScheduleOutput:
    boto3_raw_data: "type_defs.CanaryScheduleOutputTypeDef" = dataclasses.field()

    Expression = field("Expression")
    DurationInSeconds = field("DurationInSeconds")

    @cached_property
    def RetryConfig(self):  # pragma: no cover
        return RetryConfigOutput.make_one(self.boto3_raw_data["RetryConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CanaryScheduleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanaryScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupResourcesResponse:
    boto3_raw_data: "type_defs.ListGroupResourcesResponseTypeDef" = dataclasses.field()

    Resources = field("Resources")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupResourcesResponseTypeDef"]
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
class StartCanaryDryRunResponse:
    boto3_raw_data: "type_defs.StartCanaryDryRunResponseTypeDef" = dataclasses.field()

    @cached_property
    def DryRunConfig(self):  # pragma: no cover
        return DryRunConfigOutput.make_one(self.boto3_raw_data["DryRunConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCanaryDryRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCanaryDryRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupResponse:
    boto3_raw_data: "type_defs.CreateGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Group(self):  # pragma: no cover
        return Group.make_one(self.boto3_raw_data["Group"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupResponseTypeDef"]
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
    def Group(self):  # pragma: no cover
        return Group.make_one(self.boto3_raw_data["Group"])

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
class DescribeRuntimeVersionsResponse:
    boto3_raw_data: "type_defs.DescribeRuntimeVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RuntimeVersions(self):  # pragma: no cover
        return RuntimeVersion.make_many(self.boto3_raw_data["RuntimeVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRuntimeVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuntimeVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedGroupsResponse:
    boto3_raw_data: "type_defs.ListAssociatedGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupSummary.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociatedGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedGroupsResponseTypeDef"]
        ],
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
    def Groups(self):  # pragma: no cover
        return GroupSummary.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class VisualReferenceInput:
    boto3_raw_data: "type_defs.VisualReferenceInputTypeDef" = dataclasses.field()

    BaseCanaryRunId = field("BaseCanaryRunId")
    BaseScreenshots = field("BaseScreenshots")
    BrowserType = field("BrowserType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VisualReferenceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VisualReferenceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanaryLastRun:
    boto3_raw_data: "type_defs.CanaryLastRunTypeDef" = dataclasses.field()

    CanaryName = field("CanaryName")

    @cached_property
    def LastRun(self):  # pragma: no cover
        return CanaryRun.make_one(self.boto3_raw_data["LastRun"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanaryLastRunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanaryLastRunTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCanaryRunsResponse:
    boto3_raw_data: "type_defs.GetCanaryRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def CanaryRuns(self):  # pragma: no cover
        return CanaryRun.make_many(self.boto3_raw_data["CanaryRuns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCanaryRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCanaryRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCanaryRequest:
    boto3_raw_data: "type_defs.CreateCanaryRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Code(self):  # pragma: no cover
        return CanaryCodeInput.make_one(self.boto3_raw_data["Code"])

    ArtifactS3Location = field("ArtifactS3Location")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def Schedule(self):  # pragma: no cover
        return CanaryScheduleInput.make_one(self.boto3_raw_data["Schedule"])

    RuntimeVersion = field("RuntimeVersion")

    @cached_property
    def RunConfig(self):  # pragma: no cover
        return CanaryRunConfigInput.make_one(self.boto3_raw_data["RunConfig"])

    SuccessRetentionPeriodInDays = field("SuccessRetentionPeriodInDays")
    FailureRetentionPeriodInDays = field("FailureRetentionPeriodInDays")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigInput.make_one(self.boto3_raw_data["VpcConfig"])

    ResourcesToReplicateTags = field("ResourcesToReplicateTags")
    ProvisionedResourceCleanup = field("ProvisionedResourceCleanup")

    @cached_property
    def BrowserConfigs(self):  # pragma: no cover
        return BrowserConfig.make_many(self.boto3_raw_data["BrowserConfigs"])

    Tags = field("Tags")

    @cached_property
    def ArtifactConfig(self):  # pragma: no cover
        return ArtifactConfigInput.make_one(self.boto3_raw_data["ArtifactConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCanaryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCanaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Canary:
    boto3_raw_data: "type_defs.CanaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def Code(self):  # pragma: no cover
        return CanaryCodeOutput.make_one(self.boto3_raw_data["Code"])

    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def Schedule(self):  # pragma: no cover
        return CanaryScheduleOutput.make_one(self.boto3_raw_data["Schedule"])

    @cached_property
    def RunConfig(self):  # pragma: no cover
        return CanaryRunConfigOutput.make_one(self.boto3_raw_data["RunConfig"])

    SuccessRetentionPeriodInDays = field("SuccessRetentionPeriodInDays")
    FailureRetentionPeriodInDays = field("FailureRetentionPeriodInDays")

    @cached_property
    def Status(self):  # pragma: no cover
        return CanaryStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Timeline(self):  # pragma: no cover
        return CanaryTimeline.make_one(self.boto3_raw_data["Timeline"])

    ArtifactS3Location = field("ArtifactS3Location")
    EngineArn = field("EngineArn")
    RuntimeVersion = field("RuntimeVersion")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    @cached_property
    def VisualReference(self):  # pragma: no cover
        return VisualReferenceOutput.make_one(self.boto3_raw_data["VisualReference"])

    ProvisionedResourceCleanup = field("ProvisionedResourceCleanup")

    @cached_property
    def BrowserConfigs(self):  # pragma: no cover
        return BrowserConfig.make_many(self.boto3_raw_data["BrowserConfigs"])

    @cached_property
    def EngineConfigs(self):  # pragma: no cover
        return EngineConfig.make_many(self.boto3_raw_data["EngineConfigs"])

    @cached_property
    def VisualReferences(self):  # pragma: no cover
        return VisualReferenceOutput.make_many(self.boto3_raw_data["VisualReferences"])

    Tags = field("Tags")

    @cached_property
    def ArtifactConfig(self):  # pragma: no cover
        return ArtifactConfigOutput.make_one(self.boto3_raw_data["ArtifactConfig"])

    @cached_property
    def DryRunConfig(self):  # pragma: no cover
        return DryRunConfigOutput.make_one(self.boto3_raw_data["DryRunConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCanaryDryRunRequest:
    boto3_raw_data: "type_defs.StartCanaryDryRunRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Code(self):  # pragma: no cover
        return CanaryCodeInput.make_one(self.boto3_raw_data["Code"])

    RuntimeVersion = field("RuntimeVersion")

    @cached_property
    def RunConfig(self):  # pragma: no cover
        return CanaryRunConfigInput.make_one(self.boto3_raw_data["RunConfig"])

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigInput.make_one(self.boto3_raw_data["VpcConfig"])

    ExecutionRoleArn = field("ExecutionRoleArn")
    SuccessRetentionPeriodInDays = field("SuccessRetentionPeriodInDays")
    FailureRetentionPeriodInDays = field("FailureRetentionPeriodInDays")

    @cached_property
    def VisualReference(self):  # pragma: no cover
        return VisualReferenceInput.make_one(self.boto3_raw_data["VisualReference"])

    ArtifactS3Location = field("ArtifactS3Location")

    @cached_property
    def ArtifactConfig(self):  # pragma: no cover
        return ArtifactConfigInput.make_one(self.boto3_raw_data["ArtifactConfig"])

    ProvisionedResourceCleanup = field("ProvisionedResourceCleanup")

    @cached_property
    def BrowserConfigs(self):  # pragma: no cover
        return BrowserConfig.make_many(self.boto3_raw_data["BrowserConfigs"])

    @cached_property
    def VisualReferences(self):  # pragma: no cover
        return VisualReferenceInput.make_many(self.boto3_raw_data["VisualReferences"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCanaryDryRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCanaryDryRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCanaryRequest:
    boto3_raw_data: "type_defs.UpdateCanaryRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Code(self):  # pragma: no cover
        return CanaryCodeInput.make_one(self.boto3_raw_data["Code"])

    ExecutionRoleArn = field("ExecutionRoleArn")
    RuntimeVersion = field("RuntimeVersion")

    @cached_property
    def Schedule(self):  # pragma: no cover
        return CanaryScheduleInput.make_one(self.boto3_raw_data["Schedule"])

    @cached_property
    def RunConfig(self):  # pragma: no cover
        return CanaryRunConfigInput.make_one(self.boto3_raw_data["RunConfig"])

    SuccessRetentionPeriodInDays = field("SuccessRetentionPeriodInDays")
    FailureRetentionPeriodInDays = field("FailureRetentionPeriodInDays")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigInput.make_one(self.boto3_raw_data["VpcConfig"])

    @cached_property
    def VisualReference(self):  # pragma: no cover
        return VisualReferenceInput.make_one(self.boto3_raw_data["VisualReference"])

    ArtifactS3Location = field("ArtifactS3Location")

    @cached_property
    def ArtifactConfig(self):  # pragma: no cover
        return ArtifactConfigInput.make_one(self.boto3_raw_data["ArtifactConfig"])

    ProvisionedResourceCleanup = field("ProvisionedResourceCleanup")
    DryRunId = field("DryRunId")

    @cached_property
    def VisualReferences(self):  # pragma: no cover
        return VisualReferenceInput.make_many(self.boto3_raw_data["VisualReferences"])

    @cached_property
    def BrowserConfigs(self):  # pragma: no cover
        return BrowserConfig.make_many(self.boto3_raw_data["BrowserConfigs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCanaryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCanaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCanariesLastRunResponse:
    boto3_raw_data: "type_defs.DescribeCanariesLastRunResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CanariesLastRun(self):  # pragma: no cover
        return CanaryLastRun.make_many(self.boto3_raw_data["CanariesLastRun"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCanariesLastRunResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCanariesLastRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCanaryResponse:
    boto3_raw_data: "type_defs.CreateCanaryResponseTypeDef" = dataclasses.field()

    @cached_property
    def Canary(self):  # pragma: no cover
        return Canary.make_one(self.boto3_raw_data["Canary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCanaryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCanaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCanariesResponse:
    boto3_raw_data: "type_defs.DescribeCanariesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Canaries(self):  # pragma: no cover
        return Canary.make_many(self.boto3_raw_data["Canaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCanariesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCanariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCanaryResponse:
    boto3_raw_data: "type_defs.GetCanaryResponseTypeDef" = dataclasses.field()

    @cached_property
    def Canary(self):  # pragma: no cover
        return Canary.make_one(self.boto3_raw_data["Canary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetCanaryResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCanaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
