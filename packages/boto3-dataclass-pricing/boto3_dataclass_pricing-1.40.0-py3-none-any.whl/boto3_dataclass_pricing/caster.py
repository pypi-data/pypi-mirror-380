# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pricing import type_defs as bs_td


class PRICINGCaster:

    def describe_services(
        self,
        res: "bs_td.DescribeServicesResponseTypeDef",
    ) -> "dc_td.DescribeServicesResponse":
        return dc_td.DescribeServicesResponse.make_one(res)

    def get_attribute_values(
        self,
        res: "bs_td.GetAttributeValuesResponseTypeDef",
    ) -> "dc_td.GetAttributeValuesResponse":
        return dc_td.GetAttributeValuesResponse.make_one(res)

    def get_price_list_file_url(
        self,
        res: "bs_td.GetPriceListFileUrlResponseTypeDef",
    ) -> "dc_td.GetPriceListFileUrlResponse":
        return dc_td.GetPriceListFileUrlResponse.make_one(res)

    def get_products(
        self,
        res: "bs_td.GetProductsResponseTypeDef",
    ) -> "dc_td.GetProductsResponse":
        return dc_td.GetProductsResponse.make_one(res)

    def list_price_lists(
        self,
        res: "bs_td.ListPriceListsResponseTypeDef",
    ) -> "dc_td.ListPriceListsResponse":
        return dc_td.ListPriceListsResponse.make_one(res)


pricing_caster = PRICINGCaster()
