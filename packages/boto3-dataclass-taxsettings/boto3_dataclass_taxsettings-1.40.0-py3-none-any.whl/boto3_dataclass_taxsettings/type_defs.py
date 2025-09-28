# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_taxsettings import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class TaxInheritanceDetails:
    boto3_raw_data: "type_defs.TaxInheritanceDetailsTypeDef" = dataclasses.field()

    inheritanceObtainedReason = field("inheritanceObtainedReason")
    parentEntityId = field("parentEntityId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaxInheritanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaxInheritanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Address:
    boto3_raw_data: "type_defs.AddressTypeDef" = dataclasses.field()

    addressLine1 = field("addressLine1")
    city = field("city")
    countryCode = field("countryCode")
    postalCode = field("postalCode")
    addressLine2 = field("addressLine2")
    addressLine3 = field("addressLine3")
    districtOrCounty = field("districtOrCounty")
    stateOrRegion = field("stateOrRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Jurisdiction:
    boto3_raw_data: "type_defs.JurisdictionTypeDef" = dataclasses.field()

    countryCode = field("countryCode")
    stateOrRegion = field("stateOrRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JurisdictionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JurisdictionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanadaAdditionalInfo:
    boto3_raw_data: "type_defs.CanadaAdditionalInfoTypeDef" = dataclasses.field()

    canadaQuebecSalesTaxNumber = field("canadaQuebecSalesTaxNumber")
    canadaRetailSalesTaxNumber = field("canadaRetailSalesTaxNumber")
    isResellerAccount = field("isResellerAccount")
    provincialSalesTaxId = field("provincialSalesTaxId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CanadaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanadaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EgyptAdditionalInfo:
    boto3_raw_data: "type_defs.EgyptAdditionalInfoTypeDef" = dataclasses.field()

    uniqueIdentificationNumber = field("uniqueIdentificationNumber")
    uniqueIdentificationNumberExpirationDate = field(
        "uniqueIdentificationNumberExpirationDate"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EgyptAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EgyptAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EstoniaAdditionalInfo:
    boto3_raw_data: "type_defs.EstoniaAdditionalInfoTypeDef" = dataclasses.field()

    registryCommercialCode = field("registryCommercialCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EstoniaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EstoniaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeorgiaAdditionalInfo:
    boto3_raw_data: "type_defs.GeorgiaAdditionalInfoTypeDef" = dataclasses.field()

    personType = field("personType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeorgiaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeorgiaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GreeceAdditionalInfo:
    boto3_raw_data: "type_defs.GreeceAdditionalInfoTypeDef" = dataclasses.field()

    contractingAuthorityCode = field("contractingAuthorityCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GreeceAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GreeceAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndonesiaAdditionalInfo:
    boto3_raw_data: "type_defs.IndonesiaAdditionalInfoTypeDef" = dataclasses.field()

    decisionNumber = field("decisionNumber")
    ppnExceptionDesignationCode = field("ppnExceptionDesignationCode")
    taxRegistrationNumberType = field("taxRegistrationNumberType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndonesiaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndonesiaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsraelAdditionalInfo:
    boto3_raw_data: "type_defs.IsraelAdditionalInfoTypeDef" = dataclasses.field()

    customerType = field("customerType")
    dealerType = field("dealerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsraelAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsraelAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItalyAdditionalInfo:
    boto3_raw_data: "type_defs.ItalyAdditionalInfoTypeDef" = dataclasses.field()

    cigNumber = field("cigNumber")
    cupNumber = field("cupNumber")
    sdiAccountId = field("sdiAccountId")
    taxCode = field("taxCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ItalyAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ItalyAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KenyaAdditionalInfo:
    boto3_raw_data: "type_defs.KenyaAdditionalInfoTypeDef" = dataclasses.field()

    personType = field("personType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KenyaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KenyaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolandAdditionalInfo:
    boto3_raw_data: "type_defs.PolandAdditionalInfoTypeDef" = dataclasses.field()

    individualRegistrationNumber = field("individualRegistrationNumber")
    isGroupVatEnabled = field("isGroupVatEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolandAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolandAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RomaniaAdditionalInfo:
    boto3_raw_data: "type_defs.RomaniaAdditionalInfoTypeDef" = dataclasses.field()

    taxRegistrationNumberType = field("taxRegistrationNumberType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RomaniaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RomaniaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaudiArabiaAdditionalInfo:
    boto3_raw_data: "type_defs.SaudiArabiaAdditionalInfoTypeDef" = dataclasses.field()

    taxRegistrationNumberType = field("taxRegistrationNumberType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SaudiArabiaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SaudiArabiaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SouthKoreaAdditionalInfo:
    boto3_raw_data: "type_defs.SouthKoreaAdditionalInfoTypeDef" = dataclasses.field()

    businessRepresentativeName = field("businessRepresentativeName")
    itemOfBusiness = field("itemOfBusiness")
    lineOfBusiness = field("lineOfBusiness")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SouthKoreaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SouthKoreaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpainAdditionalInfo:
    boto3_raw_data: "type_defs.SpainAdditionalInfoTypeDef" = dataclasses.field()

    registrationType = field("registrationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpainAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpainAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TurkeyAdditionalInfo:
    boto3_raw_data: "type_defs.TurkeyAdditionalInfoTypeDef" = dataclasses.field()

    industries = field("industries")
    kepEmailId = field("kepEmailId")
    secondaryTaxId = field("secondaryTaxId")
    taxOffice = field("taxOffice")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TurkeyAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TurkeyAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UkraineAdditionalInfo:
    boto3_raw_data: "type_defs.UkraineAdditionalInfoTypeDef" = dataclasses.field()

    ukraineTrnType = field("ukraineTrnType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UkraineAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UkraineAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UzbekistanAdditionalInfo:
    boto3_raw_data: "type_defs.UzbekistanAdditionalInfoTypeDef" = dataclasses.field()

    taxRegistrationNumberType = field("taxRegistrationNumberType")
    vatRegistrationNumber = field("vatRegistrationNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UzbekistanAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UzbekistanAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VietnamAdditionalInfo:
    boto3_raw_data: "type_defs.VietnamAdditionalInfoTypeDef" = dataclasses.field()

    electronicTransactionCodeNumber = field("electronicTransactionCodeNumber")
    enterpriseIdentificationNumber = field("enterpriseIdentificationNumber")
    paymentVoucherNumber = field("paymentVoucherNumber")
    paymentVoucherNumberDate = field("paymentVoucherNumberDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VietnamAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VietnamAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrazilAdditionalInfo:
    boto3_raw_data: "type_defs.BrazilAdditionalInfoTypeDef" = dataclasses.field()

    ccmCode = field("ccmCode")
    legalNatureCode = field("legalNatureCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrazilAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrazilAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndiaAdditionalInfo:
    boto3_raw_data: "type_defs.IndiaAdditionalInfoTypeDef" = dataclasses.field()

    pan = field("pan")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndiaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndiaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalaysiaAdditionalInfoOutput:
    boto3_raw_data: "type_defs.MalaysiaAdditionalInfoOutputTypeDef" = (
        dataclasses.field()
    )

    businessRegistrationNumber = field("businessRegistrationNumber")
    serviceTaxCodes = field("serviceTaxCodes")
    taxInformationNumber = field("taxInformationNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MalaysiaAdditionalInfoOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalaysiaAdditionalInfoOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Authority:
    boto3_raw_data: "type_defs.AuthorityTypeDef" = dataclasses.field()

    country = field("country")
    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthorityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthorityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteTaxRegistrationError:
    boto3_raw_data: "type_defs.BatchDeleteTaxRegistrationErrorTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    message = field("message")
    code = field("code")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeleteTaxRegistrationErrorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteTaxRegistrationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteTaxRegistrationRequest:
    boto3_raw_data: "type_defs.BatchDeleteTaxRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteTaxRegistrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteTaxRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetTaxExemptionsRequest:
    boto3_raw_data: "type_defs.BatchGetTaxExemptionsRequestTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetTaxExemptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTaxExemptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutTaxRegistrationError:
    boto3_raw_data: "type_defs.BatchPutTaxRegistrationErrorTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    message = field("message")
    code = field("code")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutTaxRegistrationErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutTaxRegistrationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSupplementalTaxRegistrationRequest:
    boto3_raw_data: "type_defs.DeleteSupplementalTaxRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    authorityId = field("authorityId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSupplementalTaxRegistrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSupplementalTaxRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTaxRegistrationRequest:
    boto3_raw_data: "type_defs.DeleteTaxRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTaxRegistrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTaxRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationS3Location:
    boto3_raw_data: "type_defs.DestinationS3LocationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationS3LocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationS3LocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxDocumentMetadata:
    boto3_raw_data: "type_defs.TaxDocumentMetadataTypeDef" = dataclasses.field()

    taxDocumentAccessToken = field("taxDocumentAccessToken")
    taxDocumentName = field("taxDocumentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaxDocumentMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaxDocumentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaxRegistrationRequest:
    boto3_raw_data: "type_defs.GetTaxRegistrationRequestTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTaxRegistrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaxRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSupplementalTaxRegistrationsRequest:
    boto3_raw_data: "type_defs.ListSupplementalTaxRegistrationsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSupplementalTaxRegistrationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSupplementalTaxRegistrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaxExemptionsRequest:
    boto3_raw_data: "type_defs.ListTaxExemptionsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaxExemptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaxExemptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaxRegistrationsRequest:
    boto3_raw_data: "type_defs.ListTaxRegistrationsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaxRegistrationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaxRegistrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalaysiaAdditionalInfo:
    boto3_raw_data: "type_defs.MalaysiaAdditionalInfoTypeDef" = dataclasses.field()

    businessRegistrationNumber = field("businessRegistrationNumber")
    serviceTaxCodes = field("serviceTaxCodes")
    taxInformationNumber = field("taxInformationNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MalaysiaAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalaysiaAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTaxInheritanceRequest:
    boto3_raw_data: "type_defs.PutTaxInheritanceRequestTypeDef" = dataclasses.field()

    heritageStatus = field("heritageStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTaxInheritanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTaxInheritanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceS3Location:
    boto3_raw_data: "type_defs.SourceS3LocationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceS3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceS3LocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupplementalTaxRegistrationEntry:
    boto3_raw_data: "type_defs.SupplementalTaxRegistrationEntryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["address"])

    legalName = field("legalName")
    registrationId = field("registrationId")
    registrationType = field("registrationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SupplementalTaxRegistrationEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupplementalTaxRegistrationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupplementalTaxRegistration:
    boto3_raw_data: "type_defs.SupplementalTaxRegistrationTypeDef" = dataclasses.field()

    @cached_property
    def address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["address"])

    authorityId = field("authorityId")
    legalName = field("legalName")
    registrationId = field("registrationId")
    registrationType = field("registrationType")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupplementalTaxRegistrationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupplementalTaxRegistrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountMetaData:
    boto3_raw_data: "type_defs.AccountMetaDataTypeDef" = dataclasses.field()

    accountName = field("accountName")

    @cached_property
    def address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["address"])

    addressRoleMap = field("addressRoleMap")
    addressType = field("addressType")
    seller = field("seller")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountMetaDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountMetaDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalInfoResponse:
    boto3_raw_data: "type_defs.AdditionalInfoResponseTypeDef" = dataclasses.field()

    @cached_property
    def brazilAdditionalInfo(self):  # pragma: no cover
        return BrazilAdditionalInfo.make_one(
            self.boto3_raw_data["brazilAdditionalInfo"]
        )

    @cached_property
    def canadaAdditionalInfo(self):  # pragma: no cover
        return CanadaAdditionalInfo.make_one(
            self.boto3_raw_data["canadaAdditionalInfo"]
        )

    @cached_property
    def egyptAdditionalInfo(self):  # pragma: no cover
        return EgyptAdditionalInfo.make_one(self.boto3_raw_data["egyptAdditionalInfo"])

    @cached_property
    def estoniaAdditionalInfo(self):  # pragma: no cover
        return EstoniaAdditionalInfo.make_one(
            self.boto3_raw_data["estoniaAdditionalInfo"]
        )

    @cached_property
    def georgiaAdditionalInfo(self):  # pragma: no cover
        return GeorgiaAdditionalInfo.make_one(
            self.boto3_raw_data["georgiaAdditionalInfo"]
        )

    @cached_property
    def greeceAdditionalInfo(self):  # pragma: no cover
        return GreeceAdditionalInfo.make_one(
            self.boto3_raw_data["greeceAdditionalInfo"]
        )

    @cached_property
    def indiaAdditionalInfo(self):  # pragma: no cover
        return IndiaAdditionalInfo.make_one(self.boto3_raw_data["indiaAdditionalInfo"])

    @cached_property
    def indonesiaAdditionalInfo(self):  # pragma: no cover
        return IndonesiaAdditionalInfo.make_one(
            self.boto3_raw_data["indonesiaAdditionalInfo"]
        )

    @cached_property
    def israelAdditionalInfo(self):  # pragma: no cover
        return IsraelAdditionalInfo.make_one(
            self.boto3_raw_data["israelAdditionalInfo"]
        )

    @cached_property
    def italyAdditionalInfo(self):  # pragma: no cover
        return ItalyAdditionalInfo.make_one(self.boto3_raw_data["italyAdditionalInfo"])

    @cached_property
    def kenyaAdditionalInfo(self):  # pragma: no cover
        return KenyaAdditionalInfo.make_one(self.boto3_raw_data["kenyaAdditionalInfo"])

    @cached_property
    def malaysiaAdditionalInfo(self):  # pragma: no cover
        return MalaysiaAdditionalInfoOutput.make_one(
            self.boto3_raw_data["malaysiaAdditionalInfo"]
        )

    @cached_property
    def polandAdditionalInfo(self):  # pragma: no cover
        return PolandAdditionalInfo.make_one(
            self.boto3_raw_data["polandAdditionalInfo"]
        )

    @cached_property
    def romaniaAdditionalInfo(self):  # pragma: no cover
        return RomaniaAdditionalInfo.make_one(
            self.boto3_raw_data["romaniaAdditionalInfo"]
        )

    @cached_property
    def saudiArabiaAdditionalInfo(self):  # pragma: no cover
        return SaudiArabiaAdditionalInfo.make_one(
            self.boto3_raw_data["saudiArabiaAdditionalInfo"]
        )

    @cached_property
    def southKoreaAdditionalInfo(self):  # pragma: no cover
        return SouthKoreaAdditionalInfo.make_one(
            self.boto3_raw_data["southKoreaAdditionalInfo"]
        )

    @cached_property
    def spainAdditionalInfo(self):  # pragma: no cover
        return SpainAdditionalInfo.make_one(self.boto3_raw_data["spainAdditionalInfo"])

    @cached_property
    def turkeyAdditionalInfo(self):  # pragma: no cover
        return TurkeyAdditionalInfo.make_one(
            self.boto3_raw_data["turkeyAdditionalInfo"]
        )

    @cached_property
    def ukraineAdditionalInfo(self):  # pragma: no cover
        return UkraineAdditionalInfo.make_one(
            self.boto3_raw_data["ukraineAdditionalInfo"]
        )

    @cached_property
    def uzbekistanAdditionalInfo(self):  # pragma: no cover
        return UzbekistanAdditionalInfo.make_one(
            self.boto3_raw_data["uzbekistanAdditionalInfo"]
        )

    @cached_property
    def vietnamAdditionalInfo(self):  # pragma: no cover
        return VietnamAdditionalInfo.make_one(
            self.boto3_raw_data["vietnamAdditionalInfo"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdditionalInfoResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxExemptionType:
    boto3_raw_data: "type_defs.TaxExemptionTypeTypeDef" = dataclasses.field()

    @cached_property
    def applicableJurisdictions(self):  # pragma: no cover
        return Authority.make_many(self.boto3_raw_data["applicableJurisdictions"])

    description = field("description")
    displayName = field("displayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaxExemptionTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaxExemptionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteTaxRegistrationResponse:
    boto3_raw_data: "type_defs.BatchDeleteTaxRegistrationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchDeleteTaxRegistrationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteTaxRegistrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteTaxRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaxInheritanceResponse:
    boto3_raw_data: "type_defs.GetTaxInheritanceResponseTypeDef" = dataclasses.field()

    heritageStatus = field("heritageStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTaxInheritanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaxInheritanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaxRegistrationDocumentResponse:
    boto3_raw_data: "type_defs.GetTaxRegistrationDocumentResponseTypeDef" = (
        dataclasses.field()
    )

    destinationFilePath = field("destinationFilePath")
    presignedS3Url = field("presignedS3Url")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTaxRegistrationDocumentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaxRegistrationDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSupplementalTaxRegistrationResponse:
    boto3_raw_data: "type_defs.PutSupplementalTaxRegistrationResponseTypeDef" = (
        dataclasses.field()
    )

    authorityId = field("authorityId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSupplementalTaxRegistrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSupplementalTaxRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTaxExemptionResponse:
    boto3_raw_data: "type_defs.PutTaxExemptionResponseTypeDef" = dataclasses.field()

    caseId = field("caseId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTaxExemptionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTaxExemptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTaxRegistrationResponse:
    boto3_raw_data: "type_defs.PutTaxRegistrationResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTaxRegistrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTaxRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutTaxRegistrationResponse:
    boto3_raw_data: "type_defs.BatchPutTaxRegistrationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchPutTaxRegistrationError.make_many(self.boto3_raw_data["errors"])

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchPutTaxRegistrationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutTaxRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExemptionCertificate:
    boto3_raw_data: "type_defs.ExemptionCertificateTypeDef" = dataclasses.field()

    documentFile = field("documentFile")
    documentName = field("documentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExemptionCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExemptionCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxRegistrationDocFile:
    boto3_raw_data: "type_defs.TaxRegistrationDocFileTypeDef" = dataclasses.field()

    fileContent = field("fileContent")
    fileName = field("fileName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaxRegistrationDocFileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaxRegistrationDocFileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaxRegistrationDocumentRequest:
    boto3_raw_data: "type_defs.GetTaxRegistrationDocumentRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taxDocumentMetadata(self):  # pragma: no cover
        return TaxDocumentMetadata.make_one(self.boto3_raw_data["taxDocumentMetadata"])

    @cached_property
    def destinationS3Location(self):  # pragma: no cover
        return DestinationS3Location.make_one(
            self.boto3_raw_data["destinationS3Location"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTaxRegistrationDocumentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaxRegistrationDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSupplementalTaxRegistrationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListSupplementalTaxRegistrationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSupplementalTaxRegistrationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListSupplementalTaxRegistrationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaxExemptionsRequestPaginate:
    boto3_raw_data: "type_defs.ListTaxExemptionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTaxExemptionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaxExemptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaxRegistrationsRequestPaginate:
    boto3_raw_data: "type_defs.ListTaxRegistrationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTaxRegistrationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaxRegistrationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSupplementalTaxRegistrationRequest:
    boto3_raw_data: "type_defs.PutSupplementalTaxRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taxRegistrationEntry(self):  # pragma: no cover
        return SupplementalTaxRegistrationEntry.make_one(
            self.boto3_raw_data["taxRegistrationEntry"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSupplementalTaxRegistrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSupplementalTaxRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSupplementalTaxRegistrationsResponse:
    boto3_raw_data: "type_defs.ListSupplementalTaxRegistrationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taxRegistrations(self):  # pragma: no cover
        return SupplementalTaxRegistration.make_many(
            self.boto3_raw_data["taxRegistrations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSupplementalTaxRegistrationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSupplementalTaxRegistrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxRegistration:
    boto3_raw_data: "type_defs.TaxRegistrationTypeDef" = dataclasses.field()

    @cached_property
    def legalAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["legalAddress"])

    legalName = field("legalName")
    registrationId = field("registrationId")
    registrationType = field("registrationType")
    status = field("status")

    @cached_property
    def additionalTaxInformation(self):  # pragma: no cover
        return AdditionalInfoResponse.make_one(
            self.boto3_raw_data["additionalTaxInformation"]
        )

    certifiedEmailId = field("certifiedEmailId")
    sector = field("sector")

    @cached_property
    def taxDocumentMetadatas(self):  # pragma: no cover
        return TaxDocumentMetadata.make_many(
            self.boto3_raw_data["taxDocumentMetadatas"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaxRegistrationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaxRegistrationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxRegistrationWithJurisdiction:
    boto3_raw_data: "type_defs.TaxRegistrationWithJurisdictionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def jurisdiction(self):  # pragma: no cover
        return Jurisdiction.make_one(self.boto3_raw_data["jurisdiction"])

    legalName = field("legalName")
    registrationId = field("registrationId")
    registrationType = field("registrationType")
    status = field("status")

    @cached_property
    def additionalTaxInformation(self):  # pragma: no cover
        return AdditionalInfoResponse.make_one(
            self.boto3_raw_data["additionalTaxInformation"]
        )

    certifiedEmailId = field("certifiedEmailId")
    sector = field("sector")

    @cached_property
    def taxDocumentMetadatas(self):  # pragma: no cover
        return TaxDocumentMetadata.make_many(
            self.boto3_raw_data["taxDocumentMetadatas"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TaxRegistrationWithJurisdictionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaxRegistrationWithJurisdictionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaxExemptionTypesResponse:
    boto3_raw_data: "type_defs.GetTaxExemptionTypesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taxExemptionTypes(self):  # pragma: no cover
        return TaxExemptionType.make_many(self.boto3_raw_data["taxExemptionTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTaxExemptionTypesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaxExemptionTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxExemption:
    boto3_raw_data: "type_defs.TaxExemptionTypeDef" = dataclasses.field()

    @cached_property
    def authority(self):  # pragma: no cover
        return Authority.make_one(self.boto3_raw_data["authority"])

    @cached_property
    def taxExemptionType(self):  # pragma: no cover
        return TaxExemptionType.make_one(self.boto3_raw_data["taxExemptionType"])

    effectiveDate = field("effectiveDate")
    expirationDate = field("expirationDate")
    status = field("status")
    systemEffectiveDate = field("systemEffectiveDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaxExemptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaxExemptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTaxExemptionRequest:
    boto3_raw_data: "type_defs.PutTaxExemptionRequestTypeDef" = dataclasses.field()

    accountIds = field("accountIds")

    @cached_property
    def authority(self):  # pragma: no cover
        return Authority.make_one(self.boto3_raw_data["authority"])

    @cached_property
    def exemptionCertificate(self):  # pragma: no cover
        return ExemptionCertificate.make_one(
            self.boto3_raw_data["exemptionCertificate"]
        )

    exemptionType = field("exemptionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTaxExemptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTaxExemptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxRegistrationDocument:
    boto3_raw_data: "type_defs.TaxRegistrationDocumentTypeDef" = dataclasses.field()

    @cached_property
    def file(self):  # pragma: no cover
        return TaxRegistrationDocFile.make_one(self.boto3_raw_data["file"])

    @cached_property
    def s3Location(self):  # pragma: no cover
        return SourceS3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaxRegistrationDocumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaxRegistrationDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalInfoRequest:
    boto3_raw_data: "type_defs.AdditionalInfoRequestTypeDef" = dataclasses.field()

    @cached_property
    def canadaAdditionalInfo(self):  # pragma: no cover
        return CanadaAdditionalInfo.make_one(
            self.boto3_raw_data["canadaAdditionalInfo"]
        )

    @cached_property
    def egyptAdditionalInfo(self):  # pragma: no cover
        return EgyptAdditionalInfo.make_one(self.boto3_raw_data["egyptAdditionalInfo"])

    @cached_property
    def estoniaAdditionalInfo(self):  # pragma: no cover
        return EstoniaAdditionalInfo.make_one(
            self.boto3_raw_data["estoniaAdditionalInfo"]
        )

    @cached_property
    def georgiaAdditionalInfo(self):  # pragma: no cover
        return GeorgiaAdditionalInfo.make_one(
            self.boto3_raw_data["georgiaAdditionalInfo"]
        )

    @cached_property
    def greeceAdditionalInfo(self):  # pragma: no cover
        return GreeceAdditionalInfo.make_one(
            self.boto3_raw_data["greeceAdditionalInfo"]
        )

    @cached_property
    def indonesiaAdditionalInfo(self):  # pragma: no cover
        return IndonesiaAdditionalInfo.make_one(
            self.boto3_raw_data["indonesiaAdditionalInfo"]
        )

    @cached_property
    def israelAdditionalInfo(self):  # pragma: no cover
        return IsraelAdditionalInfo.make_one(
            self.boto3_raw_data["israelAdditionalInfo"]
        )

    @cached_property
    def italyAdditionalInfo(self):  # pragma: no cover
        return ItalyAdditionalInfo.make_one(self.boto3_raw_data["italyAdditionalInfo"])

    @cached_property
    def kenyaAdditionalInfo(self):  # pragma: no cover
        return KenyaAdditionalInfo.make_one(self.boto3_raw_data["kenyaAdditionalInfo"])

    malaysiaAdditionalInfo = field("malaysiaAdditionalInfo")

    @cached_property
    def polandAdditionalInfo(self):  # pragma: no cover
        return PolandAdditionalInfo.make_one(
            self.boto3_raw_data["polandAdditionalInfo"]
        )

    @cached_property
    def romaniaAdditionalInfo(self):  # pragma: no cover
        return RomaniaAdditionalInfo.make_one(
            self.boto3_raw_data["romaniaAdditionalInfo"]
        )

    @cached_property
    def saudiArabiaAdditionalInfo(self):  # pragma: no cover
        return SaudiArabiaAdditionalInfo.make_one(
            self.boto3_raw_data["saudiArabiaAdditionalInfo"]
        )

    @cached_property
    def southKoreaAdditionalInfo(self):  # pragma: no cover
        return SouthKoreaAdditionalInfo.make_one(
            self.boto3_raw_data["southKoreaAdditionalInfo"]
        )

    @cached_property
    def spainAdditionalInfo(self):  # pragma: no cover
        return SpainAdditionalInfo.make_one(self.boto3_raw_data["spainAdditionalInfo"])

    @cached_property
    def turkeyAdditionalInfo(self):  # pragma: no cover
        return TurkeyAdditionalInfo.make_one(
            self.boto3_raw_data["turkeyAdditionalInfo"]
        )

    @cached_property
    def ukraineAdditionalInfo(self):  # pragma: no cover
        return UkraineAdditionalInfo.make_one(
            self.boto3_raw_data["ukraineAdditionalInfo"]
        )

    @cached_property
    def uzbekistanAdditionalInfo(self):  # pragma: no cover
        return UzbekistanAdditionalInfo.make_one(
            self.boto3_raw_data["uzbekistanAdditionalInfo"]
        )

    @cached_property
    def vietnamAdditionalInfo(self):  # pragma: no cover
        return VietnamAdditionalInfo.make_one(
            self.boto3_raw_data["vietnamAdditionalInfo"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdditionalInfoRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalInfoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaxRegistrationResponse:
    boto3_raw_data: "type_defs.GetTaxRegistrationResponseTypeDef" = dataclasses.field()

    @cached_property
    def taxRegistration(self):  # pragma: no cover
        return TaxRegistration.make_one(self.boto3_raw_data["taxRegistration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTaxRegistrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaxRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountDetails:
    boto3_raw_data: "type_defs.AccountDetailsTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @cached_property
    def accountMetaData(self):  # pragma: no cover
        return AccountMetaData.make_one(self.boto3_raw_data["accountMetaData"])

    @cached_property
    def taxInheritanceDetails(self):  # pragma: no cover
        return TaxInheritanceDetails.make_one(
            self.boto3_raw_data["taxInheritanceDetails"]
        )

    @cached_property
    def taxRegistration(self):  # pragma: no cover
        return TaxRegistrationWithJurisdiction.make_one(
            self.boto3_raw_data["taxRegistration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxExemptionDetails:
    boto3_raw_data: "type_defs.TaxExemptionDetailsTypeDef" = dataclasses.field()

    heritageObtainedDetails = field("heritageObtainedDetails")
    heritageObtainedParentEntity = field("heritageObtainedParentEntity")
    heritageObtainedReason = field("heritageObtainedReason")

    @cached_property
    def taxExemptions(self):  # pragma: no cover
        return TaxExemption.make_many(self.boto3_raw_data["taxExemptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaxExemptionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaxExemptionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerificationDetails:
    boto3_raw_data: "type_defs.VerificationDetailsTypeDef" = dataclasses.field()

    dateOfBirth = field("dateOfBirth")

    @cached_property
    def taxRegistrationDocuments(self):  # pragma: no cover
        return TaxRegistrationDocument.make_many(
            self.boto3_raw_data["taxRegistrationDocuments"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerificationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerificationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaxRegistrationsResponse:
    boto3_raw_data: "type_defs.ListTaxRegistrationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accountDetails(self):  # pragma: no cover
        return AccountDetails.make_many(self.boto3_raw_data["accountDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaxRegistrationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaxRegistrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetTaxExemptionsResponse:
    boto3_raw_data: "type_defs.BatchGetTaxExemptionsResponseTypeDef" = (
        dataclasses.field()
    )

    failedAccounts = field("failedAccounts")
    taxExemptionDetailsMap = field("taxExemptionDetailsMap")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetTaxExemptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTaxExemptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaxExemptionsResponse:
    boto3_raw_data: "type_defs.ListTaxExemptionsResponseTypeDef" = dataclasses.field()

    taxExemptionDetailsMap = field("taxExemptionDetailsMap")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaxExemptionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaxExemptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxRegistrationEntry:
    boto3_raw_data: "type_defs.TaxRegistrationEntryTypeDef" = dataclasses.field()

    registrationId = field("registrationId")
    registrationType = field("registrationType")

    @cached_property
    def additionalTaxInformation(self):  # pragma: no cover
        return AdditionalInfoRequest.make_one(
            self.boto3_raw_data["additionalTaxInformation"]
        )

    certifiedEmailId = field("certifiedEmailId")

    @cached_property
    def legalAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["legalAddress"])

    legalName = field("legalName")
    sector = field("sector")

    @cached_property
    def verificationDetails(self):  # pragma: no cover
        return VerificationDetails.make_one(self.boto3_raw_data["verificationDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaxRegistrationEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaxRegistrationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutTaxRegistrationRequest:
    boto3_raw_data: "type_defs.BatchPutTaxRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @cached_property
    def taxRegistrationEntry(self):  # pragma: no cover
        return TaxRegistrationEntry.make_one(
            self.boto3_raw_data["taxRegistrationEntry"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchPutTaxRegistrationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutTaxRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTaxRegistrationRequest:
    boto3_raw_data: "type_defs.PutTaxRegistrationRequestTypeDef" = dataclasses.field()

    @cached_property
    def taxRegistrationEntry(self):  # pragma: no cover
        return TaxRegistrationEntry.make_one(
            self.boto3_raw_data["taxRegistrationEntry"]
        )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTaxRegistrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTaxRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
