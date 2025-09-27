# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_internetmonitor import type_defs as bs_td


class INTERNETMONITORCaster:

    def create_monitor(
        self,
        res: "bs_td.CreateMonitorOutputTypeDef",
    ) -> "dc_td.CreateMonitorOutput":
        return dc_td.CreateMonitorOutput.make_one(res)

    def get_health_event(
        self,
        res: "bs_td.GetHealthEventOutputTypeDef",
    ) -> "dc_td.GetHealthEventOutput":
        return dc_td.GetHealthEventOutput.make_one(res)

    def get_internet_event(
        self,
        res: "bs_td.GetInternetEventOutputTypeDef",
    ) -> "dc_td.GetInternetEventOutput":
        return dc_td.GetInternetEventOutput.make_one(res)

    def get_monitor(
        self,
        res: "bs_td.GetMonitorOutputTypeDef",
    ) -> "dc_td.GetMonitorOutput":
        return dc_td.GetMonitorOutput.make_one(res)

    def get_query_results(
        self,
        res: "bs_td.GetQueryResultsOutputTypeDef",
    ) -> "dc_td.GetQueryResultsOutput":
        return dc_td.GetQueryResultsOutput.make_one(res)

    def get_query_status(
        self,
        res: "bs_td.GetQueryStatusOutputTypeDef",
    ) -> "dc_td.GetQueryStatusOutput":
        return dc_td.GetQueryStatusOutput.make_one(res)

    def list_health_events(
        self,
        res: "bs_td.ListHealthEventsOutputTypeDef",
    ) -> "dc_td.ListHealthEventsOutput":
        return dc_td.ListHealthEventsOutput.make_one(res)

    def list_internet_events(
        self,
        res: "bs_td.ListInternetEventsOutputTypeDef",
    ) -> "dc_td.ListInternetEventsOutput":
        return dc_td.ListInternetEventsOutput.make_one(res)

    def list_monitors(
        self,
        res: "bs_td.ListMonitorsOutputTypeDef",
    ) -> "dc_td.ListMonitorsOutput":
        return dc_td.ListMonitorsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def start_query(
        self,
        res: "bs_td.StartQueryOutputTypeDef",
    ) -> "dc_td.StartQueryOutput":
        return dc_td.StartQueryOutput.make_one(res)

    def update_monitor(
        self,
        res: "bs_td.UpdateMonitorOutputTypeDef",
    ) -> "dc_td.UpdateMonitorOutput":
        return dc_td.UpdateMonitorOutput.make_one(res)


internetmonitor_caster = INTERNETMONITORCaster()
