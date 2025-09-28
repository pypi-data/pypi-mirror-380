# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_networkmonitor import type_defs as bs_td


class NETWORKMONITORCaster:

    def create_monitor(
        self,
        res: "bs_td.CreateMonitorOutputTypeDef",
    ) -> "dc_td.CreateMonitorOutput":
        return dc_td.CreateMonitorOutput.make_one(res)

    def create_probe(
        self,
        res: "bs_td.CreateProbeOutputTypeDef",
    ) -> "dc_td.CreateProbeOutput":
        return dc_td.CreateProbeOutput.make_one(res)

    def get_monitor(
        self,
        res: "bs_td.GetMonitorOutputTypeDef",
    ) -> "dc_td.GetMonitorOutput":
        return dc_td.GetMonitorOutput.make_one(res)

    def get_probe(
        self,
        res: "bs_td.GetProbeOutputTypeDef",
    ) -> "dc_td.GetProbeOutput":
        return dc_td.GetProbeOutput.make_one(res)

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

    def update_monitor(
        self,
        res: "bs_td.UpdateMonitorOutputTypeDef",
    ) -> "dc_td.UpdateMonitorOutput":
        return dc_td.UpdateMonitorOutput.make_one(res)

    def update_probe(
        self,
        res: "bs_td.UpdateProbeOutputTypeDef",
    ) -> "dc_td.UpdateProbeOutput":
        return dc_td.UpdateProbeOutput.make_one(res)


networkmonitor_caster = NETWORKMONITORCaster()
