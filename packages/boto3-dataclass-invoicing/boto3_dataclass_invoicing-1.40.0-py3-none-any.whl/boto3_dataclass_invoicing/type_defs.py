# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_invoicing import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BatchGetInvoiceProfileRequest:
    boto3_raw_data: "type_defs.BatchGetInvoiceProfileRequestTypeDef" = (
        dataclasses.field()
    )

    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetInvoiceProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetInvoiceProfileRequestTypeDef"]
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
class BillingPeriod:
    boto3_raw_data: "type_defs.BillingPeriodTypeDef" = dataclasses.field()

    Month = field("Month")
    Year = field("Year")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BillingPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BillingPeriodTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTag:
    boto3_raw_data: "type_defs.ResourceTagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CurrencyExchangeDetails:
    boto3_raw_data: "type_defs.CurrencyExchangeDetailsTypeDef" = dataclasses.field()

    SourceCurrencyCode = field("SourceCurrencyCode")
    TargetCurrencyCode = field("TargetCurrencyCode")
    Rate = field("Rate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CurrencyExchangeDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CurrencyExchangeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInvoiceUnitRequest:
    boto3_raw_data: "type_defs.DeleteInvoiceUnitRequestTypeDef" = dataclasses.field()

    InvoiceUnitArn = field("InvoiceUnitArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInvoiceUnitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInvoiceUnitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscountsBreakdownAmount:
    boto3_raw_data: "type_defs.DiscountsBreakdownAmountTypeDef" = dataclasses.field()

    Description = field("Description")
    Amount = field("Amount")
    Rate = field("Rate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiscountsBreakdownAmountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscountsBreakdownAmountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Entity:
    boto3_raw_data: "type_defs.EntityTypeDef" = dataclasses.field()

    InvoicingEntity = field("InvoicingEntity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeesBreakdownAmount:
    boto3_raw_data: "type_defs.FeesBreakdownAmountTypeDef" = dataclasses.field()

    Description = field("Description")
    Amount = field("Amount")
    Rate = field("Rate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeesBreakdownAmountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeesBreakdownAmountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filters:
    boto3_raw_data: "type_defs.FiltersTypeDef" = dataclasses.field()

    Names = field("Names")
    InvoiceReceivers = field("InvoiceReceivers")
    Accounts = field("Accounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FiltersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvoiceUnitRuleOutput:
    boto3_raw_data: "type_defs.InvoiceUnitRuleOutputTypeDef" = dataclasses.field()

    LinkedAccounts = field("LinkedAccounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvoiceUnitRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvoiceUnitRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiverAddress:
    boto3_raw_data: "type_defs.ReceiverAddressTypeDef" = dataclasses.field()

    AddressLine1 = field("AddressLine1")
    AddressLine2 = field("AddressLine2")
    AddressLine3 = field("AddressLine3")
    DistrictOrCounty = field("DistrictOrCounty")
    City = field("City")
    StateOrRegion = field("StateOrRegion")
    CountryCode = field("CountryCode")
    CompanyName = field("CompanyName")
    PostalCode = field("PostalCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceiverAddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReceiverAddressTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvoiceSummariesSelector:
    boto3_raw_data: "type_defs.InvoiceSummariesSelectorTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvoiceSummariesSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvoiceSummariesSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvoiceUnitRule:
    boto3_raw_data: "type_defs.InvoiceUnitRuleTypeDef" = dataclasses.field()

    LinkedAccounts = field("LinkedAccounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvoiceUnitRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvoiceUnitRuleTypeDef"]],
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
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxesBreakdownAmount:
    boto3_raw_data: "type_defs.TaxesBreakdownAmountTypeDef" = dataclasses.field()

    Description = field("Description")
    Amount = field("Amount")
    Rate = field("Rate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaxesBreakdownAmountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaxesBreakdownAmountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ResourceTagKeys = field("ResourceTagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInvoiceUnitResponse:
    boto3_raw_data: "type_defs.CreateInvoiceUnitResponseTypeDef" = dataclasses.field()

    InvoiceUnitArn = field("InvoiceUnitArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInvoiceUnitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInvoiceUnitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInvoiceUnitResponse:
    boto3_raw_data: "type_defs.DeleteInvoiceUnitResponseTypeDef" = dataclasses.field()

    InvoiceUnitArn = field("InvoiceUnitArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInvoiceUnitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInvoiceUnitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInvoiceUnitResponse:
    boto3_raw_data: "type_defs.UpdateInvoiceUnitResponseTypeDef" = dataclasses.field()

    InvoiceUnitArn = field("InvoiceUnitArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInvoiceUnitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInvoiceUnitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateInterval:
    boto3_raw_data: "type_defs.DateIntervalTypeDef" = dataclasses.field()

    StartDate = field("StartDate")
    EndDate = field("EndDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateIntervalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateIntervalTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvoiceUnitRequest:
    boto3_raw_data: "type_defs.GetInvoiceUnitRequestTypeDef" = dataclasses.field()

    InvoiceUnitArn = field("InvoiceUnitArn")
    AsOf = field("AsOf")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvoiceUnitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvoiceUnitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscountsBreakdown:
    boto3_raw_data: "type_defs.DiscountsBreakdownTypeDef" = dataclasses.field()

    @cached_property
    def Breakdown(self):  # pragma: no cover
        return DiscountsBreakdownAmount.make_many(self.boto3_raw_data["Breakdown"])

    TotalAmount = field("TotalAmount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiscountsBreakdownTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscountsBreakdownTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeesBreakdown:
    boto3_raw_data: "type_defs.FeesBreakdownTypeDef" = dataclasses.field()

    @cached_property
    def Breakdown(self):  # pragma: no cover
        return FeesBreakdownAmount.make_many(self.boto3_raw_data["Breakdown"])

    TotalAmount = field("TotalAmount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FeesBreakdownTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FeesBreakdownTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvoiceUnitsRequest:
    boto3_raw_data: "type_defs.ListInvoiceUnitsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filters.make_one(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    AsOf = field("AsOf")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvoiceUnitsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvoiceUnitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvoiceUnitResponse:
    boto3_raw_data: "type_defs.GetInvoiceUnitResponseTypeDef" = dataclasses.field()

    InvoiceUnitArn = field("InvoiceUnitArn")
    InvoiceReceiver = field("InvoiceReceiver")
    Name = field("Name")
    Description = field("Description")
    TaxInheritanceDisabled = field("TaxInheritanceDisabled")

    @cached_property
    def Rule(self):  # pragma: no cover
        return InvoiceUnitRuleOutput.make_one(self.boto3_raw_data["Rule"])

    LastModified = field("LastModified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvoiceUnitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvoiceUnitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvoiceUnit:
    boto3_raw_data: "type_defs.InvoiceUnitTypeDef" = dataclasses.field()

    InvoiceUnitArn = field("InvoiceUnitArn")
    InvoiceReceiver = field("InvoiceReceiver")
    Name = field("Name")
    Description = field("Description")
    TaxInheritanceDisabled = field("TaxInheritanceDisabled")

    @cached_property
    def Rule(self):  # pragma: no cover
        return InvoiceUnitRuleOutput.make_one(self.boto3_raw_data["Rule"])

    LastModified = field("LastModified")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvoiceUnitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvoiceUnitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvoiceProfile:
    boto3_raw_data: "type_defs.InvoiceProfileTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    ReceiverName = field("ReceiverName")

    @cached_property
    def ReceiverAddress(self):  # pragma: no cover
        return ReceiverAddress.make_one(self.boto3_raw_data["ReceiverAddress"])

    ReceiverEmail = field("ReceiverEmail")
    Issuer = field("Issuer")
    TaxRegistrationNumber = field("TaxRegistrationNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvoiceProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvoiceProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvoiceUnitsRequestPaginate:
    boto3_raw_data: "type_defs.ListInvoiceUnitsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filters.make_one(self.boto3_raw_data["Filters"])

    AsOf = field("AsOf")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInvoiceUnitsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvoiceUnitsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaxesBreakdown:
    boto3_raw_data: "type_defs.TaxesBreakdownTypeDef" = dataclasses.field()

    @cached_property
    def Breakdown(self):  # pragma: no cover
        return TaxesBreakdownAmount.make_many(self.boto3_raw_data["Breakdown"])

    TotalAmount = field("TotalAmount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaxesBreakdownTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaxesBreakdownTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvoiceSummariesFilter:
    boto3_raw_data: "type_defs.InvoiceSummariesFilterTypeDef" = dataclasses.field()

    @cached_property
    def TimeInterval(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimeInterval"])

    @cached_property
    def BillingPeriod(self):  # pragma: no cover
        return BillingPeriod.make_one(self.boto3_raw_data["BillingPeriod"])

    InvoicingEntity = field("InvoicingEntity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvoiceSummariesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvoiceSummariesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvoiceUnitsResponse:
    boto3_raw_data: "type_defs.ListInvoiceUnitsResponseTypeDef" = dataclasses.field()

    @cached_property
    def InvoiceUnits(self):  # pragma: no cover
        return InvoiceUnit.make_many(self.boto3_raw_data["InvoiceUnits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvoiceUnitsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvoiceUnitsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetInvoiceProfileResponse:
    boto3_raw_data: "type_defs.BatchGetInvoiceProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Profiles(self):  # pragma: no cover
        return InvoiceProfile.make_many(self.boto3_raw_data["Profiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetInvoiceProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetInvoiceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInvoiceUnitRequest:
    boto3_raw_data: "type_defs.CreateInvoiceUnitRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    InvoiceReceiver = field("InvoiceReceiver")
    Rule = field("Rule")
    Description = field("Description")
    TaxInheritanceDisabled = field("TaxInheritanceDisabled")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInvoiceUnitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInvoiceUnitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInvoiceUnitRequest:
    boto3_raw_data: "type_defs.UpdateInvoiceUnitRequestTypeDef" = dataclasses.field()

    InvoiceUnitArn = field("InvoiceUnitArn")
    Description = field("Description")
    TaxInheritanceDisabled = field("TaxInheritanceDisabled")
    Rule = field("Rule")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInvoiceUnitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInvoiceUnitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmountBreakdown:
    boto3_raw_data: "type_defs.AmountBreakdownTypeDef" = dataclasses.field()

    SubTotalAmount = field("SubTotalAmount")

    @cached_property
    def Discounts(self):  # pragma: no cover
        return DiscountsBreakdown.make_one(self.boto3_raw_data["Discounts"])

    @cached_property
    def Taxes(self):  # pragma: no cover
        return TaxesBreakdown.make_one(self.boto3_raw_data["Taxes"])

    @cached_property
    def Fees(self):  # pragma: no cover
        return FeesBreakdown.make_one(self.boto3_raw_data["Fees"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AmountBreakdownTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AmountBreakdownTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvoiceSummariesRequestPaginate:
    boto3_raw_data: "type_defs.ListInvoiceSummariesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Selector(self):  # pragma: no cover
        return InvoiceSummariesSelector.make_one(self.boto3_raw_data["Selector"])

    @cached_property
    def Filter(self):  # pragma: no cover
        return InvoiceSummariesFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInvoiceSummariesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvoiceSummariesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvoiceSummariesRequest:
    boto3_raw_data: "type_defs.ListInvoiceSummariesRequestTypeDef" = dataclasses.field()

    @cached_property
    def Selector(self):  # pragma: no cover
        return InvoiceSummariesSelector.make_one(self.boto3_raw_data["Selector"])

    @cached_property
    def Filter(self):  # pragma: no cover
        return InvoiceSummariesFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvoiceSummariesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvoiceSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvoiceCurrencyAmount:
    boto3_raw_data: "type_defs.InvoiceCurrencyAmountTypeDef" = dataclasses.field()

    TotalAmount = field("TotalAmount")
    TotalAmountBeforeTax = field("TotalAmountBeforeTax")
    CurrencyCode = field("CurrencyCode")

    @cached_property
    def AmountBreakdown(self):  # pragma: no cover
        return AmountBreakdown.make_one(self.boto3_raw_data["AmountBreakdown"])

    @cached_property
    def CurrencyExchangeDetails(self):  # pragma: no cover
        return CurrencyExchangeDetails.make_one(
            self.boto3_raw_data["CurrencyExchangeDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvoiceCurrencyAmountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvoiceCurrencyAmountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvoiceSummary:
    boto3_raw_data: "type_defs.InvoiceSummaryTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    InvoiceId = field("InvoiceId")
    IssuedDate = field("IssuedDate")
    DueDate = field("DueDate")

    @cached_property
    def Entity(self):  # pragma: no cover
        return Entity.make_one(self.boto3_raw_data["Entity"])

    @cached_property
    def BillingPeriod(self):  # pragma: no cover
        return BillingPeriod.make_one(self.boto3_raw_data["BillingPeriod"])

    InvoiceType = field("InvoiceType")
    OriginalInvoiceId = field("OriginalInvoiceId")
    PurchaseOrderNumber = field("PurchaseOrderNumber")

    @cached_property
    def BaseCurrencyAmount(self):  # pragma: no cover
        return InvoiceCurrencyAmount.make_one(self.boto3_raw_data["BaseCurrencyAmount"])

    @cached_property
    def TaxCurrencyAmount(self):  # pragma: no cover
        return InvoiceCurrencyAmount.make_one(self.boto3_raw_data["TaxCurrencyAmount"])

    @cached_property
    def PaymentCurrencyAmount(self):  # pragma: no cover
        return InvoiceCurrencyAmount.make_one(
            self.boto3_raw_data["PaymentCurrencyAmount"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvoiceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvoiceSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvoiceSummariesResponse:
    boto3_raw_data: "type_defs.ListInvoiceSummariesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InvoiceSummaries(self):  # pragma: no cover
        return InvoiceSummary.make_many(self.boto3_raw_data["InvoiceSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvoiceSummariesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvoiceSummariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
