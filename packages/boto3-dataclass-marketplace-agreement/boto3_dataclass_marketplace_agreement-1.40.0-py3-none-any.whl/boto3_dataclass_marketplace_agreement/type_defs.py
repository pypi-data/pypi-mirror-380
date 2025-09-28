# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_marketplace_agreement import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ByolPricingTerm:
    boto3_raw_data: "type_defs.ByolPricingTermTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ByolPricingTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ByolPricingTermTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurringPaymentTerm:
    boto3_raw_data: "type_defs.RecurringPaymentTermTypeDef" = dataclasses.field()

    billingPeriod = field("billingPeriod")
    currencyCode = field("currencyCode")
    price = field("price")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecurringPaymentTermTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecurringPaymentTermTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportTerm:
    boto3_raw_data: "type_defs.SupportTermTypeDef" = dataclasses.field()

    refundPolicy = field("refundPolicy")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SupportTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SupportTermTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidityTerm:
    boto3_raw_data: "type_defs.ValidityTermTypeDef" = dataclasses.field()

    agreementDuration = field("agreementDuration")
    agreementEndDate = field("agreementEndDate")
    agreementStartDate = field("agreementStartDate")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidityTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidityTermTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Acceptor:
    boto3_raw_data: "type_defs.AcceptorTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcceptorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AcceptorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Proposer:
    boto3_raw_data: "type_defs.ProposerTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProposerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProposerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimension:
    boto3_raw_data: "type_defs.DimensionTypeDef" = dataclasses.field()

    dimensionKey = field("dimensionKey")
    dimensionValue = field("dimensionValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Constraints:
    boto3_raw_data: "type_defs.ConstraintsTypeDef" = dataclasses.field()

    multipleDimensionSelection = field("multipleDimensionSelection")
    quantityConfiguration = field("quantityConfiguration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConstraintsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConstraintsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateCardItem:
    boto3_raw_data: "type_defs.RateCardItemTypeDef" = dataclasses.field()

    dimensionKey = field("dimensionKey")
    price = field("price")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RateCardItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RateCardItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Selector:
    boto3_raw_data: "type_defs.SelectorTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SelectorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgreementInput:
    boto3_raw_data: "type_defs.DescribeAgreementInputTypeDef" = dataclasses.field()

    agreementId = field("agreementId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgreementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgreementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EstimatedCharges:
    boto3_raw_data: "type_defs.EstimatedChargesTypeDef" = dataclasses.field()

    agreementValue = field("agreementValue")
    currencyCode = field("currencyCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EstimatedChargesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EstimatedChargesTypeDef"]
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
class DocumentItem:
    boto3_raw_data: "type_defs.DocumentItemTypeDef" = dataclasses.field()

    type = field("type")
    url = field("url")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantItem:
    boto3_raw_data: "type_defs.GrantItemTypeDef" = dataclasses.field()

    dimensionKey = field("dimensionKey")
    maxQuantity = field("maxQuantity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgreementTermsInput:
    boto3_raw_data: "type_defs.GetAgreementTermsInputTypeDef" = dataclasses.field()

    agreementId = field("agreementId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgreementTermsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgreementTermsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleItem:
    boto3_raw_data: "type_defs.ScheduleItemTypeDef" = dataclasses.field()

    chargeAmount = field("chargeAmount")
    chargeDate = field("chargeDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenewalTermConfiguration:
    boto3_raw_data: "type_defs.RenewalTermConfigurationTypeDef" = dataclasses.field()

    enableAutoRenew = field("enableAutoRenew")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RenewalTermConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenewalTermConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sort:
    boto3_raw_data: "type_defs.SortTypeDef" = dataclasses.field()

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurableUpfrontPricingTermConfiguration:
    boto3_raw_data: "type_defs.ConfigurableUpfrontPricingTermConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["dimensions"])

    selectorValue = field("selectorValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfigurableUpfrontPricingTermConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurableUpfrontPricingTermConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageBasedRateCardItem:
    boto3_raw_data: "type_defs.UsageBasedRateCardItemTypeDef" = dataclasses.field()

    @cached_property
    def rateCard(self):  # pragma: no cover
        return RateCardItem.make_many(self.boto3_raw_data["rateCard"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageBasedRateCardItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageBasedRateCardItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurableUpfrontRateCardItem:
    boto3_raw_data: "type_defs.ConfigurableUpfrontRateCardItemTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def constraints(self):  # pragma: no cover
        return Constraints.make_one(self.boto3_raw_data["constraints"])

    @cached_property
    def rateCard(self):  # pragma: no cover
        return RateCardItem.make_many(self.boto3_raw_data["rateCard"])

    @cached_property
    def selector(self):  # pragma: no cover
        return Selector.make_one(self.boto3_raw_data["selector"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigurableUpfrontRateCardItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurableUpfrontRateCardItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LegalTerm:
    boto3_raw_data: "type_defs.LegalTermTypeDef" = dataclasses.field()

    @cached_property
    def documents(self):  # pragma: no cover
        return DocumentItem.make_many(self.boto3_raw_data["documents"])

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LegalTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LegalTermTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FixedUpfrontPricingTerm:
    boto3_raw_data: "type_defs.FixedUpfrontPricingTermTypeDef" = dataclasses.field()

    currencyCode = field("currencyCode")
    duration = field("duration")

    @cached_property
    def grants(self):  # pragma: no cover
        return GrantItem.make_many(self.boto3_raw_data["grants"])

    price = field("price")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FixedUpfrontPricingTermTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FixedUpfrontPricingTermTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FreeTrialPricingTerm:
    boto3_raw_data: "type_defs.FreeTrialPricingTermTypeDef" = dataclasses.field()

    duration = field("duration")

    @cached_property
    def grants(self):  # pragma: no cover
        return GrantItem.make_many(self.boto3_raw_data["grants"])

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FreeTrialPricingTermTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FreeTrialPricingTermTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaymentScheduleTerm:
    boto3_raw_data: "type_defs.PaymentScheduleTermTypeDef" = dataclasses.field()

    currencyCode = field("currencyCode")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleItem.make_many(self.boto3_raw_data["schedule"])

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PaymentScheduleTermTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PaymentScheduleTermTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProposalSummary:
    boto3_raw_data: "type_defs.ProposalSummaryTypeDef" = dataclasses.field()

    offerId = field("offerId")

    @cached_property
    def resources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["resources"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProposalSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProposalSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenewalTerm:
    boto3_raw_data: "type_defs.RenewalTermTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return RenewalTermConfiguration.make_one(self.boto3_raw_data["configuration"])

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RenewalTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RenewalTermTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAgreementsInput:
    boto3_raw_data: "type_defs.SearchAgreementsInputTypeDef" = dataclasses.field()

    catalog = field("catalog")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def sort(self):  # pragma: no cover
        return Sort.make_one(self.boto3_raw_data["sort"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchAgreementsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAgreementsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageBasedPricingTerm:
    boto3_raw_data: "type_defs.UsageBasedPricingTermTypeDef" = dataclasses.field()

    currencyCode = field("currencyCode")

    @cached_property
    def rateCards(self):  # pragma: no cover
        return UsageBasedRateCardItem.make_many(self.boto3_raw_data["rateCards"])

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageBasedPricingTermTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageBasedPricingTermTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurableUpfrontPricingTerm:
    boto3_raw_data: "type_defs.ConfigurableUpfrontPricingTermTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return ConfigurableUpfrontPricingTermConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    currencyCode = field("currencyCode")

    @cached_property
    def rateCards(self):  # pragma: no cover
        return ConfigurableUpfrontRateCardItem.make_many(
            self.boto3_raw_data["rateCards"]
        )

    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigurableUpfrontPricingTermTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurableUpfrontPricingTermTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgreementViewSummary:
    boto3_raw_data: "type_defs.AgreementViewSummaryTypeDef" = dataclasses.field()

    acceptanceTime = field("acceptanceTime")

    @cached_property
    def acceptor(self):  # pragma: no cover
        return Acceptor.make_one(self.boto3_raw_data["acceptor"])

    agreementId = field("agreementId")
    agreementType = field("agreementType")
    endTime = field("endTime")

    @cached_property
    def proposalSummary(self):  # pragma: no cover
        return ProposalSummary.make_one(self.boto3_raw_data["proposalSummary"])

    @cached_property
    def proposer(self):  # pragma: no cover
        return Proposer.make_one(self.boto3_raw_data["proposer"])

    startTime = field("startTime")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgreementViewSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgreementViewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgreementOutput:
    boto3_raw_data: "type_defs.DescribeAgreementOutputTypeDef" = dataclasses.field()

    acceptanceTime = field("acceptanceTime")

    @cached_property
    def acceptor(self):  # pragma: no cover
        return Acceptor.make_one(self.boto3_raw_data["acceptor"])

    agreementId = field("agreementId")
    agreementType = field("agreementType")
    endTime = field("endTime")

    @cached_property
    def estimatedCharges(self):  # pragma: no cover
        return EstimatedCharges.make_one(self.boto3_raw_data["estimatedCharges"])

    @cached_property
    def proposalSummary(self):  # pragma: no cover
        return ProposalSummary.make_one(self.boto3_raw_data["proposalSummary"])

    @cached_property
    def proposer(self):  # pragma: no cover
        return Proposer.make_one(self.boto3_raw_data["proposer"])

    startTime = field("startTime")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgreementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgreementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptedTerm:
    boto3_raw_data: "type_defs.AcceptedTermTypeDef" = dataclasses.field()

    @cached_property
    def byolPricingTerm(self):  # pragma: no cover
        return ByolPricingTerm.make_one(self.boto3_raw_data["byolPricingTerm"])

    @cached_property
    def configurableUpfrontPricingTerm(self):  # pragma: no cover
        return ConfigurableUpfrontPricingTerm.make_one(
            self.boto3_raw_data["configurableUpfrontPricingTerm"]
        )

    @cached_property
    def fixedUpfrontPricingTerm(self):  # pragma: no cover
        return FixedUpfrontPricingTerm.make_one(
            self.boto3_raw_data["fixedUpfrontPricingTerm"]
        )

    @cached_property
    def freeTrialPricingTerm(self):  # pragma: no cover
        return FreeTrialPricingTerm.make_one(
            self.boto3_raw_data["freeTrialPricingTerm"]
        )

    @cached_property
    def legalTerm(self):  # pragma: no cover
        return LegalTerm.make_one(self.boto3_raw_data["legalTerm"])

    @cached_property
    def paymentScheduleTerm(self):  # pragma: no cover
        return PaymentScheduleTerm.make_one(self.boto3_raw_data["paymentScheduleTerm"])

    @cached_property
    def recurringPaymentTerm(self):  # pragma: no cover
        return RecurringPaymentTerm.make_one(
            self.boto3_raw_data["recurringPaymentTerm"]
        )

    @cached_property
    def renewalTerm(self):  # pragma: no cover
        return RenewalTerm.make_one(self.boto3_raw_data["renewalTerm"])

    @cached_property
    def supportTerm(self):  # pragma: no cover
        return SupportTerm.make_one(self.boto3_raw_data["supportTerm"])

    @cached_property
    def usageBasedPricingTerm(self):  # pragma: no cover
        return UsageBasedPricingTerm.make_one(
            self.boto3_raw_data["usageBasedPricingTerm"]
        )

    @cached_property
    def validityTerm(self):  # pragma: no cover
        return ValidityTerm.make_one(self.boto3_raw_data["validityTerm"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcceptedTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AcceptedTermTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAgreementsOutput:
    boto3_raw_data: "type_defs.SearchAgreementsOutputTypeDef" = dataclasses.field()

    @cached_property
    def agreementViewSummaries(self):  # pragma: no cover
        return AgreementViewSummary.make_many(
            self.boto3_raw_data["agreementViewSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchAgreementsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAgreementsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgreementTermsOutput:
    boto3_raw_data: "type_defs.GetAgreementTermsOutputTypeDef" = dataclasses.field()

    @cached_property
    def acceptedTerms(self):  # pragma: no cover
        return AcceptedTerm.make_many(self.boto3_raw_data["acceptedTerms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgreementTermsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgreementTermsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
