# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_scheduler import type_defs as bs_td


class SCHEDULERCaster:

    def create_schedule(
        self,
        res: "bs_td.CreateScheduleOutputTypeDef",
    ) -> "dc_td.CreateScheduleOutput":
        return dc_td.CreateScheduleOutput.make_one(res)

    def create_schedule_group(
        self,
        res: "bs_td.CreateScheduleGroupOutputTypeDef",
    ) -> "dc_td.CreateScheduleGroupOutput":
        return dc_td.CreateScheduleGroupOutput.make_one(res)

    def get_schedule(
        self,
        res: "bs_td.GetScheduleOutputTypeDef",
    ) -> "dc_td.GetScheduleOutput":
        return dc_td.GetScheduleOutput.make_one(res)

    def get_schedule_group(
        self,
        res: "bs_td.GetScheduleGroupOutputTypeDef",
    ) -> "dc_td.GetScheduleGroupOutput":
        return dc_td.GetScheduleGroupOutput.make_one(res)

    def list_schedule_groups(
        self,
        res: "bs_td.ListScheduleGroupsOutputTypeDef",
    ) -> "dc_td.ListScheduleGroupsOutput":
        return dc_td.ListScheduleGroupsOutput.make_one(res)

    def list_schedules(
        self,
        res: "bs_td.ListSchedulesOutputTypeDef",
    ) -> "dc_td.ListSchedulesOutput":
        return dc_td.ListSchedulesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def update_schedule(
        self,
        res: "bs_td.UpdateScheduleOutputTypeDef",
    ) -> "dc_td.UpdateScheduleOutput":
        return dc_td.UpdateScheduleOutput.make_one(res)


scheduler_caster = SCHEDULERCaster()
