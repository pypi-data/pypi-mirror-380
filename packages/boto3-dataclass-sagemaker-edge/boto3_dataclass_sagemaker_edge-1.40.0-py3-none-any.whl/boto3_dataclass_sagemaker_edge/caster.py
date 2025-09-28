# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_edge import type_defs as bs_td


class SAGEMAKER_EDGECaster:

    def get_deployments(
        self,
        res: "bs_td.GetDeploymentsResultTypeDef",
    ) -> "dc_td.GetDeploymentsResult":
        return dc_td.GetDeploymentsResult.make_one(res)

    def get_device_registration(
        self,
        res: "bs_td.GetDeviceRegistrationResultTypeDef",
    ) -> "dc_td.GetDeviceRegistrationResult":
        return dc_td.GetDeviceRegistrationResult.make_one(res)

    def send_heartbeat(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


sagemaker_edge_caster = SAGEMAKER_EDGECaster()
