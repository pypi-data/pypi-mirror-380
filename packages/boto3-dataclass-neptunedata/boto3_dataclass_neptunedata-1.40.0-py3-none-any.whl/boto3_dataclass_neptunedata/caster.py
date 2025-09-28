# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_neptunedata import type_defs as bs_td


class NEPTUNEDATACaster:

    def cancel_gremlin_query(
        self,
        res: "bs_td.CancelGremlinQueryOutputTypeDef",
    ) -> "dc_td.CancelGremlinQueryOutput":
        return dc_td.CancelGremlinQueryOutput.make_one(res)

    def cancel_loader_job(
        self,
        res: "bs_td.CancelLoaderJobOutputTypeDef",
    ) -> "dc_td.CancelLoaderJobOutput":
        return dc_td.CancelLoaderJobOutput.make_one(res)

    def cancel_ml_data_processing_job(
        self,
        res: "bs_td.CancelMLDataProcessingJobOutputTypeDef",
    ) -> "dc_td.CancelMLDataProcessingJobOutput":
        return dc_td.CancelMLDataProcessingJobOutput.make_one(res)

    def cancel_ml_model_training_job(
        self,
        res: "bs_td.CancelMLModelTrainingJobOutputTypeDef",
    ) -> "dc_td.CancelMLModelTrainingJobOutput":
        return dc_td.CancelMLModelTrainingJobOutput.make_one(res)

    def cancel_ml_model_transform_job(
        self,
        res: "bs_td.CancelMLModelTransformJobOutputTypeDef",
    ) -> "dc_td.CancelMLModelTransformJobOutput":
        return dc_td.CancelMLModelTransformJobOutput.make_one(res)

    def cancel_open_cypher_query(
        self,
        res: "bs_td.CancelOpenCypherQueryOutputTypeDef",
    ) -> "dc_td.CancelOpenCypherQueryOutput":
        return dc_td.CancelOpenCypherQueryOutput.make_one(res)

    def create_ml_endpoint(
        self,
        res: "bs_td.CreateMLEndpointOutputTypeDef",
    ) -> "dc_td.CreateMLEndpointOutput":
        return dc_td.CreateMLEndpointOutput.make_one(res)

    def delete_ml_endpoint(
        self,
        res: "bs_td.DeleteMLEndpointOutputTypeDef",
    ) -> "dc_td.DeleteMLEndpointOutput":
        return dc_td.DeleteMLEndpointOutput.make_one(res)

    def delete_propertygraph_statistics(
        self,
        res: "bs_td.DeletePropertygraphStatisticsOutputTypeDef",
    ) -> "dc_td.DeletePropertygraphStatisticsOutput":
        return dc_td.DeletePropertygraphStatisticsOutput.make_one(res)

    def delete_sparql_statistics(
        self,
        res: "bs_td.DeleteSparqlStatisticsOutputTypeDef",
    ) -> "dc_td.DeleteSparqlStatisticsOutput":
        return dc_td.DeleteSparqlStatisticsOutput.make_one(res)

    def execute_fast_reset(
        self,
        res: "bs_td.ExecuteFastResetOutputTypeDef",
    ) -> "dc_td.ExecuteFastResetOutput":
        return dc_td.ExecuteFastResetOutput.make_one(res)

    def execute_gremlin_explain_query(
        self,
        res: "bs_td.ExecuteGremlinExplainQueryOutputTypeDef",
    ) -> "dc_td.ExecuteGremlinExplainQueryOutput":
        return dc_td.ExecuteGremlinExplainQueryOutput.make_one(res)

    def execute_gremlin_profile_query(
        self,
        res: "bs_td.ExecuteGremlinProfileQueryOutputTypeDef",
    ) -> "dc_td.ExecuteGremlinProfileQueryOutput":
        return dc_td.ExecuteGremlinProfileQueryOutput.make_one(res)

    def execute_gremlin_query(
        self,
        res: "bs_td.ExecuteGremlinQueryOutputTypeDef",
    ) -> "dc_td.ExecuteGremlinQueryOutput":
        return dc_td.ExecuteGremlinQueryOutput.make_one(res)

    def execute_open_cypher_explain_query(
        self,
        res: "bs_td.ExecuteOpenCypherExplainQueryOutputTypeDef",
    ) -> "dc_td.ExecuteOpenCypherExplainQueryOutput":
        return dc_td.ExecuteOpenCypherExplainQueryOutput.make_one(res)

    def execute_open_cypher_query(
        self,
        res: "bs_td.ExecuteOpenCypherQueryOutputTypeDef",
    ) -> "dc_td.ExecuteOpenCypherQueryOutput":
        return dc_td.ExecuteOpenCypherQueryOutput.make_one(res)

    def get_engine_status(
        self,
        res: "bs_td.GetEngineStatusOutputTypeDef",
    ) -> "dc_td.GetEngineStatusOutput":
        return dc_td.GetEngineStatusOutput.make_one(res)

    def get_gremlin_query_status(
        self,
        res: "bs_td.GetGremlinQueryStatusOutputTypeDef",
    ) -> "dc_td.GetGremlinQueryStatusOutput":
        return dc_td.GetGremlinQueryStatusOutput.make_one(res)

    def get_loader_job_status(
        self,
        res: "bs_td.GetLoaderJobStatusOutputTypeDef",
    ) -> "dc_td.GetLoaderJobStatusOutput":
        return dc_td.GetLoaderJobStatusOutput.make_one(res)

    def get_ml_data_processing_job(
        self,
        res: "bs_td.GetMLDataProcessingJobOutputTypeDef",
    ) -> "dc_td.GetMLDataProcessingJobOutput":
        return dc_td.GetMLDataProcessingJobOutput.make_one(res)

    def get_ml_endpoint(
        self,
        res: "bs_td.GetMLEndpointOutputTypeDef",
    ) -> "dc_td.GetMLEndpointOutput":
        return dc_td.GetMLEndpointOutput.make_one(res)

    def get_ml_model_training_job(
        self,
        res: "bs_td.GetMLModelTrainingJobOutputTypeDef",
    ) -> "dc_td.GetMLModelTrainingJobOutput":
        return dc_td.GetMLModelTrainingJobOutput.make_one(res)

    def get_ml_model_transform_job(
        self,
        res: "bs_td.GetMLModelTransformJobOutputTypeDef",
    ) -> "dc_td.GetMLModelTransformJobOutput":
        return dc_td.GetMLModelTransformJobOutput.make_one(res)

    def get_open_cypher_query_status(
        self,
        res: "bs_td.GetOpenCypherQueryStatusOutputTypeDef",
    ) -> "dc_td.GetOpenCypherQueryStatusOutput":
        return dc_td.GetOpenCypherQueryStatusOutput.make_one(res)

    def get_propertygraph_statistics(
        self,
        res: "bs_td.GetPropertygraphStatisticsOutputTypeDef",
    ) -> "dc_td.GetPropertygraphStatisticsOutput":
        return dc_td.GetPropertygraphStatisticsOutput.make_one(res)

    def get_propertygraph_stream(
        self,
        res: "bs_td.GetPropertygraphStreamOutputTypeDef",
    ) -> "dc_td.GetPropertygraphStreamOutput":
        return dc_td.GetPropertygraphStreamOutput.make_one(res)

    def get_propertygraph_summary(
        self,
        res: "bs_td.GetPropertygraphSummaryOutputTypeDef",
    ) -> "dc_td.GetPropertygraphSummaryOutput":
        return dc_td.GetPropertygraphSummaryOutput.make_one(res)

    def get_rdf_graph_summary(
        self,
        res: "bs_td.GetRDFGraphSummaryOutputTypeDef",
    ) -> "dc_td.GetRDFGraphSummaryOutput":
        return dc_td.GetRDFGraphSummaryOutput.make_one(res)

    def get_sparql_statistics(
        self,
        res: "bs_td.GetSparqlStatisticsOutputTypeDef",
    ) -> "dc_td.GetSparqlStatisticsOutput":
        return dc_td.GetSparqlStatisticsOutput.make_one(res)

    def get_sparql_stream(
        self,
        res: "bs_td.GetSparqlStreamOutputTypeDef",
    ) -> "dc_td.GetSparqlStreamOutput":
        return dc_td.GetSparqlStreamOutput.make_one(res)

    def list_gremlin_queries(
        self,
        res: "bs_td.ListGremlinQueriesOutputTypeDef",
    ) -> "dc_td.ListGremlinQueriesOutput":
        return dc_td.ListGremlinQueriesOutput.make_one(res)

    def list_loader_jobs(
        self,
        res: "bs_td.ListLoaderJobsOutputTypeDef",
    ) -> "dc_td.ListLoaderJobsOutput":
        return dc_td.ListLoaderJobsOutput.make_one(res)

    def list_ml_data_processing_jobs(
        self,
        res: "bs_td.ListMLDataProcessingJobsOutputTypeDef",
    ) -> "dc_td.ListMLDataProcessingJobsOutput":
        return dc_td.ListMLDataProcessingJobsOutput.make_one(res)

    def list_ml_endpoints(
        self,
        res: "bs_td.ListMLEndpointsOutputTypeDef",
    ) -> "dc_td.ListMLEndpointsOutput":
        return dc_td.ListMLEndpointsOutput.make_one(res)

    def list_ml_model_training_jobs(
        self,
        res: "bs_td.ListMLModelTrainingJobsOutputTypeDef",
    ) -> "dc_td.ListMLModelTrainingJobsOutput":
        return dc_td.ListMLModelTrainingJobsOutput.make_one(res)

    def list_ml_model_transform_jobs(
        self,
        res: "bs_td.ListMLModelTransformJobsOutputTypeDef",
    ) -> "dc_td.ListMLModelTransformJobsOutput":
        return dc_td.ListMLModelTransformJobsOutput.make_one(res)

    def list_open_cypher_queries(
        self,
        res: "bs_td.ListOpenCypherQueriesOutputTypeDef",
    ) -> "dc_td.ListOpenCypherQueriesOutput":
        return dc_td.ListOpenCypherQueriesOutput.make_one(res)

    def manage_propertygraph_statistics(
        self,
        res: "bs_td.ManagePropertygraphStatisticsOutputTypeDef",
    ) -> "dc_td.ManagePropertygraphStatisticsOutput":
        return dc_td.ManagePropertygraphStatisticsOutput.make_one(res)

    def manage_sparql_statistics(
        self,
        res: "bs_td.ManageSparqlStatisticsOutputTypeDef",
    ) -> "dc_td.ManageSparqlStatisticsOutput":
        return dc_td.ManageSparqlStatisticsOutput.make_one(res)

    def start_loader_job(
        self,
        res: "bs_td.StartLoaderJobOutputTypeDef",
    ) -> "dc_td.StartLoaderJobOutput":
        return dc_td.StartLoaderJobOutput.make_one(res)

    def start_ml_data_processing_job(
        self,
        res: "bs_td.StartMLDataProcessingJobOutputTypeDef",
    ) -> "dc_td.StartMLDataProcessingJobOutput":
        return dc_td.StartMLDataProcessingJobOutput.make_one(res)

    def start_ml_model_training_job(
        self,
        res: "bs_td.StartMLModelTrainingJobOutputTypeDef",
    ) -> "dc_td.StartMLModelTrainingJobOutput":
        return dc_td.StartMLModelTrainingJobOutput.make_one(res)

    def start_ml_model_transform_job(
        self,
        res: "bs_td.StartMLModelTransformJobOutputTypeDef",
    ) -> "dc_td.StartMLModelTransformJobOutput":
        return dc_td.StartMLModelTransformJobOutput.make_one(res)


neptunedata_caster = NEPTUNEDATACaster()
