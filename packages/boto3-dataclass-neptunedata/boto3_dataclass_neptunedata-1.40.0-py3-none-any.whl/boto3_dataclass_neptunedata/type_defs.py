# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_neptunedata import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CancelGremlinQueryInput:
    boto3_raw_data: "type_defs.CancelGremlinQueryInputTypeDef" = dataclasses.field()

    queryId = field("queryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelGremlinQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelGremlinQueryInputTypeDef"]
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
class CancelLoaderJobInput:
    boto3_raw_data: "type_defs.CancelLoaderJobInputTypeDef" = dataclasses.field()

    loadId = field("loadId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelLoaderJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelLoaderJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMLDataProcessingJobInput:
    boto3_raw_data: "type_defs.CancelMLDataProcessingJobInputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    neptuneIamRoleArn = field("neptuneIamRoleArn")
    clean = field("clean")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelMLDataProcessingJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMLDataProcessingJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMLModelTrainingJobInput:
    boto3_raw_data: "type_defs.CancelMLModelTrainingJobInputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    neptuneIamRoleArn = field("neptuneIamRoleArn")
    clean = field("clean")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelMLModelTrainingJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMLModelTrainingJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMLModelTransformJobInput:
    boto3_raw_data: "type_defs.CancelMLModelTransformJobInputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    neptuneIamRoleArn = field("neptuneIamRoleArn")
    clean = field("clean")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelMLModelTransformJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMLModelTransformJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelOpenCypherQueryInput:
    boto3_raw_data: "type_defs.CancelOpenCypherQueryInputTypeDef" = dataclasses.field()

    queryId = field("queryId")
    silent = field("silent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelOpenCypherQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelOpenCypherQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMLEndpointInput:
    boto3_raw_data: "type_defs.CreateMLEndpointInputTypeDef" = dataclasses.field()

    id = field("id")
    mlModelTrainingJobId = field("mlModelTrainingJobId")
    mlModelTransformJobId = field("mlModelTransformJobId")
    update = field("update")
    neptuneIamRoleArn = field("neptuneIamRoleArn")
    modelName = field("modelName")
    instanceType = field("instanceType")
    instanceCount = field("instanceCount")
    volumeEncryptionKMSKey = field("volumeEncryptionKMSKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMLEndpointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMLEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomModelTrainingParameters:
    boto3_raw_data: "type_defs.CustomModelTrainingParametersTypeDef" = (
        dataclasses.field()
    )

    sourceS3DirectoryPath = field("sourceS3DirectoryPath")
    trainingEntryPointScript = field("trainingEntryPointScript")
    transformEntryPointScript = field("transformEntryPointScript")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomModelTrainingParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomModelTrainingParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomModelTransformParameters:
    boto3_raw_data: "type_defs.CustomModelTransformParametersTypeDef" = (
        dataclasses.field()
    )

    sourceS3DirectoryPath = field("sourceS3DirectoryPath")
    transformEntryPointScript = field("transformEntryPointScript")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomModelTransformParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomModelTransformParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMLEndpointInput:
    boto3_raw_data: "type_defs.DeleteMLEndpointInputTypeDef" = dataclasses.field()

    id = field("id")
    neptuneIamRoleArn = field("neptuneIamRoleArn")
    clean = field("clean")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMLEndpointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMLEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStatisticsValueMap:
    boto3_raw_data: "type_defs.DeleteStatisticsValueMapTypeDef" = dataclasses.field()

    active = field("active")
    statisticsId = field("statisticsId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStatisticsValueMapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStatisticsValueMapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdgeStructure:
    boto3_raw_data: "type_defs.EdgeStructureTypeDef" = dataclasses.field()

    count = field("count")
    edgeProperties = field("edgeProperties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdgeStructureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdgeStructureTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteFastResetInput:
    boto3_raw_data: "type_defs.ExecuteFastResetInputTypeDef" = dataclasses.field()

    action = field("action")
    token = field("token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteFastResetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteFastResetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FastResetToken:
    boto3_raw_data: "type_defs.FastResetTokenTypeDef" = dataclasses.field()

    token = field("token")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FastResetTokenTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FastResetTokenTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteGremlinExplainQueryInput:
    boto3_raw_data: "type_defs.ExecuteGremlinExplainQueryInputTypeDef" = (
        dataclasses.field()
    )

    gremlinQuery = field("gremlinQuery")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExecuteGremlinExplainQueryInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteGremlinExplainQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteGremlinProfileQueryInput:
    boto3_raw_data: "type_defs.ExecuteGremlinProfileQueryInputTypeDef" = (
        dataclasses.field()
    )

    gremlinQuery = field("gremlinQuery")
    results = field("results")
    chop = field("chop")
    serializer = field("serializer")
    indexOps = field("indexOps")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExecuteGremlinProfileQueryInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteGremlinProfileQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteGremlinQueryInput:
    boto3_raw_data: "type_defs.ExecuteGremlinQueryInputTypeDef" = dataclasses.field()

    gremlinQuery = field("gremlinQuery")
    serializer = field("serializer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteGremlinQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteGremlinQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GremlinQueryStatusAttributes:
    boto3_raw_data: "type_defs.GremlinQueryStatusAttributesTypeDef" = (
        dataclasses.field()
    )

    message = field("message")
    code = field("code")
    attributes = field("attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GremlinQueryStatusAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GremlinQueryStatusAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteOpenCypherExplainQueryInput:
    boto3_raw_data: "type_defs.ExecuteOpenCypherExplainQueryInputTypeDef" = (
        dataclasses.field()
    )

    openCypherQuery = field("openCypherQuery")
    explainMode = field("explainMode")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExecuteOpenCypherExplainQueryInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteOpenCypherExplainQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteOpenCypherQueryInput:
    boto3_raw_data: "type_defs.ExecuteOpenCypherQueryInputTypeDef" = dataclasses.field()

    openCypherQuery = field("openCypherQuery")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteOpenCypherQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteOpenCypherQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryLanguageVersion:
    boto3_raw_data: "type_defs.QueryLanguageVersionTypeDef" = dataclasses.field()

    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryLanguageVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryLanguageVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGremlinQueryStatusInput:
    boto3_raw_data: "type_defs.GetGremlinQueryStatusInputTypeDef" = dataclasses.field()

    queryId = field("queryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGremlinQueryStatusInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGremlinQueryStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryEvalStats:
    boto3_raw_data: "type_defs.QueryEvalStatsTypeDef" = dataclasses.field()

    waited = field("waited")
    elapsed = field("elapsed")
    cancelled = field("cancelled")
    subqueries = field("subqueries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryEvalStatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryEvalStatsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoaderJobStatusInput:
    boto3_raw_data: "type_defs.GetLoaderJobStatusInputTypeDef" = dataclasses.field()

    loadId = field("loadId")
    details = field("details")
    errors = field("errors")
    page = field("page")
    errorsPerPage = field("errorsPerPage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoaderJobStatusInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoaderJobStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLDataProcessingJobInput:
    boto3_raw_data: "type_defs.GetMLDataProcessingJobInputTypeDef" = dataclasses.field()

    id = field("id")
    neptuneIamRoleArn = field("neptuneIamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLDataProcessingJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLDataProcessingJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MlResourceDefinition:
    boto3_raw_data: "type_defs.MlResourceDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    status = field("status")
    outputLocation = field("outputLocation")
    failureReason = field("failureReason")
    cloudwatchLogUrl = field("cloudwatchLogUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MlResourceDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MlResourceDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLEndpointInput:
    boto3_raw_data: "type_defs.GetMLEndpointInputTypeDef" = dataclasses.field()

    id = field("id")
    neptuneIamRoleArn = field("neptuneIamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLEndpointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MlConfigDefinition:
    boto3_raw_data: "type_defs.MlConfigDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MlConfigDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MlConfigDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLModelTrainingJobInput:
    boto3_raw_data: "type_defs.GetMLModelTrainingJobInputTypeDef" = dataclasses.field()

    id = field("id")
    neptuneIamRoleArn = field("neptuneIamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLModelTrainingJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLModelTrainingJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLModelTransformJobInput:
    boto3_raw_data: "type_defs.GetMLModelTransformJobInputTypeDef" = dataclasses.field()

    id = field("id")
    neptuneIamRoleArn = field("neptuneIamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLModelTransformJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLModelTransformJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpenCypherQueryStatusInput:
    boto3_raw_data: "type_defs.GetOpenCypherQueryStatusInputTypeDef" = (
        dataclasses.field()
    )

    queryId = field("queryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOpenCypherQueryStatusInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpenCypherQueryStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPropertygraphStreamInput:
    boto3_raw_data: "type_defs.GetPropertygraphStreamInputTypeDef" = dataclasses.field()

    limit = field("limit")
    iteratorType = field("iteratorType")
    commitNum = field("commitNum")
    opNum = field("opNum")
    encoding = field("encoding")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPropertygraphStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPropertygraphStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPropertygraphSummaryInput:
    boto3_raw_data: "type_defs.GetPropertygraphSummaryInputTypeDef" = (
        dataclasses.field()
    )

    mode = field("mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPropertygraphSummaryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPropertygraphSummaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRDFGraphSummaryInput:
    boto3_raw_data: "type_defs.GetRDFGraphSummaryInputTypeDef" = dataclasses.field()

    mode = field("mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRDFGraphSummaryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRDFGraphSummaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSparqlStreamInput:
    boto3_raw_data: "type_defs.GetSparqlStreamInputTypeDef" = dataclasses.field()

    limit = field("limit")
    iteratorType = field("iteratorType")
    commitNum = field("commitNum")
    opNum = field("opNum")
    encoding = field("encoding")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSparqlStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSparqlStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGremlinQueriesInput:
    boto3_raw_data: "type_defs.ListGremlinQueriesInputTypeDef" = dataclasses.field()

    includeWaiting = field("includeWaiting")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGremlinQueriesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGremlinQueriesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoaderJobsInput:
    boto3_raw_data: "type_defs.ListLoaderJobsInputTypeDef" = dataclasses.field()

    limit = field("limit")
    includeQueuedLoads = field("includeQueuedLoads")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLoaderJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoaderJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoaderIdResult:
    boto3_raw_data: "type_defs.LoaderIdResultTypeDef" = dataclasses.field()

    loadIds = field("loadIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoaderIdResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoaderIdResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLDataProcessingJobsInput:
    boto3_raw_data: "type_defs.ListMLDataProcessingJobsInputTypeDef" = (
        dataclasses.field()
    )

    maxItems = field("maxItems")
    neptuneIamRoleArn = field("neptuneIamRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMLDataProcessingJobsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLDataProcessingJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLEndpointsInput:
    boto3_raw_data: "type_defs.ListMLEndpointsInputTypeDef" = dataclasses.field()

    maxItems = field("maxItems")
    neptuneIamRoleArn = field("neptuneIamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMLEndpointsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLEndpointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLModelTrainingJobsInput:
    boto3_raw_data: "type_defs.ListMLModelTrainingJobsInputTypeDef" = (
        dataclasses.field()
    )

    maxItems = field("maxItems")
    neptuneIamRoleArn = field("neptuneIamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMLModelTrainingJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLModelTrainingJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLModelTransformJobsInput:
    boto3_raw_data: "type_defs.ListMLModelTransformJobsInputTypeDef" = (
        dataclasses.field()
    )

    maxItems = field("maxItems")
    neptuneIamRoleArn = field("neptuneIamRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMLModelTransformJobsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLModelTransformJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpenCypherQueriesInput:
    boto3_raw_data: "type_defs.ListOpenCypherQueriesInputTypeDef" = dataclasses.field()

    includeWaiting = field("includeWaiting")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOpenCypherQueriesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpenCypherQueriesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagePropertygraphStatisticsInput:
    boto3_raw_data: "type_defs.ManagePropertygraphStatisticsInputTypeDef" = (
        dataclasses.field()
    )

    mode = field("mode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagePropertygraphStatisticsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagePropertygraphStatisticsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshStatisticsIdMap:
    boto3_raw_data: "type_defs.RefreshStatisticsIdMapTypeDef" = dataclasses.field()

    statisticsId = field("statisticsId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshStatisticsIdMapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshStatisticsIdMapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManageSparqlStatisticsInput:
    boto3_raw_data: "type_defs.ManageSparqlStatisticsInputTypeDef" = dataclasses.field()

    mode = field("mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManageSparqlStatisticsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManageSparqlStatisticsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeStructure:
    boto3_raw_data: "type_defs.NodeStructureTypeDef" = dataclasses.field()

    count = field("count")
    nodeProperties = field("nodeProperties")
    distinctOutgoingEdgeLabels = field("distinctOutgoingEdgeLabels")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeStructureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeStructureTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertygraphData:
    boto3_raw_data: "type_defs.PropertygraphDataTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    key = field("key")
    value = field("value")
    from_ = field("from")
    to = field("to")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertygraphDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertygraphDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectStructure:
    boto3_raw_data: "type_defs.SubjectStructureTypeDef" = dataclasses.field()

    count = field("count")
    predicates = field("predicates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubjectStructureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubjectStructureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparqlData:
    boto3_raw_data: "type_defs.SparqlDataTypeDef" = dataclasses.field()

    stmt = field("stmt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SparqlDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SparqlDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLoaderJobInput:
    boto3_raw_data: "type_defs.StartLoaderJobInputTypeDef" = dataclasses.field()

    source = field("source")
    format = field("format")
    s3BucketRegion = field("s3BucketRegion")
    iamRoleArn = field("iamRoleArn")
    mode = field("mode")
    failOnError = field("failOnError")
    parallelism = field("parallelism")
    parserConfiguration = field("parserConfiguration")
    updateSingleCardinalityProperties = field("updateSingleCardinalityProperties")
    queueRequest = field("queueRequest")
    dependencies = field("dependencies")
    userProvidedEdgeIds = field("userProvidedEdgeIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLoaderJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLoaderJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMLDataProcessingJobInput:
    boto3_raw_data: "type_defs.StartMLDataProcessingJobInputTypeDef" = (
        dataclasses.field()
    )

    inputDataS3Location = field("inputDataS3Location")
    processedDataS3Location = field("processedDataS3Location")
    id = field("id")
    previousDataProcessingJobId = field("previousDataProcessingJobId")
    sagemakerIamRoleArn = field("sagemakerIamRoleArn")
    neptuneIamRoleArn = field("neptuneIamRoleArn")
    processingInstanceType = field("processingInstanceType")
    processingInstanceVolumeSizeInGB = field("processingInstanceVolumeSizeInGB")
    processingTimeOutInSeconds = field("processingTimeOutInSeconds")
    modelType = field("modelType")
    configFileName = field("configFileName")
    subnets = field("subnets")
    securityGroupIds = field("securityGroupIds")
    volumeEncryptionKMSKey = field("volumeEncryptionKMSKey")
    s3OutputEncryptionKMSKey = field("s3OutputEncryptionKMSKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMLDataProcessingJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMLDataProcessingJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatisticsSummary:
    boto3_raw_data: "type_defs.StatisticsSummaryTypeDef" = dataclasses.field()

    signatureCount = field("signatureCount")
    instanceCount = field("instanceCount")
    predicateCount = field("predicateCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatisticsSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatisticsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelGremlinQueryOutput:
    boto3_raw_data: "type_defs.CancelGremlinQueryOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelGremlinQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelGremlinQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelLoaderJobOutput:
    boto3_raw_data: "type_defs.CancelLoaderJobOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelLoaderJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelLoaderJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMLDataProcessingJobOutput:
    boto3_raw_data: "type_defs.CancelMLDataProcessingJobOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelMLDataProcessingJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMLDataProcessingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMLModelTrainingJobOutput:
    boto3_raw_data: "type_defs.CancelMLModelTrainingJobOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelMLModelTrainingJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMLModelTrainingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMLModelTransformJobOutput:
    boto3_raw_data: "type_defs.CancelMLModelTransformJobOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelMLModelTransformJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMLModelTransformJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelOpenCypherQueryOutput:
    boto3_raw_data: "type_defs.CancelOpenCypherQueryOutputTypeDef" = dataclasses.field()

    status = field("status")
    payload = field("payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelOpenCypherQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelOpenCypherQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMLEndpointOutput:
    boto3_raw_data: "type_defs.CreateMLEndpointOutputTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    creationTimeInMillis = field("creationTimeInMillis")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMLEndpointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMLEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMLEndpointOutput:
    boto3_raw_data: "type_defs.DeleteMLEndpointOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMLEndpointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMLEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteGremlinExplainQueryOutput:
    boto3_raw_data: "type_defs.ExecuteGremlinExplainQueryOutputTypeDef" = (
        dataclasses.field()
    )

    output = field("output")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExecuteGremlinExplainQueryOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteGremlinExplainQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteGremlinProfileQueryOutput:
    boto3_raw_data: "type_defs.ExecuteGremlinProfileQueryOutputTypeDef" = (
        dataclasses.field()
    )

    output = field("output")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExecuteGremlinProfileQueryOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteGremlinProfileQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteOpenCypherExplainQueryOutput:
    boto3_raw_data: "type_defs.ExecuteOpenCypherExplainQueryOutputTypeDef" = (
        dataclasses.field()
    )

    results = field("results")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExecuteOpenCypherExplainQueryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteOpenCypherExplainQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteOpenCypherQueryOutput:
    boto3_raw_data: "type_defs.ExecuteOpenCypherQueryOutputTypeDef" = (
        dataclasses.field()
    )

    results = field("results")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteOpenCypherQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteOpenCypherQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoaderJobStatusOutput:
    boto3_raw_data: "type_defs.GetLoaderJobStatusOutputTypeDef" = dataclasses.field()

    status = field("status")
    payload = field("payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoaderJobStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoaderJobStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLDataProcessingJobsOutput:
    boto3_raw_data: "type_defs.ListMLDataProcessingJobsOutputTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMLDataProcessingJobsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLDataProcessingJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLEndpointsOutput:
    boto3_raw_data: "type_defs.ListMLEndpointsOutputTypeDef" = dataclasses.field()

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMLEndpointsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLEndpointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLModelTrainingJobsOutput:
    boto3_raw_data: "type_defs.ListMLModelTrainingJobsOutputTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMLModelTrainingJobsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLModelTrainingJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLModelTransformJobsOutput:
    boto3_raw_data: "type_defs.ListMLModelTransformJobsOutputTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMLModelTransformJobsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLModelTransformJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLoaderJobOutput:
    boto3_raw_data: "type_defs.StartLoaderJobOutputTypeDef" = dataclasses.field()

    status = field("status")
    payload = field("payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLoaderJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLoaderJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMLDataProcessingJobOutput:
    boto3_raw_data: "type_defs.StartMLDataProcessingJobOutputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    creationTimeInMillis = field("creationTimeInMillis")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMLDataProcessingJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMLDataProcessingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMLModelTrainingJobOutput:
    boto3_raw_data: "type_defs.StartMLModelTrainingJobOutputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    creationTimeInMillis = field("creationTimeInMillis")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMLModelTrainingJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMLModelTrainingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMLModelTransformJobOutput:
    boto3_raw_data: "type_defs.StartMLModelTransformJobOutputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    creationTimeInMillis = field("creationTimeInMillis")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMLModelTransformJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMLModelTransformJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMLModelTrainingJobInput:
    boto3_raw_data: "type_defs.StartMLModelTrainingJobInputTypeDef" = (
        dataclasses.field()
    )

    dataProcessingJobId = field("dataProcessingJobId")
    trainModelS3Location = field("trainModelS3Location")
    id = field("id")
    previousModelTrainingJobId = field("previousModelTrainingJobId")
    sagemakerIamRoleArn = field("sagemakerIamRoleArn")
    neptuneIamRoleArn = field("neptuneIamRoleArn")
    baseProcessingInstanceType = field("baseProcessingInstanceType")
    trainingInstanceType = field("trainingInstanceType")
    trainingInstanceVolumeSizeInGB = field("trainingInstanceVolumeSizeInGB")
    trainingTimeOutInSeconds = field("trainingTimeOutInSeconds")
    maxHPONumberOfTrainingJobs = field("maxHPONumberOfTrainingJobs")
    maxHPOParallelTrainingJobs = field("maxHPOParallelTrainingJobs")
    subnets = field("subnets")
    securityGroupIds = field("securityGroupIds")
    volumeEncryptionKMSKey = field("volumeEncryptionKMSKey")
    s3OutputEncryptionKMSKey = field("s3OutputEncryptionKMSKey")
    enableManagedSpotTraining = field("enableManagedSpotTraining")

    @cached_property
    def customModelTrainingParameters(self):  # pragma: no cover
        return CustomModelTrainingParameters.make_one(
            self.boto3_raw_data["customModelTrainingParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMLModelTrainingJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMLModelTrainingJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMLModelTransformJobInput:
    boto3_raw_data: "type_defs.StartMLModelTransformJobInputTypeDef" = (
        dataclasses.field()
    )

    modelTransformOutputS3Location = field("modelTransformOutputS3Location")
    id = field("id")
    dataProcessingJobId = field("dataProcessingJobId")
    mlModelTrainingJobId = field("mlModelTrainingJobId")
    trainingJobName = field("trainingJobName")
    sagemakerIamRoleArn = field("sagemakerIamRoleArn")
    neptuneIamRoleArn = field("neptuneIamRoleArn")

    @cached_property
    def customModelTransformParameters(self):  # pragma: no cover
        return CustomModelTransformParameters.make_one(
            self.boto3_raw_data["customModelTransformParameters"]
        )

    baseProcessingInstanceType = field("baseProcessingInstanceType")
    baseProcessingInstanceVolumeSizeInGB = field("baseProcessingInstanceVolumeSizeInGB")
    subnets = field("subnets")
    securityGroupIds = field("securityGroupIds")
    volumeEncryptionKMSKey = field("volumeEncryptionKMSKey")
    s3OutputEncryptionKMSKey = field("s3OutputEncryptionKMSKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMLModelTransformJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMLModelTransformJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePropertygraphStatisticsOutput:
    boto3_raw_data: "type_defs.DeletePropertygraphStatisticsOutputTypeDef" = (
        dataclasses.field()
    )

    statusCode = field("statusCode")
    status = field("status")

    @cached_property
    def payload(self):  # pragma: no cover
        return DeleteStatisticsValueMap.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePropertygraphStatisticsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePropertygraphStatisticsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSparqlStatisticsOutput:
    boto3_raw_data: "type_defs.DeleteSparqlStatisticsOutputTypeDef" = (
        dataclasses.field()
    )

    statusCode = field("statusCode")
    status = field("status")

    @cached_property
    def payload(self):  # pragma: no cover
        return DeleteStatisticsValueMap.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSparqlStatisticsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSparqlStatisticsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteFastResetOutput:
    boto3_raw_data: "type_defs.ExecuteFastResetOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def payload(self):  # pragma: no cover
        return FastResetToken.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteFastResetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteFastResetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteGremlinQueryOutput:
    boto3_raw_data: "type_defs.ExecuteGremlinQueryOutputTypeDef" = dataclasses.field()

    requestId = field("requestId")

    @cached_property
    def status(self):  # pragma: no cover
        return GremlinQueryStatusAttributes.make_one(self.boto3_raw_data["status"])

    result = field("result")
    meta = field("meta")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteGremlinQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteGremlinQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEngineStatusOutput:
    boto3_raw_data: "type_defs.GetEngineStatusOutputTypeDef" = dataclasses.field()

    status = field("status")
    startTime = field("startTime")
    dbEngineVersion = field("dbEngineVersion")
    role = field("role")
    dfeQueryEngine = field("dfeQueryEngine")

    @cached_property
    def gremlin(self):  # pragma: no cover
        return QueryLanguageVersion.make_one(self.boto3_raw_data["gremlin"])

    @cached_property
    def sparql(self):  # pragma: no cover
        return QueryLanguageVersion.make_one(self.boto3_raw_data["sparql"])

    @cached_property
    def opencypher(self):  # pragma: no cover
        return QueryLanguageVersion.make_one(self.boto3_raw_data["opencypher"])

    labMode = field("labMode")
    rollingBackTrxCount = field("rollingBackTrxCount")
    rollingBackTrxEarliestStartTime = field("rollingBackTrxEarliestStartTime")
    features = field("features")
    settings = field("settings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEngineStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEngineStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGremlinQueryStatusOutput:
    boto3_raw_data: "type_defs.GetGremlinQueryStatusOutputTypeDef" = dataclasses.field()

    queryId = field("queryId")
    queryString = field("queryString")

    @cached_property
    def queryEvalStats(self):  # pragma: no cover
        return QueryEvalStats.make_one(self.boto3_raw_data["queryEvalStats"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGremlinQueryStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGremlinQueryStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpenCypherQueryStatusOutput:
    boto3_raw_data: "type_defs.GetOpenCypherQueryStatusOutputTypeDef" = (
        dataclasses.field()
    )

    queryId = field("queryId")
    queryString = field("queryString")

    @cached_property
    def queryEvalStats(self):  # pragma: no cover
        return QueryEvalStats.make_one(self.boto3_raw_data["queryEvalStats"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOpenCypherQueryStatusOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpenCypherQueryStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GremlinQueryStatus:
    boto3_raw_data: "type_defs.GremlinQueryStatusTypeDef" = dataclasses.field()

    queryId = field("queryId")
    queryString = field("queryString")

    @cached_property
    def queryEvalStats(self):  # pragma: no cover
        return QueryEvalStats.make_one(self.boto3_raw_data["queryEvalStats"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GremlinQueryStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GremlinQueryStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLDataProcessingJobOutput:
    boto3_raw_data: "type_defs.GetMLDataProcessingJobOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    id = field("id")

    @cached_property
    def processingJob(self):  # pragma: no cover
        return MlResourceDefinition.make_one(self.boto3_raw_data["processingJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLDataProcessingJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLDataProcessingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLEndpointOutput:
    boto3_raw_data: "type_defs.GetMLEndpointOutputTypeDef" = dataclasses.field()

    status = field("status")
    id = field("id")

    @cached_property
    def endpoint(self):  # pragma: no cover
        return MlResourceDefinition.make_one(self.boto3_raw_data["endpoint"])

    @cached_property
    def endpointConfig(self):  # pragma: no cover
        return MlConfigDefinition.make_one(self.boto3_raw_data["endpointConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLEndpointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLModelTrainingJobOutput:
    boto3_raw_data: "type_defs.GetMLModelTrainingJobOutputTypeDef" = dataclasses.field()

    status = field("status")
    id = field("id")

    @cached_property
    def processingJob(self):  # pragma: no cover
        return MlResourceDefinition.make_one(self.boto3_raw_data["processingJob"])

    @cached_property
    def hpoJob(self):  # pragma: no cover
        return MlResourceDefinition.make_one(self.boto3_raw_data["hpoJob"])

    @cached_property
    def modelTransformJob(self):  # pragma: no cover
        return MlResourceDefinition.make_one(self.boto3_raw_data["modelTransformJob"])

    @cached_property
    def mlModels(self):  # pragma: no cover
        return MlConfigDefinition.make_many(self.boto3_raw_data["mlModels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLModelTrainingJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLModelTrainingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLModelTransformJobOutput:
    boto3_raw_data: "type_defs.GetMLModelTransformJobOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    id = field("id")

    @cached_property
    def baseProcessingJob(self):  # pragma: no cover
        return MlResourceDefinition.make_one(self.boto3_raw_data["baseProcessingJob"])

    @cached_property
    def remoteModelTransformJob(self):  # pragma: no cover
        return MlResourceDefinition.make_one(
            self.boto3_raw_data["remoteModelTransformJob"]
        )

    @cached_property
    def models(self):  # pragma: no cover
        return MlConfigDefinition.make_many(self.boto3_raw_data["models"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLModelTransformJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLModelTransformJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLoaderJobsOutput:
    boto3_raw_data: "type_defs.ListLoaderJobsOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def payload(self):  # pragma: no cover
        return LoaderIdResult.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLoaderJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLoaderJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagePropertygraphStatisticsOutput:
    boto3_raw_data: "type_defs.ManagePropertygraphStatisticsOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def payload(self):  # pragma: no cover
        return RefreshStatisticsIdMap.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagePropertygraphStatisticsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagePropertygraphStatisticsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManageSparqlStatisticsOutput:
    boto3_raw_data: "type_defs.ManageSparqlStatisticsOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def payload(self):  # pragma: no cover
        return RefreshStatisticsIdMap.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManageSparqlStatisticsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManageSparqlStatisticsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertygraphSummary:
    boto3_raw_data: "type_defs.PropertygraphSummaryTypeDef" = dataclasses.field()

    numNodes = field("numNodes")
    numEdges = field("numEdges")
    numNodeLabels = field("numNodeLabels")
    numEdgeLabels = field("numEdgeLabels")
    nodeLabels = field("nodeLabels")
    edgeLabels = field("edgeLabels")
    numNodeProperties = field("numNodeProperties")
    numEdgeProperties = field("numEdgeProperties")
    nodeProperties = field("nodeProperties")
    edgeProperties = field("edgeProperties")
    totalNodePropertyValues = field("totalNodePropertyValues")
    totalEdgePropertyValues = field("totalEdgePropertyValues")

    @cached_property
    def nodeStructures(self):  # pragma: no cover
        return NodeStructure.make_many(self.boto3_raw_data["nodeStructures"])

    @cached_property
    def edgeStructures(self):  # pragma: no cover
        return EdgeStructure.make_many(self.boto3_raw_data["edgeStructures"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertygraphSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertygraphSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertygraphRecord:
    boto3_raw_data: "type_defs.PropertygraphRecordTypeDef" = dataclasses.field()

    commitTimestampInMillis = field("commitTimestampInMillis")
    eventId = field("eventId")

    @cached_property
    def data(self):  # pragma: no cover
        return PropertygraphData.make_one(self.boto3_raw_data["data"])

    op = field("op")
    isLastOp = field("isLastOp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertygraphRecordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertygraphRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDFGraphSummary:
    boto3_raw_data: "type_defs.RDFGraphSummaryTypeDef" = dataclasses.field()

    numDistinctSubjects = field("numDistinctSubjects")
    numDistinctPredicates = field("numDistinctPredicates")
    numQuads = field("numQuads")
    numClasses = field("numClasses")
    classes = field("classes")
    predicates = field("predicates")

    @cached_property
    def subjectStructures(self):  # pragma: no cover
        return SubjectStructure.make_many(self.boto3_raw_data["subjectStructures"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RDFGraphSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RDFGraphSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparqlRecord:
    boto3_raw_data: "type_defs.SparqlRecordTypeDef" = dataclasses.field()

    commitTimestampInMillis = field("commitTimestampInMillis")
    eventId = field("eventId")

    @cached_property
    def data(self):  # pragma: no cover
        return SparqlData.make_one(self.boto3_raw_data["data"])

    op = field("op")
    isLastOp = field("isLastOp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SparqlRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SparqlRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Statistics:
    boto3_raw_data: "type_defs.StatisticsTypeDef" = dataclasses.field()

    autoCompute = field("autoCompute")
    active = field("active")
    statisticsId = field("statisticsId")
    date = field("date")
    note = field("note")

    @cached_property
    def signatureInfo(self):  # pragma: no cover
        return StatisticsSummary.make_one(self.boto3_raw_data["signatureInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatisticsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGremlinQueriesOutput:
    boto3_raw_data: "type_defs.ListGremlinQueriesOutputTypeDef" = dataclasses.field()

    acceptedQueryCount = field("acceptedQueryCount")
    runningQueryCount = field("runningQueryCount")

    @cached_property
    def queries(self):  # pragma: no cover
        return GremlinQueryStatus.make_many(self.boto3_raw_data["queries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGremlinQueriesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGremlinQueriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpenCypherQueriesOutput:
    boto3_raw_data: "type_defs.ListOpenCypherQueriesOutputTypeDef" = dataclasses.field()

    acceptedQueryCount = field("acceptedQueryCount")
    runningQueryCount = field("runningQueryCount")

    @cached_property
    def queries(self):  # pragma: no cover
        return GremlinQueryStatus.make_many(self.boto3_raw_data["queries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOpenCypherQueriesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpenCypherQueriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertygraphSummaryValueMap:
    boto3_raw_data: "type_defs.PropertygraphSummaryValueMapTypeDef" = (
        dataclasses.field()
    )

    version = field("version")
    lastStatisticsComputationTime = field("lastStatisticsComputationTime")

    @cached_property
    def graphSummary(self):  # pragma: no cover
        return PropertygraphSummary.make_one(self.boto3_raw_data["graphSummary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertygraphSummaryValueMapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertygraphSummaryValueMapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPropertygraphStreamOutput:
    boto3_raw_data: "type_defs.GetPropertygraphStreamOutputTypeDef" = (
        dataclasses.field()
    )

    lastEventId = field("lastEventId")
    lastTrxTimestampInMillis = field("lastTrxTimestampInMillis")
    format = field("format")

    @cached_property
    def records(self):  # pragma: no cover
        return PropertygraphRecord.make_many(self.boto3_raw_data["records"])

    totalRecords = field("totalRecords")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPropertygraphStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPropertygraphStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDFGraphSummaryValueMap:
    boto3_raw_data: "type_defs.RDFGraphSummaryValueMapTypeDef" = dataclasses.field()

    version = field("version")
    lastStatisticsComputationTime = field("lastStatisticsComputationTime")

    @cached_property
    def graphSummary(self):  # pragma: no cover
        return RDFGraphSummary.make_one(self.boto3_raw_data["graphSummary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RDFGraphSummaryValueMapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDFGraphSummaryValueMapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSparqlStreamOutput:
    boto3_raw_data: "type_defs.GetSparqlStreamOutputTypeDef" = dataclasses.field()

    lastEventId = field("lastEventId")
    lastTrxTimestampInMillis = field("lastTrxTimestampInMillis")
    format = field("format")

    @cached_property
    def records(self):  # pragma: no cover
        return SparqlRecord.make_many(self.boto3_raw_data["records"])

    totalRecords = field("totalRecords")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSparqlStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSparqlStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPropertygraphStatisticsOutput:
    boto3_raw_data: "type_defs.GetPropertygraphStatisticsOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def payload(self):  # pragma: no cover
        return Statistics.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPropertygraphStatisticsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPropertygraphStatisticsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSparqlStatisticsOutput:
    boto3_raw_data: "type_defs.GetSparqlStatisticsOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def payload(self):  # pragma: no cover
        return Statistics.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSparqlStatisticsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSparqlStatisticsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPropertygraphSummaryOutput:
    boto3_raw_data: "type_defs.GetPropertygraphSummaryOutputTypeDef" = (
        dataclasses.field()
    )

    statusCode = field("statusCode")

    @cached_property
    def payload(self):  # pragma: no cover
        return PropertygraphSummaryValueMap.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPropertygraphSummaryOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPropertygraphSummaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRDFGraphSummaryOutput:
    boto3_raw_data: "type_defs.GetRDFGraphSummaryOutputTypeDef" = dataclasses.field()

    statusCode = field("statusCode")

    @cached_property
    def payload(self):  # pragma: no cover
        return RDFGraphSummaryValueMap.make_one(self.boto3_raw_data["payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRDFGraphSummaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRDFGraphSummaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
