# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_swf import type_defs as bs_td


class SWFCaster:

    def count_closed_workflow_executions(
        self,
        res: "bs_td.WorkflowExecutionCountTypeDef",
    ) -> "dc_td.WorkflowExecutionCount":
        return dc_td.WorkflowExecutionCount.make_one(res)

    def count_open_workflow_executions(
        self,
        res: "bs_td.WorkflowExecutionCountTypeDef",
    ) -> "dc_td.WorkflowExecutionCount":
        return dc_td.WorkflowExecutionCount.make_one(res)

    def count_pending_activity_tasks(
        self,
        res: "bs_td.PendingTaskCountTypeDef",
    ) -> "dc_td.PendingTaskCount":
        return dc_td.PendingTaskCount.make_one(res)

    def count_pending_decision_tasks(
        self,
        res: "bs_td.PendingTaskCountTypeDef",
    ) -> "dc_td.PendingTaskCount":
        return dc_td.PendingTaskCount.make_one(res)

    def delete_activity_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_workflow_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deprecate_activity_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deprecate_domain(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deprecate_workflow_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_activity_type(
        self,
        res: "bs_td.ActivityTypeDetailTypeDef",
    ) -> "dc_td.ActivityTypeDetail":
        return dc_td.ActivityTypeDetail.make_one(res)

    def describe_domain(
        self,
        res: "bs_td.DomainDetailTypeDef",
    ) -> "dc_td.DomainDetail":
        return dc_td.DomainDetail.make_one(res)

    def describe_workflow_execution(
        self,
        res: "bs_td.WorkflowExecutionDetailTypeDef",
    ) -> "dc_td.WorkflowExecutionDetail":
        return dc_td.WorkflowExecutionDetail.make_one(res)

    def describe_workflow_type(
        self,
        res: "bs_td.WorkflowTypeDetailTypeDef",
    ) -> "dc_td.WorkflowTypeDetail":
        return dc_td.WorkflowTypeDetail.make_one(res)

    def get_workflow_execution_history(
        self,
        res: "bs_td.HistoryTypeDef",
    ) -> "dc_td.History":
        return dc_td.History.make_one(res)

    def list_activity_types(
        self,
        res: "bs_td.ActivityTypeInfosTypeDef",
    ) -> "dc_td.ActivityTypeInfos":
        return dc_td.ActivityTypeInfos.make_one(res)

    def list_closed_workflow_executions(
        self,
        res: "bs_td.WorkflowExecutionInfosTypeDef",
    ) -> "dc_td.WorkflowExecutionInfos":
        return dc_td.WorkflowExecutionInfos.make_one(res)

    def list_domains(
        self,
        res: "bs_td.DomainInfosTypeDef",
    ) -> "dc_td.DomainInfos":
        return dc_td.DomainInfos.make_one(res)

    def list_open_workflow_executions(
        self,
        res: "bs_td.WorkflowExecutionInfosTypeDef",
    ) -> "dc_td.WorkflowExecutionInfos":
        return dc_td.WorkflowExecutionInfos.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_workflow_types(
        self,
        res: "bs_td.WorkflowTypeInfosTypeDef",
    ) -> "dc_td.WorkflowTypeInfos":
        return dc_td.WorkflowTypeInfos.make_one(res)

    def poll_for_activity_task(
        self,
        res: "bs_td.ActivityTaskTypeDef",
    ) -> "dc_td.ActivityTask":
        return dc_td.ActivityTask.make_one(res)

    def poll_for_decision_task(
        self,
        res: "bs_td.DecisionTaskTypeDef",
    ) -> "dc_td.DecisionTask":
        return dc_td.DecisionTask.make_one(res)

    def record_activity_task_heartbeat(
        self,
        res: "bs_td.ActivityTaskStatusTypeDef",
    ) -> "dc_td.ActivityTaskStatus":
        return dc_td.ActivityTaskStatus.make_one(res)

    def register_activity_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def register_domain(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def register_workflow_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def request_cancel_workflow_execution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def respond_activity_task_canceled(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def respond_activity_task_completed(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def respond_activity_task_failed(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def respond_decision_task_completed(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def signal_workflow_execution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_workflow_execution(
        self,
        res: "bs_td.RunTypeDef",
    ) -> "dc_td.Run":
        return dc_td.Run.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def terminate_workflow_execution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def undeprecate_activity_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def undeprecate_domain(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def undeprecate_workflow_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


swf_caster = SWFCaster()
