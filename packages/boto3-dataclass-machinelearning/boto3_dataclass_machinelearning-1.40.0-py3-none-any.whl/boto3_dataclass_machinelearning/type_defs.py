# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_machinelearning import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class BatchPrediction:
    boto3_raw_data: "type_defs.BatchPredictionTypeDef" = dataclasses.field()

    BatchPredictionId = field("BatchPredictionId")
    MLModelId = field("MLModelId")
    BatchPredictionDataSourceId = field("BatchPredictionDataSourceId")
    InputDataLocationS3 = field("InputDataLocationS3")
    CreatedByIamUser = field("CreatedByIamUser")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Name = field("Name")
    Status = field("Status")
    OutputUri = field("OutputUri")
    Message = field("Message")
    ComputeTime = field("ComputeTime")
    FinishedAt = field("FinishedAt")
    StartedAt = field("StartedAt")
    TotalRecordCount = field("TotalRecordCount")
    InvalidRecordCount = field("InvalidRecordCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchPredictionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchPredictionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBatchPredictionInput:
    boto3_raw_data: "type_defs.CreateBatchPredictionInputTypeDef" = dataclasses.field()

    BatchPredictionId = field("BatchPredictionId")
    MLModelId = field("MLModelId")
    BatchPredictionDataSourceId = field("BatchPredictionDataSourceId")
    OutputUri = field("OutputUri")
    BatchPredictionName = field("BatchPredictionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBatchPredictionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchPredictionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataSpec:
    boto3_raw_data: "type_defs.S3DataSpecTypeDef" = dataclasses.field()

    DataLocationS3 = field("DataLocationS3")
    DataRearrangement = field("DataRearrangement")
    DataSchema = field("DataSchema")
    DataSchemaLocationS3 = field("DataSchemaLocationS3")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DataSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DataSpecTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEvaluationInput:
    boto3_raw_data: "type_defs.CreateEvaluationInputTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")
    MLModelId = field("MLModelId")
    EvaluationDataSourceId = field("EvaluationDataSourceId")
    EvaluationName = field("EvaluationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEvaluationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEvaluationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMLModelInput:
    boto3_raw_data: "type_defs.CreateMLModelInputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")
    MLModelType = field("MLModelType")
    TrainingDataSourceId = field("TrainingDataSourceId")
    MLModelName = field("MLModelName")
    Parameters = field("Parameters")
    Recipe = field("Recipe")
    RecipeUri = field("RecipeUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMLModelInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMLModelInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRealtimeEndpointInput:
    boto3_raw_data: "type_defs.CreateRealtimeEndpointInputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRealtimeEndpointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRealtimeEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealtimeEndpointInfo:
    boto3_raw_data: "type_defs.RealtimeEndpointInfoTypeDef" = dataclasses.field()

    PeakRequestsPerSecond = field("PeakRequestsPerSecond")
    CreatedAt = field("CreatedAt")
    EndpointUrl = field("EndpointUrl")
    EndpointStatus = field("EndpointStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RealtimeEndpointInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealtimeEndpointInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBatchPredictionInput:
    boto3_raw_data: "type_defs.DeleteBatchPredictionInputTypeDef" = dataclasses.field()

    BatchPredictionId = field("BatchPredictionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBatchPredictionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBatchPredictionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceInput:
    boto3_raw_data: "type_defs.DeleteDataSourceInputTypeDef" = dataclasses.field()

    DataSourceId = field("DataSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEvaluationInput:
    boto3_raw_data: "type_defs.DeleteEvaluationInputTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEvaluationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEvaluationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMLModelInput:
    boto3_raw_data: "type_defs.DeleteMLModelInputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMLModelInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMLModelInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRealtimeEndpointInput:
    boto3_raw_data: "type_defs.DeleteRealtimeEndpointInputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRealtimeEndpointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRealtimeEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagsInput:
    boto3_raw_data: "type_defs.DeleteTagsInputTypeDef" = dataclasses.field()

    TagKeys = field("TagKeys")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteTagsInputTypeDef"]],
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
class DescribeBatchPredictionsInput:
    boto3_raw_data: "type_defs.DescribeBatchPredictionsInputTypeDef" = (
        dataclasses.field()
    )

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBatchPredictionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchPredictionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSourcesInput:
    boto3_raw_data: "type_defs.DescribeDataSourcesInputTypeDef" = dataclasses.field()

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDataSourcesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEvaluationsInput:
    boto3_raw_data: "type_defs.DescribeEvaluationsInputTypeDef" = dataclasses.field()

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEvaluationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEvaluationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMLModelsInput:
    boto3_raw_data: "type_defs.DescribeMLModelsInputTypeDef" = dataclasses.field()

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMLModelsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMLModelsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsInput:
    boto3_raw_data: "type_defs.DescribeTagsInputTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceMetrics:
    boto3_raw_data: "type_defs.PerformanceMetricsTypeDef" = dataclasses.field()

    Properties = field("Properties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PerformanceMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBatchPredictionInput:
    boto3_raw_data: "type_defs.GetBatchPredictionInputTypeDef" = dataclasses.field()

    BatchPredictionId = field("BatchPredictionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBatchPredictionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBatchPredictionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceInput:
    boto3_raw_data: "type_defs.GetDataSourceInputTypeDef" = dataclasses.field()

    DataSourceId = field("DataSourceId")
    Verbose = field("Verbose")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvaluationInput:
    boto3_raw_data: "type_defs.GetEvaluationInputTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEvaluationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvaluationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLModelInput:
    boto3_raw_data: "type_defs.GetMLModelInputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")
    Verbose = field("Verbose")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMLModelInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetMLModelInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictInput:
    boto3_raw_data: "type_defs.PredictInputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")
    Record = field("Record")
    PredictEndpoint = field("PredictEndpoint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredictInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Prediction:
    boto3_raw_data: "type_defs.PredictionTypeDef" = dataclasses.field()

    predictedLabel = field("predictedLabel")
    predictedValue = field("predictedValue")
    predictedScores = field("predictedScores")
    details = field("details")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredictionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDatabaseCredentials:
    boto3_raw_data: "type_defs.RDSDatabaseCredentialsTypeDef" = dataclasses.field()

    Username = field("Username")
    Password = field("Password")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RDSDatabaseCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSDatabaseCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDatabase:
    boto3_raw_data: "type_defs.RDSDatabaseTypeDef" = dataclasses.field()

    InstanceIdentifier = field("InstanceIdentifier")
    DatabaseName = field("DatabaseName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RDSDatabaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RDSDatabaseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDatabaseCredentials:
    boto3_raw_data: "type_defs.RedshiftDatabaseCredentialsTypeDef" = dataclasses.field()

    Username = field("Username")
    Password = field("Password")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftDatabaseCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDatabaseCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDatabase:
    boto3_raw_data: "type_defs.RedshiftDatabaseTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RedshiftDatabaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDatabaseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBatchPredictionInput:
    boto3_raw_data: "type_defs.UpdateBatchPredictionInputTypeDef" = dataclasses.field()

    BatchPredictionId = field("BatchPredictionId")
    BatchPredictionName = field("BatchPredictionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBatchPredictionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBatchPredictionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceInput:
    boto3_raw_data: "type_defs.UpdateDataSourceInputTypeDef" = dataclasses.field()

    DataSourceId = field("DataSourceId")
    DataSourceName = field("DataSourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEvaluationInput:
    boto3_raw_data: "type_defs.UpdateEvaluationInputTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")
    EvaluationName = field("EvaluationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEvaluationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEvaluationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMLModelInput:
    boto3_raw_data: "type_defs.UpdateMLModelInputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")
    MLModelName = field("MLModelName")
    ScoreThreshold = field("ScoreThreshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMLModelInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMLModelInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsInput:
    boto3_raw_data: "type_defs.AddTagsInputTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsOutput:
    boto3_raw_data: "type_defs.AddTagsOutputTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddTagsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddTagsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBatchPredictionOutput:
    boto3_raw_data: "type_defs.CreateBatchPredictionOutputTypeDef" = dataclasses.field()

    BatchPredictionId = field("BatchPredictionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBatchPredictionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchPredictionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceFromRDSOutput:
    boto3_raw_data: "type_defs.CreateDataSourceFromRDSOutputTypeDef" = (
        dataclasses.field()
    )

    DataSourceId = field("DataSourceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataSourceFromRDSOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceFromRDSOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceFromRedshiftOutput:
    boto3_raw_data: "type_defs.CreateDataSourceFromRedshiftOutputTypeDef" = (
        dataclasses.field()
    )

    DataSourceId = field("DataSourceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataSourceFromRedshiftOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceFromRedshiftOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceFromS3Output:
    boto3_raw_data: "type_defs.CreateDataSourceFromS3OutputTypeDef" = (
        dataclasses.field()
    )

    DataSourceId = field("DataSourceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceFromS3OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceFromS3OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEvaluationOutput:
    boto3_raw_data: "type_defs.CreateEvaluationOutputTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEvaluationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEvaluationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMLModelOutput:
    boto3_raw_data: "type_defs.CreateMLModelOutputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMLModelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMLModelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBatchPredictionOutput:
    boto3_raw_data: "type_defs.DeleteBatchPredictionOutputTypeDef" = dataclasses.field()

    BatchPredictionId = field("BatchPredictionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBatchPredictionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBatchPredictionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceOutput:
    boto3_raw_data: "type_defs.DeleteDataSourceOutputTypeDef" = dataclasses.field()

    DataSourceId = field("DataSourceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEvaluationOutput:
    boto3_raw_data: "type_defs.DeleteEvaluationOutputTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEvaluationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEvaluationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMLModelOutput:
    boto3_raw_data: "type_defs.DeleteMLModelOutputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMLModelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMLModelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagsOutput:
    boto3_raw_data: "type_defs.DeleteTagsOutputTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTagsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTagsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsOutput:
    boto3_raw_data: "type_defs.DescribeTagsOutputTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBatchPredictionOutput:
    boto3_raw_data: "type_defs.GetBatchPredictionOutputTypeDef" = dataclasses.field()

    BatchPredictionId = field("BatchPredictionId")
    MLModelId = field("MLModelId")
    BatchPredictionDataSourceId = field("BatchPredictionDataSourceId")
    InputDataLocationS3 = field("InputDataLocationS3")
    CreatedByIamUser = field("CreatedByIamUser")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Name = field("Name")
    Status = field("Status")
    OutputUri = field("OutputUri")
    LogUri = field("LogUri")
    Message = field("Message")
    ComputeTime = field("ComputeTime")
    FinishedAt = field("FinishedAt")
    StartedAt = field("StartedAt")
    TotalRecordCount = field("TotalRecordCount")
    InvalidRecordCount = field("InvalidRecordCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBatchPredictionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBatchPredictionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBatchPredictionOutput:
    boto3_raw_data: "type_defs.UpdateBatchPredictionOutputTypeDef" = dataclasses.field()

    BatchPredictionId = field("BatchPredictionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBatchPredictionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBatchPredictionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceOutput:
    boto3_raw_data: "type_defs.UpdateDataSourceOutputTypeDef" = dataclasses.field()

    DataSourceId = field("DataSourceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEvaluationOutput:
    boto3_raw_data: "type_defs.UpdateEvaluationOutputTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEvaluationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEvaluationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMLModelOutput:
    boto3_raw_data: "type_defs.UpdateMLModelOutputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMLModelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMLModelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBatchPredictionsOutput:
    boto3_raw_data: "type_defs.DescribeBatchPredictionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Results(self):  # pragma: no cover
        return BatchPrediction.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBatchPredictionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchPredictionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceFromS3Input:
    boto3_raw_data: "type_defs.CreateDataSourceFromS3InputTypeDef" = dataclasses.field()

    DataSourceId = field("DataSourceId")

    @cached_property
    def DataSpec(self):  # pragma: no cover
        return S3DataSpec.make_one(self.boto3_raw_data["DataSpec"])

    DataSourceName = field("DataSourceName")
    ComputeStatistics = field("ComputeStatistics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceFromS3InputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceFromS3InputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRealtimeEndpointOutput:
    boto3_raw_data: "type_defs.CreateRealtimeEndpointOutputTypeDef" = (
        dataclasses.field()
    )

    MLModelId = field("MLModelId")

    @cached_property
    def RealtimeEndpointInfo(self):  # pragma: no cover
        return RealtimeEndpointInfo.make_one(
            self.boto3_raw_data["RealtimeEndpointInfo"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRealtimeEndpointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRealtimeEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRealtimeEndpointOutput:
    boto3_raw_data: "type_defs.DeleteRealtimeEndpointOutputTypeDef" = (
        dataclasses.field()
    )

    MLModelId = field("MLModelId")

    @cached_property
    def RealtimeEndpointInfo(self):  # pragma: no cover
        return RealtimeEndpointInfo.make_one(
            self.boto3_raw_data["RealtimeEndpointInfo"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRealtimeEndpointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRealtimeEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLModelOutput:
    boto3_raw_data: "type_defs.GetMLModelOutputTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")
    TrainingDataSourceId = field("TrainingDataSourceId")
    CreatedByIamUser = field("CreatedByIamUser")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Name = field("Name")
    Status = field("Status")
    SizeInBytes = field("SizeInBytes")

    @cached_property
    def EndpointInfo(self):  # pragma: no cover
        return RealtimeEndpointInfo.make_one(self.boto3_raw_data["EndpointInfo"])

    TrainingParameters = field("TrainingParameters")
    InputDataLocationS3 = field("InputDataLocationS3")
    MLModelType = field("MLModelType")
    ScoreThreshold = field("ScoreThreshold")
    ScoreThresholdLastUpdatedAt = field("ScoreThresholdLastUpdatedAt")
    LogUri = field("LogUri")
    Message = field("Message")
    ComputeTime = field("ComputeTime")
    FinishedAt = field("FinishedAt")
    StartedAt = field("StartedAt")
    Recipe = field("Recipe")
    Schema = field("Schema")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMLModelOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLModelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MLModel:
    boto3_raw_data: "type_defs.MLModelTypeDef" = dataclasses.field()

    MLModelId = field("MLModelId")
    TrainingDataSourceId = field("TrainingDataSourceId")
    CreatedByIamUser = field("CreatedByIamUser")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Name = field("Name")
    Status = field("Status")
    SizeInBytes = field("SizeInBytes")

    @cached_property
    def EndpointInfo(self):  # pragma: no cover
        return RealtimeEndpointInfo.make_one(self.boto3_raw_data["EndpointInfo"])

    TrainingParameters = field("TrainingParameters")
    InputDataLocationS3 = field("InputDataLocationS3")
    Algorithm = field("Algorithm")
    MLModelType = field("MLModelType")
    ScoreThreshold = field("ScoreThreshold")
    ScoreThresholdLastUpdatedAt = field("ScoreThresholdLastUpdatedAt")
    Message = field("Message")
    ComputeTime = field("ComputeTime")
    FinishedAt = field("FinishedAt")
    StartedAt = field("StartedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MLModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MLModelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBatchPredictionsInputPaginate:
    boto3_raw_data: "type_defs.DescribeBatchPredictionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBatchPredictionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchPredictionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSourcesInputPaginate:
    boto3_raw_data: "type_defs.DescribeDataSourcesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDataSourcesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSourcesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEvaluationsInputPaginate:
    boto3_raw_data: "type_defs.DescribeEvaluationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEvaluationsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEvaluationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMLModelsInputPaginate:
    boto3_raw_data: "type_defs.DescribeMLModelsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMLModelsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMLModelsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBatchPredictionsInputWait:
    boto3_raw_data: "type_defs.DescribeBatchPredictionsInputWaitTypeDef" = (
        dataclasses.field()
    )

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBatchPredictionsInputWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchPredictionsInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSourcesInputWait:
    boto3_raw_data: "type_defs.DescribeDataSourcesInputWaitTypeDef" = (
        dataclasses.field()
    )

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDataSourcesInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSourcesInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEvaluationsInputWait:
    boto3_raw_data: "type_defs.DescribeEvaluationsInputWaitTypeDef" = (
        dataclasses.field()
    )

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEvaluationsInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEvaluationsInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMLModelsInputWait:
    boto3_raw_data: "type_defs.DescribeMLModelsInputWaitTypeDef" = dataclasses.field()

    FilterVariable = field("FilterVariable")
    EQ = field("EQ")
    GT = field("GT")
    LT = field("LT")
    GE = field("GE")
    LE = field("LE")
    NE = field("NE")
    Prefix = field("Prefix")
    SortOrder = field("SortOrder")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMLModelsInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMLModelsInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Evaluation:
    boto3_raw_data: "type_defs.EvaluationTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")
    MLModelId = field("MLModelId")
    EvaluationDataSourceId = field("EvaluationDataSourceId")
    InputDataLocationS3 = field("InputDataLocationS3")
    CreatedByIamUser = field("CreatedByIamUser")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Name = field("Name")
    Status = field("Status")

    @cached_property
    def PerformanceMetrics(self):  # pragma: no cover
        return PerformanceMetrics.make_one(self.boto3_raw_data["PerformanceMetrics"])

    Message = field("Message")
    ComputeTime = field("ComputeTime")
    FinishedAt = field("FinishedAt")
    StartedAt = field("StartedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvaluationOutput:
    boto3_raw_data: "type_defs.GetEvaluationOutputTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")
    MLModelId = field("MLModelId")
    EvaluationDataSourceId = field("EvaluationDataSourceId")
    InputDataLocationS3 = field("InputDataLocationS3")
    CreatedByIamUser = field("CreatedByIamUser")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Name = field("Name")
    Status = field("Status")

    @cached_property
    def PerformanceMetrics(self):  # pragma: no cover
        return PerformanceMetrics.make_one(self.boto3_raw_data["PerformanceMetrics"])

    LogUri = field("LogUri")
    Message = field("Message")
    ComputeTime = field("ComputeTime")
    FinishedAt = field("FinishedAt")
    StartedAt = field("StartedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEvaluationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvaluationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictOutput:
    boto3_raw_data: "type_defs.PredictOutputTypeDef" = dataclasses.field()

    @cached_property
    def Prediction(self):  # pragma: no cover
        return Prediction.make_one(self.boto3_raw_data["Prediction"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredictOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDataSpec:
    boto3_raw_data: "type_defs.RDSDataSpecTypeDef" = dataclasses.field()

    @cached_property
    def DatabaseInformation(self):  # pragma: no cover
        return RDSDatabase.make_one(self.boto3_raw_data["DatabaseInformation"])

    SelectSqlQuery = field("SelectSqlQuery")

    @cached_property
    def DatabaseCredentials(self):  # pragma: no cover
        return RDSDatabaseCredentials.make_one(
            self.boto3_raw_data["DatabaseCredentials"]
        )

    S3StagingLocation = field("S3StagingLocation")
    ResourceRole = field("ResourceRole")
    ServiceRole = field("ServiceRole")
    SubnetId = field("SubnetId")
    SecurityGroupIds = field("SecurityGroupIds")
    DataRearrangement = field("DataRearrangement")
    DataSchema = field("DataSchema")
    DataSchemaUri = field("DataSchemaUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RDSDataSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RDSDataSpecTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSMetadata:
    boto3_raw_data: "type_defs.RDSMetadataTypeDef" = dataclasses.field()

    @cached_property
    def Database(self):  # pragma: no cover
        return RDSDatabase.make_one(self.boto3_raw_data["Database"])

    DatabaseUserName = field("DatabaseUserName")
    SelectSqlQuery = field("SelectSqlQuery")
    ResourceRole = field("ResourceRole")
    ServiceRole = field("ServiceRole")
    DataPipelineId = field("DataPipelineId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RDSMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RDSMetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDataSpec:
    boto3_raw_data: "type_defs.RedshiftDataSpecTypeDef" = dataclasses.field()

    @cached_property
    def DatabaseInformation(self):  # pragma: no cover
        return RedshiftDatabase.make_one(self.boto3_raw_data["DatabaseInformation"])

    SelectSqlQuery = field("SelectSqlQuery")

    @cached_property
    def DatabaseCredentials(self):  # pragma: no cover
        return RedshiftDatabaseCredentials.make_one(
            self.boto3_raw_data["DatabaseCredentials"]
        )

    S3StagingLocation = field("S3StagingLocation")
    DataRearrangement = field("DataRearrangement")
    DataSchema = field("DataSchema")
    DataSchemaUri = field("DataSchemaUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RedshiftDataSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDataSpecTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftMetadata:
    boto3_raw_data: "type_defs.RedshiftMetadataTypeDef" = dataclasses.field()

    @cached_property
    def RedshiftDatabase(self):  # pragma: no cover
        return RedshiftDatabase.make_one(self.boto3_raw_data["RedshiftDatabase"])

    DatabaseUserName = field("DatabaseUserName")
    SelectSqlQuery = field("SelectSqlQuery")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RedshiftMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMLModelsOutput:
    boto3_raw_data: "type_defs.DescribeMLModelsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Results(self):  # pragma: no cover
        return MLModel.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMLModelsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMLModelsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEvaluationsOutput:
    boto3_raw_data: "type_defs.DescribeEvaluationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Results(self):  # pragma: no cover
        return Evaluation.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEvaluationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEvaluationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceFromRDSInput:
    boto3_raw_data: "type_defs.CreateDataSourceFromRDSInputTypeDef" = (
        dataclasses.field()
    )

    DataSourceId = field("DataSourceId")

    @cached_property
    def RDSData(self):  # pragma: no cover
        return RDSDataSpec.make_one(self.boto3_raw_data["RDSData"])

    RoleARN = field("RoleARN")
    DataSourceName = field("DataSourceName")
    ComputeStatistics = field("ComputeStatistics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceFromRDSInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceFromRDSInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceFromRedshiftInput:
    boto3_raw_data: "type_defs.CreateDataSourceFromRedshiftInputTypeDef" = (
        dataclasses.field()
    )

    DataSourceId = field("DataSourceId")

    @cached_property
    def DataSpec(self):  # pragma: no cover
        return RedshiftDataSpec.make_one(self.boto3_raw_data["DataSpec"])

    RoleARN = field("RoleARN")
    DataSourceName = field("DataSourceName")
    ComputeStatistics = field("ComputeStatistics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataSourceFromRedshiftInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceFromRedshiftInputTypeDef"]
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

    DataSourceId = field("DataSourceId")
    DataLocationS3 = field("DataLocationS3")
    DataRearrangement = field("DataRearrangement")
    CreatedByIamUser = field("CreatedByIamUser")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    DataSizeInBytes = field("DataSizeInBytes")
    NumberOfFiles = field("NumberOfFiles")
    Name = field("Name")
    Status = field("Status")
    Message = field("Message")

    @cached_property
    def RedshiftMetadata(self):  # pragma: no cover
        return RedshiftMetadata.make_one(self.boto3_raw_data["RedshiftMetadata"])

    @cached_property
    def RDSMetadata(self):  # pragma: no cover
        return RDSMetadata.make_one(self.boto3_raw_data["RDSMetadata"])

    RoleARN = field("RoleARN")
    ComputeStatistics = field("ComputeStatistics")
    ComputeTime = field("ComputeTime")
    FinishedAt = field("FinishedAt")
    StartedAt = field("StartedAt")

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
class GetDataSourceOutput:
    boto3_raw_data: "type_defs.GetDataSourceOutputTypeDef" = dataclasses.field()

    DataSourceId = field("DataSourceId")
    DataLocationS3 = field("DataLocationS3")
    DataRearrangement = field("DataRearrangement")
    CreatedByIamUser = field("CreatedByIamUser")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    DataSizeInBytes = field("DataSizeInBytes")
    NumberOfFiles = field("NumberOfFiles")
    Name = field("Name")
    Status = field("Status")
    LogUri = field("LogUri")
    Message = field("Message")

    @cached_property
    def RedshiftMetadata(self):  # pragma: no cover
        return RedshiftMetadata.make_one(self.boto3_raw_data["RedshiftMetadata"])

    @cached_property
    def RDSMetadata(self):  # pragma: no cover
        return RDSMetadata.make_one(self.boto3_raw_data["RDSMetadata"])

    RoleARN = field("RoleARN")
    ComputeStatistics = field("ComputeStatistics")
    ComputeTime = field("ComputeTime")
    FinishedAt = field("FinishedAt")
    StartedAt = field("StartedAt")
    DataSourceSchema = field("DataSourceSchema")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSourcesOutput:
    boto3_raw_data: "type_defs.DescribeDataSourcesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Results(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDataSourcesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
