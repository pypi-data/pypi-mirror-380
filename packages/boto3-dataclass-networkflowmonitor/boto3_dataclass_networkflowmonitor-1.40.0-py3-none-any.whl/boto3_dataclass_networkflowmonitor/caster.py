# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_networkflowmonitor import type_defs as bs_td


class NETWORKFLOWMONITORCaster:

    def create_monitor(
        self,
        res: "bs_td.CreateMonitorOutputTypeDef",
    ) -> "dc_td.CreateMonitorOutput":
        return dc_td.CreateMonitorOutput.make_one(res)

    def create_scope(
        self,
        res: "bs_td.CreateScopeOutputTypeDef",
    ) -> "dc_td.CreateScopeOutput":
        return dc_td.CreateScopeOutput.make_one(res)

    def get_monitor(
        self,
        res: "bs_td.GetMonitorOutputTypeDef",
    ) -> "dc_td.GetMonitorOutput":
        return dc_td.GetMonitorOutput.make_one(res)

    def get_query_results_monitor_top_contributors(
        self,
        res: "bs_td.GetQueryResultsMonitorTopContributorsOutputTypeDef",
    ) -> "dc_td.GetQueryResultsMonitorTopContributorsOutput":
        return dc_td.GetQueryResultsMonitorTopContributorsOutput.make_one(res)

    def get_query_results_workload_insights_top_contributors(
        self,
        res: "bs_td.GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef",
    ) -> "dc_td.GetQueryResultsWorkloadInsightsTopContributorsOutput":
        return dc_td.GetQueryResultsWorkloadInsightsTopContributorsOutput.make_one(res)

    def get_query_results_workload_insights_top_contributors_data(
        self,
        res: "bs_td.GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef",
    ) -> "dc_td.GetQueryResultsWorkloadInsightsTopContributorsDataOutput":
        return dc_td.GetQueryResultsWorkloadInsightsTopContributorsDataOutput.make_one(
            res
        )

    def get_query_status_monitor_top_contributors(
        self,
        res: "bs_td.GetQueryStatusMonitorTopContributorsOutputTypeDef",
    ) -> "dc_td.GetQueryStatusMonitorTopContributorsOutput":
        return dc_td.GetQueryStatusMonitorTopContributorsOutput.make_one(res)

    def get_query_status_workload_insights_top_contributors(
        self,
        res: "bs_td.GetQueryStatusWorkloadInsightsTopContributorsOutputTypeDef",
    ) -> "dc_td.GetQueryStatusWorkloadInsightsTopContributorsOutput":
        return dc_td.GetQueryStatusWorkloadInsightsTopContributorsOutput.make_one(res)

    def get_query_status_workload_insights_top_contributors_data(
        self,
        res: "bs_td.GetQueryStatusWorkloadInsightsTopContributorsDataOutputTypeDef",
    ) -> "dc_td.GetQueryStatusWorkloadInsightsTopContributorsDataOutput":
        return dc_td.GetQueryStatusWorkloadInsightsTopContributorsDataOutput.make_one(
            res
        )

    def get_scope(
        self,
        res: "bs_td.GetScopeOutputTypeDef",
    ) -> "dc_td.GetScopeOutput":
        return dc_td.GetScopeOutput.make_one(res)

    def list_monitors(
        self,
        res: "bs_td.ListMonitorsOutputTypeDef",
    ) -> "dc_td.ListMonitorsOutput":
        return dc_td.ListMonitorsOutput.make_one(res)

    def list_scopes(
        self,
        res: "bs_td.ListScopesOutputTypeDef",
    ) -> "dc_td.ListScopesOutput":
        return dc_td.ListScopesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def start_query_monitor_top_contributors(
        self,
        res: "bs_td.StartQueryMonitorTopContributorsOutputTypeDef",
    ) -> "dc_td.StartQueryMonitorTopContributorsOutput":
        return dc_td.StartQueryMonitorTopContributorsOutput.make_one(res)

    def start_query_workload_insights_top_contributors(
        self,
        res: "bs_td.StartQueryWorkloadInsightsTopContributorsOutputTypeDef",
    ) -> "dc_td.StartQueryWorkloadInsightsTopContributorsOutput":
        return dc_td.StartQueryWorkloadInsightsTopContributorsOutput.make_one(res)

    def start_query_workload_insights_top_contributors_data(
        self,
        res: "bs_td.StartQueryWorkloadInsightsTopContributorsDataOutputTypeDef",
    ) -> "dc_td.StartQueryWorkloadInsightsTopContributorsDataOutput":
        return dc_td.StartQueryWorkloadInsightsTopContributorsDataOutput.make_one(res)

    def update_monitor(
        self,
        res: "bs_td.UpdateMonitorOutputTypeDef",
    ) -> "dc_td.UpdateMonitorOutput":
        return dc_td.UpdateMonitorOutput.make_one(res)

    def update_scope(
        self,
        res: "bs_td.UpdateScopeOutputTypeDef",
    ) -> "dc_td.UpdateScopeOutput":
        return dc_td.UpdateScopeOutput.make_one(res)


networkflowmonitor_caster = NETWORKFLOWMONITORCaster()
