# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_importexport import type_defs as bs_td


class IMPORTEXPORTCaster:

    def cancel_job(
        self,
        res: "bs_td.CancelJobOutputTypeDef",
    ) -> "dc_td.CancelJobOutput":
        return dc_td.CancelJobOutput.make_one(res)

    def create_job(
        self,
        res: "bs_td.CreateJobOutputTypeDef",
    ) -> "dc_td.CreateJobOutput":
        return dc_td.CreateJobOutput.make_one(res)

    def get_shipping_label(
        self,
        res: "bs_td.GetShippingLabelOutputTypeDef",
    ) -> "dc_td.GetShippingLabelOutput":
        return dc_td.GetShippingLabelOutput.make_one(res)

    def get_status(
        self,
        res: "bs_td.GetStatusOutputTypeDef",
    ) -> "dc_td.GetStatusOutput":
        return dc_td.GetStatusOutput.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsOutputTypeDef",
    ) -> "dc_td.ListJobsOutput":
        return dc_td.ListJobsOutput.make_one(res)

    def update_job(
        self,
        res: "bs_td.UpdateJobOutputTypeDef",
    ) -> "dc_td.UpdateJobOutput":
        return dc_td.UpdateJobOutput.make_one(res)


importexport_caster = IMPORTEXPORTCaster()
