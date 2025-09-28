# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_stepfunctions import type_defs as bs_td


class STEPFUNCTIONSCaster:

    def create_activity(
        self,
        res: "bs_td.CreateActivityOutputTypeDef",
    ) -> "dc_td.CreateActivityOutput":
        return dc_td.CreateActivityOutput.make_one(res)

    def create_state_machine(
        self,
        res: "bs_td.CreateStateMachineOutputTypeDef",
    ) -> "dc_td.CreateStateMachineOutput":
        return dc_td.CreateStateMachineOutput.make_one(res)

    def create_state_machine_alias(
        self,
        res: "bs_td.CreateStateMachineAliasOutputTypeDef",
    ) -> "dc_td.CreateStateMachineAliasOutput":
        return dc_td.CreateStateMachineAliasOutput.make_one(res)

    def describe_activity(
        self,
        res: "bs_td.DescribeActivityOutputTypeDef",
    ) -> "dc_td.DescribeActivityOutput":
        return dc_td.DescribeActivityOutput.make_one(res)

    def describe_execution(
        self,
        res: "bs_td.DescribeExecutionOutputTypeDef",
    ) -> "dc_td.DescribeExecutionOutput":
        return dc_td.DescribeExecutionOutput.make_one(res)

    def describe_map_run(
        self,
        res: "bs_td.DescribeMapRunOutputTypeDef",
    ) -> "dc_td.DescribeMapRunOutput":
        return dc_td.DescribeMapRunOutput.make_one(res)

    def describe_state_machine(
        self,
        res: "bs_td.DescribeStateMachineOutputTypeDef",
    ) -> "dc_td.DescribeStateMachineOutput":
        return dc_td.DescribeStateMachineOutput.make_one(res)

    def describe_state_machine_alias(
        self,
        res: "bs_td.DescribeStateMachineAliasOutputTypeDef",
    ) -> "dc_td.DescribeStateMachineAliasOutput":
        return dc_td.DescribeStateMachineAliasOutput.make_one(res)

    def describe_state_machine_for_execution(
        self,
        res: "bs_td.DescribeStateMachineForExecutionOutputTypeDef",
    ) -> "dc_td.DescribeStateMachineForExecutionOutput":
        return dc_td.DescribeStateMachineForExecutionOutput.make_one(res)

    def get_activity_task(
        self,
        res: "bs_td.GetActivityTaskOutputTypeDef",
    ) -> "dc_td.GetActivityTaskOutput":
        return dc_td.GetActivityTaskOutput.make_one(res)

    def get_execution_history(
        self,
        res: "bs_td.GetExecutionHistoryOutputTypeDef",
    ) -> "dc_td.GetExecutionHistoryOutput":
        return dc_td.GetExecutionHistoryOutput.make_one(res)

    def list_activities(
        self,
        res: "bs_td.ListActivitiesOutputTypeDef",
    ) -> "dc_td.ListActivitiesOutput":
        return dc_td.ListActivitiesOutput.make_one(res)

    def list_executions(
        self,
        res: "bs_td.ListExecutionsOutputTypeDef",
    ) -> "dc_td.ListExecutionsOutput":
        return dc_td.ListExecutionsOutput.make_one(res)

    def list_map_runs(
        self,
        res: "bs_td.ListMapRunsOutputTypeDef",
    ) -> "dc_td.ListMapRunsOutput":
        return dc_td.ListMapRunsOutput.make_one(res)

    def list_state_machine_aliases(
        self,
        res: "bs_td.ListStateMachineAliasesOutputTypeDef",
    ) -> "dc_td.ListStateMachineAliasesOutput":
        return dc_td.ListStateMachineAliasesOutput.make_one(res)

    def list_state_machine_versions(
        self,
        res: "bs_td.ListStateMachineVersionsOutputTypeDef",
    ) -> "dc_td.ListStateMachineVersionsOutput":
        return dc_td.ListStateMachineVersionsOutput.make_one(res)

    def list_state_machines(
        self,
        res: "bs_td.ListStateMachinesOutputTypeDef",
    ) -> "dc_td.ListStateMachinesOutput":
        return dc_td.ListStateMachinesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def publish_state_machine_version(
        self,
        res: "bs_td.PublishStateMachineVersionOutputTypeDef",
    ) -> "dc_td.PublishStateMachineVersionOutput":
        return dc_td.PublishStateMachineVersionOutput.make_one(res)

    def redrive_execution(
        self,
        res: "bs_td.RedriveExecutionOutputTypeDef",
    ) -> "dc_td.RedriveExecutionOutput":
        return dc_td.RedriveExecutionOutput.make_one(res)

    def start_execution(
        self,
        res: "bs_td.StartExecutionOutputTypeDef",
    ) -> "dc_td.StartExecutionOutput":
        return dc_td.StartExecutionOutput.make_one(res)

    def start_sync_execution(
        self,
        res: "bs_td.StartSyncExecutionOutputTypeDef",
    ) -> "dc_td.StartSyncExecutionOutput":
        return dc_td.StartSyncExecutionOutput.make_one(res)

    def stop_execution(
        self,
        res: "bs_td.StopExecutionOutputTypeDef",
    ) -> "dc_td.StopExecutionOutput":
        return dc_td.StopExecutionOutput.make_one(res)

    def test_state(
        self,
        res: "bs_td.TestStateOutputTypeDef",
    ) -> "dc_td.TestStateOutput":
        return dc_td.TestStateOutput.make_one(res)

    def update_state_machine(
        self,
        res: "bs_td.UpdateStateMachineOutputTypeDef",
    ) -> "dc_td.UpdateStateMachineOutput":
        return dc_td.UpdateStateMachineOutput.make_one(res)

    def update_state_machine_alias(
        self,
        res: "bs_td.UpdateStateMachineAliasOutputTypeDef",
    ) -> "dc_td.UpdateStateMachineAliasOutput":
        return dc_td.UpdateStateMachineAliasOutput.make_one(res)

    def validate_state_machine_definition(
        self,
        res: "bs_td.ValidateStateMachineDefinitionOutputTypeDef",
    ) -> "dc_td.ValidateStateMachineDefinitionOutput":
        return dc_td.ValidateStateMachineDefinitionOutput.make_one(res)


stepfunctions_caster = STEPFUNCTIONSCaster()
