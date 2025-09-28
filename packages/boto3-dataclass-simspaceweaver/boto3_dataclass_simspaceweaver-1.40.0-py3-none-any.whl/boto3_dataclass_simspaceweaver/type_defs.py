# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_simspaceweaver import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsLogGroup:
    boto3_raw_data: "type_defs.CloudWatchLogsLogGroupTypeDef" = dataclasses.field()

    LogGroupArn = field("LogGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsLogGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsLogGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Destination:
    boto3_raw_data: "type_defs.S3DestinationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKeyPrefix = field("ObjectKeyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppInput:
    boto3_raw_data: "type_defs.DeleteAppInputTypeDef" = dataclasses.field()

    App = field("App")
    Domain = field("Domain")
    Simulation = field("Simulation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAppInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteAppInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSimulationInput:
    boto3_raw_data: "type_defs.DeleteSimulationInputTypeDef" = dataclasses.field()

    Simulation = field("Simulation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSimulationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSimulationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppInput:
    boto3_raw_data: "type_defs.DescribeAppInputTypeDef" = dataclasses.field()

    App = field("App")
    Domain = field("Domain")
    Simulation = field("Simulation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeAppInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchOverridesOutput:
    boto3_raw_data: "type_defs.LaunchOverridesOutputTypeDef" = dataclasses.field()

    LaunchCommands = field("LaunchCommands")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchOverridesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchOverridesOutputTypeDef"]
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
class DescribeSimulationInput:
    boto3_raw_data: "type_defs.DescribeSimulationInputTypeDef" = dataclasses.field()

    Simulation = field("Simulation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSimulationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSimulationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectKey = field("ObjectKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Domain:
    boto3_raw_data: "type_defs.DomainTypeDef" = dataclasses.field()

    Lifecycle = field("Lifecycle")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchOverrides:
    boto3_raw_data: "type_defs.LaunchOverridesTypeDef" = dataclasses.field()

    LaunchCommands = field("LaunchCommands")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchOverridesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchOverridesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsInput:
    boto3_raw_data: "type_defs.ListAppsInputTypeDef" = dataclasses.field()

    Simulation = field("Simulation")
    Domain = field("Domain")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAppsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListAppsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationAppMetadata:
    boto3_raw_data: "type_defs.SimulationAppMetadataTypeDef" = dataclasses.field()

    Domain = field("Domain")
    Name = field("Name")
    Simulation = field("Simulation")
    Status = field("Status")
    TargetStatus = field("TargetStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationAppMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationAppMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationsInput:
    boto3_raw_data: "type_defs.ListSimulationsInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSimulationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationMetadata:
    boto3_raw_data: "type_defs.SimulationMetadataTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    Name = field("Name")
    Status = field("Status")
    TargetStatus = field("TargetStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationMetadataTypeDef"]
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
class SimulationClock:
    boto3_raw_data: "type_defs.SimulationClockTypeDef" = dataclasses.field()

    Status = field("Status")
    TargetStatus = field("TargetStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SimulationClockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SimulationClockTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationAppPortMapping:
    boto3_raw_data: "type_defs.SimulationAppPortMappingTypeDef" = dataclasses.field()

    Actual = field("Actual")
    Declared = field("Declared")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationAppPortMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationAppPortMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartClockInput:
    boto3_raw_data: "type_defs.StartClockInputTypeDef" = dataclasses.field()

    Simulation = field("Simulation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartClockInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartClockInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopAppInput:
    boto3_raw_data: "type_defs.StopAppInputTypeDef" = dataclasses.field()

    App = field("App")
    Domain = field("Domain")
    Simulation = field("Simulation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopAppInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopAppInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopClockInput:
    boto3_raw_data: "type_defs.StopClockInputTypeDef" = dataclasses.field()

    Simulation = field("Simulation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopClockInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopClockInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSimulationInput:
    boto3_raw_data: "type_defs.StopSimulationInputTypeDef" = dataclasses.field()

    Simulation = field("Simulation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopSimulationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSimulationInputTypeDef"]
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
class LogDestination:
    boto3_raw_data: "type_defs.LogDestinationTypeDef" = dataclasses.field()

    @cached_property
    def CloudWatchLogsLogGroup(self):  # pragma: no cover
        return CloudWatchLogsLogGroup.make_one(
            self.boto3_raw_data["CloudWatchLogsLogGroup"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogDestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotInput:
    boto3_raw_data: "type_defs.CreateSnapshotInputTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["Destination"])

    Simulation = field("Simulation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotInputTypeDef"]
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
class StartAppOutput:
    boto3_raw_data: "type_defs.StartAppOutputTypeDef" = dataclasses.field()

    Domain = field("Domain")
    Name = field("Name")
    Simulation = field("Simulation")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartAppOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartAppOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSimulationOutput:
    boto3_raw_data: "type_defs.StartSimulationOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    ExecutionId = field("ExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSimulationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSimulationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSimulationInput:
    boto3_raw_data: "type_defs.StartSimulationInputTypeDef" = dataclasses.field()

    Name = field("Name")
    RoleArn = field("RoleArn")
    ClientToken = field("ClientToken")
    Description = field("Description")
    MaximumDuration = field("MaximumDuration")

    @cached_property
    def SchemaS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SchemaS3Location"])

    @cached_property
    def SnapshotS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SnapshotS3Location"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSimulationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSimulationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsOutput:
    boto3_raw_data: "type_defs.ListAppsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Apps(self):  # pragma: no cover
        return SimulationAppMetadata.make_many(self.boto3_raw_data["Apps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAppsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListAppsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationsOutput:
    boto3_raw_data: "type_defs.ListSimulationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Simulations(self):  # pragma: no cover
        return SimulationMetadata.make_many(self.boto3_raw_data["Simulations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSimulationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveSimulationState:
    boto3_raw_data: "type_defs.LiveSimulationStateTypeDef" = dataclasses.field()

    @cached_property
    def Clocks(self):  # pragma: no cover
        return SimulationClock.make_many(self.boto3_raw_data["Clocks"])

    @cached_property
    def Domains(self):  # pragma: no cover
        return Domain.make_many(self.boto3_raw_data["Domains"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LiveSimulationStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiveSimulationStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationAppEndpointInfo:
    boto3_raw_data: "type_defs.SimulationAppEndpointInfoTypeDef" = dataclasses.field()

    Address = field("Address")

    @cached_property
    def IngressPortMappings(self):  # pragma: no cover
        return SimulationAppPortMapping.make_many(
            self.boto3_raw_data["IngressPortMappings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationAppEndpointInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationAppEndpointInfoTypeDef"]
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
    def Destinations(self):  # pragma: no cover
        return LogDestination.make_many(self.boto3_raw_data["Destinations"])

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
class StartAppInput:
    boto3_raw_data: "type_defs.StartAppInputTypeDef" = dataclasses.field()

    Domain = field("Domain")
    Name = field("Name")
    Simulation = field("Simulation")
    ClientToken = field("ClientToken")
    Description = field("Description")
    LaunchOverrides = field("LaunchOverrides")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartAppInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartAppInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppOutput:
    boto3_raw_data: "type_defs.DescribeAppOutputTypeDef" = dataclasses.field()

    Description = field("Description")
    Domain = field("Domain")

    @cached_property
    def EndpointInfo(self):  # pragma: no cover
        return SimulationAppEndpointInfo.make_one(self.boto3_raw_data["EndpointInfo"])

    @cached_property
    def LaunchOverrides(self):  # pragma: no cover
        return LaunchOverridesOutput.make_one(self.boto3_raw_data["LaunchOverrides"])

    Name = field("Name")
    Simulation = field("Simulation")
    Status = field("Status")
    TargetStatus = field("TargetStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeAppOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSimulationOutput:
    boto3_raw_data: "type_defs.DescribeSimulationOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    Description = field("Description")
    ExecutionId = field("ExecutionId")

    @cached_property
    def LiveSimulationState(self):  # pragma: no cover
        return LiveSimulationState.make_one(self.boto3_raw_data["LiveSimulationState"])

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfiguration.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    MaximumDuration = field("MaximumDuration")
    Name = field("Name")
    RoleArn = field("RoleArn")
    SchemaError = field("SchemaError")

    @cached_property
    def SchemaS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SchemaS3Location"])

    @cached_property
    def SnapshotS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SnapshotS3Location"])

    StartError = field("StartError")
    Status = field("Status")
    TargetStatus = field("TargetStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSimulationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSimulationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
