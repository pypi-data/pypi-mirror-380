# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_runtime import type_defs as bs_td


class SAGEMAKER_RUNTIMECaster:

    def invoke_endpoint(
        self,
        res: "bs_td.InvokeEndpointOutputTypeDef",
    ) -> "dc_td.InvokeEndpointOutput":
        return dc_td.InvokeEndpointOutput.make_one(res)

    def invoke_endpoint_async(
        self,
        res: "bs_td.InvokeEndpointAsyncOutputTypeDef",
    ) -> "dc_td.InvokeEndpointAsyncOutput":
        return dc_td.InvokeEndpointAsyncOutput.make_one(res)

    def invoke_endpoint_with_response_stream(
        self,
        res: "bs_td.InvokeEndpointWithResponseStreamOutputTypeDef",
    ) -> "dc_td.InvokeEndpointWithResponseStreamOutput":
        return dc_td.InvokeEndpointWithResponseStreamOutput.make_one(res)


sagemaker_runtime_caster = SAGEMAKER_RUNTIMECaster()
