# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_featurestore_runtime import type_defs as bs_td


class SAGEMAKER_FEATURESTORE_RUNTIMECaster:

    def batch_get_record(
        self,
        res: "bs_td.BatchGetRecordResponseTypeDef",
    ) -> "dc_td.BatchGetRecordResponse":
        return dc_td.BatchGetRecordResponse.make_one(res)

    def delete_record(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_record(
        self,
        res: "bs_td.GetRecordResponseTypeDef",
    ) -> "dc_td.GetRecordResponse":
        return dc_td.GetRecordResponse.make_one(res)

    def put_record(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


sagemaker_featurestore_runtime_caster = SAGEMAKER_FEATURESTORE_RUNTIMECaster()
