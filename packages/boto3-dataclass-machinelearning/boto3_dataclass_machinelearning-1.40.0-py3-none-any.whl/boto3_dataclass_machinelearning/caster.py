# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_machinelearning import type_defs as bs_td


class MACHINELEARNINGCaster:

    def add_tags(
        self,
        res: "bs_td.AddTagsOutputTypeDef",
    ) -> "dc_td.AddTagsOutput":
        return dc_td.AddTagsOutput.make_one(res)

    def create_batch_prediction(
        self,
        res: "bs_td.CreateBatchPredictionOutputTypeDef",
    ) -> "dc_td.CreateBatchPredictionOutput":
        return dc_td.CreateBatchPredictionOutput.make_one(res)

    def create_data_source_from_rds(
        self,
        res: "bs_td.CreateDataSourceFromRDSOutputTypeDef",
    ) -> "dc_td.CreateDataSourceFromRDSOutput":
        return dc_td.CreateDataSourceFromRDSOutput.make_one(res)

    def create_data_source_from_redshift(
        self,
        res: "bs_td.CreateDataSourceFromRedshiftOutputTypeDef",
    ) -> "dc_td.CreateDataSourceFromRedshiftOutput":
        return dc_td.CreateDataSourceFromRedshiftOutput.make_one(res)

    def create_data_source_from_s3(
        self,
        res: "bs_td.CreateDataSourceFromS3OutputTypeDef",
    ) -> "dc_td.CreateDataSourceFromS3Output":
        return dc_td.CreateDataSourceFromS3Output.make_one(res)

    def create_evaluation(
        self,
        res: "bs_td.CreateEvaluationOutputTypeDef",
    ) -> "dc_td.CreateEvaluationOutput":
        return dc_td.CreateEvaluationOutput.make_one(res)

    def create_ml_model(
        self,
        res: "bs_td.CreateMLModelOutputTypeDef",
    ) -> "dc_td.CreateMLModelOutput":
        return dc_td.CreateMLModelOutput.make_one(res)

    def create_realtime_endpoint(
        self,
        res: "bs_td.CreateRealtimeEndpointOutputTypeDef",
    ) -> "dc_td.CreateRealtimeEndpointOutput":
        return dc_td.CreateRealtimeEndpointOutput.make_one(res)

    def delete_batch_prediction(
        self,
        res: "bs_td.DeleteBatchPredictionOutputTypeDef",
    ) -> "dc_td.DeleteBatchPredictionOutput":
        return dc_td.DeleteBatchPredictionOutput.make_one(res)

    def delete_data_source(
        self,
        res: "bs_td.DeleteDataSourceOutputTypeDef",
    ) -> "dc_td.DeleteDataSourceOutput":
        return dc_td.DeleteDataSourceOutput.make_one(res)

    def delete_evaluation(
        self,
        res: "bs_td.DeleteEvaluationOutputTypeDef",
    ) -> "dc_td.DeleteEvaluationOutput":
        return dc_td.DeleteEvaluationOutput.make_one(res)

    def delete_ml_model(
        self,
        res: "bs_td.DeleteMLModelOutputTypeDef",
    ) -> "dc_td.DeleteMLModelOutput":
        return dc_td.DeleteMLModelOutput.make_one(res)

    def delete_realtime_endpoint(
        self,
        res: "bs_td.DeleteRealtimeEndpointOutputTypeDef",
    ) -> "dc_td.DeleteRealtimeEndpointOutput":
        return dc_td.DeleteRealtimeEndpointOutput.make_one(res)

    def delete_tags(
        self,
        res: "bs_td.DeleteTagsOutputTypeDef",
    ) -> "dc_td.DeleteTagsOutput":
        return dc_td.DeleteTagsOutput.make_one(res)

    def describe_batch_predictions(
        self,
        res: "bs_td.DescribeBatchPredictionsOutputTypeDef",
    ) -> "dc_td.DescribeBatchPredictionsOutput":
        return dc_td.DescribeBatchPredictionsOutput.make_one(res)

    def describe_data_sources(
        self,
        res: "bs_td.DescribeDataSourcesOutputTypeDef",
    ) -> "dc_td.DescribeDataSourcesOutput":
        return dc_td.DescribeDataSourcesOutput.make_one(res)

    def describe_evaluations(
        self,
        res: "bs_td.DescribeEvaluationsOutputTypeDef",
    ) -> "dc_td.DescribeEvaluationsOutput":
        return dc_td.DescribeEvaluationsOutput.make_one(res)

    def describe_ml_models(
        self,
        res: "bs_td.DescribeMLModelsOutputTypeDef",
    ) -> "dc_td.DescribeMLModelsOutput":
        return dc_td.DescribeMLModelsOutput.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.DescribeTagsOutputTypeDef",
    ) -> "dc_td.DescribeTagsOutput":
        return dc_td.DescribeTagsOutput.make_one(res)

    def get_batch_prediction(
        self,
        res: "bs_td.GetBatchPredictionOutputTypeDef",
    ) -> "dc_td.GetBatchPredictionOutput":
        return dc_td.GetBatchPredictionOutput.make_one(res)

    def get_data_source(
        self,
        res: "bs_td.GetDataSourceOutputTypeDef",
    ) -> "dc_td.GetDataSourceOutput":
        return dc_td.GetDataSourceOutput.make_one(res)

    def get_evaluation(
        self,
        res: "bs_td.GetEvaluationOutputTypeDef",
    ) -> "dc_td.GetEvaluationOutput":
        return dc_td.GetEvaluationOutput.make_one(res)

    def get_ml_model(
        self,
        res: "bs_td.GetMLModelOutputTypeDef",
    ) -> "dc_td.GetMLModelOutput":
        return dc_td.GetMLModelOutput.make_one(res)

    def predict(
        self,
        res: "bs_td.PredictOutputTypeDef",
    ) -> "dc_td.PredictOutput":
        return dc_td.PredictOutput.make_one(res)

    def update_batch_prediction(
        self,
        res: "bs_td.UpdateBatchPredictionOutputTypeDef",
    ) -> "dc_td.UpdateBatchPredictionOutput":
        return dc_td.UpdateBatchPredictionOutput.make_one(res)

    def update_data_source(
        self,
        res: "bs_td.UpdateDataSourceOutputTypeDef",
    ) -> "dc_td.UpdateDataSourceOutput":
        return dc_td.UpdateDataSourceOutput.make_one(res)

    def update_evaluation(
        self,
        res: "bs_td.UpdateEvaluationOutputTypeDef",
    ) -> "dc_td.UpdateEvaluationOutput":
        return dc_td.UpdateEvaluationOutput.make_one(res)

    def update_ml_model(
        self,
        res: "bs_td.UpdateMLModelOutputTypeDef",
    ) -> "dc_td.UpdateMLModelOutput":
        return dc_td.UpdateMLModelOutput.make_one(res)


machinelearning_caster = MACHINELEARNINGCaster()
