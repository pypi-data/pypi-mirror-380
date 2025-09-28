# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_marketplacecommerceanalytics import type_defs as bs_td


class MARKETPLACECOMMERCEANALYTICSCaster:

    def generate_data_set(
        self,
        res: "bs_td.GenerateDataSetResultTypeDef",
    ) -> "dc_td.GenerateDataSetResult":
        return dc_td.GenerateDataSetResult.make_one(res)

    def start_support_data_export(
        self,
        res: "bs_td.StartSupportDataExportResultTypeDef",
    ) -> "dc_td.StartSupportDataExportResult":
        return dc_td.StartSupportDataExportResult.make_one(res)


marketplacecommerceanalytics_caster = MARKETPLACECOMMERCEANALYTICSCaster()
