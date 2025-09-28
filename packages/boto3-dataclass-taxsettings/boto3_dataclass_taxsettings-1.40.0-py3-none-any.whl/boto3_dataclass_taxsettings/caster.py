# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_taxsettings import type_defs as bs_td


class TAXSETTINGSCaster:

    def batch_delete_tax_registration(
        self,
        res: "bs_td.BatchDeleteTaxRegistrationResponseTypeDef",
    ) -> "dc_td.BatchDeleteTaxRegistrationResponse":
        return dc_td.BatchDeleteTaxRegistrationResponse.make_one(res)

    def batch_get_tax_exemptions(
        self,
        res: "bs_td.BatchGetTaxExemptionsResponseTypeDef",
    ) -> "dc_td.BatchGetTaxExemptionsResponse":
        return dc_td.BatchGetTaxExemptionsResponse.make_one(res)

    def batch_put_tax_registration(
        self,
        res: "bs_td.BatchPutTaxRegistrationResponseTypeDef",
    ) -> "dc_td.BatchPutTaxRegistrationResponse":
        return dc_td.BatchPutTaxRegistrationResponse.make_one(res)

    def get_tax_exemption_types(
        self,
        res: "bs_td.GetTaxExemptionTypesResponseTypeDef",
    ) -> "dc_td.GetTaxExemptionTypesResponse":
        return dc_td.GetTaxExemptionTypesResponse.make_one(res)

    def get_tax_inheritance(
        self,
        res: "bs_td.GetTaxInheritanceResponseTypeDef",
    ) -> "dc_td.GetTaxInheritanceResponse":
        return dc_td.GetTaxInheritanceResponse.make_one(res)

    def get_tax_registration(
        self,
        res: "bs_td.GetTaxRegistrationResponseTypeDef",
    ) -> "dc_td.GetTaxRegistrationResponse":
        return dc_td.GetTaxRegistrationResponse.make_one(res)

    def get_tax_registration_document(
        self,
        res: "bs_td.GetTaxRegistrationDocumentResponseTypeDef",
    ) -> "dc_td.GetTaxRegistrationDocumentResponse":
        return dc_td.GetTaxRegistrationDocumentResponse.make_one(res)

    def list_supplemental_tax_registrations(
        self,
        res: "bs_td.ListSupplementalTaxRegistrationsResponseTypeDef",
    ) -> "dc_td.ListSupplementalTaxRegistrationsResponse":
        return dc_td.ListSupplementalTaxRegistrationsResponse.make_one(res)

    def list_tax_exemptions(
        self,
        res: "bs_td.ListTaxExemptionsResponseTypeDef",
    ) -> "dc_td.ListTaxExemptionsResponse":
        return dc_td.ListTaxExemptionsResponse.make_one(res)

    def list_tax_registrations(
        self,
        res: "bs_td.ListTaxRegistrationsResponseTypeDef",
    ) -> "dc_td.ListTaxRegistrationsResponse":
        return dc_td.ListTaxRegistrationsResponse.make_one(res)

    def put_supplemental_tax_registration(
        self,
        res: "bs_td.PutSupplementalTaxRegistrationResponseTypeDef",
    ) -> "dc_td.PutSupplementalTaxRegistrationResponse":
        return dc_td.PutSupplementalTaxRegistrationResponse.make_one(res)

    def put_tax_exemption(
        self,
        res: "bs_td.PutTaxExemptionResponseTypeDef",
    ) -> "dc_td.PutTaxExemptionResponse":
        return dc_td.PutTaxExemptionResponse.make_one(res)

    def put_tax_registration(
        self,
        res: "bs_td.PutTaxRegistrationResponseTypeDef",
    ) -> "dc_td.PutTaxRegistrationResponse":
        return dc_td.PutTaxRegistrationResponse.make_one(res)


taxsettings_caster = TAXSETTINGSCaster()
