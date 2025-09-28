# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediastore_data import type_defs as bs_td


class MEDIASTORE_DATACaster:

    def describe_object(
        self,
        res: "bs_td.DescribeObjectResponseTypeDef",
    ) -> "dc_td.DescribeObjectResponse":
        return dc_td.DescribeObjectResponse.make_one(res)

    def get_object(
        self,
        res: "bs_td.GetObjectResponseTypeDef",
    ) -> "dc_td.GetObjectResponse":
        return dc_td.GetObjectResponse.make_one(res)

    def list_items(
        self,
        res: "bs_td.ListItemsResponseTypeDef",
    ) -> "dc_td.ListItemsResponse":
        return dc_td.ListItemsResponse.make_one(res)

    def put_object(
        self,
        res: "bs_td.PutObjectResponseTypeDef",
    ) -> "dc_td.PutObjectResponse":
        return dc_td.PutObjectResponse.make_one(res)


mediastore_data_caster = MEDIASTORE_DATACaster()
