# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_inspector_scan import type_defs as bs_td


class INSPECTOR_SCANCaster:

    def scan_sbom(
        self,
        res: "bs_td.ScanSbomResponseTypeDef",
    ) -> "dc_td.ScanSbomResponse":
        return dc_td.ScanSbomResponse.make_one(res)


inspector_scan_caster = INSPECTOR_SCANCaster()
