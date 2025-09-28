# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_m2 import type_defs as bs_td


class M2Caster:

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_data_set_export_task(
        self,
        res: "bs_td.CreateDataSetExportTaskResponseTypeDef",
    ) -> "dc_td.CreateDataSetExportTaskResponse":
        return dc_td.CreateDataSetExportTaskResponse.make_one(res)

    def create_data_set_import_task(
        self,
        res: "bs_td.CreateDataSetImportTaskResponseTypeDef",
    ) -> "dc_td.CreateDataSetImportTaskResponse":
        return dc_td.CreateDataSetImportTaskResponse.make_one(res)

    def create_deployment(
        self,
        res: "bs_td.CreateDeploymentResponseTypeDef",
    ) -> "dc_td.CreateDeploymentResponse":
        return dc_td.CreateDeploymentResponse.make_one(res)

    def create_environment(
        self,
        res: "bs_td.CreateEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateEnvironmentResponse":
        return dc_td.CreateEnvironmentResponse.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationResponseTypeDef",
    ) -> "dc_td.GetApplicationResponse":
        return dc_td.GetApplicationResponse.make_one(res)

    def get_application_version(
        self,
        res: "bs_td.GetApplicationVersionResponseTypeDef",
    ) -> "dc_td.GetApplicationVersionResponse":
        return dc_td.GetApplicationVersionResponse.make_one(res)

    def get_batch_job_execution(
        self,
        res: "bs_td.GetBatchJobExecutionResponseTypeDef",
    ) -> "dc_td.GetBatchJobExecutionResponse":
        return dc_td.GetBatchJobExecutionResponse.make_one(res)

    def get_data_set_details(
        self,
        res: "bs_td.GetDataSetDetailsResponseTypeDef",
    ) -> "dc_td.GetDataSetDetailsResponse":
        return dc_td.GetDataSetDetailsResponse.make_one(res)

    def get_data_set_export_task(
        self,
        res: "bs_td.GetDataSetExportTaskResponseTypeDef",
    ) -> "dc_td.GetDataSetExportTaskResponse":
        return dc_td.GetDataSetExportTaskResponse.make_one(res)

    def get_data_set_import_task(
        self,
        res: "bs_td.GetDataSetImportTaskResponseTypeDef",
    ) -> "dc_td.GetDataSetImportTaskResponse":
        return dc_td.GetDataSetImportTaskResponse.make_one(res)

    def get_deployment(
        self,
        res: "bs_td.GetDeploymentResponseTypeDef",
    ) -> "dc_td.GetDeploymentResponse":
        return dc_td.GetDeploymentResponse.make_one(res)

    def get_environment(
        self,
        res: "bs_td.GetEnvironmentResponseTypeDef",
    ) -> "dc_td.GetEnvironmentResponse":
        return dc_td.GetEnvironmentResponse.make_one(res)

    def get_signed_bluinsights_url(
        self,
        res: "bs_td.GetSignedBluinsightsUrlResponseTypeDef",
    ) -> "dc_td.GetSignedBluinsightsUrlResponse":
        return dc_td.GetSignedBluinsightsUrlResponse.make_one(res)

    def list_application_versions(
        self,
        res: "bs_td.ListApplicationVersionsResponseTypeDef",
    ) -> "dc_td.ListApplicationVersionsResponse":
        return dc_td.ListApplicationVersionsResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_batch_job_definitions(
        self,
        res: "bs_td.ListBatchJobDefinitionsResponseTypeDef",
    ) -> "dc_td.ListBatchJobDefinitionsResponse":
        return dc_td.ListBatchJobDefinitionsResponse.make_one(res)

    def list_batch_job_executions(
        self,
        res: "bs_td.ListBatchJobExecutionsResponseTypeDef",
    ) -> "dc_td.ListBatchJobExecutionsResponse":
        return dc_td.ListBatchJobExecutionsResponse.make_one(res)

    def list_batch_job_restart_points(
        self,
        res: "bs_td.ListBatchJobRestartPointsResponseTypeDef",
    ) -> "dc_td.ListBatchJobRestartPointsResponse":
        return dc_td.ListBatchJobRestartPointsResponse.make_one(res)

    def list_data_set_export_history(
        self,
        res: "bs_td.ListDataSetExportHistoryResponseTypeDef",
    ) -> "dc_td.ListDataSetExportHistoryResponse":
        return dc_td.ListDataSetExportHistoryResponse.make_one(res)

    def list_data_set_import_history(
        self,
        res: "bs_td.ListDataSetImportHistoryResponseTypeDef",
    ) -> "dc_td.ListDataSetImportHistoryResponse":
        return dc_td.ListDataSetImportHistoryResponse.make_one(res)

    def list_data_sets(
        self,
        res: "bs_td.ListDataSetsResponseTypeDef",
    ) -> "dc_td.ListDataSetsResponse":
        return dc_td.ListDataSetsResponse.make_one(res)

    def list_deployments(
        self,
        res: "bs_td.ListDeploymentsResponseTypeDef",
    ) -> "dc_td.ListDeploymentsResponse":
        return dc_td.ListDeploymentsResponse.make_one(res)

    def list_engine_versions(
        self,
        res: "bs_td.ListEngineVersionsResponseTypeDef",
    ) -> "dc_td.ListEngineVersionsResponse":
        return dc_td.ListEngineVersionsResponse.make_one(res)

    def list_environments(
        self,
        res: "bs_td.ListEnvironmentsResponseTypeDef",
    ) -> "dc_td.ListEnvironmentsResponse":
        return dc_td.ListEnvironmentsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_batch_job(
        self,
        res: "bs_td.StartBatchJobResponseTypeDef",
    ) -> "dc_td.StartBatchJobResponse":
        return dc_td.StartBatchJobResponse.make_one(res)

    def update_application(
        self,
        res: "bs_td.UpdateApplicationResponseTypeDef",
    ) -> "dc_td.UpdateApplicationResponse":
        return dc_td.UpdateApplicationResponse.make_one(res)

    def update_environment(
        self,
        res: "bs_td.UpdateEnvironmentResponseTypeDef",
    ) -> "dc_td.UpdateEnvironmentResponse":
        return dc_td.UpdateEnvironmentResponse.make_one(res)


m2_caster = M2Caster()
