# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_migrationhuborchestrator import type_defs as bs_td


class MIGRATIONHUBORCHESTRATORCaster:

    def create_template(
        self,
        res: "bs_td.CreateTemplateResponseTypeDef",
    ) -> "dc_td.CreateTemplateResponse":
        return dc_td.CreateTemplateResponse.make_one(res)

    def create_workflow(
        self,
        res: "bs_td.CreateMigrationWorkflowResponseTypeDef",
    ) -> "dc_td.CreateMigrationWorkflowResponse":
        return dc_td.CreateMigrationWorkflowResponse.make_one(res)

    def create_workflow_step(
        self,
        res: "bs_td.CreateWorkflowStepResponseTypeDef",
    ) -> "dc_td.CreateWorkflowStepResponse":
        return dc_td.CreateWorkflowStepResponse.make_one(res)

    def create_workflow_step_group(
        self,
        res: "bs_td.CreateWorkflowStepGroupResponseTypeDef",
    ) -> "dc_td.CreateWorkflowStepGroupResponse":
        return dc_td.CreateWorkflowStepGroupResponse.make_one(res)

    def delete_workflow(
        self,
        res: "bs_td.DeleteMigrationWorkflowResponseTypeDef",
    ) -> "dc_td.DeleteMigrationWorkflowResponse":
        return dc_td.DeleteMigrationWorkflowResponse.make_one(res)

    def get_template(
        self,
        res: "bs_td.GetMigrationWorkflowTemplateResponseTypeDef",
    ) -> "dc_td.GetMigrationWorkflowTemplateResponse":
        return dc_td.GetMigrationWorkflowTemplateResponse.make_one(res)

    def get_template_step(
        self,
        res: "bs_td.GetTemplateStepResponseTypeDef",
    ) -> "dc_td.GetTemplateStepResponse":
        return dc_td.GetTemplateStepResponse.make_one(res)

    def get_template_step_group(
        self,
        res: "bs_td.GetTemplateStepGroupResponseTypeDef",
    ) -> "dc_td.GetTemplateStepGroupResponse":
        return dc_td.GetTemplateStepGroupResponse.make_one(res)

    def get_workflow(
        self,
        res: "bs_td.GetMigrationWorkflowResponseTypeDef",
    ) -> "dc_td.GetMigrationWorkflowResponse":
        return dc_td.GetMigrationWorkflowResponse.make_one(res)

    def get_workflow_step(
        self,
        res: "bs_td.GetWorkflowStepResponseTypeDef",
    ) -> "dc_td.GetWorkflowStepResponse":
        return dc_td.GetWorkflowStepResponse.make_one(res)

    def get_workflow_step_group(
        self,
        res: "bs_td.GetWorkflowStepGroupResponseTypeDef",
    ) -> "dc_td.GetWorkflowStepGroupResponse":
        return dc_td.GetWorkflowStepGroupResponse.make_one(res)

    def list_plugins(
        self,
        res: "bs_td.ListPluginsResponseTypeDef",
    ) -> "dc_td.ListPluginsResponse":
        return dc_td.ListPluginsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_template_step_groups(
        self,
        res: "bs_td.ListTemplateStepGroupsResponseTypeDef",
    ) -> "dc_td.ListTemplateStepGroupsResponse":
        return dc_td.ListTemplateStepGroupsResponse.make_one(res)

    def list_template_steps(
        self,
        res: "bs_td.ListTemplateStepsResponseTypeDef",
    ) -> "dc_td.ListTemplateStepsResponse":
        return dc_td.ListTemplateStepsResponse.make_one(res)

    def list_templates(
        self,
        res: "bs_td.ListMigrationWorkflowTemplatesResponseTypeDef",
    ) -> "dc_td.ListMigrationWorkflowTemplatesResponse":
        return dc_td.ListMigrationWorkflowTemplatesResponse.make_one(res)

    def list_workflow_step_groups(
        self,
        res: "bs_td.ListWorkflowStepGroupsResponseTypeDef",
    ) -> "dc_td.ListWorkflowStepGroupsResponse":
        return dc_td.ListWorkflowStepGroupsResponse.make_one(res)

    def list_workflow_steps(
        self,
        res: "bs_td.ListWorkflowStepsResponseTypeDef",
    ) -> "dc_td.ListWorkflowStepsResponse":
        return dc_td.ListWorkflowStepsResponse.make_one(res)

    def list_workflows(
        self,
        res: "bs_td.ListMigrationWorkflowsResponseTypeDef",
    ) -> "dc_td.ListMigrationWorkflowsResponse":
        return dc_td.ListMigrationWorkflowsResponse.make_one(res)

    def retry_workflow_step(
        self,
        res: "bs_td.RetryWorkflowStepResponseTypeDef",
    ) -> "dc_td.RetryWorkflowStepResponse":
        return dc_td.RetryWorkflowStepResponse.make_one(res)

    def start_workflow(
        self,
        res: "bs_td.StartMigrationWorkflowResponseTypeDef",
    ) -> "dc_td.StartMigrationWorkflowResponse":
        return dc_td.StartMigrationWorkflowResponse.make_one(res)

    def stop_workflow(
        self,
        res: "bs_td.StopMigrationWorkflowResponseTypeDef",
    ) -> "dc_td.StopMigrationWorkflowResponse":
        return dc_td.StopMigrationWorkflowResponse.make_one(res)

    def update_template(
        self,
        res: "bs_td.UpdateTemplateResponseTypeDef",
    ) -> "dc_td.UpdateTemplateResponse":
        return dc_td.UpdateTemplateResponse.make_one(res)

    def update_workflow(
        self,
        res: "bs_td.UpdateMigrationWorkflowResponseTypeDef",
    ) -> "dc_td.UpdateMigrationWorkflowResponse":
        return dc_td.UpdateMigrationWorkflowResponse.make_one(res)

    def update_workflow_step(
        self,
        res: "bs_td.UpdateWorkflowStepResponseTypeDef",
    ) -> "dc_td.UpdateWorkflowStepResponse":
        return dc_td.UpdateWorkflowStepResponse.make_one(res)

    def update_workflow_step_group(
        self,
        res: "bs_td.UpdateWorkflowStepGroupResponseTypeDef",
    ) -> "dc_td.UpdateWorkflowStepGroupResponse":
        return dc_td.UpdateWorkflowStepGroupResponse.make_one(res)


migrationhuborchestrator_caster = MIGRATIONHUBORCHESTRATORCaster()
