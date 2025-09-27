# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_launch_wizard import type_defs as bs_td


class LAUNCH_WIZARDCaster:

    def create_deployment(
        self,
        res: "bs_td.CreateDeploymentOutputTypeDef",
    ) -> "dc_td.CreateDeploymentOutput":
        return dc_td.CreateDeploymentOutput.make_one(res)

    def delete_deployment(
        self,
        res: "bs_td.DeleteDeploymentOutputTypeDef",
    ) -> "dc_td.DeleteDeploymentOutput":
        return dc_td.DeleteDeploymentOutput.make_one(res)

    def get_deployment(
        self,
        res: "bs_td.GetDeploymentOutputTypeDef",
    ) -> "dc_td.GetDeploymentOutput":
        return dc_td.GetDeploymentOutput.make_one(res)

    def get_workload(
        self,
        res: "bs_td.GetWorkloadOutputTypeDef",
    ) -> "dc_td.GetWorkloadOutput":
        return dc_td.GetWorkloadOutput.make_one(res)

    def get_workload_deployment_pattern(
        self,
        res: "bs_td.GetWorkloadDeploymentPatternOutputTypeDef",
    ) -> "dc_td.GetWorkloadDeploymentPatternOutput":
        return dc_td.GetWorkloadDeploymentPatternOutput.make_one(res)

    def list_deployment_events(
        self,
        res: "bs_td.ListDeploymentEventsOutputTypeDef",
    ) -> "dc_td.ListDeploymentEventsOutput":
        return dc_td.ListDeploymentEventsOutput.make_one(res)

    def list_deployments(
        self,
        res: "bs_td.ListDeploymentsOutputTypeDef",
    ) -> "dc_td.ListDeploymentsOutput":
        return dc_td.ListDeploymentsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_workload_deployment_patterns(
        self,
        res: "bs_td.ListWorkloadDeploymentPatternsOutputTypeDef",
    ) -> "dc_td.ListWorkloadDeploymentPatternsOutput":
        return dc_td.ListWorkloadDeploymentPatternsOutput.make_one(res)

    def list_workloads(
        self,
        res: "bs_td.ListWorkloadsOutputTypeDef",
    ) -> "dc_td.ListWorkloadsOutput":
        return dc_td.ListWorkloadsOutput.make_one(res)


launch_wizard_caster = LAUNCH_WIZARDCaster()
