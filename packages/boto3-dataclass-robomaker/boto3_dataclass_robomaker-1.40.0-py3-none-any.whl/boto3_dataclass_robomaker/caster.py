# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_robomaker import type_defs as bs_td


class ROBOMAKERCaster:

    def batch_delete_worlds(
        self,
        res: "bs_td.BatchDeleteWorldsResponseTypeDef",
    ) -> "dc_td.BatchDeleteWorldsResponse":
        return dc_td.BatchDeleteWorldsResponse.make_one(res)

    def batch_describe_simulation_job(
        self,
        res: "bs_td.BatchDescribeSimulationJobResponseTypeDef",
    ) -> "dc_td.BatchDescribeSimulationJobResponse":
        return dc_td.BatchDescribeSimulationJobResponse.make_one(res)

    def create_deployment_job(
        self,
        res: "bs_td.CreateDeploymentJobResponseTypeDef",
    ) -> "dc_td.CreateDeploymentJobResponse":
        return dc_td.CreateDeploymentJobResponse.make_one(res)

    def create_fleet(
        self,
        res: "bs_td.CreateFleetResponseTypeDef",
    ) -> "dc_td.CreateFleetResponse":
        return dc_td.CreateFleetResponse.make_one(res)

    def create_robot(
        self,
        res: "bs_td.CreateRobotResponseTypeDef",
    ) -> "dc_td.CreateRobotResponse":
        return dc_td.CreateRobotResponse.make_one(res)

    def create_robot_application(
        self,
        res: "bs_td.CreateRobotApplicationResponseTypeDef",
    ) -> "dc_td.CreateRobotApplicationResponse":
        return dc_td.CreateRobotApplicationResponse.make_one(res)

    def create_robot_application_version(
        self,
        res: "bs_td.CreateRobotApplicationVersionResponseTypeDef",
    ) -> "dc_td.CreateRobotApplicationVersionResponse":
        return dc_td.CreateRobotApplicationVersionResponse.make_one(res)

    def create_simulation_application(
        self,
        res: "bs_td.CreateSimulationApplicationResponseTypeDef",
    ) -> "dc_td.CreateSimulationApplicationResponse":
        return dc_td.CreateSimulationApplicationResponse.make_one(res)

    def create_simulation_application_version(
        self,
        res: "bs_td.CreateSimulationApplicationVersionResponseTypeDef",
    ) -> "dc_td.CreateSimulationApplicationVersionResponse":
        return dc_td.CreateSimulationApplicationVersionResponse.make_one(res)

    def create_simulation_job(
        self,
        res: "bs_td.CreateSimulationJobResponseTypeDef",
    ) -> "dc_td.CreateSimulationJobResponse":
        return dc_td.CreateSimulationJobResponse.make_one(res)

    def create_world_export_job(
        self,
        res: "bs_td.CreateWorldExportJobResponseTypeDef",
    ) -> "dc_td.CreateWorldExportJobResponse":
        return dc_td.CreateWorldExportJobResponse.make_one(res)

    def create_world_generation_job(
        self,
        res: "bs_td.CreateWorldGenerationJobResponseTypeDef",
    ) -> "dc_td.CreateWorldGenerationJobResponse":
        return dc_td.CreateWorldGenerationJobResponse.make_one(res)

    def create_world_template(
        self,
        res: "bs_td.CreateWorldTemplateResponseTypeDef",
    ) -> "dc_td.CreateWorldTemplateResponse":
        return dc_td.CreateWorldTemplateResponse.make_one(res)

    def deregister_robot(
        self,
        res: "bs_td.DeregisterRobotResponseTypeDef",
    ) -> "dc_td.DeregisterRobotResponse":
        return dc_td.DeregisterRobotResponse.make_one(res)

    def describe_deployment_job(
        self,
        res: "bs_td.DescribeDeploymentJobResponseTypeDef",
    ) -> "dc_td.DescribeDeploymentJobResponse":
        return dc_td.DescribeDeploymentJobResponse.make_one(res)

    def describe_fleet(
        self,
        res: "bs_td.DescribeFleetResponseTypeDef",
    ) -> "dc_td.DescribeFleetResponse":
        return dc_td.DescribeFleetResponse.make_one(res)

    def describe_robot(
        self,
        res: "bs_td.DescribeRobotResponseTypeDef",
    ) -> "dc_td.DescribeRobotResponse":
        return dc_td.DescribeRobotResponse.make_one(res)

    def describe_robot_application(
        self,
        res: "bs_td.DescribeRobotApplicationResponseTypeDef",
    ) -> "dc_td.DescribeRobotApplicationResponse":
        return dc_td.DescribeRobotApplicationResponse.make_one(res)

    def describe_simulation_application(
        self,
        res: "bs_td.DescribeSimulationApplicationResponseTypeDef",
    ) -> "dc_td.DescribeSimulationApplicationResponse":
        return dc_td.DescribeSimulationApplicationResponse.make_one(res)

    def describe_simulation_job(
        self,
        res: "bs_td.DescribeSimulationJobResponseTypeDef",
    ) -> "dc_td.DescribeSimulationJobResponse":
        return dc_td.DescribeSimulationJobResponse.make_one(res)

    def describe_simulation_job_batch(
        self,
        res: "bs_td.DescribeSimulationJobBatchResponseTypeDef",
    ) -> "dc_td.DescribeSimulationJobBatchResponse":
        return dc_td.DescribeSimulationJobBatchResponse.make_one(res)

    def describe_world(
        self,
        res: "bs_td.DescribeWorldResponseTypeDef",
    ) -> "dc_td.DescribeWorldResponse":
        return dc_td.DescribeWorldResponse.make_one(res)

    def describe_world_export_job(
        self,
        res: "bs_td.DescribeWorldExportJobResponseTypeDef",
    ) -> "dc_td.DescribeWorldExportJobResponse":
        return dc_td.DescribeWorldExportJobResponse.make_one(res)

    def describe_world_generation_job(
        self,
        res: "bs_td.DescribeWorldGenerationJobResponseTypeDef",
    ) -> "dc_td.DescribeWorldGenerationJobResponse":
        return dc_td.DescribeWorldGenerationJobResponse.make_one(res)

    def describe_world_template(
        self,
        res: "bs_td.DescribeWorldTemplateResponseTypeDef",
    ) -> "dc_td.DescribeWorldTemplateResponse":
        return dc_td.DescribeWorldTemplateResponse.make_one(res)

    def get_world_template_body(
        self,
        res: "bs_td.GetWorldTemplateBodyResponseTypeDef",
    ) -> "dc_td.GetWorldTemplateBodyResponse":
        return dc_td.GetWorldTemplateBodyResponse.make_one(res)

    def list_deployment_jobs(
        self,
        res: "bs_td.ListDeploymentJobsResponseTypeDef",
    ) -> "dc_td.ListDeploymentJobsResponse":
        return dc_td.ListDeploymentJobsResponse.make_one(res)

    def list_fleets(
        self,
        res: "bs_td.ListFleetsResponseTypeDef",
    ) -> "dc_td.ListFleetsResponse":
        return dc_td.ListFleetsResponse.make_one(res)

    def list_robot_applications(
        self,
        res: "bs_td.ListRobotApplicationsResponseTypeDef",
    ) -> "dc_td.ListRobotApplicationsResponse":
        return dc_td.ListRobotApplicationsResponse.make_one(res)

    def list_robots(
        self,
        res: "bs_td.ListRobotsResponseTypeDef",
    ) -> "dc_td.ListRobotsResponse":
        return dc_td.ListRobotsResponse.make_one(res)

    def list_simulation_applications(
        self,
        res: "bs_td.ListSimulationApplicationsResponseTypeDef",
    ) -> "dc_td.ListSimulationApplicationsResponse":
        return dc_td.ListSimulationApplicationsResponse.make_one(res)

    def list_simulation_job_batches(
        self,
        res: "bs_td.ListSimulationJobBatchesResponseTypeDef",
    ) -> "dc_td.ListSimulationJobBatchesResponse":
        return dc_td.ListSimulationJobBatchesResponse.make_one(res)

    def list_simulation_jobs(
        self,
        res: "bs_td.ListSimulationJobsResponseTypeDef",
    ) -> "dc_td.ListSimulationJobsResponse":
        return dc_td.ListSimulationJobsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_world_export_jobs(
        self,
        res: "bs_td.ListWorldExportJobsResponseTypeDef",
    ) -> "dc_td.ListWorldExportJobsResponse":
        return dc_td.ListWorldExportJobsResponse.make_one(res)

    def list_world_generation_jobs(
        self,
        res: "bs_td.ListWorldGenerationJobsResponseTypeDef",
    ) -> "dc_td.ListWorldGenerationJobsResponse":
        return dc_td.ListWorldGenerationJobsResponse.make_one(res)

    def list_world_templates(
        self,
        res: "bs_td.ListWorldTemplatesResponseTypeDef",
    ) -> "dc_td.ListWorldTemplatesResponse":
        return dc_td.ListWorldTemplatesResponse.make_one(res)

    def list_worlds(
        self,
        res: "bs_td.ListWorldsResponseTypeDef",
    ) -> "dc_td.ListWorldsResponse":
        return dc_td.ListWorldsResponse.make_one(res)

    def register_robot(
        self,
        res: "bs_td.RegisterRobotResponseTypeDef",
    ) -> "dc_td.RegisterRobotResponse":
        return dc_td.RegisterRobotResponse.make_one(res)

    def start_simulation_job_batch(
        self,
        res: "bs_td.StartSimulationJobBatchResponseTypeDef",
    ) -> "dc_td.StartSimulationJobBatchResponse":
        return dc_td.StartSimulationJobBatchResponse.make_one(res)

    def sync_deployment_job(
        self,
        res: "bs_td.SyncDeploymentJobResponseTypeDef",
    ) -> "dc_td.SyncDeploymentJobResponse":
        return dc_td.SyncDeploymentJobResponse.make_one(res)

    def update_robot_application(
        self,
        res: "bs_td.UpdateRobotApplicationResponseTypeDef",
    ) -> "dc_td.UpdateRobotApplicationResponse":
        return dc_td.UpdateRobotApplicationResponse.make_one(res)

    def update_simulation_application(
        self,
        res: "bs_td.UpdateSimulationApplicationResponseTypeDef",
    ) -> "dc_td.UpdateSimulationApplicationResponse":
        return dc_td.UpdateSimulationApplicationResponse.make_one(res)

    def update_world_template(
        self,
        res: "bs_td.UpdateWorldTemplateResponseTypeDef",
    ) -> "dc_td.UpdateWorldTemplateResponse":
        return dc_td.UpdateWorldTemplateResponse.make_one(res)


robomaker_caster = ROBOMAKERCaster()
