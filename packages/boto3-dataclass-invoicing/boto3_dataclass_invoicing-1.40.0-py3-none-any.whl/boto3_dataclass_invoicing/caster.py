# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_invoicing import type_defs as bs_td


class INVOICINGCaster:

    def batch_get_invoice_profile(
        self,
        res: "bs_td.BatchGetInvoiceProfileResponseTypeDef",
    ) -> "dc_td.BatchGetInvoiceProfileResponse":
        return dc_td.BatchGetInvoiceProfileResponse.make_one(res)

    def create_invoice_unit(
        self,
        res: "bs_td.CreateInvoiceUnitResponseTypeDef",
    ) -> "dc_td.CreateInvoiceUnitResponse":
        return dc_td.CreateInvoiceUnitResponse.make_one(res)

    def delete_invoice_unit(
        self,
        res: "bs_td.DeleteInvoiceUnitResponseTypeDef",
    ) -> "dc_td.DeleteInvoiceUnitResponse":
        return dc_td.DeleteInvoiceUnitResponse.make_one(res)

    def get_invoice_unit(
        self,
        res: "bs_td.GetInvoiceUnitResponseTypeDef",
    ) -> "dc_td.GetInvoiceUnitResponse":
        return dc_td.GetInvoiceUnitResponse.make_one(res)

    def list_invoice_summaries(
        self,
        res: "bs_td.ListInvoiceSummariesResponseTypeDef",
    ) -> "dc_td.ListInvoiceSummariesResponse":
        return dc_td.ListInvoiceSummariesResponse.make_one(res)

    def list_invoice_units(
        self,
        res: "bs_td.ListInvoiceUnitsResponseTypeDef",
    ) -> "dc_td.ListInvoiceUnitsResponse":
        return dc_td.ListInvoiceUnitsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_invoice_unit(
        self,
        res: "bs_td.UpdateInvoiceUnitResponseTypeDef",
    ) -> "dc_td.UpdateInvoiceUnitResponse":
        return dc_td.UpdateInvoiceUnitResponse.make_one(res)


invoicing_caster = INVOICINGCaster()
