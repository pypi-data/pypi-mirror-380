# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_robomaker import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BatchDeleteWorldsRequest:
    boto3_raw_data: "type_defs.BatchDeleteWorldsRequestTypeDef" = dataclasses.field()

    worlds = field("worlds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteWorldsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteWorldsRequestTypeDef"]
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
class BatchDescribeSimulationJobRequest:
    boto3_raw_data: "type_defs.BatchDescribeSimulationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobs = field("jobs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDescribeSimulationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeSimulationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPolicy:
    boto3_raw_data: "type_defs.BatchPolicyTypeDef" = dataclasses.field()

    timeoutInSeconds = field("timeoutInSeconds")
    maxConcurrency = field("maxConcurrency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchPolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelDeploymentJobRequest:
    boto3_raw_data: "type_defs.CancelDeploymentJobRequestTypeDef" = dataclasses.field()

    job = field("job")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelDeploymentJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelDeploymentJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelSimulationJobBatchRequest:
    boto3_raw_data: "type_defs.CancelSimulationJobBatchRequestTypeDef" = (
        dataclasses.field()
    )

    batch = field("batch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelSimulationJobBatchRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSimulationJobBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelSimulationJobRequest:
    boto3_raw_data: "type_defs.CancelSimulationJobRequestTypeDef" = dataclasses.field()

    job = field("job")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSimulationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSimulationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelWorldExportJobRequest:
    boto3_raw_data: "type_defs.CancelWorldExportJobRequestTypeDef" = dataclasses.field()

    job = field("job")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelWorldExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelWorldExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelWorldGenerationJobRequest:
    boto3_raw_data: "type_defs.CancelWorldGenerationJobRequestTypeDef" = (
        dataclasses.field()
    )

    job = field("job")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelWorldGenerationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelWorldGenerationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeResponse:
    boto3_raw_data: "type_defs.ComputeResponseTypeDef" = dataclasses.field()

    simulationUnitLimit = field("simulationUnitLimit")
    computeType = field("computeType")
    gpuUnitLimit = field("gpuUnitLimit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputeResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Compute:
    boto3_raw_data: "type_defs.ComputeTypeDef" = dataclasses.field()

    simulationUnitLimit = field("simulationUnitLimit")
    computeType = field("computeType")
    gpuUnitLimit = field("gpuUnitLimit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetRequest:
    boto3_raw_data: "type_defs.CreateFleetRequestTypeDef" = dataclasses.field()

    name = field("name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetRequestTypeDef"]
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

    uri = field("uri")

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
class RobotSoftwareSuite:
    boto3_raw_data: "type_defs.RobotSoftwareSuiteTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RobotSoftwareSuiteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RobotSoftwareSuiteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfig:
    boto3_raw_data: "type_defs.SourceConfigTypeDef" = dataclasses.field()

    s3Bucket = field("s3Bucket")
    s3Key = field("s3Key")
    architecture = field("architecture")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Source:
    boto3_raw_data: "type_defs.SourceTypeDef" = dataclasses.field()

    s3Bucket = field("s3Bucket")
    s3Key = field("s3Key")
    etag = field("etag")
    architecture = field("architecture")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRobotApplicationVersionRequest:
    boto3_raw_data: "type_defs.CreateRobotApplicationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    application = field("application")
    currentRevisionId = field("currentRevisionId")
    s3Etags = field("s3Etags")
    imageDigest = field("imageDigest")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRobotApplicationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRobotApplicationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRobotRequest:
    boto3_raw_data: "type_defs.CreateRobotRequestTypeDef" = dataclasses.field()

    name = field("name")
    architecture = field("architecture")
    greengrassGroupId = field("greengrassGroupId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRobotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRobotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenderingEngine:
    boto3_raw_data: "type_defs.RenderingEngineTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RenderingEngineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RenderingEngineTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationSoftwareSuite:
    boto3_raw_data: "type_defs.SimulationSoftwareSuiteTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationSoftwareSuiteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationSoftwareSuiteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSimulationApplicationVersionRequest:
    boto3_raw_data: "type_defs.CreateSimulationApplicationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    application = field("application")
    currentRevisionId = field("currentRevisionId")
    s3Etags = field("s3Etags")
    imageDigest = field("imageDigest")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSimulationApplicationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSimulationApplicationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfig:
    boto3_raw_data: "type_defs.LoggingConfigTypeDef" = dataclasses.field()

    recordAllRosTopics = field("recordAllRosTopics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputLocation:
    boto3_raw_data: "type_defs.OutputLocationTypeDef" = dataclasses.field()

    s3Bucket = field("s3Bucket")
    s3Prefix = field("s3Prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VPCConfigResponse:
    boto3_raw_data: "type_defs.VPCConfigResponseTypeDef" = dataclasses.field()

    subnets = field("subnets")
    securityGroups = field("securityGroups")
    vpcId = field("vpcId")
    assignPublicIp = field("assignPublicIp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VPCConfigResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VPCConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorldCount:
    boto3_raw_data: "type_defs.WorldCountTypeDef" = dataclasses.field()

    floorplanCount = field("floorplanCount")
    interiorCountPerFloorplan = field("interiorCountPerFloorplan")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorldCountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorldCountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateLocation:
    boto3_raw_data: "type_defs.TemplateLocationTypeDef" = dataclasses.field()

    s3Bucket = field("s3Bucket")
    s3Key = field("s3Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfigOutput:
    boto3_raw_data: "type_defs.DataSourceConfigOutputTypeDef" = dataclasses.field()

    name = field("name")
    s3Bucket = field("s3Bucket")
    s3Keys = field("s3Keys")
    type = field("type")
    destination = field("destination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfig:
    boto3_raw_data: "type_defs.DataSourceConfigTypeDef" = dataclasses.field()

    name = field("name")
    s3Bucket = field("s3Bucket")
    s3Keys = field("s3Keys")
    type = field("type")
    destination = field("destination")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3KeyOutput:
    boto3_raw_data: "type_defs.S3KeyOutputTypeDef" = dataclasses.field()

    s3Key = field("s3Key")
    etag = field("etag")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3KeyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3KeyOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetRequest:
    boto3_raw_data: "type_defs.DeleteFleetRequestTypeDef" = dataclasses.field()

    fleet = field("fleet")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRobotApplicationRequest:
    boto3_raw_data: "type_defs.DeleteRobotApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    application = field("application")
    applicationVersion = field("applicationVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRobotApplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRobotApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRobotRequest:
    boto3_raw_data: "type_defs.DeleteRobotRequestTypeDef" = dataclasses.field()

    robot = field("robot")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRobotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRobotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSimulationApplicationRequest:
    boto3_raw_data: "type_defs.DeleteSimulationApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    application = field("application")
    applicationVersion = field("applicationVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSimulationApplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSimulationApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorldTemplateRequest:
    boto3_raw_data: "type_defs.DeleteWorldTemplateRequestTypeDef" = dataclasses.field()

    template = field("template")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorldTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorldTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentLaunchConfigOutput:
    boto3_raw_data: "type_defs.DeploymentLaunchConfigOutputTypeDef" = (
        dataclasses.field()
    )

    packageName = field("packageName")
    launchFile = field("launchFile")
    preLaunchFile = field("preLaunchFile")
    postLaunchFile = field("postLaunchFile")
    environmentVariables = field("environmentVariables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentLaunchConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentLaunchConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Object:
    boto3_raw_data: "type_defs.S3ObjectTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")
    etag = field("etag")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentLaunchConfig:
    boto3_raw_data: "type_defs.DeploymentLaunchConfigTypeDef" = dataclasses.field()

    packageName = field("packageName")
    launchFile = field("launchFile")
    preLaunchFile = field("preLaunchFile")
    postLaunchFile = field("postLaunchFile")
    environmentVariables = field("environmentVariables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentLaunchConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentLaunchConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterRobotRequest:
    boto3_raw_data: "type_defs.DeregisterRobotRequestTypeDef" = dataclasses.field()

    fleet = field("fleet")
    robot = field("robot")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterRobotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterRobotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeploymentJobRequest:
    boto3_raw_data: "type_defs.DescribeDeploymentJobRequestTypeDef" = (
        dataclasses.field()
    )

    job = field("job")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeploymentJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeploymentJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetRequest:
    boto3_raw_data: "type_defs.DescribeFleetRequestTypeDef" = dataclasses.field()

    fleet = field("fleet")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Robot:
    boto3_raw_data: "type_defs.RobotTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    fleetArn = field("fleetArn")
    status = field("status")
    greenGrassGroupId = field("greenGrassGroupId")
    createdAt = field("createdAt")
    architecture = field("architecture")
    lastDeploymentJob = field("lastDeploymentJob")
    lastDeploymentTime = field("lastDeploymentTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RobotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RobotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRobotApplicationRequest:
    boto3_raw_data: "type_defs.DescribeRobotApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    application = field("application")
    applicationVersion = field("applicationVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRobotApplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRobotApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRobotRequest:
    boto3_raw_data: "type_defs.DescribeRobotRequestTypeDef" = dataclasses.field()

    robot = field("robot")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRobotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRobotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSimulationApplicationRequest:
    boto3_raw_data: "type_defs.DescribeSimulationApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    application = field("application")
    applicationVersion = field("applicationVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSimulationApplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSimulationApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSimulationJobBatchRequest:
    boto3_raw_data: "type_defs.DescribeSimulationJobBatchRequestTypeDef" = (
        dataclasses.field()
    )

    batch = field("batch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSimulationJobBatchRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSimulationJobBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationJobSummary:
    boto3_raw_data: "type_defs.SimulationJobSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    status = field("status")
    simulationApplicationNames = field("simulationApplicationNames")
    robotApplicationNames = field("robotApplicationNames")
    dataSourceNames = field("dataSourceNames")
    computeType = field("computeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSimulationJobRequest:
    boto3_raw_data: "type_defs.DescribeSimulationJobRequestTypeDef" = (
        dataclasses.field()
    )

    job = field("job")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSimulationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSimulationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInterface:
    boto3_raw_data: "type_defs.NetworkInterfaceTypeDef" = dataclasses.field()

    networkInterfaceId = field("networkInterfaceId")
    privateIpAddress = field("privateIpAddress")
    publicIpAddress = field("publicIpAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorldExportJobRequest:
    boto3_raw_data: "type_defs.DescribeWorldExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    job = field("job")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorldExportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorldExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorldGenerationJobRequest:
    boto3_raw_data: "type_defs.DescribeWorldGenerationJobRequestTypeDef" = (
        dataclasses.field()
    )

    job = field("job")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorldGenerationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorldGenerationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorldRequest:
    boto3_raw_data: "type_defs.DescribeWorldRequestTypeDef" = dataclasses.field()

    world = field("world")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorldRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorldRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorldTemplateRequest:
    boto3_raw_data: "type_defs.DescribeWorldTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    template = field("template")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorldTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorldTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorldFailure:
    boto3_raw_data: "type_defs.WorldFailureTypeDef" = dataclasses.field()

    failureCode = field("failureCode")
    sampleFailureReason = field("sampleFailureReason")
    failureCount = field("failureCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorldFailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorldFailureTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

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
class Fleet:
    boto3_raw_data: "type_defs.FleetTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    createdAt = field("createdAt")
    lastDeploymentStatus = field("lastDeploymentStatus")
    lastDeploymentJob = field("lastDeploymentJob")
    lastDeploymentTime = field("lastDeploymentTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorldTemplateBodyRequest:
    boto3_raw_data: "type_defs.GetWorldTemplateBodyRequestTypeDef" = dataclasses.field()

    template = field("template")
    generationJob = field("generationJob")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorldTemplateBodyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorldTemplateBodyRequestTypeDef"]
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
class SimulationJobBatchSummary:
    boto3_raw_data: "type_defs.SimulationJobBatchSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    lastUpdatedAt = field("lastUpdatedAt")
    createdAt = field("createdAt")
    status = field("status")
    failedRequestCount = field("failedRequestCount")
    pendingRequestCount = field("pendingRequestCount")
    createdRequestCount = field("createdRequestCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationJobBatchSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationJobBatchSummaryTypeDef"]
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
class ListWorldTemplatesRequest:
    boto3_raw_data: "type_defs.ListWorldTemplatesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorldTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateSummary:
    boto3_raw_data: "type_defs.TemplateSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorldSummary:
    boto3_raw_data: "type_defs.WorldSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    generationJob = field("generationJob")
    template = field("template")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorldSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorldSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortMapping:
    boto3_raw_data: "type_defs.PortMappingTypeDef" = dataclasses.field()

    jobPort = field("jobPort")
    applicationPort = field("applicationPort")
    enableOnPublicIp = field("enableOnPublicIp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortMappingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProgressDetail:
    boto3_raw_data: "type_defs.ProgressDetailTypeDef" = dataclasses.field()

    currentProgress = field("currentProgress")
    percentDone = field("percentDone")
    estimatedTimeRemainingSeconds = field("estimatedTimeRemainingSeconds")
    targetResource = field("targetResource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProgressDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProgressDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterRobotRequest:
    boto3_raw_data: "type_defs.RegisterRobotRequestTypeDef" = dataclasses.field()

    fleet = field("fleet")
    robot = field("robot")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterRobotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterRobotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestartSimulationJobRequest:
    boto3_raw_data: "type_defs.RestartSimulationJobRequestTypeDef" = dataclasses.field()

    job = field("job")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestartSimulationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestartSimulationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tool:
    boto3_raw_data: "type_defs.ToolTypeDef" = dataclasses.field()

    name = field("name")
    command = field("command")
    streamUI = field("streamUI")
    streamOutputToCloudWatch = field("streamOutputToCloudWatch")
    exitBehavior = field("exitBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadConfiguration:
    boto3_raw_data: "type_defs.UploadConfigurationTypeDef" = dataclasses.field()

    name = field("name")
    path = field("path")
    uploadBehavior = field("uploadBehavior")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorldConfig:
    boto3_raw_data: "type_defs.WorldConfigTypeDef" = dataclasses.field()

    world = field("world")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorldConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorldConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VPCConfigOutput:
    boto3_raw_data: "type_defs.VPCConfigOutputTypeDef" = dataclasses.field()

    subnets = field("subnets")
    securityGroups = field("securityGroups")
    assignPublicIp = field("assignPublicIp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VPCConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VPCConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncDeploymentJobRequest:
    boto3_raw_data: "type_defs.SyncDeploymentJobRequestTypeDef" = dataclasses.field()

    clientRequestToken = field("clientRequestToken")
    fleet = field("fleet")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SyncDeploymentJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SyncDeploymentJobRequestTypeDef"]
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
class VPCConfig:
    boto3_raw_data: "type_defs.VPCConfigTypeDef" = dataclasses.field()

    subnets = field("subnets")
    securityGroups = field("securityGroups")
    assignPublicIp = field("assignPublicIp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VPCConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VPCConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteWorldsResponse:
    boto3_raw_data: "type_defs.BatchDeleteWorldsResponseTypeDef" = dataclasses.field()

    unprocessedWorlds = field("unprocessedWorlds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteWorldsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteWorldsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetResponse:
    boto3_raw_data: "type_defs.CreateFleetResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    createdAt = field("createdAt")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRobotResponse:
    boto3_raw_data: "type_defs.CreateRobotResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    createdAt = field("createdAt")
    greengrassGroupId = field("greengrassGroupId")
    architecture = field("architecture")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRobotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRobotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorldTemplateResponse:
    boto3_raw_data: "type_defs.CreateWorldTemplateResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    clientRequestToken = field("clientRequestToken")
    createdAt = field("createdAt")
    name = field("name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorldTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorldTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterRobotResponse:
    boto3_raw_data: "type_defs.DeregisterRobotResponseTypeDef" = dataclasses.field()

    fleet = field("fleet")
    robot = field("robot")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterRobotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterRobotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRobotResponse:
    boto3_raw_data: "type_defs.DescribeRobotResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    fleetArn = field("fleetArn")
    status = field("status")
    greengrassGroupId = field("greengrassGroupId")
    createdAt = field("createdAt")
    architecture = field("architecture")
    lastDeploymentJob = field("lastDeploymentJob")
    lastDeploymentTime = field("lastDeploymentTime")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRobotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRobotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorldResponse:
    boto3_raw_data: "type_defs.DescribeWorldResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    generationJob = field("generationJob")
    template = field("template")
    createdAt = field("createdAt")
    tags = field("tags")
    worldDescriptionBody = field("worldDescriptionBody")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorldResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorldResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorldTemplateResponse:
    boto3_raw_data: "type_defs.DescribeWorldTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    clientRequestToken = field("clientRequestToken")
    name = field("name")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    tags = field("tags")
    version = field("version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorldTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorldTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorldTemplateBodyResponse:
    boto3_raw_data: "type_defs.GetWorldTemplateBodyResponseTypeDef" = (
        dataclasses.field()
    )

    templateBody = field("templateBody")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorldTemplateBodyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorldTemplateBodyResponseTypeDef"]
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
class RegisterRobotResponse:
    boto3_raw_data: "type_defs.RegisterRobotResponseTypeDef" = dataclasses.field()

    fleet = field("fleet")
    robot = field("robot")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterRobotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterRobotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorldTemplateResponse:
    boto3_raw_data: "type_defs.UpdateWorldTemplateResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorldTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorldTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RobotApplicationSummary:
    boto3_raw_data: "type_defs.RobotApplicationSummaryTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    version = field("version")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RobotApplicationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RobotApplicationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRobotApplicationRequest:
    boto3_raw_data: "type_defs.CreateRobotApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @cached_property
    def sources(self):  # pragma: no cover
        return SourceConfig.make_many(self.boto3_raw_data["sources"])

    tags = field("tags")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRobotApplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRobotApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRobotApplicationRequest:
    boto3_raw_data: "type_defs.UpdateRobotApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    application = field("application")

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @cached_property
    def sources(self):  # pragma: no cover
        return SourceConfig.make_many(self.boto3_raw_data["sources"])

    currentRevisionId = field("currentRevisionId")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRobotApplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRobotApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRobotApplicationResponse:
    boto3_raw_data: "type_defs.CreateRobotApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    version = field("version")

    @cached_property
    def sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    lastUpdatedAt = field("lastUpdatedAt")
    revisionId = field("revisionId")
    tags = field("tags")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRobotApplicationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRobotApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRobotApplicationVersionResponse:
    boto3_raw_data: "type_defs.CreateRobotApplicationVersionResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    version = field("version")

    @cached_property
    def sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    lastUpdatedAt = field("lastUpdatedAt")
    revisionId = field("revisionId")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRobotApplicationVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRobotApplicationVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRobotApplicationResponse:
    boto3_raw_data: "type_defs.DescribeRobotApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    version = field("version")

    @cached_property
    def sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    revisionId = field("revisionId")
    lastUpdatedAt = field("lastUpdatedAt")
    tags = field("tags")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    imageDigest = field("imageDigest")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRobotApplicationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRobotApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRobotApplicationResponse:
    boto3_raw_data: "type_defs.UpdateRobotApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    version = field("version")

    @cached_property
    def sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    lastUpdatedAt = field("lastUpdatedAt")
    revisionId = field("revisionId")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRobotApplicationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRobotApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSimulationApplicationRequest:
    boto3_raw_data: "type_defs.CreateSimulationApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def simulationSoftwareSuite(self):  # pragma: no cover
        return SimulationSoftwareSuite.make_one(
            self.boto3_raw_data["simulationSoftwareSuite"]
        )

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @cached_property
    def sources(self):  # pragma: no cover
        return SourceConfig.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def renderingEngine(self):  # pragma: no cover
        return RenderingEngine.make_one(self.boto3_raw_data["renderingEngine"])

    tags = field("tags")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSimulationApplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSimulationApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSimulationApplicationResponse:
    boto3_raw_data: "type_defs.CreateSimulationApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    version = field("version")

    @cached_property
    def sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def simulationSoftwareSuite(self):  # pragma: no cover
        return SimulationSoftwareSuite.make_one(
            self.boto3_raw_data["simulationSoftwareSuite"]
        )

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @cached_property
    def renderingEngine(self):  # pragma: no cover
        return RenderingEngine.make_one(self.boto3_raw_data["renderingEngine"])

    lastUpdatedAt = field("lastUpdatedAt")
    revisionId = field("revisionId")
    tags = field("tags")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSimulationApplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSimulationApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSimulationApplicationVersionResponse:
    boto3_raw_data: "type_defs.CreateSimulationApplicationVersionResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    version = field("version")

    @cached_property
    def sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def simulationSoftwareSuite(self):  # pragma: no cover
        return SimulationSoftwareSuite.make_one(
            self.boto3_raw_data["simulationSoftwareSuite"]
        )

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @cached_property
    def renderingEngine(self):  # pragma: no cover
        return RenderingEngine.make_one(self.boto3_raw_data["renderingEngine"])

    lastUpdatedAt = field("lastUpdatedAt")
    revisionId = field("revisionId")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSimulationApplicationVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSimulationApplicationVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSimulationApplicationResponse:
    boto3_raw_data: "type_defs.DescribeSimulationApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    version = field("version")

    @cached_property
    def sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def simulationSoftwareSuite(self):  # pragma: no cover
        return SimulationSoftwareSuite.make_one(
            self.boto3_raw_data["simulationSoftwareSuite"]
        )

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @cached_property
    def renderingEngine(self):  # pragma: no cover
        return RenderingEngine.make_one(self.boto3_raw_data["renderingEngine"])

    revisionId = field("revisionId")
    lastUpdatedAt = field("lastUpdatedAt")
    tags = field("tags")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    imageDigest = field("imageDigest")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSimulationApplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSimulationApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationApplicationSummary:
    boto3_raw_data: "type_defs.SimulationApplicationSummaryTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    arn = field("arn")
    version = field("version")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @cached_property
    def simulationSoftwareSuite(self):  # pragma: no cover
        return SimulationSoftwareSuite.make_one(
            self.boto3_raw_data["simulationSoftwareSuite"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationApplicationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationApplicationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSimulationApplicationRequest:
    boto3_raw_data: "type_defs.UpdateSimulationApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    application = field("application")

    @cached_property
    def simulationSoftwareSuite(self):  # pragma: no cover
        return SimulationSoftwareSuite.make_one(
            self.boto3_raw_data["simulationSoftwareSuite"]
        )

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @cached_property
    def sources(self):  # pragma: no cover
        return SourceConfig.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def renderingEngine(self):  # pragma: no cover
        return RenderingEngine.make_one(self.boto3_raw_data["renderingEngine"])

    currentRevisionId = field("currentRevisionId")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSimulationApplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSimulationApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSimulationApplicationResponse:
    boto3_raw_data: "type_defs.UpdateSimulationApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    version = field("version")

    @cached_property
    def sources(self):  # pragma: no cover
        return Source.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def simulationSoftwareSuite(self):  # pragma: no cover
        return SimulationSoftwareSuite.make_one(
            self.boto3_raw_data["simulationSoftwareSuite"]
        )

    @cached_property
    def robotSoftwareSuite(self):  # pragma: no cover
        return RobotSoftwareSuite.make_one(self.boto3_raw_data["robotSoftwareSuite"])

    @cached_property
    def renderingEngine(self):  # pragma: no cover
        return RenderingEngine.make_one(self.boto3_raw_data["renderingEngine"])

    lastUpdatedAt = field("lastUpdatedAt")
    revisionId = field("revisionId")

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSimulationApplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSimulationApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorldExportJobRequest:
    boto3_raw_data: "type_defs.CreateWorldExportJobRequestTypeDef" = dataclasses.field()

    worlds = field("worlds")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    iamRole = field("iamRole")
    clientRequestToken = field("clientRequestToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorldExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorldExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorldExportJobResponse:
    boto3_raw_data: "type_defs.CreateWorldExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    failureCode = field("failureCode")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    iamRole = field("iamRole")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorldExportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorldExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorldExportJobResponse:
    boto3_raw_data: "type_defs.DescribeWorldExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    failureCode = field("failureCode")
    failureReason = field("failureReason")
    clientRequestToken = field("clientRequestToken")
    worlds = field("worlds")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    iamRole = field("iamRole")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorldExportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorldExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorldExportJobSummary:
    boto3_raw_data: "type_defs.WorldExportJobSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    worlds = field("worlds")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorldExportJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorldExportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorldGenerationJobRequest:
    boto3_raw_data: "type_defs.CreateWorldGenerationJobRequestTypeDef" = (
        dataclasses.field()
    )

    template = field("template")

    @cached_property
    def worldCount(self):  # pragma: no cover
        return WorldCount.make_one(self.boto3_raw_data["worldCount"])

    clientRequestToken = field("clientRequestToken")
    tags = field("tags")
    worldTags = field("worldTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorldGenerationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorldGenerationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorldGenerationJobResponse:
    boto3_raw_data: "type_defs.CreateWorldGenerationJobResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    failureCode = field("failureCode")
    clientRequestToken = field("clientRequestToken")
    template = field("template")

    @cached_property
    def worldCount(self):  # pragma: no cover
        return WorldCount.make_one(self.boto3_raw_data["worldCount"])

    tags = field("tags")
    worldTags = field("worldTags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorldGenerationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorldGenerationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorldGenerationJobSummary:
    boto3_raw_data: "type_defs.WorldGenerationJobSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    template = field("template")
    createdAt = field("createdAt")
    status = field("status")

    @cached_property
    def worldCount(self):  # pragma: no cover
        return WorldCount.make_one(self.boto3_raw_data["worldCount"])

    succeededWorldCount = field("succeededWorldCount")
    failedWorldCount = field("failedWorldCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorldGenerationJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorldGenerationJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorldTemplateRequest:
    boto3_raw_data: "type_defs.CreateWorldTemplateRequestTypeDef" = dataclasses.field()

    clientRequestToken = field("clientRequestToken")
    name = field("name")
    templateBody = field("templateBody")

    @cached_property
    def templateLocation(self):  # pragma: no cover
        return TemplateLocation.make_one(self.boto3_raw_data["templateLocation"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorldTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorldTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorldTemplateRequest:
    boto3_raw_data: "type_defs.UpdateWorldTemplateRequestTypeDef" = dataclasses.field()

    template = field("template")
    name = field("name")
    templateBody = field("templateBody")

    @cached_property
    def templateLocation(self):  # pragma: no cover
        return TemplateLocation.make_one(self.boto3_raw_data["templateLocation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorldTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorldTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    name = field("name")
    s3Bucket = field("s3Bucket")

    @cached_property
    def s3Keys(self):  # pragma: no cover
        return S3KeyOutput.make_many(self.boto3_raw_data["s3Keys"])

    type = field("type")
    destination = field("destination")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentApplicationConfigOutput:
    boto3_raw_data: "type_defs.DeploymentApplicationConfigOutputTypeDef" = (
        dataclasses.field()
    )

    application = field("application")
    applicationVersion = field("applicationVersion")

    @cached_property
    def launchConfig(self):  # pragma: no cover
        return DeploymentLaunchConfigOutput.make_one(
            self.boto3_raw_data["launchConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeploymentApplicationConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentApplicationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentConfig:
    boto3_raw_data: "type_defs.DeploymentConfigTypeDef" = dataclasses.field()

    concurrentDeploymentPercentage = field("concurrentDeploymentPercentage")
    failureThresholdPercentage = field("failureThresholdPercentage")
    robotDeploymentTimeoutInSeconds = field("robotDeploymentTimeoutInSeconds")

    @cached_property
    def downloadConditionFile(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["downloadConditionFile"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetResponse:
    boto3_raw_data: "type_defs.DescribeFleetResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def robots(self):  # pragma: no cover
        return Robot.make_many(self.boto3_raw_data["robots"])

    createdAt = field("createdAt")
    lastDeploymentStatus = field("lastDeploymentStatus")
    lastDeploymentJob = field("lastDeploymentJob")
    lastDeploymentTime = field("lastDeploymentTime")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRobotsResponse:
    boto3_raw_data: "type_defs.ListRobotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def robots(self):  # pragma: no cover
        return Robot.make_many(self.boto3_raw_data["robots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRobotsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRobotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationJobsResponse:
    boto3_raw_data: "type_defs.ListSimulationJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def simulationJobSummaries(self):  # pragma: no cover
        return SimulationJobSummary.make_many(
            self.boto3_raw_data["simulationJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSimulationJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureSummary:
    boto3_raw_data: "type_defs.FailureSummaryTypeDef" = dataclasses.field()

    totalFailureCount = field("totalFailureCount")

    @cached_property
    def failures(self):  # pragma: no cover
        return WorldFailure.make_many(self.boto3_raw_data["failures"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailureSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentJobsRequest:
    boto3_raw_data: "type_defs.ListDeploymentJobsRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsRequest:
    boto3_raw_data: "type_defs.ListFleetsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFleetsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRobotApplicationsRequest:
    boto3_raw_data: "type_defs.ListRobotApplicationsRequestTypeDef" = (
        dataclasses.field()
    )

    versionQualifier = field("versionQualifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRobotApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRobotApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRobotsRequest:
    boto3_raw_data: "type_defs.ListRobotsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRobotsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRobotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationApplicationsRequest:
    boto3_raw_data: "type_defs.ListSimulationApplicationsRequestTypeDef" = (
        dataclasses.field()
    )

    versionQualifier = field("versionQualifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSimulationApplicationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationJobBatchesRequest:
    boto3_raw_data: "type_defs.ListSimulationJobBatchesRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSimulationJobBatchesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationJobBatchesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationJobsRequest:
    boto3_raw_data: "type_defs.ListSimulationJobsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSimulationJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldExportJobsRequest:
    boto3_raw_data: "type_defs.ListWorldExportJobsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorldExportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldGenerationJobsRequest:
    boto3_raw_data: "type_defs.ListWorldGenerationJobsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorldGenerationJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldGenerationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldsRequest:
    boto3_raw_data: "type_defs.ListWorldsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListWorldsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsResponse:
    boto3_raw_data: "type_defs.ListFleetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def fleetDetails(self):  # pragma: no cover
        return Fleet.make_many(self.boto3_raw_data["fleetDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListDeploymentJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeploymentJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsRequestPaginate:
    boto3_raw_data: "type_defs.ListFleetsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRobotApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListRobotApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    versionQualifier = field("versionQualifier")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRobotApplicationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRobotApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRobotsRequestPaginate:
    boto3_raw_data: "type_defs.ListRobotsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRobotsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRobotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListSimulationApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    versionQualifier = field("versionQualifier")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSimulationApplicationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationJobBatchesRequestPaginate:
    boto3_raw_data: "type_defs.ListSimulationJobBatchesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSimulationJobBatchesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationJobBatchesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListSimulationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSimulationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldExportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorldExportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorldExportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldExportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldGenerationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorldGenerationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorldGenerationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldGenerationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListWorldTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorldTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorldsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorldsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationJobBatchesResponse:
    boto3_raw_data: "type_defs.ListSimulationJobBatchesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def simulationJobBatchSummaries(self):  # pragma: no cover
        return SimulationJobBatchSummary.make_many(
            self.boto3_raw_data["simulationJobBatchSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSimulationJobBatchesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationJobBatchesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldTemplatesResponse:
    boto3_raw_data: "type_defs.ListWorldTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def templateSummaries(self):  # pragma: no cover
        return TemplateSummary.make_many(self.boto3_raw_data["templateSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorldTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldsResponse:
    boto3_raw_data: "type_defs.ListWorldsResponseTypeDef" = dataclasses.field()

    @cached_property
    def worldSummaries(self):  # pragma: no cover
        return WorldSummary.make_many(self.boto3_raw_data["worldSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorldsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortForwardingConfigOutput:
    boto3_raw_data: "type_defs.PortForwardingConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def portMappings(self):  # pragma: no cover
        return PortMapping.make_many(self.boto3_raw_data["portMappings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PortForwardingConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PortForwardingConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortForwardingConfig:
    boto3_raw_data: "type_defs.PortForwardingConfigTypeDef" = dataclasses.field()

    @cached_property
    def portMappings(self):  # pragma: no cover
        return PortMapping.make_many(self.boto3_raw_data["portMappings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PortForwardingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PortForwardingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RobotDeployment:
    boto3_raw_data: "type_defs.RobotDeploymentTypeDef" = dataclasses.field()

    arn = field("arn")
    deploymentStartTime = field("deploymentStartTime")
    deploymentFinishTime = field("deploymentFinishTime")
    status = field("status")

    @cached_property
    def progressDetail(self):  # pragma: no cover
        return ProgressDetail.make_one(self.boto3_raw_data["progressDetail"])

    failureReason = field("failureReason")
    failureCode = field("failureCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RobotDeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RobotDeploymentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRobotApplicationsResponse:
    boto3_raw_data: "type_defs.ListRobotApplicationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def robotApplicationSummaries(self):  # pragma: no cover
        return RobotApplicationSummary.make_many(
            self.boto3_raw_data["robotApplicationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRobotApplicationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRobotApplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSimulationApplicationsResponse:
    boto3_raw_data: "type_defs.ListSimulationApplicationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def simulationApplicationSummaries(self):  # pragma: no cover
        return SimulationApplicationSummary.make_many(
            self.boto3_raw_data["simulationApplicationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSimulationApplicationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSimulationApplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldExportJobsResponse:
    boto3_raw_data: "type_defs.ListWorldExportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def worldExportJobSummaries(self):  # pragma: no cover
        return WorldExportJobSummary.make_many(
            self.boto3_raw_data["worldExportJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorldExportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorldGenerationJobsResponse:
    boto3_raw_data: "type_defs.ListWorldGenerationJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def worldGenerationJobSummaries(self):  # pragma: no cover
        return WorldGenerationJobSummary.make_many(
            self.boto3_raw_data["worldGenerationJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorldGenerationJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorldGenerationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentJobResponse:
    boto3_raw_data: "type_defs.CreateDeploymentJobResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    fleet = field("fleet")
    status = field("status")

    @cached_property
    def deploymentApplicationConfigs(self):  # pragma: no cover
        return DeploymentApplicationConfigOutput.make_many(
            self.boto3_raw_data["deploymentApplicationConfigs"]
        )

    failureReason = field("failureReason")
    failureCode = field("failureCode")
    createdAt = field("createdAt")

    @cached_property
    def deploymentConfig(self):  # pragma: no cover
        return DeploymentConfig.make_one(self.boto3_raw_data["deploymentConfig"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentJob:
    boto3_raw_data: "type_defs.DeploymentJobTypeDef" = dataclasses.field()

    arn = field("arn")
    fleet = field("fleet")
    status = field("status")

    @cached_property
    def deploymentApplicationConfigs(self):  # pragma: no cover
        return DeploymentApplicationConfigOutput.make_many(
            self.boto3_raw_data["deploymentApplicationConfigs"]
        )

    @cached_property
    def deploymentConfig(self):  # pragma: no cover
        return DeploymentConfig.make_one(self.boto3_raw_data["deploymentConfig"])

    failureReason = field("failureReason")
    failureCode = field("failureCode")
    createdAt = field("createdAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncDeploymentJobResponse:
    boto3_raw_data: "type_defs.SyncDeploymentJobResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    fleet = field("fleet")
    status = field("status")

    @cached_property
    def deploymentConfig(self):  # pragma: no cover
        return DeploymentConfig.make_one(self.boto3_raw_data["deploymentConfig"])

    @cached_property
    def deploymentApplicationConfigs(self):  # pragma: no cover
        return DeploymentApplicationConfigOutput.make_many(
            self.boto3_raw_data["deploymentApplicationConfigs"]
        )

    failureReason = field("failureReason")
    failureCode = field("failureCode")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SyncDeploymentJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SyncDeploymentJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentApplicationConfig:
    boto3_raw_data: "type_defs.DeploymentApplicationConfigTypeDef" = dataclasses.field()

    application = field("application")
    applicationVersion = field("applicationVersion")
    launchConfig = field("launchConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentApplicationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentApplicationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FinishedWorldsSummary:
    boto3_raw_data: "type_defs.FinishedWorldsSummaryTypeDef" = dataclasses.field()

    finishedCount = field("finishedCount")
    succeededWorlds = field("succeededWorlds")

    @cached_property
    def failureSummary(self):  # pragma: no cover
        return FailureSummary.make_one(self.boto3_raw_data["failureSummary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FinishedWorldsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FinishedWorldsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfigOutput:
    boto3_raw_data: "type_defs.LaunchConfigOutputTypeDef" = dataclasses.field()

    packageName = field("packageName")
    launchFile = field("launchFile")
    environmentVariables = field("environmentVariables")

    @cached_property
    def portForwardingConfig(self):  # pragma: no cover
        return PortForwardingConfigOutput.make_one(
            self.boto3_raw_data["portForwardingConfig"]
        )

    streamUI = field("streamUI")
    command = field("command")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeploymentJobResponse:
    boto3_raw_data: "type_defs.DescribeDeploymentJobResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    fleet = field("fleet")
    status = field("status")

    @cached_property
    def deploymentConfig(self):  # pragma: no cover
        return DeploymentConfig.make_one(self.boto3_raw_data["deploymentConfig"])

    @cached_property
    def deploymentApplicationConfigs(self):  # pragma: no cover
        return DeploymentApplicationConfigOutput.make_many(
            self.boto3_raw_data["deploymentApplicationConfigs"]
        )

    failureReason = field("failureReason")
    failureCode = field("failureCode")
    createdAt = field("createdAt")

    @cached_property
    def robotDeploymentSummary(self):  # pragma: no cover
        return RobotDeployment.make_many(self.boto3_raw_data["robotDeploymentSummary"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDeploymentJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeploymentJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentJobsResponse:
    boto3_raw_data: "type_defs.ListDeploymentJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def deploymentJobs(self):  # pragma: no cover
        return DeploymentJob.make_many(self.boto3_raw_data["deploymentJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorldGenerationJobResponse:
    boto3_raw_data: "type_defs.DescribeWorldGenerationJobResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    failureCode = field("failureCode")
    failureReason = field("failureReason")
    clientRequestToken = field("clientRequestToken")
    template = field("template")

    @cached_property
    def worldCount(self):  # pragma: no cover
        return WorldCount.make_one(self.boto3_raw_data["worldCount"])

    @cached_property
    def finishedWorldsSummary(self):  # pragma: no cover
        return FinishedWorldsSummary.make_one(
            self.boto3_raw_data["finishedWorldsSummary"]
        )

    tags = field("tags")
    worldTags = field("worldTags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorldGenerationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorldGenerationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RobotApplicationConfigOutput:
    boto3_raw_data: "type_defs.RobotApplicationConfigOutputTypeDef" = (
        dataclasses.field()
    )

    application = field("application")

    @cached_property
    def launchConfig(self):  # pragma: no cover
        return LaunchConfigOutput.make_one(self.boto3_raw_data["launchConfig"])

    applicationVersion = field("applicationVersion")

    @cached_property
    def uploadConfigurations(self):  # pragma: no cover
        return UploadConfiguration.make_many(
            self.boto3_raw_data["uploadConfigurations"]
        )

    useDefaultUploadConfigurations = field("useDefaultUploadConfigurations")

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    useDefaultTools = field("useDefaultTools")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RobotApplicationConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RobotApplicationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationApplicationConfigOutput:
    boto3_raw_data: "type_defs.SimulationApplicationConfigOutputTypeDef" = (
        dataclasses.field()
    )

    application = field("application")

    @cached_property
    def launchConfig(self):  # pragma: no cover
        return LaunchConfigOutput.make_one(self.boto3_raw_data["launchConfig"])

    applicationVersion = field("applicationVersion")

    @cached_property
    def uploadConfigurations(self):  # pragma: no cover
        return UploadConfiguration.make_many(
            self.boto3_raw_data["uploadConfigurations"]
        )

    @cached_property
    def worldConfigs(self):  # pragma: no cover
        return WorldConfig.make_many(self.boto3_raw_data["worldConfigs"])

    useDefaultUploadConfigurations = field("useDefaultUploadConfigurations")

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    useDefaultTools = field("useDefaultTools")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SimulationApplicationConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationApplicationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfig:
    boto3_raw_data: "type_defs.LaunchConfigTypeDef" = dataclasses.field()

    packageName = field("packageName")
    launchFile = field("launchFile")
    environmentVariables = field("environmentVariables")
    portForwardingConfig = field("portForwardingConfig")
    streamUI = field("streamUI")
    command = field("command")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentJobRequest:
    boto3_raw_data: "type_defs.CreateDeploymentJobRequestTypeDef" = dataclasses.field()

    clientRequestToken = field("clientRequestToken")
    fleet = field("fleet")
    deploymentApplicationConfigs = field("deploymentApplicationConfigs")

    @cached_property
    def deploymentConfig(self):  # pragma: no cover
        return DeploymentConfig.make_one(self.boto3_raw_data["deploymentConfig"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSimulationJobResponse:
    boto3_raw_data: "type_defs.CreateSimulationJobResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    status = field("status")
    lastStartedAt = field("lastStartedAt")
    lastUpdatedAt = field("lastUpdatedAt")
    failureBehavior = field("failureBehavior")
    failureCode = field("failureCode")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    @cached_property
    def loggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["loggingConfig"])

    maxJobDurationInSeconds = field("maxJobDurationInSeconds")
    simulationTimeMillis = field("simulationTimeMillis")
    iamRole = field("iamRole")

    @cached_property
    def robotApplications(self):  # pragma: no cover
        return RobotApplicationConfigOutput.make_many(
            self.boto3_raw_data["robotApplications"]
        )

    @cached_property
    def simulationApplications(self):  # pragma: no cover
        return SimulationApplicationConfigOutput.make_many(
            self.boto3_raw_data["simulationApplications"]
        )

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

    tags = field("tags")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VPCConfigResponse.make_one(self.boto3_raw_data["vpcConfig"])

    @cached_property
    def compute(self):  # pragma: no cover
        return ComputeResponse.make_one(self.boto3_raw_data["compute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSimulationJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSimulationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSimulationJobResponse:
    boto3_raw_data: "type_defs.DescribeSimulationJobResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    status = field("status")
    lastStartedAt = field("lastStartedAt")
    lastUpdatedAt = field("lastUpdatedAt")
    failureBehavior = field("failureBehavior")
    failureCode = field("failureCode")
    failureReason = field("failureReason")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    @cached_property
    def loggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["loggingConfig"])

    maxJobDurationInSeconds = field("maxJobDurationInSeconds")
    simulationTimeMillis = field("simulationTimeMillis")
    iamRole = field("iamRole")

    @cached_property
    def robotApplications(self):  # pragma: no cover
        return RobotApplicationConfigOutput.make_many(
            self.boto3_raw_data["robotApplications"]
        )

    @cached_property
    def simulationApplications(self):  # pragma: no cover
        return SimulationApplicationConfigOutput.make_many(
            self.boto3_raw_data["simulationApplications"]
        )

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

    tags = field("tags")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VPCConfigResponse.make_one(self.boto3_raw_data["vpcConfig"])

    @cached_property
    def networkInterface(self):  # pragma: no cover
        return NetworkInterface.make_one(self.boto3_raw_data["networkInterface"])

    @cached_property
    def compute(self):  # pragma: no cover
        return ComputeResponse.make_one(self.boto3_raw_data["compute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSimulationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSimulationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationJobRequestOutput:
    boto3_raw_data: "type_defs.SimulationJobRequestOutputTypeDef" = dataclasses.field()

    maxJobDurationInSeconds = field("maxJobDurationInSeconds")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    @cached_property
    def loggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["loggingConfig"])

    iamRole = field("iamRole")
    failureBehavior = field("failureBehavior")
    useDefaultApplications = field("useDefaultApplications")

    @cached_property
    def robotApplications(self):  # pragma: no cover
        return RobotApplicationConfigOutput.make_many(
            self.boto3_raw_data["robotApplications"]
        )

    @cached_property
    def simulationApplications(self):  # pragma: no cover
        return SimulationApplicationConfigOutput.make_many(
            self.boto3_raw_data["simulationApplications"]
        )

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSourceConfigOutput.make_many(self.boto3_raw_data["dataSources"])

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VPCConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    @cached_property
    def compute(self):  # pragma: no cover
        return Compute.make_one(self.boto3_raw_data["compute"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationJobRequestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationJobRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationJob:
    boto3_raw_data: "type_defs.SimulationJobTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    status = field("status")
    lastStartedAt = field("lastStartedAt")
    lastUpdatedAt = field("lastUpdatedAt")
    failureBehavior = field("failureBehavior")
    failureCode = field("failureCode")
    failureReason = field("failureReason")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    @cached_property
    def loggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["loggingConfig"])

    maxJobDurationInSeconds = field("maxJobDurationInSeconds")
    simulationTimeMillis = field("simulationTimeMillis")
    iamRole = field("iamRole")

    @cached_property
    def robotApplications(self):  # pragma: no cover
        return RobotApplicationConfigOutput.make_many(
            self.boto3_raw_data["robotApplications"]
        )

    @cached_property
    def simulationApplications(self):  # pragma: no cover
        return SimulationApplicationConfigOutput.make_many(
            self.boto3_raw_data["simulationApplications"]
        )

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

    tags = field("tags")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VPCConfigResponse.make_one(self.boto3_raw_data["vpcConfig"])

    @cached_property
    def networkInterface(self):  # pragma: no cover
        return NetworkInterface.make_one(self.boto3_raw_data["networkInterface"])

    @cached_property
    def compute(self):  # pragma: no cover
        return ComputeResponse.make_one(self.boto3_raw_data["compute"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SimulationJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SimulationJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedCreateSimulationJobRequest:
    boto3_raw_data: "type_defs.FailedCreateSimulationJobRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def request(self):  # pragma: no cover
        return SimulationJobRequestOutput.make_one(self.boto3_raw_data["request"])

    failureReason = field("failureReason")
    failureCode = field("failureCode")
    failedAt = field("failedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FailedCreateSimulationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedCreateSimulationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDescribeSimulationJobResponse:
    boto3_raw_data: "type_defs.BatchDescribeSimulationJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def jobs(self):  # pragma: no cover
        return SimulationJob.make_many(self.boto3_raw_data["jobs"])

    unprocessedJobs = field("unprocessedJobs")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDescribeSimulationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeSimulationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RobotApplicationConfig:
    boto3_raw_data: "type_defs.RobotApplicationConfigTypeDef" = dataclasses.field()

    application = field("application")
    launchConfig = field("launchConfig")
    applicationVersion = field("applicationVersion")

    @cached_property
    def uploadConfigurations(self):  # pragma: no cover
        return UploadConfiguration.make_many(
            self.boto3_raw_data["uploadConfigurations"]
        )

    useDefaultUploadConfigurations = field("useDefaultUploadConfigurations")

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    useDefaultTools = field("useDefaultTools")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RobotApplicationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RobotApplicationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationApplicationConfig:
    boto3_raw_data: "type_defs.SimulationApplicationConfigTypeDef" = dataclasses.field()

    application = field("application")
    launchConfig = field("launchConfig")
    applicationVersion = field("applicationVersion")

    @cached_property
    def uploadConfigurations(self):  # pragma: no cover
        return UploadConfiguration.make_many(
            self.boto3_raw_data["uploadConfigurations"]
        )

    @cached_property
    def worldConfigs(self):  # pragma: no cover
        return WorldConfig.make_many(self.boto3_raw_data["worldConfigs"])

    useDefaultUploadConfigurations = field("useDefaultUploadConfigurations")

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    useDefaultTools = field("useDefaultTools")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationApplicationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationApplicationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSimulationJobBatchResponse:
    boto3_raw_data: "type_defs.DescribeSimulationJobBatchResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    status = field("status")
    lastUpdatedAt = field("lastUpdatedAt")
    createdAt = field("createdAt")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def batchPolicy(self):  # pragma: no cover
        return BatchPolicy.make_one(self.boto3_raw_data["batchPolicy"])

    failureCode = field("failureCode")
    failureReason = field("failureReason")

    @cached_property
    def failedRequests(self):  # pragma: no cover
        return FailedCreateSimulationJobRequest.make_many(
            self.boto3_raw_data["failedRequests"]
        )

    @cached_property
    def pendingRequests(self):  # pragma: no cover
        return SimulationJobRequestOutput.make_many(
            self.boto3_raw_data["pendingRequests"]
        )

    @cached_property
    def createdRequests(self):  # pragma: no cover
        return SimulationJobSummary.make_many(self.boto3_raw_data["createdRequests"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSimulationJobBatchResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSimulationJobBatchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSimulationJobBatchResponse:
    boto3_raw_data: "type_defs.StartSimulationJobBatchResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def batchPolicy(self):  # pragma: no cover
        return BatchPolicy.make_one(self.boto3_raw_data["batchPolicy"])

    failureCode = field("failureCode")
    failureReason = field("failureReason")

    @cached_property
    def failedRequests(self):  # pragma: no cover
        return FailedCreateSimulationJobRequest.make_many(
            self.boto3_raw_data["failedRequests"]
        )

    @cached_property
    def pendingRequests(self):  # pragma: no cover
        return SimulationJobRequestOutput.make_many(
            self.boto3_raw_data["pendingRequests"]
        )

    @cached_property
    def createdRequests(self):  # pragma: no cover
        return SimulationJobSummary.make_many(self.boto3_raw_data["createdRequests"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSimulationJobBatchResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSimulationJobBatchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSimulationJobRequest:
    boto3_raw_data: "type_defs.CreateSimulationJobRequestTypeDef" = dataclasses.field()

    maxJobDurationInSeconds = field("maxJobDurationInSeconds")
    iamRole = field("iamRole")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    @cached_property
    def loggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["loggingConfig"])

    failureBehavior = field("failureBehavior")
    robotApplications = field("robotApplications")
    simulationApplications = field("simulationApplications")
    dataSources = field("dataSources")
    tags = field("tags")
    vpcConfig = field("vpcConfig")

    @cached_property
    def compute(self):  # pragma: no cover
        return Compute.make_one(self.boto3_raw_data["compute"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSimulationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSimulationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulationJobRequest:
    boto3_raw_data: "type_defs.SimulationJobRequestTypeDef" = dataclasses.field()

    maxJobDurationInSeconds = field("maxJobDurationInSeconds")

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["outputLocation"])

    @cached_property
    def loggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["loggingConfig"])

    iamRole = field("iamRole")
    failureBehavior = field("failureBehavior")
    useDefaultApplications = field("useDefaultApplications")
    robotApplications = field("robotApplications")
    simulationApplications = field("simulationApplications")
    dataSources = field("dataSources")
    vpcConfig = field("vpcConfig")

    @cached_property
    def compute(self):  # pragma: no cover
        return Compute.make_one(self.boto3_raw_data["compute"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSimulationJobBatchRequest:
    boto3_raw_data: "type_defs.StartSimulationJobBatchRequestTypeDef" = (
        dataclasses.field()
    )

    createSimulationJobRequests = field("createSimulationJobRequests")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def batchPolicy(self):  # pragma: no cover
        return BatchPolicy.make_one(self.boto3_raw_data["batchPolicy"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSimulationJobBatchRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSimulationJobBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
