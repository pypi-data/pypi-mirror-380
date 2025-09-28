# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_metrics import type_defs as bs_td


class SAGEMAKER_METRICSCaster:

    def batch_get_metrics(
        self,
        res: "bs_td.BatchGetMetricsResponseTypeDef",
    ) -> "dc_td.BatchGetMetricsResponse":
        return dc_td.BatchGetMetricsResponse.make_one(res)

    def batch_put_metrics(
        self,
        res: "bs_td.BatchPutMetricsResponseTypeDef",
    ) -> "dc_td.BatchPutMetricsResponse":
        return dc_td.BatchPutMetricsResponse.make_one(res)


sagemaker_metrics_caster = SAGEMAKER_METRICSCaster()
